# TikTok Video Downloader

Este é um programa simples em Python para baixar vídeos do TikTok usando a biblioteca `yt-dlp`. O projeto oferece uma maneira prática e fácil de baixar vídeos do TikTok para seu computador, criando um diretório com a data e hora do download, e salvando o vídeo nesse diretório.

## Funcionalidades

- Baixar vídeos diretamente do TikTok.
- Criar um diretório com a data e hora do download.
- Baixar o vídeo para o diretório criado.
- Exibir uma barra de progresso durante o download.
- Exibir a mensagem de "Download concluído!" com o diretório onde o vídeo foi salvo.
- Remover o diretório em caso de falha no download.

## Requisitos

Antes de usar o programa, certifique-se de ter o Python instalado em seu sistema.

- Python 3.x
- Biblioteca `yt-dlp`
- Biblioteca `re`
- Biblioteca `os`
- Biblioteca `sys`
- Biblioteca `datetime`
- Biblioteca `shutil`

## Instalação

1. Clone o repositório ou baixe o código-fonte.
   ```bash
   git clone https://github.com/Henry0005/TikTok-Downloader.git
    ```

2. Instale a dependência yt-dlp utilizando o pip:
    ```bash
    pip install yt-dlp
    ```

3. Se tudo foi feito corretamente, o código já deve funcionar perfeitamente.

## Uso

1. Execute o programa
2. Insira a URL do vídeo do TikTok quando solicitado.
3. O programa fará o download do vídeo e o salvará em um diretório com a data e hora do download. Exemplo de saída no terminal:
    ```
    Digite a URL do TikTok: https://www.tiktok.com/@example/video/1234567890
    Iniciando o download do vídeo: https://www.tiktok.com/@example/video/1234567890
    Download concluído! O vídeo foi salvo em: TikTok-Downloader\2025-01-02_05-30-50\
    ```

