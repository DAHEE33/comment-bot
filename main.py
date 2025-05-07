import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config import CHROMEDRIVER_PATH
from utils.auth import login
from utils.target_selector import get_targets
from utils.commenter import post_comments

def setup_driver():
    options = Options()
    # 자동화 표시 제거
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    # 창 분리 (헤드리스가 아니더라도 닫히지 않도록)
    options.add_experimental_option("detach", True)

    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    # navigator.webdriver 우회
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"}
    )
    return driver


def main():
    driver = setup_driver()
    # 1) 로그인
    login(driver)
    # 2) 이웃 목록 추출 (자기 블로그 제외)
    targets = get_targets(driver, limit=10)
    print("추출된 타겟:", targets)
    # 3) 댓글 작성
    # post_comments(driver, targets)
    print("모든 작업이 완료되었습니다.")
    driver.quit()

if __name__ == "__main__":
    main()