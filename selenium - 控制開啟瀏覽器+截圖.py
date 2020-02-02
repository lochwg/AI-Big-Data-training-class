from selenium import webdriver
urls = [
'https://digitgeek.net/',
'http://angel.net.tw',
'https://www.anaconda.com/',
'https://www.jetbrains.com/pycharm/',        
'https://www.nctu.edu.tw/']

web = webdriver.Chrome()
web.set_window_position(0,0)
web.set_window_size(800,600)
i = 0
for url in urls:
    web.get(url)
    web.save_screenshot("webpage{}.png".format(i))
    i += 1
web.quit()