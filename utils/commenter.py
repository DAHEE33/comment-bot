import time
from selenium.webdriver.common.by import By
from config import COMMENT_TEXT

def post_comments(driver, user_ids):
    """
    각 user_id 당 첫 번째 포스트에 COMMENT_TEXT를 댓글로 작성
    새로운 창으로 열린 포스트에 댓글을 달고 다시 닫음
    """
    for uid in user_ids:
        blog_url = f"https://blog.naver.com/{uid}"
        driver.get(blog_url)
        time.sleep(2)
        try:
            # 첫 번째 포스트 링크 클릭
            first_post = driver.find_element(By.CSS_SELECTOR, ".lst_total .desc a")
            first_post.click()
            time.sleep(2)
            # 새 창으로 전환
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
            # 댓글 작성 영역
            comment_area = driver.find_element(By.CSS_SELECTOR, ".u_cbox_textarea")
            comment_area.click()
            comment_area.send_keys(COMMENT_TEXT)
            time.sleep(0.5)
            # 댓글 등록 버튼 클릭
            driver.find_element(By.CSS_SELECTOR, ".u_cbox_btn_write").click()
            time.sleep(2)
        except Exception as e:
            print(f"Error commenting on {uid}: {e}")
        finally:
            # 포스트 창 닫고 원래 창으로
            if len(driver.window_handles) > 1:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])