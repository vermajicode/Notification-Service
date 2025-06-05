from flask import Flask, request, jsonify
import pika
import smtplib
from twilio.rest import Client

app = Flask(__name__)

# Simple function to send an email (SMTP)
def send_email(message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("email@example.com", "password")
        server.sendmail("email@example.com", "recipient@example.com", message)
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Simple function to send SMS using Twilio
def send_sms(message):
    try:
        client = Client("your_twilio_account_sid", "your_twilio_auth_token")
        client.messages.create(
            body=message,
            from_="your_twilio_phone_number",
            to="recipient_phone_number"
        )
        return True
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False

# POST /notifications endpoint
@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.get_json()
    user_id = data['user_id']
    notification_type = data['type']
    message = data['message']
    
    # Send to RabbitMQ for processing
    send_to_queue(user_id, notification_type, message)
    
    return jsonify({"status": "Notification sent to queue!"}), 200

# Function to send data to RabbitMQ queue
def send_to_queue(user_id, notification_type, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notification_queue')

    notification_data = {
        'user_id': user_id,
        'notification_type': notification_type,
        'message': message
    }

    channel.basic_publish(exchange='',
                          routing_key='notification_queue',
                          body=str(notification_data))
    connection.close()

# GET /users/{id}/notifications endpoint
@app.route('/users/<int:user_id>/notifications', methods=['GET'])
def get_notifications(user_id):
    # In a real-world system, fetch notifications from a database
    return jsonify({"notifications": []}), 200

if __name__ == '__main__':
    app.run(debug=True)
