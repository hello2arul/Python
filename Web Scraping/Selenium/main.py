from selenium import webdriver

driver_path = "C:\Program Files (x86)\Google\Chrome\chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.amazon.in/AMD-RyzenTM-3200G-RadeonTM-Graphics/dp/B07STGHZK8/ref=sr_1_3?dchild=1&keywords=3200g&qid=1605006685&sr=8-3")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)
driver.close() #closes tab
driver.quit() #closes chrome
