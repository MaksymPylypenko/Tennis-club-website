#!/home/c/cl80114/pyenv/bin/python3.4

import sys
sys.stderr = sys.stdout # log 
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # utf-8

from util.builder import *
from util.lang import * 

from util.yamlParser import *
s = getStrings("./strings/default.yaml")  

class Constructor(Constructor):
    def top(self):
        with div(cls = 'header'):
            attr(style = 'background-image: url(img/tennis.jpg)')
            with div(cls = 'hat'):
                div(s['services']['rental'][self.language], cls = 'center')
    def body(self):
        with div(cls='full'):
            h1('Цены на летний сезон 2019г.')
            with table(id='prices'):
                with tr():
                    th('Корт')
                    th('Время')
                    th('Стоимость')
                with tr():
                    td('Грунтовый корт')
                    td('с 07:00 до 12:00')
                    td('120 грн/час')
                with tr():
                    td('Грунтовый корт')
                    td('с 12:00 до 15:00')
                    td('100 грн/час')
                with tr():
                    td('Грунтовый корт')
                    td('с 15:00 до 21:00')
                    td('150 грн/час')
                with tr():
                    td('Грунтовый корт')
                    td('Выходные')
                    td('150 грн/час')
                with tr():
                    td('Крытый корт')
                    td('с 07:00 до 22:00')
                    td('270 грн/час')
                with tr():
                    td('Ковёр ( бадминтонное поле, площадка для офп)')
                    td('с 07:00 до 22:00')
                    td('100 грн/час')
    

class Response():
    page = 'tbd'
    lang = getLanguage()
    
    def __init__(self,page):
        self.page=page
        
    def send(self):	
        self.headers()
        page = Constructor(self.page,self.lang)
        page.render()   
        
    def headers(self):
        print('Content-type: text/html; charset=utf-8;')
        print("Set-Cookie: lan=%s" % self.lang);
        print('')

                    
r = Response('rental')        
r.send()