import num2words as nm
import time as t
import jarvist_speak as js


frdy = js.speak


def only_time():
    data = list()
    hours = t.strftime('%H')
    mint = t.strftime('%M')
    data.append(nm.num2words(hours, lang='ru'))
    data.append(nm.num2words(mint, lang='ru'))
    
    return data 


def DOTW():
    dotw_dict = {
        'Sunday':'воскресение',
        'Monday':'понедельник',
        'Tuesday':'вторник',
        'Wednesday':'среда',
        'Thursday':'четверг',
        'Friday':'пятница',
        'Saturday':'суббота',
    }
    
    dotw = t.strftime('%A')
    for item in dotw_dict.items():
        if item[0] == dotw:
            dotw = item[1]
    
    return dotw 

def month():
    month = t.strftime('%B')
    month_dict = {
        'January':'января',
        'February':'февраля',
        'March':'марта',
        'April':'апреля',
        'May':'майя',
        'June':'июня',
        'July':'июля',
        'August':'августа',
        'September':'сентября',
        'October':'октября',
        'November':'ноября',
        'December':'декабря',
    }
    
    for item in month_dict.items():
        if item[0] == month:
            month = item[1]
    
    return month    

def date_month():
    date_month_dict = {
        '01':'первое','02':'второе','03':'третье',
        '04':'четвертое','05':'пятое','06':'шестое',
        '07':'седьмое','08':'восьмое','09':'девятое',
        '10':'десятое','11':'одинадцатое','12':'двенадцатое',
        '13':'тринадцатое','14':'четырнадцатое','15':'пятьнадцатое',
        '16':'шестнадцатое','17':'семнадцатое','18':'восемнадцатое',
        '19':'девятнадцатое','20':'двадцатое','21':'двадцать первое',
        '22':'двадцать второе','23':'двадцать третье','24':'двадцать четвертое',
        '25':'двадцать пятое','26':'двадцать шестое','27':'жвадцать седьмое',
        '28':'двадцать востьмое','29':'жважцать девятое','30':'тридцатое',
        '31':'тридцать первое'
    }
    day_month = t.strftime('%d')
    
    for item in date_month_dict.items():
        if item[0] == day_month:
            day_month = item[1]
            
    return day_month

def date_and_month_1():
    data = list()   
    data.append(date_month())
    data.append(month())
    return data


def ful_date():
    data = [date_month(), month(),DOTW(), only_time()]
    return data
    
