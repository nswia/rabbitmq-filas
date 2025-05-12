import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='fila_teste_stress')

for i in range(100_000):  # Altere esse valor conforme o nível de stress desejado
    message = f"Mensagem {i}"
    channel.basic_publish(exchange='', routing_key='fila_teste_stress', body=message)
    if i % 1000 == 0:
        print(f"Enviadas {i} mensagens...")

print("🚀 Envio concluído.")
connection.close()
