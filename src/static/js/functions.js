export {
    getSelectedVrstaPrograma,
    getInputs,
    getLabels
}

function getSelectedVrstaPrograma(vrstaProgramaSelect) {
    for (let option of vrstaProgramaSelect.options) {
        if (option.selected && option.value != "")
            return option;
        else if (option.selected && option.value == "")
            return null;
    }
}

function getInputs(inputIds) {
    let passwordInputs = [];
    for (let inputId of inputIds) {
        let input = document.getElementById(inputId);
        passwordInputs.push(input)
    }
    if (passwordInputs.length == 1)
        return passwordInputs[0];
    return passwordInputs;
}

function getLabels(labelForIds) {
    let passwordLabels = [];
    for (let labelForId of labelForIds) {
        let label = getLabel(labelForId);
        passwordLabels.push(label);
    }
    return passwordLabels;
}

function getLabel(labelForId) {
    let labels = document.getElementsByTagName('label');
    for (let label of labels) {
        if (label.htmlFor == labelForId) {
            return label;
        }
    }
}