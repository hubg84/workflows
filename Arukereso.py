from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://arukereso.hu")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
accept_btn = wait.until(EC.element_to_be_clickable(
    driver.find_element(By.CSS_SELECTOR,'button[id="didomi-notice-agree-button"]'))) # cookie accept
accept_btn.click()
Search_bar =wait.until(EC.visibility_of_element_located ((By.CSS_SELECTOR,'input[type="search"]')))
Search_bar.send_keys('Samsung QE43Q7FAAU')
submit_btn = wait.until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR,  'button[type="submit"]')))
submit_btn.click()

with open("urls.txt", 'w', encoding='utf-8') as f:
    f.write(driver.current_url)


driver.quit()
