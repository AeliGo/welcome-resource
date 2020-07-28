"""
This module saves a welcome message.
"""

import json


def welcome():
    message = "Welcome to Orquestra! lili"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("welcomelili.json", 'w') as f:
        f.write(
            json.dumps(message_dict, indent=2)
        )  # Write message to file as this will serve as output artifact
