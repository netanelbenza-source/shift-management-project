import data_json,solder,duty_manager,utils




def show_menu() -> None:

    print("to add_solder enter 1")
    print("to remuve solder enter 2")
    print("to view solder enter 3")
    print("to add buty enter 4")
    print("to update_duty_status enter 5")
    print("to view_soldier_duties enter 6")
    print("to exit enter 7")
    print("please enret your choice ")



def get_user_choice() -> str:
    while True:
        his_choice = input()
        if "1" <= his_choice <= "7":
            return his_choice
        print("Please enter a number from the menu")
   

def handle_add_soldier() -> None:
    stoper = True
    while stoper:
        try :
            id_solder = int(input("please enter the id solder "))
        except ValueError :
            print("the id solder it is a variable of type int ")
        else:
            stoper = False
    name_of_solder = input("please enter the name of solder ")
    solder.add_soldier(id_solder,name_of_solder) 
    print("The soldier was added successfully\n")       
    


def handle_remove_soldier() -> None:
    stoper = True
    while stoper:
        try :
            id_solder = int(input("please enter the id solder "))
        except ValueError :
            print("the id solder it is a variable of type int ")
        else:
            stoper = False
    solder.remove_soldier(id_solder)        
    print("The soldier was remove successfully\n") 


def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    pass


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass







def main():
     exit = True
     while exit:
            show_menu()
            choice = get_user_choice() 
            match choice:
                case "1" :
                    handle_add_soldier()
                case "2" :
                    handle_remove_soldier()
                case "3" :
                    handle_view_soldiers()
                case "4" :
                    handle_add_duty()
                case "5" :
                    handle_update_duty_status()
                case "6" :
                    handle_view_soldier_duties()
                case "7":
                        exit = False
                
                 
main()                 
             
        
