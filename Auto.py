import time
import pyautogui
import random

# Lista de possíveis temas para as pesquisas
temas = [
    "tecnologia", "Rock", "Anime", "James Jayden"
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
    try:
        pyautogui.press('win')
        pyautogui.write('edge')
        pyautogui.press('enter')
        time.sleep(2)  # Aumentar o tempo para garantir que o navegador abra
        pyautogui.write(pesquisa)
        pyautogui.press('enter')
        time.sleep(2)  # Tempo para carregar a página
    except Exception as e:
        pyautogui.alert(f"Erro ao abrir o Edge: {e}")

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
        try:
            pyautogui.hotkey('ctrl', 't')  # Abrir uma nova aba
            pyautogui.write(pesquisa)
            pyautogui.press('enter')
            time.sleep(2)  # Tempo para carregar a página
            pyautogui.hotkey('ctrl', 'w')  # Fechar a aba após a pesquisa
        except Exception as e:
            pyautogui.alert(f"Erro ao realizar a pesquisa: {e}")

# Limpar dados de navegação e cookies
try:
    pyautogui.hotkey('ctrl', 'shift', 'delete')
    time.sleep(2)  # Tempo para abrir a janela de limpeza de dados
    pyautogui.press('enter')  # Confirmar a limpeza dos dados
    time.sleep(2)  # Tempo para concluir a limpeza
except Exception as e:
    pyautogui.alert(f"Erro ao limpar os dados de navegação: {e}")

# Fechar o navegador
try:
    pyautogui.hotkey('alt', 'f4')
except Exception as e:
    pyautogui.alert(f"Erro ao fechar o navegador: {e}")
