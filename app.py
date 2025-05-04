from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from api.grammar import router as grammar_router

app = FastAPI(
  title="LINE LLM Bot",
  description="A LINE Bot integrated with LLM"
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(grammar_router, prefix="/api/grammar", tags=["Grammar"])


@app.get("/liff/grammar", response_class=HTMLResponse)
async def serve_grammar_liff(request: Request):
    return templates.TemplateResponse(
      "grammar_liff/index.html",
      {"request": request}
    )


if __name__ == "__main__":
    print("Running app.py directly... using uvicorn with reload=True")
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
