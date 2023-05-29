import time
import sys

class Color:
    """Classe définissant les codes de couleur ANSI RGB pour l'affichage coloré"""

    RESET = '\033[0m'

    # Définition des couleurs
    RED = '\033[38;2;255;0;0m'
    GREEN = '\033[38;2;0;255;0m'
    BLUE = '\033[38;2;0;0;255m'
    # Ajoutez d'autres couleurs ici


def print_color(text, color):
    """Affiche le texte donné dans la couleur RGB spécifiée"""
    color_code = color
    print(f"{color_code}{text}{Color.RESET}")


def animate_text(text, colors, delay=0.2):
    """Anime le texte en changeant de couleur à chaque itération"""
    num_colors = len(colors)
    for char in text:
        for i in range(num_colors):
            color = colors[i]
            sys.stdout.write(f"\r{color}{char}{Color.RESET}")
            sys.stdout.flush()
            time.sleep(delay)
    sys.stdout.write("\n")
