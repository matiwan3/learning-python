# To use the remote WebDriver, you should have the Selenium server running. To run the server, use this command:

# java -jar selenium-server-standalone-2.x.x.jar

# While running the Selenium server, you could see a message looking like this:

# 15:43:07.541 INFO - RemoteWebDriver instances should connect to: http://127.0.0.1:4444/wd/hub

# The above line says that you can use this URL for connecting to the remote WebDriver. Here are some examples:

from selenium import webdriver

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   options=webdriver.ChromeOptions()
)

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   options=webdriver.FirefoxOptions()
)