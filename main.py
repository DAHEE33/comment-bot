# main.py
from utils.auth import login
from utils.target_selector import get_targets
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from config import CHROME_PATH, NAVER_ID
import time

def main():
    # 브라우저 실행
    opts = Options()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(CHROME_PATH), options=opts)

    # 1) 로그인
    login(driver, use_clipboard=True)

    # 2) 내 블로그 홈으로 가서 최신글 URL 추출
    blog_home = f"https://blog.naver.com/{NAVER_ID}"
    driver.get(blog_home)
    time.sleep(2)

    # 네이버 블로그는 <iframe id="mainFrame"> 안에 글 목록이 뜹니다
    driver.switch_to.frame("mainFrame")
    first_post = driver.find_element(
        By.CSS_SELECTOR,
        ".list_area .item_post a"          # 최신글 링크 셀렉터 (바뀔 수 있으니 확인)
    )
    latest_url = first_post.get_attribute("href")
    driver.switch_to.default_content()
    print("▶ 최신글 URL:", latest_url)

    # 3) 세 가지 모드별 테스트 (limit=3 으로 예시)
    # 3-1) 내 이웃 새글 작성자
    driver.get("https://section.blog.naver.com/BlogHome.naver")
    time.sleep(2)
    lst1 = get_targets(driver, mode="neighbor_recent_post", limit=3)
    print("▶ 이웃 새글 작성자:", lst1)

    # 3-2) 내 최신글에 댓글 단 사람들
    driver.get(latest_url)
    time.sleep(2)
    lst2 = get_targets(driver,
                       mode="my_post_commenters",
                       post_url=latest_url,
                       limit=3)
    print("▶ 내 최신글 댓글러:", lst2)

    # 3-3) 키워드 검색 블로거
    keyword = "파이썬"
    driver.get(f"https://section.blog.naver.com/Search/Post.naver?keyword={keyword}")
    time.sleep(2)
    lst3 = get_targets(driver,
                       mode="search_keyword",
                       keyword=keyword,
                       limit=3)
    print(f"▶ 키워드 '{keyword}' 블로그 글 작성자:", lst3)

    print("✅ 다섯 단계 자동화 테스트 완료!")
    # time.sleep(999)

if __name__ == "__main__":
    main()
