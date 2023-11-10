from gtts import gTTS
import pygame


tts = gTTS('hello how are you')
tts.save('hello.mp3')


def play_mp3(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

play_mp3('hello.mp3')