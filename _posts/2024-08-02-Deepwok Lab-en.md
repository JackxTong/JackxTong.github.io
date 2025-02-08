---
layout:     post
title:      Machine Learning Internship
subtitle:   UROP at Deepwok Lab Imperial College
date:       2024-09-01
author:     TX
header-img: img/Queens-tower.png
catalog: true
label: CV
tags:
    - Pytorch
    - LLM
    - Machine Learning
    - Internship
---
## ML Internship at Imperial's AI Lab [Deepwok](https://deepwok.github.io/)
Apr - Sep 2024

### Project Overview
DNA language models apply techniques from natural language processing (NLP) to model biological sequences, treating DNA as a "language" to capture patterns, structures, and functional elements in genomic data. These models aim to understand and predict biological phenomena by encoding DNA sequences in a format that machine learning models can use.

Tokenization Methods: In DNA language models, tokenization is the process of breaking down DNA sequences into manageable units, or "tokens," which represent the genetic information. State-of-the-art DNA models like Hyena used a mere character-level naive tokenizer, simply translating 'A', 'C', 'G', 'T' to fixed integers. We were experimenting the adoptation of the 
Byte-Pair Encoding (BPE) method used in GPT3 and GPT4. The idea is to combine frequently occurring character pairs into single tokens iteratively, creating a hierarchy of tokens that balances between single characters and multi-character sequences.

### Contribution
As part of the team to develop a BPE-based DNA LLM, my work mostly involves two parts.

Firstly, I worked on fine-tuning the hyperparameters like the vocab size for BPE, sequence length, context window etc for the DNA LLM. We built our model based on Olmo LLM [1B](https://huggingface.co/allenai/OLMo-1B) and [7B](https://huggingface.co/allenai/OLMo-7B).

Secondly, I mostly worked on developping a modular evaluation framework that integrates our DNA LLM with downstream tasks (e.g. gene prediction, Protein-DNA interaction prediction) and benchmarks e.g. [Genomic Benchmarks](https://github.com/ML-Bioinfo-CEITEC/genomic_benchmarks), enabling automated performance evaluations and comparisons. 

For example, this involves comparing our model's performance with [DNABERT2](https://github.com/MAGICS-LAB/DNABERT_2) and [Hyena](https://github.com/HazyResearch/hyena-dna), both were established State-of-the-Art models on Genomic Benchmarks. 
