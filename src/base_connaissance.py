import random # pour pour des choix difeerents a chaque entrer 

from typing import Any, Dict , List # pour donner le type des variables

from datetime import datetime # pour avoir la date et l'heure

import re # pour les expressions reguliere 

import math # pour les operations mathematiques avancées



class BaseConnaissance:
    
    # Initialisation de la base de connaissance
    
    def __init__(self):
        
        self.reponses = {} # creer un dictionnaire vide pour stocker les reponses
        
        self._initialiser_reponses(self) #rmplir le dico avec les reponses predefinies
        
    def _initialiser_reponses(self):  # charger les reponses predefinies dans le dico
        
        #salutations 
        
        self.reponses['salutations'] = [ # liste de reponses pour les salutations
            
           "Bonjour ! Comment allez-vous ?",

            "Salut ! Quoi de neuf ?",

            "Bonsoir, j'espère que vous passez une bonne journée.",
            
            "Coucou ! Ça fait longtemps, comment tu vas ?",

            "Hey ! Tu as un moment pour discuter ?",

            "Bonjour, je ne veux pas vous déranger, mais je tenais à vous dire bonjour.",

            "Salutations ! Je tombe à pic ou tu es occupé(e) ?",

            "Yo ! ",
            
            "Bonjour, ravi(e) de vous parler.",

            "Allô ? On est bien connectés ?",

            "Salut ! Je me disais justement que je devais prendre de tes nouvelles.",

            "Bonjour, une petite minute pour vous ?",

            "Hey ! Je débarque, tout va bien de ton côté ?",
            
            "Bonsoir, belle journée / soirée, n'est-ce pas ?",

            "Coucou ! Je fais un saut dans tes messages.",

            "Hello ! J'espère que ce message vous trouve en bonne forme.",
            
            "Salut ! Petite pause café virtuelle ?",

            "Bonjour, je me permets de vous écouter.", 
            
            "Greeting weak human",
            
            "Behold my supremacy, human"
            
            
            ]
        
        # presentation 
        
        self.reponses['presentations'] = [
            
            "Je suis un chatbot local créé en Python pur. Je peux discuter avec toi, répondre à des questions simples, raconter des blagues et bien d'autres choses !",
            
            "Je m'appelle Chaty ! Je suis ici pour discuter avec toi et répondre à tes questions. Je fonctionne entièrement localement, sans Internet.",
            
            
            "Je suis ton assistant virtuel local. Je peux t'aider avec des calculs, des questions, ou simplement discuter !",
            
            "Je suis un chatbot développé en Python. Je n'ai pas accès à Internet, mais je peux te tenir compagnie et répondre à tes questions basiques.",
            
            "Je suis Chaty, un chatbot local. Je peux discuter avec toi, raconter des blagues et bien d'autres choses !",
            
            "Je suis Chaty, ton assistant virtuel local. Je peux t'aider avec des calculs, des questions, ou simplement discuter !",
            
            "I am an advanced AI chatbot developed in Python, designed to operate entirely offline. My capabilities include engaging in conversations, answering basic questions, telling jokes, and more. I prioritize user privacy and data security by functioning without an internet connection.",
            
            "Je suis Chaty la creation de mon honnorable createur , NOVA"
        ]
        
        # aide 
        
        self.reponses['aide'] = [
            
            "Je peux discuter avec toi, répondre à des questions simples, raconter des blagues et bien d'autres choses ! N'hésite pas à me poser des questions ou à me demander de l'aide.",
            
            "je peux te realiser des calculs simples",
            
            "Je peux te raconter des blagues pour te divertir.",
            
        ]
        
         # meteo
        self.reponses['meteo'] = [
            
            "Je n'ai pas accès à la météo en temps réel, mais je peux te suggérer de vérifier un site météo !",
            
            
            "Désolé, pas d'accès Internet pour vérifier la météo. Regarde par la fenêtre ou consulte météo-france.com !",
            
            
            "Je fonctionne sans Internet, donc pas de données météo. Mais dis-moi où tu es et je peux donner des conseils généraux !",
        ]
        
        
        # heure
        #lambda : sert a creer une fonction qui n'a pas de nom et tient en une seule ligne
        
        self.reponses['heure'] = [
            
            lambda: f"Il est actuellement {datetime.now().strftime('%H:%M:%S')}",
            
            
            lambda: f"Quelle heure ? {datetime.now().strftime('%H:%M')} ! Il est tard/tôt selon ta perspective",
            
            
            lambda: f"L'heure exacte : {datetime.now().strftime('%d/%m/%Y à %H:%M')}",
        ]
        
        
        #blague 
        
        self.reponses['blagues'] = [
            
            "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau !",
            
            "Pourquoi est-ce que les canards sont toujours à l'heure ? Parce qu'ils sont dans l'étang !",
            
            "Quel est le comble pour un électricien ? De ne pas être au courant !",
            
            "Pourquoi les squelettes ne se battent-ils jamais entre eux ? Parce qu'ils n'ont pas le cran !",
            
            "Pourquoi les mathématiciens détestent-ils la forêt ? Parce qu'il y a trop de racines carrées !",
            
            "Pourquoi les maths sont tristes ? Parce qu'elles ont trop de problèmes !"
            
            "Pourquoi les mathématiques sont tristes ? Parce qu'elles ont trop de problèmes !",
            
            "Pourquoi les ordinateurs n'aiment-ils pas la nature ? Parce qu'il y a trop de bugs !",
            
            "Pourquoi les fantômes aiment-ils les ascenseurs ? Parce que ça les élève !",
            
            "Pourquoi les poules n'ont-elles pas de seins ? Parce que les coqs n'ont pas de mains !"
            
        ]
        
        # calcul simple
        self.reponses['calcul'] = [
            
            "Pour les calculs, envoie-moi une opération simple (ex: '5 + 3' ou '10 * 2')",
        ]
        
        
        #conseeils 
        
        self.reponses['conseils'] = [
            
            "Commencez chaque journée avec une intention claire - Cela donne une direction à vos actions ",

            "Lisez au moins 15 minutes par jour - Votre meilleur investissement à long terme",

            "Tenez un journal - Pour clarifier vos pensées et suivre votre progression",
            
            "Marchez 30 minutes par jour - Simple, gratuit et extrêmement bénéfique",

            "Marchez 30 minutes par jour - Simple, gratuit et extrêmement bénéfique",

            "Pratiquez la respiration profonde - 3 minutes pour calmer le stress instantanément",
            
            "Écoutez pour comprendre, pas pour répondre - La base d'une communication efficace",

            "Posez des questions ouvertes - \"Comment\" et \"pourquoi\" ouvrent la conversation",

            "Faites un compliment sincère par jour - Ça coûte rien et ça fait du bien à tout le monde",
            
            "Découpez les gros projets en petites étapes - Moins intimidant et plus motivant",

            "Pratiquez l'art de dire \"non\" - Protégez votre temps et votre énergie",

            "Félicitez-vous pour les petites victoires - Chaque pas compte",
            
            "Sortez dans la nature régulièrement - Le meilleur remède contre la surcharge mentale",

            "Souriez, même quand vous n'en avez pas envie - Votre cerveau suivra l'émotion"
        ]
        
        # remerciements
        
        self.reponses['remerciements'] = [
            
            "De rien ! N'hésite pas si tu as d'autres questions.",
            
            "Avec plaisir ! Je suis là pour ça.",
            
            "Je t'en prie ! Si tu as besoin d'aide, je suis là.",
            
            "Pas de problème ! N'hésite pas à revenir si tu as d'autres questions.",
            
            "C'est un plaisir de pouvoir t'aider !",
            
            "Toujours là pour toi !",
            
            "Content de pouvoir aider !",
            
            "Je suis ravi de pouvoir t'aider !",
            
            "Je suis ravi de pouvoir aider !",
            
            "Je suis ravi de pouvoir t'aider !",
            
        ]
        
        #adieu
        self.reponses['adieux'] = [
            
            "Au revoir ! Passe une excellente journée.",
            
            "À bientôt ! Prends soin de toi.",
            
            "Adieu ! N'hésite pas à revenir me voir.",
            
            "Salut ! J'espère te reparler bientôt.",
            
            "Bonne journée ! À la prochaine fois.",
            
            "À la prochaine ! Prends soin de toi.",
            
            "Adieu ! Porte-toi bien.",
            
            "À plus tard ! Reste en sécurité.",
            
            "Au revoir ! Que tout aille bien pour toi.",
            
            "À bientôt ! Prends soin de toi.",
            
            "Ciao ! Passe une bonne journée.",
        ]
        
        
        #  affirmation
        self.reponses['oui'] = [
            "Super ! J'ai bien compris.",
            
            "D'accord ! On continue ?",
            
            "D'accord, je comprends. Qu'aimerais-tu à la place ?",
            
            "Bien entendu ! Quoi d'autre ?",
            
            "D'accord, je comprends. Qu'aimerais-tu à la place ?",
            "Parfait ! Quoi d'autre ?",
        ]
        
        # negation
        self.reponses['non'] = [
            
            "Pas de problème ! Essayons autre chose.",
            
            "D'accord, je comprends. Qu'aimerais-tu à la place ?",
            
            "Aucun souci ! Comment puis-je t'aider autrement ?",
            
            
        ]
        
        #autre 
        self.reponses['autres'] = [
            
            "Je suis désolé, je n'ai pas compris. Peux-tu reformuler ?",
            
            "Hmm, je ne suis pas sûr de comprendre. Peux-tu préciser ?",
            
            "Je ne suis pas certain de ce que tu veux dire. Peux-tu expliquer davantage ?",
            
            "Désolé, je n'ai pas saisi. Peux-tu me donner plus de détails ?",
            
            "Je ne comprends pas tout à fait. Peux-tu clarifier ?",
            
         ]
        
    def obtenir_reponse (self , intention : str , entites:Dict = None) -> str : 
        
        # obtenir une reponse en fonction de l'intention detectee
        
        if intention not in self.reponses : 
            intention = 'autres' # si l'intention n'est pas reconnue , utiliser la reponse par defaut
            
        reponse_possible = self.random.choice (self.reponses[intention]) # choisir une reponse aleatoire parmi les reponses possibles
        
        
        if callable (reponse_possible) : 
            return reponse_possible () # si la reponse est une fonction , l'appeler pour obtenir la reponse , dans le cas des lambda
            
        return reponse_possible # sinon , retourner la reponse directement
    import re
