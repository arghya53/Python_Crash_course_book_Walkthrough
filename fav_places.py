from survey import AnonymousSurvey

question = "What's your most favorite place to visit first?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Please enter 'q' at anytime to quit")

while True:

   # Get survey results
    new_response = input("Enter your response: ") # the program will ask for responses continuously, so we need to use while loop ana an input statement within it 
    if new_response == 'q':
        break
    # Store survey results
    my_survey.store_responses(new_response)    

# Show survey results

print("Thank you for your response.\n")
my_survey.show_response()
question