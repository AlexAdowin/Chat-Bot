import tkinter as tk
from tkinter import scrolledtext, messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from src.chatbot import Chatbot
from src.memoire import ConversationMemory
import threading
from datetime import datetime

class ChatbotGUIModerne:
    """Interface graphique moderne du chatbot"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot Local - Assistant Intelligent")
        self.root.geometry("1100x800")
        
        # Initialiser le chatbot
        self.chatbot = Chatbot()
        self.memoire = self.chatbot.memoire
        
        # Flag pour éviter les soumissions multiples
        self.traitement_en_cours = False
        
        # Créer l'interface
        self._creer_interface()
        
        # Message d'accueil
        self._afficher_accueil()
        
        # Configurer le window close
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
    
    def _creer_interface(self):
        """Crée tous les éléments de l'interface moderne"""
        
        # === CONTENEUR PRINCIPAL ===
        main_container = ttk.Frame(self.root, bootstyle="light")
        main_container.pack(fill=BOTH, expand=True)
        
        # === HEADER MODERNE ===
        self._creer_header(main_container)
        
        # === CONTENU PRINCIPAL ===
        content_frame = ttk.Frame(main_container, bootstyle="light")
        content_frame.pack(fill=BOTH, expand=True, padx=15, pady=10)
        
        # === ZONE DE CONVERSATION ===
        chat_container = ttk.Labelframe(
            content_frame,
            text="Conversation",
            bootstyle="info",
            padding=10
        )
        chat_container.pack(fill=BOTH, expand=True, pady=(0, 10))
        
        self.historique_text = scrolledtext.ScrolledText(
            chat_container,
            height=20,
            wrap=tk.WORD,
            font=("Segoe UI", 10),
            bg="#f8f9fa",
            fg="#2c3e50",
            insertbackground="#0d47a1",
            relief=tk.FLAT,
            borderwidth=0
        )
        self.historique_text.pack(fill=BOTH, expand=True)
        
        # Configuration des tags pour le style moderne
        self.historique_text.tag_config("utilisateur", foreground="#0d47a1", font=("Segoe UI", 10, "bold"))
        self.historique_text.tag_config("bot", foreground="#00796b", font=("Segoe UI", 10, "bold"))
        self.historique_text.tag_config("system", foreground="#d32f2f", font=("Segoe UI", 9, "italic"))
        self.historique_text.tag_config("timestamp", foreground="#757575", font=("Segoe UI", 8))
        
        # === ZONE DE SAISIE ===
        input_container = ttk.Labelframe(
            content_frame,
            text="Votre message",
            bootstyle="info",
            padding=10
        )
        input_container.pack(fill=BOTH, expand=False)
        
        self.saisie_text = tk.Text(
            input_container,
            height=4,
            font=("Segoe UI", 11),
            bg="white",
            fg="#2c3e50",
            insertbackground="#0d47a1",
            relief=tk.FLAT,
            borderwidth=1,
            wrap=tk.WORD
        )
        self.saisie_text.pack(fill=BOTH, expand=True, pady=(0, 10))
        self.saisie_text.bind("<Control-Return>", lambda e: self._envoyer_message())
        self.saisie_text.bind("<Control-l>", lambda e: self._effacer_historique())
        
        # Placeholder
        self.saisie_text.insert("1.0", "Tapez votre message... (Ctrl+Entrée pour envoyer)")
        self.saisie_text.bind("<FocusIn>", self._on_saisie_focus_in)
        self.saisie_text.bind("<FocusOut>", self._on_saisie_focus_out)
        
        # === BOUTONS MODERNES ===
        self._creer_boutons(input_container)
        
        # === STATUS BAR ===
        self._creer_status_bar(main_container)
    
    def _creer_header(self, parent):
        """Crée l'en-tête moderne"""
        header = ttk.Frame(parent, bootstyle="info")
        header.pack(fill=X)
        
        header_content = ttk.Frame(header, bootstyle="info")
        header_content.pack(fill=BOTH, expand=True, padx=20, pady=15)
        
        titre = ttk.Label(
            header_content,
            text="ChatBot Local",
            font=("Segoe UI", 24, "bold"),
            bootstyle="inverse-info"
        )
        titre.pack(anchor=W)
        
        sous_titre = ttk.Label(
            header_content,
            text="Assistant virtuel intelligent - Fonctionne 100% hors ligne",
            font=("Segoe UI", 10),
            bootstyle="inverse-info"
        )
        sous_titre.pack(anchor=W, pady=(3, 0))
    
    def _creer_boutons(self, parent):
        """Crée les boutons d'action modernes"""
        boutons_frame = ttk.Frame(parent)
        boutons_frame.pack(fill=X, pady=5)
        
        envoyer_btn = ttk.Button(
            boutons_frame,
            text="Envoyer",
            command=self._envoyer_message,
            bootstyle="success",
            width=20
        )
        envoyer_btn.pack(side=LEFT, padx=5)
        
        stats_btn = ttk.Button(
            boutons_frame,
            text="Statistiques",
            command=self._afficher_stats,
            bootstyle="primary",
            width=18
        )
        stats_btn.pack(side=LEFT, padx=5)
        
        aide_btn = ttk.Button(
            boutons_frame,
            text="Aide",
            command=self._afficher_aide,
            bootstyle="info",
            width=15
        )
        aide_btn.pack(side=LEFT, padx=5)
        
        clear_btn = ttk.Button(
            boutons_frame,
            text="Effacer",
            command=self._effacer_historique,
            bootstyle="danger",
            width=15
        )
        clear_btn.pack(side=LEFT, padx=5)
        
        copy_btn = ttk.Button(
            boutons_frame,
            text="Copier",
            command=self._copier_historique,
            bootstyle="secondary",
            width=15
        )
        copy_btn.pack(side=LEFT, padx=5)
    
    def _creer_status_bar(self, parent):
        """Crée la barre de statut"""
        status_frame = ttk.Frame(parent, bootstyle="dark")
        status_frame.pack(fill=X, side=BOTTOM)
        
        self.status_label = ttk.Label(
            status_frame,
            text="Pret - En attente de message...",
            font=("Segoe UI", 9),
            bootstyle="inverse-dark"
        )
        self.status_label.pack(anchor=W, padx=10, pady=6)
    
    def _on_saisie_focus_in(self, event):
        """Efface le placeholder au focus"""
        if self.saisie_text.get("1.0", tk.END).strip() == "Tapez votre message... (Ctrl+Entrée pour envoyer)":
            self.saisie_text.delete("1.0", tk.END)
            self.saisie_text.config(fg="#2c3e50")
    
    def _on_saisie_focus_out(self, event):
        """Affiche le placeholder si vide"""
        if self.saisie_text.get("1.0", tk.END).strip() == "":
            self.saisie_text.insert("1.0", "Tapez votre message... (Ctrl+Entrée pour envoyer)")
            self.saisie_text.config(fg="#999999")
    
    def _afficher_accueil(self):
        """Affiche le message d'accueil moderne"""
        self.historique_text.config(state=tk.NORMAL)
        
        accueil = """
BIENVENUE DANS CHATBOT LOCAL V2.0
Assistant virtuel intelligent - Fonctionne 100% hors ligne

DEMARRAGE REUSSI

Tapez votre message et appuyez sur Ctrl+Entrée pour envoyer.

EXEMPLES:
  - "Bonjour" - Salutation simple
  - "Qui es-tu ?" - Questions sur le bot
  - "5 + 3" - Calculs mathematiques
  - "Quelle heure ?" - Demander l'heure
  - "Raconte une blague" - Humour
  - "Donne-moi un conseil" - Conseils

Utilisez le bouton "Aide" pour voir toutes les commandes.

================================================================

"""
        self.historique_text.insert(tk.END, accueil, "system")
        self.historique_text.config(state=tk.DISABLED)
        self.historique_text.see(tk.END)
        self._update_status("Pret - En attente de message...")
    
    def _envoyer_message(self):
        """Traite et envoie le message"""
        if self.traitement_en_cours:
            self._update_status("Traitement en cours...")
            return
        
        message = self.saisie_text.get("1.0", tk.END).strip()
        
        if not message or message == "Tapez votre message... (Ctrl+Entrée pour envoyer)":
            return
        
        self.traitement_en_cours = True
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.historique_text.config(state=tk.NORMAL)
        self.historique_text.insert(tk.END, f"\n[{timestamp}] ", "timestamp")
        self.historique_text.insert(tk.END, f"Vous: {message}\n", "utilisateur")
        self.historique_text.config(state=tk.DISABLED)
        self.historique_text.see(tk.END)
        
        self.saisie_text.delete("1.0", tk.END)
        self._update_status("Traitement de votre message...")
        
        thread = threading.Thread(target=self._traiter_reponse, args=(message,))
        thread.daemon = True
        thread.start()
    
    def _traiter_reponse(self, message):
        """Traite la réponse du chatbot"""
        try:
            reponse, intention = self.chatbot.traiter_entree(message)
            
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.historique_text.config(state=tk.NORMAL)
            self.historique_text.insert(tk.END, f"[{timestamp}] ", "timestamp")
            self.historique_text.insert(tk.END, f"Bot: {reponse}\n", "bot")
            self.historique_text.config(state=tk.DISABLED)
            self.historique_text.see(tk.END)
            
            stats = self.memoire.obtenir_stats()
            self._update_status(f"Derniere intention: {intention} - Messages: {stats['total_messages']}")
            
        except Exception as e:
            self.historique_text.config(state=tk.NORMAL)
            self.historique_text.insert(tk.END, f"Erreur: {str(e)}\n", "system")
            self.historique_text.config(state=tk.DISABLED)
            self._update_status("Erreur lors du traitement")
        
        finally:
            self.traitement_en_cours = False
    
    def _afficher_stats(self):
        """Affiche les statistiques de manière moderne"""
        stats = self.memoire.obtenir_stats()
        
        message_stats = f"""

STATISTIQUES DE CONVERSATION

Total de messages: {stats['total_messages']}
Messages utilisateur: {stats['messages_utilisateur']}
Messages bot: {stats['messages_bot']}

Intentions detectees:
"""
        
        if stats['intentions']:
            sorted_intentions = sorted(stats['intentions'].items(), key=lambda x: x[1], reverse=True)
            for intention, count in sorted_intentions:
                message_stats += f"  - {intention}: {count}\n"
        else:
            message_stats += "  (Aucune)\n"
        
        self.historique_text.config(state=tk.NORMAL)
        self.historique_text.insert(tk.END, message_stats, "system")
        self.historique_text.config(state=tk.DISABLED)
        self.historique_text.see(tk.END)
    
    def _effacer_historique(self):
        """Efface l'historique avec confirmation"""
        if messagebox.askyesno("Confirmation", "Etes-vous sur de vouloir effacer tout l'historique ?\n\nCette action est irreversible."):
            self.memoire.effacer_historique()
            self.historique_text.config(state=tk.NORMAL)
            self.historique_text.delete("1.0", tk.END)
            self.historique_text.config(state=tk.DISABLED)
            self._afficher_accueil()
            self._update_status("Historique efface - Pret")
    
    def _copier_historique(self):
        """Copie l'historique dans le presse-papiers"""
        try:
            contenu = self.historique_text.get("1.0", tk.END)
            self.root.clipboard_clear()
            self.root.clipboard_append(contenu)
            self._update_status("Historique copie dans le presse-papiers")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de copier: {e}")
    
    def _afficher_aide(self):
        """Affiche l'aide de manière moderne"""
        aide = """

AIDE ET GUIDE COMPLET

CATEGORIES DE COMMANDES:

1. SALUTATIONS
   "Bonjour", "Salut", "Coucou", "Ca va ?"

2. INFORMATION SUR LE BOT
   "Qui es-tu ?", "D'ou viens-tu ?", "Presente-toi"

3. DEMANDE D'AIDE
   "Aide-moi", "Aide", "Help", "SOS"

4. BLAGUES ET HUMOUR
   "Raconte une blague", "Dis quelque chose de drole"

5. CALCULS MATHEMATIQUES
   "5 + 3", "10 * 2", "100 / 5", "5 plus 3"

6. HEURE ET DATE
   "Quelle heure ?", "Quelle est la date ?", "Donne-moi l'heure"

7. CONSEILS
   "Donne-moi un conseil", "Un conseil", "Conseil du jour"

8. REMERCIEMENTS
   "Merci", "Merci beaucoup", "Merci !"

9. ADIEU
   "Au revoir", "Bye", "A plus", "A bientot"

RACCOURCIS CLAVIER:
  - Ctrl+Entree : Envoyer le message
  - Ctrl+L : Effacer l'historique

SYSTEME DE MEMOIRE:
  Chaque conversation est automatiquement sauvegardee
  dans data/chat_history.json pour une persistance

FONCTIONNALITES:
  - 100% hors ligne (aucune connexion Internet requise)
  - Reconnaissance intelligente d'intentions
  - Memoire persistante des conversations
  - Interface moderne et reactive
  - Calculs mathematiques en temps reel
  - Timestamps pour chaque message

"""
        self.historique_text.config(state=tk.NORMAL)
        self.historique_text.insert(tk.END, aide, "system")
        self.historique_text.config(state=tk.DISABLED)
        self.historique_text.see(tk.END)
    
    def _update_status(self, text):
        """Met à jour le statut"""
        self.status_label.config(text=text)
        self.root.update_idletasks()
    
    def _on_closing(self):
        """Gère la fermeture de l'application"""
        if messagebox.askokcancel("Quitter", "Voulez-vous quitter ChatBot ?"):
            self.root.destroy()
