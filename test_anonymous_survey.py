import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ Test for class anonymous survey"""

   

    # def test_store_single_response(self):
    #     """Test that a single response is stored properly"""

    #     question = "What's your favorite place?"
    #     my_survey = AnonymousSurvey(question) # survey instance is created
    #     my_survey.store_responses('Bali')
    #     self.assertIn('Bali', my_survey.responses) # Compares my response with stored responses
    
    # def test_score_for_multiple_reesponses(self):
    #     """Test that a single response is stored properly"""

    #     question = "What is your most favorite place?"
    #     my_survey = AnonymousSurvey(question)
    #     responses = ['Bali', 'Thailnad', 'Panch Kedar', 'Char Dham']

    #     for response in responses:
    #         my_survey.store_responses(response)
        
    #     # for response in responses:
    #         self.assertIn(response, my_survey.responses)


    ######### When we define a setUp method to test the Class ############
    
    def setUp(self):
        """Creates a survey and set of responses for use in all test methods. """
        
        question = "What's your favorite place?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Bali', 'Kedar', 'Madrid', 'USA']

        #### As each these are prefixed by self, so they can be used anywhere in the class
    
    def test_store_single_response(self):
        """Test that a single response is stored properly"""

        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_multiple_responses(self):
        """Test that set of multiple responses is stored properly"""

        for response in self.responses:
            self.my_survey.store_responses(response)
        
        # for response in self.responses:
            self.assertIn(response, self.my_survey.responses)





if __name__ == '__main__':
    unittest.main()








