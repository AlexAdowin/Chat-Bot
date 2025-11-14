# Chat-Bot
# ChatBot Local v2.0

Un assistant virtuel intelligent qui fonctionne **100% hors ligne** sans Internet, sans API, sans IA externe.

## Caractéristiques Principales

✅ **Entièrement Local** - Fonctionne sur votre machine sans connexion Internet  
✅ **Reconnaissance d'Intentions** - Comprend 11+ intentions différentes  
✅ **Mémoire Persistante** - Sauvegarde automatique des conversations  
✅ **Interface Moderne** - GUI élégante avec tkinter bootstrap  
✅ **Python Pur** - Code simple à lire et comprendre  
✅ **Rapide et Léger** - Aucune dépendance lourde  
✅ **Tests Unitaires** - Suite complète de tests  

## Structure du Projet

\`\`\`
chatbot-local/
├── src/                      # Code source principal
│   ├── __init__.py
│   ├── nlp.py               # Traitement du texte
│   ├── intentions.py        # Détection d'intentions
│   ├── base_connaissance.py # Réponses du chatbot
│   ├── memoire.py           # Gestion de l'historique
│   ├── chatbot.py           # Moteur principal
│   └── interface_gui.py     # Interface graphique moderne
├── tests/                    # Tests unitaires
│   ├── __init__.py
│   ├── test_nlp.py
│   ├── test_intentions.py
│   ├── test_base_connaissance.py
│   └── test_chatbot.py
├── data/                     # Données et historique
│   └── chat_history.json    # Sauvegarde automatique
├── main.py                   # Point d'entrée principal
├── requirements.txt          # Dépendances Python
└── README.md                 # Documentation
\`\`\`

## Installation

### Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'Installation

1. **Cloner ou télécharger le projet**

\`\`\`bash
git clone <url-du-repo>
cd chatbot-local
\`\`\`

2. **Créer un environnement virtuel (recommandé)**

\`\`\`bash
# Sur macOS/Linux :
python3 -m venv venv
source venv/bin/activate

# Sur Windows :
python -m venv venv
venv\Scripts\activate
\`\`\`

3. **Installer les dépendances**

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Utilisation

### Mode Interface Graphique (par défaut)

\`\`\`bash
python main.py
\`\`\`

Lance l'interface graphique moderne avec tkinter. C'est le mode recommandé pour une meilleure expérience utilisateur.

**Fonctionnalités:**
- Chat en temps réel avec timestamps
- Statistiques de conversation
- Historique persistant
- Boutons d'action (Envoyer, Aide, Statistiques, Effacer, Copier)
- Raccourcis clavier (Ctrl+Entrée pour envoyer, Ctrl+L pour effacer)

### Mode Terminal (CLI)

\`\`\`bash
python main.py --cli
\`\`\`

Lance le chatbot en mode ligne de commande simple. Parfait pour les tests rapides ou l'intégration.

## Catégories de Commandes

### 1. Salutations
"Bonjour", "Salut", "Coucou", "Ça va ?"

### 2. Information sur le Bot
"Qui es-tu ?", "Présente-toi", "D'où viens-tu ?"

### 3. Demande d'Aide
"Aide-moi", "Aide", "Help"

### 4. Blagues et Humour
"Raconte une blague", "Dis quelque chose de drôle"

### 5. Calculs Mathématiques
"5 + 3", "10 * 2", "100 / 5", "5 plus 3"

### 6. Heure et Date
"Quelle heure ?", "Quelle est la date ?", "Donne-moi l'heure"

### 7. Conseils
"Donne-moi un conseil", "Un conseil", "Conseil du jour"

### 8. Remerciements
"Merci", "Merci beaucoup", "Merci !"

### 9. Adieu
"Au revoir", "Bye", "À plus", "À bientôt"

## Raccourcis Clavier (GUI)

| Raccourci | Action |
|-----------|--------|
| Ctrl+Entrée | Envoyer le message |
| Ctrl+L | Effacer l'historique |

## Architecture Technique

### Flux de Traitement

\`\`\`
Entrée Utilisateur
        ↓
    [NLP] → Normalisation + Tokenization
        ↓
[Intentions] → Détection d'intention + Extraction d'entités
        ↓
[Base Connaissance] → Génération de réponse
        ↓
    [Mémoire] → Sauvegarde
        ↓
    Réponse Finale
\`\`\`

### Modules Principaux

#### `nlp.py` - Traitement du Texte
- **TextProcessor**: Normalise et nettoie le texte
- **SimilarityMatcher**: Calcule la similarité entre textes (algorithme Jaccard)

#### `intentions.py` - Détection d'Intentions
- **IntentionDatabase**: Base de 11+ intentions avec patterns
- **IntentionDetector**: Détecte l'intention de l'utilisateur

#### `base_connaissance.py` - Réponses
- **BaseConnaissance**: Stocke toutes les réponses possibles
- Support des réponses dynamiques (heure, calculs)

#### `memoire.py` - Historique
- **ConversationMemory**: Gère la sauvegarde des conversations
- Persistance automatique en JSON

#### `chatbot.py` - Orchestration
- **Chatbot**: Classe principale qui orchestre tous les modules

#### `interface_gui.py` - Interface
- **ChatbotGUIModerne**: Interface graphique moderne avec ttkbootstrap

## Tests Unitaires

Exécuter tous les tests:

\`\`\`bash
python -m unittest discover tests/
\`\`\`

Exécuter un test spécifique:

\`\`\`bash
python -m unittest tests.test_nlp.TestTextProcessor.test_normaliser_minuscules
\`\`\`

Tests disponibles:
- `test_nlp.py` - Tests du traitement du texte (9 tests)
- `test_intentions.py` - Tests de détection d'intentions (6 tests)
- `test_base_connaissance.py` - Tests des réponses (8 tests)
- `test_chatbot.py` - Tests du moteur principal (6 tests)

Total: 29 tests unitaires

## Fichiers de Données

### `data/chat_history.json`

Fichier de sauvegarde automatique de l'historique. Structure:

\`\`\`json
[
  {
    "timestamp": "2024-11-12T10:30:45.123456",
    "auteur": "utilisateur",
    "contenu": "Bonjour",
    "intention": null
  },
  {
    "timestamp": "2024-11-12T10:30:46.234567",
    "auteur": "bot",
    "contenu": "Salut ! Ravi de te voir !",
    "intention": "salutation"
  }
]
\`\`\`

## Personnalisation

### Ajouter une Nouvelle Intention

Modifier `src/intentions.py`:

\`\`\`python
# Dans _initialiser_intentions()
self.intentions['ma_nouvelle_intention'] = {
    'mots_cles': ['mot1', 'mot2', 'mot3'],
    'contexte': 'Description de l\'intention'
}
\`\`\`

Puis ajouter les réponses dans `src/base_connaissance.py`:

\`\`\`python
self.reponses['ma_nouvelle_intention'] = [
    "Réponse 1",
    "Réponse 2",
]
\`\`\`

### Modifier les Stop Words

Éditer la liste dans `src/nlp.py`, classe `TextProcessor`, méthode `__init__`.

### Changer le Thème GUI

Modifier le thème dans `main.py`:

\`\`\`python
root = ttk.Window(themename="darkly")
# Autres options: "solar", "cyborg", "lumen", "superhero", etc.
\`\`\`

## Performance

- **Temps de réponse**: < 100ms
- **Utilisation mémoire**: ~50MB
- **Taille du projet**: ~150KB (code uniquement)

## Troubleshooting

### Erreur: `ModuleNotFoundError: No module named 'ttkbootstrap'`

Solution:
\`\`\`bash
pip install ttkbootstrap
\`\`\`

### L'interface GUI ne se lance pas

Solution:
\`\`\`bash
# Vérifier que tkinter est installé
python -m tkinter

# Installer sur Ubuntu/Debian:
sudo apt-get install python3-tk

# macOS: tkinter devrait être inclus avec Python
\`\`\`

### L'historique n'est pas sauvegardé

- Vérifier que le dossier `data/` existe
- Le fichier `chat_history.json` sera créé automatiquement

## Questions Fréquentes

**Q: Peut-on utiliser le chatbot hors ligne?**  
A: Oui, c'est le point fort! Le chatbot fonctionne 100% localement.

**Q: Comment ajouter plus de blagues?**  
A: Éditer `src/base_connaissance.py`, section `self.reponses['blague']`.

**Q: Le chatbot peut-il apprendre?**  
A: Actuellement, il utilise des patterns prédéfinis. La persistance en JSON permet de créer des extensions futures.

**Q: Comment exporter les conversations?**  
A: Les conversations sont en JSON dans `data/chat_history.json`. Facile à lire et traiter.

---

**Créé avec ❤️ en Python Pur**
