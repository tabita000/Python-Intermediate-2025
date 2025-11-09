import json

def main():
    #read json file
    with open("API-1.3_JSON/example7_assignment.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    school = data["school"]    
    
    #1. Find the email address of the second student in the first course of the Computer Science Department.(Expected path: school -> departments -> [0] -> courses -> [0] -> students -> [1] -> email)
    
    email_second_student_cs = school["departments"] [0] ["courses"] [0] ["students"] [1] ["email"]
    
    
    #2. Find the room number where the head of the Computer Science department has their office. Expected path: school -> departments -> [0] -> head -> office -> room
    
    room_cs_head = school["departments"] [0] ["head"] ["office"] ["room"]
    
    
    #3. Find the comment text from the first review of the first book in the library. Expected path: school -> library -> books -> [0] -> reviews -> [0] -> comment
    
    first_review_comment = school["library"] ["books"] [0] ["reviews"] [0] ["comment"]
    
    
    #4. Find the price of the second book in the library. Expected path: school -> library -> books -> [1] -> price
    
    second_book_price = school["library"] ["books"] [1] ["price"]
    
    
    #5. Find the name of the building where the second event is taking place. Expected path: school -> events -> [1] -> location -> building
    
    second_event_building = school["events"] [1] ["location"] ["building"]
    
    
    #Output
    print(f"1. Email of the second student in the first Computer Science course: {email_second_student_cs}\n")
    print(f"2. Room number of the Computer Science department head's office: {room_cs_head}\n")
    print(f"3. Comment from the first review of the first book in the library: {first_review_comment}\n")
    print(f"4. Price of the second book in the library: {second_book_price}\n")
    print(f"5. Building name of the second event location: {second_event_building}\n")


if __name__ == "__main__":
    main()
    

