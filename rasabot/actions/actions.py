# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import json
from pathlib import Path
from typing import Any, Text, Dict, List
from database_connectivity import DataUpdate

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.events import EventType


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

# class ActionPreguntarApellido(Action):
#     def name(self) -> Text:
#         return "action_ask_last_name"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         first_name = tracker.get_slot("first_name")
#         dispatcher.utter_message(text=f"So {first_name}, what is your last name?")
#         return []

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       #dispatcher.utter_message(text="Vale, me acordaré de que tu nombre es {0} y tus apellidos {1}".format(
       #    tracker.get_slot("nombre"), tracker.get_slot("apellidos")))
       DataUpdate(tracker.get_slot('nombre'),tracker.get_slot('apellidos'))
       dispatcher.utter_message("Tus datos han sido guardados. Gracias")
       return []
