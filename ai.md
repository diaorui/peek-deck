---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-23T04:24:54.065600+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 23, 2026 at 04:24 UTC  
**HTML Version:** [ai.html](https://peekdeck.ruidiao.dev/ai.html)

---

## Table of Contents

1. [Reddit: r/artificial](#reddit-rartificial)
2. [Google News: "ai"](#google-news-ai)
3. [HackerNews: "ai"](#hackernews-ai)
4. [YouTube Videos: "ai"](#youtube-videos-ai)
5. [HuggingFace Models: 🔥 Trending](#huggingface-models--trending)
6. [HuggingFace Papers: 🔥 Trending](#huggingface-papers--trending)
7. [GitHub Repositories: "ai"](#github-repositories-ai)

---

## Reddit: r/artificial

**[Microsoft Cancels Internal Anthropic Licenses As Shift To Token-Based AI Billing Blows Up Annual Budgets In Months](https://www.reddit.com/r/artificial/comments/1tkb0op/microsoft_cancels_internal_anthropic_licenses_as/)**

Summary: AGI has been cancelled due to inflation. AI has become so expensive that even Microsoft can not afford it.

🔗 [thelowdownblog.com](https://www.thelowdownblog.com/2026/05/microsoft-cancels-internal-anthropic.html) • 21h ago

---

**[LLMs are just giant probability machines pretending to think](https://www.reddit.com/r/artificial/comments/1tl59ha/llms_are_just_giant_probability_machines/)**

It’s fascinating that simple mathematics between tokens can eventually become a machine that writes essays, code, poetry, and even reasoning. We usually think probability means uncertainty. But LLMs show something strange: If probability + context + mathematical matching are scaled enough, uncertainty itself starts producing intelligent looking outputs. To understand this better, I tried breaking down an LLM from first principles using only 4 tiny training sentences. Example: The boat floated down to the bank. The investor walked into the bank to open a new account. The fisherman walked along the bank to cast his net. The bank has a vault. Then I asked: “The investor walked to the bank to lock his money in …” Why does the model predict “vault” instead of river-related words? That single question reveals almost the entire architecture of modern LLMs. The most underrated concept here is the LM Head. Most explanations immediately jump into transformers and attention, but almost nobody explains that the LM Head is essentially a gigantic token vocabulary containing all possible next token candidates the model can output. So internally the model is basically solving: “Out of all known tokens, which one best matches this context mathematically?” Then different layers help solve that problem: Embeddings: convert words into mathematical vectors Positional encoding: preserves word order Attention layer: figures out which words are related to each other in context (“investor”, “money”, “bank” become strongly connected) https://preview.redd.it/wxmpf00g7t2h1.jpg?width=2299&format=pjpg&auto=webp&s=a214113263cf008a759740474fbda4e0b8394ba5 Feed forward neural networks: act somewhat like massive learned if/else decision systems refining patterns internally And finally the LM Head converts all of that into probabilities for the next token. What surprised me most is: There is no hidden magic moment where the AI “becomes conscious”. It’s an enormous probability engine continuously finding the best contextual token match from its vocabulary. I made a beginner-friendly walkthrough explaining this visually without unnecessary jargon. https://www.youtube.com/watch?v=YTV5qUCpu2c Would genuinely love feedback from people learning transformers/LLMs from scratch.

40m ago

---

**[Rethinking AI Bubble](https://www.reddit.com/r/artificial/comments/1tkb6p9/rethinking_ai_bubble/)**

For those worried about the AI Bubble bursting, it's not happening, at least for now, not until atleast OpenAI and Anthropic are listed (later this year). And if you actually discount Nvidia, and check the PE of AI companies right now OpenAI (35x) and anthropic (13x), these valuations do not really seem unsustainable as of now, and not to mention unlike the DotCom bubble, they have massive data centre infrastructure, so this is all not in the air. AI is here to stay, it's already altering our lives, taking up workspaces and transforming work, there is a massive upfront cost but that does not immediately signal a bubble unfolding. If any bubble bursts, it would not be solely the AI Bubble, it would be the government bonds and the dollar bubble. Edit: I wrote the post hastily, sorry for writing Valuation/Revenue as PE.

21h ago

---

**[Interesting Response from Gemini](https://www.reddit.com/r/artificial/comments/1tk3y45/interesting_response_from_gemini/)**

I had a simple google search turn up the most random useless results so I asked: “Why is google search so bad now?” on google and got a surprisingly honest response from Gemini. Even highlighted the profits part lol

1d ago

---

**[I built a cognitive architecture where the AI has actual needs that drift between sessions — not prompt engineering, actual state variables](https://www.reddit.com/r/artificial/comments/1tl0o5v/i_built_a_cognitive_architecture_where_the_ai_has/)**

Most AI companions fake continuity through prompt engineering. PHI // DRIFT does something different — seven homeostatic state variables that drift between sessions and shape output before you say a word. Memory is scored by emotional salience and time decay, not just vector similarity. There's a Jungian shadow module tracking unintegrated behavioral patterns as a first-class architectural variable. Built solo in 9 months on a CPU-only mini tower. No GPU. No institution. Full preprint under review of SSRN The field ignores depth psychology as an engineering input. I think that's a mistake. github avalable if needed

4h ago

---

**[The deployment funnel nobody talks about: 60% evaluate, 20% pilot, 5% ship. MIT tracked 300 real AI implementations against profit metrics.](https://www.reddit.com/r/artificial/comments/1tky191/the_deployment_funnel_nobody_talks_about_60/)**

Late 2025, MIT researchers measured something the industry had avoided looking at directly. Not projections or pilot numbers. Documented outcomes from 300 AI deployments in real businesses, tracked against profit metrics. The funnel breaks down like this. Sixty percent of companies evaluated AI tools. Of those, twenty percent ran a pilot. Of those pilots, only 5% reached full production deployment on the service line. Ninety-five percent of AI investment dissolved before it produced a measurable outcome. The companies that made it to production had a clear pattern. They didn't ask AI to substitute for judgment. They identified bounded tasks: specific inputs, defined outputs, failure modes that were contained. They measured success criteria before deployment, not after. Content drafting. Code review. Data summarisation at volume. The 95% that didn't make it: haste, no defined success metrics, and the assumption that efficiency gains would be obvious once the tool was in the workflow. There's a line from the research worth sitting with. "We replaced X employees with AI" isn't an efficiency metric. It's a headcount metric. Those are not the same thing. Klarna is already in the reversal phase, rehiring humans after the AI efficiency numbers didn't hold up at scale. What's the clearest signal you've found for whether a deployment is actually working, before it's too late to course-correct?

5h ago

---

**[AI Can Provide Constructive Feedback on Your Written Work. You Just Need to Understand a Little Bit of Psychology. Same Exact Thing Applies to Human Feedback](https://www.reddit.com/r/artificial/comments/1tko3tm/ai_can_provide_constructive_feedback_on_your/)**

Good feedback from AI is not that different from receiving feedback from people around you. My brother and I once threw a lot of money into a proof-of-concept film because we were blinded by the encouragement and agreeableness that people around us were expressing. We weren't recognizing that they were just trying to be nice to us and not hurt our feelings. They were active screenwriters and filmmakers just like us and just like us, they would need our help when the time came. That's why all of our feedback was watered down heavily. Only one of our friends told us the truth and you know what we did? We respectively ignored the advice. Film-wise, it turned out great because the team was amazingly talented. But the story fell significantly short of what it could have been, if only we had turned our egos off for a second and insist that people give us their complete, gloves-off opinion. It's the same when engaging with AI, but actually easier to handle since you're just working with your own mental barriers instead of two. Bottom line. You just gotta come into it with the understanding that it will be a yes man. You can do prompting and that can really help if you design it well, but even then, it pales in comparison to a guy like Dov Siemen who is hilariously legendary when it comes to wrecking screenplays and bursting people's bubbles. That's honestly why I don't often ask for it's opinion. Instead, I might ask it to compare a scene to all the other movies that are out there and spot the cliches. If I ask questions with the implicit assumption that whatever I wrote is garbage, it'll riff off of that and assume with me, which causes it to focus less on justifying why my story is so great and more on what could be wrong. It's the same with people. If you simply ask for their input, they'll water it down with praise. You have to specifically instruct people to find the problems and emphasize the truth over hurting your feelings. Do the same with AI and you'll have far less problems with feedback. So, don't ask questions like, "Is this good?" or "Will people understand this?" Ask questions like, "This dialogue is terrible. How can we fix it." or "This scene feels draggy and boring. We need to find what's missing." Come into it with the assumption that your work is poor, even if it isn't. Force it to identify the problems. Otherwise, it'll suck your....Well, you know.

11h ago

---

**[AI training is becoming the new coding revolution](https://www.reddit.com/r/artificial/comments/1tke8wl/ai_training_is_becoming_the_new_coding_revolution/)**

I genuinely think people are underestimating how fast AI training is becoming accessible. A few years ago training a useful model sounded like something only OpenAI, Google, or Meta could do. Now random developers are renting GPUs for a few dollars an hour, fine tuning open models from their bedrooms, building datasets with APIs, and getting surprisingly good results. The biggest shift isn’t even the models themselves, it’s the removal of gatekeeping around experimentation. Once regular people can train specialized reasoning, coding, or teaching models without billion dollar infrastructure, the AI industry changes completely. We’re slowly moving from “only corporations can build intelligence” to “small teams can build focused intelligence better than giant companies in specific niches.”

18h ago

---

**[Claude made me realize most AI models optimize for confidence, not truth](https://www.reddit.com/r/artificial/comments/1tke1cj/claude_made_me_realize_most_ai_models_optimize/)**

People keep talking about benchmarks, censorship, refusals, personality, and “which AI is smarter,” but almost nobody talks about truthfulness in a practical way. Honestly, one thing I noticed while testing different models for coding, reasoning, and long conversations is that Claude sometimes feels less optimized to impress and more optimized to stay internally consistent. It doesn’t always give the fastest or most hyped answer, but there are moments where it genuinely feels like it’s trying to preserve logical honesty instead of just sounding confident. A lot of models today are insanely good at presentation, tone, and making the user feel satisfied, but that creates a weird problem where sounding intelligent can become more important than actually being correct. The scary part is that as AI gets more human-like, most people probably won’t even notice the difference between confidence and truth anymore. I think in the next few years the real competition won’t just be intelligence, it’ll be which model people trust when the answer actually matters.

18h ago

---

**[For those that follow the AI tech improvements, how long do you predict till AI will be capable of instantly Language Dubing Animes?](https://www.reddit.com/r/artificial/comments/1tkuf4b/for_those_that_follow_the_ai_tech_improvements/)**

For those that follow the AI tech improvements, how long do you predict till AI will be capable of instantly Language Dubing Animes? Animes usually take a long time to dub into a different language. I been wondering if AI can help smooth that issue out by making a dub of the Anime within hours to near instantly. How long y'all think it will take till we get to that point with AI were it's capable of doing that?

8h ago

---

---

## Google News: "ai"

**[Ask AI or just Google it? Google makes a big change to a little search box](https://www.npr.org/2026/05/22/nx-s1-5829915/google-search-box-ai)**

The search giant is updating its famously minimalist homepage. But what looks like a tiny design change is a very big deal.

NPR • 9h ago

---

**[You can no longer Google the word ‘disregard’](https://techcrunch.com/2026/05/22/you-can-no-longer-google-the-word-disregard/)**

After Google Search's AI update, the word "disregard" now effectively breaks the search interface.

TechCrunch • 12h ago

---

**[Even If You Hate AI, You Will Use Google AI Search](https://www.wired.com/story/even-if-you-hate-ai-you-will-use-google-ai-search/)**

The search giant’s AI-crafted answers are so convenient, you’ll be sucked in—to the detriment of the web and the artists and thinkers behind it.

WIRED • 13h ago

---

**[Microsoft reports are exposing AI's real cost problem: Using the tech is more expensive than paying human employees](https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/)**

Companies are racing to incentivize employees to use AI. But as some companies are finding, the more employees that use the technology, the heavier the bill.

Fortune • 11h ago

---

**[How Nvidia’s US$3.2 Billion AI Optics Pact At Corning (GLW) Has Changed Its Investment Story](https://finance.yahoo.com/markets/stocks/articles/nvidia-us-3-2-billion-031859221.html)**

Nvidia recently agreed to invest up to US$3.20 billion in Corning through a warrant deal to expand Corning’s U.S. optical connectivity manufacturing capacity for AI data centers, deepening their collaboration on scaling high‑performance optical solutions. This partnership effectively positions Corning as a core supplier at the physical layer of AI infrastructure, tying its long-term prospects more closely to the buildout of next‑generation data centers. We’ll now examine how Nvidia’s...

Yahoo Finance • 1h ago

---

**[Trump posts AI video depicting him throwing Colbert in a dumpster and dancing](https://thehill.com/homenews/administration/5892405-trump-shares-ai-video-colbert/)**

The Hill • 2h ago

---

**[Video: Donald Trump Tosses Stephen Colbert In Dumpster Before YMCA Dance In AI-Generated Clip](https://www.ndtv.com/world-news/watch-donald-trump-tosses-stephen-colbert-in-dumpster-before-ymca-dance-in-ai-generated-clip-11535601)**

US President Donald Trump shared an AI-generated video mocking Stephen Colbert after "The Late Show" ended.

NDTV • 2h ago

---

**[Trump attacks Colbert (literally) in stupid AI video | Opinion](https://www.yahoo.com/entertainment/tv/articles/trump-attacks-colbert-literally-stupid-040312404.html)**

Donald Trump posted another AI-generated video, this time one in which he attacks the former "Late Show" host. Stephen Colbert. It's crazy, and sad.

Yahoo • 21m ago

---

**[AI used to fake evidence that ended Korean actor's career, say police](https://www.bbc.com/news/articles/c0r2j18k2vxo)**

Police are seeking an arrest warrant for a YouTuber who allegedly fabricated evidence to defame actor Kim Soo-hyun.

BBC • 17h ago

---

**[Pope: Church must restore ‘trust in technology,’ guide people to Christ](https://www.vaticannews.va/en/pope/news/2026-05/pope-leo-xiv-audience-vatican-artificial-intelligence-conference.html)**

Meeting with participants in a Vatican conference on artificial intelligence, Pope Leo XIV encourages efforts to educate people about AI while leading ...

Vatican News • 16h ago

---

---

## HackerNews: "ai"

**[AI is just unauthorised plagiarism at a bigger scale](https://news.ycombinator.com/item?id=48222383)**

AI takes in all the input, whether the original authors have consented or not, and do some "learning", and then the AI companies sell these learned result to...

⬆️ 810 • 💬 719 • 1d ago • [Axel's blog](https://axelk.ee/ai-is-just-unauthorised-plagiarism-at-a-bigger-scale/)

---

**[Throwing AI-generated walls of text into conversations](https://news.ycombinator.com/item?id=48219992)**

Stop throwing AI-generated walls of text into conversations. If they wanted an AI essay, they would have asked ChatGPT themselves.

⬆️ 678 • 💬 414 • 1d ago • [noslopgrenade.com](https://noslopgrenade.com/)

---

**[Steve Wozniak cheered after telling students they have AI – actual intelligence](https://news.ycombinator.com/item?id=48233563)**

Apple cofounder Steve Wozniak's speech about AI at Grand Valley State University earlier this month got a laugh and applause from graduates.

⬆️ 604 • 💬 507 • 19h ago • [Business Insider](https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5)

---

**[College students drown out AI-praising commencement speeches with boos](https://news.ycombinator.com/item?id=48206241)**

Arizona students reject ex-Google exec's positive words on AI

⬆️ 375 • 💬 381 • 2d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/college-students-drown-out-ai-praising-commencement-speeches-with-boos-deal-with-it-one-speaker-fires-back-as-students-heckle-positive-pitches-for-ais-role)

---

**[Shunning AI is the human choice](https://news.ycombinator.com/item?id=48222366)**

LinkedIn may be awash with boosters, but shunning AI is the human choice.

⬆️ 366 • 💬 534 • 1d ago • [The Handbasket](https://www.thehandbasket.co/p/hating-ai-is-good-actually)

---

**[Google’s AI is being manipulated. The search giant is quietly fighting back](https://news.ycombinator.com/item?id=48205782)**

A BBC investigation revealed a simple way to get AI chatbots to spit out misinformation. Google and other AI companies are now trying to fix the problem.

⬆️ 336 • 💬 211 • 2d ago • [bbc.com](https://www.bbc.com/future/article/20260519-google-tackles-attempts-to-hack-its-ai-results)

---

**[AI has a multiplying effect on existing technical skills](https://news.ycombinator.com/item?id=48235526)**

Friendly articles and tutorials for front-end web developers. ❤️

⬆️ 294 • 💬 284 • 15h ago • [joshwcomeau.com](https://www.joshwcomeau.com/email/wham-launch-005-elephant-2-p/)

---

**[Intuit to lay off over 3k employees to refocus on AI](https://news.ycombinator.com/item?id=48216278)**

In a memo to employees, CEO Sasan Goodarzi said the layoffs are meant to reduce complexity, simplify the company's corporate structure, and deliver better AI products.

⬆️ 258 • 💬 190 • 2d ago • [TechCrunch](https://techcrunch.com/2026/05/20/intuit-to-lay-off-over-3000-employees-to-refocus-on-ai/)

---

**[Samsung chip workers will get an average $340k bonus as AI profits soar](https://news.ycombinator.com/item?id=48230892)**

The South Korean chipmaker struck a last-minute deal with its union to avert an 18-day strike, unlocking a $26.6 billion payout pool

⬆️ 249 • 💬 194 • 1d ago • [Quartz](https://qz.com/samsung-chip-workers-bonus-ai-profits-052126)

---

**[The Companies Cutting Headcount for AI Will Lose to the Ones Who Didn't](https://news.ycombinator.com/item?id=48234547)**

Organisations using AI to cut headcount are making a short-term trade with long-term consequences. The ones holding their teams together and investing in how those teams operate with AI are building something more durable.

⬆️ 198 • 💬 188 • 16h ago • [libertas.software](https://libertas.software/en/knowledge-hub/19/the-companies-cutting-headcount-for-ai-will-lose-to-the-ones-who-didnt)

---

---

## YouTube Videos: "ai"

**[AI Just Crossed The Line We Were Afraid Of: Continual Harness](https://www.youtube.com/watch?v=qCFyprzrCvA)**

Princeton researchers just revealed Continual Harness, a self-improving AI system that learns while it is already running.

📺 AI Revolution

👁️ 11K • 👍 734 • 💬 84 • ⏱️ 13:31 • 5h ago

---

**[Joe Rogan accidentally exposed AI in four words](https://www.youtube.com/watch?v=waFl4uBfXRA)**

Token mania. I've been a user of Proton for almost a decade and I'm grateful to them for agreeing to sponsor this video. Proton ...

📺 Mo Bitar

👁️ 127K • 👍 8K • 💬 1K • ⏱️ 11:39 • 13h ago

---

**[Google’s AI endgame is here… everything you missed at I/O 2026](https://www.youtube.com/watch?v=9OQ5vaYbGV0)**

Try using Emergent's specialized agents in parallel to build any full-stack application ...

📺 Fireship

👁️ 320K • 👍 12K • 💬 736 • ⏱️ 5:44 • 11h ago

---

**[Anthropic Just Reset AI Expectations](https://www.youtube.com/watch?v=9N3jEavj5Ps)**

Anthropic delivered one of the most consequential weeks any AI lab has had yet: Andrej Karpathy joined to work on ...

📺 The AI Daily Brief: Artificial Intelligence News

👁️ 10K • 👍 260 • 💬 25 • ⏱️ 21:56 • 1d ago

---

**[Ex-Google CEO just exposed the whole AI sh*tshow](https://www.youtube.com/watch?v=XSxki8gaWHk)**

Just say yes! https://x.com/@atmoio https://x.com/jasonscheer/status/2055748401783083293 ...

📺 Mo Bitar

👁️ 210K • 👍 10K • 💬 2K • ⏱️ 6:42 • 2d ago

---

**[The Real Reason They&#39;re Racing To Build AI?](https://www.youtube.com/watch?v=ivLy_73u8C8)**

In this vlog, I dive into one of the most unsettling ideas I've explored during my involuntary early retirement: Could humanity be ...

📺 Asian Dad Energy

👁️ 15K • 👍 815 • 💬 449 • ⏱️ 13:29 • 1d ago

---

**[AI Didn’t Break Education. It Exposed The Lie](https://www.youtube.com/watch?v=R0XVocLKR68)**

Princeton will now require instructors in exam rooms for the first time since 1893. The stated trigger is artificial intelligence, but ...

📺 House of El - AI

👁️ 52K • 👍 4K • 💬 1K • ⏱️ 18:48 • 2d ago

---

**[The Odds: Are Americans concerned about AI replacing jobs?](https://www.youtube.com/watch?v=C4RPb3L5Ifo)**

CNN's Sara Sidner and chief data analyst Harry Enten examine the evolving landscape facing college graduates as they enter the ...

📺 CNN

👁️ 23K • 👍 475 • 💬 125 • ⏱️ 4:08 • 7h ago

---

**[Stanford student explains how AI impacted his graduating class](https://www.youtube.com/watch?v=17b87k8rhd0)**

A recent opinion piece in The New York Times spotlighted the impact of artificial intelligence on the 2026 graduating class at one ...

📺 CBS News

👁️ 102K • 👍 1K • 💬 316 • ⏱️ 4:55 • 1d ago

---

**[Google&#39;s New Gemini Omni Is Too Much.](https://www.youtube.com/watch?v=zc1_YAi7scA)**

Google I/O 2026 dropped Gemini Omni, a world-model that simulates physics, edits video, and might be the largest AI video leap ...

📺 AI For Humans

👁️ 13K • 👍 628 • 💬 117 • ⏱️ 27:58 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model (3B parameters) supporting image/video understanding, generation, and editing, trained from scratch with a multi-task synergy approach.

`any-to-any`

⬇️ 1,001 • ❤️ 652 • 11h ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 37,545 • ❤️ 583 • 4d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 221,612 • ❤️ 905 • 3d ago

---

**[Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)**

*Tencent*

Hy-MT2-1.8B is a fast, multilingual translation model supporting 33 languages, optimized for on-device deployment with 1.25-bit quantization (440MB storage, 1.5x speedup). It excels in general, business, and instruction-following translation tasks, outperforming mainstream commercial APIs.

`translation` `2.0B`

⬇️ 564 • ❤️ 281 • 23h ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) optimized for extracting structured information from videos. It excels at generating dense scene+event captions with precise timestamps and resolving natural language queries to specific temporal spans within videos, making it ideal for applications requiring detailed video understanding and temporal grounding.

`video-text-to-text` `2.2B`

⬇️ 4,002 • ❤️ 252 • 2d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 1,249,582 • ❤️ 1,273 • 1d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model based on the Hierarchical Reasoning Model (HRM) architecture, featuring dual-timescale Transformer modules for unbounded compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning/math with a 'synth,cot' composite condition, though it is a pre-alignment model not suited for direct chat use.

`text-generation` `1.2B`

⬇️ 72,470 • ❤️ 245 • 1d ago

---

**[Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)**

*Tencent*

Hy-MT2-30B-A3B is a large-scale, "fast-thinking" Mixture-of-Experts (MoE) translation model supporting 33 languages. It excels in general, business, domain-specific, and instruction-following translation tasks, outperforming leading open-source models and commercial APIs.

`translation` `30.1B`

⬇️ 224 • ❤️ 246 • 23h ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 532,255 • ❤️ 416 • 2d ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 466,060 • ❤️ 336 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 79 • 💬 3 • ⭐ 78,594 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 64,536 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://huggingface.co/papers/2605.18678)**

*Fengyi Fu, Mengqi Huang, Shaojin Wu et al. (13 authors)*

🏢 bytedance-research

Lance is a unified multimodal model that combines understanding, generation, and editing capabilities for images and videos through collaborative multi-task training and a dual-stream architecture.

▲ 71 • 💬 4 • ⭐ 766 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18678) • [💻 code](https://github.com/bytedance/Lance) • [🔗 project](https://lance-project.github.io/)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,291 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 120 • 💬 10 • ⭐ 10,394 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation](https://huggingface.co/papers/2605.19833)**

*Zhifei Xie, Kaiyu Pang, Haobin Zhang et al. (7 authors)*

🏢 National University of Singapore

Mega-ASR framework improves robustness in real-world speech recognition through compound-data construction and progressive acoustic-to-semantic optimization techniques.

▲ 125 • 💬 2 • ⭐ 319 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.19833) • [💻 code](https://github.com/xzf-thu/Mega-ASR) • [🔗 project](https://xzf-thu.github.io/Mega-ASR/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 8 • 💬 0 • ⭐ 18,469 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 74,544 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 4 • 💬 1 • ⭐ 5,532 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[L2P: Unlocking Latent Potential for Pixel Generation](https://huggingface.co/papers/2605.12013)**

*Zhennan Chen, Junwei Zhu, Xu Chen et al. (10 authors)*

Latent-to-Pixel transfer paradigm efficiently leverages pre-trained latent diffusion models to create pixel-space models with minimal training overhead and high-resolution generation capabilities.

▲ 30 • 💬 1 • ⭐ 73 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2605.12013) • [💻 code](https://github.com/TencentYoutuResearch/T2I-L2P) • [🔗 project](https://nju-pcalab.github.io/projects/L2P/)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 4.6k • 🔱 479 • 22h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.4k • 🔱 1.0k • 5d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.6k • 🔱 175 • 5h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.3k • 🔱 383 • 1d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.2k • 🔱 340 • 5d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 1.9k • 🔱 416 • 1d ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.8k • 🔱 208 • 15d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.7k • 🔱 181 • 1d ago

---

**[Nutlope/hallmark](https://github.com/Nutlope/hallmark)**

Anti-AI-slop design skill for Claude Code, Cursor, and Codex.

`CSS`

⭐ 1.6k • 🔱 108 • 2d ago

---

**[Open-Less/openless](https://github.com/Open-Less/openless)**

Hold a key, speak, release — AI-polished text appears at your cursor in any app. Open-source voice input for macOS & Windows. (按住快捷键说话，松开即得润色后的文字)

`HTML` `ai-prompt` `asr` `dictation` `llm` `macos`

⭐ 1.5k • 🔱 129 • 3h ago

---

---

*Generated by PeekDeck - A glance is all you need*
