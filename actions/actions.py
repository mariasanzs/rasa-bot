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
from database_connectivity import *
import numpy as np

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
        problem_otro = tracker.get_slot('problema') == 'otro'

        if problem_estres:
            dispatcher.utter_message(text="El estrés en el embarazo no es bueno ni para ti ni para tu bebé 👶🏽❤️, busca tiempo para tí misma y desconecta del mundo exterior.")
            dispatcher.utter_message(text="Podemos realizar unas técnicas de relajación para que te sientas mejor 🧘🏻‍♀️.")
        if problem_miedo:
            dispatcher.utter_message(text="los dolores van y vienen, te da tiempo a recuperarte y desaparecen mágicamente en cuanto te ponen a tu hijo en los brazos 🤱🏻💚")
        if problem_incomprension:
            dispatcher.utter_message(text="Hablando tranquilamente se entienden las cosas. Hablar y expresar los sentimientos con los demás es siempre lo mejor. 💞")
        if problem_otro:
            dispatcher.utter_message(text="Vaya...Tal vez no esté preparada para ayudarte 😔, recuerda que siempre puedes hablar con los especialistas 👩🏻‍💼 que seguro que te pueden ayudar con tus problemas  👍🏼")
        return []

class ActionIniciarRelajacion(Action):

    def name(self) -> Text:
        return "action_iniciar_relajacion"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        diaphragmatic_breathing = tracker.get_slot('tecnica') == 'diafragmatica'
        guided_imagery = tracker.get_slot('tecnica') == 'imaginacion'
        feedback = tracker.get_slot('feedback')

        if diaphragmatic_breathing:
            dispatcher.utter_message(text=" 1️⃣ Afloja cualquier ropa que te apriete 👗👕👖")
            dispatcher.utter_message(text=" 2️⃣ Coloca los pies ligeramente separados. 👣 ")
            dispatcher.utter_message(text=" 3️⃣ Apoya una mano sobre el abdomen y la otra sobre el pecho. 🤰🏻")
            dispatcher.utter_message(text=" 4️⃣ Toma aire por la nariz 👃🏼 y expúlsalo por la boca 👄, si tienes algún tipo de problema nasal, puedes tomar el aire por la boca")
            dispatcher.utter_message(response="utter_feedback")
        if guided_imagery:
            dispatcher.utter_message(text="Ponte lo más comoda posible 😌")
            dispatcher.utter_message(text="Sientate a gusto 😊")
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
            dispatcher.utter_message(text="Vale, no pasa nada. Podemos volver a hacerlo cuando quieras 🤗 ")
            return [ConversationPaused()]
        else:
            if diaphragmatic_breathing:
                dispatcher.utter_message(text="Concentrate en tu respiración durante unos minutos... ⌛ Intentando hacerlo de una forma 〰️lenta y suave〰️ ")
                dispatcher.utter_message(text="Mantente así durante unos minutos ⏱️")
            if guided_imagery:
                dispatcher.utter_message(text="Acomódate en tu asiento 😌🪑")
                dispatcher.utter_message(text="Cierra los ojos lentamente 😌 y mantente así durante un minuto 1️⃣⏱️")
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
        dispatcher.utter_message(text="Expulsa ↘️ suavemente el aire de tus pulmones 🫁")
        dispatcher.utter_message(text="Toma aire profundamente ↗️ durante 3️⃣ segundos")
        dispatcher.utter_message(image="https://i.pinimg.com/originals/fa/d6/4c/fad64cf3204f92631283cb207be31ab0.gif")
        dispatcher.utter_message(text="Expulsa ↘️ ahora el aire lentamente en 3️⃣ segundos")
        dispatcher.utter_message(image="https://i.pinimg.com/originals/fa/d6/4c/fad64cf3204f92631283cb207be31ab0.gif")
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
        dispatcher.utter_message(text="Cuando quieras volver a practicar ¡ técnica u otra, solo tienes que avisarme 😉")
        return [ConversationPaused()]

class ActionGuided(Action):

    def name(self) -> Text:
        return "action_guided"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ve relajándote poco a poco ... 🧘🏻‍♀️")
        dispatcher.utter_message(text="Ve aflojando tus músculos poco a poco, de las piernas 🦵🏼, los brazos 🙆🏻, el cuello...")
        dispatcher.utter_message(text="Estaremos así durante 1️⃣ minuto..")
        return []

