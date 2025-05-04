# -*- coding: utf-8 -*-
# https://developers.notion.com/docs/create-a-notion-integration
# https://qiita.com/Yusuke_Pipipi/items/b44cb8442932019c52c9

import logging
# import os
# import sys

from notion_client import Client


# def add_project_root_to_sys_path():
#     current_path = os.path.dirname(__file__)
#     project_root = os.path.abspath(os.path.join(current_path, ".."))
#     if project_root not in sys.path:
#         sys.path.insert(0, project_root)


# add_project_root_to_sys_path()

from config.settings import NOTION_API_KEY, NOTION_DATABASE_ID  # noqa: E402

logging.basicConfig(level=logging.INFO)


def main():

    notion_database_id = NOTION_DATABASE_ID

    with Client(auth=NOTION_API_KEY) as api_client:

        def get_all_notion_users():
            response = api_client.users.list()
            logging.info("get all notion users")
            logging.info(response)
            return response

        def read_notion_database(database_id):
            response = api_client.databases.query(
                **{
                    "database_id": database_id,
                }
            )
            logging.info("read notion database")
            logging.info(response)
            return response

        # def read_notion_database(database_id):
        #     response = api_client.databases.query(
        #         **{
        #             "database_id": database_id,
        #             "filter": {
        #               "property": "Status",
        #               "status": {
        #                 "equals": "Done"
        #               }
        #             },
        #         }
        #     )

        #     return response

        def read_pages_from_database(database_id):
            response = api_client.databases.query(
                **{
                    "database_id": database_id,
                }
            )

            results = response["results"]
            page_ids = []
            for result in results:
                # print(f'page_id={result["id"]}')
                page_ids.append(result["id"])

            logging.info(
              f"read_pages_from_database completed. (len={len(page_ids)})"
            )
            return page_ids

        def add_row_to_notion_database(database_id):
            response = api_client.pages.create(
                **{
                    "parent": {"database_id": database_id},
                    "properties": {
                      "文法": {
                        "title": [
                          {
                            "text": {
                              "content": "test"
                            }
                          }
                        ]
                      },
                      "説明": {
                        "rich_text": [
                          {
                            "text": {
                              "content": "test"
                            }
                          }
                        ]
                      },
                      "例文": {
                        "rich_text": [
                          {
                            "text": {
                              "content": "test"
                            }
                          }
                        ]
                      },
                      "接続方法": {
                        "rich_text": [
                          {
                            "text": {
                              "content": "test"
                            }
                          }
                        ]
                      },
                      "類似文法": {
                        "rich_text": [
                          {
                            "text": {
                              "content": "test"
                            }
                          }
                        ]
                      },
                      "メモ": {
                        "rich_text": [
                          {
                            "text": {
                              "content": "test"
                            }
                          }
                        ]
                      },
                      "完了": {
                        "checkbox": False
                      }
                    },
                    # ページ内にコンテンツを追加する場合はchildrenを指定する
                    # "children": [
                    #     # toc block
                    #     {
                    #         "object": "block",
                    #         "type": "table_of_contents",
                    #         "table_of_contents": {},
                    #     },
                    #     # heading 1
                    #     {
                    #         "object": "block",
                    #         "type": "heading_1",
                    #         "heading_1": {
                    #             "rich_text": [
                    #               {"text": {"content": "Heading 1"}}
                    #             ],
                    #         },
                    #     },
                    #     # heading 2
                    #     {
                    #         "object": "block",
                    #         "type": "heading_2",
                    #         "heading_2": {
                    #             "rich_text": [
                    #               {"text": {"content": "Heading 2"}}
                    #             ],
                    #         },
                    #     },
                    #     # heading 3
                    #     {
                    #         "object": "block",
                    #         "type": "heading_3",
                    #         "heading_3": {
                    #             "rich_text": [
                    #               {"text": {"content": "Heading 3"}}
                    #             ],
                    #         },
                    #     },
                    #     # link
                    #     {
                    #         "object": "block",
                    #         "paragraph": {
                    #             "rich_text": [
                    #                 {
                    #                     "text": {
                    #                         "content": "test",
                    #                         "link": {
                    #                           "url": "test"
                    #                         },
                    #                     },
                    #                     "href": "test",
                    #                 }
                    #             ],
                    #             "color": "blue",
                    #         },
                    #     },
                    #     # code block python
                    #     {
                    #         "object": "block",
                    #         "type": "code",
                    #         "code": {
                    #             "caption": [],
                    #             "rich_text": [
                    #                 {
                    #                     "type": "text",
                    #                     "text": {
                    #                         "content": "x = aaa\nprint(x)",
                    #                         "link": None,
                    #                     },
                    #                 }
                    #             ],
                    #             "language": "python",
                    #         },
                    #     },
                    # ],
                }
            )

            logging.info("notion database create completed")
            logging.info(response)

        def get_page_content(page_id):
            response = api_client.blocks.children.list(
                **{"block_id": page_id, "page_size": 50}
            )
            logging.info("get page content completed")
            logging.info(response)
            return response

        def get_page_title(page_id):
            response = api_client.pages.retrieve(
                **{"page_id": page_id, "properties": ["Title"]}
            )
            page_title = response["properties"]["Title"]["title"][0][
                "plain_text"
            ]
            logging.info("get page title completed")
            logging.info(page_title)
            return page_title

        def get_page_status_property(page_id):
            response = api_client.pages.retrieve(
                **{"page_id": page_id, "properties": ["Status"]}
            )
            page_status = response["properties"]["Status"]["status"]["name"]
            logging.info("get page status property completed")
            logging.info(page_status)
            return page_status

        def get_page_email_property(page_id):
            response = api_client.pages.retrieve(
                **{"page_id": page_id, "properties": ["Email"]}
            )
            page_email = response["properties"]["Email"]["email"]
            logging.info("get page email property completed")
            logging.info(page_email)
            return page_email

        # get_all_notion_users()
        # read_notion_database(notion_database_id)
        # read_pages_from_database(notion_database_id)
        add_row_to_notion_database(notion_database_id)


main()
