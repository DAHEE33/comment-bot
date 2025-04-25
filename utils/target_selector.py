# utils/target_selector.py
from selenium.webdriver.common.by import By
import time

def get_targets(driver, mode="neighbor_recent_post", keyword=None, post_url=None, limit=10):
    if mode == "neighbor_recent_post":
        print("[DEBUG] 이웃 새글 목록에서 타겟 추출 중...")

        user_ids = []
        elements = driver.find_elements(By.CLASS_NAME, "name")

        for elem in elements:
            href = elem.get_attribute("href")
            print("[DEBUG] 추출된 href:", href)
            
            if href and "blog.naver.com" in href:
                blog_id = href.split("/")[-1]
                if blog_id not in user_ids:
                    user_ids.append(blog_id)
            if len(user_ids) >= limit:
                break

        print("[INFO] 추출된 유저:", user_ids)
        return user_ids
