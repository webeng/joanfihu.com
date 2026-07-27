---
title: "📖 Can LLMs find knowledge gaps in the Internet?"
description: "🚀 Excited to share new work on “ Harnessing Retrieval-Augmented Generation (RAG) for Uncovering Knowledge Gaps “. In this paper, I simulate how users search the Internet but instea…"
pubDate: 'Dec 21 2023'
---

🚀 Excited to share new work on “**Harnessing Retrieval-Augmented Generation (RAG) for Uncovering Knowledge Gaps**“.

In this paper, I simulate how users search the Internet but instead of searching for content that exists through traditional information retrieval methods, we search for the most relevant content, even if it doesn’t exist.

![](/uploads/2023/12/screenshot-2023-12-21-at-11.52.32.png)

Therefore, information retrieval shifts from an extraction to a generation problem.

This process is guided by the premise that a well-generalised LLM should provide useful recommendations based on the initial question and answer.

🔍 Findings:

Using Bing's web index, we found that typical internet searches hit a 'knowledge wall' just at the fifth level of topic depth. This means there's a lot more we can discover and learn!

💡 What This Means:

This research changes how we use search engines. Imagine getting deeper, more insightful answers to your questions, going beyond what's already written on the web.

More broadly, this work can be used to improve the completeness of a content library.

📚 Read & Explore:

Research paper: <https://arxiv.org/pdf/2312.07796.pdf>

Dataset and search simulations: <https://github.com/webeng/llm_knowledge_gap_finder>

Answer Engine: [AskPandi](https://askpandi.com/ask)
