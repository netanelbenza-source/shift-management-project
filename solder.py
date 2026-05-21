import data_json
import json
import utils


def add_soldier(soldier_id: int, name: str) -> None:
        is_find = utils.find_soldier_by_id
        if not is_find:
            raise ValueError ("The soldier is already registered")
        is_good_name = utils.is_valid_name(name)
        if not is_good_name:
              raise ValueError ("The value name is ereor")
        with open(r"C:\X\e\hanged_man\project1\__pycache__\data.json","w",encoding="utf-8") as file :
            data_json.the_data_of_solder.append({"id": soldier_id , "name":name})
            json.dump(data_json.the_data_of_solder,file ,indent=4, ensure_ascii=False)
   
   
     


def remove_soldier(soldier_id: int) -> None:
    """
    מסירה חייל מהמערכת לפי id.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
    
    מחזירה:
        None - הפונקציה מסירה את החייל או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של הסרת חייל.
    מבצעת בדיקת קיום ומסירה מהנתונים.
    זורקת exception במקרה שהחייל לא קיים.
    """
    is_find_the_soldier = utils.find_soldier_by_id(soldier_id)
    if is_find_the_soldier == None:
         raise KeyError("The soldier's id was not found")
    for i,dict in enumerate( data_json.the_data_of_solder):
         if dict.get("id") == soldier_id:
              data_json.the_data_of_solder.pop(i)
    with open(r"C:\X\e\hanged_man\project1\__pycache__\data.json","w",encoding="utf-8") as file :
            json.dump(data_json.the_data_of_solder,file ,indent=4, ensure_ascii=False)
             
              
              



def get_all_soldiers() -> list:

    with open(r"C:\X\e\hanged_man\project1\__pycache__\data.json","r" ,encoding="utf-8") as file:
        return json.load(file)
    """
    מחזירה את רשימת כל החיילים במערכת.
    
    סוג: גישה לנתונים (Data Access)
    
    מקבלת: כלום
    
    מחזירה:
        list: רשימה של מילונים, כל מילון מייצג חייל
              רשימה ריקה אם אין חיילים
    
    זורקת: כלום - תמיד מחזירה רשימה (ריקה או מלאה)
    
    למה הפונקציה קיימת:
    גישה לנתונים בצורה מבוקרת.
    מאפשר לקבל את הנתונים מבלי לגשת ישירות למשתנה הגלובלי.
    """
    pass

