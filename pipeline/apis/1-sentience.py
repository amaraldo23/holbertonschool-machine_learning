#!/usr/bin/env python3
"""
This module retrieves the list of home planets for all sentient species
from the Star Wars API (SWAPI).
"""

import requests


def sentientPlanets():
    """
    Fetches the names of home planets for all sentient species.

    Sentient species are identified by having "sentient" in either their
    classification or designation attributes.

    Returns:
        list: A list of unique planet names where sentient species reside.
    """
    url = "https://swapi-api.alx-tools.com/api/species/"
    planets = set()  # Use a set to store unique planet names

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            return []

        data = response.json()

        for species in data.get("results", []):
            classification = species.get("classification", "").lower()
            designation = species.get("designation", "").lower()

            if "sentient" in (classification, designation):
                homeworld = species.get("homeworld")
                if homeworld:
                    planet_response = requests.get(homeworld)
                    if planet_response.status_code == 200:
                        planet_name = planet_response.json().get("name")
                        if planet_name:
                            planets.add(planet_name)

        url = data.get("next")  # Get the next page URL for pagination

    return sorted(planets)  # Return sorted list for consistency
