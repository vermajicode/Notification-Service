# Notification-Service
This is a Notification Service built using Flask and RabbitMQ, which allows sending notifications to users via Email, SMS, and In-app notification system.

Features
Email Notifications via Gmail SMTP.

SMS Notifications via Twilio.

Message Queue using RabbitMQ to process notifications asynchronously.

API endpoints for sending and fetching notifications.

Assumptions
Gmail Account: Used for sending emails. You need to enable Less Secure Apps or generate an App Password if you have 2FA enabled.

Twilio Account: You need a Twilio Account SID, Auth Token, and a Twilio phone number to send SMS.

RabbitMQ: Assumed to be installed and running locally.

Setup Instructions
1. Clone the Repository
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/your-username/notification-service.git
cd notification-service
2. Install Dependencies
2.1 Set Up a Python Virtual Environment
It's recommended to use a virtual environment to isolate dependencies:

bash
Copy
Edit
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
2.2 Install the Required Libraries
Install the necessary dependencies using pip:

bash
Copy
Edit
pip install -r requirements.txt
The dependencies are:

Flask: A web framework to create API endpoints.

pika: Python library to interface with RabbitMQ.

Twilio: Library to send SMS using Twilio.

smtplib: Standard Python library to send emails via Gmail.

3. Configuration
3.1 Gmail Email Setup
To send emails via Gmail, you'll need to either:

Enable Less Secure Apps or

Use App Passwords (if you have 2FA enabled).

For enabling Less Secure Apps:

Enable Less Secure Apps.

If you have 2FA enabled:

Generate an App Password.

Replace the "yourpassword" in the send_email function with either your regular Gmail password (if Less Secure Apps is enabled) or your App Password (if 2FA is enabled).

3.2 Twilio Setup
Create a Twilio account at Twilio's website.

Get your Twilio Account SID, Auth Token, and Twilio phone number.

Replace the your_twilio_account_sid, your_twilio_auth_token, and your_twilio_phone_number in app.py with your Twilio credentials.

3.3 RabbitMQ Setup
Install RabbitMQ from RabbitMQ Download Page.

Make sure RabbitMQ is running locally before starting the Flask app.

On Windows: rabbitmq-server.bat start

On Linux: sudo service rabbitmq-server start

4. Run the Application
4.1 Start the Flask API
Run the Flask server:

bash
Copy
Edit
python app.py
By default, Flask will run on http://127.0.0.1:5000/.

4.2 Start the Worker
To process the notifications in RabbitMQ, run the worker in another terminal:

bash
Copy
Edit
python worker.py
4.3 Test the API
Use Postman or cURL to test the POST /notifications and GET /users/{id}/notifications endpoints.

Example of a POST /notifications request:

json
Copy
Edit
{
  "user_id": 123,
  "type": "email",
  "message": "This is your notification"
}
5. Directory Structure
bash
Copy
Edit
/Notification system
├── app.py                  # Flask API logic
├── worker.py               # Worker that processes RabbitMQ messages
├── requirements.txt        # List of required Python libraries
├── README.md               # This file
└── /env                    # Virtual environment folder
6. Known Issues
Gmail may block sign-ins if there are repeated unsuccessful attempts. You may need to check your Gmail account security settings if this happens.

Ensure RabbitMQ is running locally, otherwise notifications won’t be processed.

7. License
This project is licensed under the MIT License - see the LICENSE file for details.

Example of requirements.txt:
makefile
Copy
Edit
Flask==2.2.3
pika==1.3.1
twilio==7.10.0
