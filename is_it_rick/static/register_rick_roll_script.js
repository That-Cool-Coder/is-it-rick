const urlInput = spnr.dom.id('urlInput');

urlInput.addEventListener('keypress', event => {
    // Enter pressed
    if (event.keyCode == 13) {
        registerRickRoll();
    }
});

async function registerRickRoll() {
    var url = urlInput.value;
    if (url != '') {
        var response = await basicPost(urls.backend.registerRickRoll, {url : url});
        var json = await response.json();
        switch (json.status) {
            case Status.OK:
                alert('Ok');
                console.log(json);
                break;
            case Status.WARNING:
                alert(json.status_code);
                break;
            case Status.ERROR:
                showResponseError(json.status_code);
                break;
        }
    }
    else {
        alert('Must fill in URL input');
    }
}