# Exercise 4 - Bring It All Together

## Aim

The aim of the exercise is to:

1. Complete you Chatbot class and connect it to your datastore
2. Retreive relevant chunks and augment them into the chat
3. Generate the answer

The exercise is complete when your bot can answer a targeted 
question referencing the book.

## Method

### 1. Choose Your Class

Either:

1. Use the class that you fininshed in Exercise 2 earlier, or
2. Use the **ragbot.py** class in this directory


### 2. Connect it to Pinecone

Amend the retrieve_context() method so that it now points to a Pinecone index.

Retrieve the relevant context and inject into the System Message.

Tip: you might just want to copy some of the methods from the last exercise.

### 4. Ask your Bot Questions

Call the bot and get it to answer questions. Here are some examples:

Start with our constant question we've been using:

> 'If the earth is not curved, why does only the top half of a ship when it is far away?'

But why not try these:

> 'Do the press speak favourable about Flat Earth Theory? Give me examples.'
> 'Does the philosophical school of thought that pertains to a flat earth have a name?'
> 'Has the Smithsonian Institute embraced Flat Earth theory?'

