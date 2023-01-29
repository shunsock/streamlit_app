import pandas as pd
import random
from typing import Tuple

# reading csv data
DATA_DIR = "data/"
# 子, ロン
KO_RON_DF = pd.read_csv(DATA_DIR + "ko_ron.csv", index_col=0, dtype="str")
KO_RON_DF = KO_RON_DF.applymap(
    lambda x: "<NA>" if x == "0" else str(x)
)  # dtype strで読みこんでいる為
# 子, 自摸
KO_TUMO_FOR_OYA_DF = pd.read_csv(
    DATA_DIR + "ko_tumo_for_oya.csv", index_col=0, dtype="str"
)
KO_TUMO_FOR_KO_DF = pd.read_csv(
    DATA_DIR + "ko_tumo_for_ko.csv", index_col=0, dtype="str"
)
# (concat dataframe)
KO_TUMO_DF = pd.DataFrame(
    KO_TUMO_FOR_KO_DF.values + "-" + KO_TUMO_FOR_OYA_DF.values,
    columns=KO_TUMO_FOR_OYA_DF.columns,
    index=KO_TUMO_FOR_OYA_DF.index,
    dtype="str",
)
KO_TUMO_DF = KO_TUMO_DF.applymap(lambda x: "<NA>" if x == "0-0" else str(x))
# 親, ロン
OYA_RON_DF = pd.read_csv(DATA_DIR + "oya_ron.csv", index_col=0, dtype="str")
OYA_RON_DF = OYA_RON_DF.applymap(lambda x: "<NA>" if x == "0" else str(x))
# 親, 自摸
OYA_TUMO_DF = pd.read_csv(DATA_DIR + "oya_tumo.csv", index_col=0, dtype="str")
OYA_TUMO_DF = OYA_TUMO_DF.applymap(lambda x: "<NA>" if x == "0" else str(x) + " all")


def generate_question(mode_: str) -> Tuple[str, str, int, int]:
    """
    input
        mode_ (str): easy, normal, hard
    outputs:
        class_ (str): 親か子
        win_type_ (str): 和了形
        doubles_ (int): 翻
        points_ (int): 符
    """
    class_ = random.choice(["親", "子"])
    win_type_ = random.choice(["ツモ", "ロン"])
    doubles_ = random.choice(list(range(1, 5)))

    if mode_ == "easy":
        points_ = random.choice([20, 25, 30])
    elif mode_ == "normal":
        points_list = list(range(20, 70, 10))
        points_list.append(25)
        points_ = random.choice(points_list)
    elif mode_ == "hard":
        points_list = list(range(20, 120, 10))
        points_list.append(25)
        points_ = random.choice(points_list)

    return class_, win_type_, doubles_, points_


def create_question_text(
    class_: str, win_type_: str, doubles_: int, points_: int
) -> str:
    """
    inputs:
        class_ (str): 親か子
        win_type_ (str): 和了形
        doubles_ (int): 翻
        points_ (int): 符
    outputs:
        question_text (str): 点数
    """
    question_text = (
        str(doubles_) + "翻" + str(points_) + "符, " + class_ + "の" + win_type_ + "和了"
    )
    return question_text


def create_answer_text(class_: str, win_type_: str, doubles_: int, points_: int) -> str:
    """
    inputs:
        class_ (str): 親か子
        win_type_ (str): 和了形
        doubles_ (int): 翻
        points_ (int): 符
    outputs:
        answer_text (str): 点数
    """
    if class_ == "親" and win_type_ == "ロン":
        answer_text = OYA_RON_DF.iloc[doubles_ - 1, :][str(points_)]
    if class_ == "親" and win_type_ == "ツモ":
        answer_text = OYA_TUMO_DF.iloc[doubles_ - 1, :][str(points_)]
    if class_ == "子" and win_type_ == "ロン":
        answer_text = KO_RON_DF.iloc[doubles_ - 1, :][str(points_)]
    if class_ == "子" and win_type_ == "ツモ":
        answer_text = KO_TUMO_DF.iloc[doubles_ - 1, :][str(points_)]

    return answer_text


def question(mode: str) -> Tuple[str, str]:
    class_, win_type_, doubles_, points_ = generate_question(mode)
    question = create_question_text(class_, win_type_, doubles_, points_)
    answer = create_answer_text(class_, win_type_, doubles_, points_)

    return question, answer
