import re
import string
from typing import List, Dict, Tuple

class TextProcessor:
    """Classe pour nettoyer et traiter le texte brut"""
    
    def __init__(self):
        # Liste de mots vides (stop words) en français
        self.stop_words = {
            'le', 'la', 'les', 'de', 'du', 'des', 'un', 'une', 'des',
            'et', 'ou', 'mais', 'donc', 'car', 'par', 'pour', 'avec',
            'sans', 'sous', 'sur', 'entre', 'dans', 'à', 'au', 'aux',
            'est', 'sont', 'être', 'avoir', 'ce', 'cet', 'cette',
            'je', 'tu', 'il', 'elle', 'nous', 'vous', 'ils', 'elles'
        }
    
    def normaliser(self, texte: str) -> str:
        """
        Normalise le texte :
        - Convertit en minuscules
        - Supprime les accents
        - Supprime les caractères spéciaux
        """
        # Minuscules
        texte = texte.lower()
        
        # Supprimer les accents
        accents = {
            'à': 'a', 'â': 'a', 'ä': 'a',
            'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
            'î': 'i', 'ï': 'i',
            'ô': 'o', 'ö': 'o',
            'ù': 'u', 'û': 'u', 'ü': 'u',
            'ç': 'c'
        }
        for accent, lettre in accents.items():
            texte = texte.replace(accent, lettre)
        
        return texte
    
    def tokenizer(self, texte: str) -> List[str]:
        """
        Divise le texte en mots (tokens)
        et supprime les mots vides
        """
        # Nettoyer la ponctuation
        texte = re.sub(r'[.!?,;:\'""-]', ' ', texte)
        
        # Diviser en mots
        mots = texte.split()
        
        mots_filtres = [
            mot for mot in mots 
            if mot and mot not in self.stop_words and len(mot) > 0
        ]
        
        return mots_filtres
    
    def extraire_mots_cles(self, texte: str) -> List[str]:
        """Extrait les mots-clés du texte"""
        texte_normalise = self.normaliser(texte)
        mots_cles = self.tokenizer(texte_normalise)
        return mots_cles


class SimilarityMatcher:
    """Calcule la similarité entre deux textes"""
    
    @staticmethod
    def calcul_similarite(mots1: List[str], mots2: List[str]) -> float:
        """
        Calcule le score de similarité entre deux listes de mots
        Utilise l'algorithme Jaccard (intersection / union)
        """
        if not mots1 or not mots2:
            return 0.0
        
        # Convertir en ensembles
        ensemble1 = set(mots1)
        ensemble2 = set(mots2)
        
        # Intersection et union
        intersection = len(ensemble1 & ensemble2)
        union = len(ensemble1 | ensemble2)
        
        if union == 0:
            return 0.0
        
        # Retourner le coefficient Jaccard (0 à 1)
        return intersection / union
    
    @staticmethod
    def trouver_meilleure_correspondance(
        texte_utilisateur: str,
        patterns: Dict[str, List[str]]
    ) -> Tuple[str, float]:
        """
        Trouve le pattern le plus similaire au texte utilisateur
        Retourne (pattern_id, score_similarite)
        """
        processor = TextProcessor()
        mots_utilisateur = processor.extraire_mots_cles(texte_utilisateur)
        
        meilleur_pattern = None
        meilleur_score = 0.0
        
        for pattern_id, pattern_mots in patterns.items():
            score = SimilarityMatcher.calcul_similarite(
                mots_utilisateur, 
                pattern_mots
            )
            
            if score > meilleur_score:
                meilleur_score = score
                meilleur_pattern = pattern_id
        
        # Si aucun match fort, chercher des correspondances partielles
        if meilleur_score < 0.25:
            for pattern_id, pattern_mots in patterns.items():
                # Vérifier si plusieurs mots importants correspondent
                mots_correspondants = sum(1 for mot in mots_utilisateur if mot in pattern_mots)
                if mots_correspondants >= max(1, len(mots_utilisateur) // 2):
                    score = 0.25 + (mots_correspondants / len(pattern_mots) if pattern_mots else 0) * 0.1
                    if score > meilleur_score:
                        meilleur_score = score
                        meilleur_pattern = pattern_id
        
        return meilleur_pattern, meilleur_score
