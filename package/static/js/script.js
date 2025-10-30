// Variables globales
let currentStep = 1;
const totalSteps = 4;
const form = document.getElementById('stageForm');
const steps = document.querySelectorAll('.form-step');
const stepIndicators = document.querySelectorAll('.step');
const prevButton = document.getElementById('prevBtn');
const nextButton = document.getElementById('nextBtn');
const submitButton = document.getElementById('submitBtn');

// Fonction pour mettre à jour l'affichage de l'étape
function updateStepDisplay() {
    // Mettre à jour les étapes du formulaire
    steps.forEach((step, index) => {
        step.classList.remove('active');
        if (index + 1 === currentStep) {
            step.classList.add('active');
        }
    });

    // Mettre à jour les indicateurs de progression
    stepIndicators.forEach((indicator, index) => {
        indicator.classList.remove('active');
        if (index + 1 <= currentStep) {
            indicator.classList.add('active');
        }
    });

    // Mettre à jour les boutons de navigation
    prevButton.style.display = currentStep === 1 ? 'none' : 'inline-flex';
    nextButton.style.display = currentStep === totalSteps ? 'none' : 'inline-flex';
    submitButton.style.display = currentStep === totalSteps ? 'inline-flex' : 'none';
}

// Fonction pour passer à l'étape suivante
function nextStep() {
    if (currentStep < totalSteps) {
        // Validation simple de l'étape actuelle (peut être améliorée)
        const currentFormStep = document.querySelector(`.form-step:nth-child(${currentStep})`);
        const inputs = currentFormStep.querySelectorAll('input[required], select[required], textarea[required]');
        let isValid = true;
        inputs.forEach(input => {
            if (!input.value.trim()) {
                isValid = false;
                input.style.border = '2px solid red'; // Indiquer l'erreur
            } else {
                input.style.border = ''; // Réinitialiser le style
            }
        });

        if (isValid) {
            currentStep++;
            updateStepDisplay();
            window.scrollTo({ top: 0, behavior: 'smooth' }); // Remonter en haut du formulaire
        } else {
            alert('Veuillez remplir tous les champs obligatoires avant de continuer.');
        }
    }
}

// Fonction pour revenir à l'étape précédente
function prevStep() {
    if (currentStep > 1) {
        currentStep--;
        updateStepDisplay();
        window.scrollTo({ top: 0, behavior: 'smooth' }); // Remonter en haut du formulaire
    }
}

// Fonction pour sélectionner un domaine (utilisée par les boutons de la section domaines)
function selectDomain(domainName) {
    document.getElementById('domaine_stage').value = domainName;
    scrollToSection('formulaire');
    updateStepDisplay();
}

// Fonction pour le défilement fluide
function scrollToSection(id) {
    const element = document.getElementById(id);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
}

// Gestion de la soumission du formulaire

// Initialisation au chargement de la page
document.addEventListener('DOMContentLoaded', () => {
    updateStepDisplay();
});

// Écouteurs d'événements pour les boutons de navigation
nextButton.addEventListener('click', nextStep);
prevButton.addEventListener('click', prevStep);

