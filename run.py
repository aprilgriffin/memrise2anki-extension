import http.cookiejar, os.path, uuid, sys, datetime, html
import bs4
from anki.media import MediaManager
from aqt import mw
from functools import partial


from . import memrise, oembed

username = ""
password = ""


downloadDirectory = MediaManager(mw.col, None).dir()
cookiefilename = os.path.join(mw.pm.profileFolder(), 'memrise.cookies')
cookiejar = http.cookiejar.MozillaCookieJar(cookiefilename)
memriseService = memrise.Service(downloadDirectory, cookiejar)