import pika
from app import send_email, send_sms

def process_notifications():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notification_queue')

    def callback(ch, method, properties, body):
        data = eval(body)  # In real-world, use JSON and handle errors properly
        notification_type = data['notification_type']
        message = data['message']

        if notification_type == "email":
            if not send_email(message):
                print(f"Failed to send email: {message}")
        elif notification_type == "sms":
            if not send_sms(message):
                print(f"Failed to send SMS: {message}")
        else:
            print(f"Unknown notification type: {notification_type}")
        
    channel.basic_consume(queue='notification_queue', on_message_callback=callback, auto_ack=True)
    print('Waiting for notifications...')
    channel.start_consuming()

if __name__ == '__main__':
    process_notifications()
