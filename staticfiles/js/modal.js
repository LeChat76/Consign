// Fonction pour ouvrir le modal
function openModal(imageSrc) {
    const modal = document.getElementById("signatureModal");
    const modalImage = document.getElementById("modalImage");

    if (modal && modalImage) {
        modalImage.src = imageSrc;
        modal.style.display = "flex"; // Utilise "flex" pour centrer le contenu
    }
}

// Fonction pour fermer le modal
function closeModal() {
    const modal = document.getElementById("signatureModal");
    if (modal) {
        modal.style.display = "none";
    }
}
