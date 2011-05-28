from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from google.appengine.api import memcache
from google.appengine.ext.webapp.util import run_wsgi_app
import urllib
import cgi
from django.utils import simplejson
import os 
import time
import cProfile
import pstats

try:
    from alpha import a
    from alpha import b
    from alpha import c
    from alpha import d
    from alpha import e
    from alpha import f
    from alpha import g
    from alpha import h
    from alpha import i
    from alpha import j
    from alpha import k
    from alpha import l
    from alpha import m
    from alpha import n
    from alpha import o
    from alpha import p
    from alpha import q
    from alpha import r
    from alpha import s
    from alpha import t
    from alpha import u
    from alpha import v
    from alpha import w
    from alpha import x
    from alpha import y
    from alpha import z
except:
    pass

dic = {}
dic['a'] = a.a
dic['b'] = b.b
dic['c'] = c.c
dic['d'] = d.d
dic['e'] = e.e
dic['f'] = f.f
dic['g'] = g.g
dic['h'] = h.h
dic['i'] = i.i
dic['j'] = j.j
dic['k'] = k.k
dic['l'] = l.l
dic['m'] = m.m
dic['n'] = n.n
dic['o'] = o.o
dic['p'] = p.p
dic['q'] = q.q
dic['r'] = r.r
dic['s'] = s.s
dic['t'] = t.t
dic['u'] = u.u
dic['v'] = v.v
dic['w'] = w.w
dic['x'] = x.x
dic['y'] = y.y
dic['z'] = z.z

def scrabble_char_value(char):
    if char in ['e','a','i','o','n','r','t','l','s','u']:
        return 1
    elif char in ['d','g']:
        return 2
    elif char in ['b','c','m','p']:
        return 3
    elif char in ['f','h','v','w','y']:
        return 4
    elif char in ['k']:
        return 5
    elif char in ['j','x']:
        return 8
    elif char in ['q','z']:
        return 10
    return 0

def word2_char_value(char):
    if char in ['a','e','i','j','o','s','t']:
        return 1
    elif char in ['r','l','n','u']:
        return 2
    elif char in ['d']:
        return 3
    elif char in ['c','g','m','h','p']:
        return 4
    elif char in ['b','f','v','w','y']:
        return 5
    elif char in ['k']:
        return 6
    elif char in ['x']:
        return 8
    elif char in ['q','z']:
        return 10
    return 0

def scrabble_word_value(word):
    return sum(scrabble_char_value(char) for char in word)

def word2_word_value(word):
    return sum(word2_char_value(char) for char in word)

class BaseRequestHandler(webapp.RequestHandler):
  def generate(self, template_name, template_values={}):
    
    # We'll display the user name if available and the URL on all pages
    values = {}
    values.update(template_values)

    # Construct the path to the template
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, 'templates', template_name)

    # Respond to the request by rendering the template
    self.response.out.write(template.render(path, values))

def findWords(rack=None,board=None):
    const = []
    words = []
    word = ""
    wild = rack.count('*')

    if board:
        for char in set(board):
            const += dic[char]
        const = list(set(const))
    else:
        for char in set(rack):
            const += dic[char]
        const = list(set(const))

    for entry in const:
        word = entry
        if board in entry:
            entry = entry.replace(board,"",1)
            adj = 0
        else:
            adj = 1
        
        w = list(entry)
        for tile in rack:
            if tile in w:
                w.remove(tile)
        if len(w) <= wild + adj:
            if wild == 0 and len(w) > 0:
                if w[0] in board:
                    words.append(word)
            else:
                words.append(word)

    words = list(set(words))    
    return words

def val(words=None,source=None):
    if not words:
        return
    values = []
    for word in words:
        if source == 'ws':
            value = word2_word_value(word)
        else:
            value = scrabble_word_value(word)
        values.append(value)
    words = zip(words, values)
    words = sorted(words, key=lambda words: words[1], reverse=True)
    return words

class FetchHandler(BaseRequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json';
        self.response.headers['Access-Control-Allow-Origin'] = '*';
        self.response.headers['Access-Control-Allow-Methods'] = 'GET';
        try:
            rack = cgi.escape(self.request.get('rack')).lower()
        except:
            rack = None
        try:
            board = cgi.escape(self.request.get('board')).lower()
        except:
            board = None
        try:
            source = cgi.escape(self.request.get('source')).lower()
        except:
            source = None
        try:
            limit = int(cgi.escape(self.request.get('limit')))
        except:
            limit = 20

        if not rack and not board:
            self.response.out.write(simplejson.dumps({'words':"Null Strings"}))
        elif not rack and board:
            if len(board) < 3:
                self.response.out.write(simplejson.dumps({'words':"Board length too short."}))
        elif rack and not board:
            if len(rack) < 3:
                self.response.out.write(simplejson.dumps({'words':"Rack length too short."}))
        elif len(rack) + len(board) < 3:
            self.response.out.write(simplejson.dumps({'words':"3 tile minimum."}))
        else:
            start = time.time()
            words = findWords(rack,board)
            count = len(words)

            if len(words) > 0:
                if source == 'ws':
                    words = zip(words, map(word2_word_value, words))
                else:
                    words = zip(words, map(scrabble_word_value, words))
            words = sorted(words, key=lambda words: words[1], reverse=True)
            if len(words) > limit:
                words = words[0:limit]

            elapsed = round(time.time() - start, 3)
            self.response.out.write(simplejson.dumps({'words':words,'count':count,'elapsed':elapsed}))

        

class HSHandler(BaseRequestHandler):
    def get(self):
        cProfile.run('findWords("rstlne","aeiouqwerty")')
        cProfile.run('val(a)')

class FlushCacheHandler(BaseRequestHandler):    
  def get(self):
    memcache.flush_all()
    self.redirect("/")

class MainHandler(BaseRequestHandler):
    def get(self):
        self.generate('index.html', {})
        
def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/fetch', FetchHandler),
                                          ('/flush', FlushCacheHandler),
                                          ('/hs', HSHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
