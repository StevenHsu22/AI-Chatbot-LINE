import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LINE Bot Configuration
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
if LINE_CHANNEL_ACCESS_TOKEN is None:
    sys.stderr.write(
      "Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.\n"
    )
    sys.exit(1)
if LINE_CHANNEL_SECRET is None:
    sys.stderr.write(
      "Specify LINE_CHANNEL_SECRET as environment variable.\n"
    )
    sys.exit(1)

# Notion Configuration
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
if NOTION_API_KEY is None:
    sys.stderr.write(
      "Specify NOTION_API_KEY as environment variable.\n"
    )
    sys.exit(1)
if NOTION_DATABASE_ID is None:
    sys.stderr.write(
      "Specify NOTION_DATABASE_ID as environment variable.\n"
    )
    sys.exit(1)

# LLM Configuration
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_BASE_URL = os.getenv("LLM_API_BASE_URL")

# Base URL for the application
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

# AWS Configuration
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "ap-northeast-1")

# Redis Configuration
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))

# Application Settings
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
PORT = int(os.getenv("PORT", "8000"))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Conversation Settings
MAX_CONVERSATION_LENGTH = int(os.getenv("MAX_CONVERSATION_LENGTH", "10"))
