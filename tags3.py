from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Assuming you have a WebDriver set up, for example, ChromeDriver
driver = webdriver.Chrome()

# Load the web page
driver.get("https://www.oyorooms.com/search?location=Goa%2C%20India&city=Goa&searchType=city&coupon=&checkin=28%2F04%2F2024&checkout=29%2F04%2F2024&roomConfig%5B%5D=1&showSearchElements=false&country=india&guests=1&rooms=1&filters%5Bcity_id%5D=10")

# Wait for the page to load and the element to be present
wait = WebDriverWait(driver, 10)
project_name_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oyo-row oyo-row--no-spacing")))

# Parse the HTML content of the element
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Check if the element with the specified class is found
if project_name_div:
    # Find the ul element
    ul_element = soup.find(class_="oyo-row oyo-row--no-spacing").find('ul')
    
    if ul_element:
        # Iterate over the li elements within the ul
        for li in ul_element.find_all('li'):
            # Find the a tag within the li
            a_tag = li.find('a')
            
            # Print the link (href) of the a tag
            if a_tag and 'href' in a_tag.attrs:
                print(a_tag['href'])
else:
    print("Element with class 'oyo-row oyo-row--no-spacing' not found.")

# Close the browser
driver.quit()