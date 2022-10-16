import streamlit as st
import pandas as pd
import numpy as np
import random
from question.initialize import initialize

st.set_page_config(
    page_title="点数計算テスト(Hard)",
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
if 'answer' not in st.session_state:
    tmp_question, tmp_answer= initialize(mode='hard')
    #print(tmp_question,tmp_answer,type(tmp_answer))
    if isNA(tmp_answer):
        while isNA(tmp_answer):
            #print('looping')
            tmp_question, tmp_answer= initialize(mode='hard')
            #print(tmp_question,tmp_answer,type(tmp_answer),'looping')
        st.session_state['question_hard'], st.session_state['answer_hard'] = tmp_question, tmp_answer
    st.session_state['question_hard'], st.session_state['answer_hard'] = tmp_question, tmp_answer

### UI
st.title("点数計算テスト")
st.write('問題:この手の点数を計算してください')
st.write(st.session_state['question_hard'],key='hard')
agree = st.checkbox('答えを確認する')
if agree:
    st.write('チェックボックスを外すと次の問題へ行きます')
    st.write('答え:',st.session_state['answer_hard'])
    tmp_question, tmp_answer= initialize(mode='hard')
    #print(tmp_question,tmp_answer,type(tmp_answer))
    if isNA(tmp_answer):
        while isNA(tmp_answer):
            #print('looping')
            tmp_question, tmp_answer= initialize(mode='hard')
            #print(tmp_question,tmp_answer,type(tmp_answer),'looping')
        st.session_state['question_hard'], st.session_state['answer_hard'] = tmp_question, tmp_answer
    st.session_state['question_hard'], st.session_state['answer_hard'] = tmp_question, tmp_answer