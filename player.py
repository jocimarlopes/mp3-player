import time
import playsound

print("Player MP3")
print("Em desenvolvimento - Jocimar Lopes")
time.sleep(1)
print("-=-"*15)
print("Música na pasta: 01.mp3 (Amor pra Recomeçar - Frejat)")
print("-=-"*15)

print("Como EXEMPLO digite: 01")
music = input('Qual a musica: ')
playmusic = music + ".mp3"

playsound.playsound(playmusic)
print("Fim do sistema")
time.sleep(5)
