from selenium import webdriver

gg = webdriver.Chrome()
gg.get("https://search.jd.com/Search?keyword=%E7%94%B5%E8%84%91&enc=utf-8&wq=%E7%94%B5%E8%84%91&pvid=2dd5a7e537cf40b081854b85426123a8")
js = "var q=document.body.scrollTop=100000"
gg.execute_script(js)
