from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import xlsxwriter as excel

#define o link da pagina que irá abrir
link = 'https://www.saucedemo.com/'
#abre o navegador com o link definido
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(link)

#procura o campo username e o preenche
emailField = '//input[@id="user-name"]'
acharEmailField = driver.find_element(By.XPATH, emailField)
acharEmailField.send_keys('standard_user')
#procura o campo password e o preenche
passwordField = '//input[@id="password"]'
acharpasswordField = driver.find_element(By.XPATH, passwordField)
acharpasswordField.send_keys('secret_sauce')
#pressionar o botão login
loginButton = '//input[@id="login-button"]'
acharloginButton = driver.find_element(By.XPATH, loginButton)
acharloginButton.click()
#pegar o titulo do produto
nomeDosProdutos = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name ']")
precoDosProdutos = driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
col = 1
col2 = 2

workbook = excel.Workbook(r'C:\pasta4\Python\Basic Logon\produtos.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Nome do Produto')
worksheet.write('B1', 'Preço do Produto')

for i in range(len(nomeDosProdutos)):
  produtoNome = nomeDosProdutos[i].text
  produtoPreco = precoDosProdutos[i].text
  print(produtoNome)
  print(produtoPreco)
  worksheet.write(i + 1, 0, produtoNome)
  worksheet.write(i + 1, 1, produtoPreco)

workbook.close()
time.sleep(3)
