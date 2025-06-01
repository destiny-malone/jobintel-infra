import logging
import sys


def setup_logger(name, level=logging.INFO):
    """
    Set up a logger with the specified name and logging level.

    Args:
        name (str): Name of the logger.
        level (int): Logging level (default is logging.INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level.upper())
    # Check if the logger already has handlers to avoid duplicate logs

    # Create console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(level.upper())
    # Set the logging format

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    return logger