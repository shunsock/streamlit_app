import os

import requests
import time
import re

ROOT_URL = 'http://localhost:8501'

PAGE_PATH = "pages/"
PAGE_NAMES = []
tmp = os.listdir(PAGE_PATH) # get file name
assert 0 < len(tmp) # confirm
for i in range(len(tmp)):
    file_name = tmp[i]
    file_name = re.sub(r'[0-9]+_', '', file_name)
    file_name = re.sub(r'.py', '', file_name)
    PAGE_NAMES.append(file_name)

def test_app_root():
    print()
    print('WORKING TEST: root page')
    time.sleep(2)
    res = requests.get(ROOT_URL)
    res = str(res)
    assert '<Response [200]>' == res
    print('='*30)

def test_app_page():
    print('WORKING TEST: page under pages dir')
    for page_name in PAGE_NAMES:
        print('page name:', page_name)
        time.sleep(2)
        res = requests.get(ROOT_URL+'/'+page_name)
        res = str(res)
        assert '<Response [200]>' == res
    print('='*30)

def test_app_page():
    print('WORKING TEST: Not Found Request')
    time.sleep(2)
    res = requests.get(ROOT_URL+'/hoge')
    res = str(res)
    assert '<Response [404]>' == res
    print('='*30)