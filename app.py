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
#pegar o titulo dos produtos
nomeDosProdutos = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name ']")
#pega o preço dos produtos
precoDosProdutos = driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
#criando a planilha no excel para escrever os produtos
workbook = excel.Workbook(r'C:\pasta4\Python\Basic Logon\produtos.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Nome do Produto')
worksheet.write('B1', 'Preço do Produto')
#fazendo um loop sobre cada produto dentro da lista nomeDosProdutos
for i in range(len(nomeDosProdutos)):
  #extrai cada nome de item e valor do item para a variavel
  produtoNome = nomeDosProdutos[i].text
  produtoPreco = precoDosProdutos[i].text
  #para ter visualização se está correto
  print(produtoNome)
  print(produtoPreco)
  #ele escreve na linha+1 na coluna referenciada o nome e o preço do produto
  worksheet.write(i + 1, 0, produtoNome)
  worksheet.write(i + 1, 1, produtoPreco)
#salva o arquivo excel e finaliza
workbook.close()
time.sleep(3)
