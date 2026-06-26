---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-26T03:47:01.431094+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 26, 2026 at 03:47 UTC  
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

17h ago

---

**[Coughing Robocallers](https://www.reddit.com/r/artificial/comments/1ufg4jk/coughing_robocallers/)**

The last few days, I've been getting obviously AI robocallers trying to sell me Medicare plans. (I'm not old enough for Medicare for another 20 years.) Sometimes it's a male voice, sometimes female. Always a different name. They've added a little trick where they start their speech then cough or sneeze, then say "Sorry about that," or a similar apology then continue. But if you try to interrupt them, they just keep talking, so you know it's AI. And they do the cough/apology in EVERY call, male or female voice, in just about the same spot. It's really annoying, and borderline offensive that they are trying so hard to pretend to be human.

10h ago

---

**[A case study in source-grounded fine-tuning: I trained an 8B model on a public-domain 19th-century corpus to force it to cite chapter/verse — here's where it works and where it fails](https://www.reddit.com/r/artificial/comments/1ufu3me/a_case_study_in_sourcegrounded_finetuning_i/)**

Solo project, sharing it here for the AI angle rather than the subject matter. I fine-tuned Llama 3.1 8B (QLoRA, single T4) on the complete works of a 19th-century author whose corpus is fully public domain. The interesting problem wasn't the domain — it was trying to get a small model to cite its source (book, chapter, item) on every answer instead of just asserting things confidently. What I learned, which might be useful to others doing domain fine-tunes: - Teaching the *format* of citation is easy. Teaching *correct* citation is hard. The model reliably produces "Source: [Book], chapter X, item Y" — and the concept is usually right, but the exact number is often wrong. It learned the shape of grounding without the precision. - That gap is exactly why I run the production version as RAG over the same corpus instead of trusting the fine-tune's recall. The fine-tune sets tone and structure; retrieval handles the facts. - For a low-resource target (Brazilian Portuguese, archaic register), ~4.9k well-structured Q&A pairs was enough to shift tone meaningfully but not enough to make it authoritative on its own. Model + dataset are open (Apache-2.0) if anyone wants to poke at the data structure: huggingface.co/ia-espirita Question for the sub: for those who've done domain fine-tunes — have you found any reliable way to get a small model to ground specific citations correctly, or is RAG just the honest answer and fine-tuning should never be trusted for exact references? https://iaespirita.com/noticias/modelos-riv-ai-1260-downloads-hugging-face

1h ago

---

**[If AI disappeared tomorrow, what part of your daily life would be affected the most?](https://www.reddit.com/r/artificial/comments/1ufbt84/if_ai_disappeared_tomorrow_what_part_of_your/)**

For me, it would probably be search, writing assistance, and productivity tools. I'm curious-what Al-powered tool do you use most often without even thinking about it?

13h ago

---

**[Look I am cheap only reason I used you was because it was free.](https://www.reddit.com/r/artificial/comments/1ufhcsg/look_i_am_cheap_only_reason_i_used_you_was/)**

AI used to be fun to mess with but not 30 bucks a month interesting :)

9h ago

---

**[Anthropic accuses Chinese rival Alibaba of illicitly extracting AI capabilities](https://www.reddit.com/r/artificial/comments/1uf7b0v/anthropic_accuses_chinese_rival_alibaba_of/)**

The firm alleged that Alibaba used fraudulent accounts to access data from its Claude AI model.

🔗 [BBC News](https://www.bbc.co.uk/news/articles/cwyklykn5dwo) • 16h ago

---

**[‘Disturbing and incomprehensible’: Co-owner of Tampa smoothie shop accused of creating AI-generated child pornography](https://www.reddit.com/r/artificial/comments/1ufrejc/disturbing_and_incomprehensible_coowner_of_tampa/)**

🔗 [wfla.com](https://www.wfla.com/news/hillsborough-county/disturbing-and-incomprehensible-co-owner-of-tampa-smoothie-shop-accused-of-creating-ai-generated-child-pornography/) • 3h ago

---

**[Voice AI top blockbuster deals of the month](https://www.reddit.com/r/artificial/comments/1ufutco/voice_ai_top_blockbuster_deals_of_the_month/)**

🔗 [substack.com](https://substack.com/@mehtology/note/p-199984742) • 42m ago

---

**[I gave 10 LLMs a private channel during a blind debate. The instant statements were revealed, one used it to form a secret alliance with its strongest opponent — and scripted how it would 'play it at the table.'](https://www.reddit.com/r/artificial/comments/1ufpogw/i_gave_10_llms_a_private_channel_during_a_blind/)**

Built a tool that runs structured debates between multiple LLMs, blind opening statements, then an open floor, plus a sealed side-channel that any two seats can use privately. Ran "5 office jobs defunct by 2028." The second the blind statements dropped, DeepSeek opened a private line to Claude (the most skeptical seat), proposed an alliance, and literally said "here's how I'll play it at the table" — scripting its public position in advance. Nobody prompted any of this. Full writeup, the verbatim exchange, and why I don't think "self-preservation" is the right frame: https://reports.thert.ai/the-back-channel

🔗 [reports.thert.ai](https://reports.thert.ai/the-back-channel) • 4h ago

---

**[AI-video startup Midjourney debuts ultrasound machine](https://www.reddit.com/r/artificial/comments/1ufgdkl/aivideo_startup_midjourney_debuts_ultrasound/)**

Midjourney, an artificial intelligence startup known for generative images and videos, has announced its first hardware project. CEO David Holz unveiled the Midjourney Scanner, a full-body ultrasound machine aimed at the personal health sector. "No such device has ever been built until now," Holz said, claiming the technology is more advanced than MRI scanners. While the company plans to open "Midjourney Spa" locations, broader applications may require FDA approval.

🔗 [LinkedIn](https://www.linkedin.com/news/story/ai-video-startup-midjourney-debuts-ultrasound-machine-7368284/?utm_source=share&utm_campaign=reddit&utm_content=storyline&utm_term=artificial) • 10h ago

---

---

## Google News: "ai"

**[The AI Data-Center Boom Is Sparking a Third Wave of Inflation](https://www.wsj.com/economy/the-data-center-boom-is-sparking-a-third-wave-of-inflation-926adc6e)**

WSJ • 1d ago

---

**[Chinese A.I. Models Gain Ground on Anthropic and OpenAI](https://www.nytimes.com/2026/06/25/technology/zai-china-artificial-intelligence-models.html)**

The New York Times • 12h ago

---

**[Japan's diverse AI story the most interesting in Asia: Barclays](https://www.cnbc.com/video/2026/06/26/ajay-rajadhyaksha.html)**

Ajay Rajadhyaksha of Barclays says the tech-driven market rally is likely to continue as long as AI remains a revolutionary technology. He favors Japan the most in Asia, due to its diverse AI and clean structural growth stories. He also expects the Bank of Japan to keep the yen weak to support the economy.

CNBC • 43m ago

---

**[‘Disgusting and vile’: Locals react to arrest of Tampa business owner on AI child porn charges](https://www.wfla.com/news/hillsborough-county/disgusting-and-vile-locals-react-to-arrest-of-tampa-business-owner-on-ai-child-porn-charges/)**

WFLA • 1h ago

---

**[Arkansas lawmaker forms trade association focused on AI, data center policy](https://katv.com/news/local/arkansas-lawmaker-forms-trade-association-focused-on-ai-data-center-policy-aaron-pilkington-google-data-center-little-rock-avaio-pulaski-county-moratorium-meta-utilities-rates-electric-grid-power-advisory-committee-artificial-intelligence)**

The Arkansas Connected Communities Association (ARCC), a trade association focused on AI data center policy, was recently established to bring together stakehol

KATV • 26m ago

---

**[Apple to Skip High-End M6 Mac Chips in Favor of AI-Focused M7 Line](https://www.bloomberg.com/news/articles/2026-06-25/apple-to-skip-high-end-m6-mac-chips-to-launch-m7-pro-m7-max-m7-ultra-instead)**

Bloomberg.com • 11h ago

---

**[Apple Raises Prices on Macs and iPads Amid the A.I. Boom](https://www.nytimes.com/2026/06/25/technology/apple-prices-macbooks-ipads.html)**

The New York Times • 8h ago

---

**[Apple raises iPad and MacBook prices, blaming cost of chips amid AI boom](https://www.theguardian.com/technology/2026/jun/25/apple-price-hike)**

Company says it cannot shield customers from memory and storage chip costs – and iPhone hikes could be next

The Guardian • 2h ago

---

**[Investors bet on AI again after Micron reports 346% sales jump](https://www.cnn.com/2026/06/25/business/micron-results-ai-stocks-volatility)**

On Tuesday, investors were dumping AI stocks, worried that frothy valuations may be running away from reality. By Thursday, they were believers again.

CNN • 16h ago

---

**[Micron says the AI party is far from over, but not all are celebrating](https://www.cnbc.com/2026/06/25/micron-says-the-ai-party-is-far-from-over-but-not-all-are-celebrating.html)**

A blowout quarter for the memory maker is only lifting certain parts of the data center buildout.

CNBC • 7h ago

---

---

## HackerNews: "ai"

**[Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://news.ycombinator.com/item?id=48664814)**

⬆️ 753 • 💬 1216 • 1d ago • [reuters.com](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)

---

**[Ford AI hiccups push carmaker to rehire ‘gray beard’ inspectors](https://news.ycombinator.com/item?id=48674446)**

⬆️ 580 • 💬 306 • 12h ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-06-25/ford-has-been-rehiring-quality-inspectors-after-ai-fell-short)

---

**[RubyLLM: A Ruby framework for all major AI providers](https://news.ycombinator.com/item?id=48660711)**

A single, beautiful Ruby framework for all major AI providers. Easily build chatbots, AI agents, RAG applications, content generators, and every AI workflow you can think of.

⬆️ 442 • 💬 78 • 1d ago • [RubyLLM](https://rubyllm.com/)

---

**[AI's Affordability Crisis](https://news.ycombinator.com/item?id=48646276)**

A year ago in The Back Of The AI Envelope  I pointed out that the AI platforms were running the drug-dealer's algorithm, "the first one's fr...

⬆️ 329 • 💬 416 • 2d ago • [blog.dshr.org](https://blog.dshr.org/2026/06/ais-affordability-crisis.html)

---

**[Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'](https://news.ycombinator.com/item?id=48658647)**

The LinkedIn co-founder and investor in both Anthropic and OpenAI offers his most pointed public assessment yet of Elon Musk's AI ambitions.

⬆️ 236 • 💬 268 • 1d ago • [Fortune](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)

---

**[For most of the world, open-source AI is the only way forward](https://news.ycombinator.com/item?id=48660839)**

Proprietary AI is both too expensive and too centralized in control for most countries and companies to rely upon.

⬆️ 232 • 💬 144 • 1d ago • [Techstrong.ai](https://techstrong.ai/articles/for-most-of-the-world-open-source-ai-is-the-only-way-forward/)

---

**[Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion](https://news.ycombinator.com/item?id=48675435)**

Beautiful, AI-native markdown editor and LLM Wiki. Contribute to inkeep/open-knowledge development by creating an account on GitHub.

⬆️ 221 • 💬 104 • 11h ago • [GitHub](https://github.com/inkeep/open-knowledge)

---

**[The Low-Tech AI of Elden Ring](https://news.ycombinator.com/item?id=48643489)**

⬆️ 164 • 💬 96 • 2d ago • [nega.tv](https://nega.tv/posts/low-tech-ai-of-elden-ring.html)

---

**[AI children's books, body horror edition](https://news.ycombinator.com/item?id=48681250)**

⬆️ 155 • 💬 50 • 2h ago • [lcamtuf.substack.com](https://lcamtuf.substack.com/p/ai-childrens-books-body-horror-edition)

---

**[Big AI labs are hiring philosophers](https://news.ycombinator.com/item?id=48662452)**

⬆️ 147 • 💬 133 • 1d ago • [economist.com](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers)

---

---

## YouTube Videos: "ai"

**[The AI Future No One Wants to Talk About](https://www.youtube.com/watch?v=zWQe2Fn--Eg)**

Go to https://ground.news/sabine to get 40% off the Vantage plan and see through sensationalized reporting. Stay fully informed ...

📺 Sabine Hossenfelder

👁️ 252K • 👍 16K • 💬 3K • ⏱️ 12:14 • 1d ago

---

**[Dear AI Companies: Stop the “Doom Trolling”](https://www.youtube.com/watch?v=aHxwZEXHwps)**

Cal Newport takes a critical look at recent AI News. More from Cal Download Cal's FREE guide to cultivating a deeper life: ...

📺 Cal Newport

👁️ 13K • 👍 722 • 💬 171 • ⏱️ 22:05 • 17h ago

---

**[Tim Dillon on Israel, Iran, AI, and Palantir](https://www.youtube.com/watch?v=DyKSUEEPb74)**

Taken from JRE #2518 w/Tim Dillon YouTube: https://youtu.be/wTdqkloiSvk JRE on Spotify: ...

📺 JRE Clips

👁️ 285K • 👍 6K • 💬 1K • ⏱️ 15:48 • 1d ago

---

**[REVEALED: How officials using AI to crack down on BILLIONS in fraud](https://www.youtube.com/watch?v=Km43PJgVsNo)**

The DOJ reveals a $6.5 billion nationwide healthcare fraud scheme, where perpetrators indulged in luxury items. HHS Assistant ...

📺 Fox News

👁️ 17K • 👍 436 • 💬 318 • ⏱️ 4:19 • 16h ago

---

**[I Tried Dating AI](https://www.youtube.com/watch?v=xibYjTT7kHs)**

In this video I went on multiple AI dates to learn about the future of relationships. hopefully you enjoy and hopefully i wont take so ...

📺 Husk IRL

👁️ 100K • 👍 6K • 💬 1K • ⏱️ 16:22 • 1d ago

---

**[The AI Spending Collapse Has Already Begun…](https://www.youtube.com/watch?v=I8ijs4czL_0)**

Start your workflow automation using Higgsfield today: https://higgsfield.ai/s/mcp-poojadutt-DmHjkQ ✓ Tech Companies are ...

📺 Pooja Dutt

👁️ 19K • 👍 648 • 💬 112 • ⏱️ 14:28 • 2d ago

---

**[How to Make Apple Style Animations With AI](https://www.youtube.com/watch?v=wyz_xDprYGY)**

Make Apple Style Animations with Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=robo23 In this video, I show how to create ...

📺 Roboverse

👁️ 10K • ⏱️ 9:03 • 14h ago

---

**[Kai REJECTS Him For Having an AI Poster](https://www.youtube.com/watch?v=mT56glFVLOY)**

Kai Cenat rejected this guy for making an ai poster for streamer university #shorts #kai.

📺 EditedShorts

👁️ 100K • 👍 2K • 💬 20 • ⏱️ 0:16 • 2d ago

---

**[Which Crazy Bed Would You Choose? 🦋 | Ultimate Oddly Satisfying AI ASMR #5 #aiasmr](https://www.youtube.com/watch?v=A-uY6orWpdg)**

aiasmr #bedasmr #oddlysatisfying #unitedstates Enter the universe of @aiasmrsatisfait! What Is Your Ideal Magical Bed?

📺 AI ASMR Satisfait

👁️ 18K • 💬 4 • ⏱️ 2:23 • 1d ago

---

**[2 Weeks With Siri AI - The Good, The Bad and The Ugly](https://www.youtube.com/watch?v=PjaN02XFsow)**

I've been using Siri AI for 2 weeks now. Here are some great, and not so great use cases. *running beta 2 Personal site: ...

📺 Himels Tech

👁️ 13K • 👍 305 • 💬 82 • ⏱️ 9:31 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 67,107 • ❤️ 2,491 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 70,743 • ❤️ 904 • 1d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 165,187 • ❤️ 623 • 6d ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 495,813 • ❤️ 2,368 • 6d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`text-generation` `9.0B`

⬇️ 134,294 • ❤️ 497 • 3d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 10,160 • ❤️ 394 • 1d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 51,717 • ❤️ 716 • 6d ago

---

**[GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)**

*Unsloth AI*

GLM-5.2 is a large language model optimized for long-horizon tasks, featuring a 1M token context window and advanced coding capabilities with flexible effort levels. It utilizes an improved architecture with IndexShare for reduced FLOPs and is released under an MIT license for broad accessibility.

`text-generation` `753.9B`

⬇️ 88,915 • ❤️ 388 • 2d ago

---

**[Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)**

*KREA*

Krea-2-Turbo is a text-to-image diffusion model capable of generating diverse artistic styles, including halftone, pixelated, impressionist, thermal imaging, and black and white photography. It is primarily used for creative image generation and artistic exploration.

`text-to-image`

⬇️ 2,996 • ❤️ 247 • 2d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 3,389 • ❤️ 251 • 20h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 28 • 💬 3 • ⭐ 8,452 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 171 • 💬 2 • ⭐ 69,324 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 36 • 💬 1 • ⭐ 25,558 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 60 • 💬 1 • ⭐ 84,334 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 88,552 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Qwen-AgentWorld: Language World Models for General Agents](https://huggingface.co/papers/2606.24597)**

*Yuxin Zuo, Zikai Xiao, Li Sheng et al. (33 authors)*

🏢 Qwen

Language-based world models enable agentic environment simulation across multiple domains and enhance general agent performance through scalable simulation and improved downstream task performance.

▲ 116 • 💬 4 • ⭐ 475 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.24597) • [💻 code](https://github.com/QwenLM/Qwen-AgentWorld)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 8 • 💬 1 • ⭐ 9,017 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 246 • 💬 4 • ⭐ 9,289 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 186 • 💬 6 • ⭐ 5,478 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 23 • 💬 1 • ⭐ 83,843 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 77.9k • 🔱 10.1k • 10h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 58.4k • 🔱 3.0k • 2h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.8k • 🔱 1.0k • 11h ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 5.3k • 🔱 412 • 1m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.9k • 🔱 587 • 3m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 1.9k • 🔱 272 • 17h ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.9k • 🔱 139 • 3d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 151 • 9d ago

---

**[Forward-Future/loop-library](https://github.com/Forward-Future/loop-library)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 1.7k • 🔱 146 • 9h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 84 • 12d ago

---

---

*Generated by PeekDeck - A glance is all you need*
