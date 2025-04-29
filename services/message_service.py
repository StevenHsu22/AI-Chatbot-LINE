from line_bot.client import line_bot_api
from line_bot.handlers import handle_text_message
from utils.logger import setup_logger

logger = setup_logger()


async def process_message_event(event):
    """Process message event from LINE"""
    try:
        # For now, we only handle text messages
        # You can extend this to handle other message types
        if event.type == "message" and event.message.type == "text":
            handle_text_message(event)
        else:
            logger.info(f"Unhandled event type: {event.type}")
    except Exception as e:
        logger.error(f"Error processing message event: {e}")
