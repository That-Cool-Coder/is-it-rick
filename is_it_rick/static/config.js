if (localConfig) {
    window.config = localConfig;
}
else {
    window.config = {
        production : true,
        baseUrl : '/'
    };
}