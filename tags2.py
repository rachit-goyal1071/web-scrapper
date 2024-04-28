from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Assuming you have a WebDriver set up, for example, ChromeDriver
driver = webdriver.Chrome()

# Load the web page
driver.get("https://www.oyorooms.com/search?location=Goa%2C%20India&city=Goa&searchType=city&coupon=&checkin=28%2F04%2F2024&checkout=29%2F04%2F2024&roomConfig%5B%5D=1&showSearchElements=false&country=india&guests=1&rooms=1&filters%5Bcity_id%5D=10")

# Wait for the page to load and the element to be present
wait = WebDriverWait(driver, 20)  # Increase the timeout to 20 seconds
try:
    project_name_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "HotelListCard-234556")))
    
    # Find all 'a' tags within the md-card-left-owner element
    a_tags = project_name_div.find_elements(By.TAG_NAME, 'a')
    
    if a_tags:
        # Extract and print the link (href) of the first 'a' tag
        print(a_tags[0].get_attribute('href'))
    else:
        print("No 'a' tags found under the md-card-left-owner element.")
except Exception as e:
    print(f"Error: {e}")

# Close the browser
driver.quit()
