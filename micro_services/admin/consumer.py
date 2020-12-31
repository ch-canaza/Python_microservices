import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://sqzqxszn:IaiC_jCNVYLcw4jp183zSeB9iub6ERks@codfish.rmq.cloudamqp.com/sqzqxszn')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(body)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('product likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started Consuming')

channel.start_consuming()
channel.close()
