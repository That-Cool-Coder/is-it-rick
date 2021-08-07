const outputParagraph = spnr.dom.id('outputParagraph');
const warningParagraph = spnr.dom.id('warningParagraph');
const confirmDeleteMessage = 'Are you sure you want to delete this Rick Roll?';

async function deleteRickRoll() {
    if (! confirm(confirmDeleteMessage)) return;

    var response = await basicPost(urls.backend.deleteRickRoll, {id : rickRollId});
    var json = await response.json();
    if (json.status == Status.OK) {
        window.location.href = urls.frontend.manageRickRolls;
    }
    else {
        showResponseStatusCode(json, outputParagraph, warningParagraph);
    }
}

async function verifyRickRoll() {
    var response = await basicPost(urls.backend.verifyRickRoll, {id : rickRollId});
    var json = await response.json();
    if (json.status == Status.OK) {
        window.location.reload();
    }
    else {
        showResponseStatusCode(json, outputParagraph, warningParagraph);
    }
}