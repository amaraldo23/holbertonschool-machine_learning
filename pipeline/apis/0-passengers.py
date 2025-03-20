#!/usr/bin/env python3
"""
This module retrieves a list of ships from the Star Wars API (SWAPI)
that can hold a given number of passengers.
"""

import requests


def availableShips(passengerCount):
    """
    Fetches all Star Wars ships that can accommodate at least `passengerCount`.

    Args:
        passengerCount (int): The min number of passenger the ship should hold.

    Returns:
        list: A list of ship names that meet the criteria.
    """
    url = "https://swapi-api.alx-tools.com/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            return []

        data = response.json()

        for ship in data.get("results", []):
            passengers = ship.get("passengers", "0").replace(",", "").strip()
            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship["name"])

        url = data.get("next")  # Get the next page URL for pagination

    return ships
