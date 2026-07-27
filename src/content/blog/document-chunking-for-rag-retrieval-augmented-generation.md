---
title: "Document Chunking for RAG (Retrieval Augmented Generation)"
description: "LLMs have a limited input they can generate and output. In retrieval augmented generation (RAG) applications, a set of documents is first retrieved and added to the input alongside…"
pubDate: 'Jan 13 2024'
---

![](/uploads/2024/01/dallc2b7e-2024-01-13-17.57.31-an-8-bit-style-image-depicting-a-document-being-chunked-into-smaller-pieces.-the-document-should-appear-as-a-classic-8-bit-pixelated-paper-with-visibl.png)

LLMs have a limited input they can generate and output. In retrieval augmented generation (RAG) applications, a set of documents is first retrieved and added to the input alongside an instruction, thus creating the prompt. This is referred to as in-context learning. We can draw an analogy with computer architectures here: the LLM is the CPU, the context is the RAM, and the full document library is the hard disk.

The context length (RAM) is consistently expanding. In my early encounters with Recurrent Neural Networks (RNNs), we could make reliable predictions with input lengths of about 20 words. However, issues such as vanishing gradients lead to NANs (not bread). Nowadays, we have LLMs with a context of up to 200K tokens. Note that tokenization has also evolved over time, transitioning from words to tokens.

Chunking, a technique used to divide a document into multiple parts to fit within the context, has played a pivotal role in handling these larger contexts. With a context size of 200K tokens, we can process up to 330 pages, within a single chunk for prediction.

Initially, when I began working with LLMs, chunking posed a substantial challenge. However, as the context length expanded, this problem gradually receded into the background.

**Or did it?**

It turns out that processing vast quantities of text introduces latency to the entire system. Consequently, chunking remains a relevant strategy for developing high-performance applications.

From personal experience, the choice of chunking technique depends on the user's or system's intent. For example, when summarising a document, it's necessary to consider all the chunks. Conversely, when seeking specific answers to questions, we only need to select the most relevant chunks. Now, let's look into a few chunking techniques I've used so far.

**Static Chunking**

One straightforward method of chunking involves aligning the chunk size with the LLM context length. It's important to note that if a chunk is combined with an instruction in a prompt, the chunk's length should be smaller than the context length minus the instruction length.

For instance, if the context length is 200 tokens and the instruction spans 20 tokens, the chunk's length should be set at 180 tokens.

In practice, I haven't found many use cases where this method performs exceptionally well. It appears to be most suitable for agentic systems where the agent is aware that a document is segmented into multiple chunks, relaying the decision to retrieve chunks to the agent.

**Dynamic Chunking Based On Traditional IR**

This method involves chunking a document based on a predefined condition. In my experience, the most effective approach has been to view chunking as an information retrieval (IR) problem. We can treat a document as a dataset in which each sentence serves as an item. Given a query, we retrieve a list of ranked fragments, with fragment boundaries coinciding with common sentence delimiters. Each fragment essentially becomes a chunk. This can be effortlessly achieved using ElasticSearch (ES) and BM25, ES's default ranker.

By approaching chunking as an IR problem, we can also leverage IR techniques like stemming, lemmatisation, synonymy, query expansion, and more.

This represents a straightforward, efficient, and productive dynamic chunking technique. Unlike approaches involving embedding extraction, artificial neural networks (ANN), or neural IR, this method is less resource-intensive to implement. Furthermore, it avoids the pitfalls of Out of Distribution (OOD) shifts.

**Dynamic Chunking Based On Neural IR (Embeddings)**

Similar to the previous method, this approach involves converting a document into sentence embeddings. We then retrieve relevant chunks based on the similarity between the query and sentence embeddings. While this method is more computationally demanding, it can yield more accurate results, particularly when the embeddings align closely with the application domain. Most modern databases offer support for vector indexing and search.

**Dynamic Chunking Based On Neural IR (ColBERT)**

Many vector-based search systems necessitate pooling the query and documents into a single vector. However, such pooling operations tend to discard valuable signals. [ColBERT](https://arxiv.org/pdf/2004.12832.pdf) introduces a method that eschews pooling, thereby preserving the query and document embedding signals more effectively. Additionally, since there's no need to segment documents into sentences, as in the previous method, we can automatically identify multi-sentence fragments, delimited by sentence boundaries, akin to the traditional IR approach.

However, it's worth noting that this method comes with higher computational costs and requires the implementation of the ColBERT ranker within vector databases, which not all have it out of the box. Additionally, it is not immune to OOD data shifts.

**Summary**

While the context length keeps growing, it still makes sense to do chunking to reduce latency.

There are many static and dynamic ways to do chunking. The best one will always depend on the end application.
