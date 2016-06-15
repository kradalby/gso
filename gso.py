#!/usr/bin/env python3
import logging
import logging.config

from SourceLib.SourceQuery import SourceQuery

from flask import Flask, render_template

from logconf import LOGGING

logging.config.dictConfig(LOGGING)

DEBUG = True

logger = logging.getLogger(__name__)

app = Flask(__name__)

SERVERS = (
    ('z.fap.no', 27015),
    ('z.fap.no', 27016),
    ('z.fap.no', 27017),
    ('z.fap.no', 27024),
    ('z.fap.no', 27028),
    ('z.fap.no', 27029),
)


@app.route('/')
def index():
    servers = []
    for server in SERVERS:
        try:
            s = SourceQuery(server[0], server[1])
            servers.append({
                'info': s.info(),
                'players': s.player()
            })
        except Exception as e:
            logger.error(e)

    return render_template('index.html', servers=servers)

if __name__ == '__main__':
    app.debug = DEBUG
    app.run(port=5001)
