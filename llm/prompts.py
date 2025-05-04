# -*- coding: utf-8 -*-
from langchain.prompts import PromptTemplate

GRAMMAR_ANALYSIS_PROMPT = PromptTemplate(
    template="""
{format_instructions}
以下の日本語文法「{grammar}」について、次の情報を提供してください：
1. 文法名
2. 説明
3. 例文
4. 接続方法
5. 類似文法
6. メモ
出力は上記のJSON形式にしてください。
""",
    input_variables=["grammar"],
    partial_variables={"format_instructions": "{format_instructions}"},
)
