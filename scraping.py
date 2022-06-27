# import requests
# from lxml import html
# from bs4 import BeautifulSoup as bs
# update=requests.post('https://vconnect.inesssolutions.net/login',data={'email':'swathi@inesssolutions.com','password':'iness123'})
# s=bs(update.content,'lxml')
# print(s)
# from lxml import html
# import requests

# payload = {
# 	"email": "<swathi@inesssolutions.com>", 
# 	"password": "<iness123>", 
# 	"csrfmiddlewaretoken": "<W0CcY1tStCDtRwGuOIwojvqt9ZMgf5LN1p7FG5f2>"
# }
# session_requests = requests.session()
# extract this data.

# login_url = "https://vconnect.inesssolutions.net/login"
# result = session_requests.get(login_url)

# tree = html.fromstring(result.text)
# authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
# result = session_requests.post(
# 	login_url, 
# 	data = payload, 
# 	headers = dict(referer=login_url)
# )
# url = 'https://vconnect.inesssolutions.net/EndUserDashboard'
# result = session_requests.get(
# 	url, 
# 	headers = dict(referer = url)
# )
# tree = html.fromstring(result.content)
# bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

# print(bucket_names)
# result.ok 
# result.status_code 

import requests
from lxml import html
from bs4 import BeautifulSoup
# USERNAME = "<USERNAME>"
# PASSWORD = "<PASSWORD>"

LOGIN_URL = "https://vconnect.inesssolutions.net/login"
URL = "https://vconnect.inesssolutions.net/EndUserDashboard"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    # tree = html.fromstring(result.text)
    # authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "email": "swathi@inesssolutions.com", 
	    "password": "iness123", 
	    "csrfmiddlewaretoken": "W0CcY1tStCDtRwGuOIwojvqt9ZMgf5LN1p7FG5f2"
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    print('hi')
    # Scrape url
    # result = session_requests.get(URL, headers = dict(referer = URL))
    # tree = html.fromstring(result.content)
    # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    # print(bucket_names)

if __name__ == '__main__':
    main()
    print('hi')

# response = requests.get("https://vconnect.inesssolutions.net/EndUserDashboard")
# doc = BeautifulSoup(response.text, 'html.parser')

# # Grab all of the rows
# row_tags = doc.find_all('tr')

# # Let's print the first 5
# for row in row_tags[:5]:
#     print(row.text.strip())

data = {
    '#': '1',
    'Task ID': 'Gen-01513',
    'Task Description': 'Completed 8D module',
    'Maximum Hours': '40',
    'worked Hours': '40',
    'Start Date': '2020-04-06',
    'End Date': '2020-04-10',
    'Progress': 'Completed',}

url = "https://vconnect.inesssolutions.net/EndUserDashboard"
response = requests.post(url, data=data)
doc = BeautifulSoup(response.text, 'html.parser')

# Grab all of the rows
row_tags = doc.find_all('tr')

# Let's print the first 5
for row in row_tags:
    print(row.text.strip())