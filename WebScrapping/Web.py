import time

import selenium as s
from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
sem_mil_contra = ""
mil_contra = ""

def Entrar_no_site():
    print("Estabelecendo conexão com o site...")
    navegador.get("https://satsp.fazenda.sp.gov.br/COMSAT/Account/LoginSSL.aspx?ReturnUrl=/COMSAT")
    navegador.find_element(by=By.XPATH, value='//*[@id="details-button"]').click()
    navegador.find_element(by=By.XPATH, value='/html/body/div/div[3]/p[2]/a').click()
    navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_rbtContabilista"]').click()
    navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_imgCertificado"]').click()

    print("Processando informações...")

def Formata_cnpj():
    cnpj = input("Digite o CNPJ da empresa (Somente números): ")
    global sem_mil_contra
    sem_mil_contra = cnpj[:len(cnpj) - 6]
    global mil_contra
    mil_contra = cnpj[8:len(cnpj)]

def FazerDownload():
    print("Escolhendo a empresa...")
    navegador.get("https://satsp.fazenda.sp.gov.br/COMSAT/Private/Default.aspx")
    navegador.find_element(by=By.XPATH, value = '//*[@id="nav"]/li[5]/a').click()
    navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_txtCNPJ_ContribuinteNro"]').send_keys(sem_mil_contra)
    navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_txtCNPJ_ContribuinteFilial"]').send_keys(mil_contra)
    navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_btnPesquisar"]').click()
    navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_gridCNPJ_lnkCNPJ_0"]').click()
    time.sleep(2)
    navegador.get("https://satsp.fazenda.sp.gov.br/COMSAT/Private/VisualizarEquipamentoSat/VisualizarEquipamentoSAT.aspx")
    navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_ddlSituacao"]').click()
    navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_ddlSituacao"]/option[2]').click()
    navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_btnPesquisar"]').click()
    if navegador.find_element(by=By.XPATH, value='//*[@id="dialog-modal"]'): print("Sem registros na empresa")

