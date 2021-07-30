const usernameInput = spnr.dom.id('usernameInput');
const passwordInput = spnr.dom.id('passwordInput');
const outputParagraph = spnr.dom.id('outputParagraph');
const warningParagraph = spnr.dom.id('warningParagraph');

passwordInput.addEventListener('keypress', event => {
    // Enter pressed
    if (event.keyCode == 13) {
        signIn();
    }
});

async function signIn() {
    var username = usernameInput.value;
    var password = passwordInput.value;
    if (username == '' || password == '') {
        showWarning('You must enter a username and password',
            outputParagraph, warningParagraph);
    }
    else {
        var response = await basicPost(urls.backend.signIn,
            {username : username, password : password});
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