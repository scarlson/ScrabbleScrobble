from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from google.appengine.api import memcache
import urllib
import cgi
from django.utils import simplejson
import os 


path = os.path.join(os.path.split(__file__)[0], 'dict.txt')

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

def scrabble_word_value(word):
    value = 0
    for char in word:
        value += scrabble_char_value(char)
    return value

def reload_dict():
    file = open(path)
    dict = []
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []
    k = []
    l = []
    m = []
    n = []
    o = []
    p = []
    q = []
    r = []
    s = []
    t = []
    u = []
    v = []
    w = []
    x = []
    y = []
    z = []

    for fi in file:
        while fi[-1] not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            fi = fi[0:-1]
        dict.append(fi)
        if fi[0] == 'a':
            a.append(fi)
        elif fi[0] == 'b':
            b.append(fi)
        elif fi[0] == 'c':
            c.append(fi)
        elif fi[0] == 'd':
            d.append(fi)
        elif fi[0] == 'e':
            e.append(fi)
        elif fi[0] == 'f':
            f.append(fi)
        elif fi[0] == 'g':
            g.append(fi)
        elif fi[0] == 'h':
            h.append(fi)
        elif fi[0] == 'i':
            i.append(fi)
        elif fi[0] == 'j':
            j.append(fi)
        elif fi[0] == 'k':
            k.append(fi)
        elif fi[0] == 'l':
            l.append(fi)
        elif fi[0] == 'm':
            m.append(fi)
        elif fi[0] == 'n':
            n.append(fi)
        elif fi[0] == 'o':
            o.append(fi)
        elif fi[0] == 'p':
            p.append(fi)
        elif fi[0] == 'q':
            q.append(fi)
        elif fi[0] == 'r':
            r.append(fi)
        elif fi[0] == 's':
            s.append(fi)
        elif fi[0] == 't':
            t.append(fi)
        elif fi[0] == 'u':
            u.append(fi)
        elif fi[0] == 'v':
            v.append(fi)
        elif fi[0] == 'w':
            w.append(fi)
        elif fi[0] == 'x':
            x.append(fi)
        elif fi[0] == 'y':
            y.append(fi)
        elif fi[0] == 'z':
            z.append(fi)
    file.close()
    # memcache
    memcache.add('a',a)
    memcache.add('b',b)
    memcache.add('c',c)
    memcache.add('d',d)
    memcache.add('e',e)
    memcache.add('f',f)
    memcache.add('g',g)
    memcache.add('h',h)
    memcache.add('i',i)
    memcache.add('j',j)
    memcache.add('k',k)
    memcache.add('l',l)
    memcache.add('m',m)
    memcache.add('n',n)
    memcache.add('o',o)
    memcache.add('p',p)
    memcache.add('q',q)
    memcache.add('r',r)
    memcache.add('s',s)
    memcache.add('t',t)
    memcache.add('u',u)
    memcache.add('v',v)
    memcache.add('w',w)
    memcache.add('x',x)
    memcache.add('y',y)
    memcache.add('z',z)

def get_dict_from_memcache():
    return memcache.get('a') + memcache.get('b') + memcache.get('c') + memcache.get('d') + memcache.get('e') + memcache.get('f') + memcache.get('g') + memcache.get('h') + memcache.get('i') + memcache.get('j') + memcache.get('k') + memcache.get('l') + memcache.get('m') + memcache.get('n') + memcache.get('o') + memcache.get('p') + memcache.get('q') + memcache.get('r') + memcache.get('s') + memcache.get('t') + memcache.get('u') + memcache.get('v') + memcache.get('w') + memcache.get('x') + memcache.get('y') + memcache.get('z')

try:
    reload_dict()
    dict = get_dict_from_memcache()
except:
    pass

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

class ReloadHandler(BaseRequestHandler):
    def get(self):
        reload_dict()

def findWords(rack="",board=""):
    const = []
    words = []
    word = ""
    wild = rack.count('*')
    wildval = 0

    if len(rack) + len(board) > 2 and board is not None:
        for y in dict:
            if board in y:
                const.append(y)
    else:
        const = dict

    for entry in const:
      if entry != board:
        word = entry
        if len(board) > 0:
            entry = entry.partition(board)[0] + entry.partition(board)[2]
        wildval = 0
        for tile in rack:
            entry = entry.partition(tile)[0] + entry.partition(tile)[2]
        if len(entry) <= wild:
            for char in entry:
                wildval += scrabble_char_value(char)
            words.append(tuple([word,scrabble_word_value(word) - wildval]))


    return words
        
class FetchHandler(BaseRequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json';
        self.response.headers['Access-Control-Allow-Origin'] = '*';
        self.response.headers['Access-Control-Allow-Methods'] = 'GET';
        

        rack = cgi.escape(self.request.get('rack')).lower()
        board = cgi.escape(self.request.get('board')).lower()
        words = []
        try:
            limit = int(cgi.escape(self.request.get('limit')))
        except:
            limit = 20

        
        if len(rack) + len(board) > 2:
            if len(board) > 0:
                for tile in board:
                    words = sorted(words + findWords(rack,tile))
            words = list(set(sorted(words + findWords(rack,board))))
            words = sorted(words, key=lambda words: words[1], reverse=True)
            count = len(words)

        if len(words) < 1:
            if len(rack) + len(board) < 3:
                words = [('3 character minimum','')]
            else:
                count = 'None'
                words = [('Rack: ' + str(rack), 'Board: ' + str(board))]
        
        if len(words) > limit:
            words = words[0:limit]
    
        self.response.out.write(simplejson.dumps({'words':words,'count':count}))
        
class HSHandler(BaseRequestHandler):
    def get(self):
        words = []
        best = []
        score = 0
        for y in dict:
            if len(y) >= 15:
                words.append(y)
        
        for word in words:
            temp = scrabble_char_value(word[0]) + scrabble_char_value(word[1]) + scrabble_char_value(word[2]) + scrabble_char_value(word[3]) + scrabble_char_value(word[4]) + scrabble_char_value(word[5]) + scrabble_char_value(word[6]) + scrabble_char_value(word[7]) + scrabble_char_value(word[8]) + scrabble_char_value(word[9]) + scrabble_char_value(word[10]) + scrabble_char_value(word[11]) + scrabble_char_value(word[12]) + scrabble_char_value(word[13]) + scrabble_char_value(word[14]) + scrabble_char_value(word[4]) + scrabble_char_value(word[10])
            if(temp > score):
                best = [word,temp]
        
        self.response.out.write(simplejson.dumps({'word':best[0],'score':best[1]}))

class FlushCacheHandler(BaseRequestHandler):    
  def get(self):
    memcache.flush_all()
    self.redirect("/")

class MainHandler(BaseRequestHandler):
    def get(self):
        self.generate('index.html', {'asdf':'asdf'})
        
def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/reload', ReloadHandler),
                                          ('/fetch', FetchHandler),
                                          ('/flush', FlushCacheHandler),
                                          ('/hs', HSHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
