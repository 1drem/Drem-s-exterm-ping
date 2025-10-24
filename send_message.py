import requests

# Replace with your actual Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1431116828796784700/wAl5aWp0JoV3jb8rIiBWePc6EbRdYR1ZAR6uCSztu9eWO9f8S8O603pYUWJO5_JkaENi"

def send_discord_message(content: str):
    data = {"@everyone": content}
    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("✅ Message sent successfully!")
    else:
        print(f"❌ Failed to send message: {response.status_code}, {response.text}")

if __name__ == "__main__":
    send_discord_message("@everyone")
