import psycopg2
import os
from twilio.rest import Client
from dotenv import load_dotenv


MESSAGE = """You are cooked/overcooked. Please check the oven"""


# Twilio credentials
load_dotenv()

SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

# DB connection
conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=int(os.getenv("POSTGRES_PORT"))
)

def send_sms(phone_number, message):
    client = Client(SID, AUTH_TOKEN)
    message = client.messages.create(
        to=phone_number,
        from_=PHONE_NUMBER,
        body=message
    )
    return message.sid

def process_notifications():
    with conn.cursor() as cur:
        cur.execute("SELECT id, phone_number FROM notifications WHERE NOT status ")
        notifications = cur.fetchall()

        for notif in notifications:
            notif_id, phone_number = notif 
            try:
                message_sid = send_sms(phone_number, MESSAGE)
                cur.execute("UPDATE notifications SET Status = 'true' WHERE id = %s", (notif_id,))
                conn.commit()
                print(f"Message sent to {phone_number} - SID: {message_sid}")
            except Exception as e:
                print(f"Failed to send message to {phone_number}: {e}")




if __name__ == "__main__":
    process_notifications()
    conn.close()

