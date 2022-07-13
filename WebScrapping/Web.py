import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class CaptadorXML():

    def get_options(self):
        self.options = Options()
        self.options.add_argument('--safebrowsing-disable-download-protection')
        self.options.add_argument("--disable-web-security")
        self.options.accept_insecure_certs = True
        #options.add_argument("--headless")
        return self.options

    pasta = input(str("Digite a pasta para download: "))
    navegador = webdriver.Chrome(options=get_options(self=Options))
    params = {'behavior': 'allow', 'downloadPath': pasta}
    navegador.execute_cdp_cmd('Page.setDownloadBehavior', params)

    def entrar_no_site(self):
        print("Estabelecendo conexão com o site...")
        self.navegador.get("https://satsp.fazenda.sp.gov.br/COMSAT/Account/LoginSSL.aspx?ReturnUrl=/COMSAT")
        self.navegador.find_element(By.XPATH, '//*[@id="conteudo_rbtContabilista"]').click()
        self.navegador.find_element(By.XPATH, '//*[@id="conteudo_imgCertificado"]').click()
    
        print("Processando informações...")
    
    def formata_cnpj(self):
        cnpj = input("Digite o CNPJ da empresa (Somente números): ")
        self.sem_mil_contra = cnpj[:len(cnpj) - 6]
        self.mil_contra = cnpj[8:len(cnpj)]
    
    def navegar_ate_arquivos(self):
        try:
            print("Escolhendo a empresa...")
            dataInicial = input("Data inicial: ")
            dataFinal = input("Data Final: ")
            print("Carregando...")
            url = 'https://satsp.fazenda.sp.gov.br/COMSAT/Private/ConsultarLotesEnviados/PesquisaLotesEnviados.aspx'
            self.navegador.get("https://satsp.fazenda.sp.gov.br/COMSAT/Private/Default.aspx")
            self.navegador.find_element(By.XPATH,  '//*[@id="nav"]/li[5]/a').click()
            self.navegador.find_element(By.XPATH, '//*[@id="conteudo_txtCNPJ_ContribuinteNro"]').send_keys(self.sem_mil_contra)
            self.navegador.find_element(By.XPATH, '//*[@id="conteudo_txtCNPJ_ContribuinteFilial"]').send_keys(self.mil_contra)
            self.navegador.find_element(By.XPATH, '//*[@id="conteudo_btnPesquisar"]').click()
            self.navegador.find_element(By.XPATH, '//*[@id="conteudo_gridCNPJ_lnkCNPJ_0"]').click()
            time.sleep(2)
            self.navegador.get("https://satsp.fazenda.sp.gov.br/COMSAT/Private/VisualizarEquipamentoSat/VisualizarEquipamentoSAT.aspx")
            self.navegador.find_element(By.XPATH, '//*[@id="conteudo_ddlSituacao"]').click()
            self.navegador.find_element(By.XPATH, '//*[@id="conteudo_ddlSituacao"]/option[2]').click()
            self.navegador.find_element(By.XPATH, '//*[@id="conteudo_btnPesquisar"]').click()
            aparelho = self.navegador.find_element(By.XPATH, '//*[@id="conteudo_grvPesquisaEquipamento_lblNumeroSerie_0"]').text
            self.navegador.get('https://satsp.fazenda.sp.gov.br/COMSAT/Private/ConsultarLotesEnviados/PesquisaLotesEnviados.aspx')
            self.navegador.find_element(By.XPATH, '//*[@id="conteudo_txtDataInicio"]').send_keys(dataInicial)
            self.navegador.find_element(By.XPATH, '//*[@id="conteudo_txtDataTermino"]').send_keys(dataFinal)
            self.navegador.find_element(By.XPATH, '//*[@id="conteudo_txtNumeroSerie"]').send_keys(aparelho)
            self.navegador.find_element(By.XPATH, '//*[@id="conteudo_btnPesquisar"]').click()
        except self.navegador.find_element(by=By.XPATH, value='//*[@id="dialog-modal"]'):
            print("Sem registros na empresa ou quantidade de registros muito grande. Tente diminuir o intervalo entre as datas!")
    
    def faz_downloads(self):
        try:
            element = self.navegador.find_elements(By.LINK_TEXT, 'Download')
            item_paginas = self.navegador.find_element(By.XPATH, '//*[@id="conteudo_lblPageCount"]')
            qtd_paginas = int(item_paginas.text)
            item = 0
            print("Baixando...")
            for p in range(qtd_paginas):
                next_button = self.navegador.find_element(By.XPATH, '//*[@id="conteudo_lnkBtnProxima"]')
                for i in range(len(element)):
                    try:
                        arquivos = self.navegador.find_element(By.XPATH, f'//*[@id="conteudo_grvConsultarLotesEnviados_lkbDownloadXml_{item}"]')
                        arquivos.click()
                        time.sleep(1)
                    except:
                        print("Erro! tentando novamente...")
                        time.sleep(2)
                    item+=1
                next_button.click()
                item = 0
                time.sleep(2)
            print("Download concluído")
        except:
            print("Download concluído!")
        #arquivos_disponiveis = p.read_html(navegador.find_element(by=By.XPATH, value='//*[@id="conteudo_grvConsultarLotesEnviados"]').get_attribute('outer.html'))
        #print(arquivos_disponiveis)





