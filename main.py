from selenium import webdriver

def main():
    driver = webdriver.Firefox(executable_path='/home/user/PycharmProjects/stepik_selenium_avtotest/geckodriver/geckodriver')
    driver.get("http://www.google.by")
    driver.quit()

if __name__ == "__main__":
    main()