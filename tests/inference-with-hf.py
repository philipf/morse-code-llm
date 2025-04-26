
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "philipfourie/bi-morse-code"
tokenizer  = AutoTokenizer.from_pretrained(model_name)
model      = AutoModelForCausalLM.from_pretrained(model_name)

text = """<bos><start_of_turn>user
Is this thing on?<end_of_turn>
<start_of_turn>model
"""

print("Chat template:", text)

outputs = model.generate(
    **tokenizer([text], return_tensors = "pt"),
    max_new_tokens = 200, # Increase for longer outputs
    temperature = 1, top_p = 0.95, top_k = 64, # Recommended Gemma-3 settings!
)

output  = tokenizer.batch_decode(outputs)[0]
print("Result:\n", output)
