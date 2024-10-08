#test_tiktok.py
import yt_dlp

# URL del video de TikTok
url = 'https://www.tiktok.com/@nacionallibertario/video/7376374763670883589?_r=1&_t=8mvLPfR8IqM'

# Opciones para la descarga
ydl_opts = {
    'format': 'mp4',
    'outtmpl': 'video_tiktok.mp4'
}

# Descarga del video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video descargado exitosamente!")
