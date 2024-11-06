---
layout:     post
title:      Machine Learning Internship
subtitle:   UROP at Deepwok Lab Imperial College
date:       2024-09-01
author:     TX
header-img: img/Queens-tower.png
catalog: true
lang: en
tags:
    - Pytorch
    - LLM
    - Machine Learning
    - Internship
---
### TimeLine
Apr - Sep 2024

### Project Overview
DNA language models apply techniques from natural language processing (NLP) to model biological sequences, treating DNA as a "language" to capture patterns, structures, and functional elements in genomic data. These models aim to understand and predict biological phenomena by encoding DNA sequences in a format that machine learning models can use.

Tokenization Methods: In DNA language models, tokenization is the process of breaking down DNA sequences into manageable units, or "tokens," which represent the genetic information. State-of-the-art DNA models like Hyena used a mere character-level naive tokenizer, simply translating 'A', 'C', 'G', 'T' to fixed integers. We were experimenting the adoptation of the 
Byte-Pair Encoding (BPE) method used in GPT3 and GPT4. The idea is to combine frequently occurring character pairs into single tokens iteratively, creating a hierarchy of tokens that balances between single characters and multi-character sequences.

### Contribution

Most of my work is software development on [MASE](https://github.com/jianyicheng/mase-tools), or more specific, on Machop, MASE's software stack.

**[Mase (Machine-Learning Accelerator System Exploration Tools)](https://github.com/jianyicheng/mase-tools)** , provides an efficient and scalable approach for exploring accelerator systems to compute large ML models by directly mapping onto an efficient streaming accelerator system.

1. Mase provide Command Line Interface to train a model from scratch using specified dataset. To estimate efficiency of new dataflow accelerator, I integrated RepVGG models support into Mase, organized and documented detailed procedures for future developers.

2.Exploration of the DNN hardware accelerator required hardware-software co-simulation.  I helped with scripts writing that ship metadata to the hardware team, which would helps verify the integrity of the hardware implementation and could help identify discrepancies. Scripts include: 

-  **Transform Script:** Run a transformation pass on the specified model, e.g. quantization or pruning. 
-  **Search Script:** Apply a given search strategy over a search space to optimize a specified set of hardware/software metrics.



