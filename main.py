from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import re
import time

driver = webdriver.Chrome('chromedriver')
wait = WebDriverWait(driver, 10)

url = 'https://m.place.naver.com/my/pick'

driver.get(url)

places = driver.find_element_by_css_selector('body')
app_root = driver.find_element_by_id('app-root')

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1qB_gW6tQY')))
driver.find_element_by_class_name('_3uH_7bQln7')
driver.find_element_by_class_name('_2LRJiEXVaS')

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_3VDdKLbreA')))
driver.find_element_by_class_name('_3ne0Y17r_I')
buttons = driver.find_elements_by_class_name('_2jKeGFDxcF._1zaFE15_iG')
print(len(buttons))

post_index = 0
while True:
    print(post_index)
    buttons = driver.find_elements_by_class_name('_2jKeGFDxcF._1zaFE15_iG')
    try:
        button = buttons[post_index]
        if button.is_displayed() and button.is_enabled():
            button.click()
            time.sleep(2)

            # 파일 열기
            f = open("result.txt", 'a')

            # 정보 읽기 - 플레이스 정보
            html = driver.page_source
            place_name = re.findall('B8JgXoFczU">(.*?)</span>', html)
            place_category_address = re.findall('_2OrhaaQqUS">(.*?)</span>', html)
            if len(place_name) > 0 and len(place_category_address) > 1:
                print(place_name[0], '/', place_category_address[0], '/', place_category_address[1])
                f.write(place_name[0] + '/' + place_category_address[0] + '/' + place_category_address[1] + '\n')

            # 정보 읽기 - 이 장소의 리뷰
            html = driver.page_source
            place_section_count = re.findall('place_section_count">(.*?)</span>', html)
            if len(place_section_count) > 0:
                count = int(place_section_count[0].replace(',', ''))
            else:
                count = 0
            # print('이 장소의 리뷰', end=' ')
            # print(count)

            load_count = int(count / 20)
            for i in range(load_count):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)

            html = driver.page_source
            users = re.findall('_10a0wuNKuW">(.*?)</div>', html)
            rates = re.findall('별점</em>(.*?)</span>', html)

            print(users)
            print(rates)

            f.write(users.__str__())
            f.write('\n')
            f.write(rates.__str__())
            f.write('\n')

            f.close()

            # 뒤로 가기
            driver.back()

            post_index = post_index + 1

    except IndexError:
        # 스크롤 내려서 맛집 추가 로딩
        print('scroll down')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)


time.sleep(3)

driver.close()
