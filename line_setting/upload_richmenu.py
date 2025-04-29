# -*- coding: utf-8 -*-
# https://github.com/line/line-bot-sdk-python/blob/e49111f64fb6c436480d184b9e9f76df62f78602/examples/rich-menu/app.py#L146

import logging
import os
import sys

from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessageAction,
    MessagingApi,
    MessagingApiBlob,
    RichMenuRequest,
    RichMenuArea,
    RichMenuSize,
    RichMenuBounds,
    URIAction,
    RichMenuSwitchAction,
    CreateRichMenuAliasRequest,
)


def add_project_root_to_sys_path():
    current_path = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(current_path, ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)


add_project_root_to_sys_path()

from config.settings import LINE_CHANNEL_ACCESS_TOKEN  # noqa: E402

logging.basicConfig(level=logging.INFO)

configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)


def rich_menu_object_a_json():
    return {
        "size": {"width": 800, "height": 540},
        "selected": True,
        "name": "メニュー",
        "chatBarText": "Tap to open",
        "areas": [
            # 1. 単語
            {
                "bounds": {"x": 0, "y": 0, "width": 266, "height": 270},
                "action": {"type": "uri", "uri": "https://jpdb.io/"},
            },
            # 2. 文法
            {
                "bounds": {"x": 266, "y": 0, "width": 266, "height": 270},
                "action": {"type": "message", "text": "文法を保存"},
            },
            # 3. 画像
            {
                "bounds": {"x": 532, "y": 0, "width": 266, "height": 270},
                "action": {"type": "message", "text": "画像を生成"},
            },
            # 4. PDF Reading
            {
                "bounds": {"x": 0, "y": 270, "width": 266, "height": 270},
                "action": {"type": "message", "text": "PDFを読みたい"},
            },
            # 5. 他の
            # {
            #     "bounds": {"x": 532, "y": 270, "width": 266, "height": 270},
            #     "action": {
            #         "type": "richmenuswitch",
            #         "richMenuAliasId": "richmenu-alias-b",
            #         "data": "richmenu-changed-to-b",
            #     },
            # },
            # 6. AI chat 履歴をクリア
            {
                "bounds": {"x": 532, "y": 270, "width": 266, "height": 270},
                "action": {"type": "message", "text": "履歴をクリア"},
            },
        ],
    }


def rich_menu_object_b_json():
    return {
        "size": {"width": 2500, "height": 1686},
        "selected": False,
        "name": "richmenu-b",
        "chatBarText": "Tap to open",
        "areas": [
            {
                "bounds": {"x": 0, "y": 0, "width": 1250, "height": 1686},
                "action": {
                    "type": "richmenuswitch",
                    "richMenuAliasId": "richmenu-alias-a",
                    "data": "richmenu-changed-to-a",
                },
            },
        ],
    }


# def create_action(action):
#     if action["type"] == "uri":
#         return URIAction(uri=action.get("uri"))
#     else:
#         return RichMenuSwitchAction(
#             rich_menu_alias_id=action.get("richMenuAliasId"),
#             data=action.get("data")
#         )

def create_action(action_dict):
    action_type = action_dict.get("type")
    if action_type == "uri":
        return URIAction(uri=action_dict["uri"])
    elif action_type == "message":
        return MessageAction(text=action_dict["text"])
    elif action_type == "richmenuswitch":
        return RichMenuSwitchAction(
            data=action_dict["data"],
            rich_menu_alias_id=action_dict["richMenuAliasId"],
        )
    else:
        raise ValueError(f"Unsupported action type: {action_type}")


