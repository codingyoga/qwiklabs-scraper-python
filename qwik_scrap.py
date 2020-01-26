import requests
from lxml import html


session_requests = requests.session()

login_url = "https://www.qwiklabs.com/users/sign_in"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]

#print(authenticity_token)

payload = {'user[email]': 'your mail id',
           'user[password]': 'your password',
           "authenticity_token": authenticity_token
           }

result = session_requests.post(login_url,
                               data=payload,
                               headers=dict(referer=login_url))
#print(result.content)

#https://www.qwiklabs.com/focuses/1002?parent=catalog
#to get content of lab 1002 : Cloud Source Repositories: Qwik Start
url = 'https://www.qwiklabs.com/focuses/1002?parent=catalog'
result = session_requests.get(
    url,
    headers=dict(referer=url)
)
print(result.content)