const urlInput = spnr.dom.id('urlInput');
const outputParagraph = spnr.dom.id('outputParagraph');
const warningParagraph = spnr.dom.id('warningParagraph');

const verifiedRickRollText = 'This URL leads to a Rick Roll (verified)';
const unverifiedRickRollText = 'This URL leads to a Rick Roll (unverified)';
const noRickRollText = `This URL should not lead to a Rick Roll.
If you do find that it leads to a Rick Roll, please register it on this site.`;
const invalidUrlText = 'The URL you entered is not valid';

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
                outputParagraph.style.display = 'inline-block';
                warningParagraph.style.display = 'none';
                if (json.is_rick_roll) {
                    if (json.verified) {
                        outputParagraph.innerText = verifiedRickRollText;
                    }
                    else {
                        outputParagraph.innerText = unverifiedRickRollText;
                    } 
                }
                else {
                    outputParagraph.innerText = noRickRollText;
                }
                break;
            case Status.WARNING:
                outputParagraph.style.display = 'none';
                switch(json.status_code) {
                    case StatusCode.INVALID_URL:
                        warningParagraph.style.display = 'inline-block';
                        warningParagraph.innerText = invalidUrlText;
                        break;
                    default:
                        alert(json.status_code);
                        break;
                }
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