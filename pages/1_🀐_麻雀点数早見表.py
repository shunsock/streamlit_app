import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="点数早見表",
    page_icon="🀐",
)

data_dir = 'data/'
ko_ron_df = pd.read_csv(data_dir+'ko_ron.csv', index_col=0, dtype='str').T
ko_tumo_df = pd.read_csv(data_dir+'ko_tumo.csv', index_col=0, dtype='str').T
oya_ron_df = pd.read_csv(data_dir+'oya_ron.csv', index_col=0, dtype='str').T
oya_tumo_df = pd.read_csv(data_dir+'oya_tumo.csv', index_col=0, dtype='str').T
oya_tumo_df = oya_tumo_df.fillna('0').applymap(lambda x: '<NA>' if x == '0' else str(x)+' all')

### UI
st.title("点数早見表")

transpose = st.checkbox('行と列を入れ替える')

if transpose:
    ko_ron_df = ko_ron_df.T
    ko_tumo_df = ko_tumo_df.T
    oya_ron_df = oya_ron_df.T
    oya_tumo_df = oya_tumo_df.T

st.header("子の点数")
st.subheader("ロン和了")
st.caption('まずはここから覚えましょう')
st.dataframe(ko_ron_df,use_container_width=True)

st.subheader("ツモ和了")
st.caption('子のロンを2で割ると親への請求, 4で割ると子への請求になります')
st.dataframe(ko_tumo_df,use_container_width=True)

st.header("親の点数")
st.subheader("ロン和了")
st.caption('子のロンのおおよそ1.5倍です')
st.dataframe(oya_ron_df,use_container_width=True)

st.subheader("ツモ和了")
st.caption('親のツモ和了は子のツモの親被りと同じだけ子全員に請求します')

st.dataframe(oya_tumo_df,use_container_width=True)
st.sidebar.success("Select a demo above.")

