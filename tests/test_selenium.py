from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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
    descriptions = web_browser.find_elements(By.CSS_SELECTOR, '.card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

def test_list_my_pets(web_browser):
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

    # Проверяем, что попали на главную страницу
    assert web_browser.find_element(By.CSS_SELECTOR, 'html > body > div > div > h1').text == "PetFriends"

    # Переходим на страницу моих питомцев
    web_browser.find_element(By.CSS_SELECTOR, "a[href='/my_pets']").click()

    # Проверяем, что находимся на нужной странице
    assert web_browser.find_element(By.CSS_SELECTOR, 'div>h2').text == "Вячеслав"

    # Находим на странице количество питомцев.
    count_my_pets = WebDriverWait(web_browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.\\.col-sm-4.left'))).text
    count_my_pets = int(count_my_pets.split()[2])

    # Получаем список животных
    list_my_pets = WebDriverWait(web_browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody>tr')))

    # Проверяем, что количество животных совпадает
    assert len(list_my_pets) == count_my_pets

    # Находим фото питомцев на странице
    images = WebDriverWait(web_browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr>th>img')))
    count_pets_with_photo = 0

    # Проверяем, что питомцев с фото больше половины
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            count_pets_with_photo += 1

    assert len(list_my_pets) // 2 < count_pets_with_photo

    # Проверяем, что нет питомцев с повяторяющимися именами и одинаковых питомцев.
    pets = set()
    names = set()
    for i in range(len(list_my_pets)):
        pet_i = list_my_pets[i].find_elements(By.CSS_SELECTOR, 'td')
        names.add(pet_i[0].text)
        pets.add((pet_i[0].text, pet_i[1].text, pet_i[2].text))

    assert len(list_my_pets) == len(names)
    assert len(list_my_pets) == len(pets)




