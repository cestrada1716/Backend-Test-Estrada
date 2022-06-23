# import celery configs
from celery import shared_task
from celery.utils.log import get_task_logger

# import  function from notification module
from .functions import send_menu_slack_notification

logger = get_task_logger(__name__)


@shared_task
def slack_menu_day_notification():
    logger.info("Sending slack notification")
    send_menu_slack_notification()
