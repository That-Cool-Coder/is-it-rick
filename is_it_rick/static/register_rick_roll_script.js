const urlInput = spnr.dom.id('urlInput');
const outputParagraph = spnr.dom.id('outputParagraph');
const warningParagraph = spnr.dom.id('warningParagraph');

const successText = `Successfully added URL.
Until it is approved by a moderator, it will appear as unverified.`

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

        if (json.status == Status.OK) {
            showOnlyOutputElement(outputParagraph, warningParagraph);
            
            outputParagraph.innerText = successText;
        }
        else {
            showResponseStatusCode(json, outputParagraph, warningParagraph);
        }
    }
    else {
        alert('Must fill in URL input');
    }
}