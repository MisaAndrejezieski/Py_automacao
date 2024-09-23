import time
import pyautogui


animes =['Dragonball', 'Naruto', 'One Piece', 'Attack on Titan', 'My Hero Academia', 
        'Demon Slayer', 'Jujutsu Kaisen', 'Fullmetal Alchemist', 'Death Note', 'Sword Art Online', 
        'Bleach', 'Fairy Tail', 'Hunter x Hunter', 'Tokyo Ghoul', 'One Punch Man', 'Black Clover', 
        'Re:Zero', 'Steins;Gate', 'Code Geass', 'Neon Genesis Evangelion', 'Cowboy Bebop', 
        'Samurai Champloo', 'Gintama', 'Mob Psycho 100', 'The Promised Neverland', 'Vinland Saga', 
        'Dr. Stone', 'Fire Force', 'Blue Exorcist', 'Soul Eater','The Girl Who Leapt Through Time',
        'The Melancholy Of Haruhi Suzumiya']

pyautogui.alert('O código de automação de pesquisa no Edge vai começar....')
pyautogui.PAUSE = 0.5

# Abrindo o edge e realizando 1° pesquisa e atualizando a aba do navegador
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.write('anime one peace')
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('ctrl','t')

# Iniciando o laço de repetição, onde vai se repetir a pesquisa e fechamento da aba até
# passar por toda lista de animes
for anime in animes:
    pyautogui.write(f'anime {anime}')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('ctrl', 't')
    import pyautogui
# Fechar a janela atual com Alt + F4
pyautogui.hotkey('alt', 'f4')
