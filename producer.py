import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='instagram')
profile_url=str(input("İnstagram Kullanıcı Adını Giriniz: "))
channel.basic_publish(exchange='',routing_key='instagram',body=profile_url)
print("Instagram Kullanıcı adınız kuyruğa alındı.")
connection.close()