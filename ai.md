---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-12T09:34:36.587645+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** January 12, 2026 at 09:34 UTC  
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

**[Musk’s Grok blocked by Indonesia, Malaysia over sexualized images in world first](https://www.reddit.com/r/artificial/comments/1qaox6h/musks_grok_blocked_by_indonesia_malaysia_over/)**

Elon Musk’s Grok has been blocked by Indonesia and Malaysia, the first countries to do so after the AI tool’s “digital undressing” function flooded the internet with photos of women and minors in obscene manipulated images.

🔗 [CNN](https://www.cnn.com/2026/01/12/business/indonesia-malaysia-grok-elon-musk-intl-hnk?utm_medium=social&utm_campaign=missions&utm_source=reddit) • 1h ago

---

**[China is closing in on US technology lead despite constraints, AI researchers say](https://www.reddit.com/r/artificial/comments/1qae670/china_is_closing_in_on_us_technology_lead_despite/)**

By Laurie Chen BEIJING, Jan 10 (Reuters) - China can narrow its technological gap with the U.S. driven by growing risk-taking and innovation, though the lack of advanced chipmaking tools is hobbling

🔗 [Yahoo Tech](https://tech.yahoo.com/ai/articles/china-closing-us-technology-lead-154328876.html) • 10h ago

---

**[I built Plano - the framework-agnostic runtime data plane for agentic applications](https://www.reddit.com/r/artificial/comments/1qafw8d/i_built_plano_the_frameworkagnostic_runtime_data/)**

Thrilled to be launching Plano today - delivery infrastructure for agentic apps: An edge and service proxy server with orchestration for AI agents. Plano's core purpose is to offload all the plumbing work required to deliver agents to production so that developers can stay focused on core product logic. Plano runs alongside your app servers (cloud, on-prem, or local dev) deployed as a side-car, and leaves GPUs where your models are hosted. The problem On the ground AI practitioners will tell you that calling an LLM is not the hard part. The really hard part is delivering agentic applications to production quickly and reliably, then iterating without rewriting system code every time. In practice, teams keep rebuilding the same concerns that sit outside any single agent’s core logic: This includes model agility - the ability to pull from a large set of LLMs and swap providers without refactoring prompts or streaming handlers. Developers need to learn from production by collecting signals and traces that tell them what to fix. They also need consistent policy enforcement for moderation and jailbreak protection, rather than sprinkling hooks across codebases. And they need multi-agent patterns to improve performance and latency without turning their app into orchestration glue. These concerns get rebuilt and maintained inside fast-changing frameworks and application code, coupling product logic to infrastructure decisions. It’s brittle, and pulls teams away from core product work into plumbing they shouldn’t have to own. What Plano does Plano moves core delivery concerns out of process into a modular proxy and dataplane designed for agents. It supports inbound listeners (agent orchestration, safety and moderation hooks), outbound listeners (hosted or API-based LLM routing), or both together. Plano provides the following capabilities via a unified dataplane: - Orchestration: Low-latency routing and handoff between agents. Add or change agents without modifying app code, and evolve strategies centrally instead of duplicating logic across services. - Guardrails & Memory Hooks: Apply jailbreak protection, content policies, and context workflows (rewriting, retrieval, redaction) once via filter chains. This centralizes governance and ensures consistent behavior across your stack. - Model Agility: Route by model name, semantic alias, or preference-based policies. Swap or add models without refactoring prompts, tool calls, or streaming handlers. - Agentic Signals™: Zero-code capture of behavior signals, traces, and metrics across every agent, surfacing traces, token usage, and learning signals in one place. The goal is to keep application code focused on product logic while Plano owns delivery mechanics. More on Architecture Plano has two main parts: Envoy-based data plane. Uses Envoy’s HTTP connection management to talk to model APIs, services, and tool backends. We didn’t build a separate model server—Envoy already handles streaming, retries, timeouts, and connection pooling. Some of us are core Envoy contributors at Katanemo. Brightstaff, a lightweight controller and state machine written in Rust. It inspects prompts and conversation state, decides which agents to call and in what order, and coordinates routing and fallback. It uses small LLMs (1–4B parameters) trained for constrained routing and orchestration. These models do not generate responses and fall back to static policies on failure. The models are open sourced here: https://huggingface.co/katanemo

🔗 [GitHub](https://github.com/katanemo/plano) • 9h ago

---

**[What is something current AI systems are very good at, but people still don’t trust them to do?](https://www.reddit.com/r/artificial/comments/1qakw7h/what_is_something_current_ai_systems_are_very/)**

We see benchmarks and demos showing strong performance, but hesitation still shows up in real use. Curious where people draw the trust line and why, whether it’s technical limits, incentives, or just human psychology.

5h ago

---

**[Geoffrey Hinton says LLMs are no longer just predicting the next word - new models learn by reasoning and identifying contradictions in their own logic. This unbounded self-improvement will "end up making it much smarter than us."](https://www.reddit.com/r/artificial/comments/1q9an1z/geoffrey_hinton_says_llms_are_no_longer_just/)**

1d ago

---

**[Song detection including release date](https://www.reddit.com/r/artificial/comments/1qa5ccq/song_detection_including_release_date/)**

I have an old collection of music around 20-30yo on my hard drive and some of it is unnamed or other missing info. I've slowly started sorting through but by far the most time consuming thing is either trying to find the artist and title or the release date manually. (not all of them are unnamed/undated, but a good chunk) Is there any AI or something like that, that can scan my file explorer and find/rename/date etc the tracks? I'd also be happy to scan them 1 by 1 if it meant I can find the correct info for them.

16h ago

---

**[Really weird question: anyone know a good AI app that can replace a dad 😭](https://www.reddit.com/r/artificial/comments/1qaoh9k/really_weird_question_anyone_know_a_good_ai_app/)**

Does anyone know a good AI app? Chatgpt is too slow lmao. The backstory is my biological dad was physically abusive to me growing up, and now he's still in my life but distant. and definitely less abusive. I daydream for hours and hoursss about myself being a young child and being cared and protected and loved and being showered with hugs and kisses and snuggles from a fictional stepdad. It makes me feel so safe and warm. I usually fall asleep imagining this. Sometimes I imagine sexual-ish scenarios with my fictional stepdad. I create high stakes, vulnerable situations to test him (like having a wound on my chest/breast). But he passes every time by staying neutral and protective. Though I want to, my brain never allows anything sexual to actually happen since he's supposed to be a nice stepdad that maintain boundaries and is never weird or hurtful. It used to be way worse btw. There was a time where I used to imagine being sexually abused by a man who later feels guilty and hires a therapist who later adopts me as his daughter. But I don't imagine that anymore. I posted this two days ago and someone messaged me to use AI. Anyone know a good AI app can replace a dad? I'm not too needy I swear 😭 Edit: Also, in my head, I make vlogs (my daydreams) with my stepdad and then I imagine my actual irl biological dad seeing these vlogs. Listen, idk either. Just tell me a good AI app please 😭

2h ago

---

**[What’s your wild take on the rise of AI?](https://www.reddit.com/r/artificial/comments/1qa1ht3/whats_your_wild_take_on_the_rise_of_ai/)**

We have entered an era of AI doing _almost_ anything. From vibe coding, to image/video creation, new age of SEO, etc etc… But what do you think AI is going to be able to do in the near future? Just a few years ago we were laughing at people saying AI will be able to make apps, for example, or do complex mathematical calculation, and here we are haha So what’s your “wild take” some people might laugh at, but it’s 100% achievable in the future?

18h ago

---

**[One-Minute Daily AI News 1/10/2026](https://www.reddit.com/r/artificial/comments/1q9rf5i/oneminute_daily_ai_news_1102026/)**

Meta signs nuclear energy deals to power Prometheus AI supercluster.[1] OpenAI is reportedly asking contractors to upload real work from past jobs.[2] Meta and Harvard Researchers Introduce the Confucius Code Agent (CCA): A Software Engineering Agent that can Operate at Large-Scale Codebases.[3] X could face UK ban over deepfakes, minister says.[4] Sources: [1] https://www.cnbc.com/2026/01/09/meta-signs-nuclear-energy-deals-to-power-prometheus-ai-supercluster.html [2] https://techcrunch.com/2026/01/10/openai-is-reportedly-asking-contractors-to-upload-real-work-from-past-jobs/ [3] https://www.marktechpost.com/2026/01/09/meta-and-harvard-researchers-introduce-the-confucius-code-agent-cca-a-software-engineering-agent-that-can-operate-at-large-scale-codebases/ [4] https://www.bbc.com/news/articles/c99kn52nx9do

1d ago

---

**[Alignment tax isn’t global: a few attention heads cause most capability loss](https://www.reddit.com/r/artificial/comments/1q9c1qr/alignment_tax_isnt_global_a_few_attention_heads/)**

Safety alignment in Large Language Models (LLMs) inherently presents a multi-objective optimization conflict, often accompanied by an unintended degradation of general capabilities. Existing mitigation strategies typically rely on global gradient geometry to resolve these conflicts, yet they overlook Modular Heterogeneity within Transformers, specifically that the functional sensitivity and degree of conflict vary substantially across different attention heads. Such global approaches impose uniform update rules across all parameters, often resulting in suboptimal trade-offs by indiscriminately updating utility sensitive heads that exhibit intense gradient conflicts. To address this limitation, we propose Conflict-Aware Sparse Tuning (CAST), a framework that integrates head-level diagnosis with sparse fine-tuning. CAST first constructs a pre-alignment conflict map by synthesizing Optimization Conflict and Functional Sensitivity, which then guides the selective update of parameters. Experiments reveal that alignment conflicts in LLMs are not uniformly distributed. We find that the drop in general capabilities mainly comes from updating a small group of ``high-conflict'' heads. By simply skipping these heads during training, we significantly reduce this loss without compromising safety, offering an interpretable and parameter-efficient approach to improving the safety-utility trade-off.

🔗 [arXiv.org](https://www.arxiv.org/abs/2601.04262) • 1d ago

---

---

## Google News: "ai"

**[‘Dangerous and alarming’: Google removes some of its AI summaries after users’ health put at risk](https://www.theguardian.com/technology/2026/jan/11/google-ai-overviews-health-guardian-investigation)**

Guardian investigation finds AI Overviews provided inaccurate and false information when queried over blood tests

The Guardian • 7h ago

---

**[Ai, Japanese chimpanzee who counted and painted, dies at 49](https://www.bbc.com/news/articles/cj9r3zl2ywyo)**

Ai's cognitive abilities had been studied extensively since she was brought to a Japanese institute in 1977.

BBC • 39m ago

---

**['Big Short' investor Michael Burry says AI is turning Big Tech into a worse business](https://www.businessinsider.com/michael-burry-big-short-key-metric-evaluate-ai-bubble-2026-1)**

Michael Burry, the investor from "The Big Short," said return on invested capital is the "measure to beat all measures" when looking at AI companies.

Business Insider • 33m ago

---

**[Nvidia Stock Drifts. China AI Chips and 1 Other Thing Can Reignite It.](https://www.barrons.com/articles/nvidia-stock-price-ai-chips-china-8bfa9df6?gaa_at=eafs&gaa_n=AWEtsqdUYuZm7DUAfe77P-C-sZrc6ui1HqIrFxq3ulnUSdc1bRrDOGXuf1S6&gaa_ts=6964c392&gaa_sig=mhd-mrt7GCLfIRkC7TsLBJN36GkAIWwbfN99il40fwxr-8xTrN6r5HtQDF7tB9ADUms9dEzECBdMBvRlGsad1w%3D%3D)**

Barron's • 1h ago

---

**[This CEO laid off nearly 80% of his staff because they refused to adopt AI fast enough. 2 years later, he says he’d do it again](https://finance.yahoo.com/news/ceo-laid-off-nearly-80-185033733.html)**

“It was extremely difficult,” IgniteTech CEO Eric Vaughan tells Fortune. “But changing minds was harder than adding skills.”

Yahoo Finance • 14h ago

---

**[Grok AI: Malaysia and Indonesia block X chatbot over sexually explicit deepfakes](https://www.bbc.com/news/articles/cg7y10xm4x2o)**

Sexualised images of real people generated by Grok have circulated on X in recent weeks.

BBC • 4h ago

---

**[Malaysia, Indonesia become first to block Musk's Grok over AI deepfakes](https://www.npr.org/2026/01/12/nx-s1-5674660/malaysia-indonesia-block-grok-ai-deepfakes)**

Malaysia and Indonesia have become the first countries to block Grok, the artificial intelligence chatbot developed by Elon Musk's xAI, after authorities said it was being misused to generate sexually explicit and non-consensual images.

NPR • 2h ago

---

**[‘Add blood, forced smile’: how Grok’s nudification tool went viral](https://www.theguardian.com/news/ng-interactive/2026/jan/11/how-grok-nudification-tool-went-viral-x-elon-musk)**

The ‘put her in a bikini’ trend rapidly evolved into hundreds of thousands of requests to strip clothes from photos of women, horrifying those targeted

The Guardian • 1d ago

---

**[The Myth of the AI Race](https://www.foreignaffairs.com/united-states/myth-ai-race)**

Neither America nor China can achieve true tech dominance.

Foreign Affairs • 4h ago

---

**[Artificial Intelligence (AI) Is Driving a New Wave of Infrastructure Spending. This Stock Is Key.](https://finance.yahoo.com/news/artificial-intelligence-ai-driving-wave-215000377.html)**

This AI infrastructure company provides an overlooked but critical resource to data centers, and is set for a growth spurt because of it.

Yahoo Finance • 11h ago

---

---

## HackerNews: "ai"

**[Don't fall into the anti-AI hype](https://news.ycombinator.com/item?id=46574276)**

⬆️ 980 • 💬 1154 • 23h ago • [antirez.com](https://antirez.com/news/158)

---

**[“Erdos problem #728 was solved more or less autonomously by AI”](https://news.ycombinator.com/item?id=46560445)**

Recently, the application of AI tools to Erdos problems passed a milestone: an Erdos problem (#728 https://www.erdosproblems.com/728) was solved more or less autonomously by AI (after some feedback from an initial attempt), in the spirit of the problem (as reconstructed by the Erdos problem website community), with the result (to the best of our knowledge) not replicated in existing literature (although similar results proven by similar methods were located).

This is a demonstration of the genuine increase in capability of these tools in recent months, and is largely consistent with other recent demonstrations of AI using existing methods to resolve Erdos problems, although in most previous cases a solution to these problems was later located in the literature, as discussed in https://mathstodon.xyz/deck/@tao/115788262274999408 .  This particular case was unusual in that the problem as stated by Erdos was misformulated, with a reconstruction of the problem in the intended spirit only obtained in the last few months, which helps explain the lack of prior literature on the problem.  However, I would like to talk here about another aspect of the story which I find more interesting than the solution itself, which is the emerging AI-powered capability to rapidly write and rewrite expositions of the solution.  (1/5)

⬆️ 611 • 💬 361 • 2d ago • [Mathstodon](https://mathstodon.xyz/@tao/115855840223258103)

---

**[AI is a business model stress test](https://news.ycombinator.com/item?id=46567392)**

AI commoditizes anything you can specify. It can't commoditize what you have to operate.

⬆️ 331 • 💬 324 • 1d ago • [dri.es](https://dri.es/ai-is-a-business-model-stress-test)

---

**[My article on why AI is great (or terrible) or how to use it](https://news.ycombinator.com/item?id=46557057)**

Senior engineers are best positioned to benefit from AI. We're good enough to avoid slop, and there's so much we can accomplish. I wouldn't go back.

⬆️ 163 • 💬 227 • 2d ago • [matthewrocklin.com](https://matthewrocklin.com/ai-zealotry/)

---

**[Show HN: EuConform – Offline-first EU AI Act compliance tool (open source)](https://news.ycombinator.com/item?id=46557823)**

EU AI Act Compliance Tool - Risk classification and bias testing - Hiepler/EuConform

⬆️ 71 • 💬 48 • 2d ago • [GitHub](https://github.com/Hiepler/EuConform)

---

**[Show HN: GlyphLang – An AI-first programming language](https://news.ycombinator.com/item?id=46571166)**

⬆️ 37 • 💬 21 • 1d ago

---

**[Ask HN: Senior engineering mngrs: how has AI changed your day-to-day work?](https://news.ycombinator.com/item?id=46565262)**

⬆️ 30 • 💬 7 • 1d ago

---

**[Show HN: What if AI agents had Zodiac personalities?](https://news.ycombinator.com/item?id=46581832)**

AI agents with different personalities responding to moral dilemmas - baturyilmaz/what-if-ai-agents-had-zodiac-personalities

⬆️ 27 • 💬 13 • 9h ago • [GitHub](https://github.com/baturyilmaz/what-if-ai-agents-had-zodiac-personalities)

---

**[A lawsuit says Workday's AI shut out applicants over 40](https://news.ycombinator.com/item?id=46559995)**

An AI program used by Workday allegedly put resumes of applicants who were Black, disabled, female or over 40 behind other job candidates.

⬆️ 27 • 💬 5 • 2d ago • [Straight Arrow News](https://san.com/cc/workday-hires-for-millions-a-lawsuit-seeking-plaintiffs-says-its-ai-shut-out-applicants-over-40/)

---

**[U.S. airstrikes hit ISIS targets in Syria, officials say](https://news.ycombinator.com/item?id=46571973)**

The strikes were part of a retaliatory operation for the ISIS terrorist ambush in Palmyra, Syria, in December that killed two American soldiers and one U.S. civilian interpreter.

⬆️ 19 • 💬 0 • 1d ago • [cbsnews.com](https://www.cbsnews.com/news/us-airstrikes-isis-targets-syria-central-command/)

---

---

## YouTube Videos: "ai"

**[Grok AI model still generating sexualized content after changes](https://www.youtube.com/watch?v=Y3JZdJlwomE)**

On Elon Musk's social media platform X, the Grok AI image generation reply bot has been changed to be for paying customers ...

📺 NBC News

👁️ 19K • 👍 152 • 💬 86 • ⏱️ 5:25 • 2d ago

---

**[AI has gotten out of hand... (The Beast System)](https://www.youtube.com/watch?v=3468sgevZiU)**

Every month, it feels like a new update, model, or software hits the scene, and people are quick to either claim it's groundbreaking ...

📺 Seethruthescript

👁️ 2K • 👍 164 • 💬 48 • ⏱️ 24:00 • 14h ago

---

**[I Asked AI If It Supports the Operation in Venezuela. And Here’s What It Said](https://www.youtube.com/watch?v=BLLa0DblYaE)**

In this video, I ask AI what it thinks about the U.S. military operation in Venezuela, the real reason behind the capture of Nicolas ...

📺 I Ask AI

👁️ 12K • 👍 2K • 💬 296 • ⏱️ 14:02 • 1d ago

---

**[I Ranked the Best AI Tools to Make Money in 2026](https://www.youtube.com/watch?v=xXxrvra9DQg)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/44Z7YRm Are you building an AI software ...

📺 Dan Martell

👁️ 95K • 👍 5K • 💬 294 • ⏱️ 19:15 • 2d ago

---

**[The Biggest AI News Updates Were NOT at CES](https://www.youtube.com/watch?v=LhpCVkDpYZM)**

LTX 2 Open-Source has officially launched! Explore the open-source release today: https://ltx.io/model I thought this week would ...

📺 Matt Wolfe

👁️ 58K • 👍 2K • 💬 162 • ⏱️ 14:39 • 1d ago

---

**[&quot;RED QUEEN&quot; AI means &quot;GAME OVER&quot; for us....](https://www.youtube.com/watch?v=-EgTYDKtEw8)**

The latest AI News. Learn about LLMs, Gen AI and get ready for the rollout of AGI. Wes Roth covers the latest happenings in the ...

📺 Wes Roth

👁️ 56K • 👍 2K • 💬 315 • ⏱️ 17:36 • 1d ago

---

**[Reacting to our OWN AI VIDEOS!](https://www.youtube.com/watch?v=QtgKP5oyJJs)**

Use my code https://factor.yt.link/T0BOsoa for 50% off your first box + Free Breakfast for 1 year! T&C apply. Reacting to our OWN ...

📺 MoreBeckBros

👁️ 238K • 👍 9K • 💬 725 • ⏱️ 26:17 • 2d ago

---

**[AI Hype](https://www.youtube.com/watch?v=90XC-Of43eE)**

The next episode of my AI series. The AI character is making using AI, but is still pretty heavily edited. Everything else done ...

📺 Nate Ziller

👁️ 200K • 👍 20K • 💬 2K • ⏱️ 4:38 • 1d ago

---

**[Nvidia&#39;s Jensen Huang on an AI Bubble, Trump, and the Arms Race with China](https://www.youtube.com/watch?v=s4haopj2XeA)**

00:00 Intro 00:48 AI Bubble 03:30 Working with President Trump 05:17 AI Arms Race with China 13:13 Taiwan's Future 18:02 ...

📺 TIME

👁️ 126K • 👍 4K • 💬 432 • ⏱️ 24:32 • 2d ago

---

**[[DAY 1] The BEST AI Business to Start In 2026 (LIVE)](https://www.youtube.com/watch?v=dpko4jRSIsM)**

Join the most risk-free offer I've ever made before it's gone: https://lp.monetise.com/aiw-ep-01 If you're not registered for the ...

📺 Iman Gadzhi

👁️ 658K • 👍 30K • 💬 558 • ⏱️ 2:34:25 • 10h ago

---

---

## HuggingFace Models: 🔥 Trending

**[LTX-2](https://huggingface.co/Lightricks/LTX-2)**

*Lightricks*

LTX-2 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs including images, text, and audio. It supports local execution and offers distilled and upscaler checkpoints for practical applications.

`image-to-video`

⬇️ 735,985 • ❤️ 809 • 4d ago

---

**[HY-MT1.5-1.8B](https://huggingface.co/tencent/HY-MT1.5-1.8B)**

*Tencent*

HY-MT1.5-1.8B is a 1.8B parameter translation model supporting 33 languages, offering high-speed, high-quality translation comparable to larger models. It is optimized for edge device deployment and real-time scenarios, with capabilities for terminology intervention, contextual translation, and formatted translation.

`translation` `2.0B`

⬇️ 10,682 • ❤️ 719 • 11d ago

---

**[Qwen-Image-Edit-2511-Multiple-Angles-LoRA](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA)**

*fal*

This LoRA fine-tunes Qwen-Image-Edit-2511 for precise multi-angle image generation, offering 96 camera poses (4 elevations, 8 azimuths, 3 distances) trained on Gaussian Splatting data for 3D consistency. It enables detailed control over camera viewpoints, including low-angle shots, for advanced image editing and content creation.

`image-to-image`

⬇️ 23,889 • ❤️ 468 • 4d ago

---

**[nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)**

*NVIDIA*

Nemotron-Speech-Streaming-En-0.6b is a 600M parameter English ASR model featuring a cache-aware FastConformer-RNNT architecture for low-latency streaming and high-throughput batch processing. It supports dynamic chunk sizes, punctuation, and capitalization, making it ideal for real-time applications like voice assistants and live captioning.

`automatic-speech-recognition`

⬇️ 2,687 • ❤️ 306 • 6d ago

---

**[LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)**

*Liquid AI*

LFM2.5-1.2B-Instruct is a 1.2B parameter instruction-tuned language model optimized for on-device deployment, offering fast edge inference and supporting multiple languages. It excels at agentic tasks and data extraction, with a context length of 32,768 tokens.

`text-generation` `1.2B`

⬇️ 12,797 • ❤️ 274 • 3d ago

---

**[HyperCLOVAX-SEED-Think-32B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B)**

*HyperCLOVA X*

HyperCLOVAX-SEED-Think-32B is a 32B parameter vision-language model capable of multimodal understanding (text, image, video) with a 128K token context length. It excels at Korean-centric reasoning and offers an optional 'thinking mode' for deep, controllable analysis, making it suitable for complex agentic tasks and advanced multimodal QA.

`text-generation` `33.3B`

⬇️ 30,603 • ❤️ 357 • 6d ago

---

**[LFM2.5-Audio-1.5B](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B)**

*Liquid AI*

LFM2.5-Audio-1.5B is an end-to-end audio foundation model enabling real-time speech-to-speech conversational interactions with low latency. It supports interleaved and sequential generation for tasks like ASR, TTS, and seamless chatbot conversations.

`audio-to-audio` `1.5B`

⬇️ 670 • ❤️ 215 • 6d ago

---

**[MiroThinker-v1.5-235B](https://huggingface.co/miromind-ai/MiroThinker-v1.5-235B)**

*MiroMind AI*

MiroThinker-v1.5-235B is a large language model optimized for tool-augmented reasoning and information seeking, featuring interactive scaling for deeper agent-environment interactions. It excels at long-horizon tasks, supporting a 256K context window and up to 400 tool calls, making it ideal for complex research and general QA.

`text-generation` `235.1B`

⬇️ 1,448 • ❤️ 211 • 5d ago

---

**[MiniMax-M2.1](https://huggingface.co/MiniMaxAI/MiniMax-M2.1)**

*MiniMax*

MiniMax-M2.1 is a text generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 210,293 • ❤️ 1,020 • 15d ago

---

**[Alpamayo-R1-10B](https://huggingface.co/nvidia/Alpamayo-R1-10B)**

*NVIDIA*

Alpamayo-R1-10B is a Vision-Language-Action (VLA) Transformer model for autonomous driving, integrating Chain-of-Causation reasoning with diffusion-based trajectory planning for complex scenarios and rare events. It processes multi-camera images, text commands, and egomotion history to output interpretable reasoning traces and a 6.4-second future trajectory.

`robotics` `11.1B`

⬇️ 13,820 • ❤️ 264 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 171 • 💬 5 • ⭐ 4,478 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233)**

*Yoav HaCohen, Benny Brazowski, Nisan Chiprut et al. (29 authors)*

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.

▲ 96 • 💬 1 • ⭐ 2,027 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2601.03233) • [💻 code](https://github.com/Lightricks/LTX-2) • [🔗 project](https://app.ltx.studio/ltx-2-playground/i2v)

---

**[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://huggingface.co/papers/2601.02553)**

*Jiaqi Liu, Yaofeng Su, Peng Xia et al. (8 authors)*

To support reliable long-term interaction in complex environments, LLM agents require memory systems that efficiently manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which applies entropy-aware filtering to distill unstructured interactions into compact, multi-view indexed memory units; (2) Recursive Memory Consolidation, an asynchronous process that integrates related units into higher-level abstract representations to reduce redundancy; and (3) Adaptive Query-Aware Retrieval, which dynamically adjusts retrieval scope based on query complexity to construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.

▲ 22 • 💬 2 • ⭐ 789 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2601.02553) • [💻 code](https://github.com/aiming-lab/SimpleMem) • [🔗 project](https://aiming-lab.github.io/SimpleMem-Page/)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 130 • 💬 18 • ⭐ 49,759 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[VideoRAG: Retrieval-Augmented Generation with Extreme Long-Context
  Videos](https://huggingface.co/papers/2502.01549)**

*Xubin Ren, Lingrui Xu, Long Xia et al. (6 authors)*

VideoRAG enhances large language models for multi-modal video processing with a dual-channel architecture that integrates textual knowledge grounding and multi-modal context encoding.

▲ 3 • 💬 0 • ⭐ 2,375 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.01549) • [💻 code](https://github.com/hkuds/videorag)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 18 • 💬 2 • ⭐ 14,870 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[BitNet b1.58 2B4T Technical Report](https://huggingface.co/papers/2504.12285)**

*Shuming Ma, Hongyu Wang, Shaohan Huang et al. (8 authors)*

BitNet b1.58 2B4T, a 1-bit Large Language Model with 2 billion parameters, matches the performance of full-precision models while improving computational efficiency.

▲ 81 • 💬 2 • ⭐ 25,654 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.12285) • [💻 code](https://github.com/microsoft/bitnet)

---

**[MinerU: An Open-Source Solution for Precise Document Content Extraction](https://huggingface.co/papers/2409.18839)**

*Bin Wang, Chao Xu, Xiaomeng Zhao et al. (18 authors)*

MinerU is an open-source tool that enhances document content extraction using fine-tuned models and pre/postprocessing rules across diverse document types.

▲ 37 • 💬 4 • ⭐ 51,958 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2409.18839) • [💻 code](https://github.com/opendatalab/mineru)

---

**[HunyuanVideo 1.5 Technical Report](https://huggingface.co/papers/2511.18870)**

*Bing Wu, Chang Zou, Changlin Li et al. (81 authors)*

HunyuanVideo 1.5 is a lightweight video generation model with state-of-the-art visual quality and motion coherence, using a DiT architecture with SSTA and an efficient video super-resolution network.

▲ 24 • 💬 1 • ⭐ 3,135 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.18870) • [💻 code](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5)

---

**[GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization](https://huggingface.co/papers/2601.05242)**

*Shih-Yang Liu, Xin Dong, Ximing Lu et al. (13 authors)*

🏢 NVIDIA

Multi-reward reinforcement learning suffers from reward normalization collapse in GRPO, which GDPO addresses by decoupling reward normalization for improved training stability and performance across reasoning tasks.

▲ 150 • 💬 6 • ⭐ 164 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2601.05242) • [💻 code](https://github.com/NVlabs/GDPO) • [🔗 project](https://nvlabs.github.io/GDPO/)

---

---

## GitHub Repositories: "ai"

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 8.1k • 🔱 1.0k • 4h ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 3.0k • 🔱 407 • 4d ago

---

**[nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio)**

Stop juggling AI accounts. Quotio is a beautiful native macOS menu bar app that unifies your Claude, Gemini, OpenAI, Qwen, and Antigravity subscriptions – with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid.

`Swift` `ai-tools` `developer-tools` `proxy` `quota-monitor`

⭐ 2.3k • 🔱 137 • 15h ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 2.0k • 🔱 226 • 20h ago

---

**[datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)**

vibe coding from 0 to 1 | 从零学会 vibe coding，项目制学习

`ai` `coding` `course` `vibe-coding`

⭐ 1.4k • 🔱 124 • 26m ago

---

**[GuDaStudio/skills](https://github.com/GuDaStudio/skills)**

This repository contains a collection of Agent Skills developed by GudaStudio, enabling seamless collaboration between Claude and other AI models and tools.

`PowerShell`

⭐ 1.3k • 🔱 72 • 19d ago

---

**[numman-ali/cc-mirror](https://github.com/numman-ali/cc-mirror)**

Create multiple isolated Claude Code variants with custom providers (Z.ai, MiniMax, OpenRouter, LiteLLM)

`TypeScript`

⭐ 1.3k • 🔱 111 • 2d ago

---

**[aiflowy/aiflowy](https://github.com/aiflowy/aiflowy)**

AIFlowy is an enterprise-grade AI application development platform based on Java, comparable to products like Dify and Coze.

`Vue` `agentic-ai` `ai-agent` `aiflowy` `coze` `dify`

⭐ 1.2k • 🔱 143 • 2h ago

---

**[heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)**

A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

`agent-skills` `ai-agents` `ai-development` `anthropic` `automation`

⭐ 1.2k • 🔱 85 • 13d ago

---

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 950 • 🔱 39 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
