---
title: "Kaggle Docs QA With Gemma - Data Collection + Dataset Generation + Fine Tuning + RAG + ColBERT Re-Ranker + Evaluation"
description: "Sharing my my notebook for the Google AI Assistants For Data Task With Gemma competition. The notebook (link at the end) covers the basic building blocks to adapt LLMs for your own…"
pubDate: 'Apr 1 2024'
---

Sharing my my notebook for the [Google AI Assistants For Data Task With Gemma](https://www.kaggle.com/competitions/data-assistants-with-gemma) competition.

![](/uploads/2024/04/dallc2b7e-2024-04-01-11.17.44-an-8-bit-style-image-depicting-gemma-an-ai-assistant-designed-specifically-for-data-related-tasks.-gemma-is-visualized-as-a-charming-pixel-art-chara-1.webp)

The notebook (link at the end) covers the basic building blocks to adapt LLMs for your own use case:

- Data collection/generation/augmentation.
- Fine tuning Gemma with a P100 GPU and Lora
- Document chunking for RAG
- Chunk ranking using ColBERT and BERT/Gemma embeddings
- Evaluation using a LLM judge (Gemini Pro)
- Evaluation using a distance metric.

Here is an excerpt of the main findings so far:

Dataset generation, RAG with ColBERT and query strategy yield the best evaluation scores.

Gemma already has Kaggle knowledge out of the box so fine tuning with new data didn’t make much difference.

Fine tuning (FT) is for learning new abstractions rather than memorising new data for QA. Overfitting does help with memorisation though.

Single vector search is bad because document pooling operations throw away too much signal. ColBERT is multi-vector

so no pooling involved so signal is preserved.

Using a larger and more capable model (Gemini) as a judge is a good evaluator but pricey.

RAG + RAW: use RAG and train the model to say “I don’t know” if an answer isn’t in the context, then use the raw model as a fallback. This improves evaluation scores.

Notebook is available here: <https://www.kaggle.com/code/joanfihu/kaggle-docs-qa-fine-tuning-rag-eval>
