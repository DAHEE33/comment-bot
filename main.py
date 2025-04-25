from utils.target_selector import get_targets
from utils.commenter import write_comment
from utils.auth import login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config import CHROME_PATH
import time

def main():
    # 브라우저 실행
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(CHROME_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 로그인 + 로그인 성공 후 리디렉션 대기
    login(driver, use_clipboard=True)

    # ✅ 로그인 후 타겟 페이지로 직접 이동
    driver.get("https://section.blog.naver.com/BlogHome.naver")
    # driver.get("https://section.blog.naver.com/SearchPost.naver?keyword=파이썬")
    time.sleep(3)

    # 타겟 유저 수집 (드라이버를 넘겨줌)
    targets = get_targets(driver, limit=1)
    print("🎯 타겟 목록:", targets)

    # 댓글 달기
    for user_id in targets:
        write_comment(driver, user_id, "안녕하세요, 좋은 글 잘 봤어요!")

if __name__ == "__main__":
    main()
