from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_website_content(url):
    

    # Set up Chrome options for running in headless mode
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the specified URL
        driver.get(url)
        # Wait for the page to load (you may need to adjust the sleep time based on the page)
        driver.implicitly_wait(2)
        driver.execute_script("""
    document.addEventListener('click', function(evt) {
      if (evt.target.type === 'file')
        evt.preventDefault();
    }, true)
    """)

        # Find and click the upload button using XPath
        uploadbutton_xpath = '//*[@id="hero-section"]/div/div[1]/div/div/div[1]/button[2]'
        upload_button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, uploadbutton_xpath))
        )
        #upload_button = driver.find_element("Xpath",uploadbutton_xpath)
        upload_button.click()

        files_xpath = '//*[@id="app"]/div[3]/div/div/div/div/div/div[3]/div'
        files_xpath_button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, files_xpath))
        )
        files_xpath_button.click()
        driver.find_element("css selector",'input[type=file]').send_keys('/Users/nix/Downloads/download.jpeg')
        time.sleep(2)

        agreement1_xpath = '//*[@id="app"]/div[3]/div/div/div/div/div/div/div[5]/div[1]/label/input'
        agreement2_xpath = '//*[@id="app"]/div[3]/div/div/div/div/div/div/div[5]/div[2]/label/input'
        agreement3_xpath = '//*[@id="app"]/div[3]/div/div/div/div/div/div/div[5]/div[3]/label/input'
        submit_xpath = '//*[@id="app"]/div[3]/div/div/div/div/div/div/button'
        
        agreement1button_xpath = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, agreement1_xpath))
        )
        
        agreement2button_xpath = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, agreement2_xpath))
        )
        
        agreement3button_xpath = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, agreement3_xpath))
        )
        submitbutton_xpath = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, submit_xpath))
        )
        agreement1button_xpath.click()
        agreement2button_xpath.click()
        agreement3button_xpath.click()
        submitbutton_xpath.click()

        time.sleep(500)


        

        # Wait for some time or perform further actions as needed

        # Get the updated page content
        updated_page_content = driver.page_source

        return updated_page_content

    finally:
        # Close the browser window
        driver.quit()

# Example usage
url_to_visit = "https://pimeyes.com/en"
get_website_content(url_to_visit)
