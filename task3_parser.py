import time
from typing import Set
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))


list_of_smarts_refs = set()

def get_set_of_smarts_ref(list_of_smarts_refs: Set[str], url: str) -> Set[str]:
    if len(list_of_smarts_refs) == 100:
        return list_of_smarts_refs

    browser.get(url)
    '''Загрузка страницы.'''
    WebDriverWait(browser, timeout=10) \
        .until(lambda b: b.find_element(By.XPATH, '//div[text()=\'Дальше\' and @class=\'ui-f7\']'))
    time.sleep(3)

    '''Ссылка на следующую страницу.'''
    # button_next = next(filter(lambda e: e.text == 'Дальше', browser.find_elements(By.CLASS_NAME, 'ui-f7')))
    button_next = browser.find_element(By.XPATH, '//div[text()=\'Дальше\' and @class=\'ui-f7\']//ancestor::a')
    '''Ищем ссылки на смартфоны на странице.'''
    list_of_href_items_on_page = browser \
        .find_elements(By.XPATH, '//div[@class=\'qk2 q2k\']')

    list_of_smartphones_on_page_aTag = \
        [item.find_element(By.XPATH, './/a[@class=\'tile-hover-target o3k\']') for item in list_of_href_items_on_page \
        if len(item.find_elements(By.XPATH, './/span[text()=\'Тип: \']/font[text()=\'Смартфон\']')) != 0]

    for item in list_of_smartphones_on_page_aTag:
        list_of_smarts_refs.add(item.get_attribute('href').split('?')[0])

    print(f'items_on_page: {len(list_of_href_items_on_page)}')
    print(f'smarts_on_page: {len(list_of_smartphones_on_page_aTag)}')
    print(list_of_smarts_refs)
    # print(button_next.text)
    print(button_next.get_attribute('href'))

    ActionChains(browser) \
        .scroll_by_amount(0, 500) \
        .pause(0.5) \
        .scroll_by_amount(0, -300) \
        .pause(0.5) \
        .scroll_by_amount(0, 300) \
        .pause(0.5) \
        .scroll_by_amount(0, 500) \
        .pause(0.5) \
        .scroll_to_element(button_next) \
        .pause(0.5) \
        .perform()
    time.sleep(0.5)


    button_next_clean_ref = '&'.join(button_next.get_attribute('href').split('&')[:2])
    print(button_next_clean_ref)
    ActionChains(browser)\
        .click(button_next)\
        .perform()
    time.sleep(10)
    # get_set_of_smarts_ref(list_of_smarts_refs, button_next_clean_ref)
    browser.close()
    return list_of_smarts_refs


result = get_set_of_smarts_ref(list_of_smarts_refs, 'https://www.ozon.ru/category/smartfony-15502/?sorting=rating')
print(result)
browser.quit()

if __name__ == '__main__':
    pass
