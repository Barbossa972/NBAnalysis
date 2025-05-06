import requests
from bs4 import BeautifulSoup


def scrape(year: int):

    url = 'https://www.basketball-reference.com/'
    season = f"leagues/NBA_games{year}.html"
    link_to_games = url + season
    response = requests.get(link_to_games)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    # title = soup.select_one('h1').text
    # text = soup.select_one('p').text
    # link = soup.select_one('a').get('href')
    titles = soup.find_all("h1")
    texts = soup.find_all("p")
    links = soup.find_all("a")
    # print(titles)
    # print(texts)
    print(links)




if __name__ == '__main__':
    scrape(2025)
    