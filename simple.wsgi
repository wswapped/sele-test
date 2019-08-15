import sys
import json
from os.path import dirname
import unicodedata

sys.path.append(dirname(__file__))
from cgi import parse_qs, escape

from selenc import getContent

def application(environ,start_response):
    #url = "https://uplus.rw/scripts/browser_automation/imbwa.html"	    

    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    req = json.loads(request_body)

    url = req['link']
    sys.stderr.write(str(url))
    sys.stderr.write('done bro')
    #sys.exit()
    status = '200 OK'
    unicodedata.normalize('NFKD', url).encode('ascii','ignore')
    html = getContent(url)
    unicodedata.normalize('NFKD', html).encode('ascii','ignore')
    #sys.stderr.write(html)
    html = html.encode("utf-8")    
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]
