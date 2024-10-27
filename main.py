# filename : main.py

"""
Ce programme sert à déterminer si certains mots 
sont des palindromes, c'est-à-dire qu'ils se lisent 
de gauche à droite et de droite à gauche.

Fonctions :
    - ispalindrome() : vérifie si une chaîne de caractères 
    est un palindrome ou non.
    - main() : effectue quelques tests de fonctionnement
"""

#### Fonction secondaire


def ispalindrome(p):
    """
    Vérifife si la chaîne de caractères 'p' est un palindrome,
    en vérifiant si chaque lettre concorde en le lisant de par
    la gauche et de par la droite.

    Args:
        - p : la chaîne de caractères à vérifier

    Returns:
        True : la chaine 'p' est un palindrome.
        False : la chaîne 'p' n'est pas un palindrome.
    """
    # votre code ici
    a = p.lower().translate(str.maketrans('àâäéèêëôöç', 'aaaeeeeooc', ' ?;.:/!-,\''))
    q = a[::-1]

    palindrome = True
    l = len(a)
    for i in range (l):
        if a[i-1] != q[i-1]:
            palindrome = False
            break
    return palindrome

#### Fonction principale


def main():
    """
    Quelques tests de bon fonctionnement 
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))
    print()
    for s in ["rêver", "été", "réer", "sèves", "tallât"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
