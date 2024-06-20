import openpyxl
# from selenium import webdriver
# from selenium.webdriver.common.by import By

planilha_clientes = openpyxl.load_workbook('dados_clientes.xlsx')
pagina_clientes = planilha_clientes['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2,values_only=True):
    nome, valor, cpf, vencimento = linha
    print(nome)
    print(cpf)