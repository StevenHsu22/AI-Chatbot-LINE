from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from llm.processor import GrammarProcessor
from api.models import GrammarOutput
from services.grammar_service import save_grammar_to_notion

router = APIRouter()
grammar_processor = GrammarProcessor()


class GrammarRequest(BaseModel):
    grammar: str


@router.post("/generate_grammar", response_model=GrammarOutput)
async def generate_grammar(request: GrammarRequest):
    body = request.model_dump()
    grammar = body.get("grammar")
    result = grammar_processor.analyze_grammar(grammar)

    if not result:
        raise HTTPException(
            status_code=500,
            detail="Failed to analyze grammar"
        )

    return result
    # return {
    #         "title": grammar,
    #         "description": f"{grammar}の使い方を説明するテキスト",
    #         "example": f"彼は毎日{grammar}。",
    #         "connection": f"彼は毎日{grammar}。",
    #         "synonyms": "〜最中, 〜間",
    #         "memo": "自動生成されたデータです",
    #     }


@router.post("/save_grammar")
async def save_grammar(data: GrammarOutput):
    await save_grammar_to_notion(data)
    return {"message": "Success"}
