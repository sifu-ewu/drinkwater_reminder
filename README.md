
# Hydrate Reminder: Drink Water Reminder System

Hydrate Reminder is a Python-based project developed to remind you and your loved ones to stay hydrated throughout the day. This simple yet effective tool is designed to ensure that you maintain a healthy water intake, a crucial aspect of overall wellness that we often overlook in our busy schedules.

Built around the Gmail API, Hydrate Reminder sends friendly email reminders every two hours, prompting you to take a break and have a glass of water. Not just text, these reminders come with an engaging image of a glass of water, adding a visual appeal to the gentle nudge

# Embrace Hydration with Love

At the heart of Hydrate Reminder is a message of love and care. It's about cherishing our health and extending that care to people who matter to us the most. It's about helping each other in our journey towards better health habits.

With Hydrate Reminder, you can ensure that your loved ones are reminded of their water intake. Whether they're near or far, they'll appreciate these loving reminders, these sips of care that reach their inbox.

Hydrate Reminder isn't just about staying hydrated; it's a small step towards expressing our love and concern in a unique, healthful way. Join us in nurturing this culture of care, one reminder at a time. With Hydrate Reminder, let's toast to the health and happiness of those we hold dear.


![alt text](https://i.ibb.co/8x3W85P/received-227556656626520.jpg)



## Prerequisites
Before you can run the script, you'll need to:
   The steps are as follows:
   
    1.	Go to the Google Developer Console.
    2.	Click on "Select a project" > "New Project", give it a name and create it.
    3.	After the project is created, select "Dashboard" from the left menu, then select "+ ENABLE APIS AND SERVICES"
    4.	Search for "Gmail API" and enable it.
    5.	Go to "Credentials" from the left menu, click on "+ CREATE CREDENTIALS", and select "OAuth client ID".
    6.	Set the application type to "Desktop app", give it a name, and create it.
    7.	Download the JSON file of the created credentials and save it as "credentials.json" in the same directory as your Python script.


     







## Deployment

The first time you run the script, you'll be redirected to a Google sign-in page. After signing in, you will be asked to grant some permissions. Once you've granted the permissions, you will be redirected back to your application. Now the script will be able to send emails every 2 hours, reminding you to drink water.

This script uses the refresh token to automatically renew the access token when it expires, so you won't need to sign in again. It's a better practice than using your email and password directly in the script, as this token will only allow sending emails and will not grant access to other actions (like reading or deleting emails).

```bash
  python drinkwater.py
```


## Customization
The script sends an email to a predefined recipient email address with a reminder message and an image. You can customize the sender's email, recipient's email, the subject of the email, and the image URL by modifying the following lines in the drinkwater.py script:

```bash
    sender = 'your-email@gmail.com'
    to = 'recipient-email@gmail.com'
    subject = 'Water drinking reminder'
    image_url = 'https://your-imgbb-url'  # replace with your image URL

```
## For the time 
```bash
time.sleep(7200)  # Wait for 2 hours
```
