import streamlit as st
import pandas as pd
import numpy as np
import random
from question.initialize import initialize

st.set_page_config(
    page_title="点数計算テスト(Easy)",
    page_icon="🀐",
)

### session
if 'answer_normal' not in st.session_state:
    st.session_state['question_normal'], st.session_state['answer_normal'] = initialize(mode='normal')


### UI
st.title("点数計算テスト(Normal)")
st.write('Normalでは20符~60符の中から問題が出題されます')
st.write('問題:この手の点数を計算してください')
st.write(st.session_state['question_normal'])
agree = st.checkbox('答えを確認する',key='normal')
if agree:
    st.write('チェックボックスを外すと次の問題へ行きます')
    st.write('答え:',st.session_state['answer_normal'])
    st.session_state['question_normal'], st.session_state['answer_normal'] = initialize(mode='normal')