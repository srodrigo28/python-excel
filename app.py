import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

planilha_clientes = openpyxl.load_workbook('dados_clientes.xlsx')
pagina_clientes = planilha_clientes['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2,values_only=True):
    nome, valor, cpf, vencimento = linha
    # print(nome)
    driver = webdriver.Chrome()
    driver.get('https://consultcpf-devaprender.netlify.app/')
    sleep(5)
    # driver.find_element(By.ID, 'cpf').send_keys(cpf)
    # pegando o valor do input
    campo_pesquisar = driver.find_element(By.XPATH, "//input[@id='cpfInput']")
    sleep(1)
    # colocando o valor da variavel cpf no input
    campo_pesquisar.send_keys(cpf)
    sleep(1)
    # pegando o botão
    botao_pesquisar = driver.find_element(by.XPATH, "//button[@id='btn btn-custom btn-lg btn-block mt-3']")
    sleep(1)
    # clicando no botão
    botao_pesquisar.click()
    sleep(3)
    # aguardar o resultado da tela web
    status = driver.find_element(by.XPATH, "//span[@id='statusLabel']")

