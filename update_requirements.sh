echo '===UPDATE REQIREMENTS.TXT==='

echo 'start: updating requirements in / [1/2]'
pip freeze > requirements.txt
echo 'ok: updating requirements in / [1/2]'

echo 'start: updating requirements in /tests/ [2/2]'
pip freeze > tests/requirements.txt
echo 'ok: updating requirements in /tests/ [2/2]'

echo 'finish: UPDATE REQIREMENTS.TXT'