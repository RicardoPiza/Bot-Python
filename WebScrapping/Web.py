import time

import selenium as s
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as p

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
    global mil_contra
    sem_mil_contra = cnpj[:len(cnpj) - 6]
    mil_contra = cnpj[8:len(cnpj)]

def NavegarAteArquivos():
    print("Escolhendo a empresa...")
    dataInicial = input("Data inicial: ")
    dataFinal = input("Data Final: ")
    print("Carregando...")
    url = 'https://satsp.fazenda.sp.gov.br/COMSAT/Private/ConsultarLotesEnviados/PesquisaLotesEnviados.aspx'
    navegador.get("https://satsp.fazenda.sp.gov.br/COMSAT/Private/Default.aspx")
    navegador.find_element(By.XPATH,  '//*[@id="nav"]/li[5]/a').click()
    navegador.find_element(By.XPATH, '//*[@id="conteudo_txtCNPJ_ContribuinteNro"]').send_keys(sem_mil_contra)
    navegador.find_element(By.XPATH, '//*[@id="conteudo_txtCNPJ_ContribuinteFilial"]').send_keys(mil_contra)
    navegador.find_element(By.XPATH, '//*[@id="conteudo_btnPesquisar"]').click()
    navegador.find_element(By.XPATH, '//*[@id="conteudo_gridCNPJ_lnkCNPJ_0"]').click()
    time.sleep(2)
    navegador.get("https://satsp.fazenda.sp.gov.br/COMSAT/Private/VisualizarEquipamentoSat/VisualizarEquipamentoSAT.aspx")
    navegador.find_element(By.XPATH, '//*[@id="conteudo_ddlSituacao"]').click()
    navegador.find_element(By.XPATH, '//*[@id="conteudo_ddlSituacao"]/option[2]').click()
    navegador.find_element(By.XPATH, '//*[@id="conteudo_btnPesquisar"]').click()
    aparelho = navegador.find_element(By.XPATH, '//*[@id="conteudo_grvPesquisaEquipamento_lblNumeroSerie_0"]').text
    navegador.get('https://satsp.fazenda.sp.gov.br/COMSAT/Private/ConsultarLotesEnviados/PesquisaLotesEnviados.aspx')
    navegador.find_element(By.XPATH, '//*[@id="conteudo_txtDataInicio"]').send_keys(dataInicial)
    navegador.find_element(By.XPATH, '//*[@id="conteudo_txtDataTermino"]').send_keys(dataFinal)
    navegador.find_element(By.XPATH, '//*[@id="conteudo_txtNumeroSerie"]').send_keys(aparelho)
    navegador.find_element(By.XPATH, '//*[@id="conteudo_btnPesquisar"]').click()

def FazDownloads():
    pasta = input("Escolha a pasta que quer salvar (caminho): ")
    options = webdriver.ChromeOptions
    preferences = {"download.default_directory": pasta}
    options.add_experimental_option("prefs", preferences)
    navegador = webdriver.Chrome(chrome_options=options)
    arquivos = navegador.find_element(By.XPATH, '//*[@id="conteudo_grvConsultarLotesEnviados_lkbDownloadXml_0"]')
    while arquivos:
        arquivos.click()

    #arquivos_disponiveis = p.read_html(navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_grvConsultarLotesEnviados"]').get_attribute('outer.html'))
    #print(arquivos_disponiveis)


    if navegador.find_element(by=By.XPATH, value='//*[@id="dialog-modal"]'):
        print("Sem registros na empresa ou quantidade de registros muito grande. Tente diminuir o intervalo entre as datas!")
    else:
        print("Download Completo")


