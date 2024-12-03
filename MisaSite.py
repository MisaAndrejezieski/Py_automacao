import time
import pyautogui
import logging
import requests
import tkinter as tk
from tkinter import messagebox
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
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                logging.info(f"Conectividade com {url} verificada.")
                return True
            else:
                logging.warning(f"Conectividade com {url} falhou. Status code: {response.status_code}")
        except requests.RequestException as e:
            logging.warning(f"Falha ao acessar {url}. Exceção: {e}")
        return False

    async def executar_automacao(self, num_pesquisas=1):
        if await self.verificar_conectividade():
            if self.abrir_edge():
                url = 'https://web.dio.me/articles/programa-em-python-para-automacao-de-pesquisas-no-edge?back=%2Fhome&page=1&order=oldest'
                messagebox.showinfo("Automação Iniciada", "A pesquisa foi iniciada.")
                for _ in range(num_pesquisas):
                    sucesso = await self.acessar_pagina(url)
                    self.resultados.append({'url': url, 'status': 'Concluída' if sucesso else 'Falha'})
                    await asyncio.sleep(5)  # Intervalo entre pesquisas
                    self.limpar_cache_historico()
                self.salvar_resultados()
                logging.info("Automação concluída com sucesso.")
                messagebox.showinfo("Automação Concluída", "A pesquisa foi concluída.")
            else:
                logging.error("Falha ao abrir o navegador.")
                messagebox.showerror("Erro", "Falha ao abrir o navegador.")
        else:
            logging.error("Falha na verificação de conectividade com a internet.")
            messagebox.showerror("Erro", "Falha na verificação de conectividade com a internet.")
        self.fechar_programa()

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

    def limpar_cache_historico(self):
        try:
            pyautogui.hotkey('ctrl', 'shift', 'delete')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(2)
            logging.info("Cache e histórico de navegação limpos.")
        except Exception as e:
            logging.error(f"Erro ao limpar cache e histórico: {e}")

    def fechar_programa(self):
        logging.info("Programa encerrado.")
        os._exit(0)

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
        ttk.Label(self.root, text="Número de Pesquisas:", style='TLabel').pack(pady=10)
        self.num_pesquisas_entry = ttk.Entry(self.root, width=20)
        self.num_pesquisas_entry.pack(pady=5)
        self.num_pesquisas_entry.insert(0, "1")

        # Botão para iniciar a automação
        start_button = ttk.Button(self.root, text="Iniciar Automação", command=self.iniciar_automacao_handler)
        start_button.pack(pady=20)

        # Botão para fechar a aplicação
        close_button = ttk.Button(self.root, text="Fechar", command=self.root.quit, style='Red.TButton')
        close_button.pack(pady=10)

    def iniciar_automacao_handler(self):
        try:
            num_pesquisas = int(self.num_pesquisas_entry.get())
            threading.Thread(target=self.run_automacao, args=(num_pesquisas,)).start()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

    def run_automacao(self, num_pesquisas):
        asyncio.run(self.automacao.executar_automacao(num_pesquisas))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    automacao = Automacao()
    interface = InterfaceGrafica(automacao)
    interface.run()
