import pandas as pd
import random

DATA_DIR = 'data/'
KO_RON_DF = pd.read_csv(DATA_DIR+'ko_ron.csv', index_col=0, dtype='str')
KO_RON_DF = KO_RON_DF.applymap(lambda x: '<NA>' if x == '0' else str(x)) # dtype strで読みこんでいる為
OYA_RON_DF = pd.read_csv(DATA_DIR+'oya_ron.csv', index_col=0, dtype='str')
OYA_RON_DF = OYA_RON_DF.applymap(lambda x: '<NA>' if x == '0' else str(x))
OYA_TUMO_DF = pd.read_csv(DATA_DIR+'oya_tumo.csv', index_col=0, dtype='str')
OYA_TUMO_DF = OYA_TUMO_DF.applymap(lambda x: '<NA>' if x == '0' else str(x)+' all')

KO_TUMO_FOR_OYA_DF = pd.read_csv(DATA_DIR+'ko_tumo_for_oya.csv', index_col=0, dtype='str')
KO_TUMO_FOR_KO_DF = pd.read_csv(DATA_DIR+'ko_tumo_for_ko.csv', index_col=0, dtype='str')
# str型で読みこんでいるのでconcatできる
KO_TUMO_DF = pd.DataFrame(
    KO_TUMO_FOR_KO_DF.values+'-'+KO_TUMO_FOR_OYA_DF.values,
    columns=KO_TUMO_FOR_OYA_DF.columns,
    index=KO_TUMO_FOR_OYA_DF.index,
    dtype='str'
)
KO_TUMO_DF = KO_TUMO_DF.applymap(lambda x: '<NA>' if x == '0-0' else str(x))

def question(mode):
    oya_or_ko = random.choice(['親','子'])
    tumo_or_ron = random.choice(['ツモ','ロン'])
    han = random.choice(list(range(1,5)))
    if mode == 'easy':
        fu = random.choice([20,25,30])
    elif mode == 'normal':
        fu_list = list(range(20,70,10))
        fu_list.append(25)
        fu = random.choice(fu_list)
    elif mode == 'hard':
        fu_list = list(range(20,120,10))
        fu_list.append(25)
        fu = random.choice(fu_list)
    question = str(han) + '翻' + str(fu) + '符, ' + oya_or_ko + 'の' + tumo_or_ron + '和了'
    if oya_or_ko == '親' and tumo_or_ron == 'ロン':
        answer = OYA_RON_DF.iloc[han-1,:][str(fu)]
    if oya_or_ko == '親' and tumo_or_ron == 'ツモ':
        answer = OYA_TUMO_DF.iloc[han-1,:][str(fu)]
    if oya_or_ko == '子' and tumo_or_ron == 'ロン':
        answer = KO_RON_DF.iloc[han-1,:][str(fu)]
    if oya_or_ko == '子' and tumo_or_ron == 'ツモ':
        answer = KO_TUMO_DF.iloc[han-1,:][str(fu)]
    return question, answer