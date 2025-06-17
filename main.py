import streamlit as st
from PIL import Image
import random

# 웹 페이지 설정
st.set_page_config(
    page_title="K-Idol Recommender 💫",
    page_icon="🌟",
    layout="wide"
)

# 타이틀 영역
st.markdown("<h1 style='text-align: center; color: hotpink;'>🌟 K-Idol Recommender 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>당신의 취향 저격! 아이돌 추천 받으세요 💖</h4>", unsafe_allow_html=True)
st.markdown("---")

# 아이돌 정보 딕셔너리 (보넥도 포함)
idols = {
    "정국 (BTS)": {
        "image": "https://i.imgur.com/0UuGxVA.jpg",
        "group": "BTS",
        "youtube": "https://www.youtube.com/watch?v=kXpOEzNZ8hQ"
    },
    "민호 (SHINee)": {
        "image": "https://i.imgur.com/OdqegMj.jpg",
        "group": "SHINee",
        "youtube": "https://www.youtube.com/watch?v=6yIDlvdGQGI"
    },
    "차은우 (ASTRO)": {
        "image": "https://i.imgur.com/3qQHBRh.jpg",
        "group": "ASTRO",
        "youtube": "https://www.youtube.com/watch?v=3AJS0ZWRNbs"
    },
    "뷔 (BTS)": {
        "image": "https://i.imgur.com/7KJ3TqG.jpg",
        "group": "BTS",
        "youtube": "https://www.youtube.com/watch?v=MBdVXkSdhwU"
    },
    "백현 (EXO)": {
        "image": "https://i.imgur.com/fnTCNVR.jpg",
        "group": "EXO",
        "youtube": "https://www.youtube.com/watch?v=pSudEWBAYRE"
    },
    "보넥도 (BONNECDEAU)": {
        "image": "https://i.imgur.com/POuO5VI.jpg",  # 임시 이미지
        "group": "BONNECDEAU",
        "youtube": "https://www.youtube.com/@bonnecdeau"  # 예시 채널
    }
}

# 추천 방식 선택
option = st.sidebar.radio("💘 추천 방식", ["랜덤 추천", "아이돌 직접 선택"])

# 추천 기능
if option == "랜덤 추천":
    selected = random.choice(list(idols.keys()))
    st.markdown(f"<h2 style='text-align: center;'>✨ 오늘의 추천 아이돌: <span style='color: deeppink;'>{selected}</span> ✨</h2>", unsafe_allow_html=True)
else:
    selected = st.selectbox("⭐ 좋아하는 아이돌을 선택하세요", list(idols.keys()))
    st.markdown(f"<h2 style='text-align: center;'>💖 당신이 선택한 아이돌: <span style='color: dodgerblue;'>{selected}</span> 💖</h2>", unsafe_allow_html=True)

# 선택된 아이돌 정보 표시
idol = idols[selected]
col1, col2 = st.columns([1, 2])

with col1:
    st.image(idol["image"], caption=f"{selected} - {idol['group']}", use_column_width=True)

with col2:
    st.markdown(f"""
        ### 📌 그룹: {idol['group']}
        ### 🔗 [유튜브 채널 보기]({idol['youtube']})
        ---
        🎤 <span style='color: pink'><strong>{selected}</strong></span>는 {idol['group']}의 인기 멤버예요!  
        💫 특별한 매력과 무대를 함께 감상해보세요~
    """, unsafe_allow_html=True)

# 하단 표시
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2025 Made with 💖 by K-pop Lovers</p>", unsafe_allow_html=True)

