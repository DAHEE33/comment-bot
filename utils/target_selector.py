import time
from selenium.webdriver.common.by import By
from config import BLOG_ID, NEIGHBOR_URL

def get_targets(driver, limit=10):
    """
    이웃 새글 페이지에서 blogId를 기준으로 최근 글 작성자 ID 리스트를 가져옴
    자기 블로그(BLOG_ID)는 필터링 처리
    """
    driver.get(NEIGHBOR_URL)
    time.sleep(2)
    user_ids = []
    elements = driver.find_elements(By.CLASS_NAME, "name")
    for e in elements:
        href = e.get_attribute("href")
        if not href or "blog.naver.com" not in href:
            continue
        uid = href.rstrip('/').split('/')[-1]
        if uid == BLOG_ID:
            continue
        if uid not in user_ids:
            user_ids.append(uid)
        if len(user_ids) >= limit:
            break
    return user_ids