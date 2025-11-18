from typing import Dict, Tuple, List
import re
from src.nlp import TextProcessor, SimilarityMatcher

class IntentionDatabase:
    """Base des intentions avec mots-clés et contexte"""
    def __init__(self):
        self.intentions: Dict[str, Dict] = {}
        self._initialiser_intentions()

    def _initialiser_intentions(self):
        self.intentions = {
            'salutations': {'mots_cles': ['bonjour', 'salut', 'coucou', 'hey' , 'cc' , 'bonsoir' ], 'contexte': 'salutation'},
            'presentations': {'mots_cles': ['qui es tu', 'présente toi', 'que fais tu' , 'tu es'], 'contexte': 'presentation'},
            'aide': {'mots_cles': ['aide', 'help', 'assistance'], 'contexte': 'demande aide'},
            'meteo': {'mots_cles': ['météo', 'temps', 'soleil'], 'contexte': 'demande météo'},
            'heure': {'mots_cles': ['heure', 'date', 'moment'], 'contexte': 'demande heure/date'},
            'blagues': {'mots_cles': ['blague', 'rigolo', 'fais moi rire'], 'contexte': 'demande blague'},
            'calcul': {'mots_cles': ['calcul', '+', '-', '*', '/'], 'contexte': 'demande calcul'},
            'conseils': {'mots_cles': ['conseil', 'suggestion', 'avis'], 'contexte': 'demande conseil'},
            'remerciements': {'mots_cles': ['merci', 'thanks'], 'contexte': 'remercier bot'},
            'adieu': {'mots_cles': ['au revoir', 'bye', 'ciao'], 'contexte': 'terminer discussion'},
            'oui': {'mots_cles': ['oui', 'ok', 'yes'], 'contexte': 'affirmation'},
            'non': {'mots_cles': ['non', 'no'], 'contexte': 'négation'},
           # 'discussion': {'mots_cles': ['ça va', 'quoi de neuf', 'comment tu vas'], 'contexte': 'discussion'},
            'info_user': {'mots_cles': ['je m\'appelle', 'je suis', 'mon nom'], 'contexte': 'info utilisateur'},
            'cv': {'mots_cles': ['cv ?', 'comment ça va', 'comment tu vas' , 'sa va' , 'ca va' , 'comment vas tu ' , 'bien?' ], 'contexte': 'discussion'},
        }

    def obtenir_patterns(self) -> Dict[str, List[str]]:
        return {intent: data['mots_cles'] for intent, data in self.intentions.items()}


class IntentionDetector:
    """Détecte l'intention de l'utilisateur"""
    def __init__(self, confiance_min: float = 0.05):
        self.int_db = IntentionDatabase()
        self.processor = TextProcessor()
        self.confiance_min = confiance_min

    def detecter_intention(self, texte: str) -> Tuple[str, float]:
        texte_norm = self.processor.normaliser(texte)

        # Détection de calcul rapide
        if any(c.isdigit() for c in texte_norm) and any(op in texte_norm for op in ['+', '-', '*', '/']):
            return 'calcul', 0.95

        patterns = self.int_db.obtenir_patterns()
        intention, score = SimilarityMatcher.trouver_meilleure_correspondance(texte_norm, patterns)

        if score < self.confiance_min or intention is None:
            return 'autre', 0.0

        return intention, float(score)

    def detecter_entites(self, texte: str) -> Dict:
        """Extrait nombres et nom de l'utilisateur"""
        nombres = [float(n.replace(',', '.')) for n in re.findall(r'\d+(?:[.,]\d+)?', texte)]
        nom = None
        match = re.search(r"je\s+m[' ]appelle\s+(\w+)|je\s+suis\s+(\w+)|mon\s+nom\s+est\s+(\w+)", texte.lower())
        if match:
            nom = next(filter(None, match.groups())).capitalize()
        return {'nombres': nombres, 'nom': nom}
