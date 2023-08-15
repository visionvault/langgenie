# -*- coding: utf-8 -*-
"""Langchain Q/A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s0vQuvpyOX9GZaGYDFPrMH6hMPW5CmXQ?resourcekey=0-NhbWFNqXDS4_LjOViPlKZQ
"""

pip install newspaper3k gradio

pip install openai

# Set up OpenAI API credentials
import openai
openai.api_key = ""

from newspaper import Article
from newspaper import Config
import nltk
nltk.download('punkt')
from gradio.mix import Series
import gradio as gr
def extract_article_text(url):
  USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
  config = Config()
  config.browser_user_agent = USER_AGENT
  config.request_timeout = 10

  article = Article(url, config=config)
  article.download()
  article.parse()
  text = article.text
  return text

linkedin_text = extract_article_text('https://www.linkedin.com/posts/prabakaranchandrantheds_ai-business-work-activity-7083019606440759296-Przz?utm_source=share&utm_medium=member_desktop')

linkedin_text

langchain_text = extract_article_text('https://python.langchain.com/docs/get_started/installation')

langchain_quickstart = extract_article_text('https://python.langchain.com/docs/get_started/quickstart')

langchain_modules = extract_article_text('https://python.langchain.com/docs/modules/')

langchain_model_io = extract_article_text('https://python.langchain.com/docs/modules/model_io/')

langchain_prompts = extract_article_text('https://python.langchain.com/docs/modules/model_io/prompts/')

langchain_prompt_template = extract_article_text('https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/')

langchain_example_selector = extract_article_text('https://python.langchain.com/docs/modules/model_io/prompts/example_selectors/')

langchain_language_models = extract_article_text('https://python.langchain.com/docs/modules/model_io/models/')

langchain_output_parsers = extract_article_text('https://python.langchain.com/docs/modules/model_io/output_parsers/')

langchain_data_connection = extract_article_text('https://python.langchain.com/docs/modules/data_connection/')

langchain_document_loader = extract_article_text('https://python.langchain.com/docs/modules/data_connection/document_loaders/')

langchain_document_transformer = extract_article_text('https://python.langchain.com/docs/modules/data_connection/document_transformers/')

langchain_embedding = extract_article_text('https://python.langchain.com/docs/modules/data_connection/text_embedding/')

langchain_vector_store = extract_article_text('https://python.langchain.com/docs/modules/data_connection/vectorstores/')

langchain_retrievers = extract_article_text('https://python.langchain.com/docs/modules/data_connection/retrievers/')

langchain_chains = extract_article_text('https://python.langchain.com/docs/modules/chains/')

langchain_memory = extract_article_text('https://python.langchain.com/docs/modules/memory/')

langchain_agents = extract_article_text('https://python.langchain.com/docs/modules/agents/')

langchain_agent_types = extract_article_text('https://python.langchain.com/docs/modules/agents/agent_types/')

langchain_conversational_agent = extract_article_text('https://python.langchain.com/docs/modules/agents/agent_types/chat_conversation_agent')

langchain_openai_agent = extract_article_text('https://python.langchain.com/docs/modules/agents/agent_types/openai_functions_agent')

langchain_plan = extract_article_text('https://python.langchain.com/docs/modules/agents/agent_types/plan_and_execute')

langchain_react = extract_article_text('https://python.langchain.com/docs/modules/agents/agent_types/react')

langchain_react_store = extract_article_text('https://python.langchain.com/docs/modules/agents/agent_types/react_docstore')

langchain_self_ask = extract_article_text('https://python.langchain.com/docs/modules/agents/agent_types/self_ask_with_search')

langchain_structured_tool = extract_article_text('https://python.langchain.com/docs/modules/agents/agent_types/structured_chat')

langchain_combine_vector_store_agent = extract_article_text('https://python.langchain.com/docs/modules/agents/how_to/agent_vectorstore')

langchain_custom_agent = extract_article_text('https://python.langchain.com/docs/modules/agents/how_to/custom_agent')

langchain_custom_agent_retrieval = extract_article_text('https://python.langchain.com/docs/modules/agents/how_to/custom_agent_with_tool_retrieval')

langchain_custom_llm_agent = extract_article_text('https://python.langchain.com/docs/modules/agents/how_to/custom_llm_agent')

langchain_custom_llm_chat = extract_article_text('https://python.langchain.com/docs/modules/agents/how_to/custom_llm_chat_agent')

langchain_multiaction_agent = extract_article_text('https://python.langchain.com/docs/modules/agents/how_to/custom_multi_action_agent')

langchain_tools = extract_article_text('https://python.langchain.com/docs/modules/agents/tools/')

