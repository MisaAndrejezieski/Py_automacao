import time
import pyautogui
import random

# Lista de possíveis temas para as pesquisas
temas = [
    "tecnologia", "saúde", "educação", "esportes", "política", "economia", 
    "ciência", "arte", "música", "literatura", "história", "geografia", 
    "filosofia", "psicologia", "sociologia", "antropologia", "astronomia", 
    "biologia", "química", "física", "matemática", "engenharia", "medicina", 
    "direito", "administração", "marketing", "finanças", "arquitetura", 
    "design", "moda", "gastronomia"
]

# Função para gerar uma lista de pesquisas aleatórias
def gerar_pesquisas_aleatorias(n):
    pesquisas = []
    for _ in range(n):
        tema = random.choice(temas)
        pesquisas.append(f"Pesquisa sobre {tema}")
    return pesquisas

# Gerar 31 pesquisas aleatórias
pesquisas = gerar_pesquisas_aleatorias(31)

pyautogui.alert('O código de automação de pesquisa no Edge vai começar....')
pyautogui.PAUSE = 0.5

# Abrindo o Edge e realizando a 1ª pesquisa
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.write(pesquisas[0])
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('ctrl', 't')

# Iniciando o laço de repetição para as pesquisas restantes
for pesquisa in pesquisas[1:]:
    pyautogui.write(pesquisa)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('ctrl', 't')

# Fechar a janela atual com Alt + F4
pyautogui.hotkey('alt', 'f4')