class ActionFirstPaused(Action):

    def name(self) -> Text:
        return "action_first_paused"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Concéntrate ahora en tus sensaciones y en tu cuerpo 😌🧘🏻‍♀️")
        dispatcher.utter_message(text="Toma aire ↗️")
        dispatcher.utter_message(text="1️⃣...2️⃣...3️⃣...4️⃣.")
        dispatcher.utter_message(text="Exhala lentamente ↘️")
        dispatcher.utter_message(text="1️⃣...2️⃣...3️⃣...4️⃣.")
        dispatcher.utter_message(text="Libera la tensión conforme sueltas el aire por la boca")
        dispatcher.utter_message(text="Repite este paso varias veces hasta que estés lista 🔁 .")
        dispatcher.utter_message(text="Poco a poco estarás más cómoda y tranquila 😌❤️")
        return []

class ActionSecondPaused(Action):

    def name(self) -> Text:
        return "action_second_paused"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Esta imagen 📷 te puede servir de guía")

        if tracker.get_slot('imagen') == 'playa':
            dispatcher.utter_message(image="https://i.pinimg.com/originals/1d/89/f6/1d89f6161add2a4a674719517448face.gif")
        if tracker.get_slot('imagen') == 'montana':
            dispatcher.utter_message(image="https://i.pinimg.com/originals/66/a8/dd/66a8ddedfc584483ffb117e912548555.gif")
        if tracker.get_slot('imagen') == 'prado':
            dispatcher.utter_message(image="https://i.pinimg.com/originals/5a/2e/bf/5a2ebf61086be5f12657f0c58fdb2701.gif")
        if tracker.get_slot('imagen') == 'lago':
            dispatcher.utter_message(image="https://i.pinimg.com/originals/e4/7f/ce/e47fce52f2c08075e05c8990f8f54e98.gif")


        dispatcher.utter_message(text="Piensa en como es el lugar, fíjate en el cielo ☁️ o en la brisa que corre 🍃, 😊 ¿Puedes notar el aroma del aire? 😊 ")
        dispatcher.utter_message(text="Déjate llevar por todas las sensaciones que te produzcan")

        dispatcher.utter_message(text="Quizá esta playlist te ayude https://open.spotify.com/playlist/37i9dQZF1DXcjpPPxCzYRE?si=b3dd3d8a062b4733")
        return []

class ActionThirdPaused(Action):

    def name(self) -> Text:
        return "action_third_paused"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time.sleep(10)
        dispatcher.utter_message(text="¿Qué palabras se vienen a tu mente cuando piensas en esta escena? 🤔")
        dispatcher.utter_message(text="Deja que se repitan como un eco")
        dispatcher.utter_message(text="Sumérgete poco a poco en esas palabras y deja que se desarrollen 💭")
        dispatcher.utter_message(text="Repitete a ti misma, 〰️'me sumerjo más y más'〰️")
        return []

class Action4Paused(Action):

    def name(self) -> Text:
        return "action_4_paused"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="No te distraigas, vuelve siempre a la imagen 📷 que te relaje 🔁")
        dispatcher.utter_message(text="Sigue concentrándote durante un par de minutos ⌛ y siente como va tu cuerpo se va relajando poco a poco 🧘🏻‍♀️")
        return []

class ActionEndGuided(Action):

    def name(self) -> Text:
        return "action_end_guided"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time.sleep(5)
        dispatcher.utter_message(text="Suavemente, deja de concentrarte en tu escena 🙂")
        dispatcher.utter_message(text="Haz una inspiración profunda")
        dispatcher.utter_message(text="Ve recuperando la compostura con movimientos ligeros 🧎🏻‍♀️")
        dispatcher.utter_message(text="Ya has terminado con tu relajación! 😀")
        return []

