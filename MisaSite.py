import time
import pyautogui
import logging
import requests
import tkinter as tk
from tkinter import messagebox, PhotoImage
from tkinter import ttk
import threading
import os
import csv
import asyncio

# Configuração de logging
logging.basicConfig(
    filename='automacao_eventos.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

class Automacao:
    def __init__(self):
        self.resultados = []

    def salvar_resultados(self):
        file_exists = os.path.isfile('resultados_pesquisas.csv')
        with open('resultados_pesquisas.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["URL", "Status"])
            for resultado in self.resultados:
                writer.writerow([resultado['url'], resultado['status']])

    async def verificar_conectividade(self):
        url = 'https://web.dio.me/articles/programa-em-python-para-automacao-de-pesquisas-no-edge?back=%2Fhome&page=1&order=oldest'
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                logging.info(f"Conectividade com {url} verificada.")
                return True
        except requests.ConnectionError:
            logging.warning(f"Falha ao acessar {url}.")
        return False

    async def executar_automacao(self):
        if await self.verificar_conectividade():
            if self.abrir_edge():
                url = 'https://web.dio.me/articles/programa-em-python-para-automacao-de-pesquisas-no-edge?back=%2Fhome&page=1&order=oldest'
                sucesso = await self.acessar_pagina(url)
                self.resultados.append({'url': url, 'status': 'Concluída' if sucesso else 'Falha'})
                self.salvar_resultados()
                logging.info("Automação concluída com sucesso.")
            else:
                logging.error("Falha ao abrir o navegador.")
        else:
            logging.error("Falha na verificação de conectividade com a internet.")

    def abrir_edge(self):
        try:
            pyautogui.press('win')
            pyautogui.write('edge')
            pyautogui.press('enter')
            time.sleep(2)
            logging.info("Navegador Edge aberto com sucesso.")
            return True
        except Exception as e:
            logging.error(f"Erro ao abrir o Edge: {e}")
            return False

    async def acessar_pagina(self, url):
        try:
            pyautogui.hotkey('ctrl', 't')
            pyautogui.write(url)
            pyautogui.press('enter')
            time.sleep(10)
            pyautogui.hotkey('ctrl', 'w')
            logging.info(f"Página acessada: {url}")
            return True
        except Exception as e:
            logging.error(f"Falha ao acessar a página: {url}. Erro: {e}")
            return False

class InterfaceGrafica:
    def __init__(self, automacao):
        self.automacao = automacao
        self.root = tk.Tk()
        self.root.title("Automação de Pesquisa")
        self.root.geometry('600x500')
        self.root.configure(bg='#cfffca')
        self.setup_ui()

    def setup_ui(self):
        # Estilos
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', background='#A7D8D7', foreground='#2E4053', font=('Helvetica', 12, 'bold'))
        style.map('TButton', background=[('active', '#80C7C6')])
        style.configure('Red.TButton', background='#F28C8C', foreground='#2E4053', font=('Helvetica', 12, 'bold'))
        style.map('Red.TButton', background=[('active', '#F76C6C')])
        style.configure('TLabel', background='#F3F4F6', foreground='#2E4053', font=('Helvetica', 12))
        style.configure('TEntry', font=('Helvetica', 12), padding=5)

        # Elementos da interface
        ttk.Label(self.root, text="Número de Temas:", style='TLabel').pack(pady=10)
        self.num_temas_entry = ttk.Entry(self.root, width=20)
        self.num_temas_entry.pack(pady=5)
        self.num_temas_entry.insert(0, "6")

        ttk.Label(self.root, text="Número de Perguntas por Tema:", style='TLabel').pack(pady=10)
        self.num_perguntas_entry = ttk.Entry(self.root, width=20)
        self.num_perguntas_entry.pack(pady=5)
        self.num_perguntas_entry.insert(0, "6")

        # Botão para iniciar a automação
        start_button = ttk.Button(self.root, text="Iniciar Automação", command=self.iniciar_automacao_handler)
        start_button.pack(pady=20)

        # Botão para fechar a aplicação
        close_button = ttk.Button(self.root, text="Fechar", command=self.root.quit, style='Red.TButton')
        close_button.pack(pady=10)

    def iniciar_automacao_handler(self):
        threading.Thread(target=self.run_automacao).start()

    def run_automacao(self):
        asyncio.run(self.automacao.executar_automacao())

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    automacao = Automacao()
    interface = InterfaceGrafica(automacao)
    interface.run()
