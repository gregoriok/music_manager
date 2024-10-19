import yt_dlp

# URL da playlist
url_playlist = "https://www.youtube.com/playlist?list=PLTRU2u_bXJoqk2JDJnu95obvUnJ9UTXmK"

# Caminho para salvar os vídeos
caminho_destino = "C:\musica_gisele"

# Opções de download
ydl_opts = {
    'format': 'bestaudio/best',  # Define para baixar o melhor áudio disponível
    'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',  # Template para salvar arquivos com o título do vídeo
    'noplaylist': False,  # Permite baixar todos os vídeos da playlist
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # Usa FFmpeg para extrair o áudio
        'preferredcodec': 'mp3',  # Define o codec de saída como mp3
        'preferredquality': '192',  # Qualidade do mp3 (192 kbps neste caso)
    }],
}

# Baixa a playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url_playlist])
