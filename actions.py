






#from typing import Any, Text, Dict, List
#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher

#class GenerateSQLQueryAction(Action):
  
 #   def name(self) -> Text:
  #      return "generate_sql_query_action"

   # def run(self, dispatcher: CollectingDispatcher,
    #        tracker: Tracker,
     #       domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #print("tracker.latest_message")
        #t=next(tracker.get_latest_entity_values("table"), None)
        #print(t)
      #  dispatcher.utter_message(Text='done')
       # entity_value = tracker.get_slot("table")
        #print('entity')
        #dispatcher.utter_message(entity_value)
        #intent = tracker.latest_message.get("intent").get("name")
        #dispatcher.utter_message(intent)
        #table = tracker.get_slot("table")
        #print(tracker.latest_message)
        #if intent == "provide_table":
         #    sql_query = f"SELECT * FROM {table}"
          #   dispatcher.utter_message(template="utter_display_results", query=sql_query)
        #else:
         #    sql_query = "default"

       # return []



      #  class GenerateWHEREQueryAction(Action):
  
    #def name(self) -> Text:
       # return "generate_where_query_action"

    #def run(self, dispatcher: CollectingDispatcher,
           # tracker: Tracker,
            #domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #print("tracker.latest_message")
        #t=next(tracker.get_latest_entity_values("table"), None)
        #print(t)
       # dispatcher.utter_message(Text='done')
        #entity_value = tracker.get_slot("table")
        #print('entity')
        #dispatcher.utter_message(entity_value)
        #intent = tracker.latest_message.get("intent").get("name")
        #dispatcher.utter_message(intent)
        #table = tracker.get_slot("table")
        #operator = tracker.get_slot("operator")
        #value = tracker.get_slot("value")
        #column = tracker.get_slot("column")
        #print(tracker.latest_message)
        #if intent == "provide_table_where":
            # where_query = f"SELECT * FROM {table} WHERE {column} {operator} {value}  ;"
             #dispatcher.utter_message(template="utter_display_where", where=where_query)
        #else:
         #    sql_query = "default"

#        return []






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
        namee = tracker.get_slot("namee")
        if intent == "provide_table_where":
            where_query = f"SELECT * FROM {table} WHERE {column} {operator} {value};"
            dispatcher.utter_message(template="utter_display_where", where=where_query)
        elif intent == "provide_table_name":
            word_query = f"SELECT * FROM {table} WHERE {column} {operator} {namee};"
            dispatcher.utter_message(template="utter_display_word", word=word_query)
        else:
            print( "default")

        return []

          

  
