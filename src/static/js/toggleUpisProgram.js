import { getSelectedVrstaPrograma, getInputs } from './functions.js';

const vrstaProgramaSelect = getInputs(['id_vrsta_programa']);
const programSelect = getInputs(['id_program']);

window.onload = main();

function toggleProgramOptions(selectedOptions) {
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


function togglePrograms(data) {
    let programs = [];
    for (let program of data) {
        programs.push(program.pk)
    }
    toggleProgramOptions(programs);
}

function fetchSelectedPrograms() {
    toggleProgramOptions(null);

    let vrstaPrograma = getSelectedVrstaPrograma(vrstaProgramaSelect);
    if (vrstaPrograma) {
        let url = '/programi/vrsta/' + vrstaPrograma.value + '/api';

        fetch(url)
            .then(response => response.json())
            .then(data => togglePrograms(data))
    }
}

function main() {
    vrstaProgramaSelect.addEventListener('change', () => fetchSelectedPrograms());

}