langchain_custom_tool = extract_article_text('https://python.langchain.com/docs/modules/agents/tools/how_to/custom_tools')

langchain_hitl = extract_article_text('https://python.langchain.com/docs/modules/agents/tools/how_to/human_approval')

langchain_multiinput_tool = extract_article_text('https://python.langchain.com/docs/modules/agents/tools/how_to/multi_input_tool')

langchain_tool_input_schema = extract_article_text('https://python.langchain.com/docs/modules/agents/tools/how_to/tool_input_validation')

langchain_tool_openai_function = extract_article_text('https://python.langchain.com/docs/modules/agents/tools/how_to/tools_as_openai_functions')

len(langchain_quickstart)

"""Building the knowledge base"""

pip install langchain

pip install tiktoken

pip install "pinecone-client[grpc]"==2.2.1

import tiktoken

tiktoken.encoding_for_model('gpt-3.5-turbo')

import tiktoken

tokenizer = tiktoken.get_encoding('cl100k_base')

# create the length function
def tiktoken_len(text):
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)

tiktoken_len(langchain_text)

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1400,
    chunk_overlap=20,
    length_function=tiktoken_len,
    separators=["\n\n", "\n", " ", ""]
)

"""Create embeddings"""

from langchain.embeddings.openai import OpenAIEmbeddings

model_name = 'text-embedding-ada-002'

embed = OpenAIEmbeddings(
    model=model_name,
    openai_api_key=openai.api_key
)

texts = [
    langchain_text,
    langchain_quickstart
]

res = embed.embed_documents(texts)
len(res), len(res[0])

"""Vector Database"""

import pinecone
index_name = '<Index-name>'
# find API key in console at app.pinecone.io
PINECONE_API_KEY = ""
# find ENV (cloud region) next to API key in console
PINECONE_ENVIRONMENT = "asia-southeast1-gcp-free"


pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENVIRONMENT
)

if index_name not in pinecone.list_indexes():
    # we create a new index
    pinecone.create_index(
        name=index_name,
        metric='cosine',
        dimension=len(res[0])  # 1536 dim of text-embedding-ada-002
    )

index_name = 'gideon'
index = pinecone.GRPCIndex(index_name)

index.describe_index_stats()

import pandas as pd



