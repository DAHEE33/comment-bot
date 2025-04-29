# utils/target_selector.py
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By
import time

def get_targets(
    driver,
    mode="neighbor_recent_post",   # 'neighbor_recent_post' | 'neighbor_keyword_post' | 'my_post_commenters'
    keyword=None,                  # 키워드 모드에서 필요
    limit=10
):
    # ------------------------------------------------------------
    # 1) 내 이웃 새글 목록 모드
    # ------------------------------------------------------------
    if mode == "neighbor_recent_post":
        print("[DEBUG] 이웃 새글 목록에서 타겟 추출 중…")
        driver.get(
            "https://section.blog.naver.com/NeighborPostList.naver"
            "?blogId=YOUR_BLOG_ID&currentPage=1"
        )
        time.sleep(2)
        ids = []
        for e in driver.find_elements(By.CSS_SELECTOR, ".list_area .item_user a.name"):
            href = e.get_attribute("href") or ""
            if "blog.naver.com" in href:
                uid = href.rstrip("/").split("/")[-1]
                if uid not in ids:
                    ids.append(uid)
            if len(ids) >= limit:
                break
        print("[INFO] 이웃 새글 유저:", ids)
        return ids

    # ------------------------------------------------------------
    # 2) 키워드 모드
    # ------------------------------------------------------------
    elif mode == "neighbor_keyword_post":
        assert keyword, "keyword 파라미터를 지정해야 합니다."
        print(f"[DEBUG] 이웃 중 '{keyword}' 키워드 글 쓴 사람 추출 중…")

        # 1) 이웃 리스트 먼저
        driver.get(
            "https://section.blog.naver.com/NeighborPostList.naver"
            "?blogId=YOUR_BLOG_ID&currentPage=1"
        )
        time.sleep(2)
        neighbors = []
        for e in driver.find_elements(By.CSS_SELECTOR, ".list_area .item_user a.name"):
            href = e.get_attribute("href") or ""
            if "blog.naver.com" in href:
                bid = href.rstrip("/").split("/")[-1]
                if bid not in neighbors:
                    neighbors.append(bid)
            if len(neighbors) >= limit:
                break

        # 2) 각 블로거 최신 글 제목 검사
        matched = []
        for bid in neighbors:
            driver.get(f"https://blog.naver.com/{bid}/PostList.naver?blogId={bid}")
            time.sleep(1)
            for t in driver.find_elements(By.CSS_SELECTOR, ".post_list .item_title"):
                if keyword.lower() in t.text.lower():
                    matched.append(bid)
                    print(f"[INFO] 키워드 매칭: {bid} → \"{t.text}\"")
                    break
            if len(matched) >= limit:
                break

        print("[INFO] 키워드 매칭 유저:", matched)
        return matched

    # ------------------------------------------------------------
    # 3) 내 최신 글에 댓글단 사람들 모드
    # ------------------------------------------------------------
    elif mode == "my_post_commenters":
        print("[DEBUG] 내 최신 글에 댓글 단 이웃 추출 중…")

        # 1) 내 블로그 홈으로 이동
        driver.get("https://blog.naver.com/YourBlogID")  # Replace with YOUR_BLOG_ID
        time.sleep(2)

        # 2) 최신 글 클릭 (첫 번째 포스트)
        first_post = driver.find_element(By.CSS_SELECTOR,
            ".post_list .item_title a"
        )
        first_post.click()
        time.sleep(2)

        # 3) 댓글 영역으로 스크롤
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        # 4) 댓글 작성자 추출
        commenters = []
        comment_elems = driver.find_elements(By.CSS_SELECTOR,
            ".u_cbox_list .u_cbox_comment .u_cbox_author"
        )
        for ce in comment_elems:
            href = ce.get_attribute("href") or ""
            # 댓글 작성자 프로필 URL에서 ID 파싱 예시
            if "blog.naver.com" in href:
                uid = href.rstrip("/").split("/")[-1]
                if uid not in commenters:
                    commenters.append(uid)
            if len(commenters) >= limit:
                break

        print("[INFO] 댓글단 이웃:", commenters)
        return commenters

    else:
        raise ValueError(f"알 수 없는 mode: {mode}")

