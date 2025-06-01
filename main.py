from parser.parse_tfplan import parse_tfplan, calculate_duration
import json
from utils.logger import setup_logger
import os
from datetime import datetime
from slack.notifier import send_slack_notification, format_slack_message
from utils.config_loader import load_config


logger = setup_logger(__name__)
logger.info("Starting Terraform plan parser...")
# Load configuration
config = load_config()
TFPLAN_PATH = config.get('terraform', {}).get('tfplan_path', 'tfplan.json')
region = config.get('aws', {}).get('region', 'us-west-2')

def main():
    """
    Main function to execute the Terraform plan parsing and Slack notification.
    """
    try:
        # Parse the Terraform plan
        resources = parse_tfplan(TFPLAN_PATH)
        logger.info(f"Parsed resources: {resources}")

        # Get branch, actor, and duration from environment variables or defaults
        branch = os.environ.get('GITHUB_REF', 'dev').split('/')[-1]
        actor = os.environ.get('GITHUB_ACTOR', 'local-developer')
        logger.info(f"Branch: {branch}, Actor: {actor}")
        begin_time = os.getenv('START_TIME', datetime.now().isoformat())
        start_time = datetime.fromisoformat(begin_time) if start_time else datetime.now()
        conclude_time = os.getenv('END_TIME', datetime.now().isoformat())
        end_time = datetime.fromisoformat(conclude_time) if end_time else datetime.now()
        duration = calculate_duration(start_time, end_time)

        # Format the Slack message
        status = "Success" if resources else "No changes"
        message = format_slack_message(resources, branch, actor, duration, status)

        # Send the Slack notification
        if config.get('slack', {}).get('enabled', False):
            send_slack_notification(message)
            logger.info("Slack notification sent successfully.")
        else:
            logger.info("Slack notifications are disabled in the configuration.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
    logger.info("Terraform plan parser completed successfully.")