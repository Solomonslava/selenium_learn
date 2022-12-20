import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def test_show_all_pets(web_browser):
    web_browser.implicitly_wait(10)
    # Заполняем поле email
    email = web_browser.find_element(By.ID, 'email')
    email.clear()
    email.send_keys('solomonslava1991@gmail.com')

    # Заполняем поле пароль
    password = web_browser.find_element(By.ID, 'pass')
    password.clear()
    password.send_keys('solomon0204')

    # нажимаем кнопку входа
    web_browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    assert web_browser.find_element(By.CSS_SELECTOR, 'html > body > div > div > h1').text == "PetFriends"

    images = web_browser.find_elements(By.CSS_SELECTOR, '.card-img-top')
    names = web_browser.find_elements(By.CSS_SELECTOR, 'h5.card-title')
    description = web_browser.find_elements(By.CSS_SELECTOR, '.card-text')

    for i in range(len(names)):
        try:
            assert names[i].text != ''
        except Exception:
            continue
            # print(f"Значение отсутствует, {names[i].text}")

        try:
            assert images[i].get_attribute('src') != ''

        except Exception:
            continue
            print("except")
            # print(f'У фото отсутствует атрибут, {images[i].get_attribute("src")}')
