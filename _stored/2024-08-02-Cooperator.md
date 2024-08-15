---
layout:     post
title:      Cooperator - Fully automated github repo translator
subtitle:   2024 Summer Project 
date:       2024-05-02
author:     JY
header-img: img/post-bg-rwd.jpg
catalog: true
tags:
    - Django
    - Sqlite
    - LLM
    - Azure
    - Github
---

# Co-Operator: Automated Repository Management

## Overview

**Co-Operator** is an innovative GitHub application designed to streamline repository management. By leveraging advanced Language Models (LMs), the app automates tasks such as localization and static code analysis, significantly reducing manual effort and enhancing efficiency for development teams.

## Problem Statement

Localization is essential for making large code repositories accessible to developers globally. This process traditionally involves labor-intensive tasks, including copying, translating images, documents, and code examples. **Co-Operator** aims to automate these processes to save time and increase productivity.

## Methodology

### Developer Interaction
Developers interact with the system via GitHub's interface or the command line, providing input such as code files, documentation, and other relevant information.

### Input Analysis
The system analyzes the input using advanced language modeling techniques to understand its meaning and relationships.

### Task Automation
Automated techniques perform code analysis and documentation translation based on the analysis results.

### Feedback & Adjustment
Users review the system-generated output and provide feedback. The system adjusts until the output meets the desired standards.

### Output Generation
The system generates processed code files, dependency lists, and other outputs. This process iterates to handle continuously changing code and dependency relationships.

### Repository Update
Once confirmed, the system synchronizes the updated content to the code repository.

## Features and Benefits

### Easy Installation
- Simple setup for installing the Co-Operator GitHub App on repositories.

### Automated Translations
- Automatically translates documents and images in the repository into multiple languages, enhancing global accessibility.

### Code Improvement Suggestions
- Suggests code refactoring during pull requests to reduce human error.

### Continuous Updates
- Monitors and updates automatically with repository changes, ensuring documentation remains current without manual re-translation.

### GitHub Workflow Integration
- Fully integrates with existing GitHub workflows for smooth collaboration.

### Customizable Settings
- Allows configuration of languages and models used for each language.

## Workflow

The Co-Operator works on a separate branch, mirroring the main branch. It makes pull requests with documentation and translation changes for developers to approve before merging.

## Future Work

- **Multilingual Models**: Use dedicated multilingual models for translating code suggestions and using code-focused models for code analysis.
- **Image and Code Analysis**: Implement models for translating images and analyzing code in-depth.
- **Quality Score**: Introduce a gamification element by assigning a quality score for each translation to encourage higher-quality contributions.
- **Enhanced UI**: Update the UI using Microsoft's Fluent UI framework.

## Technologies Used

- **Django**
- **React**
- **tailwindcss**
- **Azure AI Studio**
- **OpenAI**
- **Python**
- **Semantic Kernel**
- **SQLite**
- **GitHub**

## Conclusion

The **Co-Operator** GitHub App represents a significant leap forward in repository management by automating tedious and time-consuming tasks. This automation not only accelerates development processes but also ensures high-quality code and documentation, making it an invaluable tool for developers worldwide.

---

**Contributors**:
- Lee Stott, Korey Stegard-Pace
- Yash Belur, Yazan Ayyoub, Dr. Ayush Bhandari (Supervisor)
- Renwei Liu, Junyi Wu, Han Jang, Timothy Chung
