// Délai de redirection après inactivité (1 minute = 60000 ms)
const redirectionDelay = 60 * 1000; 
const deliveryPageUrl = "/delivery_consignation/";

// Variable pour stocker le timer
let inactivityTimer;

// Fonction de redirection automatique
function redirectToDelivery() {
    window.location.href = deliveryPageUrl;
}

// Fonction pour réinitialiser le timer en cas d'activité utilisateur
function resetInactivityTimer() {
    clearTimeout(inactivityTimer);
    inactivityTimer = setTimeout(redirectToDelivery, redirectionDelay);
}

// Démarre la détection d'inactivité lors du chargement de la page
window.onload = function() {
    
    // Lance le timer dès qu'il y a une activité
    resetInactivityTimer();

    // Détecte les mouvements de la souris
    document.addEventListener('mousemove', resetInactivityTimer);

    // Détecte les clics de souris
    document.addEventListener('click', resetInactivityTimer);

    // Détecte les pressions de touches au clavier
    document.addEventListener('keydown', resetInactivityTimer);
};
