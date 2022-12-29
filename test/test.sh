echo 'start: running app [1/3]'
nohup poetry run streamlit run app.py > log.txt 2>&1 &
echo $! > save_pid.txt # save current pid
echo 'ok: running app [1/3]'

echo 'start: testing [2/3]'
pytest -s
echo 'ok: testing [2/3]'

echo 'start: shutdown [3/3]'
kill -9 `cat save_pid.txt`
rm save_pid.txt
echo 'ok: shutdown [3/3]'
