if [ -d "$PWD/env" ]; then
    echo "$PWD/env exists."
else 
    echo "$PWD/env does not exist."
    python3 -m pip install virtualenv
    virtualenv env
fi
source env/bin/activate
pip install -r requirements.txt
python3 main.py
