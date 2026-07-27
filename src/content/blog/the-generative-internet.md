---
title: "The Generative Internet"
description: "Generative AI is opening the doors to new products. It's great to witness in real time how the Internet is evolving and to imagine what it might become in the coming years. Search,…"
pubDate: 'Feb 14 2024'
---

![](/uploads/2024/02/dallc2b7e-2024-02-14-00.00.42-create-an-8-bit-style-image-representing-the-concept-of-the-generative-internet.-this-should-include-pixelated-representations-of-digital-creativity-.webp)

Generative AI is opening the doors to new products. It's great to witness in real time how the Internet is evolving and to imagine what it might become in the coming years. Search, UI navigation and content generation are the trident technologies leading this evolution.

**Search**

The Internet acts as the largest repository of knowledge worldwide. Search engines guide us through the Internet, directing us to web pages likely to have the answers we seek.

By 2014, this functionality evolved further, allowing search engines to highlight specific passages within web pages that are most likely to contain the answers to our questions. This means that search engines now fulfil both navigational and informational purposes, making it easier to find information quickly within SERPs.

![](https://blogaskpandi.files.wordpress.com/2024/02/screenshot-2024-02-13-at-01.10.40.png?w=1024)

Answer

In [2018](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), Large Language Models demonstrated a way to generate answers from the Common Crawl (CC) dataset. CC is a web index with 3B web pages. The technical breakthrough is that LLMs can retrieve relevant bits of information from all those 3B web pages. However, there are three caveats. First, LLMs can't tell what specific source has been used to generate an answer. Second, when the LLM doesn't have information about a topic, it hallucinates. Third, LLMs are not suitable to fulfil navigational intents.

In 2020, Meta introduced [RAG](https://arxiv.org/abs/2005.11401). It connects LLMs to the external data sources like the Internet so answers are grounded in sources. This is great because we can reference specific web pages and passages. However, the amount of sources that can be used to generate an answer is limited by the LLM's token context length.

![](/uploads/2024/02/screenshot-2024-01-12-at-22.23.05.png)

Answer from <https://AskPandi.com>

In 2023, the AI community gave LLMs autonomy and the concept of AI agents was born. An objective is given to an agent and it figures out what to do to complete it. This usually involves planning, multiple task execution, performing external actions, using memory, etc. For example, [AskPandi](https://AskPandi.com) is an AI search agent.

**UI Navigation**

Another advancement is in UI navigation, facilitating browser and workflow automation. This development enables us to assign tasks to an agent, which can then execute them on our behalf. As a result, we're moving from direct human-computer interaction to a more seamless human-assistant model. Here is a little example to automatically dismiss cookie consents.

https://twitter.com/joanfihu/status/1723482351533985933

**Content Generation**

We have the capability to direct a LLM to produce or modify content on our behalf, making content creation more accessible than ever. However, the key to success lies in generating content that people want. Content that lacks effort or relevance is easily recognisable and less likely to engage readers.

**The Generative Internet Is Born**

The three advancements in search, UI navigation, and content generation unlock new product opportunities. Search engines evolve into answer engines that interact with the web for us, picking only the relevant bits of information from multiple sources and composing an answer that is essentially an interactive UI.

For example, "*suggest a 5 day trip to a surf break in Europe. Also get me flight and accommodation information, including pricing*".

To complete this objective, we need to conduct multiple searches and then combine the outcomes into a single compelling answer.

But, what happens after we find the information we are looking for?

For this particular example, a natural follow-up action might be to book flights and accommodation. In this context, UI navigation proves invaluable because it allows us to instruct an AI agent to automate those tasks for us.

UI navigation facilitates workflow automation, making mundane tasks such as rescheduling a meeting, bookings, or ordering something executable in natural language. This is akin to iOS shortcuts, but without the need to write custom integrations because the web is open.

At this point, **the user rarely interacts with the web, an assistant does it for us**.

Finally, machine generated content has an important part to play because our needs to access knowledge is ever growing. In my last [research paper](https://arxiv.org/abs/2312.07796), I found out that it only takes 5 hops to find knowledge gaps on the Internet. In addition, [new research](https://gizmodo.com/google-search-results-are-getting-worse-study-finds-1851172943) has also found that our knowledge needs are outpacing the amount of content available on the public web, thus giving the impression that search engines are becoming worse. I suspect walled gardens like social media platforms have something to do with it too because their content isn't public.

**If assistants interact with the web for us, what's the point of web pages?**

Most UI navigation systems are being trained on traditional UIs so they are still relevant. In addition, there are many situations where a user will have to step in like confirm a purchase, authentication, captcha, payment details, etc.

However, interacting with the web via API calls instead of UI navigation is faster so I suspect products that provide an API to an assistant will have an edge here.

**What happens to web content creators who rely on ad-traffic?**

Ads, if relevant, are good content. Since AI assistants are very good at filtering out irrelevant content, web content creators will need to ensure that their sponsored content is also relevant.

**What's the equivalent of backlinks in a generative Internet?**

Backlinks from reputable domains are a good ranking signal in traditional search engines. However, what's the equivalent of a backlink when assistants generate unique web pages on the fly so there is no unique link to refer to? It feels there is a need for better ranking signals. I wouldn't be surprised if AEO (Answer Engine Optimisation) becomes a thing.

**What happens to social media?**

We are transitioning from information extraction to generation. This increases relevancy so good for users. I think someone will make a social network where 100% of the content is generated.

To sum up, search, UI navigation and content generation are reshaping the Internet as we know it.
