# morse-code-llm

![Person clicking](docs/clicking.png)

## Purpose

This project demonstrates how a Large Language Model (LLM) can be fine-tuned to perform specialised tasks. In this example, the base model used is Gemma 3 1B (pretrained), fine-tuned specifically to translate between English and Morse code.

Note: This LLM is intended solely for demonstration and educational purposes. It does not have practical real-world applications beyond being a teaching example.


## Prerequisites

- Python >3.11 but <3.13 (as there are known issues with 3.13)
- VS Code
- VS Code Jupyter Notebook extension
- You need an account on Hugging Face

### Steps to Obtain a Writeable Token from Hugging Face

1. Visit [Hugging Face](https://huggingface.co) and log in to your account.
2. Navigate to your profile settings by clicking on your avatar in the top-right corner and selecting "Settings."
3. In the settings menu, select "Access Tokens."
4. Click on "New Token," provide a name for the token, and set the role to "write."
5. Copy the generated token.

### Login Using the Hugging Face CLI

Run the following command in your terminal to log in:

```bash
huggingface-cli login
```

Paste your token when prompted. 


## Install

### Environment Compatibility

The notebooks in this project are best run on Linux or WSL2 environment. Running them natively on Windows can present challenges. I used WSL2 with Debian.


### Setting up a Python Virtual Environment

It is recommended to create a Python virtual environment before installing the project requirements. This ensures that dependencies are isolated and do not interfere with other projects.

To create and activate a virtual environment, follow these steps:

1. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment**:
   
     ```bash
     source .venv/bin/activate
     ```

3. **Install the requirements**:
   ```bash
   pip install -r requirements.txt
   ```

### Selecting the Virtual Environment in VS Code Jupyter Notebook

To use the virtual environment in a Jupyter Notebook within VS Code:

1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac).
2. Search for and select `Python: Select Interpreter`.
3. Choose the interpreter located in the `venv` directory (e.g., `./venv/bin/python` or `.\venv\Scripts\python.exe`).
4. Open your notebook, and in the top-right corner, select the kernel corresponding to the virtual environment.


## Notebooks

> [!TIP]
> Run the notebooks sequentially from `00-test-env.ipynb` to `02-fine-tune-bi.ipynb` for this guide.

### [00-test-env.ipynb](00-test-env.ipynb)
To verify that the custom Morse code library is installed and to confirm that the Jupyter Notebook widgets are functioning as expected.

### [01-build-dataset.ipynb](01-build-dataset.ipynb)
To create the training dataset by preparing English phrases and their Morse Code translations. This notebook includes data normalisation, encoding, deduplication, and uploading the dataset to Hugging Face.

### [02-fine-tune-bi.ipynb](02-fine-tune-bi.ipynb)
To fine-tune the Gemma 3 model for bidirectional translation between English and Morse Code. This notebook uses the dataset prepared in `01-build-dataset.ipynb` and trains the model for both directions of translation.


## Model Evaluation with TensorBoard

To evaluate the model using TensorBoard, follow these steps:

1. Run the following command to start TensorBoard:
   ```bash
   tensorboard --logdir outputs
   ```

2. Ensure your configuration includes the following settings:
   ```python
   STConfig(
       ...
       output_dir = "outputs",
       report = "tensorboard"
   )
   ```

### Understanding Key Metrics

- **Training Loss**: This metric indicates how well the model is learning during training. A decreasing training loss generally signifies that the model is improving. However, if the loss plateaus or increases, it may indicate overfitting or learning issues.

- **Gradient Norm (grad_norm)**: This measures the magnitude of gradients during backpropagation. Large gradient norms can lead to instability, while very small norms may indicate vanishing gradients. Monitor this value to ensure stable and effective training.


## LM Studio Support

After creating a [GGUF](https://huggingface.co/philipfourie/bi-morse-code-Q8_0-GGUF) file and hosting it on Hugging Face, you can download and use it in [LM Studio](https://lmstudio.ai/). LM Studio is a user-friendly interface for interacting with language models, allowing you to test and deploy your fine-tuned model efficiently. Simply follow the instructions in LM Studio to load the GGUF file and start using your model.

## Ollama Support

It is possible to build a [GGUF](https://huggingface.co/philipfourie/bi-morse-code-Q8_0-GGUF) file and host it in [Ollama](https://ollama.com/). Ollama provides a platform for [deploying](https://ollama.com/philipfourie/bi-morse-code) and managing language models with ease. For detailed instructions on how to set this up, refer to the [ollama/README.md](ollama/README.md) file included in this repository.