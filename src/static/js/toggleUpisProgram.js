import { getSelectedVrstaPrograma, getInputs } from './functions.js';

const vrstaProgramaSelect = getInputs(['id_vrsta_programa']);
const programSelect = getInputs(['id_program']);
const smjeneSelect = getInputs(['id_smjena']);

window.onload = main();

function toggleProgramOptions(selectedOptions) {
    if (!selectedOptions) {
        programSelect.disabled = true;
    }
    else {
        programSelect.disabled = false;
    }

    for (let option of programSelect.options) {
        if (option.selected && !selectedOptions && option.value != "") {
            option.style.display = "none";
        }
        else if (!selectedOptions && option.value == "") {
            option.style.display = "";
            option.selected = true;
        }
        else if (selectedOptions && selectedOptions.includes(parseInt(option.value))) {
            option.style.display = "";
        }
        else if (selectedOptions && !selectedOptions.includes(parseInt(option.value))) {
            option.style.display = "none";
        }
    }
}

function toggleSmjeneOptions(selectedOptions) {
    if (!selectedOptions) {
        smjeneSelect.disabled = true;
    }
    else {
        smjeneSelect.disabled = false;
    }
    
    for (let option of smjeneSelect.options) {
        if (!selectedOptions && option.selected && option.value != "") {
            option.style.display = "none";
        }
        else if (!selectedOptions && option.value == "") {
            option.style.display = "";
            option.selected = true;
        }
        else if (selectedOptions && selectedOptions.includes(parseInt(option.value))) {
            option.style.display = "";
        }
        else if (selectedOptions && !selectedOptions.includes(parseInt(option.value))) {
            option.style.display = "none";
        }
    }
}


function togglePrograms(data) {
    let programs = [];
    for (let program of data) {
        programs.push(program.pk)
    }
    toggleProgramOptions(programs);
}

function toggleSmjene(data) {
    let smjene = [];
    for (let smjena of data) {
        smjene.push(smjena.pk)
    }
    toggleSmjeneOptions(smjene);
}

function fetchSelectedPrograms() {
    toggleProgramOptions(null);
    toggleSmjeneOptions(null);


    let vrstaPrograma = getSelectedVrstaPrograma(vrstaProgramaSelect);
    if (vrstaPrograma) {
        let url = '/programi/vrsta/' + vrstaPrograma.value + '/api';

        fetch(url)
            .then(response => response.json())
            .then(data => togglePrograms(data))
    }
}

function fetchSelectedSmjene() {    
    toggleSmjeneOptions(null);

    let program = getSelectedVrstaPrograma(programSelect);
    if (program) {
        let url = '/programi/' + program.value + '/smjene/api';

        fetch(url)
            .then(response => response.json())
            .then(data => toggleSmjene(data));
    }
}

function main() {
    let program = getSelectedVrstaPrograma(programSelect);
    let vrstaPrograma = getSelectedVrstaPrograma(vrstaProgramaSelect);
    
    if (!program && !vrstaPrograma) {
        toggleProgramOptions(null);
        toggleSmjeneOptions(null);
    }
    
    vrstaProgramaSelect.addEventListener('change', () => fetchSelectedPrograms());
    programSelect.addEventListener('change', () => fetchSelectedSmjene());

}
