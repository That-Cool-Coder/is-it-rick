# Is It Rick

Rick Roll detector website written in Python with Flask.

## Contents of README
- [Program purpose](#program-purpose)
- [Organisation of documentation](#organisation-of-documentation)
- [Coding conventions](#coding-conventions)
- [Documentation conventions](#documentation-conventions)
- [Git conventions](#git-conventions)
- [Planned features for initial release](#planned-features-for-initial-release)
- [Program architecture and organisation](#program-architecture-and-organisation)
- [Implementation information](#implementation-information)
- [Running the development server](#running-the-development-server)
- [Switching between development and production](#switching-between-development-and-production)
- [Server/client communication protocols](#serverclient-communication-protocols)
- [API](#api)
- [Frontend views](#frontend-views)
- [Data storage](#data-storage)
- [Deployment](#deployment)

## Program purpose

To allow people to quickly and easily check if a given URL leads to a Rick Roll.

## Organisation of documentation

All of the documentation for contributors is in this file. I've decided not to split it up into multiple files as that would involve writing a lot of links and wasting time. It helps if you have a markdown reader with an outline view so that you can jump around to the different sections easily.

## Coding conventions

#### Global

- Use American English for everything.
- Value readability over speed unless speed improvements are actually needed.
- Give each function a clear purpose and put a comment/docstring before at the top.
- Put a space between the start (`//`, `#`) of a one-line comment and the content of the comment.
- Do not use one-line if-statements or loops.
- Avoid using variable names such as `i`, even for loop indexes. Name the loop index after what the index counts.
- Avoid using English contractions (eg `can't don't`).
- If practical, keep function lengths below 75 lines.
- Name all files using `snake_case`.
- Use `snake_case` for API urls (as `snake_case` has been the standard for this project) and `hyphen-snake-case` for frontend urls (as `hyphen-snake-case` looks nicer to the user).

#### In data and requests

As the data and requests are handled by multiple languages, there are multiple standards that could be used. To resolve this ambiguity, it is mandated that the naming guidelines in [PEP-8](https://www.python.org/dev/peps/pep-0008/) are used. 

#### Python

- Follow [PEP-8](https://www.python.org/dev/peps/pep-0008/) guidelines. (`snake_case` for variables and functions, `UPPER_SNAKE_CASE` for constants, `PascalCase` for class names)
- Always use type hinting if possible.
- Put a space both before and after the colon in a dictionary. Eg: `{'a' : 5}`.
- Put spaces around operators. Eg: `5 * 3 + 5`.
- Do not put spaces around the `=` in a keyword argument. Eg: `doSomething(value=True)`.

#### JavaScript

- Use `camelCase` for functions, variables and constants.
- Use `PascalCase` for class names.
- Follow all lines with a semicolon, excluding control structures, function definitions and class definitions.
- Put opening braces on the same line as the control structure they follow. Eg: `if (someCondition) {`
- When writing if-else statements, put the `else {` on a new line after the end of the if. Eg:
```javascript
if (someCondition) {
    doSomeStuff();
}
else {
    doOtherStuff();
}
```
- Using ES6 features (eg `Array.forEach`) is permitted.

#### HTML/CSS
- Use `camelCase` for custom CSS classes.

## Documentation conventions

#### High-level conventions

- As mentioned above, keep all of the documentation in this one file. Depending on how large the project gets, it might be acceptable to restructure the documentation into multiple files.
- Write the documentation in GitHub-flavoured Markdown.
- Link to all of the top-level sections in the contents at the top.
- Use `##` (heading 2) for sections.
- Use `####` (heading 4) for subsections.
- Use `######` (heading 6) for subsubsections. Some Markdown viewers show this as smaller than regular text, but GitHub doesn't.
- Avoid using headings 3 and 5.

#### Low-level conventions

- Put a blank line between a heading and the text that follows it.
- Follow all lines with a full stop, excluding link-only lines.
- Don't put a newline when the text reaches the edge of the screen - instead let your editor wrap markdown lines.
- Put all file names, variable names, and specific strings in code blocks (surround with backticks).
- When using multiline code blocks, always specify the language if applicable.

## Git conventions

- Work on one feature/bugfix at a time and create a seperate commit for each feature/bugfix.
- Write your commit messages in imperative mood as described [here](https://git.kernel.org/pub/scm/git/git.git/tree/Documentation/SubmittingPatches?id=HEAD#n133). Eg: `make homepage show users their likes` as opposed to `made homepage show users their likes`.
- When creating a commit for a bugfix, format it like so: `fix #42`. This will make GitHub automatically close the issue it relates to.

## Features

These are essentially the different actions 

#### Implemented

- People can quickly check whether a URL leads to a verified Rick Roll, an unverified Rick Roll or is safe.
- People can submit a URL as a Rick Roll, and when the URL is checked by another person, it will show as unverified.
- URLs can not be verified except through manipulation of the database by server administrators.

#### Planned

- Admin accounts exist
- Admin accounts can be created from a command line utilty
- There is a set of managment pages that admins can access
- In the management pages, Rick Rolls can be verified
- In the management pages, fake Rick Rolls can be deleted

## Program architecture and organisation

#### Framework

Both the frontend and the backend are served through Flask. While the frontend doesn't strictly need to use Flask, it makes the code neater and makes future growth easy. `flask-error-templating` is used to automatically create HTTP  error handlers.

#### Entry point

When requests arrive, Apache2 runs the app from the WSGI script - `runner.wsgi`.

#### Organisation of the `/is_it_rick/` directory

The actual program is located in the directory `is_it_rick`.

List of non-meta files (in order of importance):
- `__main__.py` is a test runner. 
- `main_app.py` is the main file in there and it doesn't do much except handle app creation and import other things.
- `config.py` holds various global constants. It's arguable that the constants should be localised to the files that use the constants, but that would make finding the constants more difficult.
- `common.py` holds things needed by the whole project, including data-loading and enums.
- `errors.py` holds all of the custom exceptions for this app.
- `frontend_routes.py` defines all of the Flask routes for pages on the frontend.
- `backend_routes.py` defines all of the Flask routes for API endpoints on the backend.
- `data_structures.py` holds classes that hold the data.
- `init_data_files.py` is not actually part of the app run by Apache2, but initialises the data files for deployment.

The `static` and `templates` folders also are located in this directory, which is the Flask default location.

## Implementation information

This section of the documentation is a place to list miscellanious information about how the program is implemented.

#### Data

The optimal solution to data loading and saving would be to have the data primarily stored in variables, loading from a file at startup and saving to the file at exit. However, Apache2 has a tendency to run multiple instances of the Flask app, which means that the different instances would have different data stored, and when it came to program shutdown, they would all overwrite each other's data in the data file and make a mess.

To partially avoid this, each instance stores the data in variables, and every *n* seconds reads it from file. When new data is added (or when data is to be modified), the existing data read from the file, the new data is added (or modifications performed) and then the updated data is written back to the file.

#### Usage of URLs

I tried to use Flask `url_for` to allow easy shifting of the app, but that was too difficult to get working. Instead `BASE_URL` is defined in `config.py`, and it is passed to all templates when rendered. Then URLs in the template can be written as so: `{{ base_url + 'static/script.js'}}`.

## Running the development server

To run the app using Flask's inbuilt Werkzeug server, run `python3 -m is_it_rick` from the root directory of this project.

If you get an error such as `No module named is_it_rick/`, make sure you're using `-m` and make sure that there is no trailing slash on the module name.

## Switching between development and production

In production, the app is designed to be located in a subdirectory of the main server. However, in development it instead runs off the root of a port. This means that the URLs for assets, scripts and API calls are different depending on whether the app is in development or production.

To switch between these modes, there are booleans called `production` in the config files of the frontend and backend. These files are `is_it_rick/static/config.js` and `is_it_rick/config.py` respectively. Changing the value of `production` will change the value of URLs in config to match the environment.

Currently, these two files are not ignored by git, so you will need to set them back to their initial values (preferably to production mode) before pushing to GitHub. In future, a system for storing this on the local machine will be created.

## Server/client communication protocols

All data in both directions is sent in JSON format. In addition to the main data, a `status` and a `status_code` must be returned in every response from the API.

#### Statuses

There are three statuses:
- `OK` signifies that everything is nominal and that the attempted procedure was completed successfully
- `WARNING` signifies that there has been an issue, probably on behalf of the client. Eg: client tries to signin but the target user is not found or the password is incorrect
- `ERROR` signifies that there is a major error on the server which caused it to fail the target procedure. Eg: the database couldn't be opened.

The statuses are stored in an enum in `is_it_rick/common.py`.

#### Status Codes

The status codes give more information about the issue. They are defined in `is_it_rick/common.py`.

## API

I didn't know what to call the different URLs in the API (endpoints?), so I just called this section `API`. It lists all of the URLs in the API, what they accept in the request and what they return.

#### `/api/is_it_rick/`

Check whether a given URL leads to a Rick Roll

Accepts:
- `url` (string) - the URL to check.

Returns:
- `is_rick_roll` (bool) - whether the URL is a Rick Roll.
- `verified` (bool) - whether the Rick Roll has been verified or not. Only sent if `is_rick_roll` is true
- `status` and `status_code`.

#### `/api/register_rick_roll`

Accepts:
- `url` (string) - the URL that leads to the Rick Roll.

Returns:
- `status` and `status_code`.

## Frontend views

#### `/`

Homepage and main page of the app. Here, users can check if URLs are Rick Rolls. 

#### `/register-rick-roll/`

A page where users can submit Rick Rolls to the database.

## Data storage

The program's data is stored in JSON (specifically `jsonpickle`) format. This section details the organisation and location of the data. For information on how it is loaded and saved, see [Implementation information](#implementation-information).

#### Data location

The data is stored in the directory `/var/www/is_it_rick_data/`.

#### Data structures

###### `RickRoll`

This structure holds a record of a potential Rick Roll.

Attributes:
- `url` (string) - the URL that holds the Rick Roll.
- `verified` (boolean) - has this Rick Roll been verified by an administrator?
- `description` (string) (unimplemented) - a user-provided description of this Rick Roll. Should be optional.

###### `URL`

This structure holds a URL and some functions that get info from it. It's mainly to make comparing URLs and checking equivalence easier.

Attriubutes:
- `url` (string) - the actual URL that this object points to.

###### `User`

This structure represents a person who has signed up to use this app. Currently, only users with admin permissions are going to be able to do anything, but having this optional will most likely be useful for future growth. 

Attributes:
- `name` (string) - a unique reference to the user.
- `password_hash` (string) - the hash of the user's password.
- `join_timestamp` (float) - time in seconds since the epoch when this user was created.
- `admin` (boolean) - whether or not this user has admin permissions.

## Deployment

These instructions are only for Linux servers with Apache2 (aka httpd) - making this cross-platform is too hard. Not all Linux systems are the same - public directory locations, filenames and program names are often different. This guide is written for Ubuntu; Arch users might have to adapt it.

Prerequisites:
- Python >= 3.7
- Pip
- Apache2

#### Step 1: Clone git repo

Clone this repo into `/var/www/is-it-rick`.

#### Step 2: Install packages needed

For Ubuntu:
```
sudo apt-get install python-dev python3-venv
```

#### Step 3: Setup Python virtual environment:

Install `virtualenv` if you haven't done so already:
```
sudo -H pip3 install virtualenv
```

Create the environment:
```
python3 -m venv venv
```
Enter the environment:
```
source venv/bin/activate
```

#### Step 4: Install mod_wsgi

Run this command from the virtual environment:

```
pip3 install mod_wsgi
```

Then add it to Apache by writing this into `/etc/apache2/mods-available/wsgi.load`. Make sure to substitute `python3.9` and all of the `39`s for the Python version in your virtual environment. Yes it is suboptimal linking to a shared object in the (easily deletable) virtual environment; this needs improving.

```
LoadModule wsgi_module "/var/www/is-it-rick/venv/lib/python3.9/site-packages/mod_wsgi/server/mod_wsgi-py39.cpython-39-x86_64-linux-gnu.so"
WSGIPythonHome "/var/www/is-it-rick/venv"
```

Finally, make sure WSGI is enabled:

```
sudo a2enmod mod_wsgi
```

#### Step 5: Install Python packages

Run this command from the virtual environment:

```
pip3 install -r requirements.txt
```

#### Step 6: Update server config file

Add these lines to your site's config file (probably `/etc/apache2/sites-available/000-default-le-ssl.conf`):
```
WSGIDaemonProcess is_it_rick user=www-data group=www-data threads=4 python-home=/var/www/is_it_rick/venv
	WSGIScriptAlias /is_it_rick /var/www/is_it_rick/runner.wsgi
```

#### Step 7: Create data storage directory

Create a directory called `/var/www/is_it_rick_data/` to hold the data. Set its permissions to everyone can read/write (octal `0777`).

#### Step 8: Initialise database

Run `init_data_files.py` to setup the data files.

#### Step 9: Restart Apache2

On Ubuntu, run this:
```
sudo systemctl restart apache2
```