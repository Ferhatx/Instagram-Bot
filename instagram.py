import requests
from bs4 import BeautifulSoup
import json
profile_url=str(input("İnstagram Kullanıcı Adını Giriniz: "))
headers = {'User-Agent': 'Mozilla/5.0'}
instagram_url = 'https://instagram.com'

response = requests.get(f"{instagram_url}/{profile_url}/?__a=1",headers = headers)

soup = BeautifulSoup(response.content, "html.parser")
insta_json=json.loads(soup.text)


userid=insta_json.get('graphql')['user']['username']
fullname=insta_json.get('graphql')['user']['full_name']
ppurl=insta_json.get('graphql')['user']['profile_pic_url_hd']
biography=insta_json.get('graphql')['user']['biography']
pcount=insta_json.get('graphql')['user']['edge_owner_to_timeline_media']['count']
fllwingcnt=insta_json.get('graphql')['user']['edge_follow']['count']
flwrscnt=insta_json.get('graphql')['user']['edge_followed_by']['count']


print('User id : @'+userid)
print('Full Name : '+fullname)
print('Biography : '+biography)
print('Post Count : '+str(pcount))
print('Followers Count : '+str(flwrscnt))
print('Following Count : '+str(fllwingcnt))
print('Profile Picture Url : '+ppurl)
