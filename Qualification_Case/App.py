import os
import pickle
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize, sent_tokenize

# getchar() -> a = input('').split(" ")[0]

def write_file(review: str, review_category: str):
    file = open("reviews.txt", "a")
    file.write(review_category + "#" + " ".join(review) + "\n")
    file.close()

def get_recommendations(doc_index, cosine_sim, documents, top_n=3):
    similarity_scores = list(enumerate(cosine_sim[doc_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommendations = similarity_scores[1:top_n+1]
    return [(documents[i], score) for i, score in recommendations]

def add_review():
    select = 0
    review = ""
    review_category = ""
    while True:
        os.system("cls")
        print("ADD REVIEW")
        print("1. ADD REVIEW")
        print("2. BACK")
        select = int(input(">> "))
        if select == 1:
            review = input("ENTER REVIEW: ")
            review = review.lower()
            review = word_tokenize(review)
            try:
                file = open("classifier.pickle", "rb")
                classifier = pickle.load(file)
                review_category = classifier.classify(FreqDist(review))
                print("REVIEW CATEGORY: " + review_category)
                file.close()
            except FileNotFoundError:
                print("ERROR: CLASSIFIER NOT FOUND.")
                print("PLEASE TRAIN THE CLASSIFIER FIRST.")
                a = input('').split(" ")[0]
            except Exception as e:
                print("ERROR: " + e)
                a = input('').split(" ")[0]
                return
            write_file(review, review_category)
            print("REVIEW ADDED SUCCESSFULLY.")
            a = input('').split(" ")[0]
        elif select == 2:
            break
        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")
            a = input('').split(" ")[0]
            continue

def view_electronic_recommendation():
    import pickle
    # Load the recommendation data from the pickle file
    try:
        with open('recommendation_data.pickle', 'rb') as file:
            tfidf_df, cosine_sim = pickle.load(file)
        print("Data loaded successfully.")
        print(tfidf_df.head())
        print(cosine_sim)
    except Exception as e:
        print(f"Error loading pickle file: {e}")
    
    print("Press any key to continue...")
    a = input('').split(" ")[0]

    # Get the recommendations for the first document
    os.system("cls")
    file = open("positive.txt", "r").read()
    documents = sent_tokenize(file)
    recommendations = get_recommendations(0, cosine_sim, documents)
    print("\nTop 3 recommendations for most buyed product:")
    for doc, score in recommendations:
        print(f"Document: {doc} (Score: {score})")
    print("Press any key to continue...")
    a = input('').split(" ")[0]

def main_menu():
    select = 0
    while True:
        review = open("reviews.txt", "r").read()
        review = sent_tokenize(review)
        review_category = ""
        review_text = ""
        if len(review) > 0:
            review_text = review[-1].split("#")[1]
            review_category = review[-1].split("#")[0]
        else:
            review = ""
        os.system("cls")
        print("ELECTRONIC REVIEW SYSTEM")
        print(f"YOUR REVIEW: {review_text}")
        print(f"YOUR REVIEW CATEGORY (POSITIVE/NEGATIVE): {review_category}")
        print("1. ADD REVIEW")
        print("2. VIEW ELECTRONIC RECOMMENDATION")
        print("3. VIEW NAMED ENTITY RECOGNITION")
        print("4. EXIT")
        select = int(input(">> "))
        if select == 1:
            add_review()
        elif select == 2:
            print("VIEW MOVIE RECOMMENDATION")
            view_electronic_recommendation()
        elif select == 3:
            print("VIEW NAMED ENTITY RECOGNITION")
            # view_named_entity_recognition()
        elif select == 4:
            break
        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")
            continue

if __name__ == "__main__":
    main_menu()