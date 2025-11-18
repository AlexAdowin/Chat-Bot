import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.intentions import IntentionDetector, IntentionDatabase


class TestIntentionDatabase(unittest.TestCase):
    """Tests pour la classe IntentionDatabase"""
    
    def setUp(self):
        """Initialise les tests"""
        self.db = IntentionDatabase()
    
    def test_initialisation(self):
        """Test que la base de données est bien initialisée"""
        patterns = self.db.obtenir_patterns()
        self.assertGreater(len(patterns), 0)
    
    def test_intentions_presentes(self):
        """Test que les intentions principales sont présentes"""
        patterns = self.db.obtenir_patterns()
        intentions_attendues = [
            'salutation', 'presentation', 'aide', 'blague',
            'calcul', 'heure', 'conseil'
        ]
        for intention in intentions_attendues:
            self.assertIn(intention, patterns)
    
    def test_obtenir_contexte(self):
        """Test la récupération du contexte"""
        contexte = self.db.obtenir_contexte('salutation')
        self.assertIsNotNone(contexte)
        self.assertIsInstance(contexte, str)


class TestIntentionDetector(unittest.TestCase):
    """Tests pour la classe IntentionDetector"""
    
    def setUp(self):
        """Initialise les tests"""
        self.detector = IntentionDetector()
    
    def test_detecter_salutation(self):
        """Test la détection d'une salutation"""
        intention, confiance = self.detector.detecter_intention("Bonjour")
        self.assertEqual(intention, 'salutation')
       # self.assertGreater(confiance, 0.5)
    
    def test_detecter_calcul(self):
        """Test la détection d'un calcul"""
        intention, confiance = self.detector.detecter_intention("5 plus 3")
        self.assertEqual(intention, 'calcul')
    
    def test_detecter_heure(self):
        """Test la détection d'une demande d'heure"""
        intention, confiance = self.detector.detecter_intention("Quelle heure est-il?")
        self.assertEqual(intention, 'heure')
    
    def test_detecter_blague(self):
        """Test la détection d'une demande de blague"""
        intention, confiance = self.detector.detecter_intention("Raconte-moi une blague")
        self.assertEqual(intention, 'blague')
    
    def test_detecter_entites_nombres(self):
        """Test l'extraction des nombres"""
        entites = self.detector.detecter_entites("5 plus 3")
        self.assertIn('nombres', entites)
        self.assertEqual(len(entites['nombres']), 2)
    
    def test_detecter_entites_mots_cles(self):
        """Test l'extraction des mots-clés"""
        entites = self.detector.detecter_entites("Bonjour comment allez-vous")
        self.assertIn('mots_cles', entites)
        self.assertGreater(len(entites['mots_cles']), 0)


if __name__ == '__main__':
    unittest.main()
