# import django settings
import datetime
from django.conf import settings

# import slack web client
from slack import WebClient

# import modules and function from menu
from modules.menu.functions import build_menu_url
from modules.menu.models import Menu


def send_menu_slack_notification() -> None:
    """
    Send a notification to Slack when a new menu is available.
    """

    menu_day = Menu.objects.filter(menu_date=datetime.date.today()).first()
    if menu_day:
        message = build_message_slack(menu_day)
        send_slack_notification(message)

    else:
        message = [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "No menu for today"},
            },
        ]
        send_slack_notification(message)


def build_message_slack(menu_day: object) -> list:
    """
    Build the message to be sent to Slack.
    """
    return [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "Menu Day is: " + str(menu_day.name)},
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*Today's menu is available at * "
                    + build_menu_url(menu_day.id),
                },
                {"type": "mrkdwn", "text": "*Have a nice day!*"},
            ],
        },
    ]


def send_slack_notification(message: object) -> None:
    """
    Send a notification to Slack.
    """
    slack_token = settings.SLACK_TOKEN
    sc = WebClient(token=slack_token)
    sc.chat_postMessage(channel=settings.SLACK_CHANNEL, blocks=message)
