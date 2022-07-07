from selenium import webdriver


opetions = webdriver.ChromeOptions()
opetions.add_argument('--headless')
opetions.add_argument('--disable-gpu')

gg = webdriver.Chrome(chrome_options=opetions)
gg.get("https://www.baidu.com/")
gg.find_element_by_id("kw").send_keys("python")
gg.find_element_by_id("su").click()
html = gg.page_source   #获取当前页面的源
print(html)
gg.quit()   #关闭浏览器