import time
import pyautogui

# Lista de URLs para acessar
urls = [
    'https://sites.google.com/view/misa-misa/home',
    'https://sites.google.com/view/deusadoshi/nicole-doshi',
    'https://sites.google.com/view/misa-misa/projetos',
    'https://sites.google.com/view/misa-misa/filmes',
    'https://sites.google.com/view/misa-misa/t-i',
    'https://sites.google.com/view/misa-misa/windows'
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
