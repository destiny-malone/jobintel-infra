import os
import sys
import json
import requests

# Constants
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '../utils'))
from config_loader import load_config
sys.path.append(os.path.join(os.path.dirname(__file__), '../slack'))
from notifier import send_slack_notification, format_slack_message


# This script parses a Terraform plan file and sends a formatted message to a Slack channel.



# Load configuration
config = load_config()

# Access configuration values
TFPLAN_PATH = config.get('terraform', {}).get('tfplan_path', 'tfplan.json')
region = config.get('aws', {}).get('region', 'us-west-2')
slack_enabled = config.get('slack', {}).get('enabled', False)



def parse_tfplan(path=TFPLAN_PATH):
    """
    Parse a Terraform plan file and return the resources to be created, updated, or deleted.
    This function reads a Terraform plan file in JSON format and extracts the resources that are
    scheduled for creation, update, or deletion. It returns a dictionary with three keys:
    Args:
        path (str): Path to the Terraform plan file in JSON format.
        'create', 'update', and 'delete', each containing a list of resource identifiers.
    Raises:
        RuntimeError: If the file cannot be read or parsed.
        ValueError: If the file format is invalid or no resource changes are found.
    Returns:
        dict: A dictionary containing resources to be created, updated, or deleted.
    """
    try:
        with open(path, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error reading or parsing the Terraform plan file: {e}")
    if not data or 'resource_changes' not in data:
        raise ValueError("Invalid Terraform plan file format or no resource changes found.")

    resources = {
        'create': [],
        'update': [],
        'delete': []}

    for resource in data.get('resource_changes', []):
        for action in resource.get('change', {}).get('actions', []):
            resource_type = resource['type']
            resource_name = resource['name']
            resource_id = resource.get('change', {}).get('before', {}).get('id', 'unknown')

            if action == 'create':
                resources['create'].append(f"{resource_type}.{resource_name} (ID: {resource_id})")
            elif action == 'update':
                resources['update'].append(f"{resource_type}.{resource_name} (ID: {resource_id})")
            elif action == 'delete':
                resources['delete'].append(f"{resource_type}.{resource_name} (ID: {resource_id})")

    return resources

def calculate_duration(start_time, end_time):
    """
    Calculate the duration between two datetime strings.

    This function assumes the input times are in ISO 8601 format (e.g., "2023-10-01T12:00:00Z").
    It returns the duration in seconds as a string.
    If the input times are not in the correct format, it raises a ValueError.
    Args:
        start_time (str): Start time in ISO 8601 format.
        end_time (str): End time in ISO 8601 format.
    Raises:
        ValueError: If the input datetime strings are not in the correct format.
    Returns:
        str: Duration in seconds.
    """
    try:
        start_dt = datetime.fromisoformat(start_time) # Ensure 'Z' is treated as UTC
        end_dt = datetime.fromisoformat(end_time) # Ensure 'Z' is treated as UTC
        duration = end_dt - start_dt
        return str(duration.total_seconds()) + 's'
    except ValueError as e:
        raise ValueError(f"Invalid datetime format: {e}")

format_slack_message = format_slack_message
send_slack_notification = send_slack_notification

def main():
    print("Starting Terraform Plan Parser...")
    START_TIME = os.environ.get('START_TIME', datetime.now().isoformat())
    END_TIME = os.environ.get('END_TIME', datetime.now().isoformat())
    BRANCH = os.environ.get('BRANCH', 'main')
    ACTOR = os.environ.get('ACTOR', 'destiny')
    STATUS = os.environ.get('STATUS', 'success')
    print(f"Parsing Terraform plan from {TFPLAN_PATH}...")


    resources = parse_tfplan()
    duration = calculate_duration(START_TIME, END_TIME)
    slack_message = format_slack_message(
        resources,
        branch=BRANCH,
        actor=ACTOR,
        duration=duration,
        status=STATUS
    )
    success = send_slack_notification(slack_message)
    if success:
        print("Slack alert sent successfully.")
    else:
        print("Failed to send Slack alert.")

if __name__ == "__main__":
    main()
# This script parses a Terraform plan file and sends a formatted message to a Slack channel.
