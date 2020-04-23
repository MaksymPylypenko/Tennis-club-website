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
            attr(style = 'background-image: url(img/stringer.jpg);')
            with div(cls = 'hat'):
                div(s['services']['shop'][self.language], cls = 'center')
    def body(self):
         with div(cls='full'):
            p('В клубе есть магазин ,где Вы можете приобрести ракетки, мячи, спортивную одежду для тенниса и другие теннисные акссесуары')
            p('Вы также можете воспльзоватся услугами стрингера для перетяжки ракеток')
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

                    
r = Response('shop')        
r.send()