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

# Função para gerar uma lista de pesquisas aleatórias sobre um tema
def gerar_pesquisas_sobre_tema(tema, n):
    perguntas = [
        f"O que é {tema}?",
        f"Quais são as últimas novidades em {tema}?",
        f"Como {tema} impacta a sociedade?",
        f"Quais são os principais desafios em {tema}?",
        f"Quem são os principais especialistas em {tema}?"
    ]
    return perguntas[:n]

pyautogui.alert('O código de automação de pesquisa no Edge vai começar....')
pyautogui.PAUSE = 0.5

# Abrindo o Edge
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
time.sleep(2)

# Iniciando o laço de repetição para 7 temas diferentes
for _ in range(7):
    tema = random.choice(temas)
    pesquisas = gerar_pesquisas_sobre_tema(tema, 5)
    
    for pesquisa in pesquisas:
        pyautogui.write(pesquisa)
        pyautogui.press('enter')
        time.sleep(30)
        pyautogui.hotkey('ctrl', 't')
    
    # Fechar a aba atual
    pyautogui.hotkey('ctrl', 'w')


# Fechar o navegador com Alt + F4
pyautogui.hotkey('alt', 'f4')

