import { getSelectedVrstaPrograma, getInputs } from './functions.js';

const vrstaProgramaSelect = getInputs(['id_vrsta_programa']);
const programSelect = getInputs(['id_program']);

const vrstaProgramaCijena = getInputs(['vrsta_programa_cijena']);
const programDobneSkupine = getInputs(['program_dobne_skupine']);
const programSmjene = getInputs(['program_smjene']);

window.onload = main();


function toggleVrstaProgramaDetails(data) {
    vrstaProgramaCijena.innerHTML = data.fields.clanstvo_cijena + ' kn/mj.';
}

function toggleProgramDobneSkupine(data) {
    for (let dobnaSkupina of data) {
        let li = document.createElement('li');
        li.innerHTML = dobnaSkupina.fields.naziv;
        programDobneSkupine.appendChild(li);
    }
}

function getNazivSmjene(fields) {
    let vrijeme_start = fields.vrijeme_start.slice(0, -3);
    let vrijeme_kraj = fields.vrijeme_kraj.slice(0, -3);
    return fields.naziv_smjene + ": " + vrijeme_start + " - " + vrijeme_kraj;
}

function toggleProgramSmjene(data) {
    for (let smjena of data) {
        let li = document.createElement('li');
        li.innerHTML = getNazivSmjene(smjena.fields);
        programSmjene.appendChild(li);
    }
}

function hideDobneSkupineCijena() {
    while (programDobneSkupine.firstChild) {
        programDobneSkupine.removeChild(programDobneSkupine.lastChild);
    }
    while (programSmjene.firstChild) {
        programSmjene.removeChild(programSmjene.lastChild);
    }
}

function fetchSelectedVrstaPrograma() {
    hideDobneSkupineCijena();
    let vrstaPrograma = getSelectedVrstaPrograma(vrstaProgramaSelect);
    if (vrstaPrograma) {
        let url = '/programi/vrsta-programa/' + vrstaPrograma.value + '/api';

        fetch(url)
            .then(response => response.json())
            .then(data => toggleVrstaProgramaDetails(data[0]));
    }
}

function fetchSelectedProgram_DobneSkupine() {
    let program = getSelectedVrstaPrograma(programSelect);
    if (program) {
        let url = '/programi/' + program.value + '/dobne-skupine/api';

        fetch(url)
            .then(response => response.json())
            .then(data => toggleProgramDobneSkupine(data));
    }
}

function fetchSelectedProgram_Smjene() {
    let program = getSelectedVrstaPrograma(programSelect);
    if (program) {
        let url = '/programi/' + program.value + '/smjene/api';

        fetch(url)
            .then(response => response.json())
            .then(data => toggleProgramSmjene(data));
    }
}


function main() {
    let program = getSelectedVrstaPrograma(programSelect);
    let vrstaPrograma = getSelectedVrstaPrograma(vrstaProgramaSelect);

    if (program && vrstaPrograma) {
        fetchSelectedVrstaPrograma();
        fetchSelectedProgram_DobneSkupine();
        fetchSelectedProgram_Smjene();
    }

    vrstaProgramaSelect.addEventListener('change', () => fetchSelectedVrstaPrograma());
    programSelect.addEventListener('change', () => fetchSelectedProgram_DobneSkupine());
    programSelect.addEventListener('change', () => fetchSelectedProgram_Smjene());
}
