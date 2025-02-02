# Teste Automação para preencher formulário Google Forms
# Passos a serem executados:
# Passo 1 - Acessar o Formulário que queremos preencher ('https://forms.gle/hWfgWJrxvwEDAsiM6')
# Passo 2 - Preencher os campos
# Passo 3 - Clicar no botão de envio das respostas

# Importar as bibliotecas
from selenium import webdriver

# Para o Firefox
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service

# Para o Google Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Criando o navegador e o serviço

# Para o Google Chrome
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico)

# Para o Firefox
# servico = Service(GeckoDriverManager().install())
# navegador = webdriver.Firefox(service=servico)

# Passo 1 - Entrando na página desejada
navegador.get("https://forms.gle/hWfgWJrxvwEDAsiM6")

# Passo 2 - Preencher os campos - identificar os elementos a serem utilizados
navegador.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Teste")
navegador.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("teste@teste.com")
navegador.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys("Teste, 123")

# Passo 3 - Clicar no campo para enviar o formulário que foi preenchido
navegador.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
