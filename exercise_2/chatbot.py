from openai import OpenAI

# Here we're using dotenv (pip install python-dotenv) to manage environment vars
from dotenv import load_dotenv
import os

load_dotenv()


class Chatbot:

    def __init__(self):

        # This works because you've set the OPENAI_API_KEY env variable with dotenv
        self.client = OpenAI()  # alternatively self.client = OpenAI(api_key=<<your OPENAI_API_KEY>>) if not using dotenv
        self.system_message = None

    # In this function we will create the system message and include the relevant context
    def include_context_in_system_message(self, context):
        #TODO Edit the system message, to include your instruction
        self.system_message = f"""
        Your fixed instructions to the bot go here
        
        Based on this context:
        
        {context}

        """

    # This is a placeholder function to retreive the relevant context.
    def retrieve_context(self, question):

        # Currently we get context from a file, but we'll replace with Vector DB call
        with open('flat_earth_extract.txt', 'r') as file:
            context = file.read()

        return context

    def respond_to_question(self, question):

        context = self.retrieve_context(question)
        self.include_context_in_system_message(context)

        # Below is an example chat.completions API call taken from the openai documentation
        #TODO Modify this call to include your question and augmented system_message
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                {"role": "user", "content": "Where was it played?"}
            ]
        )

        # TODO Parse the response to get an answer and return it
        # Look at other response properties - how many tokens did your call cost?
        print(response)

#TODO Call the chatbot to respond to a question and get the answer based on the static injected context
# Example question: If the earth is flat, why do you only see the top half of a ship when it is at a distance?
chatbot = Chatbot()

chatbot.respond_to_question('x')


