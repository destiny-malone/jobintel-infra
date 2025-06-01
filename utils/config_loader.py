import os
import yaml
# from dotenv import load_dotenv


def load_config(config_path="config/config.yaml"):
    """
    Load configuration from a YAML file and environment variables.
    
    Args:
        config_path (str): Path to the YAML configuration file.
        
    Returns:
        dict: Merged configuration dictionary.
    """
    # Load environment variables from .env file
    # load_dotenv(dotenv_path="config/.env")
    # Ensure the config directory exists
    os.makedirs(os.path.dirname(config_path), exist_ok=True)

    # Load YAML configuration file
    with open(config_path, 'r') as file:
        raw_config = yaml.safe_load(file)

    # Merge with environment variables
    for section in raw_config:
        if isinstance(raw_config[section], dict):
            for key, value in raw_config[section].items():
                env_key = f"CONFIG_{section.upper()}_{key.upper()}"
                if env_key in os.environ:
                    raw_config[section][key] = os.environ[env_key]
    return raw_config