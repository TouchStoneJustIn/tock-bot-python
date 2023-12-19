import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth

options = webdriver.ChromeOptions()

options.add_argument('--headless=new')
options.add_argument('--ignore-certificate-errors')
# options.headless = True  # newly added
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("start-maximized")
# Create a WebDriver instance
# driver = webdriver.Chrome(options=options)  # Change this to the appropriate WebDriver instance
with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver:
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
    # Navigate to a webpage
    driver.get("https://www.exploretock.com/login?continue=%2Fthedabney")

    # Use XPath to locate elements
    try:
        while True:
            try:
                email = driver.find_element("xpath", "//input[contains(@id, 'email')]")
                email.clear()
                email.send_keys("andresonethan027@skiff.com")
                # time.sleep(random() * 10)
                pwd = driver.find_element("xpath", "//input[contains(@id, 'password')]")
                pwd.clear()
                pwd.send_keys("PICpic123!@#")
                # time.sleep(random() * 10)
                driver.find_element("xpath", "//button[contains(@type, 'submit')]").click()
                time.sleep(1)
                break
            except Exception as e:
                print("Failed to input email and password input")
                time.sleep(1)
        print("Successfully login!")
        # go to dine-in restaurant
        while True:
            try:
                books = driver.find_elements("xpath", "//div[contains(@class, 'Consumer-reservationCallToAction')]/a")
                print(len(books))
                if(len(books) <= 0):
                    time.sleep(1)
                    continue
                
                for book in books:
                    if(book.text == 'Book now'):
                        book.click()
                        isSuccess = False
                        while True:
                            try:                            
                                soldout = driver.find_elements("xpath", "//div[contains(@class, 'Consumer-resultsListItem is-disabled is-sold-out Consumer-resultsListItem--wide')]")
                                print(len(soldout))
                                if(len(soldout) <= 0):
                                    time.sleep(1)
                                    continue

                                try:
                                    booknow = driver.find_element("xpath", "//button[contains(@class, 'Consumer-resultsListItem is-available Consumer-resultsListItem--wide')]")
                                    print(booknow)
                                    booknow.click()
                                    isSuccess = True
                                    break
                                except Exception as e:
                                    print(e)
                                    break

                            except Exception as e:
                                print(e)
                                time.sleep(1)
                        if(not isSuccess):
                            continue

                        while True:
                            try:
                                driver.find_element("xpath", "//button[contains(@type, 'submit')]").click()
                                break
                            except Exception as e:
                                print(e)
                                time.sleep(1)             

                    # print(book.text)
                break
            except Exception as e:
                print("Failed to get reservation list", e)
                time.sleep(1)
        
        time.sleep(200)
    except Exception as e:
        print(e)

# Close the WebDriver instance
# driver.quit()