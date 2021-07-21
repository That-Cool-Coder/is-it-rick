const Status = {
    OK : 'OK',
    WARNING : 'WARNING',
    ERROR : 'ERROR'
}

const StatusCode = {
    OK : 'OK',

    // StatusCodes that go with Status WARNING
    INVALID_URL : 'INVALID_URL',
    INVALID_REQUEST : 'INVALID_REQUEST',

    // StatusCodes that go with Status ERROR
    UNKNOWN_ERROR : 'UNKNOWN_ERROR'
}

const StatusCodeMessages = {
    // Messages that go with Status WARNING
    [StatusCode.INVALID_URL] : 'The URL you entered is not a valid URL',
    [StatusCode.INVALID_REQUEST] : 'We are having difficulty communicating with the server',

    // Messages that go with Status ERROR
    [StatusCode.UNKNOWN_ERROR] : 'Unknown server error'
}

function basicPost(url, data) {
    return fetch(url, {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        redirect: 'follow',
        referrerPolicy: 'no-referrer',
        body: JSON.stringify(data)
    });
}

function showWarning(warningText, warningOutput, errorOutput=warningOutput) {
    errorOutput.style.display = 'none';
    warningOutput.style.display = 'initial';
    warningOutput.innerText = warningText;
}

function showError(errorText, warningOutput, errorOutput=warningOutput) {
    warningOutput.style.display = 'none';
    errorOutput.style.display = 'initial';
    errorOutput.innerText = errorText;   
}

function hideWarningErrorOutput(warningOutput, errorOutput=warningOutput) {
    warningOutput.style.display = 'none';
    errorOutput.style.display = 'none';
}

function showResponseStatusCode(response, warningOutput, errorOutput=warningOutput) {
    // Show the user the any errors or warnings using the DOM.
    // If everything is OK then it shows nothing.

    switch(response.status) {
        case Status.OK:
            hideWarningErrorOutput(warningOutput, errorOutput);
            break;
        case Status.WARNING:
            showWarning(StatusCodeMessages[response.status_code], warningOutput, errorOutput);
            break;
        case Status.ERROR:
            showError(StatusCodeMessages[response.status_code], warningOutput, errorOutput);
            break;
    }
}