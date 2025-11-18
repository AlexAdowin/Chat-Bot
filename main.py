"""
POINT D'ENTREE PRINCIPAL - ChatBot Local
Lancez ce fichier pour démarrer le chatbot
"""

import sys
import argparse
import ttkbootstrap as ttk
from src.interface_gui import ChatbotGUIModerne
from src.chatbot import Chatbot


def mode_cli():
    """Mode ligne de commande interactif"""
    print("\n" + "="*60)
    print("  CHATBOT LOCAL - Mode Terminal")
    print("="*60)
    print("\nTapez vos messages ci-dessous (tapez 'quitter' pour sortir)")
    print("-"*60 + "\n")
    
    chatbot = Chatbot()
    
    while True:
        try:
            entree = input("Vous: ").strip()
            
            if not entree:
                continue
            
            if entree.lower() in ['quitter', 'quit', 'exit', 'bye']:
                print("\nBot: Au revoir! A bientôt!")
                break
            
            reponse, intention = chatbot.traiter_entree(entree)
            print(f"\nBot: {reponse}\n[Intention: {intention}]\n")
        
        except KeyboardInterrupt:
            print("\n\nBot: Au revoir!")
            break
        
        except Exception as e:
            print(f"Erreur: {e}\n")


def mode_gui():
    """Mode interface graphique (thème noir)"""
    # THEMES NOIRS POSSIBLES : 
    #  - darkly
    #  - cyborg
    #  - solar
    #  - superhero
    #  - vapor
    #  - morph
    # Je mets "darkly" car c'est le plus lisible
    root = ttk.Window(themename="darkly")
    app = ChatbotGUIModerne(root)
    root.mainloop()


def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(
        description="ChatBot Local - Assistant Virtuel 100% Hors Ligne"
    )
    parser.add_argument(
        '--cli',
        action='store_true',
        help='Lancer en mode terminal (CLI)'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='ChatBot Local v2.0.0'
    )
    
    args = parser.parse_args()

    if args.cli:
        mode_cli()
    else:
        mode_gui()


if __name__ == "__main__":
    main()
    