from bs4 import BeautifulSoup
import requests
import csv

for idx in range(10,230):
    url = f"https://www.yelp.com/biz/ozakaya-brooklyn?osq=Restaurants&start={idx}#reviews"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content,'html.parser')
    reviews=soup.find_all("p",{"class":"comment__09f24__D0cxf y-css-h9c2fl"})

    with open('reviews.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for review in reviews:
            csvwriter.writerow(review.text)
