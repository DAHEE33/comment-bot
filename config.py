from dotenv import load_dotenv
import os

load_dotenv()

NAVER_ID = os.getenv("NAVER_ID")
NAVER_PW = os.getenv("NAVER_PW")
CHROME_PATH = "./chromedriver.exe"
