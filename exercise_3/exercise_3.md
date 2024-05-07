# Exercise 3 - Pinecone and Embeddings

## Aim

The aim of the exercise is to:
1. Get you set up with Pinecone
2. Do your first embeddings
3. Gain familiarity with querying the index with embeddings

The exercise is complete when you can:
- embed the question 'How do I get a taxi in Boston?'
- retrieve the most similar questions from Pinecone

## Method

### 1. Set up Pinecone

Go to https://www.pinecone.io, set up an account and start a new project

Install pinecone-client

    pip install pinecone-client

Find your Pinecone API keys from the **API KEYS** menu item on the left hand nav.

Edit the .env file to include you PINECONE_API_KEY

    PINECONE_API_KEY=<<your-api_key>>

### 2. Get Familiar with Embedding

The 'Embeddings' guide for OpenAI is https://platform.openai.com/docs/guides/embeddings.

Use the  get_embedding_for() function to practice embedding 

    'How do I get a taxi in Boston?'

Check the raw output from the OpenAI call.

Parse the response to return only the embedding from this function.


### 3. Create Index, Embed the Data and Upsert

Use the create_index() and load_questions() functions to get the
questions data loaded into the index.

You will need to alter the create_index query to include the correct dimension.

We print index statistics in that load operation, what do you notice?

Go to the index in the project console in Pinecone. Is your data there yet?

Have a look through the data and copy and paste some vectors for a query.

### 4. Query the Index

Use the query_questions() function to embed a query and get the closest vectors back.


### 5. Stretch Activity - Only Return Most Relevant Results

How would you augment the use of the top_k parameter with logic to 

a. Only return results if they were relevant
b. If there were lots of relevant results, to just return the ones that are the best




