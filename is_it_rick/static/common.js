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
    URL_ALREADY_REGISTERED : 'URL_ALREADY_REGISTERED',
    INVALID_CREDENTITALS : 'INVALID_CREDENTIALS',

    // StatusCodes that go with Status ERROR
    UNKNOWN_ERROR : 'UNKNOWN_ERROR'
}

const StatusCodeMessages = {
    // Messages that go with Status WARNING
    [StatusCode.INVALID_URL] : 'The URL you entered is not a valid URL',
    [StatusCode.INVALID_REQUEST] : 'We are having difficulty communicating with the server',
    [StatusCode.URL_ALREADY_REGISTERED] : 'That URL is already registered',
    [StatusCode.INVALID_CREDENTITALS] : 'The username or password that you entered is incorrect',

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

function showWarning(warningText, outputElement, warningElement, errorElement=warningElement) {
    outputElement.style.display = 'none';
    errorElement.style.display = 'none';
    warningElement.style.display = 'initial';
    warningElement.innerText = warningText;
}

function showError(errorText, outputElement, warningElement, errorElement=warningElement) {
    outputElement.style.display = 'none';
    warningElement.style.display = 'none';
    errorElement.style.display = 'initial';
    errorElement.innerText = errorText;   
}

function showOnlyOutputElement(outputElement, warningElement, errorElement=warningElement) {
    outputElement.style.display = 'initial';
    warningElement.style.display = 'none';
    errorElement.style.display = 'none';
}

function showResponseStatusCode(response, outputElement, warningElement, errorElement=warningElement) {
    // Show the user the any errors or warnings using the DOM.
    // If everything is OK then it shows nothing.

    switch(response.status) {
        case Status.OK:
            showOnlyOutputElement(outputElement, warningElement, errorElement);
            break;
        case Status.WARNING:
            showWarning(StatusCodeMessages[response.status_code], outputElement,
                warningElement, errorElement);
            break;
        case Status.ERROR:
            showError(StatusCodeMessages[response.status_code], outputElement,
                warningElement, errorElement);
            break;
    }
}

function goToSignInPage() {
    // Go to the sign in page and then return to the original page
    var crntPath = encodeURIComponent(window.location.pathname);
    window.location.href = `${window.location.protocol}//${window.location.host}` +
        `${urls.frontend.signIn}?return_url=${crntPath}`;
}