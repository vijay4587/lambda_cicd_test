import json
from utils import process_data
import pandas as pd


def lambda_handler(event, context):
    """
    Sample AWS Lambda handler.
    Takes an event with a 'name' field and returns a greeting with processed data.
    """

    # Get name from event (or use default)
    name = event.get("name", "World")

    # Call function from utils.py
    processed_value = process_data(name)
    df = pd.DataFrame({'fruits': ['apple', 'guava', 'pineapple'], 'vegetables': [
                      'onion', 'spinach', 'bitter guard']})
    print(df['fruits'])

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hello, {name}! 🚀",
            "processed_value": processed_value
        })
    }
    return response
