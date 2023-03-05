from bs4 import BeautifulSoup
import re


class subreview_scrape():
    def __init__(self, bs):
        self.bs = bs

    def find_sub_reviews(self):
        reviews_subcategory = self.bs.findAll(name='div', attrs={'class': 'css-1dbjc4n r-18u37iz r-d0pm55'})
        return reviews_subcategory

    def find_specifications(self, category, point='Y'):
        details = self.find_sub_reviews()
        review = []
        if category == '추천 점수' and point == 'Y':
            for i in details:
                if i.find(name='div',
                          attrs={'class': 'css-1dbjc4n r-skblka r-13l2t4g r-zso239 r-1qfoi16'}).text == '추천 점수':
                    review.append(i.findAll(name='div', attrs={'class': 'css-1563yu1'})[1].text)
        if category == '추천 점수' and point == 'N':
            for i in details:
                if i.find(name='div',
                          attrs={'class': 'css-1dbjc4n r-skblka r-13l2t4g r-zso239 r-1qfoi16'}).text == '추천 점수':
                    review.append(i.find_next_sibling(name='div', attrs={'class': 'css-1dbjc4n'}).text)
        if category != '추천 점수' and point == 'Y':
            for i in details:
                if i.find(name='div',
                          attrs={'class': 'css-1dbjc4n r-skblka r-13l2t4g r-zso239 r-1qfoi16'}).text == category:
                    review.append(i.find(name='div', attrs={'class': 'css-1563yu1 r-cqee49 r-1d4mawv'}).text)

        if category != '추천 점수' and point == 'N':
            for i in details:
                if i.find(name='div',
                          attrs={'class': 'css-1dbjc4n r-skblka r-13l2t4g r-zso239 r-1qfoi16'}).text == category:
                    review.append(i.find_next_sibling(name='div', attrs={'class': 'css-1dbjc4n'}).text)

        if point == 'Y':
           review = [float(x) for x in review]

        return review
