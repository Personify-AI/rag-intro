# Exercise 4 - Bring It All Together

## Aim

The aim of the exercise is to:
1. Complete you Chatbot class

The exercise is complete when your bot can answer a targeted 
question referencing the book.

## Method

### 1. Choose Your Class

Either:

1. Use the class that you fininshed in Exercise 2 earlier, or
2. Use the **ragbot.py** class in this directory



### 2. Connect it to Pinecone

Amend the 


### 3. Create Your Index and Upsert

Use create_index() and upsert_chunks_from() functions to create the 
Pinecone index that will store chunks for your bot . 

Then upsert your chunks ready for your bot to use.


### 4. Query the Index

Use the retrieve_chunks() function to embed a query and get the 
closest vectors back.

How do the results look for the question:

> 'If the earth is not curved, why does only the top half of a ship when it is far away?'



