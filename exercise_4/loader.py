import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI

# you need to do a pip install of LangChain, you can just use the text splitter
# pip install -qU langchain-text-splitters
from langchain.text_splitter import RecursiveCharacterTextSplitter


load_dotenv()

oa = OpenAI()
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
index_name = 'proofs'

# We'll use this function to embed the chunk
# We'll also use it to embed the question for query
def embed_chunk(text):

    response = oa.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )

    print(response)

    embedding = response.data[0].embedding

    return embedding


# This will create your Pinecone index
def create_index(index):

    try:

        pc.delete_index(index)

    except:

        print("Index does not exist, creating new index...")

    pc.create_index(
        name=index,
        dimension=1536,
        metric='cosine',
        spec=ServerlessSpec(
            region='us-east-1',
            cloud='aws'
        )
    )

# This function will split the text into chunk and upsert them
# TODO amend the code so you are using the a suitable chunk_size and chunk_overlap
def upsert_chunks_from(text_file):

    index = pc.Index(index_name)

    with open(text_file, 'r') as file:

        text = file.read()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
    chunks = text_splitter.split_text(text)

    for i, chunk in enumerate(chunks):

        dict = {
            "id": str(i),
            "values": embed_chunk(chunk),
            "metadata": {
                "chunk": chunk,
            }
        }

        print(dict)

        index.upsert(vectors=[dict])


# This will be used to retrieve chunks from Pinecone
# Default chunk to retrieve is 5
def retrieve_chunks(query, no_of_chunks=5):

    # The query is embedded before querying Pinecone
    embedding = embed_chunk(query)

    index = pc.Index(index_name)

    response = index.query(
        vector= embedding,
        top_k=no_of_chunks,
        include_metadata=True
    )

    retrieved_chunks = ""

    for match in response['matches']:

        retrieved_chunks += "excerpt...........\n"
        retrieved_chunks += match['metadata']['chunk'] + '\n'

    return retrieved_chunks


# Run the create_index, chunking and upserting from here
create_index(index_name)
upsert_chunks_from('flat_earth.txt')

# TODO have a go at some experimental queries
# are the results relevant?
chunks = retrieve_chunks('If the earth is not curved, why can only the top half of a ship be seen at a distance?')
print(chunks)






