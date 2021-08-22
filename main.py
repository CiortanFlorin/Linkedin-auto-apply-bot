from selenium import webdriver
import time
chrome_driver_path = "E:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search?keywords=JavaScript&location=Zona%20metropolitan%C4%83%20Bucure%C8%99ti&geoId=90010080&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
#Loggin
driver.find_element_by_class_name("nav__button-secondary").click()
time.sleep(1)
driver.find_element_by_id("username").send_keys("YOUR EMAIL")
driver.find_element_by_id("password").send_keys("YOUR LINKEDIN PASSWORD")
driver.find_element_by_class_name("btn__primary--large").click()
time.sleep(2)

#Find jobs
job_list = driver.find_elements_by_css_selector(".job-card-container--clickable")

#Apply at jobs
for n in range(len(job_list)):
    job_list[n].click()
    time.sleep(2)
    #Check if there is an easy apply button:
    button_text = driver.find_element_by_css_selector("div.jobs-apply-button--top-card")
    if button_text.text == "Easy Apply":
        button_text.click()
    else:
        driver.back()
        job_list = driver.find_elements_by_css_selector(".job-card-container--clickable")
        continue
    # Check if there is text in phone field
    phone = driver.find_element_by_class_name("fb-single-line-text__input")
    if phone.get_attribute("value") == "":
        phone.send_keys('999999')
    # Submit aplication
    apply_button = driver.find_element_by_css_selector("div.display-flex button")
    if apply_button.text == "Next":
        driver.back()
        job_list = driver.find_elements_by_css_selector(".job-card-container--clickable")
        continue
    submit_button = driver.find_element_by_css_selector("footer button")
    submit_button.click()
    driver.back()
    job_list = driver.find_elements_by_css_selector(".job-card-container--clickable")
    continue

