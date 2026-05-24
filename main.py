import solder,duty_manager


def show_menu() -> None:

    print("To add_solder enter 1")
    print("To remuve solder enter 2")
    print("To view solder enter 3")
    print("To add buty enter 4")
    print("To update_duty_status enter 5")
    print("To view_soldier_duties enter 6")
    print("To exit enter 7")
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
    print(solder.get_all_soldiers())


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    stoper = True
    while stoper:
        try :
            id_solder = int(input("please enter the id solder "))
        except ValueError :
            print("the id solder it is a variable of type int ")
        else:
            stoper = False
    the_duty = input("Enter the name of duty : ")        
    day = input("Enter the day of the dowries : ").lower()
    duty_manager.add_duty_to_soldier(id_solder,the_duty,day)
    print("Adding benefits has been successfully updated")


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    stoper = True
    while stoper:
        try :
            id_solder = int(input("please enter the id solder "))
        except ValueError :
            print("the id solder it is a variable of type int ")
        else:
            stoper = False
    the_duty = input("Enter the name of duty : ").lower()
    update_status = input("Please enter the status : ").lower()
    duty_manager.update_duty_status(id_solder,the_duty,update_status)
    print("The status has been successfully updated")


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    stoper = True
    while stoper:
        try :
            id_solder = int(input("please enter the id solder "))
        except ValueError :
            print("the id solder it is a variable of type int ")
        else:
            stoper = False
    print(duty_manager.get_soldier_duties(id_solder) )       
    

def main():
     exit = True
     while exit:
            show_menu()
            choice = get_user_choice() 
            match choice:
                case "1" :
                    handle_add_soldier()
                    exit = False
                case "2" :
                    handle_remove_soldier()
                    exit = False
                case "3" :
                    handle_view_soldiers()
                    exit = False
                case "4" :
                    handle_add_duty()
                    exit = False
                case "5" :
                    handle_update_duty_status()
                    exit = False
                case "6" :
                    handle_view_soldier_duties()
                case "7":
                        exit = False
                
                 
main()                 
             
        
