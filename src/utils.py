import urllib.request
import re

def store(url, name = ""):
    if name == "":
        r = re.search("([^/]+?)(\.{1,6})?$", url)
        if r.group(2):
            filename = r.group(1) + r.group(2)
        else:
            filename = r.group(1)
        if r:
            realname = store(url, filename)
        return realname
    else:
        print("[~] Downloading " + url + " -> " + name)
        f = urllib.request.urlopen(url)
        with open(name, "b+w") as g:
            g.write(f.read())
        return name
