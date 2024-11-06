#TEST_RUMBLE.py

import yt_dlp

# URL del video de Rumble que deseas descargar
url = 'https://rumble.com/v5iaib9-the-democrats-have-fixed-the-election-vote-for-trump-rfk-on-rescuing-americ.html?utm_source=newsletter&utm_medium=email&utm_campaign=Russell%20Brand'
salida = 'C:/Users/risilvac/__NO_REPO__'

# Opciones para la descarga
ydl_opts = {
    'format': 'best',  # Descargar la mejor calidad disponible
    'outtmpl': 'C:/Users/risilvac/__NO_REPO__/TEST.%(ext)s',  # Ruta de salida y formato del archivo
}

# Descargar el video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
