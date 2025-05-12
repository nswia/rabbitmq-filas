import pika
import time

def callback(ch, method, properties, body):
    print(f"📥 Recebida: {body.decode()}")
    # Simule lentidão no processamento, se quiser
    time.sleep(0.01)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='fila_teste_stress')
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='fila_teste_stress', on_message_callback=callback, auto_ack=True)

print("🔄 Aguardando mensagens (modo stress test)...")
channel.start_consuming()
