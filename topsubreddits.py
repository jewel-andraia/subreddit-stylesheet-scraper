from utils import get_url, load_file, save_list, unique
from bs4 import BeautifulSoup
from config import SUBREDDITS
from time import sleep

def main():
    subreddits = []
    for i, offset in enumerate(range(0, 500, 100)): 
        print(offset)
        if i > 0: sleep(2)
        source = get_url('http://redditmetrics.com/top/offset/{offset}'.format(offset=offset))
        soup = BeautifulSoup(source)
        cells = soup.find_all('td', string=lambda s: s[0:3] == '/r/')
        new_subreddits = [ cell.get_text()[3:] for cell in cells ]
        subreddits += new_subreddits
        print(new_subreddits)

    subreddits[:] = unique(subreddits)
    print('Saving these subreddits:', subreddits)
    save_list(subreddits, 'subreddits.txt')
    print('Done')



if __name__ == '__main__':
    main()
