from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config import NAVER_ID, NAVER_PW
import time

def login(driver, use_clipboard=False):
    driver.get("https://nid.naver.com/nidlogin.login")
    time.sleep(1)

    id_input = driver.find_element(By.ID, "id")
    pw_input = driver.find_element(By.ID, "pw")

    if use_clipboard:
        import pyperclip
        pyperclip.copy(NAVER_ID)
        id_input.click()
        id_input.send_keys(Keys.CONTROL, "v")
        time.sleep(1)

        pyperclip.copy(NAVER_PW)
        pw_input.click()
        pw_input.send_keys(Keys.CONTROL, "v")
        time.sleep(1)
    else:
        id_input.send_keys(NAVER_ID)
        time.sleep(1)
        pw_input.send_keys(NAVER_PW)
        time.sleep(1)

    driver.find_element(By.ID, "log.login").click()

    # 로그인 성공 확인
    try:
        print("현재 URL:", driver.current_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#account"))  # 로그인 후 뜨는 상단 메뉴
        )
        print("[INFO] 로그인 성공")
    except:
        print("[ERROR] 로그인 실패 또는 추가 인증 필요")
        driver.quit()
        raise
