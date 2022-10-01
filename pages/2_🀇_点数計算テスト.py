import streamlit as st
import pandas as pd
import numpy as np
import random

st.set_page_config(
    page_title="点数早見表",
    page_icon="🀐",
)

data_dir = 'data/'
ko_ron_df = pd.read_csv(data_dir+'ko_ron.csv', index_col=0, dtype='str')
ko_tumo_df = pd.read_csv(data_dir+'ko_tumo.csv', index_col=0, dtype='str')
oya_ron_df = pd.read_csv(data_dir+'oya_ron.csv', index_col=0, dtype='str')
oya_tumo_df = pd.read_csv(data_dir+'oya_tumo.csv', index_col=0, dtype='str')
oya_tumo_df = oya_tumo_df.fillna('0').applymap(lambda x: '<NA>' if x == '0' else str(x)+' all')

def question():
    oya_or_ko = random.choice(['親','子'])
    tumo_or_ron = random.choice(['ツモ','ロン'])
    han = random.choice(list(range(1,5)))
    fu = random.choice(list(range(20,120,10)))
    question_sentence = str(han) + '翻' + str(fu) + '符, ' + oya_or_ko + 'の' + tumo_or_ron + '和了'
    st.write(question_sentence)
    answer=-1
    if oya_or_ko == '親' and tumo_or_ron == 'ロン':
        st.session_state.answer = oya_ron_df.iloc[han-1,:][str(fu)]
    if oya_or_ko == '親' and tumo_or_ron == 'ツモ':
        st.session_state.answer = oya_tumo_df.iloc[han-1,:][str(fu)]
    if oya_or_ko == '子' and tumo_or_ron == 'ロン':
        st.session_state.answer = ko_ron_df.iloc[han-1,:][str(fu)]
    if oya_or_ko == '子' and tumo_or_ron == 'ツモ':
        st.session_state.answer = ko_tumo_df.iloc[han-1,:][str(fu)]

### session
if 'answer' not in st.session_state:
    st.session_state['answer'] = '-1'
    st.session_state['your_answer'] = '-1'

### UI
st.title("点数計算テスト")
if st.button('問題を出題',key='set_question'):
    st.write('この手の点数を計算してください')
    question()
    st.session_state.your_answer = st.text_input('please input your answer')
else:
    st.write('ボタンを押すと問題が出題されます')