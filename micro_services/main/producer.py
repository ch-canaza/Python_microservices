import pika, json

params = pika.URLParameters('amqps://sqzqxszn:IaiC_jCNVYLcw4jp183zSeB9iub6ERks@codfish.rmq.cloudamqp.com/sqzqxszn')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    """
        publish RabbitMQ channel
    """
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
