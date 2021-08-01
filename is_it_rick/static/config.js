if (localConfig) {
    window.config = localConfig;
}
else {
    window.config = {
        production : true,
        baseUrl : '/'
    };
}

config.sessionIdCookieName = 'isItRickSessionId';

// Arbitrary large value - session id expiration is handled on server
config.sessionIdCookieDuration = 1000;