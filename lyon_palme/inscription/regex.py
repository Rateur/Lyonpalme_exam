import re


class Regex:
    """Ensemble centralisé d'expressions régulières utilisées pour valider les formulaires métiers."""

    @staticmethod
    def verif_mail(mail):
        """Valide les adresses e-mail au format standard (nom@domaine.tld)."""
        regex = "^[a-z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}$"
        verification = re.search(regex, mail)
        if verification :
            return True
    
    @staticmethod
    def verif_mdp(mdp):
        """Applique la politique de mot de passe forte : minuscules, majuscules, chiffres, caractères spéciaux et longueur."""
        regex_min = "(?=.*[a-z])"
        regex_maj = "(?=.*[A-Z])"
        regex_chiffre = "(?=.*[0-9])"
        regex_special = "(?=.*[^A-Za-z0-9])"
        regex_longueur = "(?=.{12,})"
        regex_longueur2 = "(?=.{14,})"
        verif_min = re.search(regex_min, mdp)
        verif_maj = re.search(regex_maj, mdp)
        verif_chiffre = re.search(regex_chiffre, mdp)
        verif_special = re.search(regex_special, mdp)
        verif_longueur = re.search(regex_longueur, mdp)
        verif_longueur2 = re.search(regex_longueur2, mdp)
        if verif_min and verif_maj and verif_chiffre and verif_special and verif_longueur or verif_min and verif_maj and verif_chiffre and verif_longueur2 :
            return True
    
    @staticmethod
    def verif_tel(tel):
        """S'assure que le numéro français commence par 0 et est composé de couples de chiffres séparés ou non."""
        regex = "^0[1-678]([-. ]?[0-9]{2}){4}$"
        verification = re.search(regex, tel)
        if verification:
            return True
    
    @staticmethod
    def verif_cp(cp):
        """Valide les codes postaux métropolitains et ultra-marins (971 à 974)."""
        regex = "^(([0-95][1-95]|2A|2B)[0-9]{3})$|^[971-974]$"
        verification = re.search(regex, cp)
        if verification:
            return True
