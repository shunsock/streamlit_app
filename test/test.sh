echo '===TEST==='

echo 'start: updating requirements in / [1/2]'
pip freeze > requirements.txt
echo 'ok: updating requirements in / [1/2]'

echo 'finish: UPDATE REQIREMENTS.TXT'

echo 'start: running app [2/2]'
nohup streamlit run app.py > log.txt 2>&1 &
echo $! > save_pid.txt # save current pid
echo 'ok: running app [2/2]'

sleep 10 # sleeping

echo 'start: shutdown [2/2]'
kill -9 `cat save_pid.txt`
rm save_pid.txt
echo 'ok: shutdown [2/2]'