import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from random import shuffle


def get_proxies(link):  
    response = requests.get(link)
    soup = BeautifulSoup(response.text,"lxml")
    https_proxies = filter(lambda item: "yes" in item.text,
                           soup.select("table.table tr"))
    for item in https_proxies:
        yield "{}:{}".format(item.select_one("td").text,
                             item.select_one("td:nth-of-type(2)").text)

def get_random_proxies_iter():
    proxies = list(get_proxies('https://www.sslproxies.org/'))
    shuffle(proxies)
    return iter(proxies)  # iter so we can call next on it to get the next proxy


def get_proxy(session, proxies, validated=False):
    session.proxies = {'https': 'https://{}'.format(next(proxies))}
    if validated:
        while True:
            try:
                return session.get('https://httpbin.org/ip').json()
            except Exception:
                session.proxies = {'https': 'https://{}'.format(next(proxies))}


def get_response(url):
    session = requests.Session()
    ua = UserAgent()
    proxies = get_random_proxies_iter()
    while True:
        try:
            session.headers = {'User-Agent': ua.random}
            print(get_proxy(session, proxies, validated=True))  #collect a working proxy to be used to fetch a valid response
            return session.get(url) # as soon as it fetches a valid response, it will break out of the while loop
        except StopIteration:
            raise  # No more proxies left to try
        except Exception:
            pass  # Other errors: try again


def parse_content(url):
    response = get_response(url)
    soup = BeautifulSoup(response.text, 'lxml')
    for items in soup.select(".info span[itemprop='name']"):
        print(items.text)


if __name__ == '__main__':
    # url = 'https://www.yellowpages.com/search?search_terms=Coffee%20Shops&geo_location_terms=Los%20Angeles%2C%20CA&page={}'
    # links = [url.format(page) for page in range(1, 2)]
    # for link in links:
    #     parse_content(link)

    url = config.websites[0]
    parse_content(url)