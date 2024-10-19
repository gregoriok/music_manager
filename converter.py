import os
from moviepy.editor import AudioFileClip

# Caminho da pasta com os arquivos .webm
caminho_pasta_origem = 'C:\musicas'

# Caminho da nova pasta onde os arquivos .mp3 serão salvos
caminho_pasta_destino = 'C:\musica_amadeu'

# Verifica se o caminho de origem existe
if not os.path.exists(caminho_pasta_origem):
    raise ValueError("Caminho da pasta de origem não encontrado!")

# Cria a nova pasta de destino, se ela ainda não existir
if not os.path.exists(caminho_pasta_destino):
    os.makedirs(caminho_pasta_destino)

# Lista todos os arquivos da pasta de origem
arquivos = os.listdir(caminho_pasta_origem)

# Filtra apenas arquivos .webm
arquivos_webm = [arquivo for arquivo in arquivos if arquivo.endswith('.webm')]

# Itera sobre os arquivos .webm e converte para .mp3
for arquivo_webm in arquivos_webm:
    caminho_completo_origem = os.path.join(caminho_pasta_origem, arquivo_webm)
    
    # Cria o objeto de áudio
    clip = AudioFileClip(caminho_completo_origem)
    
    # Define o nome do arquivo .mp3
    nome_mp3 = os.path.splitext(arquivo_webm)[0] + '.mp3'
    caminho_completo_destino = os.path.join(caminho_pasta_destino, nome_mp3)
    
    # Escreve o arquivo convertido como .mp3 na nova pasta
    clip.write_audiofile(caminho_completo_destino)

    # Fecha o arquivo para liberar memória
    clip.close()

print("Conversão concluída! Arquivos salvos na nova pasta.")