class ActionPointsValorate(Action):

    def name(self) -> Text:
        return "action_points_valorate"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        puntuacion1 = int(tracker.get_slot('puntos1'))
        puntuacion2 = int(tracker.get_slot('puntos2'))
        puntuacion3 = int(tracker.get_slot('puntos3'))
        
        dispatcher.utter_message(text="Me has dado una puntuación de ...")
        points = puntuacion1+puntuacion2+puntuacion3
        if points == 0:
            dispatcher.utter_message(text="*️⃣*️⃣*️⃣*️⃣*️⃣") 
            dispatcher.utter_message(text="Jo, intentaremos mejorar, gracias")
        elif points <= 6:
            dispatcher.utter_message(text="⭐*️⃣*️⃣*️⃣*️⃣")
            dispatcher.utter_message(text="Algo es algo ... seguiremos mejorando")
        elif points <=12:
            dispatcher.utter_message(text="⭐⭐*️⃣*️⃣*️⃣")
            dispatcher.utter_message(text="bueno, muchas gracias por tu valoración")
        elif points <=18:
            dispatcher.utter_message(text="⭐⭐⭐*️⃣*️⃣")
            dispatcher.utter_message(text="No está mal, muchas gracias.")
        elif points <=24:
            dispatcher.utter_message(text="⭐⭐⭐⭐*️⃣")
            dispatcher.utter_message(text="Genial!, muchisimas gracias")
        else:
            dispatcher.utter_message(text="⭐⭐⭐⭐⭐")
            dispatcher.utter_message(text="Guau!, muchisimas gracias, me alegro de que te haya gustado tanto")
        return []

class ActionAskQuestion(Action):

    def name(self) -> Text:
        return "action_ask_question"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        npregunta = int(tracker.get_slot('n_pregunta'))
        dispatcher.utter_message(text="Pregunta {0}".format(npregunta))
        pregunta = np.array(DataSelectPregunta(npregunta))
        punto = int(pregunta[0][3])
        button_resp=[
                {
                    "title": "{0}".format(pregunta[0][2]),
                    "payload": "/contar_puntos{'puntos_quiz': '{0}'}".format(punto)
                },
                {
                    "title": "{0}".format(pregunta[0][4]),
                    "payload": '/contar_puntos{"puntos_quiz": "{0}".format(pregunta[0][5]) }'
                },
                {
                    "title": "{0}".format(pregunta[0][6]),
                    "payload": '/contar_puntos{"puntos_quiz": "{0}".format(pregunta[0][7]) }'
                }
            ]

        dispatcher.utter_message(text="{0}".format(pregunta[0][1]), buttons=button_resp)
        dispatcher.utter_message(response="utter_siguiente_pregunta")
        npregunta = npregunta + 1
        #notas como se va yendo la tensión? LLevas x veces ¿Repetir?
        return [SlotSet("n_pregunta", npregunta)]

class ActionPasarPregunta(Action):

    def name(self) -> Text:
        return "action_pasar_pregunta"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        feedback = tracker.get_slot('feedback')
        puntos = int(tracker.get_slot('puntos_quiz'))
        puntos_totales = puntos + int(tracker.get_slot('total_quiz'))
        dispatcher.utter_message(text="puntos totales: {0}".format(puntos_totales))
        
        if feedback=='siguiente':
            accion =  "action_ask_question"
        if feedback=='parar':
            accion =  "action_end_quiz"
        return [SlotSet("total_quiz", puntos_totales), FollowupAction(accion)]

class ActionEndQuiz(Action):

    def name(self) -> Text:
        return "action_end_quiz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Fin del quiz")
        ##poner slot a 0
        return [ConversationPaused()]

class ActionPreguntarApellido(Action):
     def name(self) -> Text:
         return "action_ask_last_name"
     def run(
         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
     ) -> List[EventType]:
         first_name = tracker.get_slot("first_name")
         dispatcher.utter_message(text=f"So {first_name}, what is your last name?")
         return []


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      #dispatcher.utter_message(text="Vale, me acordaré de que tu nombre es {0} y tus apellidos {1}".format(
      #    tracker.get_slot("nombre"), tracker.get_slot("apellidos")))
       DataUpdate(tracker.get_slot('nombre'))
       nombre = tracker.get_slot('nombre')
       dispatcher.utter_message("Tus datos han sido guardados. Gracias")
       return []

class ActionSubmitValoracion(Action):
    def name(self) -> Text:
        return "action_submit_valoracion"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       puntuacion1 = tracker.get_slot('puntos1')
       puntuacion2 = tracker.get_slot('puntos2')
       puntuacion3 = tracker.get_slot('puntos3')
       sugerencias = tracker.get_slot('cambios')

       DataValoracion(puntuacion1,puntuacion2,puntuacion3,sugerencias) 
       dispatcher.utter_message("Genial! tendremos en cuenta tu opinión")
       return []
"""
class ValorateForm(FormAction):
    def name(self) -> Text:
        return "valorate_form"
    
    @staticmethod
    def required_slots(tracker):

        if tracker.get_slot('puntos1') == True:
            return ["puntos1", "puntos2", "puntos3","cambios"]
        else:
            return ["confirm_exercise", "sleep",
             "diet", "stress", "goal"]

"""