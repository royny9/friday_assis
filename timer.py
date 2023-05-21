import data_set_timer as dt_t
import pyglet
import threading as the
import jarvist_speak as js

        
def rasp(str_z):
    list_z = str_z.split()
    if ((list_z[-1] == 'минут') and (len(list_z) == 2)):
        for i in dt_t.data_kr_10.items():
            if list_z[0] == i[0]:
                return i[1] * 60
    elif ((list_z[-1] in dt_t.data_set_podez) and (len(list_z) == 2)):
        for i in dt_t.data_set_one_nine.items():
            if list_z[0] == i[0]:
                return i[1] * 60
    elif ((len(list_z) == 3) and (list_z[-1] in dt_t.data_set_podez)):
        sec_des = list_z[0]
        fst_des = list_z[1]
        for i in dt_t.data_set_one_nine.items():
            if fst_des == i[0]:
                fst_des = i[1]
        for i in dt_t.data_kr_10.items():
            if sec_des == i[0]:
                sec_des = i[1]
        return (sec_des + fst_des) * 60
    elif list_z[-1] == 'секунд':
        if (len(list_z) == 2):
            for i in dt_t.data_kr_10.items():
                if list_z[0] == i[0]:
                    return i[1]
    elif ((list_z[-1] in dt_t.data_set_podez_sec) and (len(list_z) == 2)):
                 for i in dt_t.data_set_one_nine.items():
                    if list_z[0] == i[0]:
                        return i[1]
    elif ((len(list_z) == 3) and (list_z[-1] in dt_t.data_set_podez_sec)):
        sec_des = list_z[0]
        fst_des = list_z[1]
        for i in dt_t.data_set_one_nine.items():
            if fst_des == i[0]:
                fst_des = i[1]
        for i in dt_t.data_kr_10.items():
            if sec_des == i[0]:
                sec_des = i[1]
        return (sec_des + fst_des)
    elif list_z[-1] == 'час':
        for i in dt_t.data_kr_10.items():
            if list_z[0] == i[0]:
                return i[1] * 60**2
    elif ((list_z[-1] in dt_t.data_set_podez_hours) and (len(list_z) == 2)):
        for i in dt_t.data_kr_10.items():
            if list_z[0] == i[0]:
                return i[1] * 60**2
    elif ((len(list_z) == 2) and (list_z[-1] in dt_t.data_set_podez_hours)):
        for i in dt_t.data_set_one_nine.items():
            if list_z[0] == i[0]:
                return i[1] * 60**2
    elif ((len(list_z) == 3) and (list_z[-1] in dt_t.data_set_podez_hours)):
        sec_des = list_z[0]
        fst_des = list_z[1]
        for i in dt_t.data_set_one_nine.items():
            if fst_des == i[0]:
                fst_des = i[1]
        for i in dt_t.data_kr_10.items():
            if sec_des == i[0]:
                sec_des = i[1]
        return (sec_des + fst_des) * 60**2
    
         
def sound_play():            
    sound = pyglet.resource.media(r'ANTONBUDILNIK2.mp3')  
    sound.play()
    pyglet.app.run()            

# def start_async_timer(text):
#     friday = js.speak()
#     friday.va_speak('уже засекла')
#     timer = the.Timer(rasp(text), sound_play)
#     timer.start()


#clear other
def clear_other(text):
    if 'засеки' in text:
        text = text.replace('засеки', '')
    elif 'поставь таймер' in text:
        text = text.replace('поставь таймер', '')
    return text


