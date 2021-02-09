import { getSelectedVrstaPrograma, getInputs } from './functions.js';

const vrstaProgramaSelect = getInputs(['id_vrsta_programa']);
const programSelect = getInputs(['id_program']);

const vrstaProgramaCijena = getInputs(['vrsta_programa_cijena']);
const programDobneSkupine = getInputs(['program_dobne_skupine']);
const programUpisanaDjeca = getInputs(['program_upisana_djeca']);

window.onload = main();

function main() {
    let program = getSelectedVrstaPrograma(programSelect);
    let vrstaPrograma = getSelectedVrstaPrograma(vrstaProgramaSelect);
    console.log(program && vrstaPrograma);

    if (program && vrstaPrograma) {
        fetchSelectedVrstaPrograma();
        fetchSelectedProgram();
    }

    vrstaProgramaSelect.addEventListener('change', () => fetchSelectedVrstaPrograma());
    programSelect.addEventListener('change', () => fetchSelectedProgram());
}


function fetchSelectedVrstaPrograma() {
    hideDobneSkupine();
    hideUpisanaDjeca();
    
    let vrstaPrograma = getSelectedVrstaPrograma(vrstaProgramaSelect);
    if (vrstaPrograma) {
        let url = '/programi/vrsta-programa/' + vrstaPrograma.value + '/api';

        fetch(url)
            .then(response => response.json())
            .then(data => toggleVrstaProgramaDetails(data[0]));
    }
}

function fetchSelectedProgram() {
    hideDobneSkupine();
    hideUpisanaDjeca();
    fetchSelectedProgram_DobneSkupine();
    fetchSelectedProgram_UpisanaDjeca();
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


function fetchSelectedProgram_UpisanaDjeca() {
    let program = getSelectedVrstaPrograma(programSelect);
    if (program) {
        let url = '/programi/' + program.value + '/upisana-djeca/api';

        fetch(url)
            .then(response => response.json())
            .then(data => toggleProgramUpisanaDjeca(data));
    }
}


function toggleVrstaProgramaDetails(data) {
    let clanstvo = parseFloat(data.fields.clanstvo_cijena);
    vrstaProgramaCijena.innerHTML = (clanstvo * 30 * 8) + ' kn/mj.';
}

function toggleProgramDobneSkupine(data) {
    for (let dobnaSkupina of data) {
        let li = document.createElement('li');
        li.innerHTML = dobnaSkupina.fields.naziv;
        programDobneSkupine.appendChild(li);
    }
}

function toggleProgramUpisanaDjeca(data) {
    let upisanoDjece = data.upisano_djece;
    let maxBrojDjece = data.max_broj_djece;

    let li1 = document.createElement('li');
    let li2 = document.createElement('li');
    li1.innerHTML = "Maksimalni broj djece: " + maxBrojDjece;
    li2.innerHTML = "Broj upisane djece: " + upisanoDjece;
    programUpisanaDjeca.appendChild(li1);
    programUpisanaDjeca.appendChild(li2);
}


function hideDobneSkupine() {
    while (programDobneSkupine.firstChild) {
        programDobneSkupine.removeChild(programDobneSkupine.lastChild);
    }
}

function hideUpisanaDjeca() {
    while (programUpisanaDjeca.firstChild) {
        programUpisanaDjeca.removeChild(programUpisanaDjeca.lastChild);
    }
}