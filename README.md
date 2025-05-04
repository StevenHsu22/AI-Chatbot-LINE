# AI-Chatbot with LINE

自分用の日本語学習 ＆ AI 活用実験

## Table of Contents

1. [Feature](#feature)
2. [Setup & Usage](#setup--usage)
3. [Directory structure](#directory-structure)
4. [To do](#to-do)

## Feature

* 📚 **Japanese Grammar Learning Support**

Users can send grammar entries via LINE. The system uses LLMs (e.g., Gemini, GPT, Ollama) to analyze, classify, and save them to Notion for personalized grammar notes.

* 🗂️ **Notion Integration**

Automatically stores learning records and grammar entries into a Notion database, creating a personalized study log.

* 🖼️ **Image Generation (Experimental)**

Users can send prompts to generate images using models like Grok—exploring creative language learning through visuals.

* 📄 **PDF Reading (Experimental)**

Supports uploading and parsing PDF documents as potential reading practice material using vector search (FAISS).

## Setup & Usage

Visit the wiki for [Setup](https://github.com/StevenHsu22/AI-Chatbot-LINE/wiki)

## Directory structure

```

AI-Chatbot-LINE/               # Project root directory
├── .env                       # Environment variables configuration file
├── .env.example               # Example environment variables file
├── .gitignore                 # Git ignore file
├── requirements.txt           # Dependency package list
├── README.md                  # Project documentation
├── app.py                     # Main application entry point
├── Dockerfile                 # Docker build file
├── docker-compose.yml         # Docker Compose configuration file
├── api/
│   ├── __init__.py
│   ├── models.py              # pydantic type for api
│   └── grammar.py             # grammar api
├── config/                    # Configuration directory
│   ├── __init__.py
│   ├── settings.py            # Configuration settings
│   └── logging_config.py      # Logging configuration
├── data/                      # Data storage directory
│   ├── conversations/         # Conversation history
│   └── logs/                  # Log files
├── line_bot/                  # LINE Bot related modules
│   ├── __init__.py
│   ├── client.py              # LINE API client
│   ├── handlers.py            # Message handlers
│   └── models.py              # LINE related data models
├── line_setting/              # LINE Bot API usage
│   ├── __init__.py
│   └── upload_richmenu.py     # Upload LINE bot rich menu
├── llm/                       # LLM related modules
│   ├── __init__.py
│   ├── client.py              # LLM API client
│   ├── prompts.py             # Prompt templates
│   └── processor.py           # LLM response processor
├── scripts/                   # Scripts directory
│   ├── deploy.sh              # Scripts for Dockerfile
│   ├── start_local_docker.sh  # Scripts for local Docker Compose
│   ├── start_local.sh         # Scripts for local python test
│   └── stop_local_docker.sh   
├── services/                  # Business logic services
│   ├── __init__.py
│   ├── document_processing/
│   ├── image_processing/
│   ├── grammar_service.py     # Grammar related service (save to notion,...)
│   ├── message_service.py     # Message processing service
│   └── conversation_service.py # Conversation management service
├── static/
│   ├── icon/
│   └── images/
├── templates/
│   └── grammar_liff/          # grammar html
└── tests/                     # Test directory
│   ├── __init__.py
│   ├── line_api_test.py
│   ├── notion_api_test.py
│   ├── test_line_bot.py
│   └── test_llm.py
├── utils/                     # Utility functions
    ├── __init__.py
    ├── logger.py              # Logging tools
    └── helpers.py             # General helper functions

```

## To do

0. parse LINE message
1. connect with db (SQLAlchemy)
2. image generate (grok)
3. pdf reading (faiss)
