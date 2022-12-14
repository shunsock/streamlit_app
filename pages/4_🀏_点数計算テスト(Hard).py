import streamlit as st
import pandas as pd
import numpy as np
import random
from utils.question import question
from utils.is_na import is_na

st.set_page_config(
    page_title="点数計算テスト(Hard)",
    page_icon="🀐",
)

GAME_MODE = 'hard'
KEY_ANSWER = 'answer_' + GAME_MODE
KEY_QUESTION = 'question_' + GAME_MODE

### session
if 'answer' not in st.session_state:
    tmp_question, tmp_answer= question(mode=GAME_MODE)
    
    if is_na(tmp_answer):
        # 存在しない翻と符の組み合わせだった場合やり直す
        # 存在する翻と符の組み合わせが得られるまで試行を繰り返す
        while is_na(tmp_answer):
            tmp_question, tmp_answer= question(mode=GAME_MODE)
    
    # 存在する翻と符の組み合わせが得られたら更新する
    st.session_state[KEY_QUESTION], st.session_state[KEY_ANSWER] = tmp_question, tmp_answer

### UI
st.title("点数計算テスト")
st.write('問題:この手の点数を計算してください')
st.write(st.session_state[KEY_QUESTION], key=GAME_MODE)
agree = st.checkbox('答えを確認する')
if agree:
    st.write('チェックボックスを外すと次の問題へ行きます')
    st.write('答え:',st.session_state[KEY_ANSWER])
    tmp_question, tmp_answer= question(mode=GAME_MODE)

    # 存在しない翻と符の組み合わせだった場合やり直す
    # 存在する翻と符の組み合わせが得られるまで試行を繰り返す
    while is_na(tmp_answer):
        tmp_question, tmp_answer= question(mode=GAME_MODE)
    
    # 存在する翻と符の組み合わせが得られたら更新する
    st.session_state[KEY_QUESTION], st.session_state[KEY_ANSWER] = tmp_question, tmp_answer