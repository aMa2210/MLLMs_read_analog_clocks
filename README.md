# MLLMs Read Analog Clocks

A research project for evaluating and fine-tuning **Multimodal Large Language Models (MLLMs)** on **analog clock reading tasks**.

---

## 📖 Overview
This repository contains scripts and notebooks for testing various vision-language models’ ability to **read analog clocks** and for fine-tuning them to improve performance.  
The project supports multiple model architectures including **GPT, Gemma, LLaMA, and Qwen**.

---

## ✨ Features
- **Model Evaluation**  
  Evaluate pre-trained MLLMs on analog clock reading tasks.  
  Example: [`Gemma3.ipynb`](Scripts/Gemma3.ipynb)

- **Fine-tuning Support**  
  Fine-tune models with custom clock datasets.  
  Examples:  
  - [`Fine_tune_Gemma3.ipynb`](Scripts/Fine_tune_Gemma3.ipynb)  

- **Multiple Model Types**  
  Out-of-the-box support for **Gemma3**, **LLaMA**, and **Qwen** vision-language models.

- **Dataset Processing**  
  Automatic processing of clock images with time labels.

---

## 📂 Repository Structure
```text
├── Scripts/                       # Jupyter notebooks for model evaluation and fine-tuning  
├── Dataset_for_experiment/        # Clock image datasets (standard, distorted, thin_hands, real_clocks)  
└── Results/                       # Excel files with model predictions and evaluation results  
```

---

## 🚀 Usage

### 1. Model Evaluation
Run the evaluation notebooks to test pre-trained models on clock reading tasks.  
- Example: [`QwenVL.ipynb`](Scripts/QwenVL.ipynb)  
- Results: Saved as **Excel files** with model predictions vs. ground truth.  

## 2. Fine-tuning  

### Fine-tuning OpenAI Models  
1. Configure your **OpenAI API key** in the system environment variables.  By default, the fine-tuning job uses OpenAI’s standard hyperparameter settings.
You can override them by adding a hyperparameters argument to the job creation call, e.g.:

```python
hyperparameters={
  "n_epochs": 3,
  "batch_size": 3,
  "learning_rate_multiplier": 0.05
}
```
2. Run [`Scripts/Generate_jsonl_For_FT.py`](Scripts/Generate_jsonl_For_FT.py) to generate a JSONL dataset.  
3. Update the `file` path in [`Scripts/Fine-tuneGPT.py`](Scripts/Fine-tuneGPT.py) to point to the generated JSONL file, then run the script.  
4. Use [`Scripts/AccessFinetunedModel.py`](Scripts/AccessFinetunedModel.py) to check the fine-tuning job status.  
5. Once fine-tuning is completed, replace the `model` parameter in [`Scripts/Openai.ipynb`](Scripts/Openai.ipynb) with the fine-tuned model ID, and proceed with evaluation.  

### Fine-tuning Open-Source Models  
1. Configure your **Hugging Face token** in the first cell of the target notebook . By default, fine-tuning of open-source models uses standard settings defined in `SFTConfig`. These include parameters such as number of training epochs, batch size, learning rate, optimizer, and logging intervals. You can modify them directly in the training script (e.g., [`Scripts/Fine_tune_Gemma3.ipynb`](Scripts/Fine_tune_Gemma3.ipynb)).  
2. In the third cell, set the values of `prefix` and `folder_name` so that `Data/{prefix}/{folder_name}` points to your fine-tuning dataset.  
3. Run all cells sequentially. The fine-tuned model files will be saved in the `Finetuned_models` directory.  
4. Update the `prefix` variable in the evaluation notebook (e.g., [`Scripts/Gemma3-finetuned.ipynb`](Scripts/Gemma3-finetuned.ipynb)) to ensure that `adapter_path` points to the saved model path.  
5. Run the evaluation notebook to complete the process.  

---
