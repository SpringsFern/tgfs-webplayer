import logging
from pathlib import Path

import jinja2
import aiohttp_jinja2
from aiohttp import web

from tgfs.app import init_handlers
from . import routes

path = Path(__file__).parent

log = logging.getLogger(__name__)

def init_jinja2(app: web.Application) -> None:
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(path / 'templates')
    )
    log.debug("Jinja2 setup done")

init_handlers.append(init_jinja2)
