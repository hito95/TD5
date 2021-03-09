virtualenv -q -p /usr/bin/python3.8 $1
source $1/bin/activate
$1/bin/pip install -r requirements.txt
