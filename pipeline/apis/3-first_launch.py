#!/usr/bin/env python3
"""
This script fetches the first SpaceX launch from the SpaceX API and displays 
the launch details including the name of the launch, the date, the rocket used, 
and the launchpad used. The launch details are displayed in the following format:

    <launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)

The script uses the SpaceX API to get the necessary information and sorts the 
launches by the 'date_unix' field to find the first launch.
"""

import requests
from datetime import datetime

def get_first_launch():
    """
    Fetches the first launch from the SpaceX API, sorts by date, and prints the
    details of the launch in a specific format.

    The format is: 
    <launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)

    The function makes multiple requests to the SpaceX API to get data about 
    the launch, rocket, and launchpad, and then prints the details.
    """
    # SpaceX API URL for launches
    url = "https://api.spacexdata.com/v4/launches"
    
    # Make an HTTP GET request to the SpaceX API to fetch launch data
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data from SpaceX API")
        return

    # Get the list of launches from the response
    launches = response.json()

    if not launches:
        print("No launches found")
        return

    # Sort the launches by the 'date_unix' field (ascending)
    launches.sort(key=lambda launch: launch['date_unix'])

    # Get the first launch
    first_launch = launches[0]

    try:
        # Extracting the necessary details
        launch_name = first_launch['name']
        launch_date = datetime.utcfromtimestamp(first_launch['date_unix']).strftime('%Y-%m-%dT%H:%M:%S%z')
        
        # Fetch rocket information using the rocket ID
        rocket_id = first_launch['rocket']
        rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
        rocket_response = requests.get(rocket_url)
        rocket_response.raise_for_status()
        rocket_name = rocket_response.json().get('name', 'Unknown Rocket')

        # Fetch launchpad information using the launchpad ID
        launchpad_id = first_launch['launchpad']
        launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
        launchpad_response = requests.get(launchpad_url)
        launchpad_response.raise_for_status()
        launchpad_data = launchpad_response.json()
        launchpad_name = launchpad_data.get('name', 'Unknown Launchpad')
        launchpad_locality = launchpad_data.get('locality', 'Unknown Locality')

        # Print the result in the required format
        print(f"{launch_name} ({launch_date}) {rocket_name} - {launchpad_name} ({launchpad_locality})")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: Network request failed - {e}")
    except KeyError as e:
        print(f"Error: Missing key {e} in launch data.")
    except TypeError as e:
        print(f"Error: Type error - {e}")

if __name__ == '__main__':
    """
    This checks if the script is being run as the main program and, if so, 
    it calls the get_first_launch function to print the first launch details.
    """
    get_first_launch()
