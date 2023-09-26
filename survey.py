class AnonymousSurvey:

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """ Show the survey question """
        print(self.question)
    
    def store_responses(self, new_response):
        """Get the responses """

        self.responses.append(new_response)
    
    def show_response(self):
        """Show the responses """
        
        print("The responses are:")
        for response in self.responses:
            

            print(f"-{response}")

