import schedule
import time
import requests
import random

# EbulkSMS credentials and girlfriend's phone number
username = "charlescollins476@gmail.com"
apikey = "c3c7182d27bd23ef941cabd6da37d13a68d9f50d"
sendername = "Collins"
recipient_msidn = "+2347031089677"
# recipient_msidn = "+2348108719984"

# Read the list of love messages from a file
with open("love_messages.txt", "r") as file:
    love_messages = file.readlines()


def send_love_message():
    # Randomly select a message from the list
    message_text = random.choice(love_messages)

    # Create the JSON request data
    request_data = {
        "SMS": {
            "auth": {
                "username": username,
                "apikey": apikey,
            },
            "message": {
                "sender": sendername,
                "messagetext": message_text,
                "flash": "0",
            },
            "recipients": {
                "gsm": [
                    {
                        "msidn": recipient_msidn,
                        "msgid": "uniqueid1",
                    },
                ],
            },
            "dndsender": 1,
        },
    }

    # Send the POST request to the EbulkSMS API
    url = "https://api.ebulksms.com:8080/sendsms.json"
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers, json=request_data)

    # Check if the SMS was sent successfully
    if response.status_code == 200:
        print("Love message sent successfully!")
    else:
        print("Error sending love message:", response.status_code, response.text)


# Schedule the task to send love messages every morning at 7:00 AM
schedule.every().day.at("07:00").do(send_love_message)
# schedule.every().day.at("18:35").do(send_love_message)

while True:
    schedule.run_pending()
    time.sleep(1)
