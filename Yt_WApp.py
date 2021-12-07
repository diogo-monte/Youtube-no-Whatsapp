from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
mensagens_lista = []

def clicar_e_digitar_msg(mensagem:str):
    chat_box = driver.find_element(By.CLASS_NAME, 'p3_M1')
    sleep(0.5)
    chat_box.click()
    chat_box.send_keys(mensagem)


def apenas_enviar_msg():
    botao_enviar = driver.find_element(By.XPATH, "//span[@data-icon='send']")
    sleep(0.5)
    botao_enviar.click()

def musica_yt(mensagem:str):
    nome_music_yt = '+'.join(mensagem.split())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    link_com_musica = f'https://www.youtube.com/results?search_query={nome_music_yt}'
    driver.get(link_com_musica)
    video = driver.find_element(By.XPATH, "//div[contains(@class,'text-wrapper style-scope ytd-video-renderer')]")
    video.click()
    sleep(1)
    clicar_e_digitar_msg(driver.current_url)
    driver.quit()
    sleep(2.5)
    apenas_enviar_msg()

webdriver.ChromeOptions().add_argument('lang=pt-br')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get(f"https://web.whatsapp.com/")
sleep(30)

while True:
    sleep(0.1)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    emissor = str(soup.find_all('div',class_="copyable-text")).split('data-pre-plain-text="')[1:]
    achar = 'dir="ltr"><span>'
    achar_fim = '</span></span><span'
    for x in emissor:
        if x.find('Diogo') == -1:
            fim_msg = (x.find(achar_fim))
            inicio_msg = (x.find(achar) + len(achar))
            mensagem_chave = x[:x.find(">") - 1] + x[inicio_msg:fim_msg]
            if mensagem_chave not in mensagens_lista:
                mensagens_lista.append(mensagem_chave)
                print(mensagem_chave)
                if x[inicio_msg:fim_msg][:3] == ".yt":
                    musica_yt(x[inicio_msg:fim_msg][3:])
