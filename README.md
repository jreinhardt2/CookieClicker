# CookieClicker Clickbot
Clickbot for the famous Cookie Clicker Game by orteil. This Clickbot uses the selenium framework to control a Chrome Webbrowser. It clicks repeatedly as fast as your hardware allows on the Cookie to generate income. 
## Setup
You need python3 with installed pip. The only dependency is selenium, so you can either install it with:
``` 
pip3 install selenium 
```
or 
```
pip3 install -r requirements.txt
```
You need Google Chrome Browser for Selenium. If you receive an error concerning the version of your Chrome, you can download
the latest Chromedriver here: https://chromedriver.chromium.org. Just replace it with the provided one. 

## Execution
You can start the script with the following command. Please note that you need a different chromedriver for each platform and if the driver is in the same directory add ./ before the name, e.g. python3 clicker.py "./chromedriver.exe".
``` 
python3 clicker.py "path_to_chromedriver"
```
or if you want to use a virtual environment
``` 
source /env/bin/activate
python3 clicker.py "path_to_chromedriver"
```
