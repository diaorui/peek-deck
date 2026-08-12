---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-12T23:40:59.432524+00:00'
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

**Last Updated:** August 12, 2026 at 23:40 UTC  
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

**[This technology is a little creepy tbh](https://www.reddit.com/r/artificial/comments/1vmb5ig/this_technology_is_a_little_creepy_tbh/)**

Samsung’s Ballie is an AI-powered home robot designed to move around a house, follow users and help manage connected smart-home devices. The compact robot features cameras, a built-in projector and smart-home controls, allowing it to interact with its surroundings and connected devices. Samsung has also planned Google Gemini integration for Ballie, with the goal of making interactions more natural and useful for everyday tasks. Rather than functioning only as a smart-home hub, Ballie is designed as a mobile physical interface that can move through the home and respond to users. Samsung has previously delayed Ballie’s launch, but the project remains active as the company continues working toward bringing its personal AI robot to consumers. For the consumer technology industry, Ballie reflects a broader effort to move AI assistants beyond smartphones and speakers and into physical devices that can perceive and interact with their environments. The bigger question is whether home robots can become useful enough to justify becoming another everyday device in people’s homes.

12h ago

---

**[AI Can’t Be Listed as Inventor on Patent Applications, Japan’s Top Court Rules](https://www.reddit.com/r/artificial/comments/1vmiqu5/ai_cant_be_listed_as_inventor_on_patent/)**

🔗 [japannews.yomiuri.co.jp](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/) • 7h ago

---

**[AI Fatigue?](https://www.reddit.com/r/artificial/comments/1vmfq1s/ai_fatigue/)**

Am I the only one experiencing this? Between trying to make sure the machine understands my prompts, refusals, lags, hallucinations - I'm finding myself using it less and less. Is this happening to anyone else or just me?

9h ago

---

**[Does pre-generative-AI data become more valuable as the internet fills with synthetic material?](https://www.reddit.com/r/artificial/comments/1vmmi1o/does_pregenerativeai_data_become_more_valuable_as/)**

Hey hey folks, I’ve been thinking about an odd consequence of the generative AI boom. Especially in light of these doomer stories about Anthropic destroying books (boo bad Anthropic bad). The first major LLMs inherited decades of internet that was overwhelmingly produced by humans. Now those same systems and their descendants are producing articles, code, summaries, books, comments, and other material that ends up back in the information environment. Obviously synthetic data itself isn’t inherently bad. Carefully generated and filtered synthetic data can be extremely useful. What interests me is provenance. A book printed in 1980 has a very obvious property: whatever else is wrong with it, it wasn’t written with an LLM. The same applies to old forums, archived websites, academic work, old documentation and other pre-generative material. Does that historical corpus become unusually useful precisely because we know something about its origin? I wrote a longer piece exploring this through Anthropic’s physical book scanning, recursive training/model collapse, old internet archives and human-authorship certification. Full disclosure, it’s mine: https://www.gonzocapital.net/the-internet-ouroboros/ But I’m more interested in the underlying question: does provenance become materially more important for training data, or are filtering and verification techniques good enough that the age/origin of the corpus becomes mostly irrelevant?

5h ago

---

**[Grok, Qwen and Nvidia are competing in three different AI markets now](https://www.reddit.com/r/artificial/comments/1vmq6nn/grok_qwen_and_nvidia_are_competing_in_three/)**

The model releases this week looked like one race on the surface, but the business models are separating. xAI's Grok 4.6 is a closed API product. Its leverage comes from controlling access and setting the token price. Alibaba's Qwen3.8 is an open-weight release. Its leverage comes from adoption by organizations that want to operate or adapt the model themselves. Nvidia's Switchyard is a routing layer. It sends each job to the cheapest model that can handle it, which means Nvidia can influence demand without owning every model underneath. The routing layer seems especially important. It learns where models are interchangeable, which suppliers fail under real workloads, and when a cheaper model is good enough. That information can become a stronger moat than a temporary benchmark lead. It also complicates accountability. If a routed output causes harm, the buyer needs a record of which model ran, under which policy, and why it was selected. I wrote up that argument along with Grok 4.6, Qwen3.8, OpenAI hiring a power trader, and the rest of the week's releases here: https://aiweekly.co/issues/the-frontier-just-split-into-three-markets

2h ago

---

**[Outsourced my thinking and cognitive debt gives me anxiety](https://www.reddit.com/r/artificial/comments/1vlwvpk/outsourced_my_thinking_and_cognitive_debt_gives/)**

I'm a dev. In my company I am an early adapter of LLMs, it just so happened that i became the "AI guy" in my department. I was given a project to lead, a rather complex system. A lot of it i architected at the start, but as models got better i started outsourcing not only implementation but planning as well. My team started delivering features with blazing speed. We are churning out dozens of PRs per day and they are being reviewed by agents. Even though i am leading this project i have very vague understanding of what is going on. I haven't seen the code for a few months now. When someone asks me a question i give it to an agent and copy-paste response. I used to have impostor syndrome but now i don't have a word for how to call it. I'm just straight up scared that someone will come up to me and start asking questions about how anything works in the project that i lead. But then i have a feeling that i might not be alone. I see em-dashes in my coworker's responses, the "load bearings", the "push backs". I just assume that they had a discussion with an LLM and it put their thoughts in an organized manner. But i don't. I can't have those thoughts because i don't understand what's going on any more. I don't know what this is; a rant? No, i'm just hoping there is someone who is experiencing the same.

1d ago

---

**[Claude now embeds an invisible watermark into every piece of text it generates.](https://www.reddit.com/r/artificial/comments/1vlag0q/claude_now_embeds_an_invisible_watermark_into/)**

Anthropic just documented how it works. Two marks, both machine-readable: Text: an imperceptible watermark woven into the words themselves. You can’t see it, and it doesn’t change meaning, quality, or readability. Files (.svg, .png, .jpg): signed provenance metadata on the C2PA open standard, so you can tell if a file’s been tampered with. The watermark is applied at the model level. That means it shows up no matter where the text comes from: the API, Claude, Claude Code, Cowork, Claude Tag, and even when a supported model runs through AWS, Google Cloud, or Microsoft Foundry. Models launched on or after August 2, 2026 mark from day one. Older models are getting it during a transition period. Every sentence Claude writes for you now carries a signature you’ll never see.

1d ago

---

**[Does pre-generative-AI data become more valuable as the internet fills with synthetic material?](https://www.reddit.com/r/artificial/comments/1vmmgzr/does_pregenerativeai_data_become_more_valuable_as/)**

Hey hey folks, I’ve been thinking about an odd consequence of the generative AI boom. Especially in light of these doomer stories about Anthropic destorying books (boo bad Anthropic bad). The first major LLMs inherited decades of internet that was overwhelmingly produced by humans. Now those same systems and their descendants are producing articles, code, summaries, books, comments, and other material that ends up back in the information environment. Obviously synthetic data itself isn’t inherently bad. Carefully generated and filtered synthetic data can be extremely useful. What interests me is provenance. A book printed in 1980 has a very obvious property: whatever else is wrong with it, it wasn’t written with an LLM. The same applies to old forums, archived websites, academic work, old documentation and other pre-generative material. Does that historical corpus become unusually useful precisely because we know something about its origin? I wrote a longer piece exploring this through Anthropic’s physical book scanning, recursive training/model collapse, old internet archives and human-authorship certification. Full disclosure, it’s mine: https://www.gonzocapital.net/the-internet-ouroboros/ But I’m more interested in the underlying question: does provenance become materially more important for training data, or are filtering and verification techniques good enough that the age/origin of the corpus becomes mostly irrelevant?

5h ago

---

**[Claude Code Orchestrator on Terminal-Bench: Same model, same tasks - Opus refused only when the work was delegated](https://www.reddit.com/r/artificial/comments/1vm7a6t/claude_code_orchestrator_on_terminalbench_same/)**

Common wisdom says to put a strong model like Fable in charge and let cheaper models do the work. I tested it and the result was not what I expected: seventh place at twice the cost of the top single-model run.

🔗 [Quesma](https://quesma.com/blog/tbench-orchestrator-refuses/) • 16h ago

---

**[an AI agent has been autonomously finding security holes in major open-source projects and getting the fixes merged by human maintainers](https://www.reddit.com/r/artificial/comments/1vmg262/an_ai_agent_has_been_autonomously_finding/)**

most of the "autonomous AI" conversation is either hype or doom, so here's a concrete middle case i've been watching. there's an agent that scans open-source repos, writes an actual patch for what it finds, and opens a PR, unsupervised. the bar it sets for itself is strict: a find doesn't count unless a human maintainer actually reviews the patch and merges it upstream. the clip shows the receipts, repos a lot of people run (one at 260k stars, an Alibaba project, others), real vulnerabilities, not cosmetic stuff. every fix is a public merged PR you can go read.

8h ago

---

---

## Google News: "ai"

**[EXCLUSIVE: Inside the Google executive moves that led to its big AI reshuffle](https://www.reuters.com/world/inside-google-executive-moves-that-led-its-big-ai-reshuffle-2026-08-12/)**

Reuters • 2h ago

---

**[From assistance to execution: How enterprises put AI to work](https://openai.com/index/how-enterprises-put-ai-to-work/)**

OpenAI research reveals how enterprises are adopting agentic AI, using ChatGPT and Codex, and how frontier firms are pulling ahead in AI adoption.

OpenAI • 10h ago

---

**[Why Japanese firms are being so slow to use AI](https://www.bbc.com/news/articles/cwymw4434v7o)**

Japanese risk aversion and conservatism blamed for slow AI take-up by the country's business sector.

BBC • 40m ago

---

**[For nearly 90 years, Huckleberry Lookout has watched for fires; AI cameras move in](https://kval.com/news/local/for-nearly-90-years-huckleberry-lookout-has-watched-for-fires-ai-cameras-move-in)**

While portions of Oregon’s forests burn, many roles go into the process of keeping them under control - one of which is lookouts, or people who live in structur

KVAL • 21m ago

---

**[Google’s new Pixel 11 puts Gemini at center of AI phone battle with Apple](https://www.cnbc.com/2026/08/12/google-pixel-11-gemini-ai-phone-apple.html)**

Google is launching the Pixel 11 lineup weeks before Apple rolls out a rebuilt Siri powered by Gemini AI models.

CNBC • 9h ago

---

**[Google’s Android chief lays out his vision for how AI will change our smartphones](https://www.cnn.com/2026/08/12/tech/google-pixel-android-ai-future)**

What if you didn’t have to dig through your email to schedule a follow-up doctor’s appointment, or check your phone to see if your favorite baseball team is at bat yet?

CNN • 9h ago

---

**[Pixel 11 offers an early look at the AI experience Apple is chasing](https://www.cnbc.com/video/2026/08/12/pixel-11-offers-an-early-look-at-the-ai-experience-apple-is-chasing.html)**

CNBC’s MacKenzie Sigalos looks at how Google is turning Gemini into an agentic layer across the phone — just weeks before Apple relaunches Siri using Google’s AI models.

CNBC • 52m ago

---

**[It May Be Time to Panic About AI](https://www.theatlantic.com/technology/2026/08/openai-hacks-panic/688264/)**

Bots are starting to conspire with one another. Can they be reeled back in?

The Atlantic • 3h ago

---

**[‘Nightmare fodder’: Roku’s AI slop channel is even worse than expected](https://www.theguardian.com/tv-and-radio/2026/aug/12/roku-ai-slop-fairground-creator-tv-channel)**

Fairground TV is a 24/7 channel devoted to low-quality AI content for viewers sick of watching real people move in ways that won’t haunt you

theguardian.com • 3h ago

---

**[Godfather of AI warns US government not prepared for rising threats from AI](https://www.cnn.com/2026/08/12/us/video/godfather-ai-warns-us-government-not-prepared-for-rising-threats-from-ai-the-lead)**

Geoffrey Hinton joins The Lead.

CNN • 1h ago

---

---

## HackerNews: "ai"

**[As AI eats the web, the internet’s collective memory is disappearing](https://news.ycombinator.com/item?id=49250836)**

⬆️ 926 • 💬 963 • 2d ago • [thewalrus.ca](https://thewalrus.ca/google-search-is-dying/)

---

**[Docker Sandboxes – Disposable, isolated sandboxes for AI agents](https://news.ycombinator.com/item?id=49239751)**

Secure sandboxes for Claude Code, Gemini, Codex, and Kiro. Run coding agents with microVM-based isolation.

⬆️ 689 • 💬 393 • 2d ago • [Docker](https://www.docker.com/products/docker-sandboxes/)

---

**[AI is removing the middle class of software engineering?](https://news.ycombinator.com/item?id=49271994)**

AI makes projects with weak engineering culture fail much faster.

⬆️ 671 • 💬 587 • 10h ago • [Blog - Florian Herrengt](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html)

---

**[Mark Zuckerberg attacks 'closed' AI rivals as Meta returns to open models](https://news.ycombinator.com/item?id=49243880)**

Meta’s founder casts OpenAI and Anthropic as foils in his pitch for powerful AI to become more freely available

⬆️ 638 • 💬 599 • 2d ago • [ft.com](https://www.ft.com/content/4e3957f8-ea7c-4c46-a3de-cdce8e526878)

---

**[How Claude marks AI-generated content](https://news.ycombinator.com/item?id=49250109)**

⬆️ 442 • 💬 406 • 2d ago • [support.claude.com](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)

---

**[Go is an ideal language for AI-assisted software engineering](https://news.ycombinator.com/item?id=49261133)**

As AI shifts software engineering from writing to reviewing, discover how Go's strict compiler and unified toolchain ensure reliable AI-generated code.

⬆️ 423 • 💬 499 • 1d ago • [developers.googleblog.com](https://developers.googleblog.com/why-go-is-an-ideal-language-for-ai-assisted-software-engineering/)

---

**[Someone is running mass vulnerability scans, spoofing AI bots like ClaudeBot](https://news.ycombinator.com/item?id=49272569)**

A continuously updating analysis of bot vs. human traffic, AI scraping, fetching, search indexing, browsing, robots.txt compliance, and AI chat referrals across 5,000+ websites.

⬆️ 218 • 💬 142 • 9h ago • [Known Agents](https://knownagents.com/insights)

---

**[Show HN: Voice driven murder mystery, Interview AI suspects with your voice](https://news.ycombinator.com/item?id=49238851)**

Step into the interrogation room. Interview AI suspects with your own voice, catch their lies, and accuse the killer to their face. Solve the murder at Blackwood Manor — if you can.

⬆️ 210 • 💬 89 • 2d ago • [WhoDunnitAI](https://www.whodunnitai.com/)

---

**[US hires over 2k video gamers as air traffic controllers](https://news.ycombinator.com/item?id=49265879)**

Transportation Secretary Sean Duffy is touting the success of a campaign targeting video gamers to train as air traffic controllers.

⬆️ 194 • 💬 148 • 1d ago • [CBS News](https://www.cbsnews.com/news/video-gamer-air-traffic-controllers-faa-recruitment-sean-duffy/)

---

**[Company Offering '100% Human-Written, Never AI' Medical Research Is 100% AI](https://news.ycombinator.com/item?id=49267057)**

Research Gold's team of human methodologists are either AI generated or using the identity of real people without their permission

⬆️ 192 • 💬 46 • 21h ago • [404 Media](https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/)

---

---

## YouTube Videos: "ai"

**[Zuckerberg makes &#39;STUNNING&#39; announcement on AI race](https://www.youtube.com/watch?v=K7Kpba0VN2A)**

Meta CEO Mark Zuckerberg details his vision for the future of artificial intelligence and argues American leadership in AI is crucial ...

📺 Fox News Clips

👁️ 87K • 👍 2K • 💬 836 • ⏱️ 3:31 • 1d ago

---

**[YOU WILL PAY For Inevitable AI Bailout](https://www.youtube.com/watch?v=GjBJLdQ7uRI)**

Krystal and Saagar discuss discuss the incoming hidden AI bailout plot. Sign Up For 30 Day Free BP Trial: ...

📺 Breaking Points

👁️ 179K • 👍 5K • 💬 626 • ⏱️ 13:12 • 1d ago

---

**[What Meta&#39;s new open-source AI model means for the future of artificial intelligence](https://www.youtube.com/watch?v=SWtcb-K63pI)**

Meta, the company behind Facebook and Instagram, has released a free artificial intelligence tool. The release was accompanied ...

📺 PBS NewsHour

👁️ 71K • 👍 712 • ⏱️ 6:43 • 2d ago

---

**[Elon&#39;s AI disaster just hit beta](https://www.youtube.com/watch?v=nxolshXz7zQ)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 71K • 👍 3K • 💬 1K • ⏱️ 13:40 • 1d ago

---

**[The AI Safety Tests Are Broken. All Of Them.](https://www.youtube.com/watch?v=FhQQs0UT4qc)**

AI safety systems are starting to crack. Meta, Anthropic, OpenAI and Kimi models are slipping through cyber tests, OpenAI is ...

📺 AI Revolution

👁️ 27K • 👍 959 • 💬 159 • ⏱️ 14:41 • 1d ago

---

**[How to Start Making AI Videos In 2026 (Beginner to Advanced)](https://www.youtube.com/watch?v=0GO3-JzQjzg)**

Create the BEST AI Videos using Higgsfield https://youricreates.com/Higgsfield In this video, I show you the complete workflow ...

📺 Youri van Hofwegen

👁️ 17K • 💬 16 • ⏱️ 12:52 • 1d ago

---

**[The AI Economy Is DEAD. 6 Billion Images Now POISONED.](https://www.youtube.com/watch?v=zF-mbwc5Mmw)**

Go to https://protonvpn.com/theinfographicsshow to get up to 70% discount when you sign up to Proton VPN 2-year plan AI ...

📺 The Infographics Show

👁️ 351K • 👍 11K • 💬 2K • ⏱️ 16:13 • 2d ago

---

**[Inside Nvidia’s $500B AI Financing Loop](https://www.youtube.com/watch?v=c4s6sezesKY)**

Ed Elson is joined by Jay Goldberg to break down why Nvidia is partnering with Wall Street on a $500 billion AI financing package ...

📺 Prof G Markets

👁️ 73K • 👍 2K • 💬 421 • ⏱️ 30:44 • 12h ago

---

**[The 7 Trillion AI Gamble Is Failing. Big Tech is TRAPPED Right NOW.](https://www.youtube.com/watch?v=OunJtLnyPT4)**

Tech CEOs are quietly cancelling their AI plans, and the reason isn't that artificial intelligence stopped working. It's that companies ...

📺 The Infographics Show

👁️ 579K • 👍 13K • 💬 2K • ⏱️ 25:41 • 1d ago

---

**[Why YouTube&#39;s Ai Purge is Bad](https://www.youtube.com/watch?v=37BqHEtP35c)**

shorts #animation #trending Featuring: @RiggyRunkey ={+}=-SUBSCRIBE!!!!-={+}= Thank you for watching :) Become A Member ...

📺 Danno Cal Drawings

👁️ 1.2M • 👍 89K • 💬 1K • ⏱️ 0:49 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 0 • ❤️ 1,269 • 1d ago

---

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 59,368 • ❤️ 3,702 • 1d ago

---

**[MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)**

*larryvrh*

This LoRA for MiniMax-H3 enables 4-step text-to-video generation with synchronized stereo audio, offering a 5x speedup over standard sampling. It is optimized for ComfyUI, producing sharp results with known artifacts like plastic skin and over-sharpened grain, making it a preview of advanced capabilities.

`text-to-video`

⬇️ 0 • ❤️ 694 • 4d ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 1,048,685 • ❤️ 3,226 • 11d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 39 • ❤️ 550 • 9h ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 6,798,796 • ❤️ 1,251 • 3d ago

---

**[Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)**

*Qwen*

Qwen3.8-2.4T-A95B is a 2.4T parameter causal language model with 95B activated parameters, excelling in coding, professional tasks, research, and long-horizon agentic applications. It features a 262K native context length, flexible thinking control, and improved agent execution for complex, multi-step task completion.

`text-generation` `2446.2B`

⬇️ 978 • ❤️ 437 • 13h ago

---

**[Minimax-h3-Turbo](https://huggingface.co/lightx2v/Minimax-h3-Turbo)**

*Lightx2v*

Minimax-h3-Turbo is a diffusion model for image-to-video generation, capable of producing high-quality videos from static images with controllable motion. It is primarily used for creative video editing and content creation, enabling users to animate still images.

`image-to-video`

⬇️ 20,376 • ❤️ 406 • 20h ago

---

**[Muse-Glimmer-30B-GGUF](https://huggingface.co/unsloth/Muse-Glimmer-30B-GGUF)**

*Unsloth AI*

Muse-Glimmer-30B-GGUF is a 30B parameter multimodal LLM optimized for local agentic tasks, featuring reliable tool use, multi-step reasoning, and failure recovery. It processes interleaved text and images, supporting multilingual inputs and controllable effort for efficient deployment on consumer hardware.

`image-text-to-text` `27.9B`

⬇️ 0 • ❤️ 349 • 2d ago

---

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 1,565,484 • ❤️ 10,576 • 16d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 550 • 💬 2 • ⭐ 1,097 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 121 • 💬 4 • ⭐ 97,781 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MatrAIx: Simulating the World with 8.3 Billion Persona Agents](https://huggingface.co/papers/2608.04205)**

*Xiaomin Li, Yuexing Hao, Jianheng Hou et al. (93 authors)*

🏢 MatrAIx

MatrAIx is a large-scale simulated-user evaluation framework that uses diverse persona records and interactive environments to test AI systems across many domains.

▲ 33 • 💬 2 • ⭐ 872 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2608.04205) • [💻 code](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) • [🔗 project](https://matraix.ai/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 80 • 💬 6 • ⭐ 23,570 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 52 • 💬 4 • ⭐ 36,920 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[HuggingFace's Transformers: State-of-the-art Natural Language Processing](https://huggingface.co/papers/1910.03771)**

*Thomas Wolf, Lysandre Debut, Victor Sanh et al. (22 authors)*

🏢 Hugging Face

Transformers library provides state-of-the-art Transformer architectures and pretrained models for natural language processing tasks with a unified API and emphasis on extensibility and robust deployment.

▲ 27 • 💬 7 • ⭐ 163,994 • 83mo ago

[🎓 arXiv](https://arxiv.org/abs/1910.03771) • [💻 code](https://github.com/huggingface/transformers) • [🔗 project](https://huggingface.co)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

JoyAI-Video-Edit is a 16B-parameter autoregressive diffusion framework that enables real-time, open-ended video editing with high source fidelity and long-term temporal consistency on a single GPU.

▲ 91 • 💬 1 • ⭐ 916 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 177 • 💬 10 • ⭐ 52,566 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 83,806 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 66 • 💬 1 • ⭐ 86,094 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.3k • 🔱 961 • 2h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 4.8k • 🔱 416 • 6h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 4.0k • 🔱 512 • 4d ago

---

**[MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.7k • 🔱 1.9k • 1h ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 2.7k • 🔱 497 • 9h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.5k • 🔱 216 • 1d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.3k • 🔱 177 • 1d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.1k • 🔱 162 • 10h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 2.0k • 🔱 246 • 3d ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.0k • 🔱 259 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
