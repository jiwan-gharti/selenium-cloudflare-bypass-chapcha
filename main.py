# Import necessary modules from the Selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Chrome options to customize the browser's behavior
options = webdriver.ChromeOptions()

# Keep the browser open after the script finishes
options.add_experimental_option("detach", True)

# Exclude switches related to automation
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Disable the usage of the automation extension
options.add_experimental_option('useAutomationExtension', False)

# Disable certain Blink features controlled by automation
options.add_argument("--disable-blink-features=AutomationControlled")

# Disable browser extensions
options.add_argument('--disable-extensions')

# Disable sandbox mode
options.add_argument('--no-sandbox')

# Disable info bars in the browser
options.add_argument('--disable-infobars')

# Disable shared memory usage by the browser
options.add_argument('--disable-dev-shm-usage')

# Disable navigation in the browser side
options.add_argument('--disable-browser-side-navigation')

# Disable GPU acceleration in the browser
options.add_argument('--disable-gpu')

# Automatically open developer tools for tabs
options.add_argument("--auto-open-devtools-for-tabs")

# Initialize the Chrome webdriver with the configured options
driver = webdriver.Chrome(options=options)

# Open a new tab in the browser and navigate to the specified URL
driver.execute_script("window.open('https://www.propertyguru.com.sg', '_blank')")

# Pause execution for 15 seconds to allow the page to load
time.sleep(15)

# Switch the focus of the webdriver to the newly opened tab (index 1)
driver.switch_to.window(driver.window_handles[1])

# Switch the webdriver's focus to the first frame (index 0) within the current context
driver.switch_to.frame(0)

# Find the input element within the specified frame using its XPath and perform a click action
driver.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/label/input').click()
