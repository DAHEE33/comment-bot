def write_comment(driver, user_id, message):
    # 예: https://blog.naver.com/{user_id}
    driver.get(f"https://blog.naver.com/{user_id}")
    # TODO: 댓글 작성 위치 찾고 message 입력 후 전송
    print(f"[INFO] {user_id} 에게 댓글 달기")