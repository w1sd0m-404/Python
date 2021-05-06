from youtube_dl import YoutubeDL

downloader = YoutubeDL({"format":"bestaudio"})

while True:
    try:
        print("Mp3 Downloader".center(40,'-'))

        URL = input("Link giriniz: ")
        downloader.extract_info(URL)

    except Exception:
        print("Mp3 indirilemedi")

    finally:
        options = int(input("1 - Tekrar indir\n2 - Çıkış"))

        if options != 1:
            break