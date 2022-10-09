import streamlit as st
import pandas as pd
import numpy as np
import random
from question.initialize import initialize

st.set_page_config(
    page_title="点数計算テスト(Hard)",
    page_icon="🀐",
)

### session
if 'answer' not in st.session_state:
    st.session_state['question_hard'], st.session_state['answer_hard'] = initialize(mode='hard')

### UI
st.title("点数計算テスト")
st.write('問題:この手の点数を計算してください')
st.write(st.session_state['question_hard'],key='hard')
agree = st.checkbox('答えを確認する')
if agree:
    st.write('チェックボックスを外すと次の問題へ行きます')
    st.write('答え:',st.session_state['answer_hard'])
    st.session_state['question_hard'], st.session_state['answer_hard'] = initialize(mode='hard')