import threading as th
import time as t
import pygame


stop = True


def sound_p():
    while stop:
        pygame.init()
        song = pygame.mixer.Sound('ANTONBUDILNIK0.mp3.mp3')
        clock = pygame.time.Clock()
        song.play()
        clock.tick(60)
        t.sleep(3.5)
    
    
# t1 = th.Timer(2, sound_p)
# t1.start()
# t.sleep(10)
# print('end')
# stop = False

