#!/home/c/cl80114/pyenv/bin/python3.4

import sys
sys.stderr = sys.stdout # log 
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # utf-8

from util.builder import *
from util.lang import * 
from dominate.util import raw

from util.yamlParser import *
s = getStrings("./strings/default.yaml")  

class Constructor(Constructor):
    def top(self):
        with div(cls = 'header'):
            attr(style = 'background-image: url(img/badminton.jpg);')
            with div(cls = 'hat'):
                div(s['services']['sports'][self.language], cls = 'center')
    def body(self):
         with div(cls='full'):
            p('В нашем клубе теперь можно поиграть в бамбинтон. Аренда тёплой и освещённой площадки всего 100 грн/час. Также есть услуги тренера и аренда инвентаря! ')
            div(cls='break')
            raw('<iframe src="https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2FGRaNiBC%2Fvideos%2F586745461779168%2F&show_text=0&width=560" width="450" height="315" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowTransparency="true" allowFullScreen="true"></iframe>')
            br()
            raw('<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3D380489159370874%26id%3D100022293780525&width=500" width="500" height="783" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowTransparency="true" allow="encrypted-media"></iframe>')
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

                    
r = Response('sports')        
r.send()