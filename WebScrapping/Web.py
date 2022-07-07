import selenium as s
from selenium import webdriver
from selenium.webdriver.common.by import By

def Entrar_no_site():
    print("Estabelecendo conexão com o site...")
    navegador = webdriver.Chrome()
    navegador.get("https://satsp.fazenda.sp.gov.br/COMSAT/Account/LoginSSL.aspx?ReturnUrl=/COMSAT")
    navegador.find_element(by=By.XPATH, value='//*[@id="details-button"]').click()
    navegador.find_element(by=By.XPATH, value='/html/body/div/div[3]/p[2]/a').click()
    navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_rbtContabilista"]').click()
    navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_imgCertificado"]').click()

    print("Processando informações...")

def Formata_cnpj():
    cnpj = input("Digite o CNPJ da empresa (Somente números): ")
    milcontra = len(cnpj)
    sem_mil_contra = cnpj[:milcontra - 6]
    mil_contra = cnpj[8:milcontra]

