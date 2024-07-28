"""selenium coding challenge 1
1. open the chrome/firefox browser
2.Launch the Url:https://www.worldometers.info/world-population/
3.Keep getting the count of:
-Current world population
-Today: Births,Deaths and population growth today
-This Year: Birhts,Deaths,Population growth this year"""

from selenium.webdriver.chrome.webdriver import WebDriver
d={}
li1_=["Today","This year"]
li_by_today_and_this_year=["Births today ","Deaths today ","Population Growth today ","Births this year ","Deaths this year ","Population Growth this year "]
driver=WebDriver()
driver.get("https://www.worldometers.info/world-population/#google_vignette")
driver.maximize_window()
driver.implicitly_wait(20)
driver.execute_script("window.scrollBy(0, 500);")
population_elemnt=driver.find_element('xpath',' //div[@id="maincounter-wrap"]//span[@class="rts-counter"]')
driver.implicitly_wait(20)
d['Total_population']=population_elemnt.text
while(True):
    for i in li1_:
        for j in li_by_today_and_this_year:
            if i.lower() in j:
                today_report_elemnt = f'//div[text()="{i}"]/..//div[text()="{j}"]/following-sibling::div'
                element = driver.find_element('xpath', today_report_elemnt)
                driver.implicitly_wait(20)
                d[j] = element.text

    break
driver.get_screenshot_as_file("a.png")
print(d)

