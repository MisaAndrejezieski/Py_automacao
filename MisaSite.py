import time
import pyautogui

# Lista de URLs para acessar
urls = [
    'https://web.dio.me/topics/o-que-e-pyautogui?back=%2Ftrack%2Fcoding-the-future-claro-java-spring-boot&order=undefined&page=1&search=&tab=forum&track_id=2e52ad2d-0a3b-4ade-a4ae-17830f528834'
]

pyautogui.alert('O código de automação de pesquisa no Edge vai começar....')
pyautogui.PAUSE = 0.5

# Abrindo o Edge e realizando a primeira pesquisa
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('ctrl', 't')

# Iniciando o laço de repetição para acessar cada URL
for url in urls:
    pyautogui.write(url)
    pyautogui.press('enter')
    time.sleep(10)  # Espera 5 segundos para carregar a página
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('ctrl', 't')

# Fechar a janela atual com Alt + F4
pyautogui.hotkey('alt', 'f4')
