# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import json
import time
from pathlib import Path
from typing import Any, Text, Dict, List
#from database_connectivity import DataUpdate

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.events import EventType, SlotSet, FollowupAction, ConversationPaused


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

class ActionIniciarRelajacion(Action):

    def name(self) -> Text:
        return "action_iniciar_relajacion"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        diaphragmatic_breathing = tracker.get_slot('tecnica') == 'diafragmatica'
        guided_imagery = tracker.get_slot('tecnica') == 'imaginacion'
        feedback = tracker.get_slot('feedback')

        if diaphragmatic_breathing:
            dispatcher.utter_message(text="Afloja cualquier ropa que te apriete")
            dispatcher.utter_message(text="Coloca los pies ligeramente separados. Apoya una mano sobre el abdomen y la otra sobre el pecho. Toma aire por la nariz y expúlsalo por la boca")
            dispatcher.utter_message(text="Si tienes algún tipo de problema nasal, puedes tomar el aire por la boca")
            dispatcher.utter_message(response="utter_feedback")
        if guided_imagery:
            dispatcher.utter_message(text="Ponte lo más comoda posible")
            dispatcher.utter_message(text="Sientate a gusto")
            dispatcher.utter_message(text="Reposa cómodamente tus brazos sobre tu regazo")
        return []

class ActionRelajacion(Action):

    def name(self) -> Text:
        return "action_relajacion"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        diaphragmatic_breathing = tracker.get_slot('tecnica') == 'diafragmatica'
        guided_imagery = tracker.get_slot('tecnica') == 'imaginacion'
        feedback = tracker.get_slot('feedback')

        if feedback == 'no':
            dispatcher.utter_message(text="Bueeeeno no pasa na")
        else:
            if diaphragmatic_breathing:
                dispatcher.utter_message(text="Concentrate en tu respiración durante unos minutos. Intentando hacerlo de una forma lenta y suave")
                dispatcher.utter_message(text="Mantente así durante unos minutos")
                # prueba = tracker.latest_message['text']
                # print(prueba)
                # dispatcher.utter_message(text = prueba)
            if guided_imagery:
                dispatcher.utter_message(text="Acomódate en tu asiento")
                dispatcher.utter_message(text="Cierra los ojos lentamente y mantente así durante un minuto")
        return []

class ActionModo(Action):

    def name(self) -> Text:
        return "action_modo"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        diaphragmatic_breathing = tracker.get_slot('tecnica') == 'diafragmatica'
        guided_imagery = tracker.get_slot('tecnica') == 'imaginacion'

        if diaphragmatic_breathing:
            accion =  "action_diaphragmatic"
        if guided_imagery:
            accion =  "action_guided"
        return [FollowupAction(accion)]

class ActionDiafragmatic(Action):

    def name(self) -> Text:
        return "action_diaphragmatic"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        repeticion = tracker.get_slot('repeticiones')
        dispatcher.utter_message(text="Expulsa suavemente el aire de tus pulmones")
        dispatcher.utter_message(text="Toma aire profundamente durante 3 segundos")
        dispatcher.utter_message(text="3")
        dispatcher.utter_message(text="2")
        dispatcher.utter_message(text="1")
        dispatcher.utter_message(text="Expulsa ahora el aire lentamente en otros 3 segundos")
        dispatcher.utter_message(text="3")
        dispatcher.utter_message(text="2")
        dispatcher.utter_message(text="1")
        dispatcher.utter_message(response="utter_repetir")
        repeticion = repeticion + 1
        #notas como se va yendo la tensión? LLevas x veces ¿Repetir?
        return [SlotSet("repeticiones", repeticion)]

class ActionRepeticion(Action):

    def name(self) -> Text:
        return "action_repeticion"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        feedback = tracker.get_slot('feedback')

        if feedback=='repeticion':
            accion =  "action_diaphragmatic"
        if feedback=='repeticion2':
            accion =  "action_end_diaph"
        return [FollowupAction(accion)]

class ActionEndDiaph(Action):

    def name(self) -> Text:
        return "action_end_diaph"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="❤️Espero que te encuentres mucho mejor❤️")
        dispatcher.utter_message(text="Cuando quieras volver a practicar esta técnica u otra avísame")
        return [ConversationPaused()]

