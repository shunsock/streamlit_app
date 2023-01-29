import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="点数早見表",
    page_icon="🀐",
)

# reading data from csv
DATA_DIR = "data/"

OYA_RON_DF = pd.read_csv(DATA_DIR + "oya_ron.csv", index_col=0, dtype="int").T
OYA_TUMO_DF = (
    pd.read_csv(DATA_DIR + "oya_tumo.csv", index_col=0, dtype="int")
    .applymap(lambda x: x * 3)
    .T
)
KO_RON_DF = pd.read_csv(DATA_DIR + "ko_ron.csv", index_col=0, dtype="int").T
KO_TUMO_FOR_OYA_DF = pd.read_csv(
    DATA_DIR + "ko_tumo_for_oya.csv", index_col=0, dtype="int"
).T
KO_TUMO_FOR_KO_DF = pd.read_csv(
    DATA_DIR + "ko_tumo_for_ko.csv", index_col=0, dtype="int"
).T
tmp = []
for i in range(len(KO_TUMO_FOR_KO_DF)):
    tmp_i = []
    for j in range(13):
        tmp_ij = KO_TUMO_FOR_KO_DF.iloc[i, j] + KO_TUMO_FOR_OYA_DF.iloc[i, j]
        tmp_i.append(tmp_ij)
    tmp.append(tmp_i)

# str型で読みこんでいるのでconcatできる
KO_TUMO_DF = pd.DataFrame(
    tmp, columns=KO_TUMO_FOR_OYA_DF.columns, index=KO_TUMO_FOR_OYA_DF.index, dtype="int"
)


# UI COMPONENT
def show_picture(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots()
    for i in range(len(df.index.values)):
        ax.plot(df.loc[i])
    ax.set_xlabel("Han")
    ax.set_ylabel("Point")
    ax.legend(df.index.values)

    st.pyplot(fig)


# UI
st.title("点数早見表")

sns.set()
sns.set_style("whitegrid", {"grid.linestyle": "--"})
sns.set_context("talk", 0.5, {"lines.linewidth": 2})
sns.set_palette("cool", 13, 0.8)

st.subheader("子: ロン和了")
look_ko_ron = st.checkbox("LOOK IT!", key="ko_ron")
if look_ko_ron:
    show_picture(KO_RON_DF)

st.subheader("子: 自摸和了")
look_ko_tumo = st.checkbox("LOOK IT!", key="ko_tumo")
if look_ko_tumo:
    show_picture(KO_TUMO_DF)

st.subheader("親: ロン和了")
look_ko_ron = st.checkbox("LOOK IT!", key="oya_ron")
if look_ko_ron:
    show_picture(OYA_RON_DF)
st.subheader("親: 自摸和了")
look_ko_tumo = st.checkbox("LOOK IT!", key="oya_tumo")
if look_ko_tumo:
    show_picture(OYA_TUMO_DF)
