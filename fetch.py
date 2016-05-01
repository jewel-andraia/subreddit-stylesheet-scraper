#!/bin/python
import os
import urllib

SUBREDDITS='subreddits.txt'
STYLESHEETS='stylesheets'

def main():
	global SUBREDDITS
	global STYLESHEETS

	subreddits = load_file(SUBREDDITS)
	output_folder = STYLESHEETS
	urls = [ ( r, 'https://www.reddit.com/r/{r}/stylesheet.css'.format(r=r), '{dir}/{r}.css'.format(dir=output_folder, r=r) )
				for r in subreddits ]
	try:
	    os.stat(output_folder)
	except:
	    os.mkoutput_folder(dir) 

	for i, (r, url, output) in enumerate(urls):
		o = urllib.URLopener()
		o.retrieve(url, output)
		print('Fetched {r} ({i}/{len})'.format(r=r, i=i, len=len(urls)))
		sleep(2)


def load_file(filename):
	with open(filename, 'r') as file:
		lines = [ l for l in file ]
			
	return set(lines)

if __name__ == '__main__':
    main()
