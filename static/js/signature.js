// Fonction pour effacer la signature
function clearSignature(who) {
    if (who === "chauffeur") {
        if (window.signaturePadChauffeur) {
            signaturePadChauffeur.clear();
        } else {
            console.error("Erreur : SignaturePadChauffeur n'est pas initialisé.");
        }
    } else if (who === "employe") {
        if (window.signaturePadEmploye) {
            signaturePadEmploye.clear();
        } else {
            console.error("Erreur : SignaturePadEmploye n'est pas initialisé.");
        }
    }
}

// Attendre que le DOM soit chargé
document.addEventListener("DOMContentLoaded", function () {

    // Récupérer les canvas pour les signatures
    const canvasChauffeur = document.getElementById("signature-pad-chauffeur");
    const canvasEmploye = document.getElementById("signature-pad-employe");

    // Initialiser les instances de SignaturePad
    window.signaturePadChauffeur = new SignaturePad(canvasChauffeur);
    window.signaturePadEmploye = new SignaturePad(canvasEmploye);

    // récupération des noms des chauffeur et employe
    const nomChauffeur = document.getElementById("nom_chauffeur").value;
    const nomEmploye = document.getElementById("nom_employe").value;

    const nomChauffeurField = document.getElementById("nom_chauffeur");
    const nomEmployeField = document.getElementById("nom_employe");

    // Récupérer le formulaire
    const form = document.getElementById("livraisonForm");
    if (!form) {
        console.error("Erreur : Le formulaire 'livraisonForm' est introuvable !");
        return;
    }

    // Gestion de la soumission du formulaire
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Empêche le rechargement de la page

        // Vérifier si les signatures sont vides
        if (signaturePadChauffeur.isEmpty()) {
            alert("La signature du transporteur est obligatoire.");
            return;
        }
        if (signaturePadEmploye.isEmpty()) {
            alert("La signature de l'employé est obligatoire.");
            return;
        }

        // Création des données du formulaire
        const formData = new FormData(form);
        formData.append("signature_chauffeur", signaturePadChauffeur.toDataURL());
        formData.append("signature_employe", signaturePadEmploye.toDataURL());

        //console.log("Envoi des données avec fetch...");

        //console.log("Transporteur :", document.getElementById("transporteur").value);
        //console.log("Nombre de palettes :", document.getElementById("nombre_palettes").value);
        //console.log("Numéro de commande :", document.getElementById("numero_commande").value);
        //console.log("Réserve :", document.getElementById("reserve").value);
        //console.log("Nom chauffeur :", document.getElementById("nom_chauffeur").value);
        //console.log("Signature transporteur :", signaturePadChauffeur.toDataURL());
        //console.log("Nom employé :", document.getElementById("nom_employe").value);
        //console.log("Signature employé :", signaturePadEmploye.toDataURL());   

        // Envoi des données au serveur
        fetch(form.action, {
            method: "POST",
            body: formData,
        })
            .then((response) => response.json())
            .then((data) => {
                //console.log("Réponse du serveur :", data);
                //alert(data.message);
                location.reload(); // Recharge la page après l'enregistrement
            })
            .catch((error) => console.error("Erreur lors de l'envoi des données :", error));
    });
});
