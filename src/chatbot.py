from src.nlp import TextProcessor, SimilarityMatcher
from src.intentions import IntentionDetector, IntentionDatabase
from src.base_connaissance import BaseConnaissance
from src.memoire import ConversationMemory
from typing import Tuple, Dict

class Chatbot:
    """Classe principale du chatbot"""
    
    def __init__(self):
        self.detector = IntentionDetector()
        self.intention_db = IntentionDatabase()
        self.base_connaissance = BaseConnaissance()
        self.memoire = ConversationMemory()
        self.processor = TextProcessor()
        
        # Compteur de confiance pour les réponses
        self.seuil_confiance = 0.2
    
    def traiter_entree(self, texte_utilisateur: str) -> Tuple[str, str]:
        """
        Traite l'entrée utilisateur et retourne une réponse
        Retourne (reponse, intention)
        """
        # Ajouter à la mémoire
        self.memoire.ajouter_message('utilisateur', texte_utilisateur)
        
        # Détecter l'intention
        intention, confiance = self.detector.detecter_intention(texte_utilisateur)
        
        # Extraire les entités
        entites = self.detector.detecter_entites(texte_utilisateur)
        
        # Si c'est un calcul, le traiter spécialement
        if intention == 'calcul' and confiance > 0.3:
            reponse = self.base_connaissance.traiter_calcul(texte_utilisateur)
        else:
            # Récupérer une réponse appropriée
            reponse = self.base_connaissance.obtenir_reponse(
                intention if confiance > self.seuil_confiance else 'autre',
                entites
            )
        
        # Ajouter la réponse à la mémoire
        self.memoire.ajouter_message('bot', reponse, intention)
        
        return reponse, intention
    
    def obtenir_reponse_avec_debug(self, texte: str) -> Dict:
        """Version avec informations de debug"""
        intention, confiance = self.detector.detecter_intention(texte)
        entites = self.detector.detecter_entites(texte)
        
        return {
            'texte_utilisateur': texte,
            'intention': intention,
            'confiance': round(confiance, 2),
            'entites': entites,
            'reponse': self.traiter_entree(texte)[0]
        }
