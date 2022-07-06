from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import warnings

warnings.filterwarnings('ignore')


def find_names(page):
    '''Поиск названий животных'''

    soup = BeautifulSoup(page, "html.parser")
    all_names = soup.findAll('li')

    arr, count = [], 0
    for i in all_names:
        if '\n' not in i.text and count < 202:
            try:
                arr.append(i.text)
                count += 1
            except:
                pass
    return arr[2:], arr[-1][0]


chromedriver = 'C:\\Users\\Stas\\Desktop\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get(
    'https://ru.m.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83')
time.sleep(1)

all_names = []
while True:
    names, error = find_names(browser.page_source)
    all_names += names
    browser.find_element(By.LINK_TEXT, "Следующая страница").click()

    # выход из цикла, когда перейдет к английскому алфавиту
    if error == 'A':
        break
# Закрытие браузера
browser.close()

# Составление русского алфавита
a = ord('А')
alphabet = [chr(i) for i in range(a, a + 32)]

# Нахождение кол-ва животных на заглавную букву
letters_dict = dict()
for i in all_names:
    if i[0] in alphabet:
        if i[0] not in letters_dict.keys():
            letters_dict[i[0]] = 1
        else:
            letters_dict[i[0]] += 1

# Вывод отсортированного списка
for key, value in sorted(letters_dict.items()):
    print(f'{key} : {value}')
