#!/usr/bin/env python3
"""
This script retrieves the location of a specific GitHub user
using the GitHub API.
"""

import sys
import requests
import time


def get_user_location(api_url):
    """
    Fetches and prints the location of a GitHub user.

    Args:
        api_url (str): The GitHub API URL of the user.

    Returns:
        None
    """
    response = requests.get(api_url)

    if response.status_code == 200:
        user_data = response.json()
        location = user_data.get("location")
        print(location if location else "Location not available")
    elif response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:  # Rate limit exceeded
        reset_time = int(response.headers.get("X-RateLimit-Reset", time.time()))

        minutes_remaining = max(0, (reset_time - time.time()) // 60)
        print(f"Reset in {int(minutes_remaining)} min")
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
        sys.exit(1)

    api_url = sys.argv[1]
    get_user_location(api_url)
