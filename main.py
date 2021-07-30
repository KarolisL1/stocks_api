import requests
import smtplib
import time

import config

apiKey = "90lPqyA1NbfpaGO8OlOYxx3awDEYxiP1"
ticker = "TSLA"
limit = "1"

year = "2021"
month = "07"
day = "29"

my_email = "karolistest0@gmail.com"
password = "testlabukas1"
subject = "Stocks news"

api_url = f"https://api.polygon.io/v2/reference/news?limit={limit}&order=descending&sort=published_utc&ticker={ticker}&published_utc.gte={year}-{month}-{day}&apiKey={apiKey}"
data = requests.get(api_url).json()

list1 = []
list2 = []
list3 = []

def send_email(my_email, password, msg):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls() #secure the connection
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=msg)
        print("Success: Email Send!")
    except:
        print("Email failed to send.")

for i in range(int(limit)):
    news_title = data['results'][i]['title']
    news_article_url = data['results'][i]['article_url']
    news_description = data['results'][i]['description']
    list1.append(news_title)
    list2.append(news_article_url)
    list3.append(news_description)

msg = f"Subject:{subject}\n\n" \
      f"News: {list1}\n" \
      f"URL: {list2}\n" \
#      f"Description: {list3}" Description is just too long should check on this

send_email(config.MY_EMAIL, config.PASSWORD, msg)




