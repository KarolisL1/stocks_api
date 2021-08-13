import requests
import smtplib
from datetime import date


apiKey = "90lPqyA1NbfpaGO8OlOYxx3awDEYxiP1"
ticker = input("Ivesk norima akcija:").upper()
limit = "1"

today = date.today()
year = today.strftime("%Y")
month = today.strftime("%m")
day = today.strftime("%d")

my_email = "karolistest0@gmail.com"
password = input("Password: ")
subject = "Stocks news"

api_url = f"https://api.polygon.io/v2/reference/news?limit={limit}&order=descending&sort=published_utc&ticker={ticker}&published_utc.gte={year}-{month}-{day}&apiKey={apiKey}"
data = requests.get(api_url).json()

list1 = []
list2 = []
list3 = []


def send_email(my_email, password, msg):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # secure the connection
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=msg)
        print("Success: Email Send!")
    except Exception as e:
        print("Email failed to send. ", e)


for i in range(int(limit)):
    news_title = data['results'][i]['title']
    news_article_url = data['results'][i]['article_url']
    news_description = data['results'][i]['description']

    list1.append(news_title)
    list2.append(news_article_url)
    list3.append(news_description)

    str1 = ''.join(news_title)
    str2 = ''.join(news_article_url)
    str3 = ''.join(news_description)

msg = f"Subject:{subject}\n\n" \
      f"News: {str1}\n" \
      f"URL: {str2}\n" \
      f"Description: {str3}"

send_email(my_email, password, msg)

