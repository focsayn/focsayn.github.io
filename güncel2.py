import moviepy.editor as mp
from pytube import YouTube
import moviepy.editor as mp

url = input("İndirmek istediğiniz video URL'sini girin: ")
yt = YouTube(url)

print("Başlık: ", yt.title)
print("İzlenme sayısı: ", yt.views)
print("Video süresi: ", yt.length, "saniye")
print("Video değerlendirmesi: ", yt.rating)

print("Kullanılabilir çözünürlükler:")
streams = yt.streams.filter(progressive=True)
for i in range(len(streams)):
    print(f"{i+1}. {streams[i].resolution} ({streams[i].filesize_approx/(1024*1024):.2f} MB)")

res_choice = int(input("İndirmek istediğiniz çözünürlüğü seçin (sayı girin): "))
ys = streams[res_choice-1]

output_path = "D:/yt video"
ys.download(output_path)

print("İndirme tamamlandı!")
download_type = input("Video mu yoksa sadece ses mi indirmek istiyorsunuz? 'v' için video, 'a' için ses girin: ")

if download_type == 'v':
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)
    print(f"Video başarıyla indirildi! Boyutu: {stream.filesize_approx/(1024*1024):.2f} MB")
    
elif download_type == 'a':
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(output_path)
    print(f"Ses dosyası başarıyla indirildi! Boyutu: {audio.filesize_approx/(1024*1024):.2f} MB")
    file_title = audio.title.replace(".", "_")
    mp4_path = f"{output_path}/{file_title}.mp4"
    mp3_path = f"{output_path}/{file_title}.mp3"
    video = mp.AudioFileClip(mp4_path)
    video.write_audiofile(mp3_path)
    video.close()
    print(f"MP3 dönüşümü başarıyla tamamlandı! Dosya: {file_title}.mp3")
    
else:
    print("Geçersiz giriş! 'v' veya 'a' girin.")


