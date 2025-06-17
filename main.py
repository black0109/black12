import streamlit as st
import random

st.set_page_config(
    page_title="최애 남자 아이돌 추천 💖",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
        min-height: 100vh;
        padding: 2rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1, h2, h4 {
        font-weight: 800;
        text-shadow: 1px 1px 2px #fff;
    }
    a {
        color: #d6336c;
        font-weight: 700;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#b5179e;'>🌟 남자 아이돌 추천 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#720026;'>BOYNEXTDOOR부터 BTS, EXO, NCT, Stray Kids, SEVENTEEN까지! 최애를 만나보세요 💫</h4>")
st.markdown("---")

idols = {
    "명재현": {"group": "BOYNEXTDOOR", "position": "리더, 메인보컬", "youtube": "https://www.youtube.com/watch?v=zhkuZsLY-3g"},
    "리우": {"group": "BOYNEXTDOOR", "position": "리드보컬", "youtube": "https://www.youtube.com/watch?v=_6nMvhN8Z54"},
    "성호": {"group": "BOYNEXTDOOR", "position": "리드래퍼", "youtube": "https://www.youtube.com/watch?v=Q8Tnh-nwFe8"},
    "태산": {"group": "BOYNEXTDOOR", "position": "메인래퍼", "youtube": "https://www.youtube.com/watch?v=Go9Hv5aLW6Y"},
    "이한": {"group": "BOYNEXTDOOR", "position": "메인댄서", "youtube": "https://www.youtube.com/watch?v=ptH3I1swWKU"},
    "운학": {"group": "BOYNEXTDOOR", "position": "서브보컬, 서브댄서", "youtube": "https://www.youtube.com/watch?v=L2okFxnSX98"},

    "정국": {"group": "BTS", "position": "메인보컬, 리드댄서", "youtube": "https://www.youtube.com/watch?v=kXpOEzNZ8hQ"},
    "뷔": {"group": "BTS", "position": "비주얼, 리드댄서", "youtube": "https://www.youtube.com/watch?v=MBdVXkSdhwU"},
    "RM": {"group": "BTS", "position": "리더, 메인래퍼", "youtube": "https://www.youtube.com/watch?v=1jsKo3OkI8s"},

    "백현": {"group": "EXO", "position": "메인보컬", "youtube": "https://www.youtube.com/watch?v=pSudEWBAYRE"},
    "카이": {"group": "EXO", "position": "메인댄서, 서브보컬", "youtube": "https://www.youtube.com/watch?v=KpJA53fL6DQ"},

    "태용": {"group": "NCT", "position": "리더, 리드래퍼", "youtube": "https://www.youtube.com/watch?v=3qEcc-dj0r0"},
    "재민": {"group": "NCT", "position": "리드보컬", "youtube": "https://www.youtube.com/watch?v=OtVI0vILGvE"},

    "방찬": {"group": "Stray Kids", "position": "리더, 리드래퍼", "youtube": "https://www.youtube.com/watch?v=mhXq5_rDD6A"},
    "현진": {"group": "Stray Kids", "position": "비주얼, 리드댄서", "youtube": "https://www.youtube.com/watch?v=9p3d_j7QpJo"},

    "원우": {"group": "SEVENTEEN", "position": "리드댄서, 서브보컬", "youtube": "https://www.youtube.com/watch?v=Pt9fX7tLvJg"},
    "민규": {"group": "SEVENTEEN", "position": "메인래퍼", "youtube": "https://www.youtube.com/watch?v=GY8tICpE1pM"},
}

mode = st.sidebar.radio("추천 방식 선택", ["랜덤 추천", "직접 선택"])

if mode == "랜덤 추천":
    member = random.choice(list(idols.keys()))
    st.markdown(f"<h2 style='text-align:center; color:#720026;'>🎉 오늘의 추천 아이돌: {member} ({idols[member]['group']}) 🎉</h2>", unsafe_allow_html=True)
else:
    member = st.selectbox("좋아하는 아이돌을 선택하세요", sorted(idols.keys()))
    st.markdown(f"<h2 style='text-align:center; color:#720026;'>💖 선택한 아이돌: {member} ({idols[member]['group']}) 💖</h2>", unsafe_allow_html=True)

info = idols[member]

st.markdown(
    f"""
    ### 🏷 그룹명: {info['group']}
    ### 👑 포지션: {info['position']}
    ### 🎬 유튜브 영상: [영상 보러가기]({info['youtube']})
    ---
    {member}는 {info['group']}의 멤버로 무대 위에서 빛나는 모습을 보여줍니다! 그의 멋진 무대를 꼭 감상해보세요.
    """
)

st.markdown("---")
st.markdown("<p style='text-align:center; color: gray;'>© 2025 K-Pop Idol Recommender 💖</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