# Create a dictionary with your data
data = {
    'url': [
        "https://python.langchain.com/docs/get_started/installation",
        "https://python.langchain.com/docs/get_started/quickstart",
        'https://python.langchain.com/docs/modules/',
        'https://python.langchain.com/docs/modules/model_io/',
        'https://python.langchain.com/docs/modules/model_io/prompts/',
        'https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/',
        'https://python.langchain.com/docs/modules/model_io/prompts/example_selectors/',
        'https://python.langchain.com/docs/modules/model_io/models/',
        'https://python.langchain.com/docs/modules/model_io/output_parsers/',
        'https://python.langchain.com/docs/modules/data_connection/',
        'https://python.langchain.com/docs/modules/data_connection/document_loaders/',
        'https://python.langchain.com/docs/modules/data_connection/document_transformers/',
        'https://python.langchain.com/docs/modules/data_connection/text_embedding/',
        'https://python.langchain.com/docs/modules/data_connection/vectorstores/',
        'https://python.langchain.com/docs/modules/data_connection/retrievers/',
        'https://python.langchain.com/docs/modules/chains/',
        'https://python.langchain.com/docs/modules/memory/',
        'https://python.langchain.com/docs/modules/agents/',
        'https://python.langchain.com/docs/modules/agents/agent_types/',
        'https://python.langchain.com/docs/modules/agents/agent_types/chat_conversation_agent',
        'https://python.langchain.com/docs/modules/agents/agent_types/openai_functions_agent',
        'https://python.langchain.com/docs/modules/agents/agent_types/plan_and_execute',
        'https://python.langchain.com/docs/modules/agents/agent_types/react',
        'https://python.langchain.com/docs/modules/agents/agent_types/react_docstore',
        'https://python.langchain.com/docs/modules/agents/agent_types/self_ask_with_search',
        'https://python.langchain.com/docs/modules/agents/agent_types/structured_chat',
        'https://python.langchain.com/docs/modules/agents/how_to/agent_vectorstore',
        'https://python.langchain.com/docs/modules/agents/how_to/custom_agent',
        'https://python.langchain.com/docs/modules/agents/how_to/custom_agent_with_tool_retrieval',
        'https://python.langchain.com/docs/modules/agents/how_to/custom_llm_agent',
        'https://python.langchain.com/docs/modules/agents/how_to/custom_llm_chat_agent',
        'https://python.langchain.com/docs/modules/agents/how_to/custom_multi_action_agent',
        'https://python.langchain.com/docs/modules/agents/tools/',
        'https://python.langchain.com/docs/modules/agents/tools/how_to/custom_tools',
        'https://python.langchain.com/docs/modules/agents/tools/how_to/human_approval',
        'https://python.langchain.com/docs/modules/agents/tools/how_to/multi_input_tool',
        'https://python.langchain.com/docs/modules/agents/tools/how_to/tool_input_validation',
        'https://python.langchain.com/docs/modules/agents/tools/how_to/tools_as_openai_functions'


    ],
    'text': [
        langchain_text,
        langchain_quickstart,
        langchain_modules,
        langchain_model_io,
        langchain_prompts,
        langchain_prompt_template,
        langchain_example_selector,
        langchain_language_models,
        langchain_output_parsers,
        langchain_data_connection,
        langchain_document_loader,
        langchain_document_transformer,
        langchain_embedding,
        langchain_vector_store,
        langchain_retrievers,
        langchain_chains,
        langchain_memory,
        langchain_agents,
        langchain_agent_types,
        langchain_conversational_agent,
        langchain_openai_agent,
        langchain_plan,
        langchain_react,
        langchain_react_store,
        langchain_self_ask,
        langchain_structured_tool,
        langchain_combine_vector_store_agent,
        langchain_custom_agent,
        langchain_custom_agent_retrieval,
        langchain_custom_llm_agent,
        langchain_custom_llm_chat,
        langchain_multiaction_agent,
        langchain_tools,
        langchain_custom_tool,
        langchain_hitl,
        langchain_multiinput_tool,
        langchain_tool_input_schema,
        langchain_tool_openai_function


    ]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

from tqdm.auto import tqdm
for i in df.head():
  print (record)

"""Creating Indexes"""

from tqdm.auto import tqdm
from uuid import uuid4

batch_limit = 100

texts = []
metadatas = []

# Assuming 'df' is your DataFrame
for i, record in tqdm(df.iterrows(), total=df.shape[0]):
    # Get metadata fields for this record
    metadata = {
        'source': record['url'],
    }
    # Now we create chunks from the record text
    # Assuming 'text_splitter' is a function that splits text into chunks
    record_texts = text_splitter.split_text(record['text'])
    # Create individual metadata dicts for each chunk
    record_metadatas = [{
        "chunk": j, "text": text, **metadata
    } for j, text in enumerate(record_texts)]
    # Append these to current batches
    texts.extend(record_texts)
    metadatas.extend(record_metadatas)
    # If we have reached the batch_limit we can add texts
    if len(texts) >= batch_limit:
        ids = [str(uuid4()) for _ in range(len(texts))]
        # Assuming 'embed' is an object that can embed documents
        embeds = embed.embed_documents(texts)
        # Assuming 'index' is an object that can upsert vectors
        index.upsert(vectors=zip(ids, embeds, metadatas))
        texts = []
        metadatas = []

if len(texts) > 0:
    ids = [str(uuid4()) for _ in range(len(texts))]
    embeds = embed.embed_documents(texts)
    index.upsert(vectors=zip(ids, embeds, metadatas))

index.describe_index_stats()

"""Vector Database"""

from langchain.vectorstores import Pinecone

text_field = "text"

# switch back to normal index for langchain
index = pinecone.Index(index_name)

vectorstore = Pinecone(
    index, embed.embed_query, text_field
)

query = "What does Langchain memory mean?"

vectorstore.similarity_search(
    query,  # our search query
    k=3  # return 3 most relevant docs
)

"""Generative Question answering"""

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# completion llm
llm = ChatOpenAI(
    openai_api_key=openai.api_key,
    model_name='gpt-3.5-turbo',
    temperature=0.2,
    stop = None,
    max_tokens = 512
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

query = "Explain with a real-world example the difference between an agent and a tool in Langchain"

qa.run(query)

import gradio as gr
def langchain_qa(question):

    answer = qa.run(question)
    return answer

examples = [
    ["What does memory mean in Langchain?"],
    ["What real-world problems can be solved by creating agents in Langchain?"],
    ["Explain with a real-world example the difference between an agent and a tool in Langchain"]
]

iface = gr.Interface(fn=langchain_qa,
                     inputs=gr.inputs.Textbox(lines=2, placeholder='What do you want to know about Langchain?'),
                     outputs='text',
                     title='LangGenie: Your personal LangChain Assistant',
                     description='This application provides answers to your queries about Langchain. Feel free to ask anything related to Langchain features, modules, or use-cases.',

                     examples=examples)

iface.launch(share=True)

