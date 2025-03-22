#!/usr/bin/env python3
"""
Task 0: Generating personalized invitation files from a template
"""

import os


def generate_invitations(template: str, attendees: list[dict]) -> None:
    """
    Generates invitation files from a template
    and list of attendee dictionaries.

    Parameters:
    - template (str): Template string with placeholders.
    - attendees (list): List of dictionaries with keys: name, event_title,
      event_date, event_location.
    """

    # Validate template type
    if not isinstance(template, str):
        print("Error: Invalid input type. Template must be a string.")
        return

    # Validate attendees type
    if not isinstance(attendees, list) or not all(
        isinstance(att, dict) for att in attendees
    ):
        print("Error: Invalid input type. Attendees must be a list of \
        dictionaries.")
        return

    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Generate files
    for index, attendee in enumerate(attendees, start=1):
        # Get values with fallback to "N/A" for missing or None
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Replace placeholders
        personalized = template
        personalized = personalized.replace("{name}", name)
        personalized = personalized.replace("{event_title}", event_title)
        personalized = personalized.replace("{event_date}", event_date)
        personalized = personalized.replace("{event_location}", event_location)

        # File name: output_1.txt, output_2.txt, ...
        filename = f"output_{index}.txt"

        try:
            with open(filename, 'w') as file:
                file.write(personalized)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")
