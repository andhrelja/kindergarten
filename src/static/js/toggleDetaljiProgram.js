import { getSelectedVrstaPrograma, getInputs } from './functions.js';

const vrstaProgramaSelect = getInputs(['id_vrsta_programa']);
const programSelect = getInputs(['id_program']);
const smjenaSelect = getInputs(['id_smjena']);

const smjenaCijena = getInputs(['vrsta_programa_cijena']);
const programDobneSkupine = getInputs(['program_dobne_skupine']);
const programUpisanaDjeca = getInputs(['program_upisana_djeca']);

window.onload = main();

function main() {
    let program = getSelectedVrstaPrograma(programSelect);
    let vrstaPrograma = getSelectedVrstaPrograma(vrstaProgramaSelect);

    if (program && vrstaPrograma) {
        fetchSelectedProgram();
    }

    vrstaProgramaSelect.addEventListener('change', () => hideAll());
    programSelect.addEventListener('change', () => fetchSelectedProgram());
    smjenaSelect.addEventListener('change', () => fetchSelectedSmjenaProgram_Cijena());
}

function hideAll() {
    hideDobneSkupine();
    hideUpisanaDjeca();
    hideSmjenaCijena();
}


function fetchSelectedProgram() {
    fetchSelectedProgram_DobneSkupine();
    fetchSelectedProgram_UpisanaDjeca();
    fetchSelectedSmjenaProgram_Cijena();
}

function fetchSelectedSmjenaProgram_Cijena() {
    let program = getSelectedVrstaPrograma(programSelect);
    let smjena = getSelectedVrstaPrograma(smjenaSelect);
    
    if (program && smjena) {
        let url = '/programi/' + program.value + '/smjena/'+ smjena.value + '/cijena/api';

        fetch(url)
            .then(response => response.json())
            .then(data => toggleSmjenaCijenaDetails(data));
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


function fetchSelectedProgram_UpisanaDjeca() {
    let program = getSelectedVrstaPrograma(programSelect);
    if (program) {
        let url = '/programi/' + program.value + '/upisana-djeca/api';

        fetch(url)
            .then(response => response.json())
            .then(data => toggleProgramUpisanaDjeca(data));
    }
}


function toggleSmjenaCijenaDetails(data) {
    let clanstvo = parseFloat(data.clanstvo);
    let broj_sati = parseFloat(data.broj_sati);
    smjenaCijena.innerHTML = (clanstvo * 20 * broj_sati) + ' kn/mj.';
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

function hideSmjenaCijena() {
    smjenaCijena.innerHTML = '';
}