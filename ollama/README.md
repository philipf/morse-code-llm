# Ollama Notes

## How to Create and Build

First, create a `Modelfile`. See the [Modelfile](Modelfile) in this directory as an example. Note that the [template](https://github.com/ollama/ollama/blob/main/docs/template.md) included in this file is for Gemma 3. Additionally, it only retains the last message in the conversation.

The structure for the `Modelfile` is described in detail [here](https://github.com/ollama/ollama/blob/main/docs/modelfile.md).

To create the Ollama model, run:
```bash
ollama create -f Modelfile philipfourie/bi-morse-code
```

For quick iterations, you can create and run the model with:
```bash
ollama create bi-morse-code; ollama run bi-morse-code
```

## How to Push a Model to Ollama.com

1. Ensure you have an account on [Ollama's website](https://ollama.com).
2. Update your public key as described in their documentation.

Then, push your model with:
```bash
ollama push philipfourie/bi-morse-code
```

## Debugging the Template

To enable debugging, set the `OLLAMA_DEBUG` environment variable and start the server:
```powershell
$env:OLLAMA_DEBUG="1"
ollama serve
```

## Additional Notes

- For more details on using Ollama, refer to the [official documentation](https://github.com/ollama/ollama).
- Ensure your `Modelfile` adheres to the required structure to avoid errors during creation or deployment.