class ActionGuided(Action):

    def name(self) -> Text:
        return "action_guided"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ve relajándote poco")
        dispatcher.utter_message(text="Ve aflojando tus músculos poco a poco, de las piernas, los brazos, el cuello...")
        dispatcher.utter_message(text="Estaremos así durante 1 minuto..")
        return []

class ActionFirstPaused(Action):

    def name(self) -> Text:
        return "action_first_paused"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time.sleep(10)
        dispatcher.utter_message(text="Concéntrate ahora en tus sensaciones y en tu cuerpo")
        dispatcher.utter_message(text="Toma aire")
        dispatcher.utter_message(text="1...2...3...4.")
        dispatcher.utter_message(text="Exhala lentamente")
        dispatcher.utter_message(text="1...2...3...4.")
        dispatcher.utter_message(text="Libera la tensión conforme sueltas el aire por la boca")
        dispatcher.utter_message(text="Repite este paso varias veces.")
        dispatcher.utter_message(text="Poco a poco estarás más cómoda y tranquila")
        return []

class ActionSecondPaused(Action):

    def name(self) -> Text:
        return "action_second_paused"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if tracker.get_slot('imagen') == 'playa':
            dispatcher.utter_message(image="https://i.pinimg.com/originals/1d/89/f6/1d89f6161add2a4a674719517448face.gif")
            dispatcher.utter_message(image="https://i.pinimg.com/564x/7b/e8/cc/7be8cca080f1c3fc9ecd0395795e76b6.jpg")
        if tracker.get_slot('imagen') == 'montana':
            dispatcher.utter_message(image="https://i.pinimg.com/564x/7b/e8/cc/7be8cca080f1c3fc9ecd0395795e76b6.jpg")
        if tracker.get_slot('imagen') == 'prado':
            dispatcher.utter_message(text="https://i.pinimg.com/564x/7b/e8/cc/7be8cca080f1c3fc9ecd0395795e76b6.jpg")
        if tracker.get_slot('imagen') == 'lago':
            dispatcher.utter_message(image="https://i.pinimg.com/564x/7b/e8/cc/7be8cca080f1c3fc9ecd0395795e76b6.jpg")

        dispatcher.utter_message(text="Esta imagen te puede servir de guía")
        dispatcher.utter_message(text="Piensa en como es el sitio, fíjate en el cielo")
        dispatcher.utter_message(text="Imagina la brisa que corre")
        dispatcher.utter_message(text="¿Puedes notar el aroma del aire?")
        dispatcher.utter_message(text="Déjate llevar por todas las sensaciones que te produzcan")

        dispatcher.utter_message(text="QUIZÁ AQUÍ PEGUE UNA PLAYLIST")
        return []

class ActionThirdPaused(Action):

    def name(self) -> Text:
        return "action_third_paused"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time.sleep(5)
        dispatcher.utter_message(text="¿Qué palabras se vienen a tu mente cuando piensas en esta escena?")
        dispatcher.utter_message(text="Deja que se repitan como un eco")
        dispatcher.utter_message(text="Sumérgete poco a poco en esas palabras y deja que se desarrollen")
        dispatcher.utter_message(text="Repitete a ti misma, 'me sumerjo más y más'")
        return []

class Action4Paused(Action):

    def name(self) -> Text:
        return "action_4_paused"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time.sleep(5)
        dispatcher.utter_message(text="No te distraigas, vuelve siempre a la imagen que te relaje")
        dispatcher.utter_message(text="Sigue concentrándote durante un par de minutos y siente como va tu cuerpo se va relajando poco a poco ")
        return []

class ActionEndGuided(Action):

    def name(self) -> Text:
        return "action_end_guided"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time.sleep(5)
        dispatcher.utter_message(text="Suavemente, deja de concentrarte en tu escena")
        dispatcher.utter_message(text="Haz una inspiración profunda")
        dispatcher.utter_message(text="Ve recuperando la compostura con movimientos ligeros")
        dispatcher.utter_message(text="Ya has terminado con tu relajación 😀")
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

#class ActionSubmit(Action):
#    def name(self) -> Text:
#        return "action_submit"

#    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       #dispatcher.utter_message(text="Vale, me acordaré de que tu nombre es {0} y tus apellidos {1}".format(
       #    tracker.get_slot("nombre"), tracker.get_slot("apellidos")))
#       DataUpdate(tracker.get_slot('nombre'),tracker.get_slot('apellidos'))
#       dispatcher.utter_message("Tus datos han sido guardados. Gracias")
#       return []
