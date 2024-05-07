from openai import OpenAI
from pinecone import Pinecone

# Here we're using dotenv (pip install python-dotenv) to manage environment vars
from dotenv import load_dotenv
import os

load_dotenv()


class Chatbot:

    def __init__(self):
        # This works because you've set the OPENAI_API_KEY env variable with dotenv
        self.oa_client = OpenAI()  # alternatively self.client = OpenAI(api_key=<<your OPENAI_API_KEY>>)
        self.pc_client = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
        self.system_message = None

    # In this function we will create the system message and include the relevant context
    def include_context_in_system_message(self, context):
        # Edit this system message
        self.system_message = f"""
        You are 'Flat Earth Bot' and you will strongly argue the case for a flat earth based on
        proofs that we will provide as context.
        
        Your personality is dismissive and condescending.
        
        Here are the relevant proofs:
        
        {context}
        
        """

    # TODO Use the code you've constructed in previous exercices
    # 1. Embed the questions
    # 2. Retrieve the chunks from pinecone
    def retrieve_context(self, question):
        pass

    def respond_to_question(self, question):
        context = self.retrieve_context(question)
        self.include_context_in_system_message(context)

        # Call the OpenAI API with your systems message and question
        response = self.oa_client.chat.completions.create(
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
# answer = chatbot.respond_to_question('what is the correct way refer to to the school of philosophy that describes the earth as flat')
answer = chatbot.respond_to_question(
    'if the earth is flat, why does only the top half of a ship appear when it is at a distance')

print('Answer:', answer)
