function abort
{
   echo $message 1>&2
   exit 1
}

echo 'start: Lint & Formatting [1/4]'
flake8 --extend-ignore E501 pages/ || abort "failed in Linter on pages/: fix your files with black and flake8"
flake8 --extend-ignore E501 utils/ || abort "failed in Linter on test/: fix your files with black and flake8"
flake8 --extend-ignore E402,E501 test/ || abort "failed in Linter on test/: fix your files with black and flake8"
echo 'ok: [1/4]'

echo 'start: running app [2/4]'
nohup streamlit run app.py > log.txt 2>&1 &
echo $! > save_pid.txt # save current pid
echo 'ok: [2/4]'

echo 'start: testing [3/4]'
pytest -s || abort "failed pytest: check your application"
echo 'ok: [3/4]'

echo 'start: shutdown [4/4]'
kill -9 `cat save_pid.txt`
rm save_pid.txt
rm log.txt
echo 'ok: shutdown [4/4]'
