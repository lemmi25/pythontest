# python-test
simple python package

```
pip3 install -e .
```
```
from python_test import greeting
test = greeting.Employee("Hans",1000)
test.displayCount()
test.displayEmployee()
```

gunicorn --workers 3 --bind unix:test.sock -m 007 /usr/lib/python3.9/site-packages/python_test/wsgi:app
