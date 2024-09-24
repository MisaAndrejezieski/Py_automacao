import time
import pyautogui


#animes =#['Dragonball', 'Naruto', 'One Piece', 'Attack on Titan', 'My Hero Academia', 
        #'Demon Slayer', 'Jujutsu Kaisen', 'Fullmetal Alchemist', 'Death Note', 'Sword Art Online', 
        #'Bleach', 'Fairy Tail', 'Hunter x Hunter', 'Tokyo Ghoul', 'One Punch Man', 'Black Clover', 
        #'Re:Zero', 'Steins;Gate', 'Code Geass', 'Neon Genesis Evangelion', 'Cowboy Bebop', 
        #'Samurai Champloo', 'Gintama', 'Mob Psycho 100', 'The Promised Neverland', 'Vinland Saga', 
        #'Dr. Stone', 'Fire Force', 'Blue Exorcist', 'Soul Eater','The Girl Who Leapt Through Time',
        #'The Melancholy Of Haruhi Suzumiya']
sites = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.wikipedia.org",
    "https://www.amazon.com",
    "https://www.reddit.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.linkedin.com",
    "https://www.netflix.com",
    "https://www.spotify.com",
    "https://www.pinterest.com",
    "https://www.quora.com",
    "https://www.medium.com",
    "https://www.coursera.org",
    "https://www.udemy.com",
    "https://www.khanacademy.org",
    "https://www.canva.com",
    "https://www.dropbox.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.trello.com",
    "https://www.slack.com",
    "https://www.zoom.us",
    "https://www.whatsapp.com",
    "https://www.telegram.org",
    "https://www.bbc.com",
    "https://www.cnn.com",
    "https://www.nytimes.com",
    "https://www.theguardian.com"
]


pyautogui.alert('O código de automação de pesquisa no Edge vai começar....')
pyautogui.PAUSE = 0.5

# Abrindo o edge e realizando 1° pesquisa e atualizando a aba do navegador
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.write('anime one peace')
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('ctrl','t')

# Iniciando o laço de repetição, onde vai se repetir a pesquisa e fechamento da aba até
# passar por toda lista de animes
for anime in sites:
    pyautogui.write(f'anime {anime}')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('ctrl', 't')
    import pyautogui
# Fechar a janela atual com Alt + F4
pyautogui.hotkey('alt', 'f4')
