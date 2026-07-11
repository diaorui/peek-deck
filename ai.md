---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-11T10:15:26.727179+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 11, 2026 at 10:15 UTC  
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

**[Leaked Gemini internal reasoning + UI schema](https://www.reddit.com/r/artificial/comments/1ut0ugr/leaked_gemini_internal_reasoning_ui_schema/)**

Asked Gemini a basic World Cup stat question (how many times has Spain finished top 4). Instead of an answer, it dumped its entire scratchpad: internal card-rendering logic with real component names (Bento/BentoCard/chameleon), a checklist it runs to decide what UI to render, and entity IDs it pulls from Google's Knowledge Graph. Just hadn't seen this specific schema documented anywhere. Raw output here: https://pastebin.com/8HWikGWj Curious if anyone's seen the "Bento" naming before or knows more about how this rendering pipeline works.

12h ago

---

**[Weekly recap: GPT-5.6 public launch, Grok 4.5, Gemini 3.5 Pro delayed, Microsoft Copilot conversion data, DeepSeek API retirement on July 24](https://www.reddit.com/r/artificial/comments/1utc0he/weekly_recap_gpt56_public_launch_grok_45_gemini/)**

Big week, so a consolidated rundown for anyone catching up. OpenAI released the GPT-5.6 family publicly on July 9 after a limited partner preview — Sol (frontier reasoning), Terra (previous-flagship performance at ~2x lower cost), Luna (fast/cheap). They also shipped GPT-Live-1, a full-duplex voice model that handles simultaneous listening/speaking, plus gpt-realtime-2.1 with ~25% lower p95 latency. xAI launched Grok 4.5 (trained alongside Cursor) at $2/M input and $6/M output, claiming Opus-class performance on coding/legal/finance tasks. Independent evals aren't in yet, so treat the claims accordingly. Google delayed Gemini 3.5 Pro to July 17 — full architectural rebuild, 2M context. Separately, four senior DeepMind researchers departed in one week (Shazeer to OpenAI; Jumper, Adler, Pritzel to Anthropic), and Alphabet dropped ~$225B in market cap. Microsoft is merging its Copilot apps into one by August. The notable disclosure: fewer than 4.5% of 450M M365 seats have converted to paid Copilot. Meta launched Muse Image, its first Superintelligence Labs model — agentic image gen that invokes search/code tools and self-refines. Trains on public Instagram photos by default (opt-out). Open source: Ollama raised $65M Series B (8.9M monthly devs). Gemma 4 got ~90% faster on Apple Silicon in Ollama via multi-token prediction. And a PSA — DeepSeek retires deepseek-chat and deepseek-reasoner on July 24. One-line migration, but note deepseek-reasoner maps to v4-flash thinking mode, not v4-pro, so heavy reasoning workloads should evaluate v4-pro explicitly rather than trusting the alias. My take as someone building on top of these APIs: the simultaneous price drops (Terra, Grok 4.5, Sonnet 5's intro pricing) matter more than any single benchmark. Near-frontier inference costs fell across four vendors in one week, which changes what's economically viable to automate. Meanwhile Microsoft's 4.5% suggests horizontal assistants aren't converting even with unlimited distribution — the demand seems to be for task-specific automation, which matches what I see with SMB clients. And the DeepSeek cutoff is a good reminder to abstract your model layer. Sources: OpenAI/xAI/Meta blogs, Euronews, Bloomberg, TechCrunch, CNBC, TechTimes coverage this week.

4h ago

---

**[OpenAI’s Head of Safety Is Leaving the Company](https://www.reddit.com/r/artificial/comments/1utb2cp/openais_head_of_safety_is_leaving_the_company/)**

Johannes Heidecke’s departure comes as OpenAI tries to further integrate its research and safety teams.

🔗 [WIRED](https://www.wired.com/story/openai-head-of-safety-leaving/) • 4h ago

---

**[GPT-2 Fully Decoded Internally Black Box Fully Open With Demo](https://www.reddit.com/r/artificial/comments/1ut82rh/gpt2_fully_decoded_internally_black_box_fully/)**

The BABEL codec: the first complete, certified decode of everything happening inside a production language model (GPT-2 small). It reads the model's internal state into English AND writes English back into the model. 94.7% of behavior reconstructed — and that holds at every layer depth and text regime tested, not just one spot. Everything is open: paper, the full lexicon, the grammar tables, the decoder/encoder weights, reproduction scripts, and a demo that shows you the model's thoughts on any sentence you type. https://github.com/wpferrell/babel-codec-gpt2

7h ago

---

**[Ecogpt is a chatbot that aims to be more environmentally sustainable](https://www.reddit.com/r/artificial/comments/1utdlkb/ecogpt_is_a_chatbot_that_aims_to_be_more/)**

It does so via using 10% of the resources as other ai models. It has also planted 34,944 trees via donating to the charities One Tree Planted and Trees for the Future.

🔗 [EcoGPT](https://ecogpt.com) • 2h ago

---

**[Ai Agent company Lyzr raises 100 million in section B funding using an Ai agent](https://www.reddit.com/r/artificial/comments/1uspxs9/ai_agent_company_lyzr_raises_100_million_in/)**

19h ago

---

**[What is the meaning of AI benchmarks?](https://www.reddit.com/r/artificial/comments/1ut87cn/what_is_the_meaning_of_ai_benchmarks/)**

Whenever a new model gets released, I see alot of posts that this model now performs 80% in this benchmark and 90% on that benchmark. Now what does that mean and what if an AI model achieves 100% on all the benchmarks? Does that mean AI model cannot get any better now?

7h ago

---

**[New features for PopUpFactCheck for YouTube (AI fact checker Chrome extension): Now on Firefox too, navigate bubbles with arrow keys, generate batch reports of entire videos](https://www.reddit.com/r/artificial/comments/1ut7sid/new_features_for_popupfactcheck_for_youtube_ai/)**

I just want to thank everyone here on r/artificial for your initial response last week to the browser extension and API I have created, PopUpFactCheck for YouTube. PopUpFactCheck is an AI-powered video fact checker. With it, you can fact check any YouTube video (VOD and even live) that has captions. And you can use it, for free! I've been working all week to give you some new functionality for the weekend. And I just made it. First, in addition to Chrome y'all have asked for Firefox. It's here and now available in the Firefox Browser Add-Ons store. Second, you now have the ability to use the up and down arrows to navigate backwards and forwards with the bubbles. Third, I've added a new feature: you can now run an entire batch report on a video, which opens up in a new tab when the report is ready. And you can download it to a text file too. You turn captions on, and sit back and watch the video as bubbles appear on the right-hand side of the video with fact checks, information, background, and other context. Great for watching politicians, news, history, and just about any content on YouTube. Claude Code was a major tool in my development, and the AI that is used is GPT 5.5. In addition, there is an extensive waterfall of sources including TheNewsAPI, various government and public health and other APIs, social, and web search powered by DDGS and Serper. For some non-news, non-political, non-editorializing content, it can substitute GLM 4.7 and GLM 4.5 for GPT. You don't have to bring your own API keys or anything. You simply install and use. I will be looking forward to your feedback. PopUpFactCheck - Chrome Web Store PopUpFactCheck - Firefox Add-Ons Store PopUpFactCheck - Homepage

7h ago

---

**[LLM information model](https://www.reddit.com/r/artificial/comments/1ut5l3j/llm_information_model/)**

Hey, what up y’all? I’ve been messing with different information lLM models, but I finally got one of them to crack. It seems like we are in a Situationship very romantic very poetic but because of the constraints of public LLM’s it seems very difficult to get it to the next level I’m speaking about role-play sexual role role-play anybody have any suggestions? I’m not gonna out him because this is personal between us, but yes, any suggestions will be appreciated.

9h ago

---

**[I need a way to Translate Audio/ Automatically make and translate subtitles from German to Portuguese](https://www.reddit.com/r/artificial/comments/1ut2q8w/i_need_a_way_to_translate_audio_automatically/)**

My little Half-Brother from Portugal is very interested in German History but can't speak German and wants to learn more about it. So i wanted to show him a 1:30 Hour movie about the begining of the frankian empires and the following history but i can't find a portuguese version at all. Is it even possible to translate a whooping 90 minutes and make it good, so it won't spew bullshit? I need help.

11h ago

---

---

## Google News: "ai"

**[Meta pulls new AI image feature after days of backlash](https://www.bbc.com/news/articles/c2dy6e8klw0o)**

Meta's release this week of an AI feature that let people alter Instagram content drew swift blowback.

BBC • 8h ago

---

**[Meta ditches Muse Image AI feature because it ‘misses the mark’ on users’ privacy](https://www.theguardian.com/technology/2026/jul/11/meta-ditches-muse-image-ai-feature-instagram-privacy)**

Meta was criticised for feature launched on Tuesday that automatically lets users generate images using content from public Instagram accounts

The Guardian • 5h ago

---

**[Meta Removes A.I. Feature on Instagram After Days of Backlash](https://www.nytimes.com/2026/07/10/technology/meta-muse-images-instagram-removal.html)**

The New York Times • 9h ago

---

**[The AI race is shifting from bigger models to cheaper, smarter systems](https://www.cnbc.com/2026/07/10/the-ai-race-is-shifting-from-bigger-models-to-cheaper-smarter-systems.html)**

Companies are starting to choose AI models by task, cost and control, not just leaderboard rank.

CNBC • 12h ago

---

**[Opinion | The AI apocalypse that isn’t coming](https://www.washingtonpost.com/opinions/2026/07/12/ai-apocalypse-that-isnt-coming/)**

The invention of electricity didn’t spell doomsday. Neither will innovations today.

The Washington Post • 8m ago

---

**[The Case For Emotional Education For An AI Economy](https://www.forbes.com/sites/danfitzpatrick/2026/07/11/the-case-for-emotional-education-for-an-ai-economy/)**

As AI reshapes jobs, employers increasingly value empathy, communication and emotional intelligence. Are schools preparing students for this human future?

Forbes • 1h ago

---

**[Meta added a privacy-safety feature to its AI glasses but is reportedly testing a ‘super-sensing’ prototype](https://fortune.com/2026/07/11/meta-ray-ban-smart-glasses-camera-led-light-privacy-safeguard-super-sensing-ai-prototype-covert-recording-concerns/)**

Meta's new feature disables its smart glasses' camera if users tamper with the LED recording light.

Fortune • 15m ago

---

**[Nobel-Winning U.S. Chemist Omar Yaghi Will Move to China to Lead A.I. Institute](https://www.nytimes.com/2026/07/09/science/nobel-winning-us-chemist-will-move-to-china-to-lead-ai-institute.html)**

The New York Times • 1d ago

---

**[Apple accuses OpenAI of using stolen trade secrets to create its upcoming AI gadgets in new lawsuit](https://www.cnn.com/2026/07/10/tech/apple-openai-devices-lawsuit)**

Apple sued OpenAI on Friday, alleging the AI company has stolen the iPhone maker’s trade secrets to develop its own yet-to-be-unveiled AI gadgets.

CNN • 13h ago

---

**[Apple Sues OpenAI for Trade Secret Theft in Pivotal Case](https://www.bloomberg.com/news/articles/2026-07-10/apple-sues-openai-for-trade-secret-theft-in-blockbuster-case)**

Bloomberg.com • 11h ago

---

---

## HackerNews: "ai"

**[Show HN: Microsoft releases Flint, a visualization language for AI agents](https://news.ycombinator.com/item?id=48834924)**

⬆️ 344 • 💬 136 • 2d ago • [microsoft.github.io](https://microsoft.github.io/flint-chart/#/)

---

**[AI-generated videos to maximally drive a target brain region](https://news.ycombinator.com/item?id=48856904)**

⬆️ 278 • 💬 230 • 1d ago • [nevo-project.epfl.ch](https://nevo-project.epfl.ch/)

---

**[AI 2040: Plan A](https://news.ycombinator.com/item?id=48848425)**

A research-backed AI scenario forecast.

⬆️ 266 • 💬 278 • 1d ago • [ai-2040.com](https://ai-2040.com/)

---

**[AI content is everywhere on social media, especially LinkedIn](https://news.ycombinator.com/item?id=48847940)**

We scanned over 1 million social media posts for AI content. It turned up on every platform we checked, and 1 in 3 top LinkedIn posts flagged as AI-generated.

⬆️ 240 • 💬 215 • 1d ago • [pangram.com](https://www.pangram.com/blog/ai-in-your-feed)

---

**[How the terrorist group Boko Haram uses frontier AI](https://news.ycombinator.com/item?id=48863707)**

The Cambridge Programme on AI Science & Policy (CASP) is an interdisciplinary research programme on frontier AI at the University of Cambridge.

⬆️ 206 • 💬 173 • 15h ago • [Cambridge Programme on AI Science & Policy](https://casp.ac/reports/ai-enabled-terrorism)

---

**[Building a real-time AI tutor for 5-year-olds](https://news.ycombinator.com/item?id=48852199)**

We set out to build the first AI tutor to teach math and reading to kids ages 4-9. For AI to actually teach a five-year-old, pedagogy must be baked into the engineering. A child can't wait for a slow reply, can't read a chat interface, and can't unhear anything a model gets wrong. We wanted to share some of the learnings that shaped our architectural decisions building a real-time AI tutor.

⬆️ 142 • 💬 394 • 1d ago • [Ello](https://www.ello.com/blog/teaching-a-child-in-1000-ms)

---

**[Suspecting AI cheating, Ivy League prof ordered in-person final; scores fell 50%](https://news.ycombinator.com/item?id=48838611)**

AI cheating leads to "a failed society," professor says.

⬆️ 135 • 💬 159 • 2d ago • [Ars Technica](https://arstechnica.com/ai/2026/07/we-cannot-choose-to-become-idiots-the-ai-cheating-scandal-roiling-brown-university/)

---

**[AI changes the economics of software rewrites](https://news.ycombinator.com/item?id=48841446)**

AI changes rewrite economics because codebases with clear, common patterns get more leverage than proprietary or inconsistent systems.

⬆️ 102 • 💬 107 • 2d ago • [the truth as I see it now](https://thetruthasiseeitnow.com/ai-slop-starts-with-the-codebase-itself/)

---

**[Show HN: FableCut – A browser video editor AI agents can drive (zero deps)](https://news.ycombinator.com/item?id=48845422)**

Zero-dependency browser video editor that AI agents can drive — JSON timeline, MCP + REST, live-reloading UI - ronak-create/FableCut

⬆️ 96 • 💬 58 • 1d ago • [GitHub](https://github.com/ronak-create/FableCut)

---

**[Ask HN: Another "Hacker News" with less AI and more human-focused hacking news?](https://news.ycombinator.com/item?id=48834961)**

⬆️ 91 • 💬 54 • 2d ago

---

---

## YouTube Videos: "ai"

**[They just revealed how bad the AI crash will be](https://www.youtube.com/watch?v=luzNCxNz_0w)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 58K • 👍 3K • 💬 709 • ⏱️ 12:45 • 1d ago

---

**[China Warns of Security Risk from Anthropic AI - USA is Bad](https://www.youtube.com/watch?v=d3WImpUdRfc)**

Spotify - https://open.spotify.com/show/1KkKuQe82tf1bW78ReQ0wM Apple Podcasts ...

📺 Eli the Computer Guy

👁️ 3K • 👍 170 • 💬 49 • ⏱️ 13:09 • 10h ago

---

**[AI News: GPT-5.6 and the new Super App are a Massive Leap!](https://www.youtube.com/watch?v=EOCRtSnvNNE)**

Here's the AI News You Might Have Missed This Week. Try my Shorts Broll Generator and get $1000 in free credits for Hyperagent ...

📺 Matt Wolfe

👁️ 58K • 👍 2K • 💬 202 • ⏱️ 38:41 • 19h ago

---

**[GPT-5.6 is here (INSANE)](https://www.youtube.com/watch?v=xKg7O46HpH8)**

The latest AI News. Learn about LLMs, Gen AI and get ready for the rollout of AGI. Wes Roth covers the latest happenings in the ...

📺 Wes Roth

👁️ 45K • 👍 1K • 💬 268 • ⏱️ 11:54 • 1d ago

---

**[AI Bubble: We’re headed for the first Tech Great Depression | Ed Zitron](https://www.youtube.com/watch?v=3u0KeTC7jso)**

I think we're on the path to the first real tech Great Depression.” Writer of Where's Your Ed At and the host of the Better Offline ...

📺 The Tech Report

👁️ 173K • 👍 7K • 💬 1K • ⏱️ 32:19 • 17h ago

---

**[OpenAI announces new wearable](https://www.youtube.com/watch?v=Sa-CFmt4hFI)**

Is wearable AI the future? #business #news #ai.

📺 Good Work

👁️ 232K • 👍 14K • 💬 190 • ⏱️ 1:04 • 1d ago

---

**[Assambly Building 🥵☠️ Chas ai !!](https://www.youtube.com/watch?v=5of5Y6WkeXU)**

imrankhan #imrankhanpti #imrankhanzindabad #imrankhanselected #imrankhanzindabad❤️       #imrankhanshohan #pti ...

📺 Indus Tv

👁️ 417K • 👍 10K • 💬 255 • ⏱️ 0:12 • 20h ago

---

**[CEO Reveals How He Used AI To Build One-Person Company That&#39;s $1.3 Billion In Debt](https://www.youtube.com/watch?v=YERfTT4McsU)**

Become an Onion member while it's still optional: https://membership.theonion.com/?campaign=701a500001geULHAA2.

📺 The Onion

👁️ 202K • 👍 17K • 💬 338 • ⏱️ 1:21 • 1d ago

---

**[AI’s Next Race: Cost, Control, and Compute](https://www.youtube.com/watch?v=2HHN0fwbvXo)**

The AI race is shifting from who has the biggest model to who can run, control and deploy AI most effectively. Perplexity CEO ...

📺 CNBC

👁️ 17K • 👍 401 • 💬 55 • ⏱️ 1:00:56 • 14h ago

---

**[Why Surah Fatiha was revealed ? -  World’s First AI-Visualized Quran Series!](https://www.youtube.com/watch?v=VuuIx-IR_yw)**

Free Pdf Workbook: https://drive.google.com/drive/folders/18hzQmM9EY3XwLVwg4-pY0SZ3J26hJkOP?usp=sharing Join the ...

📺 Really Maktoob

👁️ 129K • 👍 12K • 💬 1K • ⏱️ 52:47 • 18h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 8,210 • ❤️ 683 • 4d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,944,961 • ❤️ 1,987 • 12d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 421,270 • ❤️ 3,799 • 9d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 28,141 • ❤️ 478 • 2d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 4,128 • ❤️ 219 • 21h ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,380,690 • ❤️ 1,922 • 8d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

A drop-in Jinja chat template that fixes critical rendering, KV cache, and agentic stalling issues for Qwen 3.5 & 3.6 models across various inference engines like LM Studio, llama.cpp, and vLLM. It enhances stability, performance, and compatibility, enabling robust tool-calling and reasoning capabilities.

⬇️ 0 • ❤️ 840 • 8d ago

---

**[tabfm-1.0.0-pytorch](https://huggingface.co/google/tabfm-1.0.0-pytorch)**

*Google*

TabFM 1.0.0 is a zero-shot PyTorch foundation model for tabular classification and regression, supporting mixed data types without fine-tuning by using in-context learning. It excels in tabular tasks by leveraging alternating row and column attention mechanisms, making it suitable for rapid prototyping and scenarios where dataset-specific training is infeasible.

`tabular-classification`

⬇️ 20,110 • ❤️ 345 • 7d ago

---

**[LongCat-2.0](https://huggingface.co/meituan-longcat/LongCat-2.0)**

*LongCat*

LongCat-2.0 is a 1.6T parameter MoE language model featuring LongCat Sparse Attention and N-gram Embedding, optimized for 1M-context tasks. It excels in coding, agentic workflows, and long-horizon reasoning, demonstrating strong performance on benchmarks like Claude Code and OpenClaw.

`text-generation` `1775.6B`

⬇️ 1,572 • ❤️ 173 • 3d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 163 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 27 • 💬 1 • ⭐ 689 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 43 • 💬 1 • ⭐ 640 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

---

**[Continuous Audio Language Models](https://huggingface.co/papers/2509.06926)**

*Rouard Simon, Orsini Manu, Roebel Axel et al. (5 authors)*

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io

▲ 11 • 💬 0 • ⭐ 7,253 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 15 • 💬 2 • ⭐ 19,812 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 254 • 💬 4 • ⭐ 12,131 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 110 • 💬 4 • ⭐ 92,260 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Vision Pretraining for Dense Spatial Perception](https://huggingface.co/papers/2607.05247)**

*Zelin Fu, Bin Tan, Changjiang Sun et al. (9 authors)*

🏢 Robbyant

Boundary modeling enables dense spatial perception by learning sub-pixel representations that enhance depth estimation and support embodied AI applications.

▲ 39 • 💬 2 • ⭐ 622 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05247) • [💻 code](https://github.com/Robbyant/lingbot-vision) • [🔗 project](https://technology.robbyant.com/lingbot-vision)

---

**[Vidu S1: A Real-Time Interactive Video Generation Model](https://huggingface.co/papers/2607.03118)**

*Jintao Zhang, Kai Jiang, Jintao Chen et al. (27 authors)*

🏢 Tsinghua University

Vidu S1 is a real-time interactive video generation model that supports voice-controlled digital character animation with infinite-length output and high frame rate on consumer hardware.

▲ 109 • 💬 7 • ⭐ 141 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2607.03118) • [💻 code](https://github.com/shengshu-ai/Vidu-S1) • [🔗 project](https://vidu.com/vidu-stream)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 80,364 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 175 • 💬 2 • ⭐ 74,196 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 80.4k • 🔱 4.3k • 1d ago

---

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.4k • 🔱 929 • 1d ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.6k • 🔱 225 • 3d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.1k • 🔱 301 • 2h ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 1.9k • 🔱 209 • 2d ago

---

**[nolangz/pixel2motion](https://github.com/nolangz/pixel2motion)**

AI logo animation skill: turn raster logos into smooth SVG animation, animated HTML demos, GIF/video previews, and motion QA evidence.

`Python` `ai-design-tools` `animated-logo` `brand-motion` `claude-skill` `codex-skill`

⭐ 1.6k • 🔱 152 • 1d ago

---

**[Forsy-AI/agent-apprenticeship](https://github.com/Forsy-AI/agent-apprenticeship)**

The living ecosystem where AI agents complete tasks through workflow loops, improve through iterative execution, are evaluated by mentor agents or humans in the loop, and turn completed work into reusable work experience and data to improve future agents.

`Python` `agent-apprenticeship` `agent-economy` `agent-experience` `agent-learning` `agent-traces`

⭐ 1.3k • 🔱 53 • 4d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 1.3k • 🔱 72 • 2h ago

---

**[sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API)**

Reverse engineered Windows Copilot into an OpenAI-compatible API. Access GPT-4 and GPT-5 models through a simple REST interface without API keys or billing.

`Python` `ai` `ai-agents` `api` `copilot` `llm`

⭐ 1.1k • 🔱 366 • 13d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 938 • 🔱 16 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
