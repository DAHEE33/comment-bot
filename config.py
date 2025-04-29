# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # 프로젝트 루트에 있는 .env를 불러옵니다

NAVER_ID             = os.getenv("NAVER_ID")                    # 블로그 로그인 아이디 :contentReference[oaicite:0]{index=0}
NAVER_PW             = os.getenv("NAVER_PW")                    # 블로그 로그인 비밀번호 :contentReference[oaicite:1]{index=1}
MAX_COMMENTS_PER_DAY = int(os.getenv("MAX_COMMENTS_PER_DAY", 100))  # 하루 최대 댓글 수 :contentReference[oaicite:2]{index=2}
MIN_DELAY_SEC        = int(os.getenv("MIN_DELAY_SEC", 20))         # 댓글 간 최소 지연(sec) :contentReference[oaicite:3]{index=3}
MAX_DELAY_SEC        = int(os.getenv("MAX_DELAY_SEC", 60))         # 댓글 간 최대 지연(sec) :contentReference[oaicite:4]{index=4}

# ChromeDriver 경로도 환경변수로 관리하고 싶다면:
# CHROME_PATH = os.getenv("CHROME_PATH", "./chromedriver.exe")
CHROME_PATH         = "./chromedriver.exe"
