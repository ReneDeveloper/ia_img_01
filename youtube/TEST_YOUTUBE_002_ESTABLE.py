#TEST_YOUTUBE_002.py


import yt_dlp

# URL del video de Rumble que deseas descargar
#url = 'https://www.youtube.com/watch?v=oT8gw9EXaRQ'
url = 'https://www.youtube.com/watch?v=KLVQWwn-zOM'


salida = 'C:/Users/risilvac/__NO_REPO__'

# Opciones para la descarga
ydl_opts = {
    'format': 'mp4',  # Descargar la mejor calidad disponible
    'outtmpl': 'C:/Users/risilvac/__NO_REPO__/TEST_YOUTUBE_002.%(ext)s',  # Ruta de salida y formato del archivo
}

# Descargar el video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])


