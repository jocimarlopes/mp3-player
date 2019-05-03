import time
import playsound

time.sleep(1)
print("Player MP3")
time.sleep(1)
print("Em desenvolvimento - Jocimar Lopes")
time.sleep(1)
print("50% [========        ]")
time.sleep(1)
print("100%[================]")

music = input('Qual a musica: ')
playmusic = music + ".mp3"

playsound.playsound(playmusic)