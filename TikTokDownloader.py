import yt_dlp
import os
import re
import sys
from datetime import datetime
import shutil

VERMELHO = '\033[91m'
RESET = '\033[0m'

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def verificar_url_tiktok(url):
    tiktok_pattern = r"https?://(www\.)?tiktok\.com/.*"
    if re.match(tiktok_pattern, url):
        return True
    else:
        print("URL inválida ou não é um link do TikTok.")
        return False

def criar_diretorio():
    horario_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_diretorio = f"{horario_atual}"
    os.makedirs(nome_diretorio, exist_ok=True)
    return nome_diretorio

def remover_diretorio(diretorio):
    if os.path.exists(diretorio):
        shutil.rmtree(diretorio)

def baixar_video_tiktok(url):
    diretorio = criar_diretorio()
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(diretorio, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'quiet': True,
        'progress_hooks': [progress_bar],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Iniciando o download do vídeo: {url}")
            info = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info)
            print(f"\nDownload concluído! O vídeo foi salvo em: {os.path.abspath(diretorio)}")
    except Exception as e:
        print(f"{VERMELHO}Erro ao baixar o vídeo: {e}{RESET}")
        remover_diretorio(diretorio)

def progress_bar(d):
    if d['status'] == 'downloading':
        progress = d['downloaded_bytes'] / d['total_bytes'] * 100
        sys.stdout.write(f"\r{progress:.2f}%")
        sys.stdout.flush()
    elif d['status'] == 'finished':
        print("\nDownload concluído!")

if __name__ == "__main__":
    url_tiktok = input("Digite a URL do TikTok: ")
    if verificar_url_tiktok(url_tiktok):
        baixar_video_tiktok(url_tiktok)


