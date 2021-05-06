import datetime

from pytube import YouTube


def downloader():
    while True:
        url = input("Video linki giriniz: ")
        link = YouTube(url)
        print(link.title)
        print(link.length, 'saniye')

        choise = int(input("1 - İNDİR\n2 - İPTAL\n: "))
        if choise == 1:
            t1 = datetime.datetime.now()
            link.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
            t2 = datetime.datetime.now()
            t3 = t2 - t1
            print("İşlem tamamlandı...")
            print(f"Başlangıç {t1} , Bitiş {t2} , Süre {t3.seconds} saniye sürdü...")
        else:
            break


downloader()
