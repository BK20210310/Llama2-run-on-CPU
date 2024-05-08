from llama_cpp import Llama
llm = Llama(
      model_path="./llama-2-7b-chat.Q4_0.gguf",
      chat_format="chatml", 
      n_ctx=4096
)

finish_reason = ""
output_str = ""
prompt = [
            {
                "role": "system",
                "content": "You are a story teller.",
            }
        ]

while True:

    try:

        input_str = input("Please enter your question: ")
        if input_str == "END":
            break

        prompt.append({"role": "user", "content": input_str})

        if output_str != "":
            prompt.append({"role": "assistant", "content": output_str})
        if finish_reason == 'length':
            prompt.pop(1)
            prompt.pop(1)

        output = llm.create_chat_completion(
            messages=prompt,
            temperature=1.1,
        )

        output_str = output["choices"][0]["message"]["content"]

        print("Answer:", output)

        finish_reason = output["choices"][0]["finish_reason"]

    
    except:
        prompt.pop(1)
    

print(prompt)
