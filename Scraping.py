from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import ElementClickInterceptedException

# Configurar el controlador del navegador
driver = webdriver.Chrome()

# Abrir la página web
driver.get("https://www.everyonesinvited.uk/read")
#print(driver.page_source)
# Esperar a que el botón "Load more" esté disponible
wait = WebDriverWait(driver, 20)
load_more_button = driver.find_element(By.XPATH, "//button[contains(@class, 'font-surt bg-DemonicYellow px-6 py-2 rounded-full')]")

# Hacer clic en el botón "Load more" hasta que no haya más información
while load_more_button.is_displayed():
    try:
            
        load_more_button.click()
        sleep(5)
        load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'font-surt bg-DemonicYellow px-6 py-2 rounded-full')]")))
    except ElementClickInterceptedException:
        break

###BEATIFULSOUP
soup = BeautifulSoup(driver.page_source, 'lxml')
content = soup.find_all("p", class_="text-left font-surt")
print(content)
#text = content.find_all('p', class_='text-left font-surt')
with open('text.csv', mode='w', newline='', encoding='utf-8') as outputFile:
    textCSV = csv.writer(outputFile, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
    textCSV.writerow(['Abuse'])
    for x in content:
        textCSV.writerow([x.text])
driver.close()
