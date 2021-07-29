import requests

apiKey = "90lPqyA1NbfpaGO8OlOYxx3awDEYxiP1"
ticker = "TSLA"
limit = "10"

year = "2021"
month = "07"
day = "28"



api_url = f"https://api.polygon.io/v2/reference/news?limit={limit}&order=descending&sort=published_utc&ticker={ticker}&published_utc.gte={year}-{month}-{day}&apiKey={apiKey}"

data = requests.get(api_url).json()

list1 = []
list2 = []
list3 = []
for i in range(int(limit)):
    news_title = data['results'][i]['title']
    news_article_url = data['results'][i]['article_url']
    news_description = data['results'][i]['description']
    list1.append(news_title)
    list2.append(news_article_url)
    list3.append(news_description)

print(list3)
