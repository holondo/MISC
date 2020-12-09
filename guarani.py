from selenium import webdriver
import selenium

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get("https://www.youtube.com/channel/UC4g3SvOjNCJu5PUrqdrscOg/search?query=CLASE%20DE%20GUARANI%20-%20")
driver.implicitly_wait(50);
#driver.executeScript("window.scrollTo(0, document.body.scrollHeight)")

links = []
names = []
for video in driver.find_elements_by_partial_link_text("CLASE DE "):
    links.append(str(video.get_attribute('href')))
    names.append(video.text)

rep = open('clasesGuarani.txt', 'w+')

for x, y in zip(names, links):
    rep.write(x.replace("CLASE DE GUARANI - ", "") +": " + y + "\n")