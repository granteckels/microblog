* To run a dummy email server on the terminal  
`python -m smtpd -n -c DebuggingServer localhost:8025`
* To run a Redis Queue worker process named `microblog-tasks`  
`rq worker microblog-tasks`
* To update the language translation, from the base directory run  
`pybabel extract -F babel.cfg -k _l -o messages.pot .`  
`pybabel update -i messages.pot -d app/translations`  
Then update `app/translations/fr/LC_MESSAGES/messages.po` to add the translations. Then run  
`pybabel compile -d app/translations`