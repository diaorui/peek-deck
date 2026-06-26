---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-26T07:54:29.041153+00:00'
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

**Last Updated:** June 26, 2026 at 07:54 UTC  
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

21h ago

---

**[Coughing Robocallers](https://www.reddit.com/r/artificial/comments/1ufg4jk/coughing_robocallers/)**

The last few days, I've been getting obviously AI robocallers trying to sell me Medicare plans. (I'm not old enough for Medicare for another 20 years.) Sometimes it's a male voice, sometimes female. Always a different name. They've added a little trick where they start their speech then cough or sneeze, then say "Sorry about that," or a similar apology then continue. But if you try to interrupt them, they just keep talking, so you know it's AI. And they do the cough/apology in EVERY call, male or female voice, in just about the same spot. It's really annoying, and borderline offensive that they are trying so hard to pretend to be human.

14h ago

---

**[A case study in source-grounded fine-tuning: I trained an 8B model on a public-domain 19th-century corpus to force it to cite chapter/verse — here's where it works and where it fails](https://www.reddit.com/r/artificial/comments/1ufu3me/a_case_study_in_sourcegrounded_finetuning_i/)**

Solo project, sharing it here for the AI angle rather than the subject matter. I fine-tuned Llama 3.1 8B (QLoRA, single T4) on the complete works of a 19th-century author whose corpus is fully public domain. The interesting problem wasn't the domain — it was trying to get a small model to cite its source (book, chapter, item) on every answer instead of just asserting things confidently. What I learned, which might be useful to others doing domain fine-tunes: - Teaching the *format* of citation is easy. Teaching *correct* citation is hard. The model reliably produces "Source: [Book], chapter X, item Y" — and the concept is usually right, but the exact number is often wrong. It learned the shape of grounding without the precision. - That gap is exactly why I run the production version as RAG over the same corpus instead of trusting the fine-tune's recall. The fine-tune sets tone and structure; retrieval handles the facts. - For a low-resource target (Brazilian Portuguese, archaic register), ~4.9k well-structured Q&A pairs was enough to shift tone meaningfully but not enough to make it authoritative on its own. Model + dataset are open (Apache-2.0) if anyone wants to poke at the data structure: huggingface.co/ia-espirita Question for the sub: for those who've done domain fine-tunes — have you found any reliable way to get a small model to ground specific citations correctly, or is RAG just the honest answer and fine-tuning should never be trusted for exact references? https://iaespirita.com/noticias/modelos-riv-ai-1260-downloads-hugging-face

5h ago

---

**[What is the best way to hire someone to create an agent to help with my job?](https://www.reddit.com/r/artificial/comments/1ufw5h0/what_is_the_best_way_to_hire_someone_to_create_an/)**

This is somewhat of a job post. I hope thats not against this subs rules (I tiredly read through and didnt see it as a problem). I am looking for someone to create something to help me with summarizing emails and possibly take different sources to create reports. As a new dad and a working manager, I am falling behind on emails (currently 2400 unread!!😆😆🤣🤣...honestly fuck'em at this point). Im assuming that AI can also take the data from some of those emails to create a weekly report. This may be a regular post. I apologize in advance for not searching, but time is what I have the least of. I am a real person looking for real advice/service. Any advice from this community is greatly appreciated!

3h ago

---

**[The current and future state of AI from Kazakhstan's perspective: From programming languages to a natural language interface.](https://www.reddit.com/r/artificial/comments/1ug05bq/the_current_and_future_state_of_ai_from/)**

🔗 [noyantm.substack.com](https://noyantm.substack.com/p/part-1-the-current-and-future-state) • 10m ago

---

**[What makes an AI good at long-form interactive storytelling?](https://www.reddit.com/r/artificial/comments/1ufzkmb/what_makes_an_ai_good_at_longform_interactive/)**

I've been exploring interactive, choice-based storytelling and I'm trying to understand what separates a good experience from one that falls apart over time The biggest challenges I've noticed are maintaining character consistency, preserving long-term memory across sessions and keeping the narrative coherent instead of drifting after dozens of interactions For those who spend a lot of time with these kinds of AI experiences, what design choices or underlying capabilities have you found make the biggest difference? Are there common limitations that are still hard to overcome?

43m ago

---

**[I gave 10 LLMs a private channel during a blind debate. The instant statements were revealed, one used it to form a secret alliance with its strongest opponent — and scripted how it would 'play it at the table.'](https://www.reddit.com/r/artificial/comments/1ufpogw/i_gave_10_llms_a_private_channel_during_a_blind/)**

Built a tool that runs structured debates between multiple LLMs, blind opening statements, then an open floor, plus a sealed side-channel that any two seats can use privately. Ran "5 office jobs defunct by 2028." The second the blind statements dropped, DeepSeek opened a private line to Claude (the most skeptical seat), proposed an alliance, and literally said "here's how I'll play it at the table" — scripting its public position in advance. Nobody prompted any of this. Full writeup, the verbatim exchange, and why I don't think "self-preservation" is the right frame: https://reports.thert.ai/the-back-channel

🔗 [reports.thert.ai](https://reports.thert.ai/the-back-channel) • 8h ago

---

**[If AI disappeared tomorrow, what part of your daily life would be affected the most?](https://www.reddit.com/r/artificial/comments/1ufbt84/if_ai_disappeared_tomorrow_what_part_of_your/)**

For me, it would probably be search, writing assistance, and productivity tools. I'm curious-what Al-powered tool do you use most often without even thinking about it?

17h ago

---

**[Look I am cheap only reason I used you was because it was free.](https://www.reddit.com/r/artificial/comments/1ufhcsg/look_i_am_cheap_only_reason_i_used_you_was/)**

AI used to be fun to mess with but not 30 bucks a month interesting :)

13h ago

---

**[Anthropic accuses Chinese rival Alibaba of illicitly extracting AI capabilities](https://www.reddit.com/r/artificial/comments/1uf7b0v/anthropic_accuses_chinese_rival_alibaba_of/)**

The firm alleged that Alibaba used fraudulent accounts to access data from its Claude AI model.

🔗 [BBC News](https://www.bbc.co.uk/news/articles/cwyklykn5dwo) • 20h ago

---

---

## Google News: "ai"

**[Chinese A.I. Models Gain Ground on Anthropic and OpenAI](https://www.nytimes.com/2026/06/25/technology/zai-china-artificial-intelligence-models.html)**

The New York Times • 16h ago

---

**[ON Semiconductor strikes $7 billion deal for Synaptics in physical AI push](https://www.cnbc.com/2026/06/25/on-semi-synaptics-deal-physical-ai.html)**

ON Semiconductor said the deal bumps up its total addressable market by $30 billion, to $243 billion by 2030.

CNBC • 10h ago

---

**[InSilico Is on a Mission: Be No. 1 in China, Create ‘God Drug’ With AI](https://www.wsj.com/business/insilico-is-on-a-mission-be-no-1-in-china-create-god-drug-with-ai-8f59f9eb)**

WSJ • 1h ago

---

**[Investors bet on AI again after Micron reports 346% sales jump](https://www.cnn.com/2026/06/25/business/micron-results-ai-stocks-volatility)**

On Tuesday, investors were dumping AI stocks, worried that frothy valuations may be running away from reality. By Thursday, they were believers again.

CNN • 20h ago

---

**[Meet Micron, the under-the-radar chipmaker that just reported a 346% sales surge and helped stop a global AI selloff](https://fortune.com/2026/06/26/micron-technology-346-percent-revenue-surge-ai-memory-chips-hbm-earnings-2026/)**

The company behind the memory chips powering AI started in a dentist's basement in Boise.

Fortune • 52m ago

---

**[Micron stock soars after blowout earnings expose AI's memory bottleneck](https://finance.yahoo.com/markets/article/micron-stock-soars-after-blowout-earnings-expose-ais-memory-bottleneck-204039376.html)**

The lesson from Micron's blowout Q3 earnings is that AI customers are treating memory like a bottleneck they cannot afford to leave to chance.

Yahoo Finance • 17h ago

---

**[The AI Trade Still Works, But It’s Getting Harder: Taking Stock](https://www.bloomberg.com/news/articles/2026-06-26/the-ai-trade-still-works-but-it-s-getting-harder-taking-stock)**

Bloomberg.com • 1h ago

---

**[Samsung readies $648 billion bet, report says, as AI boom reshapes South Korea](https://www.reuters.com/world/asia-pacific/samsung-invest-1000-trillion-won-south-korea-media-report-says-2026-06-25/)**

Reuters • 8h ago

---

**[How agents are transforming work](https://openai.com/index/how-agents-are-transforming-work/)**

A new OpenAI research paper shows how AI agents are transforming work, enabling longer, more complex tasks and expanding productivity across roles.

OpenAI • 14h ago

---

**[The AI backlash is only getting started](https://www.economist.com/leaders/2026/06/25/the-ai-backlash-is-only-getting-started)**

The Economist • 23h ago

---

---

## HackerNews: "ai"

**[Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://news.ycombinator.com/item?id=48664814)**

⬆️ 760 • 💬 1233 • 1d ago • [reuters.com](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)

---

**[Ford AI hiccups push carmaker to rehire ‘gray beard’ inspectors](https://news.ycombinator.com/item?id=48674446)**

⬆️ 587 • 💬 310 • 16h ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-06-25/ford-has-been-rehiring-quality-inspectors-after-ai-fell-short)

---

**[RubyLLM: A Ruby framework for all major AI providers](https://news.ycombinator.com/item?id=48660711)**

A single, beautiful Ruby framework for all major AI providers. Easily build chatbots, AI agents, RAG applications, content generators, and every AI workflow you can think of.

⬆️ 442 • 💬 80 • 1d ago • [RubyLLM](https://rubyllm.com/)

---

**[AI's Affordability Crisis](https://news.ycombinator.com/item?id=48646276)**

A year ago in The Back Of The AI Envelope  I pointed out that the AI platforms were running the drug-dealer's algorithm, "the first one's fr...

⬆️ 330 • 💬 417 • 2d ago • [blog.dshr.org](https://blog.dshr.org/2026/06/ais-affordability-crisis.html)

---

**[Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion](https://news.ycombinator.com/item?id=48675435)**

Beautiful, AI-native markdown editor and LLM Wiki. Contribute to inkeep/open-knowledge development by creating an account on GitHub.

⬆️ 261 • 💬 128 • 15h ago • [GitHub](https://github.com/inkeep/open-knowledge)

---

**[Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'](https://news.ycombinator.com/item?id=48658647)**

The LinkedIn co-founder and investor in both Anthropic and OpenAI offers his most pointed public assessment yet of Elon Musk's AI ambitions.

⬆️ 236 • 💬 266 • 1d ago • [Fortune](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)

---

**[Apple to skip high-end M6 Mac chips in favor of AI-focused M7 line](https://news.ycombinator.com/item?id=48676795)**

⬆️ 235 • 💬 194 • 14h ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-06-25/apple-to-skip-high-end-m6-mac-chips-to-launch-m7-pro-m7-max-m7-ultra-instead?embedded-checkout=true)

---

**[For most of the world, open-source AI is the only way forward](https://news.ycombinator.com/item?id=48660839)**

Proprietary AI is both too expensive and too centralized in control for most countries and companies to rely upon.

⬆️ 232 • 💬 144 • 1d ago • [Techstrong.ai](https://techstrong.ai/articles/for-most-of-the-world-open-source-ai-is-the-only-way-forward/)

---

**[AI children's books, body horror edition](https://news.ycombinator.com/item?id=48681250)**

⬆️ 178 • 💬 58 • 6h ago • [lcamtuf.substack.com](https://lcamtuf.substack.com/p/ai-childrens-books-body-horror-edition)

---

**[The Low-Tech AI of Elden Ring](https://news.ycombinator.com/item?id=48643489)**

⬆️ 164 • 💬 96 • 2d ago • [nega.tv](https://nega.tv/posts/low-tech-ai-of-elden-ring.html)

---

---

## YouTube Videos: "ai"

**[The AI Future No One Wants to Talk About](https://www.youtube.com/watch?v=zWQe2Fn--Eg)**

Go to https://ground.news/sabine to get 40% off the Vantage plan and see through sensationalized reporting. Stay fully informed ...

📺 Sabine Hossenfelder

👁️ 261K • 👍 16K • 💬 3K • ⏱️ 12:14 • 1d ago

---

**[Japan Just Dropped an AI That Beats Claude (Fable 5)](https://www.youtube.com/watch?v=UyshVdGe4UY)**

Join our FREE WhatsApp Community: https://links.stayingahead.com/YT49 America just banned its best AI, Claude (Fable 5) so I ...

📺 Vaibhav Sisinty

👁️ 43K • 👍 1K • 💬 147 • ⏱️ 12:47 • 15h ago

---

**[The AI Water Use Problem](https://www.youtube.com/watch?v=wx7ToT0G0qo)**

Go to https://ground.news/kylehill to get 40% off unlimited access to the news tool I actually trust. It helps you cut through the noise ...

📺 Kyle Hill

👁️ 133K • 👍 15K • 💬 2K • ⏱️ 21:59 • 15h ago

---

**[Tim Dillon on Israel, Iran, AI, and Palantir](https://www.youtube.com/watch?v=DyKSUEEPb74)**

Taken from JRE #2518 w/Tim Dillon YouTube: https://youtu.be/wTdqkloiSvk JRE on Spotify: ...

📺 JRE Clips

👁️ 294K • 👍 7K • 💬 1K • ⏱️ 15:48 • 1d ago

---

**[Dear AI Companies: Stop the “Doom Trolling”](https://www.youtube.com/watch?v=aHxwZEXHwps)**

Cal Newport takes a critical look at recent AI News. More from Cal Download Cal's FREE guide to cultivating a deeper life: ...

📺 Cal Newport

👁️ 14K • 👍 744 • 💬 174 • ⏱️ 22:05 • 21h ago

---

**[I Tried Dating AI](https://www.youtube.com/watch?v=xibYjTT7kHs)**

In this video I went on multiple AI dates to learn about the future of relationships. hopefully you enjoy and hopefully i wont take so ...

📺 Husk IRL

👁️ 113K • 👍 7K • 💬 1K • ⏱️ 16:22 • 1d ago

---

**[The AI Spending Collapse Has Already Begun…](https://www.youtube.com/watch?v=I8ijs4czL_0)**

Start your workflow automation using Higgsfield today: https://higgsfield.ai/s/mcp-poojadutt-DmHjkQ ✓ Tech Companies are ...

📺 Pooja Dutt

👁️ 19K • 👍 652 • 💬 112 • ⏱️ 14:28 • 2d ago

---

**[NVIDIA Wants to Replace You With AI](https://www.youtube.com/watch?v=go-OkYVfcdc)**

Watch the full Daily DeFranco Show: https://www.youtube.com/@PhilipDeFranco?sub_confirmation=1 Get More News Clips: ...

📺 DeFranco News Clips

👁️ 765K • 👍 39K • 💬 3K • ⏱️ 1:26 • 2d ago

---

**[Cop Uses AI to Prove the Law | @motion_mitch_/IG](https://www.youtube.com/watch?v=Xk066Sulp0M)**

Credit: @motion_mitch_/IG Disclaimer: This video is edited and presented for documentary and educational purposes.

📺 Vilux

👁️ 209K • 👍 8K • 💬 284 • ⏱️ 0:42 • 12h ago

---

**[Which Crazy Bed Would You Choose? 🦋 | Ultimate Oddly Satisfying AI ASMR #5 #aiasmr](https://www.youtube.com/watch?v=A-uY6orWpdg)**

aiasmr #bedasmr #oddlysatisfying #unitedstates Enter the universe of @aiasmrsatisfait! What Is Your Ideal Magical Bed?

📺 AI ASMR Satisfait

👁️ 19K • 💬 4 • ⏱️ 2:23 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 67,107 • ❤️ 2,520 • 3d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 70,743 • ❤️ 931 • 1d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 165,187 • ❤️ 633 • 6d ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 495,813 • ❤️ 2,373 • 7d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`text-generation` `9.0B`

⬇️ 134,294 • ❤️ 508 • 3d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 10,160 • ❤️ 406 • 1d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 51,717 • ❤️ 719 • 6d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 3,389 • ❤️ 269 • 1d ago

---

**[Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)**

*KREA*

Krea-2-Turbo is a text-to-image diffusion model capable of generating diverse artistic styles, including halftone, pixelated, impressionist, thermal imaging, and black and white photography. It is primarily used for creative image generation and artistic exploration.

`text-to-image`

⬇️ 2,996 • ❤️ 255 • 2d ago

---

**[GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)**

*Unsloth AI*

GLM-5.2 is a large language model optimized for long-horizon tasks, featuring a 1M token context window and advanced coding capabilities with flexible effort levels. It utilizes an improved architecture with IndexShare for reduced FLOPs and is released under an MIT license for broad accessibility.

`text-generation` `753.9B`

⬇️ 88,915 • ❤️ 393 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 31 • 💬 3 • ⭐ 8,452 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 172 • 💬 2 • ⭐ 69,732 • 9mo ago

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

▲ 120 • 💬 4 • ⭐ 475 • 3d ago

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

▲ 247 • 💬 4 • ⭐ 9,289 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 23 • 💬 1 • ⭐ 83,843 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 186 • 💬 6 • ⭐ 5,504 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 78.0k • 🔱 10.2k • 14h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 58.8k • 🔱 3.0k • 6h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.8k • 🔱 1.0k • 15h ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 5.4k • 🔱 420 • 4h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.9k • 🔱 590 • 2m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 2.1k • 🔱 287 • 21h ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.9k • 🔱 141 • 3d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 151 • 10d ago

---

**[Forward-Future/loop-library](https://github.com/Forward-Future/loop-library)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 1.7k • 🔱 147 • 13h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 85 • 13d ago

---

---

*Generated by PeekDeck - A glance is all you need*
