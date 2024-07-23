# Selenium Wallet Connection Automation Script to get data from the user page  

This repository contains a Python script that automates the process of connecting a wallet (specifically MetaMask) to the Brahma. fi console application using Selenium WebDriver. It also navigates to the "UI - Testing Console" section and verifies the dashboard status.  

## Table of Contents  

- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Script Overview](#script-overview)  
 
## Prerequisites  

Before running the script, ensure you have:  

- Python (version 3.7 or higher) installed on your machine.  
- Google Chrome browser installed on your machine.  
- ChromeDriver installed and the path set correctly, or the ChromeDriver binary in your working directory.  
- The following Python packages are installed via pip:  

  ```bash  
  pip install selenium
  
## Installation
Clone this repository to your local machine:

git clone <repository-url>  
Navigate to the project directory:

cd <repository-directory>  
Make sure you have the required packages installed as mentioned in the prerequisites.

## Usage

Ensure that your MetaMask wallet is set up and unlocked in your Chrome browser.

Run the script using Python:

python wallet_connection_script.py  
The script will:

Open the Brahma.fi console application.
Click on "Connect Wallet" and interact with the MetaMask extension.
Attempt to sign a message.
Navigate to the "UI - Testing Console".
Verify the dashboard title and take a screenshot.
Assert that the displayed balance is "$0.00".
After the script finishes execution, a screenshot (dashboard_screenshot.png) will be saved in the same directory.

## Script Overview

WebDriver Setup: Initializes the Chrome WebDriver and sets a wait time.
Wallet Connection: Handles wallet connection via MetaMask modal popups.
Error Handling: Catches any issues during wallet connection and continues with subsequent tasks.
Page Navigation: Clicks on the necessary links to navigate to the "UI - Testing Console".
Assertions:
Verifies the title of the dashboard.
Check that the user balance is displayed as "$0.00".
Screenshots: Takes a screenshot of the dashboard.


  
