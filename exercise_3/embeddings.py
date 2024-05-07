import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI


# We're loading env variables with dotenv
# Store your env variable in .env for PINECONE_API_KEY
load_dotenv()
oa = OpenAI()
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))


# These are the questions we're uploading
questions = [
    "which airlines fly from boston to washington dc via other cities",
    "show me the airlines that fly between toronto and denver",
    "show me round trip first class tickets from new york to miami",
    "i'd like the lowest fare from denver to pittsburgh",
    "show me a list of ground transportation at boston airport",
    "show me boston ground transportation",
    "of all airlines which airline has the most arrivals in atlanta",
    "what ground transportation is available in boston",
    "i would like your rates between atlanta and boston on september third",
    "which airlines fly between boston and pittsburgh"
]


# Function to create the Pinecone index
def create_index():

    try:
        pc.delete_index('questions')

    except:

        print('No index to delete')

    # TODO familiarise yourself with the create_index call
    # Update the dimensions to reflect the number of vectors in OpenAI embedding model
    pc.create_index(
        name='questions',
        dimension=n, # How many dimensions?
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )


# Function to embed text, it will be used for uploading vectors
# and for embedding any query before querying Pinecone
def get_embedding_for(text):

    response = oa.embeddings.create(
        model="text-embedding-3-small",
        input=text

    )

    # TODO make a call to this function and have a look at the OpenAI response
    # Adjust the function to return just the embedding
    print(response)


# Function to upload vectors and associated question data
def load_questions():

    index = pc.Index('questions')

    rows = []

    for i, question in enumerate(questions):

        # Note how we store the original question alongside the vector
        # in the metadata
        row = {
            'id': str(i), # each Pinecone record needs a string id
            'values': get_embedding_for(question),
            'metadata': {'question': question}
        }

        rows.append(row)

    # Upload the rows as a batch
    index.upsert(
        rows
    )

    # Here, we show you how the vectors take some time to create
    print('Index Description...........')
    print("you won't see nay vectors.. yet!")
    print(index.describe_index_stats())


# This function queries the vector database
# TODO alter this function to embed the query and return similar phrases
def query_questions(query):

    index = pc.Index('questions')

    # After a short time you will see there are 10 vectors there
    print(index.describe_index_stats())

    results = index.query(
        vector=[],
        top_k=5,
    )

    return results



# Use this space to call functions
get_embedding_for('How do I get a taxi in Boston?')

# Use these function calls to create and load
#create_index()
#load_questions()


