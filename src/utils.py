import urllib.request

def store(url, name = ""):
    if name == "":
        r = re.search("([^/]+?)(\.{1,6}$", url)
        if r:
            store(url, r.group(1) + r.group(2))
    else:
        print("[~] Downloading " + url + " -> " + name)
        f = urllib.request.urlopen(url)
        with open(name, "b+w") as g:
            g.write(f.read())
