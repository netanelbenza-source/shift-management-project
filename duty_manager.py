import solder , data_json , utils,json




def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    """
    מוסיפה תורנות חדשה לחייל.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        day (str): יום בשבוע (sunday/monday/tuesday/wednesday/thursday)
    
    מחזירה:
        None - הפונקציה מוסיפה את התורנות או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        ValueError: אם תורנות עם שם זה כבר קיימת לחייל
        ValueError: אם day לא חוקי (friday/saturday או ערך לא תקין)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של הוספת תורנות.
    מבצעת בדיקות ומוסיפה תורנות לחייל.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    is_find_soldeir = utils.find_soldier_by_id(soldier_id)
    if not is_find_soldeir:
        raise KeyError("The soldier's id was not found")
    
    has_a_duty = utils.soldier_has_duty(is_find_soldeir,duty_name)
    if has_a_duty:
         raise ValueError("The soldier is already on duty")
    
    is_valid_day = utils.is_valid_day(day)   
    if not is_valid_day:
         raise ValueError("There are no shifts these days")
    
    new_dict = {"name" : duty_name , "day" : day, "status" : "pending"}
    is_find_soldeir["duties"].append(new_dict)
    with open(r"C:\X\e\hanged_man\project1\__pycache__\data.json","w",encoding = "utf-8") as file :
        json.dump(data_json.the_data_of_solder,file,indent = 4, ensure_ascii = False)



def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    """
    מעדכנת את הסטטוס של תורנות.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        new_status (str): סטטוס חדש (pending/completed/missed)
    
    מחזירה:
        None - הפונקציה מעדכנת את הסטטוס או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        KeyError: אם תורנות עם שם זה לא נמצאה לחייל
        ValueError: אם new_status לא חוקי (לא pending/completed/missed)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של עדכון סטטוס.
    מבצעת בדיקות ומעדכנת את הסטטוס.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    # is_find_soldeir = utils.find_duty_by_name(soldier_id)
    # if not is_find_soldeir:
    #     raise KeyError("The soldier's id was not found")
    
    pass


def get_soldier_duties(soldier_id: int) -> list:
    """
    מחזירה את רשימת התורנויות של חייל.
    
    סוג: גישה לנתונים (Data Access)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
    
    מחזירה:
        list: רשימת תורנויות (מילונים)
              רשימה ריקה אם אין תורנויות
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
    
    למה הפונקציה קיימת:
    גישה מבוקרת לתורנויות של חייל.
    מפרידה בין הנתונים לבין הגישה אליהם.
    זורקת exception אם החייל לא קיים (במקום להחזיר רשימה ריקה).
    """
    is_find = utils.find_soldier_by_id(soldier_id)
    if not is_find:
            raise KeyError("The soldier is already registered")
    return is_find.get("duties")

