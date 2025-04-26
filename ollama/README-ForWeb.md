# Bidirectional Morse Code LLM

![person-clicking-small.png](/assets/philipfourie/bi-morse-code/61c907c2-234b-4851-a048-6a3d87ca87b8)

This project demonstrates how a Large Language Model (LLM) can be fine-tuned to perform specialised tasks. In this example, the base model used is Gemma 3 1B (pretrained), fine-tuned specifically to translate between English and Morse code.

> **Note:** This LLM is intended solely for demonstration and educational purposes. It does not have practical real-world applications beyond being a teaching example.

## How to Use

Run the model using the following command:

```bash
ollama run philipfourie/bi-morse-code
```

This model is designed for command-line interaction. Make sure to enter sentences with correct punctuation, especially ending with a period. For example:

```
>>> Hello World.
.... . .-.. .-.. --- / .-- --- .-. .-.. -.. .-.-.-
```

or the reverse

```
>>> --. --- --- -.. / -... -.-- . / .-- --- .-. .-.. -.. .-.-.-
Good bye world.
```

**Important:**
- The model expects properly punctuated sentences (e.g., ending with a period).
- It is not intended for conversational use. The input provided must be a single sentence at a time.

## References

- [Hugging Face Model (Q8 GGUF)](https://huggingface.co/philipfourie/bi-morse-code-Q8_0-GGUF)
- [Hugging Face Model (SafeTensors)](https://huggingface.co/philipfourie/bi-morse-code-Q8_0-GGUF)
- [GitHub Repository](https://github.com/philipf/morse-code-llm)