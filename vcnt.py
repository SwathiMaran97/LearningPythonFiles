import requests
from lxml import html
from bs4 import BeautifulSoup

LOGIN_URL = "https://vconnect.inesssolutions.net/login"
URL = "https://vconnect.inesssolutions.net/EndUserDashboard"

def main():
    session_requests = requests.session()

    result = session_requests.get(LOGIN_URL)
   
    # Create payload
    payload = {
        "email": "swathi@inesssolutions.com", 
	    "password": "iness123", 
	    "csrfmiddlewaretoken": "SmfvK5QAqPKbqZeiaMkgVF9wJj4DsdyXLRr7apvU"
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    print('hi')
   

if __name__ == '__main__':
    main()
    print('SAN')

data = {
    '#': '1',
    'Task ID': 'Gen-01513',
    'Task Description': 'Completed 8D module',
    'Maximum Hours': '40',
    'worked Hours': '40',
    'Start Date': '2020-04-06',
    'End Date': '2020-04-10',
    'Progress': 'Completed',}
print('jjjjj')

url = "https://vconnect.inesssolutions.net/login"
print('swa')
response = requests.get(url, timeout=9000)
content = BeautifulSoup(response.content, 'html.parser')
print(content)
UL = "https://vconnect.inesssolutions.net/EndUserDashboard"
print('swa')
response = requests.get(UL, timeout=9000)
content = BeautifulSoup(response.content, 'html.parser')
print(content)
# row_tags = doc.find_all('tr')

# for row in row_tags:
#     print(row.text.strip())