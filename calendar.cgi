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
            attr(style = 'background-image: url(img/collaboration.jpg); background-position: top')
            with div(cls = 'hat'):
                div(s['events']['calendar'][self.language], cls = 'center')
    def body(self):
         with div(cls='full'):
            a('Календарь фту',href='http://www.ftu.org.ua/?start_date=01.01.2019&end_date=01.01.2022&order_type=DATE&vozr=all&mid=5&action=turnirs_list&search_name=&search_town=%D0%9A%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D1%87%D1%83%D0%BA&option=com_calendar&page=5')
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

                    
r = Response('calendar')        
r.send()