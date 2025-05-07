import os

BASE_DIR = os.path.dirname(__file__)
CHROMEDRIVER_PATH = os.path.join(BASE_DIR, "chromedriver.exe")
NAVER_LOGIN_URL   = "https://nid.naver.com/nidlogin.login"
NAVER_ID             = os.getenv("NAVER_ID")                    
NAVER_PW             = os.getenv("NAVER_PW")   
BLOG_ID           = os.getenv("NAVER_ID")  
NEIGHBOR_URL      = f"https://blog.naver.com/PostList.naver?blogId={BLOG_ID}&from=neighbor_new_post"
COMMENT_TEXT      = "안녕하세요! 좋은 글 잘 보고 갑니다 :)"