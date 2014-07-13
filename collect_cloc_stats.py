#!/usr/bin/env python

import os
import subprocess
import xml.dom.minidom
import json

def collect_xml(repo):
    return subprocess.check_output(["cloc", "--xml", "--quiet", "repos/" + repo])

def collect(repo):
    xmls = collect_xml(repo).strip()
    if not xmls:
        return None
    dom = xml.dom.minidom.parseString(xmls)
    langs = {}
    total = {}
    for ele in dom.getElementsByTagName("language"):
        entry = {
            "blank": int(ele.getAttribute("blank")),
            "comment": int(ele.getAttribute("comment")),
            "code": int(ele.getAttribute("code")),
        }
        entry["total"] = sum(entry.values())
        for k in entry:
            if not k in total:
                total[k] = entry[k]
            else:
                total[k] += entry[k]
        langs[str(ele.getAttribute("name"))] = entry
    langs["SUM"] = total
    return langs

m = {}
for repo in os.listdir("repos"):
    print "Collecting stats on " + repo + "..."
    collected = collect(repo)
    if not collected:
        print "Failed to read info for " + repo
        continue
    m[repo] = collected

with open("cloc.json", "w") as f:
    json.dump(m, f)
