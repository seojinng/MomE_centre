import sqlite3
import streamlit as st
from datetime import datetime
from streamlit_option_menu import option_menu


with st.sidebar:
    menu = option_menu("MomE", ['Home','Dashboard','Diary','육아 SNS','community', '하루 자가진단','LogOut'],
                        icons=['bi bi-house-fill','bi bi-grid-1x2-fill','book-half','Bi bi-star-fill','Bi bi-star-fill' ,'bi bi-capsule-pill', 'box-arrow-in-right'],
                        menu_icon="baby", default_index=4,
                        styles={
                            "icon": {"font-size": "23px"},
                            "title": {"font-weight": "bold"}  # MomE 글씨를 볼드체로 변경
                        })

    # 선택된 메뉴에 따라 페이지 변경
    if menu =='Dashboard':
        st.switch_page("pages/dashboard_page.py")
    elif menu =='Diary':
        st.switch_page("pages/diary_page.py")
    elif menu =='육아 SNS':
        st.switch_page("pages/SNS2.py")
    elif menu =='Home':
        st.switch_page("pages/home.py")
    elif menu =='하루 자가진단':
        st.switch_page('pages/self_diagnosis.py')
    elif menu =='LogOut':
        st.switch_page("dd1.py")


# 데이터베이스 초기화
def init_db():
    conn = sqlite3.connect('community.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT,
            content TEXT,
            created_at TEXT,
            likes INTEGER
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER,
            author TEXT,
            content TEXT,
            created_at TEXT,
            FOREIGN KEY (post_id) REFERENCES posts (id)
        )
    ''')
    conn.commit()
    conn.close()

# 데이터 삽입 및 조회 함수
def add_post(author, content):
    conn = sqlite3.connect('community.db')
    c = conn.cursor()
    c.execute('INSERT INTO posts (author, content, created_at, likes) VALUES (?, ?, ?, ?)',
              (author, content, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0))
    conn.commit()
    conn.close()

def get_posts():
    conn = sqlite3.connect('community.db')
    c = conn.cursor()
    c.execute('SELECT * FROM posts ORDER BY datetime(created_at) ASC')
    posts = c.fetchall()
    conn.close()
    return posts

def add_comment(post_id, author, content):
    conn = sqlite3.connect('community.db')
    c = conn.cursor()
    c.execute('INSERT INTO comments (post_id, author, content, created_at) VALUES (?, ?, ?, ?)',
              (post_id, author, content, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_comments(post_id):
    conn = sqlite3.connect('community.db')
    c = conn.cursor()
    c.execute('SELECT * FROM comments WHERE post_id = ? ORDER BY datetime(created_at) ASC', (post_id,))
    comments = c.fetchall()
    conn.close()
    return comments

def like_post(post_id):
    conn = sqlite3.connect('community.db')
    c = conn.cursor()
    c.execute('UPDATE posts SET likes = likes + 1 WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()

def delete_post(post_id):
    conn = sqlite3.connect('community.db')
    c = conn.cursor()
    c.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    c.execute('DELETE FROM comments WHERE post_id = ?', (post_id,))
    conn.commit()
    conn.close()

def update_post(post_id, author, content):
    conn = sqlite3.connect('community.db')
    c = conn.cursor()
    c.execute('UPDATE posts SET author = ?, content = ? WHERE id = ?', (author, content, post_id))
    conn.commit()
    conn.close()

# 게시글 작성 폼
def post_form():
    st.subheader("게시글 작성")
    author = st.text_input("작성자 이름", key='post_author')
    content = st.text_area("내용", key='post_content')
    if st.button("게시글 작성", key='post_submit'):
        if author and content:
            add_post(author, content)
            st.success("게시글이 작성되었습니다.")
            st.experimental_rerun()  # 데이터가 변경되면 자동으로 새로고침
        else:
            st.error("모든 필드를 입력해주세요.")

# 댓글 작성 폼
def comment_form(post_id):
    with st.expander("댓글 작성/숨기기"):
        comment_author = st.text_input("작성자 이름 (댓글)", key=f'comment_author_{post_id}_form')
        comment_content = st.text_input("내용 (댓글)", key=f'comment_content_{post_id}_form')
        if st.button("댓글 작성", key=f'comment_button_{post_id}_form'):
            if comment_author and comment_content:
                add_comment(post_id, comment_author, comment_content)
                st.success("댓글이 작성되었습니다.")
                st.experimental_rerun()  # 데이터가 변경되면 자동으로 새로고침
            else:
                st.error("모든 필드를 입력해주세요.")
        st.write("댓글 목록:")
        comments = get_comments(post_id)
        for comment in comments:
            st.write(f"**{comment[2]}**: {comment[3]} ({comment[4]})")

# 게시글 수정 폼
def edit_post_form(post_id):
    posts = get_posts()
    post = next((p for p in posts if p[0] == post_id), None)
    if not post:
        st.error("게시글을 찾을 수 없습니다.")
        return
    st.write("게시글 수정")
    author = st.text_input("작성자 이름", value=post[1], key=f'edit_post_author_{post_id}')
    content = st.text_area("내용", value=post[2], key=f'edit_post_content_{post_id}')
    if st.button("게시글 수정 완료", key=f'edit_post_button_{post_id}'):
        if author and content:
            update_post(post_id, author, content)
            st.success("게시글이 수정되었습니다.")
            st.session_state.editing_post_id = None  # 수정 완료 후 수정 폼 숨기기
            st.experimental_rerun()  # 데이터가 변경되면 자동으로 새로고침
        else:
            st.error("모든 필드를 입력해주세요.")

# 게시글 목록 표시
def post_list():
    st.subheader("게시글 목록")
    posts = get_posts()
    for post in posts:
        st.markdown(f"<div class='post-card'>**{post[1]}** ({post[3]}): {post[2]}<br>좋아요: {post[4]}</div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("좋아요", key=f'like_button_{post[0]}'):
                like_post(post[0])
                st.experimental_rerun()  # 데이터가 변경되면 자동으로 새로고침
        with col2:
            if st.button("게시글 수정", key=f'edit_button_{post[0]}'):
                st.session_state.editing_post_id = post[0]  # 현재 수정 중인 게시글 ID를 세션 상태에 저장
        with col3:
            if st.button("게시글 삭제", key=f'delete_button_{post[0]}'):
                delete_post(post[0])
                if 'editing_post_id' in st.session_state and st.session_state.editing_post_id == post[0]:
                    del st.session_state.editing_post_id  # 삭제된 게시글이 수정 중인 게시글일 경우 초기화
                st.experimental_rerun()  # 데이터가 변경되면 자동으로 새로고침
        comment_form(post[0])
        st.write("---")

    # 수정 중인 게시글이 있을 경우 수정 폼 표시
    if "editing_post_id" in st.session_state and st.session_state.editing_post_id:
        edit_post_form(st.session_state.editing_post_id)
    elif "editing_post_id" in st.session_state:
        del st.session_state.editing_post_id  # ID가 없으면 초기화

# 게시글 전체 삭제 함수
def delete_all_posts():
    conn = sqlite3.connect('community.db')
    c = conn.cursor()
    c.execute('DELETE FROM posts')
    c.execute('DELETE FROM comments')
    conn.commit()
    conn.close()
    st.success("모든 게시글이 삭제되었습니다.")
    st.experimental_rerun()  # 데이터가 변경되면 자동으로 새로고침

# Streamlit 앱 실행
def main():
    # CSS 스타일 추가
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6; /* 배경을 연한 회색으로 설정 */
        }
        .reportview-container .main .block-container {
            padding: 2rem; /* 전체 컨테이너의 패딩 설정 */
        }
        .stTextInput > div > div > input, .stTextArea > div > textarea {
            border: 1px solid #ccc; /* 입력 필드 테두리 색상 설정 */
            padding: 10px; /* 입력 필드 패딩 설정 */
            border-radius: 5px; /* 입력 필드 테두리 둥글게 설정 */
        }
        .stButton button {
            background-color: #4CAF50; /* 버튼 배경색을 녹색으로 설정 */
            color: white; /* 버튼 글자색을 흰색으로 설정 */
            border: none; /* 버튼 테두리 없애기 */
            border-radius: 5px; /* 버튼 테두리를 둥글게 설정 */
            padding: 5px 10px; /* 버튼 패딩 설정 (크기 작게) */
            font-size: 12px; /* 버튼 폰트 크기 설정 (크기 작게) */
            margin: 5px 2px; /* 버튼 외부 마진 설정 */
            cursor: pointer; /* 커서를 포인터로 설정 */
        }
        .stButton button:hover {
            background-color: #45a049; /* 버튼 호버 시 배경색 설정 */
        }
        .small-button {
            background-color: #4CAF50; /* 작은 버튼 배경색을 녹색으로 설정 */
            color: white; /* 작은 버튼 글자색을 흰색으로 설정 */
            border: none; /* 작은 버튼 테두리 없애기 */
            border-radius: 5px; /* 작은 버튼 테두리를 둥글게 설정 */
            padding: 2px 5px; /* 작은 버튼 패딩 설정 */
            font-size: 10px; /* 작은 버튼 폰트 크기 설정 */
            margin: 5px 2px; /* 작은 버튼 외부 마진 설정 */
            cursor: pointer; /* 커서를 포인터로 설정 */
        }
        .small-button:hover {
            background-color: #45a049; /* 작은 버튼 호버 시 배경색 설정 */
        }
        .post-card {
            background-color: #ffffff; /* 카드 배경색을 흰색으로 설정 */
            padding: 15px; /* 카드 패딩 설정 */
            margin: 10px 0; /* 카드 외부 마진 설정 */
            border-radius: 5px; /* 카드 테두리를 둥글게 설정 */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 카드 그림자 설정 */
        }
        .comment-section {
            margin-top: 10px; /* 댓글 섹션 상단 마진 설정 */
            margin-left: 20px; /* 댓글 섹션 좌측 마진 설정 */
        }
        .fixed-button {
            position: fixed;
            top: 10px;
            right: 10px;
            z-index: 9999;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("초보 엄마,아빠들을 위한 커뮤니티 게시판")

    # 페이지 상단에 고정된 버튼
    st.markdown('<div class="fixed-button"><button class="stButton" onclick="document.getElementById(\'delete_all\').click();">게시글 전체 삭제</button></div>', unsafe_allow_html=True)
    if st.button("게시글 전체 삭제", key='delete_all'):
        delete_all_posts()

    # 페이지를 두 부분으로 나누기
    col1, col2 = st.columns(2)

    with col1:
        post_form()

    with col2:
        post_list()



if __name__ == "__main__":
    init_db()
    main()
