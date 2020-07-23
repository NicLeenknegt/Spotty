from urllib.request import Request
import urllib.parse

def set_url(url:str):
    def wrap(f):
        def wrap_w_args(*args):
            new_url:str = url + f(*args)
            print(new_url)
        return wrap_w_args
    return wrap

def add_query_parameters():
    def wrap(f):
        def wrap_w_args(*args):
            parameters = f(*args)
            return urllib.parse.urlencode(parameters)
        return wrap_w_args
    return wrap

def add_headers(headers:dict):
    def wrap(f):
        def wrap_w_args(*args):
            url:str = f()
            req:Request = Request(url);
            for key in headers.keys():
                req.add_header(key, headers[key])
            return req
