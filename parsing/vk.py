import requests
from bs4 import BeautifulSoup

def getFollowerCount(vkId):
    url = 'https://vk.com/'+ vkId
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers',
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text)
    script = soup.select('.header_count.fl_l')
    text = script[0]
    final = text.get_text()
    final = final.replace(",", "")
    final = int(final)
    return final