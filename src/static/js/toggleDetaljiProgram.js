import { getSelectedVrstaPrograma, getInputs } from './functions.js';

const vrstaProgramaSelect = getInputs(['id_vrsta_programa']);
const programSelect = getInputs(['id_program']);

const vrstaProgramaCijena = getInputs(['vrsta_programa_cijena']);
const programDobneSkupine = getInputs(['program_dobne_skupine']);
const programSmjene = getInputs(['program_smjene']);
const programUpisanaDjeca = getInputs(['program_upisana_djeca']);

window.onload = main();

function main() {
    let program = getSelectedVrstaPrograma(programSelect);
    let vrstaPrograma = getSelectedVrstaPrograma(vrstaProgramaSelect);

    if (program && vrstaPrograma) {
        fetchSelectedVrstaPrograma();
        fetchSelectedProgram();
    }

    vrstaProgramaSelect.addEventListener('change', () => fetchSelectedVrstaPrograma());
    programSelect.addEventListener('change', () => fetchSelectedProgram());
}


function fetchSelectedVrstaPrograma() {
    hideDobneSkupine();
    hideSmjene();
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
    hideSmjene();
    hideUpisanaDjeca();
    fetchSelectedProgram_DobneSkupine();
    fetchSelectedProgram_Smjene();
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

function fetchSelectedProgram_Smjene() {
    let program = getSelectedVrstaPrograma(programSelect);
    if (program) {
        let url = '/programi/' + program.value + '/smjene/api';

        fetch(url)
            .then(response => response.json())
            .then(data => toggleProgramSmjene(data));
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

function hideDobneSkupine() {
    while (programDobneSkupine.firstChild) {
        programDobneSkupine.removeChild(programDobneSkupine.lastChild);
    }
}

function hideSmjene() {
    while (programSmjene.firstChild) {
        programSmjene.removeChild(programSmjene.lastChild);
    }
}

function hideUpisanaDjeca() {
    while (programUpisanaDjeca.firstChild) {
        programUpisanaDjeca.removeChild(programUpisanaDjeca.lastChild);
    }
}