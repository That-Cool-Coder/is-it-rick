const urlInput = spnr.dom.id('urlInput');
const outputDiv = spnr.dom.id('outputDiv');

const verifiedRickRollText = 'This URL leads to a Rick Roll (verified)';
const unverifiedRickRollText = 'This URL leads to a Rick Roll (unverified)';
const noRickRollText = `This URL should not lead to a Rick Roll.
If you do find that it leads to a Rick Roll, please register it on this site.`

urlInput.addEventListener('keypress', event => {
    // Enter pressed
    if (event.keyCode == 13) {
        checkUrl();
    }
});

async function checkUrl() {
    var url = urlInput.value;
    if (url != '') {
        var response = await basicPost(urls.backend.isItRick, {url : url});
        var json = await response.json();
        switch (json.status) {
            case Status.OK:
                if (json.is_rick_roll) {
                    if (json.verified) {
                        outputDiv.innerText = verifiedRickRollText;
                    }
                    else {
                        outputDiv.innerText = unverifiedRickRollText;
                    } 
                }
                else {
                    outputDiv.innerText = noRickRollText;
                }
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