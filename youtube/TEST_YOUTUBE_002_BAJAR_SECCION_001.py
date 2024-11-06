#TEST_YOUTUBE_002.py


import yt_dlp

# URL del video de YouTube que deseas descargar
url = 'https://www.youtube.com/watch?v=KLVQWwn-zOM'

# Opciones para la descarga
ydl_opts = {
    'format': 'mp4',  # Descargar la mejor calidad disponible
    'outtmpl': 'C:/Users/risilvac/__NO_REPO__/TEST_YOUTUBE_002.00-01-00_00-01-20.%(ext)s',  # Ruta de salida y formato del archivo
    'download_sections': [
        '00:01:00-00:01:20',  # Descargar entre el minuto 1:00 y el 1:20
    ],
}

# Descargar el video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
