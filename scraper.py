from bs4 import BeautifulSoup
import requests
import csv

restaurants = ['ozakaya-brooklyn','arden-brooklyn','the-canary-brooklyn']

for restaurant in restaurants:
    for idx in range(30):
        url = f"https://www.yelp.com/biz/{restaurant}start={idx}#reviews"
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content,'html.parser')
        reviews=soup.find_all("p",{"class":"comment__09f24__D0cxf y-css-h9c2fl"})
        print(reviews)
        with open('reviews.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            for review in reviews:
                csvwriter.writerow(review.text)
