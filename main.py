import streamlit as st
import random

st.set_page_config(
    page_title="최애 남자 아이돌 추천 💖",
    page_icon="🎤",
    layout="wide"
)

st.markdown("<h1 style='text-align: center; color: deeppink;'>🌟 남자 아이돌 추천 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: hotpink;'>BOYNEXTDOOR부터 BTS, EXO, NCT, Stray Kids, SEVENTEEN까지! 최애를 만나보세요 💫</h4>")
st.markdown("---")

# 아이돌 데이터
idols = {
    # BOYNEXTDOOR
    "명재현": {"group": "BOYNEXTDOOR", "image": "https://i.imgur.com/5VQYJHN.jpg", "position": "리더, 메인보컬", "youtube": "https://www.youtube.com/watch?v=zhkuZsLY-3g"},
    "리우": {"group": "BOYNEXTDOOR", "image": "https://i.imgur.com/KmQ93I6.jpg", "position": "리드보컬", "youtube": "https://www.youtube.com/watch?v=_6nMvhN8Z54"},
    "성호": {"group": "BOYNEXTDOOR", "image": "https://i.imgur.com/WQ2Ra6k.jpg", "position": "리드래퍼", "youtube": "https://www.youtube.com/watch?v=Q8Tnh-nwFe8"},
    "태산": {"group": "BOYNEXTDOOR", "image": "https://i.imgur.com/bFGVIV6.jpg", "position": "메인래퍼", "youtube": "https://www.youtube.com/watch?v=Go9Hv5aLW6Y"},
    "이한": {"group": "BOYNEXTDOOR", "image": "https://i.imgur.com/RTYAH1x.jpg", "position": "메인댄서", "youtube": "https://www.youtube.com/watch?v=ptH3I1swWKU"},
    "운학": {"group": "BOYNEXTDOOR", "image": "https://i.imgur.com/srs0yx3.jpg", "position": "서브보컬, 서브댄서", "youtube": "https://www.youtube.com/watch?v=L2okFxnSX98"},

    # BTS
    "정국": {"group": "BTS", "image": "https://i.imgur.com/0UuGxVA.jpg", "position": "메인보컬, 리드댄서", "youtube": "https://www.youtube.com/watch?v=kXpOEzNZ8hQ"},
    "뷔": {"group": "BTS", "image": "https://i.imgur.com/7KJ3TqG.jpg", "position": "비주얼, 리드댄서", "youtube": "https://www.youtube.com/watch?v=MBdVXkSdhwU"},
    "RM": {"group": "BTS", "image": "https://i.imgur.com/oh14CSP.jpg", "position": "리더, 메인래퍼", "youtube": "https://www.youtube.com/watch?v=1jsKo3OkI8s"},

    # EXO
    "백현": {"group": "EXO", "image": "https://i.imgur.com/fnTCNVR.jpg", "position": "메인보컬", "youtube": "https://www.youtube.com/watch?v=pSudEWBAYRE"},
    "카이": {"group": "EXO", "image": "https://i.imgur.com/tkVq3lv.jpg", "position": "메인댄서, 서브보컬", "youtube": "https://www.youtube.com/watch?v=KpJA53fL6DQ"},

    # NCT
    "태용": {"group": "NCT", "image": "https://i.imgur.com/5mAJgwE.jpg", "position": "리더, 리드래퍼", "youtube": "https://www.youtube.com/watch?v=3qEcc-dj0r0"},
    "재민": {"group": "NCT", "image": "https://i.imgur.com/qbhL0Fg.jpg", "position": "리드보컬", "youtube": "https://www.youtube.com/watch?v=OtVI0vILGvE"},

    # Stray Kids
    "방찬": {"group": "Stray Kids", "image": "https://i.imgur.com/3G9TiIt.jpg", "position": "리더, 리드래퍼", "youtube": "https://www.youtube.com/watch?v=mhXq5_rDD6A"},
    "현진": {"group": "Stray Kids", "image": "https://i.imgur.com/7tCgmpW.jpg", "position": "비주얼, 리드댄서", "youtube": "https://www.youtube.com/watch?v=9p3d_j7QpJo"},

    # SEVENTEEN
    "원우": {"group": "SEVENTEEN", "image": "https://i.imgur.com/Y96OqKh.jpg", "position": "리드댄서, 서브보컬", "youtube": "https://www.youtube.com/watch?v=Pt9fX7tLvJg"},
    "민규": {"group": "SEVENTEEN", "image": "https://i.imgur.com/E9JhQOq.jpg", "position": "메인래퍼", "youtube": "https://www.youtube.com/watch?v=GY8tICpE1pM"},
}

# 추천 방식 선택
mode = st.sidebar.radio("추천 방식 선택", ["랜덤 추천", "직접 선택"])

if mode == "랜덤 추천":
    member = random.choice(list(idols.keys()))
    st.markdown(f"<h2 style='text-align: center; color: mediumvioletred;'>🎉 오늘의 추천 아이돌: {member} ({idols[member]['group']}) 🎉</h2>", unsafe_allow_html=True)
else:
    member = st.selectbox("좋아하는 아이돌을 선택하세요", sorted(idols.keys()))
    st.markdown(f"<h2 style='text-align: center; color: mediumvioletred;'>💖 선택한 아이돌: {member} ({idols[member]['group']}) 💖</h2>", unsafe_allow_html=True)

info = idols[member]

col1, col2 = st.columns([1, 2])
with col1:
    st.image(info["image"], caption=f"{member} - {info['position']}", use_column_width=True)

with col2:
    st.markdown(f"""
    ### 🏷 그룹명: {info['group']}
    ### 👑 포지션: {info['position']}
    ### 🎬 유튜브 영상: [바로가기]({info['youtube']})
    ---
    {member}는 {info['group']}의 멤버로, 무대 위에서 빛나는 모습을 보여줍니다!  
    그의 멋진 무대를 꼭 감상해보세요.
    """)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2025 K-Pop Idol Recommender 💖</p>", unsafe_allow_html=True)

