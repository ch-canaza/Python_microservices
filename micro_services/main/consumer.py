import pika, json
from main import Product, db

params = pika.URLParameters('amqps://sqzqxszn:IaiC_jCNVYLcw4jp183zSeB9iub6ERks@codfish.rmq.cloudamqp.com/sqzqxszn')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    """ 
        receive information  and convert in to object 
    """
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()

    elif properties.content_type =='product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()

        
channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('started Consuming')

channel.start_consuming()
channel.close()
