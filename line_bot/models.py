from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field

from linebot.v3.messaging import (
    ApiClient,
    Configuration,
    MessagingApi,
    TextMessage,
    ImageMessage,
    TemplateMessage,
    ButtonsTemplate,
    PostbackAction,
    URIAction
)


class UserProfile(BaseModel):
    """User profile data model"""
    user_id: str
    display_name: Optional[str] = None
    picture_url: Optional[str] = None
    status_message: Optional[str] = None


class ConversationTurn(BaseModel):
    """Single turn in a conversation"""
    user_message: str
    bot_response: str
    timestamp: Optional[str] = None


class ConversationHistory(BaseModel):
    """Conversation history data model"""
    user_id: str
    turns: List[ConversationTurn] = []
    metadata: Dict[str, Any] = Field(default_factory=dict)


class RichMenuConfig(BaseModel):
    """Rich menu configuration model"""
    name: str
    chat_bar_text: str
    size_full: bool = True
    selected: bool = False
    areas: List[Dict[str, Any]] = []


class MessageFactory:
    """Factory class for creating LINE v3 API messages"""

    @staticmethod
    def create_text_message(text: str) -> TextMessage:
        """Create a text message"""
        return TextMessage(text=text)

    @staticmethod
    def create_image_message(
        image_url: str,
        preview_url: Optional[str] = None
      ) -> ImageMessage:
        """Create an image message"""
        if not preview_url:
            preview_url = image_url
        return ImageMessage(
            original_content_url=image_url,
            preview_image_url=preview_url
        )

    @staticmethod
    def create_button_template(
        alt_text: str,
        title: str,
        text: str,
        thumbnail_url: Optional[str] = None,
        actions: Optional[List[Union[PostbackAction, URIAction]]] = None
    ) -> TemplateMessage:
        """Create a button template message"""
        if actions is None:
            actions = []

        template = ButtonsTemplate(
            title=title[:40],  # LINE's limitation
            text=text[:160],   # LINE's limitation
            thumbnail_image_url=thumbnail_url,
            actions=actions
        )

        return TemplateMessage(
            alt_text=alt_text,
            template=template
        )


class MessageHelper:
    """Helper class for sending messages using v3 API"""

    def __init__(self, channel_access_token: str):
        """Initialize with channel access token"""
        self.configuration = Configuration(
            access_token=channel_access_token
        )
        self.api_client = ApiClient(self.configuration)
        self.messaging_api = MessagingApi(self.api_client)

    def send_reply_message(
        self,
        reply_token: str,
        messages: List[Any]
      ) -> Dict[str, Any]:
        """Send reply message using v3 API"""
        response = self.messaging_api.reply_message(
            reply_token=reply_token,
            request_body={"messages": messages}
        )
        return response

    def send_push_message(
        self,
        user_id: str,
        messages: List[Any]
      ) -> Dict[str, Any]:
        """Send push message using v3 API"""
        response = self.messaging_api.push_message(
            request_body={
                "to": user_id,
                "messages": messages
            }
        )
        return response

    def get_profile(self, user_id: str) -> UserProfile:
        """Get user profile using v3 API"""
        profile = self.messaging_api.get_profile(user_id=user_id)

        return UserProfile(
            user_id=profile.user_id,
            display_name=profile.display_name,
            picture_url=profile.picture_url,
            status_message=profile.status_message
        )

    def close(self):
        """Close API client"""
        if self.api_client:
            self.api_client.close()
