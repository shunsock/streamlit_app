import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="点数早見表",
    page_icon="🀐",
)

DATA_DIR = "data/"

KO_RON_DF = pd.read_csv(DATA_DIR + "ko_ron.csv", index_col=0, dtype="str").T
KO_RON_DF = KO_RON_DF.applymap(
    lambda x: "<NA>" if x == "0" else str(x)
)  # dtype strで読みこんでいる為
KO_RON_DF.index = [obj + "符" for obj in KO_RON_DF.index]
KO_RON_DF.columns = index = [str(i) + "翻" for i in range(1, 14)]

OYA_RON_DF = pd.read_csv(DATA_DIR + "oya_ron.csv", index_col=0, dtype="str").T
OYA_RON_DF = OYA_RON_DF.applymap(lambda x: "<NA>" if x == "0" else str(x))
OYA_RON_DF.index = [obj + "符" for obj in OYA_RON_DF.index]
OYA_RON_DF.columns = index = [str(i) + "翻" for i in range(1, 14)]

OYA_TUMO_DF = pd.read_csv(DATA_DIR + "oya_tumo.csv", index_col=0, dtype="str").T
OYA_TUMO_DF = OYA_TUMO_DF.applymap(lambda x: "<NA>" if x == "0" else str(x) + " all")
OYA_TUMO_DF.index = [obj + "符" for obj in OYA_TUMO_DF.index]
OYA_TUMO_DF.columns = index = [str(i) + "翻" for i in range(1, 14)]

KO_TUMO_FOR_OYA_DF = pd.read_csv(
    DATA_DIR + "ko_tumo_for_oya.csv", index_col=0, dtype="str"
).T
KO_TUMO_FOR_KO_DF = pd.read_csv(
    DATA_DIR + "ko_tumo_for_ko.csv", index_col=0, dtype="str"
).T
# str型で読みこんでいるのでconcatできる
KO_TUMO_DF = pd.DataFrame(
    KO_TUMO_FOR_KO_DF.values + "-" + KO_TUMO_FOR_OYA_DF.values,
    columns=KO_TUMO_FOR_OYA_DF.columns,
    index=KO_TUMO_FOR_OYA_DF.index,
    dtype="str",
)

KO_TUMO_DF = KO_TUMO_DF.applymap(lambda x: "<NA>" if x == "0-0" else str(x))
KO_TUMO_DF.index = [obj + "符" for obj in KO_TUMO_DF.index]
KO_TUMO_DF.columns = index = [str(i) + "翻" for i in range(1, 14)]


# UI
st.title("点数早見表")

transpose = st.checkbox("行と列を入れ替える")

if transpose:
    KO_RON_DF = KO_RON_DF.T
    KO_TUMO_DF = KO_TUMO_DF.T
    OYA_RON_DF = OYA_RON_DF.T
    OYA_TUMO_DF = OYA_TUMO_DF.T

st.header("子の点数")
st.subheader("ロン和了")
st.caption("まずはここから覚えましょう")
st.dataframe(KO_RON_DF, use_container_width=True)

st.subheader("ツモ和了")
st.caption("子のロンを2で割ると親への請求, 4で割ると子への請求になります")
st.dataframe(KO_TUMO_DF, use_container_width=True)

st.header("親の点数")
st.subheader("ロン和了")
st.caption("子のロンのおおよそ1.5倍です")
st.dataframe(OYA_RON_DF, use_container_width=True)

st.subheader("ツモ和了")
st.caption("親のツモ和了は子のツモの親被りと同じだけ子全員に請求します")
st.dataframe(OYA_TUMO_DF, use_container_width=True)
