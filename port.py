#!/usr/bin/env python
from GentooOperations import GentooOperations
import sys
import json

f = open('config.json', 'r').read()
config = json.loads(f)
gentooOps = GentooOperations()

if sys.argv[1] == "update":
    gentooOps.update()
elif sys.argv[1] == "installDeps":
    gentooOps.installDeps()
elif sys.argv[1] == "regenConfig":
    print 'Regenerating config...1'
    gentooOps.config(config)
