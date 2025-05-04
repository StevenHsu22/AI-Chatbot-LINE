from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    # ImageMessage,
    # AudioMessage,
    # VideoMessage,
)
from line_bot.client import handler, line_bot_api
from llm.client import get_llm_response
from services.conversation_service import (
    get_conversation_history,
    save_conversation
)
from utils.logger import setup_logger

logger = setup_logger()


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    """Handle text message from LINE"""
    try:
        user_id = event.source.user_id
        message_text = event.message.text

        # Get conversation history
        conversation_history = get_conversation_history(user_id)

        # Get response from LLM
        response = get_llm_response(message_text, conversation_history)

        # Save conversation
        save_conversation(user_id, message_text, response)

        # Reply to user
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=response)
        )
    except Exception as e:
        logger.error(f"Error handling text message: {e}")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="Sorry, something went wrong. Please try again later."
            ),
        )
