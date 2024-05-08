import llama_cpp

llm = llama_cpp.Llama(model_path="./llama-2-7b-chat.Q4_0.gguf", embedding=True)
token = llm.tokenize("Hello, world!".encode())
print(token)
print(type(token))

output = llm.detokenize(token)
print(output)
print(type(output))

print("Hello, world!".encode())


