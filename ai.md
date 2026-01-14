---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-14T22:48:50.092980+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** January 14, 2026 at 22:48 UTC  
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

**[Senate passes bill letting victims sue over Grok AI explicit images](https://www.reddit.com/r/artificial/comments/1qcpxzs/senate_passes_bill_letting_victims_sue_over_grok/)**

The US Senate backs new civil rights for victims of AI-generated sexual abuse as lawmakers confront misuse of Elon Musk's Grok chatbot on X.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/us-senate-passes-grok-ai-explicit-images-bill) • 7h ago

---

**[Bandcamp bans purely AI-generated music from its platform](https://www.reddit.com/r/artificial/comments/1qd11nu/bandcamp_bans_purely_aigenerated_music_from_its/)**

Indie music store says it wants fans to have confidence music was largely made by humans.

🔗 [Ars Technica](https://arstechnica.com/ai/2026/01/bandcamp-bans-purely-ai-generated-music-from-its-platform/) • 41m ago

---

**[Google went from being "disrupted" by ChatGPT, to having the best LLM as well as rivalling Nvidia in hardware (TPUs). The narrative has changed](https://www.reddit.com/r/artificial/comments/1qcfcm6/google_went_from_being_disrupted_by_chatgpt_to/)**

The public narrative around Google has changed significantly over the past 1 year. (I say public, because people who were closely following google probably saw this coming). Since Google's revenue primarily comes from ads, LLMs eating up that market share questioned their future revenue potential. Then there was this whole saga of selling the Chrome browser. But they made a great comeback with the Gemini 3 and also TPUs being used for training it. Now the narrative is that Google is the best position company in the AI era.

🔗 [decodingthefutureresearch.substack.com](https://decodingthefutureresearch.substack.com/p/how-has-the-narrative-around-google) • 16h ago

---

**[Gemini can now scan your photos, email, and more to provide better answers | The feature will start with paid users only, and it’s off by default.](https://www.reddit.com/r/artificial/comments/1qcwigc/gemini_can_now_scan_your_photos_email_and_more_to/)**

The feature will start with paid users only, and it's off by default.

🔗 [Ars Technica](https://arstechnica.com/google/2026/01/gemini-can-now-scan-your-photos-email-and-more-to-provide-better-answers/) • 3h ago

---

**[How do you use AI but not be known but, it can reference and be aware of your past questions?](https://www.reddit.com/r/artificial/comments/1qd02jc/how_do_you_use_ai_but_not_be_known_but_it_can/)**

So, some kind of identifier is assigned to you but it or its corporate overlords never know who you are. No cookies, no tracking, etc. Maybe just a white, female, 2 kids, interested in dogs, biking, business, making cakes, etc. So it knows you and is more helpful that way but not who you are specifically. IOW: privately but not total and forgotten anonymity with each session. The only options I can find are to use Apple Intelligence (not ready for prime time, maybe when Gemini is fully integrated…) or create an anonymous Google account while on a VPN (don't have one) and just use that with Gemini. But the second you are off the VPN, Google will connect the dots and know who you are. If I use Apple Private Relay, it will figure me out even faster. A final option is to set up an AI on your Mac. No thanks on that one. It seems like there should be a privacy AI relay which makes an artificial version of you, which the AI thinks is you in Amsterdam or Bogata or Vancouver or Palo Alto but other than working with what you have asked, is not knowing a damn thing about the real you. OK, maybe I need a VPN but, why should I need one for something so simply obvious desired by so many: Privacy. Just wondering how can I remain private in my use of AI but still train it to know me? Simply. On a Mac.

1h ago

---

**[Jeff Bezos Says the AI Bubble is Like the Industrial Bubble](https://www.reddit.com/r/artificial/comments/1qc1dif/jeff_bezos_says_the_ai_bubble_is_like_the/)**

Jeff Bezos: financial bubbles like 2008 are just bad. Industrial bubbles, like biotech in the 90s, can actually benefit society. AI is an industrial bubble, not a financial bubble – and that's an important distinction. Investors may lose money, but when the dust settles, we still get the inventions.

1d ago

---

**[Architecting Autonomy: Modern Design Patterns for AI Assistants](https://www.reddit.com/r/artificial/comments/1qcvi7y/architecting_autonomy_modern_design_patterns_for/)**

In the early days of generative AI, an "assistant" was little more than a text box waiting for a prompt. You typed, the model predicted, and you hoped for the best. But as we move deeper into 2026, the industry has shifted from simple chatbots to sophisticated Agentic Systems.1 The difference lies in Design Patterns. Just as the software industry matured through the adoption of MVC (Model-View-Controller) or Microservices, the AI space is now formalizing the blueprints that make assistants reliable, safe, and truly autonomous. Here are the essential design patterns shaping the next generation of AI assistants. 1. The "Plan-Then-Execute" Pattern Early assistants often "hallucinated" because they began writing an answer before they had a full strategy. The Plan-Then-Execute pattern (often implemented as Reason-and-Act or ReAct) forces the assistant to pause. When a user asks a complex question—like "Analyze our Q3 spending and find three areas for cost reduction"—the assistant doesn't start typing the report. Instead, it creates a Task Decomposition tree: Access the financial database. Filter for Q3 transactions. Categorize expenses. Run a comparison against Q2. By separating the "thinking" (planning) from the "doing" (execution), assistants become significantly more accurate and can handle multi-step workflows without losing the thread. 2. The "Reflective" Pattern (Self-Correction)2 Even the best models make mistakes. The Reflection Pattern introduces a secondary "Critic" loop. In this architecture, the assistant generates an initial output, but before the user sees it, the system passes that output back to itself (or a specialized "Verifier" model) with a prompt: "Check this response for factual errors or compliance violations." If the Verifier finds a mistake, the assistant iterates. This design pattern is the backbone of Safe AI, ensuring that "Shadow AI" behaviors—like leaking internal PII or hallucinating legal clauses—are caught in a private, internal loop before they ever reach the user interface. 3. The "Human-in-the-Loop" (HITL) Gateway As AI assistants move into high-stakes environments like M&A due diligence or medical reporting, total autonomy is often a liability. The HITL Gateway pattern creates mandatory "checkpoints." Rather than the AI executing a wire transfer or finalizing a contract, the pattern requires the assistant to present a Draft & Justification. The Draft: The proposed action. The Justification: A "chain-of-thought" explanation of why it chose this action. The human acts as the final "gatekeeper," clicking "Approve" or "Edit" before the agent proceeds.3 This builds trust and ensures accountability in regulated industries. 4. The Multi-Agent Orchestration (Swarm) Pattern The most powerful assistants today aren't single models; they are teams. In the Orchestration Pattern, a "Manager Agent" receives the user's request and delegates sub-tasks to specialized "Worker Agents."4 For example, a Legal Assistant might consist of: The Researcher: Specialized in searching internal document silos (Vectorization/RAG). The Writer: Specialized in drafting compliant prose. The Auditor: A high-precision model trained specifically on SEC or GDPR guidelines. This modular approach allows developers to "swap" out the Researcher or Auditor as new, better models become available without rebuilding the entire system. 5. The "Context-Aware Memory" Pattern Standard LLMs are "stateless"—they forget who you are the moment the chat ends. Modern assistants use a Stateful Memory Pattern. This involves two layers: Short-Term Memory: Current session context (stored in the prompt window). Long-Term Memory: User preferences, past projects, and "Local Data" (stored in a Vector Database). By using Vectorization to index a user’s history, the assistant can recall that "Project X" refers to the merger discussed three months ago, providing a seamless, personalized experience that feels like a real partnership. The Future: Zero-Trust Design As we look toward the end of 2026, the "Golden Pattern" is becoming Zero-Trust AI Architecture. This pattern assumes that even the model cannot be fully trusted with raw data. It utilizes local redaction agents to scrub sensitive information before the planning and execution loops begin. By implementing these patterns, organizations can move past the "experimental" phase of AI and build robust, enterprise-grade tools that don't just chat, but actually solve problems.

4h ago

---

**[Apple Creator Studio Is Here: A New Creative Suite Challenging Adobe](https://www.reddit.com/r/artificial/comments/1qccvkb/apple_creator_studio_is_here_a_new_creative_suite/)**

Apple Creator Studio launch brings a powerful creative suite for video editing, music production, and design. See pricing, features, AI tools, and creator benefits.

🔗 [techputs](https://techputs.com/apple-creator-studio/) • 19h ago

---

**[Grok and the A.I. Porn Problem](https://www.reddit.com/r/artificial/comments/1qcxxk0/grok_and_the_ai_porn_problem/)**

Elon Musk’s X is living up to its name.

🔗 [The New Yorker](https://www.newyorker.com/culture/infinite-scroll/grok-and-the-ai-porn-problem) • 2h ago

---

**[One-Minute Daily AI News 1/13/2026](https://www.reddit.com/r/artificial/comments/1qcfdh1/oneminute_daily_ai_news_1132026/)**

Slackbot, the automated assistant baked into the Salesforce-owned corporate messaging platform Slack, is entering a new era as an AI agent.[1] Pentagon task force to deploy AI-powered UAS systems to capture drones.[2] Stanford researchers use AI to monitor rare cancer.[3] Anthropic Releases Cowork As Claude’s Local File System Agent For Everyday Work.[4] Sources: [1] https://techcrunch.com/2026/01/13/slackbot-is-an-ai-agent-now/ [2] https://www.defensenews.com/unmanned/2026/01/13/pentagon-task-force-to-deploy-ai-powered-uas-systems-to-capture-drones/ [3] https://www.almanacnews.com/health-care/2026/01/13/stanford-researchers-use-ai-to-monitor-rare-cancer/ [4] https://www.marktechpost.com/2026/01/13/anthropic-releases-cowork-as-claudes-local-file-system-agent-for-everyday-work/

16h ago

---

---

## Google News: "ai"

**[The risks of AI in schools outweigh the benefits, report says](https://www.npr.org/2026/01/14/nx-s1-5674741/ai-schools-education)**

A new report warns that AI poses a serious threat to children's cognitive development and emotional well-being.

NPR • 10h ago

---

**[Can A.I. Generate New Ideas?](https://www.nytimes.com/2026/01/14/technology/ai-ideas-chat-gpt-openai.html)**

The New York Times • 3h ago

---

**[Big Tech plans AI data centers in space: Lonestar to orbit moon by 2028](https://www.foxbusiness.com/video/6387729285112)**

FOX Business correspondent Madison Alworth reports on Lonestar planning A.I. data centers in space, with satellites launching this fall and goals for lunar centers by 2030 on 'Varney & Co.'

Fox Business • 31m ago

---

**[4 key principles of an AI governance and ethics framework](https://www.fastcompany.com/91473566/4-key-principles-of-an-ai-governance-and-ethics-framework)**

Fast Company • 45m ago

---

**[Robotics software maker Skild AI hits $14B valuation](https://finance.yahoo.com/news/robotics-software-maker-skild-ai-161333284.html)**

Skild AI, which is building general-purpose robotic software, just raised a $1.4 billion funding round led by SoftBank.

Yahoo Finance • 6h ago

---

**[Skild AI aims to be the picks and shovels of robotics with $14b valuation](https://www.axios.com/pro/all-deals/2026/01/14/skild-ai-14-billion-valuation)**

Axios • 52m ago

---

**[Skild AI Raises $1.4B, Now Valued Over $14B](https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-%241.4B-Now-Valued-Over-%2414B)**

Business Wire • 7h ago

---

**[AI Can’t Touch These Skilled Trade Jobs. If Only Enough Humans Would Fill Them.](https://www.wsj.com/lifestyle/careers/ai-cant-touch-these-skilled-trade-jobs-if-only-enough-humans-would-fill-them-9f2f05e9?gaa_at=eafs&gaa_n=AWEtsqdQyithGnSInsqy4LIYfHDM4eFpJLmr8rN39zRJz-2_DVtjFomBru6k&gaa_ts=696820aa&gaa_sig=RswlQBVvoky-tpl83yBY2o-nQCWVCiTbyNWfWOinCJs692erspoVDzwQck_Idd7IG2sZA_jIMSMrDZl8eW_azw%3D%3D)**

The Wall Street Journal • 5h ago

---

**[OpenAI partners with Cerebras](https://openai.com/index/cerebras-partnership/)**

OpenAI • 2h ago

---

**[OpenAI Forges $10 Billion Deal With Cerebras for AI Computing](https://www.bloomberg.com/news/articles/2026-01-14/openai-forges-10-billion-deal-with-cerebras-for-ai-computing)**

Bloomberg.com • 53m ago

---

---

## HackerNews: "ai"

**[AI generated music barred from Bandcamp](https://news.ycombinator.com/item?id=46605490)**

⬆️ 915 • 💬 697 • 1d ago • [old.reddit.com](https://old.reddit.com/r/BandCamp/comments/1qbw8ba/ai_generated_music_on_bandcamp/)

---

**[We can't have nice things because of AI scrapers](https://news.ycombinator.com/item?id=46608840)**

⬆️ 449 • 💬 250 • 1d ago • [blog.metabrainz.org](https://blog.metabrainz.org/2025/12/11/we-cant-have-nice-things-because-of-ai-scrapers/)

---

**[Signal leaders warn agentic AI is an insecure, unreliable surveillance risk](https://news.ycombinator.com/item?id=46605553)**

With agentic AI embedded at the OS level, databases storing entire digital lives accessible to malware, tasks whose reliability quickly breaks down at each step, and being opted-in without consent, Signal leadership is sounding the alarm for the industry to pull back until threats can be mitigated.

⬆️ 339 • 💬 102 • 1d ago • [Coywolf](https://coywolf.com/news/productivity/signal-president-and-vp-warn-agentic-ai-is-insecure-unreliable-and-a-surveillance-nightmare/)

---

**[The chess bot on Delta Air Lines will destroy you (2024) [video]](https://news.ycombinator.com/item?id=46593395)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 338 • 💬 335 • 2d ago • [youtube.com](https://www.youtube.com/watch?v=c0mLhHDcY3I)

---

**[Games Workshop bans staff from using AI](https://news.ycombinator.com/item?id=46607681)**

Warhammer maker Games Workshop has banned the use of AI in its content production and its design process, insisting that none of its senior managers are currently excited about the technology.

⬆️ 230 • 💬 125 • 1d ago • [IGN](https://www.ign.com/articles/warhammer-maker-games-workshop-bans-its-staff-from-using-ai-in-its-content-or-designs-says-none-of-its-senior-managers-are-currently-excited-about-the-tech)

---

**[Google removes AI health summaries](https://news.ycombinator.com/item?id=46595419)**

AI Overviews provided false liver test information experts called alarming.

⬆️ 225 • 💬 172 • 1d ago • [Ars Technica](https://arstechnica.com/ai/2026/01/google-removes-some-ai-health-summaries-after-investigation-finds-dangerous-flaws/)

---

**[Let's be honest, Generative AI isn't going all that well](https://news.ycombinator.com/item?id=46605587)**

⬆️ 218 • 💬 296 • 1d ago • [garymarcus.substack.com](https://garymarcus.substack.com/p/lets-be-honest-generative-ai-isnt)

---

**[Show HN: OSS AI agent that indexes and searches the Epstein files](https://news.ycombinator.com/item?id=46611348)**

Search the Epstein archive — an AI agent grounded in indexed emails, messages, and documents, powered by Nia

⬆️ 199 • 💬 89 • 20h ago • [epstein.trynia.ai](https://epstein.trynia.ai/)

---

**[Mozilla's open source AI strategy](https://news.ycombinator.com/item?id=46599897)**

The future of intelligence is being set right now, and the path we’re on leads somewhere I don’t want to go. We’re drifting toward a worl

⬆️ 189 • 💬 199 • 1d ago • [blog.mozilla.org](https://blog.mozilla.org/en/mozilla/mozilla-open-source-ai-strategy/)

---

**[Ai, Japanese chimpanzee who counted and painted dies at 49](https://news.ycombinator.com/item?id=46585947)**

Ai's cognitive abilities had been studied extensively since she was brought to a Japanese institute in 1977.

⬆️ 189 • 💬 64 • 2d ago • [bbc.com](https://www.bbc.com/news/articles/cj9r3zl2ywyo)

---

---

## YouTube Videos: "ai"

**[we just arrived at the &quot;WTF&quot; moment in AI](https://www.youtube.com/watch?v=N8I2wYXt4m8)**

GPT 5.2 just solved the Erdos Problems. Terence Tao confirms. We're officially at the "WTF" moment in AI development. The latest ...

📺 Wes Roth

👁️ 98K • 👍 3K • 💬 725 • ⏱️ 23:05 • 2d ago

---

**[Anthropic: Our AI just created a tool that can ‘automate all white collar work’, Me:](https://www.youtube.com/watch?v=wYs6HWZ2FdM)**

A new tool, with code written *only* by AI, has gone omega-viral: Claude Cowork. But is the hype justified? What do the stats say ...

📺 AI Explained

👁️ 27K • 👍 1K • 💬 241 • ⏱️ 19:03 • 6h ago

---

**[OpenAI Just Dropped GPT HEALTH And People Are Freaking Out](https://www.youtube.com/watch?v=sPl_jYF8E5k)**

OpenAI just launched ChatGPT Health — a dedicated health and wellness space inside ChatGPT — and it pushes ChatGPT into ...

📺 AI Revolution

👁️ 58K • 👍 2K • 💬 203 • ⏱️ 14:42 • 1d ago

---

**[The AI Endgame](https://www.youtube.com/watch?v=rqR7z2eHOBE)**

The tech oligarchs want to RETVRN. If you like my stuff, consider supporting me on Patreon, which will give you early access to ...

📺 Adam Something

👁️ 338K • 👍 31K • 💬 4K • ⏱️ 11:40 • 1d ago

---

**[Microsoft Shocks AI World: &quot;China AI Is Now Too Powerful&quot;](https://www.youtube.com/watch?v=vcUBUQOyzFI)**

Microsoft just issued a warning that reframes the AI race: outside the West, China is gaining fast through scale, affordability, and ...

📺 AI Revolution

👁️ 36K • 👍 1K • 💬 149 • ⏱️ 14:32 • 23h ago

---

**[MARIO.AI](https://www.youtube.com/watch?v=pOAmybui4Zs)**

DISCLAIMER: This game has ZERO usage of AI and was 100% made entirely by a team of real people nor does it have affiliation ...

📺 Luigikid Gaming

👁️ 11K • 👍 937 • 💬 76 • ⏱️ 11:30 • 1d ago

---

**[Wired&#39;s Steven Levy on DeepSeek&#39;s latest AI model, state of AI tech race](https://www.youtube.com/watch?v=_67YjLqjYbk)**

Steven Levy, Wired editor-at-large, joins 'Squawk Box' to discuss what to expect from Chinese AI startup DeepSeek's latest model, ...

📺 CNBC Television

👁️ 65K • 👍 492 • 💬 118 • ⏱️ 7:57 • 2d ago

---

**[Which One is AI?](https://www.youtube.com/watch?v=1ttPxy5d1xg)**

ZoomPartner Which one do you think it is? So excited to host this Live Event with Zoom please sign up and tell your school so we ...

📺 Rebecca Zamolo

👁️ 567K • 👍 7K • 💬 328 • ⏱️ 0:23 • 2d ago

---

**[Create Hollywood-Level Short Films Using Nano Banana Pro + Higgsfield AI](https://www.youtube.com/watch?v=1zcAjI3hBAc)**

Try Higgsfield AI: https://goto.higgsfield.ai/19xgJx This video is a masterclass in AI cinematography. I'm breaking down the exact ...

📺 WealthWise

👁️ 2K • 👍 122 • 💬 8 • ⏱️ 9:36 • 11h ago

---

**[Open Source AI Agents Just Got Too Powerful: Confucius AI Agent](https://www.youtube.com/watch?v=GnQCyxa4TjA)**

Meta and Harvard just released an open-source coding agent called Confucius Code Agent, built on top of the Confucius SDK, ...

📺 AI Revolution

👁️ 42K • 👍 1K • 💬 57 • ⏱️ 14:29 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen-Image-Edit-2511-Multiple-Angles-LoRA](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA)**

*fal*

This LoRA fine-tunes Qwen-Image-Edit-2511 for precise multi-angle image generation, offering 96 camera poses (4 elevations, 8 azimuths, 3 distances) trained on Gaussian Splatting data for 3D consistency. It enables detailed control over camera viewpoints, including low-angle shots, for advanced image editing and content creation.

`image-to-image`

⬇️ 36,933 • ❤️ 625 • 7d ago

---

**[LTX-2](https://huggingface.co/Lightricks/LTX-2)**

*Lightricks*

LTX-2 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs including images, text, and audio. It supports local execution and offers distilled and upscaler checkpoints for practical applications.

`image-to-video`

⬇️ 1,064,063 • ❤️ 992 • 4h ago

---

**[GLM-Image](https://huggingface.co/zai-org/GLM-Image)**

*Z.ai*

GLM-Image is a text-to-image model with a hybrid autoregressive + diffusion decoder architecture, excelling in text rendering and knowledge-intensive generation. It supports both text-to-image and image-to-image tasks including editing and style transfer.

`text-to-image`

⬇️ 203 • ❤️ 496 • 16h ago

---

**[nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)**

*NVIDIA*

Nemotron-Speech-Streaming-En-0.6b is a 600M parameter English ASR model featuring a cache-aware FastConformer-RNNT architecture for low-latency streaming and high-throughput batch processing. It supports dynamic chunk sizes, punctuation, and capitalization, making it ideal for real-time applications like voice assistants and live captioning.

`automatic-speech-recognition`

⬇️ 3,897 • ❤️ 366 • 8d ago

---

**[AgentCPM-Explore](https://huggingface.co/openbmb/AgentCPM-Explore)**

*OpenBMB*

AgentCPM-Explore is a 4B parameter agent foundation model excelling in long-horizon tasks across 8 benchmarks like GAIA and BrowserComp. It features over 100 rounds of continuous interaction, multi-source validation, and dynamic strategy adjustment for on-device deep research.

`text-generation` `4.0B`

⬇️ 77 • ❤️ 254 • 13h ago

---

**[LTXV2_comfy](https://huggingface.co/Kijai/LTXV2_comfy)**

*Jukka Seppänen*

LTXV2_comfy is a separated checkpoint model designed for ComfyUI, enabling an alternative method for loading LTX2 models. It is compatible with LTX2 GGUFs that include metadata, though it may require a specific PR for ComfyUI-GGUF nodes.

`18.9B`

⬇️ 32,276 • ❤️ 253 • 2h ago

---

**[Qwen3-VL-Embedding-8B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B)**

*Qwen*

Qwen3-VL-Embedding-8B is a multimodal embedding model that generates high-dimensional vectors from text, images, and videos for tasks like retrieval and clustering. It supports over 30 languages and customizable embedding dimensions, enabling efficient cross-modal understanding and search.

`image-to-text` `8.1B`

⬇️ 26,915 • ❤️ 239 • 5d ago

---

**[HyperCLOVAX-SEED-Think-32B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B)**

*HyperCLOVA X*

HyperCLOVAX-SEED-Think-32B is a 32B parameter vision-language model capable of multimodal understanding (text, image, video) with a 128K token context length. It excels at Korean-centric reasoning and offers an optional 'thinking mode' for deep, controllable analysis, making it suitable for complex agentic tasks and advanced multimodal QA.

`text-generation` `33.3B`

⬇️ 31,045 • ❤️ 377 • 8d ago

---

**[LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)**

*Liquid AI*

LFM2.5-1.2B-Instruct is a 1.2B parameter instruction-tuned language model optimized for on-device deployment, offering fast edge inference and supporting multiple languages. It excels at agentic tasks and data extraction, with a context length of 32,768 tokens.

`text-generation` `1.2B`

⬇️ 22,649 • ❤️ 332 • 5d ago

---

**[Qwen3-VL-Embedding-2B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B)**

*Qwen*

Qwen3-VL-Embedding-2B is a 2B parameter multimodal embedding model that generates high-dimensional vectors for text, images, and videos. It excels at cross-modal understanding and retrieval tasks, supporting over 30 languages and customizable embedding dimensions for flexible integration.

`image-to-text` `2.1B`

⬇️ 28,833 • ❤️ 212 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](https://huggingface.co/papers/2601.07372)**

*Xin Cheng, Wangding Zeng, Damai Dai et al. (14 authors)*

Conditional memory via Engram module enhances Transformer models by enabling efficient knowledge lookup and improving reasoning capabilities through optimized sparsity allocation.

▲ 4 • 💬 1 • ⭐ 2,042 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2601.07372) • [💻 code](https://github.com/deepseek-ai/Engram)

---

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 178 • 💬 5 • ⭐ 4,848 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233)**

*Yoav HaCohen, Benny Brazowski, Nisan Chiprut et al. (29 authors)*

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.

▲ 109 • 💬 3 • ⭐ 2,404 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2601.03233) • [💻 code](https://github.com/Lightricks/LTX-2) • [🔗 project](https://app.ltx.studio/ltx-2-playground/i2v)

---

**[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://huggingface.co/papers/2601.02553)**

*Jiaqi Liu, Yaofeng Su, Peng Xia et al. (8 authors)*

To support reliable long-term interaction in complex environments, LLM agents require memory systems that efficiently manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which applies entropy-aware filtering to distill unstructured interactions into compact, multi-view indexed memory units; (2) Recursive Memory Consolidation, an asynchronous process that integrates related units into higher-level abstract representations to reduce redundancy; and (3) Adaptive Query-Aware Retrieval, which dynamically adjusts retrieval scope based on query complexity to construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.

▲ 26 • 💬 2 • ⭐ 1,034 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2601.02553) • [💻 code](https://github.com/aiming-lab/SimpleMem) • [🔗 project](https://aiming-lab.github.io/SimpleMem-Page/)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 3 • 💬 0 • ⭐ 28,606 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

**[Multi-Agent Software Development through Cross-Team Collaboration](https://huggingface.co/papers/2406.08979)**

*Zhuoyun Du, Chen Qian, Wei Liu et al. (8 authors)*

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.

▲ 0 • 💬 0 • ⭐ 28,624 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.08979) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 131 • 💬 19 • ⭐ 50,009 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models](https://huggingface.co/papers/2403.13372)**

*Yaowei Zheng, Richong Zhang, Junhao Zhang et al. (5 authors)*

LlamaFactory is a unified framework enabling efficient fine-tuning of large language models across various tasks using a web-based user interface.

▲ 176 • 💬 6 • ⭐ 65,695 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.13372) • [💻 code](https://github.com/hiyouga/LLaMA-Factory) • [🔗 project](https://huggingface.co/spaces/hiyouga/LLaMA-Board)

---

**[ArenaRL: Scaling RL for Open-Ended Agents via Tournament-based Relative Ranking](https://huggingface.co/papers/2601.06487)**

*Qiang Zhang, Boli Chen, Fanrui Zhang et al. (17 authors)*

🏢 Alibaba-NLP

Reinforcement learning for large language model agents suffers from discrimination collapse in open-ended tasks due to pointwise scalar scoring, which ArenaRL addresses through relative ranking and pairwise evaluation mechanisms.

▲ 29 • 💬 1 • ⭐ 41 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2601.06487) • [💻 code](https://github.com/Alibaba-NLP/qqr) • [🔗 project](https://tongyi-agent.github.io/blog/arenarl/)

---

**[Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking](https://huggingface.co/papers/2601.04720)**

*Mingxin Li, Yanzhao Zhang, Dingkun Long et al. (12 authors)*

🏢 Qwen

The Qwen3-VL-Embedding and Qwen3-VL-Reranker models form an end-to-end multimodal search pipeline, leveraging multi-stage training and cross-attention mechanisms to achieve high-precision retrieval across diverse modalities.

▲ 38 • 💬 2 • ⭐ 707 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2601.04720) • [💻 code](https://github.com/QwenLM/Qwen3-VL-Embedding)

---

---

## GitHub Repositories: "ai"

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 8.5k • 🔱 1.1k • 2h ago

---

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 4.8k • 🔱 198 • 18h ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 3.9k • 🔱 520 • 7d ago

---

**[nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio)**

Stop juggling AI accounts. Quotio is a beautiful native macOS menu bar app that unifies your Claude, Gemini, OpenAI, Qwen, and Antigravity subscriptions – with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid.

`Swift` `ai-tools` `developer-tools` `proxy` `quota-monitor`

⭐ 2.4k • 🔱 145 • 7h ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 2.1k • 🔱 234 • 3d ago

---

**[datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)**

Learn vibe coding from 0 to 1 | 实战中从零学会 AI 编程｜产品思维、前后端开发

`JavaScript` `agent` `ai` `coding` `course` `gemini`

⭐ 1.6k • 🔱 130 • 11h ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A 股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 1.4k • 🔱 1.1k • 8h ago

---

**[GuDaStudio/skills](https://github.com/GuDaStudio/skills)**

This repository contains a collection of Agent Skills developed by GudaStudio, enabling seamless collaboration between Claude and other AI models and tools.

`PowerShell`

⭐ 1.4k • 🔱 76 • 22d ago

---

**[numman-ali/cc-mirror](https://github.com/numman-ali/cc-mirror)**

Create multiple isolated Claude Code variants with custom providers (Z.ai, MiniMax, OpenRouter, LiteLLM)

`TypeScript`

⭐ 1.4k • 🔱 117 • 2d ago

---

**[heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)**

A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

`agent-skills` `ai-agents` `ai-development` `anthropic` `automation`

⭐ 1.2k • 🔱 90 • 16d ago

---

---

*Generated by PeekDeck - A glance is all you need*
