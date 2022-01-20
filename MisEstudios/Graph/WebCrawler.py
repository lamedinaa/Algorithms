import requests
import re

class WebCrawler:

    def __init__(self):
        self.url_visited = []

    def crawl(self,start_url):
        queue = [start_url]
        self.url_visited.append(start_url)

        while queue:
            actual_url = queue.pop(0)
            print(actual_url)
            actual_url_html = self.read_raw_html(actual_url)
            for link in self.get_links_from_html(actual_url_html):
                if link not in self.url_visited:
                    self.url_visited.append(link)
                    queue.append(link)

    
    def get_links_from_html(self,html):
        return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",html)

    def read_raw_html(self,url):
        raw_html =""

        try:
            raw_html = requests.get(url).text
        except Exception as e:
            pass

        return raw_html


if __name__=="__main__":
    crawler = WebCrawler()
    crawler.crawl("https://www.cnn.com")    



