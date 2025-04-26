
# Load model directly
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModel

model_name = "philipfourie/bi-morse-code"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)



text = """<bos><start_of_turn>user
Is it working?<end_of_turn>
<start_of_turn>model
"""

print(text)

outputs = model.generate(
    **tokenizer([text], return_tensors = "pt"),
    max_new_tokens = 200, # Increase for longer outputs!
    # Recommended Gemma-3 settings!
    temperature = 1, top_p = 0.95, top_k = 64,
)

output  = tokenizer.batch_decode(outputs)[0]
print(output)
