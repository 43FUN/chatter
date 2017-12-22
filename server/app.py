import os
import sys
import argparse

import aiopg.sa
import jinja2
import aiohttp_jinja2
from aiohttp import web
import aiohttp_debugtoolbar

from apps.chatter.routes import setup_routes
import settings


async def init_pg(app):
    engine = await aiopg.sa.create_engine(
        database=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        host='db',
        port='5432',
        loop=app.loop,
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


p = argparse.ArgumentParser()
p.add_argument('--host', required=False)
p.add_argument('--port', required=False, type=int)

opts, args = p.parse_known_args(sys.argv[1:])
host, port, path = opts.host, opts.port, opts.path

app = web.Application()
aiohttp_debugtoolbar.setup(app)
app['config'] = {}
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(searchpath=settings.TEMPLATE_PATH))
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
setup_routes(app)