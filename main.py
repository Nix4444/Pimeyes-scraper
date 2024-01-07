from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver
import time
import getProxy

url = "https://pimeyes.com/en"

def upload(url):
    prox = getProxy.fetchsocks5()  #FORMAT = USERNAME:PASS@IP:PORT
    options = {
        'proxy':{
            'http': prox,
            'https':prox,
            'no_proxy': 'localhost,127.0.0.1'
        }
    }
    
    chrome_options = Options()
    #chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    
    driver = webdriver.Chrome(seleniumwire_options=options)
    results = None
    currenturl = None 

    try:
        
        driver.get(url)
        upload_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="hero-section"]/div/div[1]/div/div/div[1]/button[2]'))
        )

        upload_button.click()

        
        file_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=file]'))
        )

        file_input.send_keys('C:\\Users\\Nix\\Desktop\\download.jpg')

        agreement1_xpath = '#app > div.wrapper.mobile-fullscreen-mode.mobile-full-height > div > div > div > div > div > div > div.permissions > div:nth-child(1) > label > input[type=checkbox]'
        agreement2_xpath = '#app > div.wrapper.mobile-fullscreen-mode.mobile-full-height > div > div > div > div > div > div > div.permissions > div:nth-child(2) > label > input[type=checkbox]'
        agreement3_xpath = '#app > div.wrapper.mobile-fullscreen-mode.mobile-full-height > div > div > div > div > div > div > div.permissions > div:nth-child(3) > label > input[type=checkbox]'
        submit_xpath = '#app > div.wrapper.mobile-fullscreen-mode.mobile-full-height > div > div > div > div > div > div > button'

        agreement1button_xpath = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, agreement1_xpath))
        )

        agreement2button_xpath = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, agreement2_xpath))
        )

        agreement3button_xpath = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, agreement3_xpath))
        )
        submitbutton_xpath = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, submit_xpath))
        )
        agreement1button_xpath.click()
        agreement2button_xpath.click()
        agreement3button_xpath.click()
        submitbutton_xpath.click()

        time.sleep(5)  # Adjust the sleep time as needed
        currenturl = driver.current_url
        resultsXPATH = '//*[@id="results"]/div/div/div[3]/div/div/div[1]/div/div[1]/button/div/span/span'
        results = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,resultsXPATH))
        )
        results = results.text
        

    except Exception as e:
        print(f"An exception occurred: {e}")

    finally:
        
        print("Results: ", results)
        print("URL: ", currenturl)
        driver.quit()

def main():
    upload(url)


if __name__ == "__main__":
    main()