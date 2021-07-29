from is_it_rick.main_app import app, start_background_tasks
from is_it_rick import config

if __name__ == '__main__':
    start_background_tasks()
    app.run(host='0.0.0.0', port=config.TESTING_PORT, debug=True)