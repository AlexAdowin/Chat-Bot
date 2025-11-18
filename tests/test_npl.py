import unittest
import sys
import os

# Ajouter le répertoire racine au chemin Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.nlp import TextProcessor, SimilarityMatcher


class TestTextProcessor(unittest.TestCase):
    """Tests pour la classe TextProcessor"""
    
    def setUp(self):
        """Initialise les tests"""
        self.processor = TextProcessor()
    
    def test_normaliser_minuscules(self):
        """Test la conversion en minuscules"""
        resultat = self.processor.normaliser("BONJOUR")
        self.assertEqual(resultat, "bonjour")
    
    def test_normaliser_accents(self):
        """Test la suppression des accents"""
        resultat = self.processor.normaliser("Café")
        self.assertEqual(resultat, "cafe")
    
    def test_normaliser_multiples_accents(self):
        """Test avec plusieurs accents"""
        resultat = self.processor.normaliser("À Éèêë Îï Ôö Ùûü Ç")
        self.assertEqual(resultat, "a eeee ii oo uuu c")
    
    def test_tokenizer_basique(self):
        """Test la tokenisation simple"""
        resultat = self.processor.tokenizer("bonjour comment allez vous")
        self.assertIn("bonjour", resultat)
        self.assertIn("comment", resultat)
    
    def test_tokenizer_ponctuation(self):
        """Test la suppression de la ponctuation"""
        resultat = self.processor.tokenizer("Bonjour! Comment ça va?")
        self.assertNotIn("!", resultat)
        self.assertNotIn("?", resultat)
    
    def test_extraire_mots_cles(self):
        """Test l'extraction des mots-clés"""
        resultat = self.processor.extraire_mots_cles("Bonjour, comment allez-vous?")
        self.assertIn("bonjour", resultat)


class TestSimilarityMatcher(unittest.TestCase):
    """Tests pour la classe SimilarityMatcher"""
    
    def test_similarite_identique(self):
        """Test avec des listes identiques"""
        score = SimilarityMatcher.calcul_similarite(
            ['bonjour', 'comment'],
            ['bonjour', 'comment']
        )
        self.assertEqual(score, 1.0)
    
    def test_similarite_vide(self):
        """Test avec listes vides"""
        score = SimilarityMatcher.calcul_similarite([], ['bonjour'])
        self.assertEqual(score, 0.0)
    
    def test_similarite_partielle(self):
        """Test avec similarité partielle"""
        score = SimilarityMatcher.calcul_similarite(
            ['bonjour', 'comment'],
            ['bonjour', 'allez']
        )
        self.assertAlmostEqual(score, 1/3, places=2)
    
    def test_trouver_meilleure_correspondance(self):
        """Test la recherche de la meilleure correspondance"""
        patterns = {
            'salutation': ['bonjour', 'salut', 'coucou'],
            'calcul': ['plus', 'moins', 'calcul'],
            'aide': ['aide', 'help', 'assistance']
        }
        
        intention, score = SimilarityMatcher.trouver_meilleure_correspondance(
            "Bonjour comment ça va",
            patterns
        )
        
        self.assertEqual(intention, 'salutation')
        self.assertGreater(score, 0.0)


if __name__ == '__main__':
    unittest.main()
