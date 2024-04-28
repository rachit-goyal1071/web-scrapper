from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Assuming you have a WebDriver set up, for example, ChromeDriver
driver = webdriver.Chrome()
# Scrape the table data and store it in a DataFrame
table_data = []  # List to store the table data
rows = driver.find_elements(By.XPATH, "//table[@class='gv-datatables display dataTable']/tbody/tr")
for row in rows:
    data = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text for cell in data]
    table_data.append(row_data)

# Create a DataFrame from the table data
df = pd.DataFrame(table_data)

# Save the DataFrame as a CSV file
df.to_csv("table_data.csv", index=False)

# Load the web page
driver.get("https://srip.iitgn.ac.in/portal/projects/")

# Wait for the page to load and the element to be present
wait = WebDriverWait(driver, 10)
project_name_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "gv-datatables display dataTable")))

# Check if the element with the specified class is found
if project_name_div:
    # Find the 'a' tag within the md-card-left-owner element
    a_tag = project_name_div.find_element(By.TAG_NAME, 'td')
    

    print(a_tag)
else:
    print("Element with class 'md-card-left-owner' not found.")

# Close the browser
driver.quit()
