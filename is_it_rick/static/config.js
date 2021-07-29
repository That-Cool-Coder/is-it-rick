const config = {
    production : true
}

if (config.production) {
    config.base_url = '/is-it-rick/';
}
else {
    config.base_url = '/';
}

const urls = {
    frontend : {
        homepage : config.base_url,
        registerRickRoll : config.base_url + 'register_rick_roll/'
    },
    backend : {
        isItRick : config.base_url + 'api/is_it_rick/',
        registerRickRoll : config.base_url + 'api/register_rick_roll/'
    }
}