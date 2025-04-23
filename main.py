from unsloth import FastModel
import torch

max_seq_length = 2048 # Choose any! We auto support RoPE Scaling internally!
dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
load_in_4bit = True # Use 4bit quantization to reduce memory usage. Can be False.

model, tokenizer = FastModel.from_pretrained(
    model_name = "./gemma-3-finetune",
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
        "text" : "The cat sat on the>>",
    }]
}]
text = tokenizer.apply_chat_template(
    messages,
    tokenize= False,
    add_generation_prompt = True, # Must add for generation
)


outputs = model.generate(
    **tokenizer([text], return_tensors = "pt").to("cuda"),
    max_new_tokens = 120, # Increase for longer outputs!
    # Recommended Gemma-3 settings!
    temperature = 0.01, top_p = 0.95, top_k = 64,
)

output  = tokenizer.batch_decode(outputs)[0]
print(output)

print("saving gguf")
model.save_pretrained_gguf(
    "/home/philipf/dev/testj/gemma-3-finetune",
    quantization_type = "Q8_0", # For now only Q8_0, BF16, F16 supported
)
