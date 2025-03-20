#!/usr/bin/env python3

"""
This script fetches launch data from the SpaceX API and displays the number of launches per rocket.

It makes a request to the SpaceX API, processes the launch data, and counts the number of launches
for each rocket. The results are then printed in descending order of launch count and, in case of ties,
alphabetically by the rocket name.

Example output:
    Falcon 9: 103
    Falcon 1: 5
    Falcon Heavy: 3
"""

import requests

def get_launch_count_by_rocket():
    """
    Fetches data from the SpaceX API and displays the number of launches per rocket.

    The function retrieves launch data from SpaceX's unofficial API,
    counts the number of launches for each rocket, and displays the results.
    The results are sorted first by the number of launches in descending order
    and then by rocket name in alphabetical order if the count is the same.

    Output:
        - Prints the rocket name and the count of launches in the format: 'Rocket Name: Count'
    """
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    launches = response.json()

    # Dictionary to store rocket names and their launch counts
    rocket_counts = {}

    # Counting the number of launches for each rocket
    for launch in launches:
        rocket_id = launch['rocket']
        rocket_name = launch['name']  # Assuming the rocket name is available here
        if rocket_name not in rocket_counts:
            rocket_counts[rocket_name] = 1
        else:
            rocket_counts[rocket_name] += 1

    # Sorting the rockets by launch count in descending order, 
    # and by rocket name alphabetically if launch counts are the same
    sorted_rockets = sorted(rocket_counts.items(), key=lambda x: (-x[1], x[0]))

    # Printing the results
    for rocket_name, count in sorted_rockets:
        print(f"{rocket_name}: {count}")

if __name__ == '__main__':
    get_launch_count_by_rocket()
