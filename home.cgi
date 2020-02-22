#!/home/c/cl80114/pyenv/bin/python3.4

import sys
sys.stderr = sys.stdout # log 
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # utf-8

from util.builder import *
from util.lang import * 

from util.yamlParser import *
strings_home = getStrings("./strings/home.yaml")  

class Constructor(Constructor):
    def top(self):
        with div(cls='carousel'):
            attr(data_flickity='{ "autoPlay": true }')
            with div(cls='carousel-cell'):
                with div(cls = 'header'):
                    attr(style = 'background-image: url(img/premier.jpg)')
                    with div(cls = 'hat'):
                        div(cls = 'br')
                        div(strings_home['slide1-name'][self.language], cls = 'name')
                        div(strings_home['slide1-details'][self.language], cls = 'desc')
                        a(strings_home['slide1-action'][self.language], href = 'https://www.youtube.com/watch?v=zBQj0iRsDOE', cls = 'action', target='_blank')
            with div(cls='carousel-cell'):
                with div(cls = 'header'):
                    attr(style = 'background-image: url(img/clay.jpg); background-position: bottom')
                    with div(cls = 'hat'):
                        div(cls = 'br')
                        div(strings_home['slide2-name'][self.language], cls = 'name')
                        div(strings_home['slide2-details'][self.language], cls = 'desc')
                        a(strings_home['slide2-action'][self.language], href = '#', cls = 'action')
            with div(cls='carousel-cell'):
                with div(cls = 'header'):
                    attr(style = 'background-image: url(img/learn.jpg); background-position: center')
                    with div(cls = 'hat'):
                        div(cls = 'br')
                        div(strings_home['slide3-name'][self.language], cls = 'name')
                        div(strings_home['slide3-details'][self.language], cls = 'desc')
                        a(strings_home['slide3-action'][self.language], href = '#', cls = 'action')
         
        # Sub header 
        with div(cls = 'sub-header'):
            with span(cls = 'contact',__pretty=False):
                img(src = 'img/svg/clock.svg')
                text('8:00-22:00')
            with span(cls = 'contact',__pretty=False):
                img(src = 'img/svg/place.svg')
                a(s['location'][self.language], href ='https://goo.gl/maps/nUHL2XjdY812')
            with span(cls = 'contact',__pretty=False):
                img(src = 'img/svg/phone.svg')
                text('(098) 510-00-01')
                
    def body(self):
        # Offers
        with div(cls='full dark'):
            h1(strings_home['offers'][self.language])
            div(cls='underline')
            with div(cls='offer'):
                with div(cls='offer-circle yellow'):
                    i('event_available',cls='material-icons inside-circle')
                with div(cls='offer-title',__pretty=False):
                    text(strings_home['offer1-name'][self.language])
                    p(strings_home['offer1-date'][self.language])
                img(src='img/camp-full.jpg')
                p(strings_home['offer1-details'][self.language])
                with div(cls='offer-action'):
                    a(strings_home['more'][self.language], href='https://www.instagram.com/p/BxkbzYjAao_/', cls='light-action', target='_blank')
            with div(cls='offer'):
                with div(cls='offer-circle red'):
                    i('new_releases',cls='material-icons inside-circle')
                with div(cls='offer-title',__pretty=False):
                    text(strings_home['offer2-name'][self.language])
                    p(strings_home['offer2-date'][self.language])
                img(src='img/offer-1.jpg')
                p(strings_home['offer2-details'][self.language])
                with div(cls='offer-action'):
                    a(strings_home['more'][self.language], href='https://www.instagram.com/p/BwW7WTVgrPi/', cls='light-action', target='_blank')

        # What you get 
        with div(cls='full'):
            h1(strings_home['youget-name'][self.language])
            div(cls='underline')
            p(strings_home['youget-details'][self.language])
            with div(cls='cards'):
                with a(cls='card'):
                    img(src='img/svg/layers.svg')
                    p(strings_home['tile-court'][self.language])      
                with a(cls='card'):
                    img(src='img/svg/racket.svg')
                    p(strings_home['tile-learn'][self.language])                  
                with a(cls='card'):
                    img(src='img/svg/high-five.svg')
                    p(strings_home['tile-friends'][self.language])               
                with a(cls='card'):
                    img(src='img/svg/coffee-cup.svg')
                    p(strings_home['tile-chill'][self.language])
                with a(cls='card'):
                    img(src='img/svg/run.svg')
                    p(strings_home['tile-shop'][self.language])  
                    
        # Google reviews --------------------------------------------------------               
        with div(cls='full'):
            h1(strings_home['reviews'][self.language])
            div(cls='underline')
            div(id='google-reviews')
            br()
            a(strings_home['all-reviews'][self.language],cls='gray',href='https://www.google.com/search?q=%D1%82%D0%B5%D0%BD%D0%BD%D0%B8%D1%81%D0%BD%D1%8B%D0%B9+%D0%BA%D0%BB%D1%83%D0%B1+%D0%BF%D1%80%D0%B5%D0%BC%D1%8C%D0%B5%D1%80&oq=%D1%82%D0%B5%D0%BD%D0%BD%D0%B8%D1%81%D0%BD%D1%8B%D0%B9+%D0%BA%D0%BB%D1%83%D0%B1+%D0%BF%D1%80%D0%B5%D0%BC%D1%8C%D0%B5%D1%80+&aqs=chrome..69i57j69i61l3j35i39j0.4292j0j4&sourceid=chrome&ie=UTF-8#lrd=0x40d753410ce3712f:0x94c89a26ad34b80,1,,,', target='_blank')


        # Instagram feed--------------------------------------------------------               
        # with div(cls='full three'):
        #     h1(strings_home['events'][self.language])
        #     div(cls='underline')
        #     div(id='instafeed')
        #     a(strings_home['load-more'][self.language], id='instafeed-load')
        
        div(cls = 'break')
        
class Response():
    page = 'home'
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

                    
r = Response('home')        
r.send()