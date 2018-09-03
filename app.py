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
    ('193.202.115.74', 27121),
    ('193.202.115.74', 27125),
    ('193.202.115.74', 27117),
    ('193.202.115.74', 27123),
    ('193.202.115.74', 27133),
    ('193.202.115.74', 27139),
    ('193.202.115.74', 27127),
    ('193.202.115.74', 27135),
    ('193.202.115.74', 27115),
    ('193.202.115.74', 27131),
    ('193.202.115.74', 27129),
    ('193.202.115.74', 27137),
    ('193.202.115.82', 27117),
    ('193.202.115.82', 27119),
    ('193.202.115.82', 27115),
    ('193.202.115.74', 27143),
    ('193.202.115.74', 27153),
    ('193.202.115.82', 27121),
    ('193.202.115.74', 27145),
)


@app.route('/')
def index():
    servers = []
    for server in SERVERS:
        try:
            s = SourceQuery(server[0], server[1])
            servers.append({
                'server': {
                    'address': server[0],
                    'port': server[1]
                    },
                'info': s.info(),
                'players': s.player()
            })
        except Exception as e:
            print(server)
            logger.error(e)

    return render_template('index.html', servers=servers)

if __name__ == '__main__':
    app.debug = DEBUG
    app.run(port=5001)
