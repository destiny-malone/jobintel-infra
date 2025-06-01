import os
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

sys.path.append(os.path.join(os.path.dirname(__file__), '../utils'))
from config_loader import load_config


# Load configuration
config = load_config()
slack_config = config.get('slack', {})
webhook_url = os.environ.get("SLACK_WEBHOOK_URL"), slack_config.get('webhook_url')

def send_slack_notification(message: str) -> bool:
    """
    Send a message to a Slack channel using a webhook URL from environment variables.

    Args:
        message (str): Formatted Slack message to send.

    Returns:
        Raise: True if response from the Slack API sent successfully, Raise Exception otherwise.
    """
    # client = WebClient(token=)
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    # Ensure webhool url is set
    if not webhook_url:
        raise ValueError("SLACK_WEBHOOK_URL not set in environment.")

    headers = {'Content-Type': 'application/json'}
    payload = {
        'text': message,
        'username': 'Terraform Bot',
        'icon_emoji': ':terraform:',
        'mrkdwn': True
    }

    # Send the POST request to the Slack webhook URL
    # This will send the message to the specified Slack channel
    try:
        response = requests.post(webhook_url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")

def format_slack_message(resources, branch, actor, duration, status="success"):
    """
    Format the resources and job details into a Slack message.
    Args:
        resources (dict): Dictionary containing resources to be created, updated, or deleted.
        branch (str): Branch name where the job was run.
        actor (str): Actor who triggered the job.
        duration (str): Duration of the job in seconds.
        status (str): Status of the job, default is "success".

    Returns:
        str: Formatted Slack message.
    """
    # Format the status with an emoji
    emoji = {
        'success': ':white_check_mark:',
        'failure': ':x:',
        'in_progress': ':hourglass_flowing_sand:',
    }
    status_str = f"{emoji.get(status, ':question:')} {status.capitalize()}


    # Format the message
    message = "```"
    message += f"*Terraform Plan Notification*\n\n"
    message += f"*Branch:* `{branch}`\n"
    message += f"*Triggered By:* `{actor}`\n"
    message += f"*Status:* `{status_str}`\n"
    message += f"*Duration:* `{duration}`\n\n"

    for action in ['create', 'update', 'delete']:
        if resources.get(action):
            # Use emojis for each action
            emoji = {
                'create': ':heavy_plus_sign:',
                'update': ':arrows_counterclockwise:',
                'delete': ':heavy_minus_sign:'
            }[action]
            message += f"{emoji} *{action.capitalize()} ({len(resources[action])}):*\n"
            for resource in resources[action]:
                message += f"- `{resource}`\n"
        else:
            message += f"*No resources to {action}.*\n"
    message += "\n*End of Terraform Plan*\n"
    message += "```"
    return message.strip()
