import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.is_na import is_na
from utils.question import question

def test_is_na_false():
    print()
    print('FUNCTION WORKING TEST: is_na (output must be false)')
    assert is_na(text="1000") == False
    print('='*30)

def test_is_na_true():
    print('FUNCTION WORKING TEST: is_na (output must true)')
    assert is_na(text="<NA>") == True
    assert is_na(text=1.3) == True
    print('='*30)

def test_question():
    print('FUNCTION WORKING TEST: question')
    for mode in ['easy','normal','hard']:
        question_, answer_ = question(mode)
        assert type(question_) == str
    print('='*30)