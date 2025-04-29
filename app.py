# Standard Library
import uvicorn

# Third-Party Libraries
from fastapi import FastAPI, Request, HTTPException, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

# Local Libraries
from config.settings import (
    LINE_CHANNEL_SECRET,
    LINE_CHANNEL_ACCESS_TOKEN,
    DEBUG,
    PORT,
    WEBHOOK_URL,
)
from line_bot.client import line_bot_api, handler
from services.message_service import process_message_event
from utils.logger import setup_logger


# Setup logger
logger = setup_logger()

app = FastAPI(title="LINE LLM Bot", description="A LINE Bot integrated with LLM")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "LINE LLM Bot is running"}


@app.post("/webhook")
async def webhook(request: Request, background_tasks: BackgroundTasks):
    """LINE Bot webhook endpoint"""
    signature = request.headers.get("X-Line-Signature", "")
    body = await request.body()
    body_str = body.decode("utf-8")

    try:
        # Validate signature
        handler.handle_body(body_str, signature)

        # Process events in background to avoid LINE API timeout
        background_tasks.add_task(process_webhook_events, body_str)

        return {"status": "ok"}
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        raise HTTPException(status_code=400, detail=str(e))


async def process_webhook_events(body_str: str):
    """Process LINE webhook events in background"""
    try:
        events = handler.parse_events_from_body(body_str)
        for event in events:
            await process_message_event(event)
    except Exception as e:
        logger.error(f"Error processing events: {e}")


if __name__ == "__main__":
    logger.info(f"Starting LINE LLM Bot on port {PORT}")
    uvicorn.run("app:app", host="0.0.0.0", port=PORT, reload=DEBUG)
