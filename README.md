# InstaCrushBot

## Overview
This project is an **Instagram automation script** written in Python using **Selenium**. The script automates logging into Instagram, finding a specific contact, and sending a message. This tool is meant for educational purposes only and should be used responsibly to comply with Instagram’s terms of service.

## Features
- Automates Instagram login.
- Navigates to the Direct Messages (DMs) section.
- Finds a specific contact and sends a message.
- Includes error handling and waits for elements to load properly.

## Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- **Google Chrome**
- **ChromeDriver** compatible with your version of Chrome
- **Selenium** library

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/sumitrajkumar/InstaCrushBot.git
   cd InstaCrushBot
   ```

2. **Install required Python libraries**:
   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**:
   - Ensure that ChromeDriver matches your version of Chrome. [Download ChromeDriver](https://chromedriver.chromium.org/downloads) and place it in an accessible folder.

## Usage
1. **Update the script**:
   - Replace `sumit_username` and `sumit_password` in the script with your Instagram credentials or use environment variables for added security.
   - Specify the contact name (e.g., `pookie`) and the message you want to send.

2. **Run the script**:
   ```bash
   python instagram_bot.py
   ```

## Important Notes
- **Security**: Avoid hard-coding your Instagram credentials. Use environment variables or a secure method to store and access sensitive information.
- **XPath Selectors**: Instagram's dynamic class names can change frequently. You may need to update the XPaths if elements cannot be located.
- **Usage Compliance**: Ensure that this script is used in accordance with Instagram’s terms of service to avoid account suspension.

## Example Code Snippet
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
service = Service(executable_path='path/to/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://www.instagram.com/')

# Login and navigate to DMs...
```

## Contributing
Feel free to submit pull requests or suggest improvements. Contributions are always welcome!


