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
            attr(style = 'background-image: url(img/taxi.jpg)')
            with div(cls = 'hat'):
                div(s['about']['contacts'][self.language], cls = 'center')
    def body(self):
        # Into 
        with div(cls='full'):
            h1('Расположение')
            div(cls='underline')
            # img(src = 'img/svg/logo-long.svg')
            p('Теннисный клуб "Премьер" расположен в Комсомольском парке, это отличное место для отдыха и релаксации и занятий спортом. Смена надоевшей рабочей или домашней обстановки, физические нагрузки, а также непринужденное общение с другими игроками и тренером, прекрасно способствуют полной психологической разгрузке. Посещая теннисный клуб, каждый раз вы получаете заряд бодрости и энергии на длительное время, укрепляете свое физическое состоянии и совершенствуете мастерство игры в большой теннис. Мы предлагаем максимально комфортные условия для всех желающих научиться играть в большой теннис, а также для всех любителей.')
            div(cls='break')

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

                    
r = Response('contacts')        
r.send()