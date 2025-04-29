from fastapi import APIRouter
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
    save_grammar_to_notion(data)  # 實作寫在 services 中
    return {"message": "Success"}
