import llama_cpp

llm = llama_cpp.Llama(model_path="./llama-2-7b-chat.Q4_0.gguf", embedding=True)

embeddings = llm.create_embedding("Hello, world!")
print(embeddings)

embeddings = llm.create_embedding("Machine learning (ML) is a field of study in artificial intelligence concerned with the \
                                  development and study of statistical algorithms that can learn from data and generalize to \
                                  unseen data, and thus perform tasks without explicit instructions.")
print(embeddings)
print(len(embeddings["data"][0]["embedding"]))


