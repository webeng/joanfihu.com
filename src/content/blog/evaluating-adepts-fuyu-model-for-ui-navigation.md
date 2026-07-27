---
title: "How can Adept's FUYU be used for  UI Navigation?"
description: "Adept's mission to enable computers to interact with UIs will enhance our productivity and save time. I have been eagerly awaiting their ACT-1 model for quite some time. However, w…"
pubDate: 'Oct 19 2023'
---

Adept's mission to enable computers to interact with UIs will enhance our productivity and save time.

I have been eagerly awaiting their ACT-1 model for quite some time. However, while that is being developed, they have released FUYU, a multimodal LLM or MLMM. The term 'multimodal' implies its ability to process both text and images. More here: https://www.adept.ai/blog/fuyu-8b.

Adept has introduced an architectural simplification that eliminates the need for the image encoder.

> Image patches are instead linearly projected into the first layer of the transformer, bypassing the embedding lookup. We simply treat the normal transformer decoder like an image transformer (albeit with no pooling and causal attention).
>
> https://www.adept.ai/blog/fuyu-8b

Eliminating the need to scale or crop images to meet certain specifications is a significant advantage. This has profound implications for UI navigation, especially since aspect ratios are not always consistent. For instance, 5:1 aspect ratios are frequently seen on web pages. Traditional image preprocessing often discards too much valuable information.

However, a notable limitation is its variable memory requirements, which led me to frequently encounter out-of-memory (OOM) errors. To address the issue of non-uniform aspect ratios, I segmented the images and placed each segment side-by-side to achieve a consistent aspect ratio.

Interestingly, when I fed screenshots of web pages to GPT-4V, I faced OOM errors with images that also had irregular aspect ratios. This leads me to speculate whether GPT-4V might operate on a decoder-only model.

On the plus side, FUYU is relatively lightweight. It comfortably fits within an AWS g5.2xlarge instance that offers 24GB GPU memory. The only modification I made was to adjust the precision to float16 to ensure smooth operation

*model = FuyuForCausalLM.from\_pretrained(pretrained\_path, device\_map="cuda:0", torch\_dtype=torch.float16)*

I've assessed FUYU with a focus on UI navigation capabilities, even though this may not align with its original training purpose. While one could argue that this is not an equitable evaluation, FUYU remains the best open-source model available for UI navigation. With Adept's mission in mind, it's anticipated that their models will, in time, exhibit specialised capabilities for UI navigation, much like FUYU's resolution-agnostic feature. This assessment establishes a foundation, highlighting areas where fine-tuning and future models can concentrate.

I've captured screenshots of various UIs from mobile websites and posed questions about them. This article will specifically discuss the screenshot from Amazon presented below.

![](/uploads/2023/10/amazon_screenshot-2.png)

**Generate A Web Page Caption**

**prompt:** Generate a caption.

**generation**: The image shows a screen shot of a "sunnyscopa" product listing, which features "free delivery by amazon". The screen shot also includes the "home & kitchen" tab, where the user has selected "sunnyscopa waterslide decal paper for laser printer - clear, a4, 100 sheets - personalized waterslide decal paper

**comment**: The caption seems to focus on the text in the screenshot. No comments about the other visual components nor the page layout.

**VQA based on text in images**

This model is good at doing VQA based on text in images. This is presumably due to the OCR capabilities that this model posses.

**prompt**: What's the price of the product?

**generation**: Sunnyscopa Waterslide Decal Paper for Laser Printer - Clear, A4, 100 Sheets - Personalized Waterslides

**comment**: Maybe my prompt was to challenging here. I assumed that because there is only one product listed and one price, the model would figure it out.

---------------------------------------------

**prompt**: What is the price of the sunnyscopa product?

**generation**: 79.72

**comment**: The model got the price right whenever I included the product name in the prompt

**VQA based on elements in images**

**prompt**: What it's in the product thumbnail?

**generation**: Joan joan amazon

**comment**: It didn't understand what a product thumbnail is.

**VQA based on Spatial Awareness**

This was the area that I was looking forward the most because UI navigation requires spatial awareness. This means that the model needs to understand how the UI components are laid out and what the UI components are for. For example, buttons can have icons as well as text and they lead the user to a new web page state.

**prompt**: What is the colour of the search button?

**generation**: orange

**comment**: Good, the model understands what is a button and has figured out that the magnifying glass means search.

---------------------------------------------

**prompt**: What's the text in the search box?

**generation**: The search box displays an advertisement for a waterslide decal paper for laser printers.

**comment**: Ok there are no ads in the search box... Maybe the model is confusing the search result listing as an autocomplete dropdown?

---------------------------------------------

**prompt**: Where is the Amazon logo located?

**generation**: bottom

**comment**: It's at the top left

---------------------------------------------

**prompt**: Where is the Amazon logo located? Generate bounding box coordinates.

**generation**: SunnySCOPA Waterslide Decal Paper for Laser Printer - Clear, A4, 100 Sheets - Personalized Waterproof Paper

**comment**: Incorrect. Being able to generate coordinates to locate any element in an image will be necessary. Adept's has teased this capability for text but it will also be necessary for other UI components too. The blog post mentions this capability. This will be great.

**UI Interactivity Awareness**

In this scenario we want to check if the model is aware of the interactive elements in the web page. Interactivity awareness is essential for UI navigation

**prompt**: "Given this web page screenshot from the Amazon mobile site, what should I do next if I am searching for a water bottle?

**generation**: In the Amazon app, you can search for Sunnyscopa Waterslide Decal Paper for Laser Printer - Clear, A4, 100 Sheets - Personalized Water Bottle Label. If you can find the product, simply tap or click "GET IT" button.

**comment**: The model understood that you need to go to an app, search for things and tap or click to buy it. The model is aware of mobile/touchscreen vs. desktop by referencing tap (mobile) and click (desktop) . However, it swept through the screenshot to do the reasoning. The right answer would have been along the lines:

- Delete the current text in the search box
- Type "water bottle"
- Click/Tap on the orange search button

---------------------------------------------

**prompt**: What will happen if I click on Joan?

**generation**: You can now print the Joan ad.

**comment**: The model doesn't understand that a menu or new page with user settings will open up.

****UI Interactivity Awareness**** **With Markers**

![](/uploads/2023/10/screenshot-2023-10-19-at-17.31.13.png)

Adding markers to the images helps the model to provide more concise references when generating an output. Some new research in this direction: https://som-gpt4v.github.io/

**prompt**: I've taken a screenshot of a web page. The web page has the following interactive elements #text\_input\_1, #button\_1 and #button\_2. I'm looking for a water bottle, what actions should I take next?

**generation**:1. Select the "Sunnyscopa Waterslide Decal Paper for Laser Printer - Clear, A4, 100 Sheets - Personalized Water Bottle Label" from the available options.\n2. Select the "Joan" option from the available options.\n3. Select the "Free Delivery by Amazon".....

**comment**: Adding anchors strengthens the communication between modalities (text-image, image-text) but it ads the overhead of having to do image segmentation and tagging. It did not seem to help in our case.

**Summary**

Overall, this open-source foundation MLMM is commendable. However, it requires some fine-tuning for UI navigation. I anticipate that Adept will release a UI navigation model soon.

I conducted similar tests with GPT-4V, and it performed well overall. Nonetheless, it's not an equitable comparison, as GPT-4V has undergone more extensive QA and refinement, and it is closed-source.
