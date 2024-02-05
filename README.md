* To install, after cloning, go into the directory and run  
`python3 -m venv env`  
`. env/bin/activate`  
`pip install -r requirements`  
`flask run -p 8000`  
* To run a dummy email server on the terminal  
`python -m smtpd -n -c DebuggingServer localhost:8025`
* To run a Redis Queue worker process named `microblog-tasks`  
`rq worker microblog-tasks`
* To update the language translation, from the base directory run  
`pybabel extract -F babel.cfg -k _l -o messages.pot .`  
`pybabel update -i messages.pot -d app/translations`  
Then update `app/translations/fr/LC_MESSAGES/messages.po` to add the translations. Then run  
`pybabel compile -d app/translations`  
* To obtain a token to use the API  
`http --auth <username>:<password> POST http://localhost:5000/api/tokens`  
* To use token  
`http GET http://localhost:5000/api/<resource> "Authorization:Bearer <token>"`  
* To view API resources, browse `app/api/users.py`
* Links to tutorial  
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world-2018  
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
