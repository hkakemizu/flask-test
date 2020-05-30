# python setup

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

# db setup

```
$ python models.py
```

# run

```
$ python app.py
```

# usage

```
$ curl -X POST http://localhost:5000/timerecord/1234 -d 'type=begin'
$ curl -X POST http://localhost:5000/timerecord/1234 -d 'type=end'  
$ curl -X GET http://localhost:5000/timerecord/1234           
{"records":[{"id":1234,"time":1590802060.625858,"type":"begin"},{"id":1234,"time":1590802068.877625,"type":"end"}]}
```