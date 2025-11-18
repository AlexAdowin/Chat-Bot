import unittest  # Importe le module pour créer des tests unitaires
import sys       # Importe le module pour interagir avec le système Python
import os        # Importe le module pour interagir avec le système d'exploitation

# Configure le chemin d'accès pour trouver les modules du projet
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importe la classe à tester depuis le module base_connaissance
from src.base_connaissance import BaseConnaissance


class TestBaseConnaissance(unittest.TestCase):
    """Classe de tests pour vérifier le bon fonctionnement de BaseConnaissance"""
    
    def setUp(self):
        """Méthode exécutée avant chaque test - initialise l'objet à tester"""
        self.base = BaseConnaissance()  # Crée une instance de BaseConnaissance pour les tests
    
    def test_obtenir_reponse_salutation(self):
        """Teste si la base peut donner une réponse pour une salutation"""
        reponse = self.base.obtenir_reponse('salutations')  # Demande une réponse pour salutations
        
        self.assertIsNotNone(reponse)     # Vérifie que la réponse n'est pas vide
        
        self.assertIsInstance(reponse, str)  # Vérifie que c'est bien une chaîne de caractères
        
        self.assertGreater(len(reponse), 0)  # Vérifie que la réponse a au moins 1 caractère
    
    def test_obtenir_reponse_presentation(self):
        
        """Teste si la réponse de présentation contient les mots-clés attendus"""
        
        reponse = self.base.obtenir_reponse('presentations')  # Demande une réponse pour présentation
        
        # Vérifie que la réponse contient 'chatbot' ou 'chaty' (en minuscules)
        self.assertTrue('chatbot' in reponse.lower() or 'chaty' in reponse.lower())

    
    def test_obtenir_reponse_blague(self):
        """Teste si la base peut retourner une blague"""
        reponse = self.base.obtenir_reponse('blagues')  # Demande une blague
        
        self.assertIsNotNone(reponse)     # Vérifie que la réponse existe
        
        self.assertIsInstance(reponse, str)  # Vérifie que c'est bien du texte
    
    def test_obtenir_reponse_intention_inconnue(self):
        """Teste le comportement avec une intention qui n'existe pas"""
        reponse = self.base.obtenir_reponse('intention_inexistante')  # Demande une intention inconnue
        
        self.assertIsNotNone(reponse)  # Vérifie qu'on a quand même une réponse (pas d'erreur)
    
    def test_traiter_calcul_addition(self):
        """Teste le calcul d'une addition simple"""
        reponse = self.base.traiter_calcul("5 + 3")  # Demande de calculer 5+3
        
        self.assertIn("8", reponse)  # Vérifie que le résultat "8" est dans la réponse
    
    def test_traiter_calcul_multiplication(self):
        
        """Teste le calcul d'une multiplication simple"""
        reponse = self.base.traiter_calcul("5 * 3")  # Demande de calculer 5×3
        
        self.assertIn("15", reponse)  # Vérifie que le résultat "15" est dans la réponse
    
    def test_traiter_calcul_avec_mots(self):
        """Teste le calcul avec des mots au lieu de symboles mathématiques"""
        
        reponse = self.base.traiter_calcul("5 plus 3")  # Demande de calculer "5 plus 3"
        
        self.assertIn("8", reponse)  # Vérifie que le résultat "8" est dans la réponse
    
    def test_traiter_calcul_invalide(self):
        """Teste le comportement avec un calcul invalide"""
        
        reponse = self.base.traiter_calcul("abc def ghi")  # Demande un calcul impossible
        
        # Vérifie qu'un message d'erreur approprié est retourné
        self.assertIn("Expression mathématique invalide", reponse)


# Point d'entrée pour exécuter les tests
if __name__ == '__main__':
    unittest.main()  # Lance tous les tests de la classe