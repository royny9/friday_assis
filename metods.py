import os
import webbrowser
import jarvist_speak
from test_weather import Weather_today
import anecdots_data_set
import random as rd
import time as t
from date_and_time import *
from timer import *

friday = jarvist_speak.speak()

##weather##
def weather_today():
    wether = Weather_today()
    data = wether.select_today()
    print(data)
    friday.va_speak(f'сейчас в москве {data[0]}, {data[1]} под цельсию, {data[2]}')
    
def weather_tomorrow():
    wether = Weather_today()
    data = wether.select_tomorrow()
    print(data)
    friday.va_speak(f'завтра в москве днем {data[0]}, ночью {data[1]} под цельсию, {data[2]}')
##coin##
def coin_flip():
    data = ['орел', "решка", "ой, я ее потеряла", 'орел', "решка"]
    random_index = data[rd.randint(0,len(data) - 1)]
    print(random_index)
    if random_index == 'орел':
        friday.va_speak(f'выпал {random_index}')  
        t.sleep(0.01)
        friday.va_speak('повезло, не повезло?')
    elif random_index == "решка":
        friday.va_speak(f'выпала {random_index}')
        t.sleep(0.01)
        friday.va_speak('повезло, не повезло?')
    else:
        friday.va_speak(f'сейчас поищу')
        t.sleep(0.1)
        friday.va_speak(f'{random_index}')
##web##
def web_serch(serch):
    webbrowser.open(f'https://www.google.com/search?q={serch}&oq={serch}&aqs=chrome..69i57j46i433i512j0i433i512j46i433i512j0i433i512j46i512j46i433i512j46i512j46i433i512j46i131i433i512.2471j0j15&sourceid=chrome&ie=UTF-8')

def browser():
    print('сайт открыт')
    webbrowser.open('https://www.google.com/')
    friday.va_speak('все как вы и просили')
    
def serega_pirat():
    webbrowser.open('https://www.youtube.com/watch?v=UfH6bZD6uBk&t=2977s&ab_channel=bebajao')#

##anecdots##
def anecdots():
    data_set = anecdots_data_set.data_set_anecdots
    friday.va_speak(data_set[rd.randint(0,len(data_set) - 1)])    
##power select##
def power_off():
    print('компютер выключен')
    os.system('shutdown /s /t 60')
    
def sleep_mode():
    print('спящий режим включен')
    os.system('shutdown /h ')

##date and time##
def time():
    data = only_time()
    friday.va_speak(f'сейчас {data[0]} часов {data[1]} минуты')

def date():
    data = ful_date()
    friday.va_speak(f'{data[0]} {data[1]}, {data[2]}, {data[3][0]} часов {data[3][1]} минут')

def date_and_month():
    data = date_and_month_1()
    friday.va_speak(f'сегодня {data[0]} {data[1]}')

def date_mon():
    friday.va_speak(f'{date_month()}')
####
def pasive():
    pass

def off():
    exit()





def start_async_timer():
    pass
