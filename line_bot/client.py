from linebot.v3 import WebhookHandler
from linebot.v3.messaging import (
    AsyncApiClient,
    ApiClient,
    Configuration,
)

from config.settings import (  # noqa: E402
  LINE_CHANNEL_ACCESS_TOKEN,
  LINE_CHANNEL_SECRET
)

# Initialize LINE Bot API client
configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

async_api_client = AsyncApiClient(configuration)
sync_api_client = ApiClient(configuration)
