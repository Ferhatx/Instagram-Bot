import pika
import requests
from bs4 import BeautifulSoup
import json
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
headers = {'User-Agent': 'Mozilla/5.0'}
channel.queue_declare(queue='instagram')
def callback(ch,method,properties,body):
    url = 'https://www.instagram.com/'+str(body.decode())+'/?__a=1'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    insta_json = json.loads(soup.text)

    userid = insta_json.get('graphql')['user']['username']
    fullname = insta_json.get('graphql')['user']['full_name']
    ppurl = insta_json.get('graphql')['user']['profile_pic_url_hd']
    biography = insta_json.get('graphql')['user']['biography']
    pcount = insta_json.get('graphql')['user']['edge_owner_to_timeline_media']['count']
    fllwingcnt = insta_json.get('graphql')['user']['edge_follow']['count']
    flwrscnt = insta_json.get('graphql')['user']['edge_followed_by']['count']
    print('')

    print(str(body.decode())+' instangram kullanıcısının bilgileri;')
    print('')
    print('User id : @' + userid)
    print('Full Name : ' + fullname)
    print('Biography : ' + biography)
    print('Post Count : ' + str(pcount))
    print('Followers Count : ' + str(flwrscnt))
    print('Following Count : ' + str(fllwingcnt))
    print('Profile Picture Url : ' + ppurl)
print('Kuyruğa instagram kullanıcısı eklenmesi için bekleniyor...')
channel.basic_consume('instagram',callback,auto_ack=True)
channel.start_consuming()