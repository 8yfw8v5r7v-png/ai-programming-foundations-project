"""
Helper utilities for the project.
"""

import os
from datetime import datetime


def create_directory(path):
    """
    Create a directory if it doesn't exist.
    
    Args:
        path (str): Directory path to create
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")


def get_timestamp():
    """
    Get current timestamp as string.
    
    Returns:
        str: Current timestamp in format YYYY-MM-DD_HH-MM-SS
    """
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def log_message(message, level='INFO'):
    """
    Log a message with timestamp.
    
    Args:
        message (str): Message to log
        level (str): Log level (INFO, WARNING, ERROR)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")
