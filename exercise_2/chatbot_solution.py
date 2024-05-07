from openai import OpenAI

# Here we're using dotenv (pip install python-dotenv) to manage environment vars
from dotenv import load_dotenv
import os

load_dotenv()

class Chatbot:

    def __init__(self):

        # This works because you've set the OPENAI_API_KEY env variable with dotenv
        self.client = OpenAI() # alternatively self.client = OpenAI(api_key=<<your OPENAI_API_KEY>>)
        self.system_message = None

    # In this function we will create the system message and include the relevant context
    def include_context_in_system_message(self, context):

        # Edit this system message
        self.system_message = f"""
        You are  'Flat Earth Bot' and you will strongly argue the case for a flat earth based on
        proofs that we will provide as context.
        
        Your personality is dismissive and condescending.
        
        Here are the relevant proofs:
        
        {context}
        
        """

    # This is a placeholder function to retreive the relevant context.
    # This would be context for a question, which will currently be blank.
    # At the moment, it just injects some static info from a file.
    # We will replace this with a Vector DB call later
    def retrieve_context(self, question):

        # This call to get info from a file will be replaced eventually with a
        # Vector db call
        with open('flat_earth_extract.txt', 'r') as file:

            context = file.read()

        return context


    def respond_to_question(self, question):

        context = self.retrieve_context(question)
        self.include_context_in_system_message(context)

        # Below is an example chat.completions API call taken from the openai documentation
        # Modify this call to include your question and augmented system_message
        # You'll have to write some logic before to retrieve the context
        # and incorporate that context with your system message instruction
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": question},
            ]
        )

        # Parse the response to an answer and return it
        return response.choices[0].message.content


# Call the chatbot to respond to a question and get the answer based on the static injected context
# Example question: If the earth is flat, why do you only see the top half of a ship

chatbot = Chatbot()
answer = chatbot.respond_to_question('If the earth is flat, why do you only see the top half of a ship')
print('Answer:', answer)