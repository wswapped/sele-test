
from selenc import getContent
url = "https://www.bogotobogo.com/python/Flask/Python_Flask_HelloWorld_App_with_Apache_WSGI_Ubuntu14.php"

def application(environ,start_response):
    status = '200 OK'
    html = getContent(url)
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]
