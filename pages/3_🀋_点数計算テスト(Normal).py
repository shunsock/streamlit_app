import streamlit as st
import pandas as pd
import numpy as np
import random
from question.initialize import initialize

st.set_page_config(
    page_title="点数計算テスト(Normal)",
    page_icon="🀐",
)
# textがnaならTrueを返す
def isNA(text):
    flag = False
    if text=='<NA>':
        #print('NA founded')
        flag=True
    if type(text)==float:
        flag=True
        #print('NA founded')
    return flag
### session
if 'answer_normal' not in st.session_state:
    tmp_question, tmp_answer= initialize(mode='normal')
    #print(tmp_question,tmp_answer,type(tmp_answer))
    if isNA(tmp_answer):
        while isNA(tmp_answer):
            #print('looping')
            tmp_question, tmp_answer= initialize(mode='normal')
            #print(tmp_question,tmp_answer,type(tmp_answer),'looping')
        st.session_state['question_normal'], st.session_state['answer_normal'] = tmp_question, tmp_answer
    st.session_state['question_normal'], st.session_state['answer_normal'] = tmp_question, tmp_answer


### UI
st.title("点数計算テスト(Normal)")
st.write('Normalでは20符~60符の中から問題が出題されます')
st.write('問題:この手の点数を計算してください')
st.write(st.session_state['question_normal'])
agree = st.checkbox('答えを確認する',key='normal')
if agree:
    st.write('チェックボックスを外すと次の問題へ行きます')
    st.write('答え:',st.session_state['answer_normal'])
    tmp_question, tmp_answer= initialize(mode='normal')
    #print(tmp_question,tmp_answer,type(tmp_answer))
    if isNA(tmp_answer):
        while isNA(tmp_answer):
            #print('looping')
            tmp_question, tmp_answer= initialize(mode='normal')
            #print(tmp_question,tmp_answer,type(tmp_answer),'looping')
        st.session_state['question_normal'], st.session_state['answer_normal'] = tmp_question, tmp_answer
    st.session_state['question_normal'], st.session_state['answer_normal'] = tmp_question, tmp_answer