def main():
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_blob_api = MessagingApiBlob(api_client)

        # 1. Delete all rich menus & alias
        try:
            default_rich_menu_id = line_bot_api.get_default_rich_menu_id()
            line_bot_api.delete_rich_menu(default_rich_menu_id)
            logging.info("Default rich menu deleted successfully.")
        except Exception as e:
            logging.error(
                f"An error occurred while deleting the default rich menu: {e}"
            )

        try:
            line_bot_api.delete_rich_menu_alias("richmenu-alias-a")
            logging.info("Rich menu alias deleted successfully.")
        except Exception as e:
            logging.error(
                f"An error occurred while deleting the rich menu alias: {e}"
            )

        try:
            rich_menu_list = line_bot_api.get_rich_menu_list()
            rich_menu_ids = [
                menu.rich_menu_id for menu in rich_menu_list.richmenus
            ]
            for rich_menu_id in rich_menu_ids:
                line_bot_api.delete_rich_menu(rich_menu_id)
            logging.info("Rich menu deleted successfully.")
        except Exception as e:
            logging.error(
                f"An error occurred while deleting the rich menu: {e}"
            )

        # 2. Create rich menu A (richmenu-a)
        rich_menu_object_a = rich_menu_object_a_json()
        areas = [
            RichMenuArea(
                bounds=RichMenuBounds(
                    x=info["bounds"]["x"],
                    y=info["bounds"]["y"],
                    width=info["bounds"]["width"],
                    height=info["bounds"]["height"],
                ),
                action=create_action(info["action"]),
            )
            for info in rich_menu_object_a["areas"]
        ]

        rich_menu_to_a_create = RichMenuRequest(
            size=RichMenuSize(
                width=rich_menu_object_a["size"]["width"],
                height=rich_menu_object_a["size"]["height"],
            ),
            selected=rich_menu_object_a["selected"],
            name=rich_menu_object_a["name"],
            chat_bar_text=rich_menu_object_a["chatBarText"],
            areas=areas,
        )

        rich_menu_a_id = line_bot_api.create_rich_menu(
            rich_menu_request=rich_menu_to_a_create
        ).rich_menu_id

        # 3. Upload image to rich menu A
        with open("./static/images/richmenu-a.png", "rb") as image:
            line_bot_blob_api.set_rich_menu_image(
                rich_menu_id=rich_menu_a_id,
                body=bytearray(image.read()),
                _headers={"Content-Type": "image/png"},
            )

        # 4. Create rich menu B (richmenu-b)
        # rich_menu_object_b = rich_menu_object_b_json()
        # areas = [
        #     RichMenuArea(
        #         bounds=RichMenuBounds(
        #             x=info["bounds"]["x"],
        #             y=info["bounds"]["y"],
        #             width=info["bounds"]["width"],
        #             height=info["bounds"]["height"],
        #         ),
        #         action=create_action(info["action"]),
        #     )
        #     for info in rich_menu_object_b["areas"]
        # ]

        # rich_menu_to_b_create = RichMenuRequest(
        #     size=RichMenuSize(
        #         width=rich_menu_object_b["size"]["width"],
        #         height=rich_menu_object_b["size"]["height"],
        #     ),
        #     selected=rich_menu_object_b["selected"],
        #     name=rich_menu_object_b["name"],
        #     chat_bar_text=rich_menu_object_b["name"],
        #     areas=areas,
        # )

        # rich_menu_b_id = line_bot_api.create_rich_menu(
        #     rich_menu_request=rich_menu_to_b_create
        # ).rich_menu_id

        # # 5. Upload image to rich menu B
        # with open("./static/images/richmenu.png", "rb") as image:
        #     line_bot_blob_api.set_rich_menu_image(
        #         rich_menu_id=rich_menu_b_id,
        #         body=bytearray(image.read()),
        #         _headers={"Content-Type": "image/png"},
        #     )

        # 6. Set rich menu A as the default rich menu
        line_bot_api.set_default_rich_menu(rich_menu_id=rich_menu_a_id)

        # 7. Create rich menu alias A
        alias_a = CreateRichMenuAliasRequest(
            rich_menu_alias_id="richmenu-alias-a", rich_menu_id=rich_menu_a_id
        )
        line_bot_api.create_rich_menu_alias(alias_a)

        # 8. Create rich menu alias B
        # alias_b = CreateRichMenuAliasRequest(
        #     rich_menu_alias_id="richmenu-alias-b",
        #     rich_menu_id=rich_menu_b_id
        # )
        # line_bot_api.create_rich_menu_alias(alias_b)
        logging.info("success")


main()
