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

def initialize():
    oya_or_ko = random.choice(['親','子'])
    tumo_or_ron = random.choice(['ツモ','ロン'])
    han = random.choice(list(range(1,5)))
    fu = random.choice(list(range(20,120,10)))
    question = str(han) + '翻' + str(fu) + '符, ' + oya_or_ko + 'の' + tumo_or_ron + '和了'
    if oya_or_ko == '親' and tumo_or_ron == 'ロン':
        answer = oya_ron_df.iloc[han-1,:][str(fu)]
    if oya_or_ko == '親' and tumo_or_ron == 'ツモ':
        answer = oya_tumo_df.iloc[han-1,:][str(fu)]
    if oya_or_ko == '子' and tumo_or_ron == 'ロン':
        answer = ko_ron_df.iloc[han-1,:][str(fu)]
    if oya_or_ko == '子' and tumo_or_ron == 'ツモ':
        answer = ko_tumo_df.iloc[han-1,:][str(fu)]
    return question, answer

### session
if 'answer' not in st.session_state:
    st.session_state['question'], st.session_state['answer'] = initialize()


### UI
st.title("点数計算テスト")
st.write('この手の点数を計算してください')
st.write(st.session_state['question'])
agree = st.checkbox('答えを確認する')
if agree:
    st.write('チェックボックスを外すと次の問題へ行きます')
    st.write('答え:',st.session_state['answer'])
    st.session_state['question'], st.session_state['answer'] = initialize()