import streamlit as st

st.set_page_config(
    page_title="Mahjong Utils",
    page_icon="🀀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://mahjong.streamlit.app',
        'Report a bug': "https://github.com/ShunDeveloper/streamlit_app",
        'About': "mahjong calc app"
    }
)

st.write("# Mahjong Util 🀀")

st.sidebar.success("Select a tool above.")

st.markdown(
    """
## 日本の方へ
私はShunDeveloperです. このサイトはstreamlitの勉強と快適な麻雀ライフの為に作成しました. 何かあればGithubでお聞きください

- Site: [mahjong.streamlit.app](https://mahjong.streamlit.app/)
- Contact: [GitHub](https://github.com/ShunDeveloper/streamlit_app)

## For Overseas friends
Hello! I'm ShunDeveloper. I made this site for learning streamlit and good mahjong life. if you have any question, you can ask me at Github

- Site: [mahjong.streamlit.app](https://mahjong.streamlit.app/)
- Contact: [GitHub](https://github.com/ShunDeveloper/streamlit_app)

# UPDATE
- 2022-10-09
    - added New mode for 点数計算テスト
    - changed some title for page
- 2022-10-17
    - fix csv file for oya_ron.csv
- 2022-10-19
    - fix csv file for ko_ron.csv
- 2022-11-19
    - change app subdomain
    - change app documentation file
- 2022-12-16
    - security update
    - refactoring
- 2022-12-17
    - add testing with GitHub Actions
    - change csv file for future update: visualizing
"""
)
