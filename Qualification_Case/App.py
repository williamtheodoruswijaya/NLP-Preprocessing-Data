import os

# getchar() -> a = input('').split(" ")[0]

def write_file(review: str, review_category: str):
    if review_category == "pos":
        file = open("positive.txt", "a")
        file.write(review + "\n")
        file.close()
    elif review_category == "neg":
        file = open("negative.txt", "a")
        file.write(review + "\n")
        file.close()

def add_review():
    select = 0
    review = ""
    review_category = ""
    while True:
        os.system("cls")
        print("ADD REVIEW")
        print("1. ADD POSITIVE REVIEW")
        print("2. ADD NEGATIVE REVIEW")
        print("3. BACK")
        select = int(input(">> "))
        if select == 1:
            review = input("ENTER REVIEW: ")
            review_category = "pos"
            write_file(review, review_category)
            print("REVIEW ADDED SUCCESSFULLY.")
            a = input('').split(" ")[0]
        elif select == 2:
            review = input("ENTER REVIEW: ")
            review_category = "neg"
            write_file(review, review_category)
            print("REVIEW ADDED SUCCESSFULLY.")
            a = input('').split(" ")[0]
        elif select == 3:
            break
        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")
            a = input('').split(" ")[0]
            continue

def main_menu():
    select = 0
    while True:
        os.system("cls")
        print("ELECTRONIC REVIEW SYSTEM")
        print("YOUR REVIEW: ")
        print("YOUR REVIEW CATEGORY (POSITIVE/NEGATIVE): ")
        print("1. ADD REVIEW")
        print("2. VIEW MOVIE RECOMMENDATION")
        print("3. VIEW NAMED ENTITY RECOGNITION")
        print("4. EXIT")
        select = int(input(">> "))
        if select == 1:
            add_review()
        elif select == 2:
            print("VIEW MOVIE RECOMMENDATION")
            # view_movie_recommendation()
        elif select == 3:
            print("VIEW NAMED ENTITY RECOGNITION")
            # view_named_entity_recognition()
        elif select == 4:
            break
        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")
            continue

main_menu()