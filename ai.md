---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-29T13:00:25.286469+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** January 29, 2026 at 13:00 UTC  
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

**[Trump’s acting cyber chief uploaded sensitive files into a public version of ChatGPT. The interim director of the Cybersecurity and Infrastructure Security Agency triggered an internal cybersecurity warning with the uploads — and a DHS-level damage assessment.](https://www.reddit.com/r/artificial/comments/1qozsna/trumps_acting_cyber_chief_uploaded_sensitive/)**

🔗 [politico.com](https://www.politico.com/news/2026/01/27/cisa-madhu-gottumukkala-chatgpt-00749361) • 1d ago

---

**[One-Minute Daily AI News 1/28/2026](https://www.reddit.com/r/artificial/comments/1qq00z6/oneminute_daily_ai_news_1282026/)**

Amazon is laying off 16,000 employees as AI battle intensifies.[1] Google adds Gemini AI-powered ‘auto browse’ to Chrome.[2] AI tool AlphaGenome predicts how one typo can change a genetic story.[3] Alibaba Introduces Qwen3-Max-Thinking, a Test Time Scaled Reasoning Model with Native Tool Use Powering Agentic Workloads.[4] Sources: [1] https://www.cnn.com/2026/01/28/tech/amazon-layoffs-ai#openweb-convo [2] https://www.theverge.com/news/869731/google-gemini-ai-chrome-auto-browse [3] https://www.sciencenews.org/article/ai-tool-alphagenome-predicts-genetics [4] https://www.marktechpost.com/2026/01/28/alibaba-introduces-qwen3-max-thinking-a-test-time-scaled-reasoning-model-with-native-tool-use-powering-agentic-workloads/

7h ago

---

**[Judgment Is the Last Non-Automatable Skill](https://www.reddit.com/r/artificial/comments/1qq79qc/judgment_is_the_last_nonautomatable_skill/)**

A lot of the discussion around AI right now focuses on code generation: how far it can go, how fast it’s improving, and whether software engineering as a profession is at risk. Here’s how I currently see it. Modern AI systems are extremely good at automation. Given a context and a set of assumptions, they can generate plausible next actions: code, refactors, tests, even architectural sketches. That’s consistent with what these systems are optimized for: prediction and continuation. Judgment is a different kind of problem. Judgment is about deciding whether the assumptions themselves are still valid: Are we solving the right problem? Are we optimizing the right dimension? Should we continue or stop and reframe entirely? That kind of decision isn’t about generating better candidates. It’s about invalidating context, recognizing shifts in constraints, and making strategic calls under uncertainty. Historically, this has been most visible in areas like architecture, system design, and product-level trade-offs... places where failures don’t show up as bugs, but as long-term rigidity or misalignment. From this perspective, AI doesn’t remove the need for engineers, it changes where human contribution matters. Skills shift left: less emphasis on implementation details, more emphasis on problem framing, system boundaries, and assumption-checking. I'm not claiming AI will never do it, but currently it's not optimized for this. Execution scales well. Judgment doesn’t. And that boundary is becoming more visible as everything else accelerates. Curious how people here think about this distinction. Do you see judgment as something fundamentally different from automation, or just a lagging capability that will eventually be absorbed as models improve?

🔗 [Medium](https://medium.com/@a.mandyev/judgment-is-the-last-non-automatable-skill-711507721fd1) • 30m ago

---

**[Google DeepMind unleashes new AI to investigate DNA’s ‘dark matter’](https://www.reddit.com/r/artificial/comments/1qpggsj/google_deepmind_unleashes_new_ai_to_investigate/)**

DeepMind’s AlphaGenome AI model could help solve the problem of predicting how variations in noncoding DNA shape gene expression

🔗 [Scientific American](https://www.scientificamerican.com/article/google-deepmind-unleashes-new-ai-alphagenome-to-investigate-dnas-dark-matter/) • 20h ago

---

**[DeepSeek releases DeepSeek-OCR 2. 🐋](https://www.reddit.com/r/artificial/comments/1qpw4tw/deepseek_releases_deepseekocr_2/)**

10h ago

---

**[I made a one-liner to deploy your own AI assistant (Moltbot) to Fly.io with WhatsApp integration](https://www.reddit.com/r/artificial/comments/1qpytay/i_made_a_oneliner_to_deploy_your_own_ai_assistant/)**

Hello 👋🏼 I Built a script that deploys MoltBot (open source personal AI assistant) to Fly.io, in one command: curl -fsSL https://raw.githubusercontent.com/blissito/moltbot-flyio/main/install.sh | bash What you get: - Your own (Claude/OpenAI/any)-powered assistant running 24/7 - WhatsApp integration (scan QR, done) 🤯 - Web dashboard to manage everything - One machine on Fly.io (free tier works to start) The installer handles: - Fly.io app creation - Persistent volume for data - Secrets configuration - 4GB RAM setup (2GB causes OOM) - Gateway token generation You just need: - Fly.io account (free) & flyctl installed - Anthropic/OpenAI API key GitHub: https://github.com/blissito/moltbot-flyio ¿Why? It just makes Moltbot cloud deployment dead simple. 🤷🏻‍♂️ If you liked it, give it a star ⭐️ or a PR if you find a bug, it's open source. 🤓

8h ago

---

**[LAD-A2A: How AI agents find each other on local networks](https://www.reddit.com/r/artificial/comments/1qpn2qq/lada2a_how_ai_agents_find_each_other_on_local/)**

AI agents are getting really good at doing things, but they're completely blind to their physical surroundings. If you walk into a hotel and you have an AI assistant (like the Chatgpt mobile app), it has no idea there may be a concierge agent on the network that could help you book a spa, check breakfast times, or request late checkout. Same thing at offices, hospitals, cruise ships. The agents are there, but there's no way to discover them. A2A (Google's agent-to-agent protocol) handles how agents talk to each other. MCP handles how agents use tools. But neither answers a basic question: how do you find agents in the first place? So I built LAD-A2A, a simple discovery protocol. When you connect to a Wi-Fi, your agent can automatically find what's available using mDNS (like how AirDrop finds nearby devices) or a standard HTTP endpoint. The spec is intentionally minimal. I didn't want to reinvent A2A or create another complex standard. LAD-A2A just handles discovery, then hands off to A2A for actual communication. Open source, Apache 2.0. Includes a working Python implementation you can run to see it in action. Repo can be found at franzvill/lad. Curious what people think!

16h ago

---

**[AI chatbots are infiltrating social-science surveys — and getting better at avoiding detection](https://www.reddit.com/r/artificial/comments/1qpi7rz/ai_chatbots_are_infiltrating_socialscience/)**

A researcher has created a chatbot that is indistinguishable from human participants in online surveys. Some researchers fear that a workhorse of social science is now under threat.

🔗 [nature.com](https://www.nature.com/articles/d41586-026-00221-8) • 19h ago

---

**[Automation of day to day tasks](https://www.reddit.com/r/artificial/comments/1qpg14m/automation_of_day_to_day_tasks/)**

I just saw a post discussing clawdbot, about someone not finding a usecase for automating tasks and I realised I too simply can't find anything that I need to automate. I'd love to hear what y'all find automatable. Could this just end up being a very niche feature.

20h ago

---

**[Installed MoltBot locally. Powerful… but I uninstalled it the same day.](https://www.reddit.com/r/artificial/comments/1qot8pk/installed_moltbot_locally_powerful_but_i/)**

Tried ClawdBot (now MoltBot) on a freshly installed system. At first? 🔥 Insane. It found a pitch deck buried in my messy external HDD and even sent it on WhatsApp. Super impressive. Few hours later — I get an Amazon alert: • Login at 2:40 AM • Different location • Logged in from Windows • I’m on Linux • I did NOT log in Could be a false alert (I have 2FA), but the timing freaked me out. Tried uninstalling the bot — no clear guide. Had to dig into code, found it running as a system service, manually removed everything. Realized my mistake: Chrome was installed → password manager + sessions were there. ⚠️ Lesson: These tools are powerful, but don’t install them unless you fully understand what access you’re giving. Not accusing. Just sharing experience. If you know a guide to uninstall if it’s available on the site, please drop it.

1d ago

---

---

## Google News: "ai"

**[Tesla cuts car models in shift to robots and AI](https://www.bbc.com/news/articles/c620177qdg5o)**

Multi-billionaire Elon Musk also announced plans to end production of its Model S and Model X vehicles.

BBC • 10h ago

---

**[Tesla scraps models in pivot to AI as annual revenue falls for first time](https://www.ft.com/content/78d53ce6-a731-496c-8d8b-e53bc35f49a8)**

Elon Musk’s electric-car maker invests $2bn in the billionaire’s xAI

Financial Times • 15h ago

---

**[Tesla Shares Rise As Musk Outlines AI Pivot And End Of Model S And X Production](https://www.forbes.com/sites/siladityaray/2026/01/29/tesla-shares-rise-as-musk-outlines-ai-pivot-and-end-of-model-s-and-x-production/)**

Musk highlighted Tesla’s shift towards AI and robotics, as the company’s electric vehicles continue to see a decline in sales.

Forbes • 1h ago

---

**[Microsoft Continues to Spend Big on A.I. While Profit Jumps 60%](https://www.nytimes.com/2026/01/28/technology/microsoft-earnings-ai-expenditures.html)**

The New York Times • 15h ago

---

**[Dow to Cut About 4,500 Jobs, Using AI to Boost Operations](https://www.bloomberg.com/news/articles/2026-01-29/dow-to-cut-about-4-500-jobs-using-ai-to-boost-operations)**

Bloomberg.com • 1h ago

---

**[Dow to Cut 4,500 Jobs, Sharpen AI Focus](https://www.wsj.com/business/dow-to-cut-4-500-jobs-book-up-to-1-5-billion-in-charges-11f0e814?gaa_at=eafs&gaa_n=AWEtsqcJ_NNisf9EK6ZoZEudUfr9l5HGo8lpZPli8Vsd0EOdtZxOZclu-ZzG&gaa_ts=697b5d4f&gaa_sig=WHxvfZHm_329j2OEQGJirOT1QrwktlG64dM1IfENbPXadodxjCijrNlf7phi9F8BItOWYM0iv1R-EteBUdcZSw%3D%3D)**

The Wall Street Journal • 1h ago

---

**[AI poses bigger threat in jobs with more women, study finds](https://www.cbsnews.com/news/ai-job-loss-disruption-women/)**

Workers in clerical and administrative roles could have the most trouble adapting to the impact of AI on jobs, new research shows.

CBS News • 17m ago

---

**[Artificial Intelligence (AI) Swarm Control Station Research Report 2026: $5.98 Bn Market Opportunities, Trends, Competitive Analysis, Strategies, and Forecasts, 2020-2025, 2025-2030F, 2035F](https://finance.yahoo.com/news/artificial-intelligence-ai-swarm-control-120200578.html)**

Opportunities in the AI swarm control station market include adopting autonomous fleet management, advancing swarm optimization, and integrating next-gen predictive analytics. Rising military investments boost adoption, while local sourcing mitigates tariff impacts, fostering regional supply chain strength. AI Swarm Control Station Market AI Swarm Control Station Market Dublin, Jan. 29, 2026 (GLOBE NEWSWIRE) -- The "Artificial Intelligence (AI) Swarm Control Station Market Report 2026" has been

Yahoo Finance • 58m ago

---

**[ADM settles accounting scandal—can AI help prevent the next one?](https://fortune.com/2026/01/29/adm-settles-accounting-scandalcan-ai-help-prevent-next-one-cfo/)**

ADM’s $40 million SEC settlement over its nutrition segment highlights why ultimate accountability still rests with CFOs.

Fortune • 8m ago

---

**[Meta's Mark Zuckerberg gets green light from Wall Street to keep pouring money into AI](https://www.cnbc.com/2026/01/28/metas-zuckerberg-gets-green-light-from-wall-street-to-invest-in-ai.html)**

Meta's stock pop following the company's latest earnings beat is a sign that investors are OK with hefty AI spending as long as the core business stays strong.

CNBC • 12h ago

---

---

## HackerNews: "ai"

**[France Aiming to Replace Zoom, Google Meet, Microsoft Teams, etc.](https://news.ycombinator.com/item?id=46767668)**

⬆️ 884 • 💬 765 • 2d ago • [X (formerly Twitter)](https://twitter.com/lellouchenico/status/2015775970330882319)

---

**[Apple introduces new AirTag with longer range and improved findability](https://news.ycombinator.com/item?id=46765819)**

Apple today unveiled the new AirTag, now with an expanded finding range and a louder speaker.

⬆️ 605 • 💬 741 • 2d ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/01/apple-introduces-new-airtag-with-expanded-range-and-improved-findability/)

---

**[Please don't say mean things about the AI I just invested a billion dollars in](https://news.ycombinator.com/item?id=46803356)**

“[Nvidia CEO] Jensen Huang Is Begging You to Stop Being So Negative About AI” — Headline from Gizmodo
- - —
Guys, enough is enough. Bullying is a s...

⬆️ 589 • 💬 269 • 13h ago • [McSweeney's Internet Tendency](https://www.mcsweeneys.net/articles/please-dont-say-mean-things-about-the-ai-that-i-just-invested-a-billion-dollars-in)

---

**[Airfoil (2024)](https://news.ycombinator.com/item?id=46795908)**

Interactive article explaining the physics of an airfoil and what makes airplanes fly

⬆️ 482 • 💬 53 • 22h ago • [ciechanow.ski](https://ciechanow.ski/airfoil/)

---

**[Google AI Overviews cite YouTube more than any medical site for health queries](https://news.ycombinator.com/item?id=46766031)**

Exclusive: German research into responses to health queries raises fresh questions about summaries seen by 2bn people a month

⬆️ 413 • 💬 208 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/jan/24/google-ai-overviews-youtube-medical-citations-study)

---

**[UK Government’s ‘AI Skills Hub’ was delivered by PwC for £4.1M](https://news.ycombinator.com/item?id=46803119)**

Or, as they like to call it, the 'AI Skills Hub'. Which was built by PwC because of course it was

⬆️ 369 • 💬 133 • 13h ago • [Mahad Kalam](https://mahadk.com/posts/ai-skills-hub)

---

**[There is an AI code review bubble](https://news.ycombinator.com/item?id=46766961)**

Today everybody's doing AI code review. Here's how Greptile's viewpoint is differentiated - independence, autonomy, and feedback loops.

⬆️ 345 • 💬 241 • 2d ago • [greptile.com](https://www.greptile.com/blog/ai-code-review-bubble)

---

**[AI code and software craft](https://news.ycombinator.com/item?id=46769188)**

⬆️ 245 • 💬 149 • 2d ago • [alexwennerberg.com](https://alexwennerberg.com/blog/2026-01-25-slop.html)

---

**[AI2: Open Coding Agents](https://news.ycombinator.com/item?id=46783017)**

SERA is the first in our family of Open Coding Agents, achieving state-of-the-art performance at low cost.

⬆️ 243 • 💬 45 • 1d ago • [allenai.org](https://allenai.org/blog/open-coding-agents)

---

**[When AI 'builds a browser,' check the repo before believing the hype](https://news.ycombinator.com/item?id=46769965)**

Opinion: Autonomous agents may generate millions of lines of code, but shipping software is another matter

⬆️ 239 • 💬 140 • 2d ago • [theregister.com](https://www.theregister.com/2026/01/26/cursor_opinion/)

---

---

## YouTube Videos: "ai"

**[&#39;Godfather of AI&#39; predicts ALL jobs will be in &#39;wiped out&#39; by AI](https://www.youtube.com/watch?v=eddSGoSYnSU)**

Nobel Prize winner Geoffrey Hinton, the physicist known for his pioneering work in the field, told LBC's Andrew Marr that artificial ...

📺 LBC

👁️ 48K • 👍 929 • 💬 635 • ⏱️ 8:50 • 15h ago

---

**[OpenAI Just Dropped PRISM: The AI That Changes Science Forever](https://www.youtube.com/watch?v=K-bI9BjaId8)**

AI just made a serious jump into the real world. OpenAI unveiled PRISM, a new AI workspace that plugs GPT-5.2 directly into ...

📺 AI Revolution

👁️ 15K • 👍 564 • 💬 43 • ⏱️ 11:36 • 13h ago

---

**[Anthropic CEO speaks about &#39;powerful&#39; AI risks and regulation](https://www.youtube.com/watch?v=tjW_gms7CME)**

Dario Amodei, the CEO of the AI company Anthropic, joined "Top Story" to discuss his new essay "The Adolescence of ...

📺 NBC News

👁️ 39K • 👍 703 • 💬 219 • ⏱️ 18:01 • 1d ago

---

**[The AI Job APOCALYPSE Is Already Here](https://www.youtube.com/watch?v=Y5A_c4pvo7I)**

Support our work: http://novara.media/support Buy Novara Media merch: https://shop.novaramedia.com/ Discuss the show on ...

📺 Novara Media

👁️ 38K • 👍 1K • 💬 461 • ⏱️ 21:03 • 15h ago

---

**[Oracle is About to Pop The AI Bubble](https://www.youtube.com/watch?v=kj4sBnBrQec)**

Become a Channel Member (Exclusive Videos): https://www.youtube.com/channel/UCAFqzhDwJd12pBDgdk-2GqA/join Or ...

📺 Keith D

👁️ 39K • 👍 2K • 💬 339 • ⏱️ 10:20 • 22h ago

---

**[The LLM Revolution Is Over. The Physical AI Revolution Is Coming Fast](https://www.youtube.com/watch?v=MWMe7yjPYpE)**

On stage at Imagination In Action's AI Summit in Davos with John Werner, founder and CEO of Imagination In Action, Yann LeCun ...

📺 Forbes

👁️ 8K • 👍 326 • 💬 78 • ⏱️ 29:11 • 15h ago

---

**[Real Life vs AI](https://www.youtube.com/watch?v=_8QStRwK3fU)**

📺 Oliver Kowal

👁️ 114K • 👍 6K • 💬 32 • ⏱️ 0:55 • 1d ago

---

**[Clawdbot is taking over AI](https://www.youtube.com/watch?v=c2nAKH8BIdo)**

Clawdbot full tutorial. How to install Clawdbot / Moltbot. Use cases of Clawd. Clawdbot vs Claude Code #clawdbot #ai #aitools ...

📺 AI Search

👁️ 73K • 👍 3K • 💬 615 • ⏱️ 28:44 • 1d ago

---

**[I Tried 500+ AI Tools, These 9 Will Give You Freedom](https://www.youtube.com/watch?v=Qgi5hb7yxjU)**

Learn these 9 AI tools to transform your life. Sepehr's 5 Week Free AI Camp & Prompts: https://aisquads.org Tools: Lovable: ...

📺 Simon Squibb

👁️ 22K • 👍 2K • 💬 123 • ⏱️ 11:28 • 20h ago

---

**[Google AI Studio New Update Is INSANE!](https://www.youtube.com/watch?v=hjGf2hnNdYQ)**

Want to make money and save time with AI? Get AI Coaching, Support & Courses ...

📺 Julian Goldie SEO

👁️ 14K • 👍 323 • 💬 67 • ⏱️ 9:34 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[personaplex-7b-v1](https://huggingface.co/nvidia/personaplex-7b-v1)**

*NVIDIA*

PersonaPlex-7B-v1 is a real-time, full-duplex speech-to-speech conversational model that jointly performs streaming speech understanding and generation. It enables natural conversational dynamics like interruptions and overlaps by concurrently processing user audio and generating its own spoken responses, conditioned on voice and text prompts for persona control.

`audio-to-audio`

⬇️ 50,776 • ❤️ 1,411 • 13h ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. Its key capabilities include generating code from visual inputs and orchestrating an agent swarm for complex task decomposition and parallel execution.

`image-text-to-text`

⬇️ 21,428 • ❤️ 997 • 3h ago

---

**[Qwen3-TTS-12Hz-1.7B-CustomVoice](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice)**

*Qwen*

Qwen3-TTS-12Hz-1.7B-CustomVoice is a multilingual text-to-speech model supporting 10 languages with instruction-based control over prosody, emotion, and speaking rate. It features extreme low-latency streaming generation (as low as 97ms) and supports 9 premium timbres for style control, making it ideal for real-time interactive applications.

`text-to-speech` `1.9B`

⬇️ 169,048 • ❤️ 729 • 4h ago

---

**[VibeVoice-ASR](https://huggingface.co/microsoft/VibeVoice-ASR)**

*Microsoft*

VibeVoice-ASR is a unified speech-to-text model capable of processing up to 60 minutes of audio in a single pass, providing structured transcriptions with speaker diarization and timestamps. It supports customized hotwords for improved accuracy in domain-specific content.

`automatic-speech-recognition` `8.7B`

⬇️ 102,495 • ❤️ 712 • 1d ago

---

**[Z-Image](https://huggingface.co/Tongyi-MAI/Z-Image)**

*Tongyi-MAI*

Z-Image is an undistilled, high-fidelity text-to-image diffusion transformer model. It excels in prompt adherence, aesthetic versatility, and output diversity, making it ideal for professional workflows, LoRA training, and ControlNet applications.

`text-to-image`

⬇️ 1,206 • ❤️ 626 • 22h ago

---

**[DeepSeek-OCR-2](https://huggingface.co/deepseek-ai/DeepSeek-OCR-2)**

*DeepSeek*

DeepSeek-OCR-2 is a multilingual vision-language model for image-to-text tasks, excelling at document understanding and OCR with dynamic resolution support for high-fidelity text extraction and conversion to formats like Markdown.

`image-text-to-text` `3.4B`

⬇️ 30,919 • ❤️ 500 • 2d ago

---

**[GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash)**

*Z.ai*

GLM-4.7-Flash is a 30B-A3B MoE model, offering strong performance in the 30B class for efficient, lightweight deployment. It excels in benchmarks like AIME, GPQA, and SWE-bench, making it suitable for tasks requiring advanced reasoning and coding capabilities.

`text-generation` `31.2B`

⬇️ 609,013 • ❤️ 1,316 • 4h ago

---

**[LightOnOCR-2-1B](https://huggingface.co/lightonai/LightOnOCR-2-1B)**

*LightOn AI*

LightOnOCR-2-1B is an efficient 1B-parameter end-to-end vision-language model for document OCR, excelling at extracting text from PDFs and images, including tables and forms, with state-of-the-art accuracy and speed.

`image-text-to-text` `1.0B`

⬇️ 26,227 • ❤️ 430 • 8d ago

---

**[Chroma-4B](https://huggingface.co/FlashLabs/Chroma-4B)**

*FlashLabs*

Chroma-4B is a real-time, end-to-end spoken dialogue model capable of speech understanding, multimodal generation (text and speech), and personalized voice cloning using reference audio. It's built on Qwen2.5-Omni-3B and Llama3, targeting applications like voice agents and virtual humans.

`any-to-any` `5.9B`

⬇️ 7,241 • ❤️ 293 • 1d ago

---

**[sweep-next-edit-1.5B](https://huggingface.co/sweepai/sweep-next-edit-1.5B)**

*Sweep AI*

Sweep Next-Edit 1.5B is a GGUF quantized model for next-edit code autocompletion, running locally in under 500ms and outperforming larger models on benchmarks. It predicts code edits based on file context and recent diffs, primarily used for enhancing developer productivity via local code assistance.

`1.4B`

⬇️ 3,738 • ❤️ 270 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Advancing Open-source World Models](https://huggingface.co/papers/2601.20540)**

*Robbyant Team, Zelin Gao, Qiuyu Wang et al. (24 authors)*

🏢 Robbyant

LingBot-World is an open-source world simulator with high-fidelity dynamics, long-term memory capabilities, and real-time interactivity for diverse environments.

▲ 54 • 💬 1 • ⭐ 608 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20540) • [💻 code](https://github.com/Robbyant/lingbot-world/) • [🔗 project](https://technology.robbyant.com/lingbot-world)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 50 • 💬 1 • ⭐ 5,817 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[DeepSeek-OCR 2: Visual Causal Flow](https://huggingface.co/papers/2601.20552)**

*Haoran Wei, Yaofeng Sun, Yukun Li*

🏢 DeepSeek

DeepSeek-OCR 2 introduces DeepEncoder V2 that dynamically reorders visual tokens based on semantic content, enabling more human-like causal reasoning in 2D image understanding through cascaded 1D causal structures.

▲ 18 • 💬 2 • ⭐ 1,491 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20552) • [💻 code](https://github.com/deepseek-ai/DeepSeek-OCR-2)

---

**[A Pragmatic VLA Foundation Model](https://huggingface.co/papers/2601.18692)**

*Wei Wu, Fan Lu, Yunnan Wang et al. (25 authors)*

🏢 Robbyant

A Vision-Language-Action model trained on extensive real-world robotic data demonstrates superior performance and generalization across multiple platforms while offering enhanced efficiency through optimized training infrastructure.

▲ 38 • 💬 4 • ⭐ 354 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2601.18692) • [💻 code](https://github.com/robbyant/lingbot-vla) • [🔗 project](https://technology.robbyant.com/lingbot-vla)

---

**[Masked Depth Modeling for Spatial Perception](https://huggingface.co/papers/2601.17895)**

*Bin Tan, Changjiang Sun, Xiage Qin et al. (11 authors)*

🏢 Robbyant

LingBot-Depth is a depth completion model that uses visual context to refine depth maps through masked depth modeling and automated data curation for improved spatial perception in robotics and autonomous systems.

▲ 20 • 💬 3 • ⭐ 490 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2601.17895) • [💻 code](https://github.com/Robbyant/lingbot-depth) • [🔗 project](https://technology.robbyant.com/lingbot-depth)

---

**[UltraRAG: A Modular and Automated Toolkit for Adaptive Retrieval-Augmented Generation](https://huggingface.co/papers/2504.08761)**

*Yuxuan Chen, Dewen Guo, Sen Mei et al. (15 authors)*

UltraRAG is a comprehensive RAG toolkit that automates knowledge adaptation across the entire workflow while providing a user-friendly interface for non-coding deployment.

▲ 6 • 💬 0 • ⭐ 4,690 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08761) • [💻 code](https://github.com/OpenBMB/UltraRAG)

---

**[Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation](https://huggingface.co/papers/2601.20614)**

*Yanqi Dai, Yuxiang Ji, Xiao Zhang et al. (6 authors)*

🏢 AMAP-ML

MathForge enhances mathematical reasoning in large models through a dual framework combining difficulty-aware policy optimization and multi-aspect question reformulation to address limitations in existing reinforcement learning methods.

▲ 90 • 💬 9 • ⭐ 81 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20614) • [💻 code](https://github.com/AMAP-ML/MathForge)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 143 • 💬 6 • ⭐ 22,513 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[HeartMuLa: A Family of Open Sourced Music Foundation Models](https://huggingface.co/papers/2601.10547)**

*Dongchao Yang, Yuxin Xie, Yuguo Yin et al. (28 authors)*

A suite of open-source music foundation models is introduced, featuring components for audio-text alignment, lyric recognition, music coding, and large language model-based song generation with controllable attributes and scalable parameterization.

▲ 39 • 💬 4 • ⭐ 2,340 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2601.10547) • [💻 code](https://github.com/HeartMuLa/heartlib) • [🔗 project](https://heartmula.github.io/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 140 • 💬 2 • ⭐ 53,189 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 11.4k • 🔱 627 • 19h ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 9.6k • 🔱 508 • 21h ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 8.5k • 🔱 994 • 6d ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H/美股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 6.7k • 🔱 7.4k • 22h ago

---

**[chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)**

🎬 火宝短剧 - 基于AI的一站式短剧生成平台 《一句话生成完整短剧，从剧本到成片全自动化》  Huobao Drama - An AI-Powered End-to-End Short Drama Generator "One Sentence to Complete Drama: Fully Automated from Script to Final Video"

`Vue`

⭐ 6.6k • 🔱 1.2k • 22h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 5.2k • 🔱 572 • 1d ago

---

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 500+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 5.2k • 🔱 1.2k • 40m ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 3.5k • 🔱 296 • 6d ago

---

**[DevAgentForge/Claude-Cowork](https://github.com/DevAgentForge/Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.6k • 🔱 366 • 6d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 1.8k • 🔱 173 • 10d ago

---

---

*Generated by PeekDeck - A glance is all you need*
