# AI-Chatbot with LINE

自分用の日本語学習 ＆ AI 活用実験

## Table of Contents

1. [Setup & Usage](#setup--usage)
2. [Directory structure](#directory-structure)
3. [To do](#to-do)

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
│   └── grammar.py             # grammar api
├── scripts/                   # Scripts directory
│   ├── start.sh               # Service start script
│   ├── stop.sh                # Service stop script
│   ├── deploy.sh              # Deployment script
│   └── backup.sh              # Data backup script
├── config/                    # Configuration directory
│   ├── __init__.py
│   ├── settings.py            # Configuration settings
│   └── logging_config.py      # Logging configuration
├── line_bot/                  # LINE Bot related modules
│   ├── __init__.py
│   ├── client.py              # LINE API client
│   ├── handlers.py            # Message handlers
│   └── models.py              # LINE related data models
├── line_setting/              # LINE Bot API usage
│   ├── __init__.py
│   ├── line_api_test.py
│   └── upload_richmenu.py     # Upload LINE bot rich menu
├── llm/                       # LLM related modules
│   ├── __init__.py
│   ├── client.py              # LLM API client
│   ├── prompts.py             # Prompt templates
│   └── processor.py           # LLM response processor
├── services/                  # Business logic services
│   ├── __init__.py
│   ├── message_service.py     # Message processing service
│   └── conversation_service.py # Conversation management service
├── static/
│   └── images/
├── utils/                     # Utility functions
│   ├── __init__.py
│   ├── logger.py              # Logging tools
│   └── helpers.py             # General helper functions
├── data/                      # Data storage directory
│   ├── conversations/         # Conversation history
│   └── logs/                  # Log files
├── templates/
│   └── grammar_liff/          # grammar html
└── tests/                     # Test directory
    ├── __init__.py
    ├── test_line_bot.py
    └── test_llm.py
```

## To do

SQLAlchemy