import requests
from lxml import html
from bs4 import BeautifulSoup

LOGIN_URL = "https://beautyprodutcs.net/login"
URL = "https://beautyprodutcs.net/EndUserDashboard"

def main():
    session_requests = requests.session()

    result = session_requests.get(LOGIN_URL)
   
    # Create payload
    payload = {
        "email": "swathi@gmail.com", 
	    "password": "9238293921", 
	    "csrfmiddlewaretoken": "SmfvK5QAqPKbqZeiaMkgVF9wJj4DsdyXLRr7apvU"
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    print('hi')
   

if __name__ == '__main__':
    main()
    print('Got Output')

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

url = "https://beautyprodutcs.net/login"
print('swa')
response = requests.get(url, timeout=9000)
content = BeautifulSoup(response.content, 'html.parser')
print(content)
UL = "https://beautyprodutcs.net/EndUserDashboard"
print('swa')
response = requests.get(UL, timeout=9000)
content = BeautifulSoup(response.content, 'html.parser')
print(content)
# row_tags = doc.find_all('tr')

# for row in row_tags:
#     print(row.text.strip())
