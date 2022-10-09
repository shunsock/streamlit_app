import streamlit as st
import pandas as pd
import numpy as np
import random
from question.initialize import initialize

st.set_page_config(
    page_title="点数早見表",
    page_icon="🀐",
)

### session
if 'answer_easy' not in st.session_state:
    st.session_state['question_easy'], st.session_state['answer_easy'] = initialize(mode='easy')


### UI
st.title("点数計算テスト")
st.write('Easyでは20符~30符の中から問題が出題されます')
st.write('問題:この手の点数を計算してください')
st.write(st.session_state['question_easy'])
agree = st.checkbox('答えを確認する',key='easy')
if agree:
    st.write('チェックボックスを外すと次の問題へ行きます')
    st.write('答え:',st.session_state['answer_easy'])
    st.session_state['question_easy'], st.session_state['answer_easy'] = initialize(mode='easy')