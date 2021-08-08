const urlInput = spnr.dom.id('urlInput');
const outputParagraph = spnr.dom.id('outputParagraph');
const warningParagraph = spnr.dom.id('warningParagraph');

const noUrlInputtedText = 'You must input a URL';
const successText = `Successfully added URL.
Until it is approved by a moderator, it will appear as unverified.`;

urlInput.addEventListener('keypress', event => {
    // Enter pressed
    if (event.keyCode == 13) {
        registerRickRoll();
    }
});

async function registerRickRoll() {
    var url = urlInput.value;
    if (url == '') {
        showWarning(noUrlInputtedText, outputParagraph, warningParagraph);
    }
    hideAllElements(outputParagraph, warningParagraph);
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