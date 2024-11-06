import youtube_dl

def progress_hook(d):
    if d['status'] == 'downloading':
        percentage = d['_percent_str']
        print(f"Descargando... {percentage}", end='\r')
    elif d['status'] == 'finished':
        print("\nDescarga completada.")

def descargar_video_youtube(url):
    ydl_opts = {
        'format': 'mp4',
        'progress_hooks': [progress_hook],
    }
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Ocurrió un error durante la descarga: {e}")

if __name__ == "__main__":
    # URL del video de YouTube proporcionado
    url = 'https://www.youtube.com/watch?v=oT8gw9EXaRQ'
    descargar_video_youtube(url)
