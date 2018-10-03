from twilio.rest import Client
import config

client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)


def send_warning_message():
    message = client.messages.create(
        to="+919633898159",
        from_=config.TWILIO_PHONE_NUMBER,
        body="Warning!")

    print(message.sid)
