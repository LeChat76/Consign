// URL fixe vers la page historique
const historicUrl = "/historique/";

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

// Affiche le modal
function showPasswordModal() {
    document.getElementById('passwordModal').style.display = 'flex';
}

// Masque le modal
function closePasswordModal() {
    document.getElementById('passwordModal').style.display = 'none';
}

// Vérifie le mot de passe et redirige si correct
function checkPassword() {
    const password = document.getElementById('passwordInput').value;
    const correctPassword = "motdepasse"; // Remplace par le mot de passe réel

    if (password === correctPassword) {
        window.location.href = "/historique/";
    } else {
        alert("Mot de passe incorrect.");
    }
}

// Ferme le modal en cliquant en dehors du contenu
window.onclick = function(event) {
    const modal = document.getElementById('passwordModal');
    if (event.target === modal) {
        closeModal();
    }
}

let currentLivraisonId = null;

// Afficher le modal de confirmation
function showCancelModal(livraisonId) {
    currentLivraisonId = livraisonId;
    document.getElementById('cancelModal').style.display = 'flex';
}

// Fermer le modal
function closeCancelModal() {
    document.getElementById('cancelModal').style.display = 'none';
    currentLivraisonId = null;
}

function confirmCancel() {
    console.log("La fonction confirmCancel est appelée !");
    
    if (currentLivraisonId) {
        console.log("Envoi de la requête pour annuler l'enregistrement :", currentLivraisonId);

        fetch(`/annuler-livraison/${currentLivraisonId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({ recordDisabled: true }),
        })
        .then(response => {
            if (response.ok) {
                console.log("Enregistrement annulé avec succès !");
                window.location.reload();
            } else {
                console.error("Erreur lors de l'annulation de l'enregistrement.");
            }
        })
        .catch(error => console.error("Erreur de requête :", error));
    } else {
        console.error("ID de livraison introuvable !");
    }
}
