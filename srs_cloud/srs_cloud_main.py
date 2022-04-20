#!/usr/bin/python
# coding: utf-8

import sys, os, json

os.chdir("/www/server/panel")
sys.path.append("class/")
import public

class srs_cloud_main:
    def __init__(self):
        pass

    def helloworld(self, args):
        return public.returnMsg(True, json.dumps({
            'r0': 100, 'r1': args.born, 'r2': args.category,
        }))
