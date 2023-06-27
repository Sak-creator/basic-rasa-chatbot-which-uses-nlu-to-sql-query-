from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class GenerateSQLQueryAction(Action):
    def name(self) -> Text:
        return "generate_sql_query_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entity_value = tracker.get_slot("table")
        intent = tracker.latest_message.get("intent").get("name")
        table = tracker.get_slot("table")

        if intent == "provide_table":
            sql_query = f"SELECT * FROM {table}"
            dispatcher.utter_message(template="utter_display_results", query=sql_query)
        else:
            sql_query = "default"

        return []
        

class GenerateWHEREQueryAction(Action):
    def name(self) -> Text:
        return "generate_where_query_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message.get("intent").get("name")
        table = tracker.get_slot("table")
        operator = tracker.get_slot("operator")
        value = tracker.get_slot("value")
        column = tracker.get_slot("column")

        if intent == "provide_table_where":
            where_query = f"SELECT * FROM {table} WHERE {column} {operator} {value};"
            dispatcher.utter_message(template="utter_display_where", where=where_query)
        else:
            sql_query = "default"

        return []








  
