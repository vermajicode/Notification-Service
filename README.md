# Notification Service
This service provides an API to send notifications (SMS and Email) to users. Notifications are queued using RabbitMQ for processing, and messages are sent either through Twilio for SMS or via SMTP for email.

Setup Instructions
Prerequisites
Python 3.x - Make sure you have Python 3.x installed on your machine.

RabbitMQ - This service uses RabbitMQ for queuing messages. Ensure you have RabbitMQ installed and running locally.

Twilio Account - You need a Twilio account with the SID, Auth Token, and a phone number to send SMS.

SMTP Credentials - For sending email notifications, you need an SMTP service (e.g., Gmail, SendGrid). You'll need the email and password for the SMTP login.

1. Clone the repository
git clone https://github.com/yourusername/notification-service.git
cd notification-service

2. Install dependencies
Ensure you have the required dependencies by running the following command:

pip install -r requirements.txt

3. Configure SMTP and Twilio
In the app.py file, update the following with your credentials:

SMTP:

Update the SMTP server configuration with your email provider's settings.

Replace "email@example.com" and "password" with your actual credentials.

Twilio:

Replace "your_twilio_account_sid", "your_twilio_auth_token", and "your_twilio_phone_number" with your actual Twilio details.

4. Start RabbitMQ
Make sure RabbitMQ is running on your machine. If not, you can start it with the following command (depending on your installation method):

rabbitmq-server

5. Run the Flask API
To run the notification service API, use the following command:

python app.py

This will start a Flask server on http://localhost:5000. The available endpoints are:

POST /notifications: Send a notification to a user. Requires JSON body with user_id, type (email/sms), and message.

GET /users/{id}/notifications: Fetch notifications for a user (returns an empty list for now).

6. Process the Notifications
To start processing the notifications, run the worker script:

python worker.py

This will consume notifications from the RabbitMQ queue and send either an email or SMS depending on the notification_type.

Assumptions
The API is only processing email and SMS notifications; support for other notification types is not implemented yet.

RabbitMQ is used as the messaging queue for notification delivery.

The code assumes that the user_id is an identifier for the user who should receive the notification but does not handle user data or store notifications.

You need valid email and Twilio credentials for the notification system to function.
