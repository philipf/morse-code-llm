from unsloth import FastModel
from unsloth.chat_templates import get_chat_template


model, tokenizer = FastModel.from_pretrained(
    model_name = "philipfourie/bi-morse-code",
    max_seq_length = 2048, # Choose any for long context!
    load_in_4bit = True,  # 4 bit quantization to reduce memory
    load_in_8bit = False, # [NEW!] A bit more accurate, uses 2x memory
    full_finetuning = False, # [NEW!] We have full finetuning now!
)

tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma-3",
)

# Can be English or Morse code
prompt = "Is this thing on?"
#text = ".. / .- -- / -. --- - / -.-- --- ..- .-. / -- --- - .... . .-. .-.-.-"

messages = [{
    "role": "user",
    "content": [{
        "type" : "text",
        "text" : prompt,
    }]
}]

text = tokenizer.apply_chat_template(
    messages,
    tokenize= False,
    add_generation_prompt = True, # Must add for generation
)

print("Chat template:\n", text)

outputs = model.generate(
    **tokenizer([text], return_tensors = "pt").to("cuda"),
    max_new_tokens = 200,                          # Increase for longer outputs
    temperature = 1, top_p = 0.95, top_k = 64,     # Recommended Gemma-3 settings
)

output = tokenizer.batch_decode(outputs)[0]
print("Result:\n", output)