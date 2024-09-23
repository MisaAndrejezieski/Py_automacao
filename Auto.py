import time
import pyautogui


pyautogui.alert('O código de automação vai começar....')
pyautogui.PAUSE = 0.5 
# Abrindo o edge e realizando 1° pesquisa e atualizando a aba do navegador
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.write('anime one peace')
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl','w')
