import streamlit as st

st.set_page_config(
    page_title="Mahjong Utils",
    page_icon="🀀",
)

st.write("# Hello World! 🀀")

st.sidebar.success("Select a tool above.")

st.markdown(
    """
    # Thank you for visiting
    ## 日本の方へ
    私は**ShunDeveloper**です. このサイトはstreamlitの勉強と快適な麻雀ライフの為に作成しました.
    何かあれば[Github](https://github.com/ShunDeveloper)でお聞きください
    ## For Overseas friends
    Hello! I'm **ShunDeveloper**. I made this site for learning streamlit and good mahjong life.
    if you have any question, you can ask me at [Github](https://github.com/ShunDeveloper)
    # UPDATE
    - 2022-10-09
        - added New mode for 点数計算テスト
        - changed some title for page
    - 2022-10-17
        - fix csv file for oya_ron.csv
    - 2022-10-19
        - fix csv file for ko_ron.csv
"""
)
