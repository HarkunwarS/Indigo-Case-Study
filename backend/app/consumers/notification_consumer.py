import pika
import json
from app.utils.notifications import send_sms, send_email

def callback(ch, method, properties, body):
    notification = json.loads(body)
    if notification['method'] == 'SMS':
        send_sms(notification['recipient'], notification['message'])
    elif notification['method'] == 'Email':
        send_email(notification['recipient'], "Flight Update", notification['message'])
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notifications')
    channel.basic_consume(queue='notifications', on_message_callback=callback)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
