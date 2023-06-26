






from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class GenerateSQLQueryAction(Action):
  
    def name(self) -> Text:
        return "generate_sql_query_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       # print("tracker.latest_message")
        #t=next(tracker.get_latest_entity_values("table"), None)
       # print(t)
        dispatcher.utter_message(Text='done')
        entity_value = tracker.get_slot("table")
        #print('entity')
        dispatcher.utter_message(entity_value)
        intent = tracker.latest_message.get("intent").get("name")
        dispatcher.utter_message(intent)
        table = tracker.get_slot("table")
        #print(tracker.latest_message)
        if intent == "provide_table":
             sql_query = f"SELECT * FROM {table} ORDER BY sales DESC LIMIT 10"
             dispatcher.utter_message(template="utter_display_results", query=sql_query)
        else:
             sql_query = "default"

        return []
