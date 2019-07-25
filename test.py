import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()

channel.queue_declare(queue='export')

channel.basic_publish(exchange='', routing_key='export', body="{'task_id': 787878787, 'form_id': 1, 'groups': [1], 'export_format': 'csv', 'email': 'leorik09@gmail.com'}")
print(" [x] Sent 'Hello World!'")
connection.close()

print('111111111111111111111111111')