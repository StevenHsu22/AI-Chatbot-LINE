from fastapi import APIRouter, Request
from pydantic import BaseModel
from services.grammar_service import save_grammar_to_notion

router = APIRouter(prefix="/api")


class GrammarInput(BaseModel):
    title: str
    description: str
    example: str
    synonyms: str
    memo: str


@router.post("/grammar")
async def submit_grammar(data: GrammarInput):
    save_grammar_to_notion(data)
    return {"message": "Success"}


@router.post("/grammar/generate")
async def generate_grammar(request: Request):
    body = await request.json()
    keyword = body.get("keyword")

    return {
        "title": keyword,
        "description": f"{keyword}の使い方を説明するテキスト",
        "example": f"彼は毎日{keyword}。",
        "synonyms": "〜最中, 〜間",
        "memo": "自動生成されたデータです",
    }
