import queue
import sounddevice as sd
import json
import vosk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import words
from metods import * 
from jarvist_speak import *
import threading as thr
from timer import *
import pygame
import time as t


friday = speak()

q = queue.Queue()

device = sd.default.device = (1, 6)
# device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

model = vosk.Model('model_small')
  

def recognize(data, vectoraizer, clf, friday):
    stop = True
    def sound_p():
        for _ in range(1,5):
            if stop:
                pygame.init()
                song = pygame.mixer.Sound('ANTONBUDILNIK0.mp3.mp3')
                clock = pygame.time.Clock()
                song.play()
                clock.tick(60)
                t.sleep(3.5)
            if not stop:
                break
        
        
    trg = words.TRIGGER.intersection(data.split())
    if not trg:
        return 
    
    data.replace(list(trg)[0],'')
    text_vector = vectoraizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    friday.va_speak(answer)
    data = data.replace('пятница','', 1).replace('найди в интернете', '')
    func_name = answer.split()[0] 
    if func_name == 'web_serch':
        web_serch(data)
        friday.va_speak('я поискала в интернете, и открыла что это такое')
    elif func_name == 'start_async_timer':
        print(f'-----------------{data}------------------')
        print(f'-------------------{clear_other(data)}-----------------')
        friday.va_speak('уже засекла')
        timer = thr.Timer(rasp(clear_other(data)), sound_p)
        timer.start()
    if func_name == 'stop_timer':
        stop = False
    else:
        exec(func_name +'()')
        print(answer)


def callback(indata, frames, time, status):
    q.put(bytes(indata))

def main_lisn():
    vectoraizer = CountVectorizer()
    vectors = vectoraizer.fit_transform(list(words.data_set.keys()))
    
    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))
     
    del words.data_set
    
    
    with sd.RawInputStream(samplerate=samplerate,
                        blocksize = 16000, device=device[0],
                            dtype="int16", channels=1,
                            callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectoraizer, clf, friday)


if __name__ == "__main__":
    main_lisn()