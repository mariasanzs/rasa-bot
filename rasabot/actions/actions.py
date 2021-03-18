# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import json
from pathlib import Path
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class ActionDarConsejo(Action):

    def name(self) -> Text:
        return "action_dar_consejo"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        problem_estres = tracker.get_slot('problema') == 'estres'
        problem_miedo = tracker.get_slot('problema') == 'miedo'
        problem_incomprension = tracker.get_slot('problema') == 'incomprension'

        if problem_estres:
            dispatcher.utter_message(text="El estrés en el embarazo no es bueno ni para ti ni para tu bebé, busca tiempo para tí misma y desconecta del mundo exterior ")
        if problem_miedo:
            dispatcher.utter_message(text="los dolores van y vienen, te da tiempo a recuperarte y desaparecen mágicamente en cuanto te ponen a tu hijo en los brazos")
        if problem_incomprension:
            dispatcher.utter_message(text="Hablando tranquilamente se entienden las cosas. Hablar y expresar los sentimientos con los demás es siempre lo mejor.")
        return []

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
