import { getInputs, getLabels } from './functions.js';

const odobrenInput = getInputs(['id_odobren']);
const passwordLabels = getLabels(['id_password1', 'id_password2']);
const passwordInputs = getInputs(['id_password1', 'id_password2']);
const helpUl = document.getElementsByTagName('ul');

const allElements = [passwordLabels, passwordInputs];

window.onload = main();

function switchHelpDisplay() {
    for (let ul of helpUl) {
        if (ul.classList.length == 0 && ul.style.display == "")
            ul.style.display = "none";
        else if (ul.classList.length == 0 && ul.style.display == "none")
            ul.style.display = "";
    }
}

function switchDisplay() {
    switchHelpDisplay();
    for (let elements of allElements)
        elementsSwitchDisplay(elements);
}

function elementsSwitchDisplay(elements) {
    for (let element of elements) {
        if (odobrenInput !== null && odobrenInput.checked) {
            element.style.display = "";
            if (passwordInputs.includes(element))
                element.required = true;
        }
        else {
            element.style.display = "none";
        }
    }
}

function main() {
    //console.log(odobrenInput)
    switchDisplay();
    odobrenInput.addEventListener('click', () => switchDisplay());
}
