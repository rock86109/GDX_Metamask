
# pip install webdriver-manager
# pip install playsound
# pip install PyObjC
# pip install beepy

import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import beepy
# os.system('say "Claim!"')
# playsound('file.mp3')

send_keys = ["job", "solar", "celery", "abstract", "seven", "amateur", "people", "setup", "bleak", "speed", "dwarf", "walk"]


chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument("--disable-javascript")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_extension("Metamask3.crx")
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

## Metamask
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password')
driver.get("https://trade.d5.xyz/trade")
# print(len(driver.window_handles))
time.sleep(10)
# driver.switch_to.window(driver.window_handles[1])
# driver.execute_script('''window.open("https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome", "_blank");''')
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
# time.sleep(5)
# driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div/div").click()



# time.sleep(50000)
# time.sleep(5)
# action = ActionChains(driver)#.move_to_element(driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div"))
# action.send_keys(Keys.ENTER).send_keys(Keys.SPACE).perform()
# driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div/div").send_keys(Keys.ARROW_RIGHT)
# driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div/div").send_keys(Keys.SPACE)
# time.sleep(10000)


# driver.get("")
time.sleep(2)
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/button").click()
time.sleep(2)
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div/button[1]").click()
time.sleep(2)

for i in range(1, 13):
    driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[{i}]/div[1]/div/input").send_keys(send_keys[i-1])
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button").click()
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input").send_keys("00000000")
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input").send_keys("00000000")
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input").click()
time.sleep(1)
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button").click()
time.sleep(3)
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/button").click()
time.sleep(3)
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/button").click()
time.sleep(3)
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/button").click() ## Done

# driver.find_element(by=By.XPATH, value="").click()
## Arbitrum Network
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div/div").click()
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[3]/button").click()
time.sleep(2)
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/button").click()
time.sleep(1)
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/section/div/div/div[2]/div/button[2]").click()
time.sleep(1)
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/section/div/div/button[1]").click()
time.sleep(1)
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/section/div[3]/button").click()

## switch back to exchange
driver.switch_to.window(driver.window_handles[0])
driver.refresh()
time.sleep(3)
driver.find_element(by=By.XPATH, value="/html/body/div/article/header/div[2]/article/button").click()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div/div[1]/ul/li[1]/div").click()

time.sleep(5)
driver.switch_to.window(driver.window_handles[2])
#next
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[3]/div[2]/button[2]").click()
time.sleep(1)
# connect
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]").click()


# "job solar celery abstract seven amateur people setup bleak speed dwarf walk"
# discard = input("Place your order and then Enter.")
# driver.minimize_window()
driver.switch_to.window(driver.window_handles[0])
print("Ready to monitor.")
beepy.beep(sound='ready')
while True:
    try:
        text = driver.find_element(by=By.XPATH, value="/html/body/div/article/main/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/button").text
        # text = driver.find_element(by=By.XPATH, value="/html/body/div/article/main/div[1]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/article/article/section[1]/div[1]/div[1]").text # bid
        print(f"text:{text}")
        if text == "領取":
            beepy.beep(sound='ready')
            beepy.beep(sound='ready')
            os.system("osascript -e 'Tell application \"System Events\" to display dialog \""+"領錢啦！！！！"+"\"'")
            discard = input("If claimed and placed a new order, then enter... ")
        driver.refresh()
        time.sleep(10)
        

    except Exception as e:
        driver.refresh()
        time.sleep(10)
        print(e)


## Bid
# "/html/body/div/article/main/div[1]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/article/article/section[3]/div[1]/div[1]"

## Ask
# "/html/body/div/article/main/div[1]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/article/article/section[1]/div[1]/div[1]"

## 取消
# "/html/body/div/article/main/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[8]/button"

## Claim
# "/html/body/div/article/main/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/button"

## import wallet
# /html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/button

