import re

class Regex:
    @staticmethod
    def verif_mail(mail):
        regex = "^[a-z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}$"
        verification = re.search(regex, mail)
        if verification :
            return True
    
    @staticmethod
    def verif_mdp(mdp):
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
        regex = "^0[1-678]([-. ]?[0-9]{2}){4}$"
        verification = re.search(regex, tel)
        if verification:
            return True
    
    @staticmethod
    def verif_cp(cp):
        regex = "^(([0-95][1-95]|2A|2B)[0-9]{3})$|^[971-974]$"
        verification = re.search(regex, cp)
        if verification:
            return True