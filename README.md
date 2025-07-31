 # -Offline-Integration-with-Open-Source-LLMs-using-Transformers_mini_project

### Learning Objectives
     💠 Understand how to use open source LLMs locally without API access.
     💠 Install and use the Hugging Face Transformers library locally.
     💠 Perform text generation using pre-trained models such as GPT-2.
     💠 Understand how tokenizers and model pipelines work in LLMs
### Introduction to Concept
     💠 Large Language Models (LLMs) like GPT-2 are pre-trained neural networks capable ofgenerating and understanding text. 
     💠 Using the Hugging Face Transformers library, we candownload and run these models locally without needing an API key or internet connection after the initial model download.
     💠 This approach is ideal for offline work, local testing, or educational purposes where cloud services are unavailable.
### Prerequisites
     ✅ Python 3.8 or later
     ✅ Basic Python programming skills
     ✅ Internet connection (only for initial model download)
     ✅ A computer with enough memory (at least 4GB RAM recommended)
### Tools Required
    🔧 Python environment (Anaconda, Jupyter Notebook, or plain Python)
    🔧 Hugging Face `transformers` and `torch` libraries

### Setup Instructions
   #### Install required libraries:
        ⬇️pip install transformers torch

### Scenario
    You are developing a writing assistant tool that helps users brainstorm ideas for
    articles. Use GPT-2 to generate 3 possible titles for a blog post on 'climate change and
    technology'. Modify the `prompt` to match this topic and set `num_return_sequences=3`.
