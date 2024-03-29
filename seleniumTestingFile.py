from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import webbrowser
from urllib.parse import urljoin
session = HTMLSession()

url = "https://vconnect.inesssolutions.net/login"
url = "https://vconnect.inesssolutions.net/EndUserDashboard" 

# url="https://vconnect.inesssolutions.net/login"

def get_all_forms(url):
    """Returns all form tags found on a web page's `url` """
    # GET request
    res = session.get(url)
    # for javascript driven website
    # res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """Returns the HTML details of a form,
    including action, method and list of form controls (inputs, etc)"""
    details = {}
    # get the form action (requested URL)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, DELETE, etc)
    # if not specified, GET is the default in HTML
    method = form.attrs.get("method", "get").lower()
    # get all form inputs
    inputs = []
    for input_tag in form.find_all("input"):
        # get type of input form control
        input_type = input_tag.attrs.get("type", "text")
        # get name attribute
        input_name = input_tag.attrs.get("name")
        # get the default value of that input tag
        input_value =input_tag.attrs.get("value", "")
        # add everything to that list
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


# url = "https://wikipedia.org"
# get all form tags
forms = get_all_forms(url)
# iteratte over forms
for i, form in enumerate(forms, start=1):
    form_details = get_form_details(form)
    print("="*75, f"form #{i}", "="*75)
    print(form_details)    

first_form = get_all_forms(url)[0]
form_details = get_form_details(first_form)


data = {}
for input_tag in form_details["inputs"]:
    if input_tag["type"] == "hidden":
        # if it's hidden, use the default value
        data[input_tag["name"]] = input_tag["value"]
    elif input_tag["type"] != "submit":
        # all others except submit, prompt the user to set it
        value = input(f"Enter the value of the field '{input_tag['name']}' (type: {input_tag['type']}): ")
        data[input_tag["name"]] = value

url = urljoin(url, form_details["action"])

# if form_details["method"] == "post":
#     res = session.post(url, data=data)
#     print('hiiii')
if form_details["method"] == "get":
    res = session.get(url, params=data)
    print('jjiii')        
elif form_details["method"] == "post":
    res = session.post(url, data=data)
    print('hiiii')
# soup = BeautifulSoup(res.content, "html.parser")
# for link in soup.find_all("link"):
#     try:
#         link.attrs["href"] = urljoin(url, link.attrs["href"])
#     except:
#         pass
# for script in soup.find_all("script"):
#     try:
#         script.attrs["src"] = urljoin(url, script.attrs["src"])
#     except:
#         pass
# for img in soup.find_all("img"):
#     try:
#         img.attrs["src"] = urljoin(url, img.attrs["src"])
#     except:
#         pass
# for a in soup.find_all("a"):
#     try:
#         a.attrs["href"] = urljoin(url, a.attrs["href"])
#     except:
#         pass

# # write the page content to a file
# open('E:\swathi\employee\examples\sele.py', "w").write(str(soup))



webbrowser.open("https://vconnect.inesssolutions.net/login")
