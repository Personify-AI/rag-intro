# Exercise 2 - The OpenAI API Chat Completions

## Aim

The aim of the exercise is to:
1. Get you familiar with the Open AI API calls for Chat Completions
2. Build of a class for our chatbot, with placeholder functions that we can implement later

The exercise is complete when your code can answer the question:

'If the earth is flat, why do you only see the top half of a ship when it is at a distance?'

Based on the context we'll inject from file **flat_earth_extract.txt**

## Method

### 1. Set up your environment 

You've likely created a new directory for this project, if you haven't, create one now.

Within that directory, set up a Python Venv, you will need Python 3.8 or greater. 
Follow these instructions or do it the way you would normally

    python -m venv venv

Then, on a Mac

    source venv/bin/activate 
    
or a PC

    venv/bin/activate 

Install openai and python-dotenv:

    pip install openai python-dotenv

Find you OpenAI API Key at https://platform.openai.com/api-keys

Edit the .env file to include you OPENAI_API_KEY

    OPENAI_API_KEY=<<your-api_key>>

### 2. Code your System Message

In the file **chatbot.py** find this function:

        def include_context_in_system_message(self, context):
        # Edit the system message
        self.system_message = f"""
        Your fixed instructions to the bot go here
        
        Based on this context:
        
        {context}

        """  

Edit it to give a System Message instruction to the Chatbot, likely the 
System Message you fleshed out in Exercise 1.


### 3. Get the OpenAI AI call working

In the file **chatbot.py** find this function:

       def respond_to_question(self, question):

        context = self.retrieve_context(question)
        self.include_context_in_system_message(context)

        # Below is an example chat.completions API call taken from the openai documentation
        # Modify this call to include your question and augmented system_message
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                {"role": "user", "content": "Where was it played?"}
            ]
        )

        # Parse the response to get an answer and return it
        print(response)


Take a few minutes to understand the API call and its response, run it as is if you want.

Alter the API call to include your system message and question.


### 4. Stretch Exercise - Tokens

How many tokens did your call use?
How much did that call cost?

Tip - token costs are on the https://openai.com/api/pricing page.

Try it with GPT-4 as a model, how much did that cost?