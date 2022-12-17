import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.is_na import is_na
from utils.question import question

def test_is_na_false():
    assert is_na(text=1) == False

def test_is_na_true():
    assert is_na(text='<NA>') == True
    assert is_na(text=1.3) == True

def test_question():
    for mode in ['easy','normal','hard']:
        question_, answer_ = question(mode)
        assert type(question_) == str