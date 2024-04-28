import csv
from bs4 import BeautifulSoup

# Read the file
file_path = "/Users/rachit_goyal/scrapper/file2"
with open(file_path, "r") as file:
    content = file.read()

# Extract the data from the <tbody> tag
soup = BeautifulSoup(content, "html.parser")
tbody = soup.find("tbody")
data = []
for row in tbody.find_all("tr"):
    row_data = [cell.get_text(strip=True) for cell in row.find_all("td")]
    data.append(row_data)

# Save the data in a CSV file
csv_file_path = "/Users/rachit_goyal/scrapper/data.csv"
with open(csv_file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)