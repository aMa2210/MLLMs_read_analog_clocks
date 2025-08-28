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
Scripts/
├── Fine_tune_Gemma3.ipynb # Fine-tuning script for Gemma3 models
├── Fine_tune_LLaMa.ipynb # Fine-tuning script for LLaMA models
├── Fine_tune_Qwen.ipynb # Fine-tuning script for Qwen models
├── Gemma3.ipynb # Evaluation script for Gemma3 models
└── QwenVL.ipynb # Evaluation script for Qwen-VL models

- **Input format**: PNG clock images with filenames encoding the time.  
  Example: `12_30_06.png` → 12:30:06.  
- **Supported clock types**:
  - Standard clocks  
  - Distorted clocks  
  - Thin-hands clocks  
  - Real clock images  

---

## 🚀 Usage

### 1. Model Evaluation
Run the evaluation notebooks to test pre-trained models on clock reading tasks.  
- Example: [`QwenVL.ipynb`](Scripts/QwenVL.ipynb)  
- Results: Saved as **Excel files** with model predictions vs. ground truth.  

### 2. Fine-tuning
Use the fine-tuning notebooks to train models on your custom clock dataset.  
- Proper data formatting and collation functions included.  
- Example: [`Fine_tune_LLaMa.ipynb`](Scripts/Fine_tune_LLaMa.ipynb)

---
