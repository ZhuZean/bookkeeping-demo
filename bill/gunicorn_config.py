from os import environ as env
import multiprocessing

from helper.utils import string_to_bool


PORT = int(env.get("GUNICORN_PORT", 80))
DEBUG_FLAG = string_to_bool(env.get("GUNICORN_DEBUG_FLAG"))
RELOAD_FLAG = string_to_bool(env.get("GUNICORN_RELOAD_FLAG"))

bind = f':{PORT}'
workers = multiprocessing.cpu_count() * 1
threads = 1 * multiprocessing.cpu_count()
debug = DEBUG_FLAG
reload = RELOAD_FLAG
