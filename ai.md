---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-25T13:36:32.197123+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 25, 2026 at 13:36 UTC  
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

**[Claude Fable 5 may return today after 13-day government-forced suspension](https://www.reddit.com/r/artificial/comments/1uf5pzu/claude_fable_5_may_return_today_after_13day/)**

Here’s the full timeline: -June 9: Anthropic releases Claude Fable 5, their most powerful public model ever (Mythos-class with safeguards) -June 12: US government issues an export control directive at 5:21 PM, ordering Anthropic to cut off access to ALL foreign nationals. Model goes offline worldwide within 90 minutes -The reason? Amazon engineers reportedly found a narrow jailbreak that could bypass Fable’s cybersecurity classifiers -Anthropic complied but publicly pushed back, calling the action unfair -Trump met Dario Amodei at the G7 and softened his stance, but the directive was never officially lifted -June 26 (today): Congressional deadline for Commerce Secretary Lutnick to respond in writing about the export controls Prediction markets are pricing ~57% odds of restoration before July 1. Developers have been stuck on Opus 4.8 this whole time. This whole situation raises a serious question: if a government can pull your AI model offline in 90 minutes, what does that mean for anyone building on closed, hosted models?

3h ago

---

**[Anthropic accuses Chinese rival Alibaba of illicitly extracting AI capabilities](https://www.reddit.com/r/artificial/comments/1uf7b0v/anthropic_accuses_chinese_rival_alibaba_of/)**

The firm alleged that Alibaba used fraudulent accounts to access data from its Claude AI model.

🔗 [BBC News](https://www.bbc.co.uk/news/articles/cwyklykn5dwo) • 2h ago

---

**[Opus 4.8 The Worst Claude Ever](https://www.reddit.com/r/artificial/comments/1ueqjvq/opus_48_the_worst_claude_ever/)**

I have worked with most all of Anthropics LLM's for development, but hands down Opus 4.8 has caused me more grief, aggravation, and it lies in every thing it does - especially near context mid-load and if you're doing deterministic work with no heuristics constraints you can't trust a thing out of it. So I stopped using it a while back, but today I had to do a container rebuild and in VS it slipped back into Opus 4.8 from Sonnet. And without even realizing the switch happen I could tell about a 1/3 of the way in into developing complex code it started arguing with me - I was about to loose it when I remembered the crap from the past and sure enough when I check the model... well you get the picture.... I was wondering if anyone else had similar experience with Opus 4.8 too?

16h ago

---

**[We chased a hallucinated quote through 30k training records, 4,600 transcripts, and our own system prompt. Turned out to be two separate bugs](https://www.reddit.com/r/artificial/comments/1ueaya4/we_chased_a_hallucinated_quote_through_30k/)**

Some of our customers noticed Inter-1 (our omni-modal social-signal model) would occasionally "hear" a quote that didn't exist. Feed it a video with zero audio and ask what was said, and it would sometimes report: "Yeah, Friday at five." Verbatim. Same line, every time. We assumed it had to be baked into the training data somewhere, so we went looking everywhere: 30,960 training records with datetime mentions → zero hits on the phrase 4,603 video transcripts → zero hits ~800 inference probes, 584 storage objects → zero hits Turns out the phrase was sitting in our own system prompt — a worked example we'd written to show the model the expected output format, buried in a version our GEPA prompt-optimizer had shipped. But that only explained where the words came from, not why the model would say them over total silence. So we ran two ablations in our internal eval harness: Swap the word, keep the model: changed the prompt's example to "Tuesday at noon." Fabrication rate went up (37%→50%), and the invented quote tracked the swap exactly — Friday→Tuesday. Swap the model, keep the prompt: ran the same byte-identical prompt through larger variants and an earlier checkpoint of our own model. They barely fabricated (0–2%). Only the further-post-trained Inter-1 confabulated at ~12%. So it's not one bug, it's two stacked priors: the prompt supplied the script, but post-training is what gave the model the compulsion to recite something rather than report silence. Deleting the prompt example stops that one sentence — it doesn't stop the model from inventing different dialogue instead. We think this is a textual/in-context variant of the audio-visual "Clever Hans effect" that's been documented for vision priors (model writes "thud" over a silent skateboard wipeout) — except ours shows the same reflex gets worded by whatever's nearest in the context window, which a vision-only diagnostic wouldn't catch. Full writeup with the fabrication-rate forest plot and log data: https://www.interhuman.ai/blog/goblin-yeah-friday-at-five

1d ago

---

**[After Anthropic shutdown, China's Z.ai closes frontier gap as it plans dual listing](https://www.reddit.com/r/artificial/comments/1uf88ul/after_anthropic_shutdown_chinas_zai_closes/)**

Chinese AI company Z.ai (formerly Zhipu AI) says its new GLM-5.2 model is now performing close to leading models from OpenAI and Anthropic on coding and AI agent benchmarks. The company claims the model delivers competitive results at a much lower cost and has been optimized to run on domestic Chinese hardware, including Huawei chips. Z.ai is also planning a dual listing in Hong Kong and Shanghai to fund its long-term AGI ambitions. The news comes as China's AI sector continues to narrow the gap with leading U.S. AI labs despite ongoing restrictions on advanced chip access. Are we entering a world where frontier AI is no longer dominated by a handful of U.S. companies?

🔗 [reuters.com](https://www.reuters.com/world/asia-pacific/after-anthropic-shutdown-chinas-zai-closes-frontier-gap-it-plans-dual-listing-2026-06-25/) • 1h ago

---

**[6 years into this career and I finally stopped solving communication problems with code](https://www.reddit.com/r/artificial/comments/1uf7zpw/6_years_into_this_career_and_i_finally_stopped/)**

We had a legacy endpoint crawling under load. Two years ago I would've spent a week fixing it myself. Instead I looked at the logs, saw an team was hammering it with a cron job, and sent their dev a Slack message asking if they still needed that data. Got an answer the next day, a simple no and they turned off the job. Latency dropped. Problem solved The embarrassing part is how many times I've probably dove headfirst into a problem that could be solved with communication Has anyone else noticed this becoming more obvious the longer they're in the industry? where people try to fix communication problem with code?

1h ago

---

**[AMD contributes ONNX Runtime backend to FFmpeg DNN filter](https://www.reddit.com/r/artificial/comments/1uf7vli/amd_contributes_onnx_runtime_backend_to_ffmpeg/)**

An AMD engineer has contributed to the upstream FFmpeg library an ONNX Runtime back-end for its DNN filter

🔗 [phoronix.com](https://www.phoronix.com/news/FFmpeg-DNN-ONNX-Runtime) • 1h ago

---

**[Are our AI models getting dumber/lazier - how do AI companies determine what is "sufficient thinking"?](https://www.reddit.com/r/artificial/comments/1ufa2g0/are_our_ai_models_getting_dumberlazier_how_do_ai/)**

Sorry if this comes across as a rant, I just came off a frustrating session with my LLM, who tries to be "smart" by assuming that their mode of thinking is "sufficient" for my requirement. I recalled in 2024/2025, which new model brought a new excitement to the users than the previous version - "you mean the model can do this now?" Now, it is the inverse - "you mean the models are trying to optimise itself?" Flexible thinking on the pretext of saving tokens, while increasing the cost of the tokens for the newer models. My past models used to be able to search across chats and folders proactively, and be able to infer my intent even before I ask it explicitly. It frequently surprises me with the unexpected insights. I used to enjoy reading its thoughts, how it formulates its reply to my query. Now I can't see its thinking, and it gets it wrong frequently, because it assumes its answer is good enough. I gave the new models a long document to read, and it skim and give me a shoddy answer, until I explicitly challenge it ("that is not right!"). It will not volunteer to read the document carefully (but if it does, it will tell you explicitly "let me read the document carefully before responding to you" - hello - that is your job - you need to read it carefully regardless!) Now it even asked me to repeat to it what my past prompts are, unless I ask it to search explictly, it will just sit on its a**, on the pretext of saving tokens. And the selection of "low", "med", "high", etc thinking levels. If we got it wrong, we have to restart the query on a higher setting, wasting more tokens. What has been your experience in this? How is this better customer experience? At this moment, the models are becoming useless for daily use, despite scoring higher and higher on benchmarks. I think the time may be coming where humans have to underlearn this technology and go back to the pre-AI days, before we lose all our cognitive abilities. To all the AI expert/engineers out there - how does the latest AI model know what is enough of an answer to my query? Especially in a new chat, they don't even know me well enough or my question in detail? Is it through multiple wasted tokens - "that is not good enough", "that is wrong", etc, that it finally get to the required answer? I hope some AI companies' execs recognize this and one of them will take action. Or is that too much to hope for?

7m ago

---

**[How to maintain consistent context across ChatGPT, Claude, and other AI tools](https://www.reddit.com/r/artificial/comments/1uf9818/how_to_maintain_consistent_context_across_chatgpt/)**

The core problem with using multiple AI models is that each one only knows what you tell it in that specific conversation. Switch to a different model and you're re-briefing from scratch. By the time you've caught Claude up on what ChatGPT already knows, you've lost ten minutes and half the momentum. Worse, they end up with different versions of your project because you explained it slightly different ways, so you get contradicting outputs. Most people handle this in one of three ways. The first is manual context passing. You keep a master document of your project, decisions, everything that matters, and you paste it into each model before you start. This works in theory but in practice the document gets outdated as your project evolves, you forget to update it, and you end up pasting stale context. Each model ends up with a slightly different picture of what you're doing. The second is picking one primary model and treating others as specialists. Claude for reasoning, ChatGPT for speed, whatever. You keep your main context there and only switch when you need something specific. This cuts down on fragmentation but you're capped by one model's strengths and if you want to run something in parallel across models, you're back to manual context management. The third is keeping everything in a unified workspace that connects to multiple models. Use for example Notebooks App for this, dumping their docs, videos, research, everything into one place, then feeding that into whichever model they're using that day. The pro is genuinely singular source of truth, you're not re-explaining the project to each model, and when you switch models you're always working from the same context so the outputs stay consistent. The con is it's another tool running, and you have to actually use it instead of half-assing notes into scattered docs. But the ones who stick with it say the compounding is real because each model is actually building on the same material instead of working in a silo. What ends up working best is usually a hybrid. One primary model where most of your context lives, a couple secondaries for specific tasks, but everything anchored to a single source instead of letting context scatter across conversations. The real unlock isn't which models you use, it's whether you have one place that holds everything and actually pull from it instead of rebuilding in each chat.

41m ago

---

**[Automate multi-source Research and Report Generation](https://www.reddit.com/r/artificial/comments/1uf7vx7/automate_multisource_research_and_report/)**

In this demo, I show how to use Row-Bot for a practical research workflow: taking a research question, combining recent web research with an uploaded client context document, creating a structured briefing, exporting it as a PDF, and drafting an email with the report attached. We start by configuring the tools needed for the workflow: web search, URL reading, the Documents library, PDF export, Gmail, and the Deep Research skill. Then we run an end-to-end scenario where Row-Bot prepares a client-ready briefing on how AI agents can help small business operations. The key idea is that Row-Bot does not just generate generic answers. It can combine public information with your own private documents and turn the result into a useful deliverable. Open Source and Local-First

1h ago

---

---

## Google News: "ai"

**[Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)**

Reuters • 16h ago

---

**[Anthropic accuses Chinese rival Alibaba of illicitly extracting AI capabilities](https://www.bbc.com/news/articles/cwyklykn5dwo)**

The firm alleged that Alibaba used fraudulent accounts to access data from its Claude AI model.

BBC • 10h ago

---

**[Alibaba Group Holding (BABA) Is Down 7.1% After Pentagon Suit And AI Misuse Claims Surface](https://finance.yahoo.com/technology/ai/articles/alibaba-group-holding-baba-down-070913513.html)**

In recent days, Alibaba Group has sued the U.S. Department of Defense to challenge its designation as a Chinese military-linked company, while also facing accusations from Anthropic that operators tied to its Qwen AI lab illicitly accessed Claude AI models through large-scale misuse of fake accounts. Together, these legal and AI-related controversies intensify regulatory and reputational pressure on Alibaba at a time when its cloud and artificial intelligence ambitions are central to its...

Yahoo Finance • 6h ago

---

**[$500 million AI jobs push launches with bipartisan backing](https://www.politico.com/news/2026/06/25/500-million-ai-jobs-push-launches-with-bipartisan-backing-00975439)**

Politico • 4h ago

---

**[Brown University gets a seat at Raimondo’s $500 million AI table](https://www.bostonglobe.com/2026/06/25/metro/brown-university-workforce-raise-us-ai/)**

The partnership links Brown’s new Workforce Development Policy Lab with RAISE US, a nonprofit launched by Raimondo and former Indiana governor Eric Holcomb.

The Boston Globe • 42m ago

---

**[The New Push to Ready Millions for AI Career Upheaval](https://www.wsj.com/lifestyle/careers/the-new-push-to-ready-millions-for-ai-career-upheaval-dfb04cc5)**

WSJ • 4h ago

---

**[Exclusive: Nebulock raises $25M for AI threat hunting](https://www.axios.com/pro/enterprise-software-deals/2026/06/25/nebulock-threat-hunting-cybersecurity)**

Axios • 10m ago

---

**[IBM stock pops as company unveils chip 'the size of a fingernail' in AI push](https://finance.yahoo.com/markets/article/ibm-stock-pops-as-company-unveils-chip-the-size-of-a-fingernail-in-ai-push-130640214.html)**

IBM soared in pre-market trading after announcing a non-chip computing breakthrough.

Yahoo Finance • 29m ago

---

**[Google Revamps New AI Coding Strike Team Amid Struggle to Catch Up With Anthropic](https://www.theinformation.com/articles/google-revamps-new-ai-coding-strike-team-amid-struggle-catch-anthropic)**

Google is reorganizing its recently launched strike team working on AI coding tools to try to catch up with Anthropic in the most lucrative AI applications, according to people familiar with the changes. The goal is for the months-old strike team to change the approach to training Google’s AI ...

The Information • 36m ago

---

**[Opinion | There’s One Clear Reason Why Americans Are Gloomy About A.I.](https://www.nytimes.com/2026/06/25/opinion/ai-americans-pessimism.html)**

The New York Times • 8h ago

---

---

## HackerNews: "ai"

**[Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://news.ycombinator.com/item?id=48664814)**

⬆️ 556 • 💬 909 • 17h ago • [reuters.com](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)

---

**[RubyLLM: A Ruby framework for all major AI providers](https://news.ycombinator.com/item?id=48660711)**

A single, beautiful Ruby framework for all major AI providers. Easily build chatbots, AI agents, RAG applications, content generators, and every AI workflow you can think of.

⬆️ 410 • 💬 70 • 22h ago • [RubyLLM](https://rubyllm.com/)

---

**[AI's Affordability Crisis](https://news.ycombinator.com/item?id=48646276)**

A year ago in The Back Of The AI Envelope  I pointed out that the AI platforms were running the drug-dealer's algorithm, "the first one's fr...

⬆️ 328 • 💬 415 • 1d ago • [blog.dshr.org](https://blog.dshr.org/2026/06/ais-affordability-crisis.html)

---

**[Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'](https://news.ycombinator.com/item?id=48658647)**

The LinkedIn co-founder and investor in both Anthropic and OpenAI offers his most pointed public assessment yet of Elon Musk's AI ambitions.

⬆️ 232 • 💬 263 • 1d ago • [Fortune](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)

---

**[For most of the world, open-source AI is the only way forward](https://news.ycombinator.com/item?id=48660839)**

Proprietary AI is both too expensive and too centralized in control for most countries and companies to rely upon.

⬆️ 218 • 💬 142 • 22h ago • [Techstrong.ai](https://techstrong.ai/articles/for-most-of-the-world-open-source-ai-is-the-only-way-forward/)

---

**[The Low-Tech AI of Elden Ring](https://news.ycombinator.com/item?id=48643489)**

⬆️ 162 • 💬 96 • 2d ago • [nega.tv](https://nega.tv/posts/low-tech-ai-of-elden-ring.html)

---

**[Big AI labs are hiring philosophers](https://news.ycombinator.com/item?id=48662452)**

⬆️ 141 • 💬 129 • 20h ago • [economist.com](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers)

---

**[Meta pauses AI training program tracking employee keystrokes after internal leak](https://news.ycombinator.com/item?id=48636632)**

Meta pauses an AI training program after sensitive employee data leaks, sparking internal backlash and highlighting security concerns.

⬆️ 123 • 💬 31 • 2d ago • [Business Insider](https://www.businessinsider.com/meta-ai-training-data-leak-exposed-employee-activity-across-company-2026-6)

---

**[AI Built a Nuke and Still Lost](https://news.ycombinator.com/item?id=48641927)**

Either AI is ready to help run a country, or it can't be trusted with a board game. The honest answer is both.

⬆️ 89 • 💬 98 • 2d ago • [lwilko.com](https://www.lwilko.com/blog/i-gave-an-ai-a-civilization)

---

**[Haystack: Open-Source AI Framework for Production Ready Agents, RAG](https://news.ycombinator.com/item?id=48658095)**

Create agentic, context engineered AI systems using Haystack’s modular and customizable building blocks, built for real-world, production-ready applications.

⬆️ 87 • 💬 21 • 1d ago • [Haystack](https://haystack.deepset.ai/)

---

---

## YouTube Videos: "ai"

**[The AI Future No One Wants to Talk About](https://www.youtube.com/watch?v=zWQe2Fn--Eg)**

Go to https://ground.news/sabine to get 40% off the Vantage plan and see through sensationalized reporting. Stay fully informed ...

📺 Sabine Hossenfelder

👁️ 196K • 👍 13K • 💬 3K • ⏱️ 12:14 • 22h ago

---

**[Meta’s AI Clusterf*ck Is Humiliating Zuckerberg](https://www.youtube.com/watch?v=SFZ9ZlNyljc)**

In this video, I break down what is happening inside Meta: the layoffs, the collapsing employee morale, the AI restructuring chaos, ...

📺 House of El - AI

👁️ 91K • 👍 8K • 💬 1K • ⏱️ 24:31 • 21h ago

---

**[We Asked AI To Simulate If The U.S. Had A Second Civil War](https://www.youtube.com/watch?v=OdxH1KZbjOY)**

What would happen if Civil War broke out in the United States again in 2026? Thankfully, with modern AI technology, we no ...

📺 The Babylon Bee

👁️ 160K • 👍 17K • 💬 2K • ⏱️ 2:31 • 1d ago

---

**[China&#39;s Free AI Just Embarrassed Claude.. ](https://www.youtube.com/watch?v=8xkYrUz3Iuc)**

China just released a FREE open AI model that's shaking up the entire AI industry. In this week's AI Updates, we break down ...

📺 Your AI Guy

👁️ 9K • 👍 251 • 💬 50 • ⏱️ 15:48 • 12h ago

---

**[Tim Dillon on Israel, Iran, AI, and Palantir](https://www.youtube.com/watch?v=DyKSUEEPb74)**

Taken from JRE #2518 w/Tim Dillon YouTube: https://youtu.be/wTdqkloiSvk JRE on Spotify: ...

📺 JRE Clips

👁️ 226K • 👍 5K • 💬 1K • ⏱️ 15:48 • 20h ago

---

**[I Tried Dating AI](https://www.youtube.com/watch?v=xibYjTT7kHs)**

In this video I went on multiple AI dates to learn about the future of relationships. hopefully you enjoy and hopefully i wont take so ...

📺 Husk IRL

👁️ 52K • 👍 4K • 💬 870 • ⏱️ 16:22 • 17h ago

---

**[21,000 Oracle Employees Just Got Replaced by AI](https://www.youtube.com/watch?v=JdMIdaGG7EQ)**

Oracle just axed 21000 jobs. Why? Start your FREE Intro Course with CourseCareers NOW!

📺 Mark Savant

👁️ 8K • 👍 321 • 💬 159 • ⏱️ 11:58 • 1d ago

---

**[AI glasses are creating a cheating problem](https://www.youtube.com/watch?v=R6WdmGwflRE)**

With the rapid development in AI-powered wearables, educators in East Asia are scrambling to deal with cheating students who ...

📺 CNN

👁️ 16K • 👍 440 • 💬 26 • ⏱️ 1:09 • 5h ago

---

**[The AI Spending Collapse Has Already Begun…](https://www.youtube.com/watch?v=I8ijs4czL_0)**

Start your workflow automation using Higgsfield today: https://higgsfield.ai/s/mcp-poojadutt-DmHjkQ ✓ Tech Companies are ...

📺 Pooja Dutt

👁️ 18K • 👍 614 • 💬 105 • ⏱️ 14:28 • 1d ago

---

**[MIT Just Revealed the AI Bubble&#39;s Fatal Flaw](https://www.youtube.com/watch?v=3ESclFr8m7I)**

How I Became a Sovereign Professional - The Freelance Formula https://www.brendandell.com/freelance-formula-299 Currently ...

📺 Brendan Dell 

👁️ 253K • 👍 8K • 💬 2K • ⏱️ 22:04 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 67,107 • ❤️ 2,426 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 70,743 • ❤️ 827 • 1d ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 495,813 • ❤️ 2,323 • 6d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 165,187 • ❤️ 571 • 6d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`text-generation` `9.0B`

⬇️ 134,294 • ❤️ 427 • 3d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 51,717 • ❤️ 706 • 5d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 10,160 • ❤️ 352 • 21h ago

---

**[GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)**

*Unsloth AI*

GLM-5.2 is a large language model optimized for long-horizon tasks, featuring a 1M token context window and advanced coding capabilities with flexible effort levels. It utilizes an improved architecture with IndexShare for reduced FLOPs and is released under an MIT license for broad accessibility.

`text-generation` `753.9B`

⬇️ 88,915 • ❤️ 370 • 1d ago

---

**[Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)**

*KREA*

Krea-2-Turbo is a text-to-image diffusion model capable of generating diverse artistic styles, including halftone, pixelated, impressionist, thermal imaging, and black and white photography. It is primarily used for creative image generation and artistic exploration.

`text-to-image`

⬇️ 2,996 • ❤️ 221 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 3,520,206 • ❤️ 2,219 • 2mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 27 • 💬 1 • ⭐ 7,206 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 36 • 💬 1 • ⭐ 25,507 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 170 • 💬 2 • ⭐ 68,952 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 60 • 💬 1 • ⭐ 84,119 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 88,369 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 246 • 💬 4 • ⭐ 9,251 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 8 • 💬 1 • ⭐ 8,825 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 186 • 💬 6 • ⭐ 5,445 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 23 • 💬 1 • ⭐ 83,731 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 44 • 💬 4 • ⭐ 31,227 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 77.7k • 🔱 10.1k • 17h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 57.1k • 🔱 2.9k • 23h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.7k • 🔱 1.0k • 1h ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 5.3k • 🔱 403 • 1d ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.8k • 🔱 572 • 2m ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.5k • 🔱 437 • 3d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.2k • 🔱 213 • 3d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.9k • 🔱 137 • 2d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 150 • 9d ago

---

**[Forward-Future/loop-library](https://github.com/Forward-Future/loop-library)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 1.6k • 🔱 141 • 13h ago

---

---

*Generated by PeekDeck - A glance is all you need*
