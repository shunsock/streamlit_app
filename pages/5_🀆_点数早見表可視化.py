import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="点数早見表",
    page_icon="🀐",
)

DATA_DIR = 'data/'

KO_RON_DF = pd.read_csv(DATA_DIR+'ko_ron.csv', index_col=0, dtype='int').T
OYA_RON_DF = pd.read_csv(DATA_DIR+'oya_ron.csv', index_col=0, dtype='int').T
OYA_TUMO_DF = pd.read_csv(DATA_DIR+'oya_tumo.csv', index_col=0, dtype='int').T

KO_TUMO_FOR_OYA_DF = pd.read_csv(DATA_DIR+'ko_tumo_for_oya.csv', index_col=0, dtype='int').T
KO_TUMO_FOR_KO_DF = pd.read_csv(DATA_DIR+'ko_tumo_for_ko.csv', index_col=0, dtype='int').T
tmp = []
for i in range(len(KO_TUMO_FOR_KO_DF)):
    tmp_i = []
    for j in range(13):
        tmp_ij = KO_TUMO_FOR_KO_DF.iloc[i,j]+KO_TUMO_FOR_OYA_DF.iloc[i,j]
        tmp_i.append(tmp_ij)
    tmp.append(tmp_i)

# str型で読みこんでいるのでconcatできる
KO_TUMO_DF = pd.DataFrame(
    tmp,
    columns=KO_TUMO_FOR_OYA_DF.columns,
    index=KO_TUMO_FOR_OYA_DF.index,
    dtype='int'
)


### UI
st.title("点数早見表")

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
sns.set_context("talk", 0.5, {"lines.linewidth": 2})
sns.set_palette("cool", 13, 0.8)

st.subheader("子: ロン和了")
look_ko_ron = st.checkbox('LOOK IT!',key='ko_ron')
if look_ko_ron:
    fig, ax = plt.subplots()
    plots = [
        ax.plot(
            KO_RON_DF.loc[i]
        )
        for i in KO_RON_DF.index.values
    ]
    ax.set_xlabel('Han')
    ax.set_ylabel('Point')
    ax.legend(KO_RON_DF.index.values)

    st.pyplot(fig)

st.subheader("子: 自摸和了")
look_ko_tumo = st.checkbox('LOOK IT!',key='ko_tumo')
if look_ko_tumo:
    fig, ax = plt.subplots()
    plots = [
        ax.plot(
            KO_TUMO_DF.loc[i]
        )
        for i in KO_TUMO_DF.index.values
    ]
    ax.set_xlabel('Han')
    ax.set_ylabel('Point')
    ax.legend(KO_TUMO_DF.index.values)

    st.pyplot(fig)

st.subheader("親: ロン和了")
look_ko_ron = st.checkbox('LOOK IT!',key='oya_ron')
if look_ko_ron:
    fig, ax = plt.subplots()
    plots = [
        ax.plot(
            OYA_RON_DF.loc[i]
        )
        for i in OYA_RON_DF.index.values
    ]
    ax.set_xlabel('Han')
    ax.set_ylabel('Point')
    ax.legend(OYA_RON_DF.index.values)

    st.pyplot(fig)

st.subheader("親: 自摸和了")
look_ko_tumo = st.checkbox('LOOK IT!',key='oya_tumo')
if look_ko_tumo:
    fig, ax = plt.subplots()
    plots = [
        ax.plot(
            OYA_TUMO_DF.loc[i]
        )
        for i in OYA_TUMO_DF.index.values
    ]
    ax.set_xlabel('Han')
    ax.set_ylabel('Point')
    ax.legend(OYA_TUMO_DF.index.values)

    st.pyplot(fig)