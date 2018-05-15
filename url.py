# coding=utf-8
import sys
import importlib
importlib.reload(sys)

import handlers.index

url = [
    (r'/', handlers.index.IndexHandler),
]