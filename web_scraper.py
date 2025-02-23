import requests
from bs4 import BeautifulSoup

def get_news_articles(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    
    for item in soup.find_all("h2", class_="article-title"):
        title = item.get_text(strip=True)
        link = item.find("a")["href"] if item.find("a") else ""
        articles.append({"title": title, "link": link})
    
    return articles

if __name__ == "__main__":
    url = "https://www.developer-tech.com//"
    news_articles = get_news_articles(url)
    
    for index, article in enumerate(news_articles, start=1):
        print(f"{index}. {article['title']} - {article['link']}")
