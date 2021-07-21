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
    if (url == '') {
        debugger;
        showWarning('You must enter a URL', outputParagraph, warningParagraph);
    }
    else {
        var response = await basicPost(urls.backend.isItRick, {url : url});
        var json = await response.json();
        if (json.status == Status.OK) {
            showOnlyOutputElement(outputParagraph, warningParagraph);
            
            if (json.verified && json.is_rick_roll) {
                outputParagraph.innerText = verifiedRickRollText;
            }
            else if (! json.verified && json.is_rick_roll) {
                outputParagraph.innerText = unverifiedRickRollText;
            } 
            else {
                outputParagraph.innerText = noRickRollText;
            }
        }
        else {
            showResponseStatusCode(json, outputParagraph, warningParagraph);
        }
    }
}