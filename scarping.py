import requests
from lxml import html
from bs4 import BeautifulSoup

headers = {
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36
}
token='/html/body/header/section/div/div/div/div[2]/div/div/form/input'
login_data ={
   '_token': token,
    'email': 'swathi@inesssolutions.com',
    'password': 'iness123'
}
print(token)
with requests.Session() as s:
    url = "https://vconnect.inesssolutions.net/login"
    url2= "https://vconnect.inesssolutions.net/EndUserDashboard" 
    r = s.get(url, headers=headers)
    r.status_code
    print(r.status_code)
    soup = BeautifulSoup(r.content, 'html5lib')
    login_data['_token']=soup.find("input", attrs={'name':'_token'})['value']
    print('value')
    r1= s.post(url, data=login_data,headers=headers)
    print(r.status_code)
    a="//*[@id='addgeneraltask']/div/div/form/div[1]/div[2]/textarea"
    a1=input("enter the task:")
    a=a1
    a2="//*[@id='addgeneraltask']/div/div/form/div[1]/div[3]/input"
    a3=input("enter the date:")
    a2=a3
    a4="//*[@id='addgeneraltask']/div/div/form/div[1]/div[4]/input"
    a5=input("enter the date:")
    a4=a5
    a6="//*[@id='addgeneraltask']/div/div/form/div[1]/div[5]/input"
    a7=input("enter the hours:")
    a6=a7
    token1="//*[@id='addgeneraltask']/div/div/form/input"
    login_data1 = {
        '_token':token1,
        'taskDescription':a1,
        'startDate': a3,
        'endDate': a5,
        'maximumHours': a7
    }
    headers1 ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    login_data1['_token']=soup.find("input", attrs={'name':'_token'})['value']
    print(r.status_code)
    r1= s.post(url2,data=login_data1,headers=headers1)
    print(r1.status_code)
    
    










