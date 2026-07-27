---
title: "Software Engineering Has Expanded: Choosing Between Rules, Prompts, Chains, and Agents"
description: "Software engineering has expanded to solve new kinds of problems that weren’t practical before. There are 4 ways to solve problems , depending on how certain we are about the path …"
pubDate: 'Jan 1 2026'
---

![](https://joanfihu.wordpress.com/wp-content/uploads/2026/01/chatgpt-image-jan-1-2026-03_21_56-pm.jpg?w=800)

Software engineering has expanded to solve new kinds of problems that weren’t practical before.

There are **4 ways to solve problems**, depending on **how certain we are about the path to success**.

### 0) Hard rules / constraints

Use when you need **deterministic outcomes**. The result must be correct every time.  
For example, bank transactions must always transfer the required amount with 100% certainty.

### 1) Single prompt

Use when **“good enough” is acceptable** and a human (or fallback) can cover the misses.  
Best when quality is **easy to judge quickly**.

Example: Generate “related searches” suggestions for a query (good enough, quick human-like usefulness).

### 2) Chains (structured workflow)

Use when you can **decompose the problem into known, repeatable steps** and the **order of steps is known upfront**.  
Reliability comes from **checkpoints** between steps.

Example: Interpret intent → retrieve results → rerank → generate a short answer snippet with citations.

### 3) Agents (open-ended exploration)

Use when you **don’t know the steps upfront** and the work requires **discovery**.  
Best when the system must **choose what to do next** as it learns.

Example: “Help me research X” mode that iteratively searches, reads sources, refines queries, and updates the answer as it learns.

### Key rule

As you move up the ladder (toward more uncertainty), you must **increase verification**: stronger evidence, clearer checks, tighter constraints.
