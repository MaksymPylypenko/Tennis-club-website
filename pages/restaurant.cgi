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
            attr(style = 'background-image: url(img/food.jpg);')
            with div(cls = 'hat'):
                div(s['services']['restaurant'][self.language], cls = 'center')
    def body(self):
         with div(cls='full'):
            p('Информация о ресторане')
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

                    
r = Response('restaurant')        
r.send()