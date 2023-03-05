import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chrome_Serivce
from bs4 import BeautifulSoup
from Utilities.find_subcategory_review import subreview_scrape
from Utilities.click_hidden_btns import go_to_apt_page


#골든센트로 : https://www.zigbang.com/home/apt/danjis/20337/reviews?apt_name=%EB%AF%B8%EC%82%AC%EA%B0%95%EB%B3%80%EA%B3%A8%EB%93%A0%EC%84%BC%ED%8A%B8%EB%A1%9C
#롯데캐슬 : 'https://www.zigbang.com/home/apt/danjis/15953/reviews?apt_name=%EA%B0%95%EB%8F%99%EB%A1%AF%EB%8D%B0%EC%BA%90%EC%8A%AC%ED%8D%BC%EC%8A%A4%ED%8A%B8'
chrome_service = Chrome_Serivce(executable_path='//Users//imjaehwan//PycharmProjects//driver_file//chromedriver')
driver = webdriver.Chrome(service=chrome_service)
baseURL = 'https://www.zigbang.com/home/apt/danjis/20337/reviews?apt_name=%EB%AF%B8%EC%82%AC%EA%B0%95%EB%B3%80%EA%B3%A8%EB%93%A0%EC%84%BC%ED%8A%B8%EB%A1%9C'


#Click Hidden Buttons in the Review
hidden_btn_click = go_to_apt_page(driver, baseURL)
hidden_btn_click.click_hidden_btns()

'''교통 여건 등 내용 가져오기'''
html = driver.page_source
bs = BeautifulSoup(html, 'html.parser')

'''전체 리뷰에서 하위 항목 리뷰'''
review_details = subreview_scrape(bs)


'''추출한 리뷰를 Dictionary 형태로 정리'''
details = {'recommended': review_details.find_specifications('추천 점수','Y')
    ,'recommended_review': review_details.find_specifications('추천 점수','N')
    ,'transportation': review_details.find_specifications('교통 여건','Y')
    ,'transportaion_review': review_details.find_specifications('교통 여건','N')
    , 'nearby': review_details.find_specifications('주변 환경','Y')
    , 'nearby_review': review_details.find_specifications('주변 환경','N')
    ,'facility': review_details.find_specifications('단지 관리','Y')
    , 'facility_review': review_details.find_specifications('단지 관리','N')
    , 'living_env': review_details.find_specifications('거주 환경','Y')
    , 'living_review': review_details.find_specifications('거주 환경','N')
           }


'''csv파일로 내보내기'''
df = pd.DataFrame.from_dict(details)
df.to_csv('df_golden.csv', index=False, encoding="utf-8-sig")