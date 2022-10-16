import pandas as pd
import random

data_dir = 'data/'
ko_ron_df = pd.read_csv(data_dir+'ko_ron.csv', index_col=0, dtype='str')
ko_tumo_df = pd.read_csv(data_dir+'ko_tumo.csv', index_col=0, dtype='str')
oya_ron_df = pd.read_csv(data_dir+'oya_ron.csv', index_col=0, dtype='str')
oya_tumo_df = pd.read_csv(data_dir+'oya_tumo.csv', index_col=0, dtype='str')
oya_tumo_df = oya_tumo_df.fillna('0').applymap(lambda x: '<NA>' if x == '0' else str(x)+' all')

def initialize(mode):
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
        answer = oya_ron_df.iloc[han-1,:][str(fu)]
    if oya_or_ko == '親' and tumo_or_ron == 'ツモ':
        answer = oya_tumo_df.iloc[han-1,:][str(fu)]
    if oya_or_ko == '子' and tumo_or_ron == 'ロン':
        answer = ko_ron_df.iloc[han-1,:][str(fu)]
    if oya_or_ko == '子' and tumo_or_ron == 'ツモ':
        answer = ko_tumo_df.iloc[han-1,:][str(fu)]
    return question, answer