#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Standard Library Imports
import os
import time

# Web Automation Imports
from selenium import webdriver
from selenium.webdriver.common.by import By

# Data Handling Imports
import pandas as pd

# HTTP Requests Imports
import requests

# Record the start time
start_time = time.time()

# Initialize WebDriver (assuming Chrome)
driver = webdriver.Chrome()

# Open rpachallenge.com
driver.get("https://rpachallenge.com")
driver.maximize_window()

# Locate the download link by class name
download_link = driver.find_element(By.XPATH, "//a[contains(text(),'Download Excel')]")

# Get the URL of the download link
download_url = download_link.get_attribute("href")

# Download the file
response = requests.get(download_url)

# Save the downloaded file
with open("challenge.xlsx", "wb") as file:
    file.write(response.content)

# Load the Excel file into pandas
data = pd.read_excel("challenge.xlsx", header = 0)

driver.find_element(By.XPATH, "//button[contains(text(),'Start')]").click()

for index, record in data.iterrows():
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']").send_keys(record[0])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']").send_keys(record[1])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']").send_keys(record[2])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']").send_keys(record[3])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']").send_keys(record[4])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']").send_keys(record[5])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']").send_keys(record[6])
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()

# Locate the message elements by class name
message1_element = driver.find_element(By.CLASS_NAME, "message1")
message2_element = driver.find_element(By.CLASS_NAME, "message2")

# Extract text from the elements
message1_text = message1_element.text
message2_text = message2_element.text

# Write the text to a text file
with open("output.txt", "w") as file:
    file.write(f"Message 1: {message1_text}\n")
    file.write(f"Message 2: {message2_text}\n")

# Delete the Excel file
os.remove("challenge.xlsx")

# Close the web driver
driver.quit()

# Open the text file
with open("output.txt", "r") as file:
    # Read the contents of the file
    file_contents = file.read()

# Print the contents of the file
print(file_contents)

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")

