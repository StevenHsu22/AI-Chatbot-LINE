# -*- coding: utf-8 -*-
# https://github.com/line/line-bot-sdk-python/blob/e49111f64fb6c436480d184b9e9f76df62f78602/examples/rich-menu/app.py#L146

import logging
# import os
# import sys

from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
)


# def add_project_root_to_sys_path():
#     current_path = os.path.dirname(__file__)
#     project_root = os.path.abspath(os.path.join(current_path, ".."))
#     if project_root not in sys.path:
#         sys.path.insert(0, project_root)


# add_project_root_to_sys_path()

from config.settings import LINE_CHANNEL_ACCESS_TOKEN  # noqa: E402

logging.basicConfig(level=logging.INFO)

configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)


def main():
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        # line_bot_blob_api = MessagingApiBlob(api_client)

        rich_menu_list = line_bot_api.get_rich_menu_list()
        logging.info(f"Rich menu list: {rich_menu_list}")

        # default_rich_menu_id = line_bot_api.get_default_rich_menu_id()
        # logging.info(f"Default rich menu ID: {default_rich_menu_id}")

        # rich_menu_alias_list = line_bot_api.get_rich_menu_alias_list()
        # logging.info(f"Rich menu alias list: {rich_menu_alias_list}")

        # line_bot_api.delete_rich_menu_alias("richmenu-alias-a")
        # logging.info("Rich menu alias deleted successfully.")

        # rich_menu_list = line_bot_api.get_rich_menu_list()
        # rich_menu_ids = [
        #   menu.rich_menu_id for menu in rich_menu_list.richmenus
        # ]
        # print(f"Rich menu IDs: {rich_menu_ids}")
        # for rich_menu_id in rich_menu_ids:
        #     line_bot_api.delete_rich_menu(rich_menu_id)
        #     logging.info(f"Rich menu {rich_menu_id} deleted successfully.")


main()
