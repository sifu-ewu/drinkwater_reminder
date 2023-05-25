import os
import pickle
import base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

if os.path.exists('token.pickle'):
    os.remove('token.pickle')
else:
    print("The file does not exist")


def service_gmail():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    try:
        service = build('gmail', 'v1', credentials=creds)
        return service
    except Exception as e:
        print(e)
        return None


def create_message_with_image_url(sender, to, subject, image_url):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to

    # Plain-text version of the email
    text = "This is a reminder to drink water!"

    # HTML version of the email. This one includes an image from a URL.
    html = f"""
    <html>
    <body>
        <p>This is a reminder to drink water!</p>
        <img src="{image_url}" alt="Water reminder">
    </body>
    </html>
    """

    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(html, 'html'))

    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    return {'raw': raw }

def send_email(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    service = service_gmail()
    sender = 'khabomara159@gmail.com'
    to = 'yotullah@gmail.com'
    subject = 'Water drinking reminder'
    image_url = 'https://i.ibb.co/8x3W85P/received-227556656626520.jpg'  # replace with your image URL

    while True:
        message = create_message_with_image_url(sender, to, subject, image_url)
        send_email(service, 'me', message)
        time.sleep(7200)  # Wait for 2 hours
