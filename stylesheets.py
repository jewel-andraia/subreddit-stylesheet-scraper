from time import sleep
from config import SUBREDDITS, STYLESHEETS
from utils import load_file, save_url, mkdir_p

def main():
    urls = get_urls()
    mkdir_p(STYLESHEETS)

    for i, (r, url, filename) in enumerate(get_urls()):
        print('({i}/{len}) Saving {r} ({url}) to {filename}'.format(r=r, i=i, url=url, filename=filename, len=len(urls)))
        save_url(url, filename)
        print('({i}/{len}) Saved {r}'.format(r=r, i=i+1, url=url, filename=filename, len=len(urls)))
        if i > 0:
            sleep(2)

def get_urls():
    subreddits = load_file(SUBREDDITS)
    output_folder = STYLESHEETS
    urls = [ ( r, 'https://www.reddit.com/r/{r}/stylesheet.css'.format(r=r), '{dir}/{r}.css'.format(dir=output_folder, r=r) )
                for r in subreddits ]
    return urls

if __name__ == '__main__':
    main()
