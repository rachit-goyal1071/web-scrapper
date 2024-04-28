import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# Check if the element with the specified class is found
project_name_div = soup.find(class_="md-card-left-owner")
if project_name_div:
    # Iterate over the found elements
    for div in project_name_div:
        print(div)
else:
    print("Element with class 'p-project-name' not found.")
