import json
import redis
from typing import List, Dict
from config.settings import REDIS_HOST, REDIS_PORT, REDIS_DB, MAX_CONVERSATION_LENGTH
from utils.logger import setup_logger

logger = setup_logger()

# Initialize Redis client
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def get_conversation_history(user_id: str) -> List[Dict[str, str]]:
    """Get conversation history for a user"""
    try:
        conversation_key = f"conversation:{user_id}"
        if redis_client.exists(conversation_key):
            conversation_data = redis_client.get(conversation_key)
            return json.loads(conversation_data)
        return []
    except Exception as e:
        logger.error(f"Error getting conversation history: {e}")
        return []


def save_conversation(user_id: str, user_message: str, assistant_message: str):
    """Save conversation for a user"""
    try:
        conversation_key = f"conversation:{user_id}"

        # Get existing conversation
        conversation = get_conversation_history(user_id)

        # Add new turn
        conversation.append({"user": user_message, "assistant": assistant_message})

        # Limit conversation length
        if len(conversation) > MAX_CONVERSATION_LENGTH:
            conversation = conversation[-MAX_CONVERSATION_LENGTH:]

        # Save conversation
        redis_client.set(conversation_key, json.dumps(conversation))

        # Set expiration (7 days)
        redis_client.expire(conversation_key, 60 * 60 * 24 * 7)
    except Exception as e:
        logger.error(f"Error saving conversation: {e}")
