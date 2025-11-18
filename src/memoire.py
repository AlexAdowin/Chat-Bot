# src/memoire.py
from collections import Counter
from typing import List, Dict



class ConversationMemory:
    """Mémoire pour stocker tous les messages de la conversation"""

    def __init__(self):
        self.messages = []  # liste de dicts : {role, texte, intention, emotion}

    def ajouter_message(self, role: str, texte: str, intention: str = None, emotion: str = None):
        self.messages.append({
            'role': role,
            'texte': texte,
            'intention': intention,
            'emotion': emotion
        })

    def dernier_message(self, role: str = None):
        """Retourne le dernier message du role spécifié, ou de tous si role=None"""
        for msg in reversed(self.messages):
            if role is None or msg['role'] == role:
                return msg
        return None

    def obtenir_stats(self):
        """Retourne des statistiques simples pour debug"""
        total = len(self.messages)
        intentions = {}
        for msg in self.messages:
            if msg['intention']:
                intentions[msg['intention']] = intentions.get(msg['intention'], 0) + 1
        return {
            'total_messages': total,
            'intentions': intentions
        }