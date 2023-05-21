import torch
import sounddevice as sd
import time as t

class speak:
    def __init__(self):
        self.language = 'ru'
        self.model_id = 'ru_v3'
        self.sample_rate = 48000
        self.speaker = 'xenia'
        self.put_accent = True
        self.put_yo = True
        self.device = torch.device('cpu')
            
        self.model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                            model='silero_tts',
                          language=self.language,
                          speaker=self.model_id)
        
        self.model.to(self.device)        


    def va_speak(self, text):
        audio = self.model.apply_tts(text=text+"..",
                                speaker=self.speaker,
                                sample_rate=self.sample_rate,
                                put_accent=self.put_accent,
                                put_yo=self.put_yo)

        sd.play(audio, self.sample_rate * 1.05)
        t.sleep((len(audio) / self.sample_rate) + 0.5)
        sd.stop()

    