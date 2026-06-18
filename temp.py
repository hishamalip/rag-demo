from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-embeddinggemma-300m",
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
    check_embedding_ctx_length=False
)

vec = embeddings.embed_query("Hello world")
print(len(vec))
print(vec[:5])