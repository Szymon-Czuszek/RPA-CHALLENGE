# 🤖 Web Automation Script with Selenium

## 🌟 Introduction
This script automates the process of downloading a file from a website, filling a form with data from an Excel file, submitting the form, and extracting messages from the webpage. It utilizes Selenium for web automation, pandas for data handling, and requests for HTTP requests.

This project automates repetitive web interactions using Selenium.
The script:
- 📥 Downloads an Excel file from a website
- 📊 Reads and processes the file with pandas
- 📝 Fills and submits a form automatically
- 📤 Extracts confirmation messages from the webpage
- 💾 Saves the results into a text file

It’s a simple yet powerful RPA-style automation example built in Python

## ⚙️ Setup and Requirements

Make sure you have Python 3.x installed.

Install the required Python packages using pip:

📦 Install dependencies:

```python
pip install selenium pandas requests
```

🌐 Install the WebDriver for your browser (this script is configured for Chrome).

Make sure you have the appropriate WebDriver installed for your browser. This script is configured for Chrome; you may need to download the corresponding WebDriver for other browsers.

## Usage
Run the script.
```terminal
python RPA-Challenge.py
```

✅ The script will:
1. 🌍 The script will open the specified webpage (https://rpachallenge.com), maximize the window, and locate the download link for an Excel file.
2. ⬇️ It will download the file and save it as challenge.xlsx.
3. 📖 The script will read the Excel file into a pandas DataFrame.
4. 📝 It will then fill out a form on the webpage with data from the Excel file and submit it.
5. 📋 The messages displayed on the webpage after form submission will be extracted.
<br><br> ![Pictures/rpachallenge-complete.png](Pictures/rpachallenge-complete.png)
6. 💾 The messages will be saved to a text file named output.txt.
The Excel file (challenge.xlsx) will be deleted.
The WebDriver instance will be closed.

## Files
RPA-Challenge.py: The Python script containing the automation code.
output.txt: The text file where messages from the webpage are saved.

## Note
Ensure that the WebDriver path is correctly set up in the script (webdriver.Chrome()). Adjust it according to your WebDriver's location if necessary.
The script assumes the presence of specific elements on the webpage (//input[@ng-reflect-name='labelFirstName'], etc.). Make sure these elements exist and their attributes match the script's expectations.

## License
This project is licensed under the [License Name] License - see the LICENSE.md file for details.
