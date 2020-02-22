import os
import re
from os import environ

# Detect language
def getLanguage():
    msg = ""
    
    language = "tbd"
    supported_languages = ['ru', 'uk', 'en']
    
    # check post 
    GET={}
    args=os.getenv("QUERY_STRING")
    if args is not None:
        args = args.split('&')
        for arg in args: 
            t=arg.split('=')
            if len(t)>1: k,v=arg.split('='); GET[k]=v
            
    if ('lan' in GET and GET['lan'] in supported_languages):
        language = GET['lan']
        msg = "post"
    else:
        # ask cookie
        if 'HTTP_COOKIE' in environ:
            for cookie in environ['HTTP_COOKIE'].split(';'):
                cookie = cookie.strip()
                (key, value) = cookie.split('=', 1)                
                if key == "lan":
                    if value in supported_languages:
                        language = value  
                        msg = "cookie used"
        
        # ask browser
        if language == "tbd":
            if 'HTTP_ACCEPT_LANGUAGE' in environ:
                languages = re.split(",|;", environ['HTTP_ACCEPT_LANGUAGE'])
                for l in languages:
                    if l in supported_languages:
                        language = l
                        msg = "client used"
                        break
            else:
                language = supported_languages[0]
                msg = "default"
    return language