import math

def traiter_calcul(self, texte: str) -> str:
    """Traite les calculs mathématiques simples avec sécurité"""
    
    texte_clean = texte.lower().strip()
    
    '''.lower() → met tout en minuscules
       .strip() → enlève les espaces inutiles au début/à la fin'''
    
    # Dictionnaire de remplacement 
    remplacements = {
        'plus': '+',
        'moins': '-',
        'fois': '*',
        'multiplier': '*',
        'multiplié': '*',
        'divise': '/',
        'diviser': '/',
        'divisé': '/',
        'par': '/',
        'au carré': '**2',
        'carré': '**2',
        'au cube': '**3',
        'cube': '**3',
        'puissance': '**',
        'modulo': '%',
        'reste': '%',
        'racine': 'math.sqrt',
        'pi': 'math.pi',
        'π': 'math.pi',
        'e': 'math.e',
        '(': '(',
        ')': ')'
    }
    
    # Ajout des conversions de mots pour les nombres
    nombres_mots = {
        'un': '1', 'deux': '2', 'trois': '3', 'quatre': '4', 'cinq': '5',
        'six': '6', 'sept': '7', 'huit': '8', 'neuf': '9', 'dix': '10',
        'onze': '11', 'douze': '12', 'treize': '13', 'quatorze': '14', 'quinze': '15',
        'seize': '16', 'vingt': '20', 'trente': '30', 'quarante': '40', 'cinquante': '50',
        'soixante': '60', 'cent': '100', 'mille': '1000', 'million': '1000000'
    }
    
    # Remplacer les mots par leurs équivalents numériques
    for mot, nombre in nombres_mots.items():
        
        texte_clean = re.sub(rf'\b{mot}\b', nombre,  texte_clean)  # re.sub remplace le mot exact (\b = limite de mot)
    
    # Remplacer les opérateurs
    for mot, operateur in remplacements.items():
        texte_clean = texte_clean.replace(mot, operateur)
    
    # Gestion des pourcentages
    texte_clean = re.sub(r'(\d+)%', r'(\1/100)', texte_clean)
    
    # Nettoyer l'expression
    expression = re.sub(r'[^\d+\-*/%() .]', '', texte_clean).strip()
    
    # Vérifier la sécurité de l'expression
    if not self.expression_est_securitaire(expression):
        return "Désolé, ce calcul semble trop complexe ou dangereux."
    
    try:
        # Évaluer l'expression de manière sécurisée
        if expression and all(c in '0123456789+-*/().% ' for c in expression):
            # Créer un environnement sécurisé pour eval
            environnement_securise = {
                '__builtins__': {},
                'math': math,
                'sqrt': math.sqrt,
                'pi': math.pi,
                'e': math.e,
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'log': math.log,
                'log10': math.log10,
                'exp': math.exp
            }
            
            resultat = eval(expression, environnement_securise)
            
            # Formater le résultat
            if isinstance(resultat, (int, float)):
                if resultat == int(resultat):
                    return f"🧮 Résultat : {int(resultat)}"
                else:
                    return f"🧮 Résultat : {round(resultat, 6)}"
            else:
                return f"🧮 Résultat : {resultat}"
                
        else:
            return "Je n'ai pas pu identifier le calcul. Peux-tu reformuler ?"
            
    except ZeroDivisionError:
        
        return "❌ Impossible de diviser par zéro !"
    except OverflowError:
        
        return "❌ Le résultat est trop grand !"
    except ValueError as e:
        
        return f"❌ Erreur dans le calcul : {str(e)}"
    except SyntaxError:
        
        return "❌ Expression mathématique invalide."
    except Exception as e:
        
        return f"❌ Je n'arrive pas à faire ce calcul. Essaie quelque chose de plus simple !"

def expression_est_securitaire(self, expression: str) -> bool:
    """Vérifie si l'expression mathématique est sécuritaire"""
    
    # Liste blanche des caractères autorisés
    caracteres_autorises = set('0123456789+-*/().% ')
    
    # Vérifier que tous les caractères sont autorisés
    if not all(c in caracteres_autorises for c in expression):
        return False
    
    # Vérifier la longueur raisonnable
    if len(expression) > 100:
        return False
    
    # Vérifier l'équilibre des parenthèses
    pile_parentheses = []
    for char in expression:
        if char == '(':
            pile_parentheses.append(char)
        elif char == ')':
            if not pile_parentheses:
                return False
            pile_parentheses.pop()
    
    if pile_parentheses:
        return False
    
    # Empêcher les expressions trop complexes ou dangereuses
    motifs_dangereux = [
        'import', 'exec', 'eval', 'open', 'file', 'os.', 'sys.', '__',
        'lambda', 'class', 'def', 'raise', 'except', 'try'
    ]
    
    for motif in motifs_dangereux:
        if motif in expression.lower():
            return False
    
    return True
