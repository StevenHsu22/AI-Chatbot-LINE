# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field

class GrammarOutput(BaseModel):
    """日本語文法解析用のモデル"""
    title: str = Field(description="文法名")
    description: str = Field(description="文法の説明")
    example: str = Field(description="例文（一つ例）")
    connection: str = Field(
      description='''接続方法（例：「名詞 + っぽい」、\
      「動詞のます形 + っぽい」、「い形容詞の語幹 + っぽい」など）'''
    )
    synonyms: str = Field(description="類似文法（例：〜みたい, 〜らしい）")
    memo: str = Field(description="メモ")