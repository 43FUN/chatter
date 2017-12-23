import os
import sys
import argparse

import aiopg.sa
import jinja2
import aiohttp_jinja2
from aiohttp import web
import aiohttp_debugtoolbar
from motor import motor_asyncio

from apps.chatter.routes import setup_routes
import settings


async def init_pg(app):
    app.client = motor_asyncio.AsyncIOMotorClient(settings.MONGO_HOST)
    app.db = app.client[settings.MONGO_DB_NAME]


p = argparse.ArgumentParser()
p.add_argument('--host', required=False)
p.add_argument('--port', required=False, type=int)

opts, args = p.parse_known_args(sys.argv[1:])
host, port = opts.host, opts.port

app = web.Application()
aiohttp_debugtoolbar.setup(app)
app['config'] = {}
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(searchpath=settings.TEMPLATE_PATH))
app.on_startup.append(init_pg)
setup_routes(app)