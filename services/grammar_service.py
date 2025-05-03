# -*- coding: utf-8 -*-

import logging
import os
import sys
from typing import Any

from notion_client import Client


def add_project_root_to_sys_path():
    current_path = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(current_path, ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)


add_project_root_to_sys_path()

from config.settings import NOTION_API_KEY, NOTION_DATABASE_ID  # noqa: E402

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

notion_database_id = NOTION_DATABASE_ID


def save_grammar_to_notion(data: Any) -> None:
    """
    Save grammar data to Notion database.
    """

    logging.info("Start to save grammar to Notion:", data.dict())

    try:
        with Client(auth=NOTION_API_KEY) as api_client:
            api_client.pages.create(
                parent={"database_id": notion_database_id},
                properties={
                    "文法": {
                        "title": [{"text": {"content": data.title}}]
                    },
                    "説明": {
                        "rich_text": [{"text": {"content": data.description}}]
                    },
                    "例文": {
                        "rich_text": [{"text": {"content": data.example}}]
                    },
                    "類似文法": {
                        "rich_text": [{"text": {"content": data.synonyms}}]
                    },
                    "メモ": {
                        "rich_text": [{"text": {"content": data.memo}}]
                    },
                    "完了": {"checkbox": False},
                },
            )
        logging.info("✅ Grammar successfully saved to Notion.")

    except Exception as e:
        logging.error(f"❌ Failed to save grammar to Notion: {str(e)}")
