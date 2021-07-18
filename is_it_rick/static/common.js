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

function showResponseError(statusCode) {
    alert(`Error: ${statusCode}`);
}