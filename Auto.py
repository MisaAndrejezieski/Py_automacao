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

# Função para abrir o Edge e realizar uma pesquisa
def abrir_edge_e_pesquisar(pesquisa):
    pyautogui.press('win')
    pyautogui.write('edge')
    pyautogui.press('enter')
    time.sleep(1)  # Aumentar o tempo para garantir que o navegador abra
    pyautogui.write(pesquisa)
    pyautogui.press('enter')
    time.sleep(1)  # Tempo para carregar a página

# Alerta inicial
pyautogui.alert('O código de automação de pesquisa no Edge vai começar....')
pyautogui.PAUSE = 0.5

# Abrindo o Edge uma vez
abrir_edge_e_pesquisar('')

# Iniciando o laço de repetição para 7 temas diferentes
for _ in range(2):
    tema = random.choice(temas)
    pesquisas = gerar_pesquisas_sobre_tema(tema, 5)
    
    for pesquisa in pesquisas:
        pyautogui.hotkey('ctrl', 't')  # Abrir uma nova aba
        pyautogui.write(pesquisa)
        pyautogui.press('enter')
        time.sleep(1)  # Tempo para carregar a página
        pyautogui.hotkey('ctrl', 'w')  # Fechar a aba após a pesquisa

# Limpar dados de navegação e cookies
pyautogui.hotkey('ctrl', 'shift', 'delete')
time.sleep(1)  # Tempo para abrir a janela de limpeza de dados
pyautogui.press('enter')  # Confirmar a limpeza dos dados

# Fechar o navegador
pyautogui.hotkey('alt', 'f4')

