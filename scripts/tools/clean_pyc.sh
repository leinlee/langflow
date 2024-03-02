#!/bin/bash

# clean pyc and orig files
find src | grep '\.pyc$' | awk '{print "remove "$0;system("rm -f "$0)}'
find src | grep '\.orig$' | awk '{print "remove "$0;system("rm -f "$0)}'

# three pass to clean empty folders under app
find src -type d -empty | awk '{print "remove empty folder "$0}'
find src -type d -empty -print0 | xargs -0 -I {} /bin/rmdir "{}"
find src -type d -empty | awk '{print "remove empty folder "$0}'
find src -type d -empty -print0 | xargs -0 -I {} /bin/rmdir "{}"
find src -type d -empty | awk '{print "remove empty folder "$0}'
find src -type d -empty -print0 | xargs -0 -I {} /bin/rmdir "{}"

find tests | grep '\.pyc$' | awk '{print "remove "$0;system("rm -f "$0)}'
find tests | grep '\.orig$' | awk '{print "remove "$0;system("rm -f "$0)}'

# one pass to clean folders under tests
find tests -type d -empty | awk '{print "remove empty folder "$0}'
find tests -type d -empty -print0 | xargs -0 -I {} /bin/rmdir "{}"