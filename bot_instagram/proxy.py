from selenium import webdriver
PROXY = proxies[0].get_address()
webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    
    "proxyType":"MANUAL",
    
}
driver = webdriver.Chrome(executable_path= r"C:\Users\lante\Desktop\Projects\bot_instagram\chromedriver.exe")
