import random

import boto3

GERMAN_WORDS = [
    "die Verschlimmbessern",
    "das Fernweh",
    "die Backpfeifengesicht",
]


def get_todays_word():
    return random.choice(GERMAN_WORDS)


def lambda_handler(_event, _context):
    german_word = get_todays_word()
    subject = f"Do you know what {german_word} means?"
    body = f"{german_word} means ..."

    ses_client = boto3.client("ses")

    response = ses_client.send_email(
        Source="monicamengni@gmail.com",
        Destination={
            "ToAddresses": ["monicamengni@gmail.com"],
        },
        Message={
            "Subject": {"Data": subject, "Charset": "UTF-8"},
            "Body": {"Text": {"Data": body, "Charset": "UTF-8"}},
        },
    )

    return {
        "statusCode": 200,
        "body": f"Email sent successfully with word: {german_word}. MessageId: {response['MessageId']}",
    }
