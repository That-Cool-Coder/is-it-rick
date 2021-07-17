# Is It Rick

Rick Roll detector website written in Python with Flask.

## Contents of README
- [Purpose](#purpose)
- [Organisation of documentation](#organisation-of-documentation)
- [Coding conventions](#coding-conventions)
- [Documentation conventions](#documentation-conventions)
- [Git conventions](#git-conventions)
- [Planned features for initial release](#planned-features-for-initial-release)
- [Program architecture and organisation](#program-architecture-and-organisation)
- [Deployment](#deployment)

## Purpose

To allow people to quickly and easily check if a URL leads to a Rick Roll.

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
- Put a space before and after the colon in a dictionary.

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

Both the frontend and the backend will be served through Flask. While there are no frontend features in the initial release that require Flask, using Flask will make future growth easy. The entry point is the WSGI script - `runner.wsgi`. The main program is in the directory `is_it_rick`, and the main file in there is `main.py`.

## Deployment

(Only for Linux servers with apache2 (aka httpd) - making this cross-platform is too hard)

Prerequisites:
- Python >= 3.6
- Pip

Step 1: Clone this repo into a directory (I am not sure what that would be yet).

Step 2: Install things needed for WSGI:
```
sudo apt-get install libapache2-mod-wsgi-py3 python-dev
```

Step 3: Install python packages (You must use `sudo` or they won't be installed globally and therefore won't be available when the app is run):
```
sudo -H pip3 install Flask flask-error-templating
```

Step 4: Add a line to your server's config to make WSGI work (not sure yet)

Step 6: Restart apache2 (this might be different on your machine):
```
sudo systemctl restart apache2
```