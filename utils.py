import os
import urllib.request
import urllib.error

def mkdir_p(dirname):
    try:
        os.stat(dirname)
    except:
        os.mkdir(dirname)

def get_url(url):
    try:
        fp = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        print('Wait a few minutes and try again')
        raise

    contents = fp.read()
    return contents.decode('utf-8')

def save_url(url, filename):
    contents = get_url(url)
    with open(filename, 'w') as fo:
        fo.write(contents)

def load_file(filename):
    with open(filename, 'r') as file:
        lines = [ str(l).strip() for l in file ]
            
    return lines

def save_list(lines, filename):
    with open(filename, 'w') as fo:
        for line in lines:
            fo.write('{}\n'.format(line))

def unique(seq):
    seen = set()
    for item in seq:
        if item not in seen:
            seen.add(item)
            yield item
