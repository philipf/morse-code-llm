# # Use a pipeline as a high-level helper
# from transformers import pipeline

# messages = [{
#     "role": "user",
#     "content": [{
#         "type" : "text",
#         "text" : "Hi Phil, can you please send food and water as soon as possible?",
#     }]
# }]

# pipe = pipeline("text-generation", model="")
# output = pipe(messages,
#               temperature = 1, top_p = 0.95, top_k = 64,
              
#               )

# print(output)



from unsloth import FastModel
import torch

model, tokenizer = FastModel.from_pretrained(
    #model_name = "unsloth/gemma-3-1b-pt-unsloth-bnb-4bit",
    model_name = "philipfourie/bi-morse-code",
    max_seq_length = 2048, # Choose any for long context!
    load_in_4bit = True,  # 4 bit quantization to reduce memory
    load_in_8bit = False, # [NEW!] A bit more accurate, uses 2x memory
    full_finetuning = False, # [NEW!] We have full finetuning now!
)


from unsloth.chat_templates import get_chat_template
tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma-3",
)
messages = [{
    "role": "user",
    "content": [{
        "type" : "text",
        "text" : "Is it working?",
    }]
}]

# messages = [{
#     "role": "user",
#     "content": [{
#         "type" : "text",
#         "text" : ".. / .- -- / -. --- - / -.-- --- ..- .-. / -- --- - .... . .-. .-.-.-",
#     }]
# }]

text = tokenizer.apply_chat_template(
    messages,
    tokenize= False,
    add_generation_prompt = True, # Must add for generation
)

print(text)

outputs = model.generate(
    **tokenizer([text], return_tensors = "pt").to("cuda"),
    max_new_tokens = 200, # Increase for longer outputs!
    # Recommended Gemma-3 settings!
    temperature = 1, top_p = 0.95, top_k = 64,
)

output  = tokenizer.batch_decode(outputs)[0]
print(output)



outputs = model.generate(
    **tokenizer([text], return_tensors = "pt").to("cuda"),
    max_new_tokens = 200, # Increase for longer outputs!
    # Recommended Gemma-3 settings!
    temperature = 1, top_p = 0.95, top_k = 64,
)

output  = tokenizer.batch_decode(outputs)[0]
print(output)
