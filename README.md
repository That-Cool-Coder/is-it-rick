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
- [Server/client communication protocols](#serverclient-communication-protocols)
- [API](#api)
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

#### In data and requests

As the data and requests will be handled by multiple languages, there are multiple standards that could be used. To resolve this ambiguity, it is mandated that the naming guidelines in [PEP-8](https://www.python.org/dev/peps/pep-0008/) are used. 

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

## Planned features for initial release

The initial release will be quite limited as I want to get something working very quickly.

- People can quickly check whether a URL leads to a verified Rick Roll, an unverified Rick Roll or is safe.
- People can submit a URL as a Rick Roll, and when the URL is checked by another person, it will show as unverified.
- URLs can not be verified except through manipulation of the database by server administrators.

## Program architecture and organisation

#### Framework

Both the frontend and the backend will be served through Flask. While there are no frontend features in the initial release that require Flask, using Flask will make future growth easy.

#### Entry point

When requests arrive, Apache2 runs the app from the WSGI script - `runner.wsgi`.

#### Organisation of the `/is_it_rick/` directory

The actual program is located in the directory `is_it_rick`.

List of non-meta files (in order of importance):
- `main.py` is the main file in there and it doesn't do much except handle app creation and import other things.
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

## Server/client communication protocols

All data in both directions will be sent in JSON format. In addition to the main data, a `status` and a `status_code` must be returned in every response from the API.

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

## Data storage

Note: this an abstract view of the data storage. For implementation details such as file location and how to actually load the data see [#Implementation information](#implementation-information).

The program's data is stored in JSON format. This section details the organisation and location of the data. For information on how it is loaded and saved, see [#Implementation information](#implementation-information).

#### Data location

The data is stored in the directory `/var/www/is_it_rick_data/`.

#### Data structures

###### `RickRoll`

This structure holds a record of a potential Rick Roll.

Attributes:
- `url` (string) - the URL that holds the Rick Roll
- `verified` (boolean) - has this Rick Roll been verified by an administrator?

## Deployment

(Only for Linux servers with Apache2 (aka httpd) - making this cross-platform is too hard)

Prerequisites:
- Python >= 3.6
- Pip
- Apache2

Step 1: Clone this repo into a directory (I am not sure what that would be yet).

Step 2: Install things needed for WSGI:
```
sudo apt-get install libApache2-mod-wsgi-py3 python-dev
```

Step 3: Install python packages (You must use `sudo` or they won't be installed globally and therefore won't be available when the app is run):
```
sudo -H pip3 install Flask flask-error-templating validators
```

Step 4: Add a line to your server's config to make WSGI work (not sure yet)

Step 5: Create a directory `/var/www/is_it_rick_data/` to hold the data. Set its permissions to everyone can read/write.

Step 6: Run `is_it_rick/init_data_files.py` to setup the data files.

Step 7: Restart Apache2 (this might be different on your machine):
```
sudo systemctl restart Apache2
```