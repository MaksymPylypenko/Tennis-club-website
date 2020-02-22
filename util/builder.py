#!/home/c/cl80114/pyenv/bin/python3.4

import dominate
from dominate.tags import *
from dominate.util import text
from util.yamlParser import *
import sys
sys.stderr = sys.stdout 

s = getStrings("./strings/default.yaml")  
            
class Constructor:
    language = 'ru'
    page = 'home'
    def __init__(self,page,lan):
        self.page = page
        self.language = lan
        
    def render(self):
        a_ = a(cls = 'reset-svg white-svg', id = 'home',__pretty=False)
        with a_:
            if(self.page=='home'):
                attr(href='#')
            else:
                attr(href='home.cgi')
            img(src = 'img/svg/logo.svg')
            text(s['title'][self.language])
                
        doc = dominate.document(title = s['title'][self.language])
        doc['lang'] = self.language
    
        # Head --------------------------------------------------------
        with doc.head:
            meta(name = 'description', content = s['club_description'][self.language])
            meta(name = 'keywords', content = s['key_words'])
            meta(name= 'viewport', content= 'width=device-width, initial-scale=1, minimum-scale=0.5')
            link(rel = 'icon', href = 'img/svg/browser-icon.ico')
            link(rel = 'stylesheet', href = 'https://fonts.googleapis.com/css?family=Roboto:400,500&subset=cyrillic')
            link(rel = 'stylesheet', href = 'styles/default.css?v1.901')
            link(rel = 'stylesheet', href = 'styles/google-places.css?v1.88')
            link(rel = 'stylesheet', href = 'styles/flickity.css')
            link(rel = 'stylesheet', href = 'https://fonts.googleapis.com/icon?family=Material+Icons')
            

        
        with doc:
            #Navigation-------------------------------------------------------
            with div(a_):
                attr(cls = 'navbar')
                div('☰', id = 'navbar-toggle', cls = 'reset-svg white-svg')
                with div(cls = 'navbar-sections'):
                    for section in s['sections']:
                        with div(cls = 'navbar-item'):
                            button(s['sections'][section][self.language], cls = 'item-label white')
                            with div(cls = 'item-content'):
                                for item in s[section]:
                                    a(s[section][item][self.language], href = item+'.cgi')
        
                    with div(cls = 'navbar-item no-padding'):
                        with a(cls = 'item-label reset-svg white-svg', id = 'lang'):
                            img(src = 'img/svg/language.svg')
                        with div(cls = 'item-content lang-content'):
                            a("Eng", href = self.page+'.cgi?lan=en')
                            a("Рус", href = self.page+'.cgi?lan=ru')
                            a("Укр", href = self.page+'.cgi?lan=uk')
            div(cls = 'overlay hidden')
            
            # Content --------------------------------------------------------
            self.top()
            self.body()
            
            # Footer --------------------------------------------------------          
            with div(cls='full'):
                with div(cls='sub-footer'):
                    img(id='map', src='img/svg/map.svg')
                    a(s['path'][self.language],target='_blank', href='https://goo.gl/maps/nUHL2XjdY812', cls='action')
                
                with div(cls='sub-header dark'):
                    with span(cls = 'contact',__pretty=False):
                        img(id="img-left", src = 'img/svg/clock.svg')
                        text('8:00-22:00')
                    span(cls = 'contact',id="fake")
                    with span(cls = 'contact',__pretty=False):
                        img(id="img-left", src = 'img/svg/phone.svg')
                        text('(098) 510-00-01')
                
                with div(cls='footer'):
                    with a(target='_blank', href='https://www.facebook.com/premier2010',__pretty=False):
                        img(cls='social-network',src='img/svg/facebook.svg')
                    with a(target='_blank', href='https://www.instagram.com/premiertennis.club/?fbclid=IwAR3wh2pHc-viuR61N3E3z6PDIrOVxcZCp34vdXYA8D6INIY9SVTrKYwKuuk',__pretty=False):
                        img(cls='social-network',src='img/svg/instagram.svg')
                    with a(target='_blank', href='https://www.youtube.com/channel/UCOppuml3tF_8Fbl6wlkhRBw',__pretty=False):
                        img(cls='social-network',src='img/svg/youtube.svg')
                    p('2010 - 2019 © '+s['title'][self.language])
                        
            # Scripts --------------------------------------------------------     
            script(src = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js')
            script(src = 'js/google-places.js')
            script(src = 'https://maps.googleapis.com/maps/api/js?v=3.exp&key=REPLACE_WITH_A_KEY&signed_in=true&libraries=places')
            script(src = 'js/flickity.pkgd.min.js')
            script(src = 'js/instafeed.min.js')
            script(src = 'js/actions.js?v1.88')
        print(doc)
        
    def top(self):
        pass
               
    def body(self):
        pass
            
#Test = Constructor('home','ru')
#Test.render()