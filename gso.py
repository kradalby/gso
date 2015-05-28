#!/usr/bin/env python

from flask import Flask, render_template
from SourceQuery import SourceQuery as q

app = Flask(__name__)

SERVERS = (
    ('z.fap.no', 27015),
    ('z.fap.no', 27016),
    ('z.fap.no', 27017),
    ('z.fap.no', 27024),
    ('z.fap.no', 27028),
    #('z.fap.no', 27029),
)

@app.route('/')
def index():
    servers = []
    for server in SERVERS:
        print(server)
        try:
            s = q(server[0], server[1])
            servers.append({ 
                "info": s.info(),
                "players": s.player()
                })
            
        except Exception, e:
            print(e)
    return render_template('index.html', servers=servers)

if __name__ == '__main__':
    app.debug = True
    app.run()
