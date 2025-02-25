import psycopg2
from twilio.rest import Client

# message

MESSAGE = """Hello, this is a test message"""

# twilio
SID = ""
AUTH_TOKEN = ""
PHONE_NUMBER = ""

# DB connection

conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="",
    port=""
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
        cur.execute("SELECT Tel_number FROM notifications WHERE status = 'false'")
        notifications = cur.fetchall()

        for notif in notifications:
            notif_id, phone_number = notif 
            try:
                message_sid = send_sms(phone_number, MESSAGE)
                cur.execute("UPDATE notifications SET status = 'true' WHERE id = %s", (notif_id,))
                conn.commit()
            except Exception as e:
                print(f"Failed to send message to {phone_number}: {e}")




if __name__ = "__main__":
    process_notifications()
    conn.close()

