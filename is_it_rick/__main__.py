'''File to use for testing the program.
It will be run if you do python -m is_it_rick.
Imports the app and runs it with the Flask test server.
'''

from is_it_rick import app, config, start_background_tasks

start_background_tasks()

app.run(host='0.0.0.0', port=config.TESTING_PORT)