import requests
from bs4 import BeautifulSoup
from num2words import num2words as nm

class Weather_today:
    def __init__(self):
        self.headers = requests.utils.default_headers()
        self.headers.update(
            {
                'User-Agent': 'My User Agent 1.0',
            }
        )
    def padez(self, num):
        s_a = ['2','3','4']
        s_ov = ['5','6','7','8','9', '0']
        if str(num)[-1] == '1':
            return ' градус '
        elif str(num)[-1] in s_a:
            return ' градуса '
        elif num[-1] in s_ov:
            return ' градусов '
        

    def select_today(self):
        data = list()
        url_today ='https://www.gismeteo.ru/weather-moscow-4368/now/'
        rec = requests.get(url_today, headers=self.headers)
        soup = BeautifulSoup(rec.text, 'html.parser')
        
        temp_True = soup.find('span', class_="unit unit_temperature_c")
        temp_Not_True = soup.find('div', class_="weather-feel")
        state_weather = soup.find('div', class_="now-desc")
        
        str_with_num = temp_Not_True.text[12:-3]
        str_temp_true_with_zn = temp_True.text[0]
        temp_True = str_temp_true_with_zn.replace('-', 'минус ').replace('+', 'плюс ') + nm(temp_True.text, lang='ru') + ' ' +  self.padez(temp_True.text)
        temp_Not_True = (temp_Not_True.text[:13] + nm(str_with_num, lang='ru')  + ' ' +  self.padez(str_with_num)).replace('-', 'минус ').replace('+', 'плюс ')
        
        data.append(temp_True)        
        data.append(temp_Not_True)
        data.append(state_weather.text)
        return data
    
    
    def select_tomorrow(self):
        data = list()
        url_tomorrow = 'https://pogoda.mail.ru/prognoz/moskva/'
        rec = requests.get(url_tomorrow, headers=self.headers)
        soup = BeautifulSoup(rec.text, 'html.parser')
        
        temp = soup.find('div',class_="day__temperature")
        state_w = soup.find('div', class_="day__description")
        temp = temp.text.split()
        for item in temp:
            item
            data.append(item)

        data.append(state_w.text)
        data[0] = data[0].replace('-', 'минус ').replace('+', 'плюс ').replace('°', '').replace(data[0][1:-1],  nm(data[0][1:-1],lang='ru')) + self.padez(data[0][1:-1])
        data[1] = data[1].replace('-', 'минус ').replace('+', 'плюс ').replace('°', '').replace(data[1][1:-1],  nm(data[1][1:-1],lang='ru')) + self.padez(data[1][1:-1])
        
        return data


