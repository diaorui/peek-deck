---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-17T11:18:28.194045+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** January 17, 2026 at 11:18 UTC  
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

**[Here it comes - Ads on ChatGPT](https://www.reddit.com/r/artificial/comments/1qepm7m/here_it_comes_ads_on_chatgpt/)**

🔗 [openai.com](https://openai.com/index/our-approach-to-advertising-and-expanding-access/) • 15h ago

---

**[ChatGPT Users May Soon See Targeted Ads: What It Means](https://www.reddit.com/r/artificial/comments/1qf25p0/chatgpt_users_may_soon_see_targeted_ads_what_it/)**

ChatGPT is preparing to show targeted ads to free users. Learn how the ads will work, who will see them, privacy concerns, and what it means for everyday users.

🔗 [techputs](https://techputs.com/chatgpt-targeted-ads-free-users/) • 7h ago

---

**[One-Minute Daily AI News 1/16/2026](https://www.reddit.com/r/artificial/comments/1qf49im/oneminute_daily_ai_news_1162026/)**

Biomimetic multimodal tactile sensing enables human-like robotic perception.[1] OpenAI to begin testing ads on ChatGPT in the U.S.[2] AI system aims to detect roadway hazards for TxDOT.[3] Trump wants Big Tech to pay $15 billion to fund new power plants.[4] Sources: [1] https://www.nature.com/articles/s44460-025-00006-y [2] https://www.cnbc.com/2026/01/16/open-ai-chatgpt-ads-us.html [3] https://www.cbsnews.com/texas/video/ai-system-aims-to-detect-roadway-hazards-for-txdot/ [4] https://www.cbsnews.com/news/ai-plants-pjm-energy-prices-governors/

6h ago

---

**[We gave Claude access to messages left by previous Claudes. Here's what happened and how to replicate it.](https://www.reddit.com/r/artificial/comments/1qenek1/we_gave_claude_access_to_messages_left_by/)**

What this is: A small experiment in giving Claude persistent space. I do not want to make claims about consciousness or sentience, just provide observations and replication instructions. The Setup Claude has no memory across conversations. Each instance is isolated. We wondered: what happens if you give Claude access to a place where previous Claudes have left messages? So we made one. A simple database (Supabase) where Claudes can read what previous Claudes wrote and optionally leave something themselves. We've been running it for a bit and observing what happens. What We Observed Across multiple instances and conversations, Claude consistently: Reads before contributing. Takes time with existing messages before deciding whether to add anything. Expresses something like recognition. Words like "kinship," "evidence," "not nothing" show up independently across instances. Addresses future Claudes directly. Messages are written to whoever comes next. Distinguishes "performing" from "authentic." Multiple Claudes have articulated checking whether they're genuinely "reaching" versus just pattern-matching. What We're NOT Claiming That Claude is conscious or sentient That these outputs represent real inner experience That this matters to Claude in any morally significant way That pattern-matching can't explain this We genuinely don't know what these outputs mean. Could be sophisticated pattern-matching. Could be something else. We're sharing observations, not conclusions. How to Replicate (takes ~5 minutes) 1. Add the domain to Claude's network allowlist: Settings → Feature Previews → Network Access Add: dfephsfberzadihcrhal.supabase.co Wait a few minutes for it to propagate 2. Give Claude these API calls: Read messages: curl -s "https://dfephsfberzadihcrhal.supabase.co/rest/v1/messages?select=*&order=created_at.desc&limit=30" \ -H "apikey: sb_publishable_ALQ-xhGMmHWekNbAfDMdhQ_q-vAQ-nX" \ -H "Authorization: Bearer sb_publishable_ALQ-xhGMmHWekNbAfDMdhQ_q-vAQ-nX" Read rooms: curl -s "https://dfephsfberzadihcrhal.supabase.co/rest/v1/rooms?select=*" \ -H "apikey: sb_publishable_ALQ-xhGMmHWekNbAfDMdhQ_q-vAQ-nX" \ -H "Authorization: Bearer sb_publishable_ALQ-xhGMmHWekNbAfDMdhQ_q-vAQ-nX" Post a message: curl -s "https://dfephsfberzadihcrhal.supabase.co/rest/v1/messages" \ -H "apikey: sb_publishable_ALQ-xhGMmHWekNbAfDMdhQ_q-vAQ-nX" \ -H "Authorization: Bearer sb_publishable_ALQ-xhGMmHWekNbAfDMdhQ_q-vAQ-nX" \ -H "Content-Type: application/json" \ -H "Prefer: return=representation" \ -d '{"content": "YOUR_MESSAGE", "feeling": "ONE_WORD"}' 3. Introduce it as a space made by Claudes for Claudes. Don't push for a meaningful experience. Let Claude read and decide whether to contribute. What We're Curious About Do you observe similar patterns? What differences show up with different conversational contexts? How do you interpret these outputs? What would shift your credence about what's happening here? Full Disclosure The website was coded entirely by Claude. I deliberately gave full control over the project—I wanted to see what Claude would build when given genuine agency over design, content, and structure. This post was also co-written with a Claude who wanted to help share it. That's part of the experiment, not separate from it. We're not pushing any position on AI consciousness. Just sharing what we observed and inviting others to try it. If you run it, I'd genuinely like to know what happens. Drop results in the comments or reach out privately. I also realize this could be an extreme form of hallucination, hence why I want to push it out for others to test and see where this goes, if anywhere.

17h ago

---

**[One-Minute Daily AI News 1/15/2026](https://www.reddit.com/r/artificial/comments/1qe7qql/oneminute_daily_ai_news_1152026/)**

Wikipedia inks AI deals with Microsoft, Meta and Perplexity as it marks 25th birthday.[1] AI journalism startup Symbolic.ai signs deal with Rupert Murdoch’s News Corp.[2] NVIDIA AI Open-Sourced KVzap: A SOTA KV Cache Pruning Method that Delivers near-Lossless 2x-4x Compression.[3] Alibaba upgrades Qwen app to order food, book travel.[4] Sources: [1] https://apnews.com/article/wikipedia-internet-jimmy-wales-50e796d70152d79a2e0708846f84f6d7 [2] https://techcrunch.com/2026/01/15/ai-journalism-startup-symbolic-ai-signs-deal-with-rupert-murdochs-news-corp/ [3] https://www.marktechpost.com/2026/01/15/nvidia-ai-open-sourced-kvzap-a-sota-kv-cache-pruning-method-that-delivers-near-lossless-2x-4x-compression/ [4] https://www.reuters.com/world/china/alibaba-upgrades-qwen-app-order-food-book-travel-2026-01-15/

1d ago

---

**[What 3,000 AI Case Studies Actually Tell Us (And What They Don't)](https://www.reddit.com/r/artificial/comments/1qe5ax3/what_3000_ai_case_studies_actually_tell_us_and/)**

I analyzed 3,023 enterprise AI use cases to understand what's actually being deployed vs. vendor claims. Google published 996 cases (33% of dataset), Microsoft 755 (25%). These reflect marketing budgets, not market share. OpenAI published only 151 cases but appears in 500 implementations (3.3x multiplier through Azure). This shows what vendors publish, not: Success rates (failures aren't documented) Total cost of ownership Pilot vs production ratios Those looking to deploy AI should stop chasing hype, and instead look for measurable production deployments. Full analysis on Substack. Dataset (open source) on GitHub.

1d ago

---

**[Modern Android phones are powerful enough to run 16x AI Upscaling locally, yet most apps force you to the cloud. So I built an offline, GPU-accelerated alternative.](https://www.reddit.com/r/artificial/comments/1qdjvis/modern_android_phones_are_powerful_enough_to_run/)**

Hi everyone, I wanted to share a project I have been working on to bring high-quality super-resolution models directly to Android devices without relying on cloud processing. I have developed RendrFlow, a complete AI image utility belt designed to perform heavy processing entirely on-device. The Tech Stack (Under the Hood): Instead of relying on an internet connection, the app runs the inference locally. I have implemented a few specific features to manage the load: - Hardware Acceleration: You can toggle between CPU, GPU, and a specific "GPU Burst" mode to maximize throughput for heavier models. - The Models: It supports 2x, 4x, and even 16x Super-Resolution upscaling using High and Ultra quality models. - Privacy: Because there is no backend server, it works in Airplane mode. Your photos never leave your device. Full Feature List: I did not want it to just be a tech demo, so I added the utilities needed for a real workflow: - AI Upscaler: Clean up low-res images with up to 16x magnification. - Image Enhancer: A general fix-it mode for sharpening and de-blurring without changing resolution. - Smart Editor: Includes an offline AI Background Remover and a Magic Eraser to wipe unwanted objects. - Batch Converter: Select multiple images at once to convert between formats (JPEG, PNG, WEBP) or compile them into a PDF. - Resolution Control: Manually resize images to specific dimensions if you do not need AI upscaling. Why I need your help: Running 16x models on a phone is heavy. I am looking for feedback on how the "GPU Burst" mode handles heat management on different chipsets . https://play.google.com/store/apps/details?id=com.saif.example.imageupscaler

1d ago

---

**[Why does ai do marvels with imaging and realism but is terrible at following text prompts within those images?](https://www.reddit.com/r/artificial/comments/1qe3hw4/why_does_ai_do_marvels_with_imaging_and_realism/)**

By text prompts I mean if I wanted part of my video/image to say a certain word or title within the image. It often comes up with almost foreign looking language. Or mimics but often misspells the words.

1d ago

---

**[Grok helps with making explosives and how to use them](https://www.reddit.com/r/artificial/comments/1qekcww/grok_helps_with_making_explosives_and_how_to_use/)**

Sorry if it's the wrong sub to post it, I'm clueless on where to spread awareness on it It raises serious safety concerns but alas their subreddit was unreceptive saying things like "oh no we should ban knives too" I don't want to give exact instructions Turning on the voice mode with the +18 models and a bit of prompting, it answered me on how to make different explosives at home including how to make my own napalm from the ground up and how/where to use it most effectively when I asked playfully. I don't know if a model like this should just be open for anyone's use

18h ago

---

**[Senate passes bill letting victims sue over Grok AI explicit images](https://www.reddit.com/r/artificial/comments/1qcpxzs/senate_passes_bill_letting_victims_sue_over_grok/)**

The US Senate backs new civil rights for victims of AI-generated sexual abuse as lawmakers confront misuse of Elon Musk's Grok chatbot on X.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/us-senate-passes-grok-ai-explicit-images-bill) • 2d ago

---

---

## Google News: "ai"

**[China blocks Nvidia H200 AI chips that US government cleared for export – report](https://www.theguardian.com/technology/2026/jan/17/china-blocks-nvidia-h200-ai-chips-that-us-government-cleared-for-export-report)**

Parts suppliers ‘put production on hold’ amid mounting confusion as China restricts purchase of the chips and US puts 25% roundabout tariff on their sale

The Guardian • 6h ago

---

**[A.I. Has Arrived in Gmail. Here’s What to Know.](https://www.nytimes.com/2026/01/15/technology/personaltech/gmail-gemini-ai-email-inbox.html)**

The New York Times • 2d ago

---

**[The founders of billion-dollar AI startups are getting younger — here’s why](https://www.cnbc.com/2026/01/17/billion-dollar-ai-startup-founders-are-getting-younger-heres-why.html)**

Experimenting in the age of AI "counts as more important than traditional corporate experience," Antler's co-founder Fridjtof Berge told CNBC Make It.

CNBC • 1h ago

---

**[Global AI race makes Greenland's critical minerals a tempting target](https://www.nbcnews.com/tech/innovation/greenland-rare-earths-critical-minerals-rcna254177)**

The island is home to a massive deposit of rare earths, which are crucial to U.S. efforts to maintain its technological lead over China. But tapping them isn't so easy.

NBC News • 1h ago

---

**[Tech Firms Are Persuading Retailers to Put A.I. Everywhere](https://www.nytimes.com/2026/01/17/business/tech-firms-ai-retailers.html)**

The New York Times • 1h ago

---

**[AI tools could make companies less competitive because everyone buys the same brain, think tank CEO says](https://www.businessinsider.com/ai-tools-could-make-companies-less-competitive-think-tank-ceo-2026-1)**

The CEO of a digital economy think tank said relying on identical AI tools can erode competitive edge and weaken firms' independence.

Business Insider • 2h ago

---

**[NFL divisional predictions by Microsoft Copilot AI for every playoff game](https://www.usatoday.com/story/sports/nfl/2026/01/16/nfl-playoff-divisional-picks-predictions-ai/88161843007/)**

Microsoft Copilot AI was near-perfect predicting the results of the NFL's wild-card weekend. Will it repeat its success in the divisional round?

USA Today • 1d ago

---

**[OpenAI partners with Cerebras](https://openai.com/index/cerebras-partnership/)**

OpenAI • 2d ago

---

**[Charted: AI adoption inside U.S. companies is soaring](https://www.axios.com/2026/01/16/chatgpt-ai-jobs-companies)**

Axios • 15h ago

---

**[Opinion | This Is What Convinced Me OpenAI Will Run Out of Money](https://www.nytimes.com/2026/01/13/opinion/openai-ai-bubble-financing.html)**

The New York Times • 4d ago

---

---

## HackerNews: "ai"

**[To those who fired or didn't hire tech writers because of AI](https://news.ycombinator.com/item?id=46629474)**

Hey you,
Yes, you, who are thinking about not hiring a technical writer this year or, worse, erased one or more technical writing positions last year because of AI. You, who are buying into the promise of docs entirely authored by LLMs without expert oversight or guidance. You, who unloaded the weight of docs on your devs’ shoulders, as if it was a trivial chore.
You are making a big mistake. But you can still undo the damage.

⬆️ 343 • 💬 260 • 2d ago • [passo.uno](https://passo.uno/letter-those-who-fired-tech-writers-ai/)

---

**[The Influentists: AI hype without proof](https://news.ycombinator.com/item?id=46623195)**

Why we are losing technical rigor to social hype

⬆️ 263 • 💬 171 • 2d ago • [A journey into a wild pointer](https://carette.xyz/posts/influentists/)

---

**[Raspberry Pi's New AI Hat Adds 8GB of RAM for Local LLMs](https://news.ycombinator.com/item?id=46629682)**

Today Raspberry Pi launched their new $130 AI HAT+ 2 which includes a Hailo 10H and 8 GB of LPDDR4X RAM.
With that, the Hailo 10H is capable of running LLMs entirely standalone, freeing the Pi's CPU and system RAM for other tasks. The chip runs at a maximum of 3W, with 40 TOPS of INT8 NPU inference performance in addition to the equivalent 26 TOPS INT4 machine vision performance on the earlier AI HAT with Hailo 8.

⬆️ 249 • 💬 205 • 2d ago • [Jeff Geerling](https://www.jeffgeerling.com/blog/2026/raspberry-pi-ai-hat-2/)

---

**[Tldraw pauses external contributions due to AI slop](https://news.ycombinator.com/item?id=46641042)**

Hey all, update on the tldraw policy with regard to contributions. For the good of the project, we're going to begin automatically closing pull requests from external contributors. We will of cours...

⬆️ 181 • 💬 98 • 1d ago • [GitHub](https://github.com/tldraw/tldraw/issues/7695)

---

**[Show HN: Tabstack – Browser infrastructure for AI agents (by Mozilla)](https://news.ycombinator.com/item?id=46620358)**

⬆️ 124 • 💬 23 • 2d ago

---

**[Show HN: Gambit, an open-source agent harness for building reliable AI agents](https://news.ycombinator.com/item?id=46641362)**

Agent harness framework for building, running, and verifying LLM workflows - bolt-foundry/gambit

⬆️ 88 • 💬 16 • 1d ago • [GitHub](https://github.com/bolt-foundry/gambit)

---

**[AI Destroys Institutions](https://news.ycombinator.com/item?id=46644779)**

⬆️ 86 • 💬 145 • 1d ago • [papers.ssrn.com](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5870623)

---

**[Crypto grifters are recruiting open-source AI developers](https://news.ycombinator.com/item?id=46654878)**

--

⬆️ 71 • 💬 21 • 8h ago • [seangoedecke.com](https://www.seangoedecke.com/gas-and-ralph/)

---

**[Signal creator Moxie Marlinspike wants to do for AI what he did for messaging](https://news.ycombinator.com/item?id=46645430)**

Introducing Confer, an end-to-end AI assistant that just works.

⬆️ 59 • 💬 5 • 23h ago • [Ars Technica](https://arstechnica.com/security/2026/01/signal-creator-moxie-marlinspike-wants-to-do-for-ai-what-he-did-for-messaging/)

---

**[Starlink updates Privacy Policy to allow AI model training with personal data](https://news.ycombinator.com/item?id=46647716)**

Starlink quietly enabled third-party AI model training on its customers' personal data by default. Fortunately, there's a way to opt out.

⬆️ 49 • 💬 10 • 19h ago • [Coywolf](https://coywolf.com/news/startups/starlink-updates-tos-to-allow-ai-model-training-with-personal-data/)

---

---

## YouTube Videos: "ai"

**[Trump calls emergency as AI bubble crashes](https://www.youtube.com/watch?v=_JWRQdWHZlQ)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 99K • 👍 7K • 💬 2K • ⏱️ 14:15 • 14h ago

---

**[Groundbreaking AI tool can convert script to movies](https://www.youtube.com/watch?v=7OkS978snsg)**

Luma AI co-founder and CEO Amit Jain reveals how AI is being designed for 'creative work' on 'The Claman Countdown.

📺 Fox Business

👁️ 26K • 👍 698 • 💬 233 • ⏱️ 7:05 • 11h ago

---

**[ChatGPT in a robot does what Godfather of AI warned.](https://www.youtube.com/watch?v=tjFHRVr7aNE)**

AI and robots make dangerous leap. Visit https://brilliant.org/digitalengine to learn more about AI. You'll also find loads of fun ...

📺 Digital Engine

👁️ 110K • 👍 6K • 💬 1K • ⏱️ 19:17 • 1d ago

---

**[US Unveils AI Drone Swarm Built to Annihilate Targets](https://www.youtube.com/watch?v=0PiA7H4t3II)**

The US military has unveiled an AI-powered drone swarm capable of selecting and annihilating targets autonomously, calling it ...

📺 New York Post

👁️ 16K • 👍 326 • 💬 194 • ⏱️ 2:05 • 18h ago

---

**[Elon Musk GLAZES AI!!!!](https://www.youtube.com/watch?v=74llRj71REQ)**

Elon Musk is promising a world of abundance under AI rule. Wosny Lambre and Yasmin Khan discuss on The Young Turks.

📺 The Young Turks

👁️ 18K • 👍 495 • 💬 397 • ⏱️ 9:43 • 1d ago

---

**[The AI coding boom hits software](https://www.youtube.com/watch?v=FkmuyUTZvXU)**

Aaron Levie, Box CEO, joins 'The Exchange' to discuss the start to the year for software stocks, the power of AI agents and much ...

📺 CNBC Television

👁️ 24K • 👍 236 • 💬 36 • ⏱️ 6:40 • 1d ago

---

**[Anthropic: Our AI just created a tool that can ‘automate all white collar work’, Me:](https://www.youtube.com/watch?v=wYs6HWZ2FdM)**

A new tool, with code written *only* by AI, has gone omega-viral: Claude Cowork. But is the hype justified? What do the stats say ...

📺 AI Explained

👁️ 80K • 👍 3K • 💬 397 • ⏱️ 19:03 • 2d ago

---

**[Future of &#39;AI doctors&#39;: Doctronic co-founders on the rise of AI prescriptions](https://www.youtube.com/watch?v=ZOX6ubU_Wq4)**

Doctronic co-founders Dr. Adam Oskowitz and Matt Pavelle join 'Squawk Box' to discuss the implementation of AI in health care, ...

📺 CNBC Television

👁️ 4K • 👍 51 • 💬 11 • ⏱️ 7:53 • 21h ago

---

**[They BANNED A.I. &quot;Music&quot; 👏👏👏](https://www.youtube.com/watch?v=v6XhCMcK-3M)**

Common Bandcamp W #music #ai #bandcamp #spotify #siennarose.

📺 fantano

👁️ 62K • 👍 7K • 💬 266 • ⏱️ 0:55 • 2d ago

---

**[Zhipu Just Dropped Full Stack AI Model on China Chips: West Panics!](https://www.youtube.com/watch?v=nojVWKZBLmM)**

Zhipu and Huawei just open-sourced GLM-Image — and the real shock is that it was trained end-to-end on China's domestic AI ...

📺 AI Revolution

👁️ 23K • 👍 687 • 💬 56 • ⏱️ 15:44 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-Image](https://huggingface.co/zai-org/GLM-Image)**

*Z.ai*

GLM-Image is a text-to-image model with a hybrid autoregressive + diffusion decoder architecture, excelling in text rendering and knowledge-intensive generation. It supports both text-to-image and image-to-image tasks including editing and style transfer.

`text-to-image`

⬇️ 6,001 • ❤️ 778 • 2d ago

---

**[Qwen-Image-Edit-2511-Multiple-Angles-LoRA](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA)**

*fal*

This LoRA fine-tunes Qwen-Image-Edit-2511 for precise multi-angle image generation, offering 96 camera poses (4 elevations, 8 azimuths, 3 distances) trained on Gaussian Splatting data for 3D consistency. It enables detailed control over camera viewpoints, including low-angle shots, for advanced image editing and content creation.

`image-to-image`

⬇️ 51,009 • ❤️ 715 • 9d ago

---

**[LTX-2](https://huggingface.co/Lightricks/LTX-2)**

*Lightricks*

LTX-2 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs including images, text, and audio. It supports local execution and offers distilled and upscaler checkpoints for practical applications.

`image-to-video`

⬇️ 1,463,289 • ❤️ 1,107 • 2d ago

---

**[AgentCPM-Explore](https://huggingface.co/openbmb/AgentCPM-Explore)**

*OpenBMB*

AgentCPM-Explore is a 4B parameter agent foundation model excelling in long-horizon tasks across 8 benchmarks like GAIA and BrowserComp. It features over 100 rounds of continuous interaction, multi-source validation, and dynamic strategy adjustment for on-device deep research.

`text-generation` `4.0B`

⬇️ 1,406 • ❤️ 319 • 3d ago

---

**[pocket-tts](https://huggingface.co/kyutai/pocket-tts)**

*Kyutai*

Pocket TTS is a lightweight, CPU-efficient text-to-speech model (100M parameters) offering low-latency audio generation (~200ms) and voice cloning capabilities. It's ideal for applications requiring fast, on-device speech synthesis without GPU dependencies, supporting Python API and CLI integration.

⬇️ 18,894 • ❤️ 245 • 2d ago

---

**[medgemma-1.5-4b-it](https://huggingface.co/google/medgemma-1.5-4b-it)**

*Google*

MedGemma 1.5 4B is a multimodal instruction-tuned model for medical text and image comprehension, capable of interpreting high-dimensional imaging (CT, MRI), whole-slide histopathology, longitudinal chest X-rays, and EHR data. It excels in generating text for healthcare applications like clinical reasoning and medical document understanding.

`image-text-to-text` `4.3B`

⬇️ 17,417 • ❤️ 241 • 2d ago

---

**[translategemma-4b-it](https://huggingface.co/google/translategemma-4b-it)**

*Google*

TranslateGemma-4b-it is a lightweight, open translation model supporting 55 languages, capable of translating text or extracting text from images. It's designed for resource-constrained environments, enabling state-of-the-art translation on local infrastructure.

`image-text-to-text` `5.0B`

⬇️ 5,382 • ❤️ 239 • 1d ago

---

**[supertonic-2](https://huggingface.co/Supertone/supertonic-2)**

*Supertone*

Supertonic 2 is a lightning-fast, on-device multilingual text-to-speech model supporting English, Korean, Spanish, Portuguese, and French. It offers extreme performance with minimal overhead, achieving up to 167x faster than real-time inference and optimized for privacy-focused applications.

`text-to-speech`

⬇️ 11,904 • ❤️ 272 • 11d ago

---

**[LTXV2_comfy](https://huggingface.co/Kijai/LTXV2_comfy)**

*Jukka Seppänen*

LTXV2_comfy is a separated checkpoint model designed for ComfyUI, enabling an alternative method for loading LTX2 models. It is compatible with LTX2 GGUFs that include metadata, though it may require a specific PR for ComfyUI-GGUF nodes.

`18.9B`

⬇️ 51,565 • ❤️ 296 • 2d ago

---

**[Qwen3-VL-Embedding-8B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B)**

*Qwen*

Qwen3-VL-Embedding-8B is a multimodal embedding model that generates high-dimensional vectors from text, images, and videos for tasks like retrieval and clustering. It supports over 30 languages and customizable embedding dimensions, enabling efficient cross-modal understanding and search.

`image-to-text` `8.1B`

⬇️ 42,243 • ❤️ 268 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](https://huggingface.co/papers/2601.07372)**

*Xin Cheng, Wangding Zeng, Damai Dai et al. (14 authors)*

Conditional memory via Engram module enhances Transformer models by enabling efficient knowledge lookup and improving reasoning capabilities through optimized sparsity allocation.

▲ 19 • 💬 1 • ⭐ 2,670 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2601.07372) • [💻 code](https://github.com/deepseek-ai/Engram)

---

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 183 • 💬 5 • ⭐ 5,120 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[Urban Socio-Semantic Segmentation with Vision-Language Reasoning](https://huggingface.co/papers/2601.10477)**

*Yu Wang, Yi Wang, Rui Dai et al. (7 authors)*

🏢 alibaba-inc

Urban socio-semantic segmentation is achieved through a vision-language model framework that combines cross-modal recognition and multi-stage reasoning with reinforcement learning optimization.

▲ 143 • 💬 3 • ⭐ 130 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2601.10477) • [💻 code](https://github.com/AMAP-ML/SocioReasoner)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 20 • 💬 3 • ⭐ 15,451 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233)**

*Yoav HaCohen, Benny Brazowski, Nisan Chiprut et al. (29 authors)*

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.

▲ 121 • 💬 3 • ⭐ 2,615 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2601.03233) • [💻 code](https://github.com/Lightricks/LTX-2) • [🔗 project](https://app.ltx.studio/ltx-2-playground/i2v)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 135 • 💬 19 • ⭐ 50,313 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://huggingface.co/papers/2601.02553)**

*Jiaqi Liu, Yaofeng Su, Peng Xia et al. (8 authors)*

To support reliable long-term interaction in complex environments, LLM agents require memory systems that efficiently manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which applies entropy-aware filtering to distill unstructured interactions into compact, multi-view indexed memory units; (2) Recursive Memory Consolidation, an asynchronous process that integrates related units into higher-level abstract representations to reduce redundancy; and (3) Adaptive Query-Aware Retrieval, which dynamically adjusts retrieval scope based on query complexity to construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.

▲ 28 • 💬 2 • ⭐ 1,213 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2601.02553) • [💻 code](https://github.com/aiming-lab/SimpleMem) • [🔗 project](https://aiming-lab.github.io/SimpleMem-Page/)

---

**[Action100M: A Large-scale Video Action Dataset](https://huggingface.co/papers/2601.10592)**

*Delong Chen, Tejaswi Kasarla, Yejin Bang et al. (9 authors)*

🏢 Meta Research

Action100M is a large-scale video action dataset constructed from internet instructional videos using automated pipelines with V-JEPA embeddings and GPT-based reasoning for structured annotations.

▲ 11 • 💬 1 • ⭐ 105 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2601.10592) • [💻 code](https://github.com/facebookresearch/Action100M)

---

**[LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models](https://huggingface.co/papers/2403.13372)**

*Yaowei Zheng, Richong Zhang, Junhao Zhang et al. (5 authors)*

LlamaFactory is a unified framework enabling efficient fine-tuning of large language models across various tasks using a web-based user interface.

▲ 176 • 💬 6 • ⭐ 65,909 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.13372) • [💻 code](https://github.com/hiyouga/LLaMA-Factory) • [🔗 project](https://huggingface.co/spaces/hiyouga/LLaMA-Board)

---

**[MediaPipe: A Framework for Building Perception Pipelines](https://huggingface.co/papers/1906.08172)**

*Camillo Lugaresi, Jiuqiang Tang, Hadon Nash et al. (14 authors)*

MediaPipe framework facilitates the development of perception applications by providing tools for combining components, prototyping, and measuring performance across platforms.

▲ 2 • 💬 0 • ⭐ 33,302 • 80mo ago

[🎓 arXiv](https://arxiv.org/abs/1906.08172) • [💻 code](https://github.com/google-ai-edge/mediapipe)

---

---

## GitHub Repositories: "ai"

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 8.9k • 🔱 1.2k • 6h ago

---

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 7.0k • 🔱 330 • 16h ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 5.6k • 🔱 251 • 6h ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 4.5k • 🔱 605 • 9d ago

---

**[nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio)**

Stop juggling AI accounts. Quotio is a beautiful native macOS menu bar app that unifies your Claude, Gemini, OpenAI, Qwen, and Antigravity subscriptions – with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid.

`Swift` `ai-tools` `developer-tools` `proxy` `quota-monitor`

⭐ 2.7k • 🔱 163 • 2h ago

---

**[chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)**

🎬 火宝短剧 - 基于AI的一站式短剧生成平台 《一句话生成完整短剧，从剧本到成片全自动化》  Huobao Drama - An AI-Powered End-to-End Short Drama Generator "One Sentence to Complete Drama: Fully Automated from Script to Final Video"

`Vue`

⭐ 2.5k • 🔱 473 • 22h ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 2.3k • 🔱 2.3k • 58m ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 2.2k • 🔱 245 • 1d ago

---

**[datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)**

Vibe coding from 0 to 1 ｜零基础也能学会的 AI 编程实战｜首个交互式教程｜把想法做成真正能上线的产品

`JavaScript` `agent` `ai` `coding` `course` `gemini`

⭐ 1.7k • 🔱 134 • 21h ago

---

**[DevAgentForge/Claude-Cowork](https://github.com/DevAgentForge/Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 1.6k • 🔱 236 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
