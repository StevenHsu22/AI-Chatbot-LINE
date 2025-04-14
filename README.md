# AI-Chatbot with LINE

## Table of Contents

1. [Setup & Usage](#Setup & Usage)
2. [Directory structure](#Directory structure)

## Setup & Usage

write github wiki 

```bash

```

## Directory structure

```

line-llm-bot/                  # Project root directory
├── .env                       # Environment variables configuration file
├── .env.example               # Example environment variables file
├── .gitignore                 # Git ignore file
├── requirements.txt           # Dependency package list
├── README.md                  # Project documentation
├── app.py                     # Main application entry point
├── Dockerfile                 # Docker build file
├── docker-compose.yml         # Docker Compose configuration file
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
├── llm/                       # LLM related modules
│   ├── __init__.py
│   ├── client.py              # LLM API client
│   ├── prompts.py             # Prompt templates
│   └── processor.py           # LLM response processor
├── services/                  # Business logic services
│   ├── __init__.py
│   ├── message_service.py     # Message processing service
│   └── conversation_service.py # Conversation management service
├── utils/                     # Utility functions
│   ├── __init__.py
│   ├── logger.py              # Logging tools
│   └── helpers.py             # General helper functions
├── data/                      # Data storage directory
│   ├── conversations/         # Conversation history
│   └── logs/                  # Log files
└── tests/                     # Test directory
    ├── __init__.py
    ├── test_line_bot.py
    └── test_llm.py
```
