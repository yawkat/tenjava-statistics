#!/usr/bin/env python

import json
import os
import urllib2
import re

def load_page(page):
    return json.load(urllib2.urlopen("https://api.github.com/users/tenjava/repos?page=" + str(page)))

def list_repos():
    i = 1
    while True:
        page = load_page(i)
        if len(page) is 0:
            break
        for entry in page:
            yield entry["name"]
        i += 1

# regex for participant repos (abc-t1)
repo_regex = re.compile(r".+-t[123]")

for repo in list_repos():
    if not repo_regex.match(repo):
        print "Skipping " + repo
        continue
    os.system("git clone https://github.com/tenjava/" + repo + ".git repos/" + repo)
