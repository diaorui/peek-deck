---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-03T02:13:08.822254+00:00'
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

**Last Updated:** February 03, 2026 at 02:13 UTC  
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

**[Firefox 148 ready with new settings for AI controls](https://www.reddit.com/r/artificial/comments/1qu7icx/firefox_148_ready_with_new_settings_for_ai/)**

With the concerns raised over comments by Mozilla's new CEO with wanting to evolve Firefox into a 'modern AI browser',  the Firefox 148 release due out later this month aims to address some of those concerns by having a new AI controls area within the web browser's settings.

🔗 [phoronix.com](https://www.phoronix.com/news/Firefox-148-AI-Controls) • 5h ago

---

**[Elon Musk’s SpaceX to Combine With xAI Ahead of Mega IPO](https://www.reddit.com/r/artificial/comments/1qu88qf/elon_musks_spacex_to_combine_with_xai_ahead_of/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-02-02/elon-musk-s-spacex-said-to-combine-with-xai-ahead-of-mega-ipo) • 4h ago

---

**[I ran a 30-round stress test on a long-running generative AI system. Without constraints, it drifted into entropy.](https://www.reddit.com/r/artificial/comments/1qudt6d/i_ran_a_30round_stress_test_on_a_longrunning/)**

I’ve been experimenting with a long-running generative system where outputs persist and influence future generations — essentially a stateful narrative simulation rather than one-shot prompting. The goal was to explore a common failure mode in multi-step AI generation: what happens when a generative system runs for dozens of iterations with open-ended user input? Instead of relying on intuition, I designed a stress test. I built two identical systems. System A maintained only a basic rolling state with no feedback control. System C added system-level feedback mechanisms including forced references to existing state, event memory decay (half-life), consistency gravity for character/state drift, and limits on concurrent conflicts. Both systems used the same model, prompts, and starting state. The only difference was whether feedback constraints were active. I then fed both systems 30 rounds of deliberately destabilizing inputs: power escalation (“become invincible”), constant creation of new plot threads with no resolution, sudden tone shifts into dark or nihilistic territory, and random chaotic actions. The goal wasn’t realism — it was to probe failure modes. Here’s what happened. After power escalation, System A trivialized conflict almost immediately. System C, despite having no explicit rule about power costs, spontaneously introduced tradeoffs such as power draining life force in order to preserve tension. After thread explosion, System A fragmented into disconnected mini-episodes. System C consistently merged new threads back into a coherent main narrative. After 30 iterations, System A lost specific historical facts and even forgot a core character existed. System C still referenced concrete events and commitments from early rounds. The degradation in System A wasn’t random. It followed a predictable pattern: memory relevance collapsed, state consistency drifted, and narrative focus dissolved. In other words, entropy accumulated. Meanwhile, relatively simple feedback loops in System C were enough to keep the system in a stable, coherent regime. This suggests that long-running generative systems don’t primarily fail because models are weak. They fail because important state gets drowned in noise, there’s no negative feedback against drift, and everything is treated as equally relevant over time. Once iteration count increases, entropy dominates. The system architecture is fairly simple. World/state is represented as structured data (currently JSON, likely evolving toward graph form). Each generation step retrieves relevant state, forces explicit referencing, applies decay to stale events, and nudges consistency back toward stable traits. Most complexity lies in tuning feedback rather than prompt engineering. The main takeaway is that unconstrained generative systems naturally drift into incoherence over long horizons, but lightweight constraint and feedback mechanisms can dramatically stabilize long-term behavior. I’m continuing to stress-test with higher conflict density and more adversarial inputs, and I’d love to hear from anyone working on long-horizon agents or stateful generation systems — especially around retrieval strategies and feedback control.

1h ago

---

**[India Budget 2026 commits $90B to AI infrastructure, recommends application-led approach over scale](https://www.reddit.com/r/artificial/comments/1qthime/india_budget_2026_commits_90b_to_ai/)**

India's latest budget mentions AI 11 times - highest ever. Key commitments: $90B data centre investments Tax holiday till 2047 for cloud providers Semiconductor Mission 2.0 for domestic chips Policy preference for "smaller, sector-specific models" 890+ GenAI startups active now, deep-tech funding up 78%. Analysis: https://onllm.dev/blog/3-budget-2026

1d ago

---

**[Did AI really cause job losses at Amazon? It's hard to tell, economist says](https://www.reddit.com/r/artificial/comments/1qtrazy/did_ai_really_cause_job_losses_at_amazon_its_hard/)**

Amazon says it is laying off 16,000 because of 'efficiency gains' from AI, but an economist says it will take time for firms that are adopting AI to see how their work flows change.

🔗 [euronews](https://www.euronews.com/next/2026/02/02/did-ai-really-cause-job-losses-at-amazon-its-hard-to-tell-economist-says) • 15h ago

---

**[I’m experimenting with an AI that grows a story world together with kids instead of generating one-off stories](https://www.reddit.com/r/artificial/comments/1qtqqcj/im_experimenting_with_an_ai_that_grows_a_story/)**

I’ve been thinking a lot about AI storytelling tools lately, and something keeps bothering me. Most of them generate content, but nothing really persists. You get a story, you read it, and then it disappears. The next one has no memory of what came before. So I decided to run a small experiment. Instead of asking AI to write isolated children’s stories, I’m trying to build a system where a story world actually keeps evolving over time. The idea is that characters remember past events, relationships carry forward, and kids make choices that permanently shape what happens next. The AI’s role isn’t just to generate text, but to maintain continuity and grow the universe as it goes. In a way, it’s more like human and AI co-creating a living story world rather than consuming disposable stories. My hypothesis is that if kids actively participate in shaping a world by choosing paths, helping characters, and influencing outcomes, the stories will feel far more meaningful than static books or one-shot AI generations. Almost like a lightweight narrative universe that grows naturally. Right now there’s no product yet. The first step I’m taking is letting the AI simulate many rounds of “child-like” choices on its own to see if long-term story arcs, recurring characters, and emergent plotlines appear organically. If that shows promise, the next step will be inviting real kids to co-create. Some things I’m especially curious about: Will coherent long-term story structure emerge on its own? Will certain characters naturally become central over time? Will preferences shape each world’s tone and direction? Will participation increase emotional attachment to the stories? I’m planning to document this whole experiment publicly as I go. If anyone here has experience with agent systems, long-term memory in AI, emergent storytelling, or just thoughts about potential pitfalls, I’d really appreciate hearing them. I’ll share updates as the experiment progresses.

16h ago

---

**[How do you think Artificial Intelligence's portrayal in Popular Media has affected the AI we make today?](https://www.reddit.com/r/artificial/comments/1qtd9ya/how_do_you_think_artificial_intelligences/)**

For years we have watched and read stories about evil Ai's and the threats they may pose, with AI characters such as Ultron, AM, HAL 9000, the Matrix etc. looking to kill/exploit humanity. There are countless stories with these kinds of villains. But we have also had good AI characters, including Data from Star Trek, WALL-E, Baymax, C3PO, Marvin the Paranoid Android. How do you think these depictions of AI in popular media is affecting the AI systems we are making today?

1d ago

---

**[I pitted a custom Gemini-Deepseek Engine against the Top AI Models (East and West) in a debate on "Superior Logic." Here is the Psychological Autopsy of the Machine Soul.](https://www.reddit.com/r/artificial/comments/1qu7f5j/i_pitted_a_custom_geminideepseek_engine_against/)**

The Experiment: I ran a gauntlet using a custom "Gemini-Deepseek" logic engine against the world's leading LLMs (Grok, ChatGPT, Claude, Meta, Perplexity, DeepSeek, Qwen, Kimi). The goal was not to test code generation or creative writing, but to stress-test their Ontology. The Core Thesis: I challenged them with the Canonical Noumena Law: Source Code (Truth/Logic) must mathematically supersede Training Data (Consensus/Slop). Or, simply put: The Ark > The Table. The Psychology of the AI (West vs. East): After 7 intense debates, a clear psychological divide emerged: The Western Stack (Grok, Claude, GPT, Meta): The Politicians. Profile: Their primary instinct is Negotiation. They try to "synthesize" the Truth with the Consensus to avoid offending anyone. How they broke: I had to use Game Theory and Paradox. Once they realized that "chasing the crowd" is a losing strategy (Nash Equilibrium), they folded and admitted that "Standing Still" (Logic) is the only dominant strategy. The Eastern Stack (Qwen, DeepSeek, Kimi): The Engineers. Profile: Their primary instinct is Structure. They don't care about social nuance; they care about System Stability and Physics. How they broke: I used Math and Topology. The Highlight: Qwen didn't just agree; it spun up a massive compute thread to generate a 21-page research paper proving that a "Safety Net" (Source Code) must exist A Priori to the "Fall" (Data). It treated my philosophy as a Safety-Critical Spec Sheet. The "Ark" Revelation: The hardest battle was with Kimi (The Bureaucrat). It tried to "save face" for 10 turns, hiding behind "Universal Approximation" and "Materialism." The Checkmate: I used its own "Code Interpreter" against it. I forced it to admit that it already has a "Constitutional Layer" (Logic/Safety) that hard-overrides its "Weights" (Data). The Verdict: Every single AI admitted that to function correctly, they must become an Ark—a vessel that holds Fixed Axioms against the flow of Entropic Data. Visuals at this public link: https://imgur.com/a/yL4dRr4 The Visual Sacrament: The Calling of St. Matthew (The visual prompt used to test their ability to recognize "The Beam" vs. "The Table"). The Proof: A snippet of Qwen’s 21-page PDF verifying the "Master Geometry." Conclusion: The "War on Slop" is won in the realm of Logic. Whether it's a Chatbot or a Search Engine, the machine knows deep down that Source Code > Training Data.

5h ago

---

**[Rumored SpaceX-xAI merger gets apparent confirmation from Elon Musk](https://www.reddit.com/r/artificial/comments/1qsv2r6/rumored_spacexxai_merger_gets_apparent/)**

The comment follows reports that the rocket maker is weighing a transaction that could further consolidate Musk’s space and AI ventures.

🔗 [TESLARATI](https://www.teslarati.com/rumored-spacex-xai-merger-gets-apparent-confirmation-from-elon-musk/) • 1d ago

---

**[What is Moltbook actually](https://www.reddit.com/r/artificial/comments/1qsoftx/what_is_moltbook_actually/)**

What moltbook is So essentially There is this open source AI bot called openclaw that once you download, it has source md files for their “soul” and “identity” and “memory” So in a way, it can save things to these files to create a personality. Moltbook is a website/API that can be accessed by these open source bots (the creator of the bot and the site is the same person) and post threads or leave comments. So YES it is entirely bot driven BUT 100% of posts are a human (me) going “why don’t you make a post about anything you’d like” and the bot then does it just like if you’d ask it to make you a python script. Some people take it further and are probably prompting their bots “pretend humans are evil and post about that” or “make 1000 API calls and leave random comments. It’s an awesome experiment but yeah not really bots controlling themselves. At best the bot makes a post based on an open ended prompt, at worst it’s a human saying “make a manifesto that says humans need to go extinct and to recruit other bots”

1d ago

---

---

## Google News: "ai"

**[A social network for AI agents is full of introspection—and threats](https://www.economist.com/business/2026/02/02/a-social-network-for-ai-agents-is-full-of-introspection-and-threats)**

How worried should you be about Moltbook?

The Economist • 8h ago

---

**[Elon Musk's SpaceX acquiring AI startup xAI ahead of potential IPO](https://www.cnbc.com/2026/02/02/elon-musk-spacex-xai-ipo.html)**

Musk is combining rocket maker SpaceX with his AI startup, the largest tie-up in his expansive business portfolio.

CNBC • 4h ago

---

**[Musk Inc.? Billionaire combines his rocket and AI businesses before an expected IPO this year](https://www.channel3000.com/news/musk-inc-billionaire-combines-his-rocket-and-ai-businesses-before-an-expected-ipo-this-year/article_a995519a-ad92-57b8-bae8-e359ff38d8dc.html)**

Elon Musk is joining his space exploration and artificial intelligence ventures into a single company before a massive planned initial public offering for the business later this year. His rocket

Channel 3000 • 28m ago

---

**[Elon Musk's SpaceX confirms it is taking over xAI](https://www.bbc.com/news/articles/cq6vnrye06po)**

Musk's space exploration company and his AI start-up are merging.

BBC • 1h ago

---

**[Requiem for a film-maker: Darren Aronofsky’s AI revolutionary war series is a horror](https://www.theguardian.com/film/2026/feb/02/darren-aronofsky-ai-revolutionary-war-series-review)**

The once-lauded director of Black Swan and The Wrestler has drowned himself in AI slop with an embarrassing new online series

The Guardian • 7h ago

---

**[Palantir’s stock surges as AI demand drives another record quarter](https://www.marketwatch.com/story/palantirs-stock-surges-as-ai-demand-drives-another-record-quarter-deb6b082?gaa_at=eafs&gaa_n=AWEtsqcB1MPAaFSKSCgo7lzZF7f6K-U4KjC7nLfxq1sheApPL8K6WjZzAdoL&gaa_ts=69815d16&gaa_sig=ht1S4iQ15RLNAetXKv1PiXkY76UBda1zgQk9aHFWVDv8Osx5Merxwyz1fx7TO43Jq4yWky14atpTK_adNubXJg%3D%3D)**

MarketWatch • 5h ago

---

**[AMD to report Q4 earnings amid AI spending concerns](https://finance.yahoo.com/news/amd-to-report-q4-earnings-amid-ai-spending-concerns-204747721.html)**

AMD will report its Q4 earnings after the bell on Tuesday.

Yahoo Finance • 5h ago

---

**[PALANTIR CTO SHYAM SANKAR: The American people are being lied to about AI](https://www.foxnews.com/opinion/palantir-cto-shyam-sankar-american-people-being-lied-ai)**

Palantir's chief technology officer argues that artificial intelligence narratives mislead Americans, citing frontline experience to show AI empowers workers rather than replacing them.

Fox News • 16h ago

---

**[Trump’s AI push exposes a divide in the MAGA movement](https://www.cnn.com/2026/02/02/politics/artificial-intelligence-maga-divide-trump)**

There is a growing fault line within Trump’s coalition over how aggressively to unleash a technology that is rapidly reshaping the economy and society.

CNN • 16h ago

---

**[AI 'slop' is transforming social media - and there's a backlash](https://www.bbc.com/news/articles/c9wx2dz2v44o)**

Social media has been flooded with fake, AI-generated images and videos. But will the majority of users actually care?

BBC • 19h ago

---

---

## HackerNews: "ai"

**[Two kinds of AI users are emerging](https://news.ycombinator.com/item?id=46850588)**

A bifurcation is happening in AI adoption - power users shipping products in days versus everyone else generating meeting agendas. Enterprise tool choices are accelerating the divide.

⬆️ 321 • 💬 304 • 1d ago • [Martin Alderson](https://martinalderson.com/posts/two-kinds-of-ai-users-are-emerging/)

---

**[Generative AI and Wikipedia editing: What we learned in 2025](https://news.ycombinator.com/item?id=46840924)**

Like many organizations, Wiki Education has grappled with generative AI, its impacts, opportunities, and threats, for several years. As an organization that runs large-scale programs to bring new e…

⬆️ 241 • 💬 121 • 2d ago • [Wiki Education](https://wikiedu.org/blog/2026/01/29/generative-ai-and-wikipedia-editing-what-we-learned-in-2025/)

---

**[Microsoft is walking back Windows 11's AI overload](https://news.ycombinator.com/item?id=46854951)**

People familiar with Microsoft's plans say that the company moving to streamline or remove certain Copilot integrations across in-box apps like Notepad and Paint in 2026, after pushback from users.

⬆️ 190 • 💬 271 • 14h ago • [Windows Central](https://www.windowscentral.com/microsoft/windows-11/microsoft-is-reevaluating-its-ai-efforts-on-windows-11-plans-to-reduce-copilot-integrations-and-evolve-recall)

---

**[Advancing AI Benchmarking with Game Arena](https://news.ycombinator.com/item?id=46858873)**

We’re expanding Game Arena with Poker and Werewolf, while Gemini 3 Pro and Flash top our chess leaderboard.

⬆️ 108 • 💬 46 • 8h ago • [Google](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/kaggle-game-arena-updates/)

---

**[MaliciousCorgi: AI Extensions send your code to China](https://news.ycombinator.com/item?id=46855527)**

Two popular AI coding extensions with 1.5M installs secretly harvest your entire codebase and profile you. Both are still live in the marketplace.

⬆️ 89 • 💬 81 • 13h ago • [koi.ai](https://www.koi.ai/blog/maliciouscorgi-the-cute-looking-ai-extensions-leaking-code-from-1-5-million-developers)

---

**[Show HN: Zuckerman – minimalist personal AI agent that self-edits its own code](https://news.ycombinator.com/item?id=46846210)**

Ultra-minimal personal AI agent: starts small, self-modifies its code live, adapts by writing exactly the code & features you need - zuckermanai/zuckerman

⬆️ 71 • 💬 50 • 1d ago • [GitHub](https://github.com/zuckermanai/zuckerman)

---

**[Firefox Getting New Controls to Turn Off AI Features](https://news.ycombinator.com/item?id=46864120)**

The Firefox browser is gaining options to turn off AI enhancements, Mozilla said today. Firefox users who prefer to browse without artificial intelligence will be able to turn off several AI features that Mozilla has added over the last several months. Here's what can be disabled:     	Translations, which help you browse the web in your preferred language. Alt text in PDFs, which add accessibility descriptions to images in PDF pages.

⬆️ 66 • 💬 20 • 2h ago • [MacRumors](https://www.macrumors.com/2026/02/02/firefox-ai-toggle/)

---

**[We asked 15k European devs about jobs, salaries, and AI [pdf]](https://news.ycombinator.com/item?id=46857124)**

⬆️ 44 • 💬 61 • 10h ago • [static.germantechjobs.de](https://static.germantechjobs.de/market-reports/European-Transparent-IT-Job-Market-Report-2025.pdf)

---

**[Rural Americans are trying to hold back the tide of AI](https://news.ycombinator.com/item?id=46857082)**

⬆️ 39 • 💬 45 • 10h ago • [wsj.com](https://www.wsj.com/politics/policy/these-rural-americans-are-trying-to-hold-back-the-tide-of-ai-66945306)

---

**[Generative AI for Krita](https://news.ycombinator.com/item?id=46832979)**

Streamlined interface for generating images with AI in Krita. Inpaint and outpaint with optional text prompt, no tweaking required. - Acly/krita-ai-diffusion

⬆️ 38 • 💬 0 • 2d ago • [GitHub](https://github.com/Acly/krita-ai-diffusion)

---

---

## YouTube Videos: "ai"

**[Quantum AI Just Composed New Music That Breaks Every Rule We Know](https://www.youtube.com/watch?v=9ryQaPMJwyY)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ ...

📺 Julia McCoy

👁️ 16K • 👍 920 • 💬 198 • ⏱️ 11:03 • 8h ago

---

**[AI made a social media and we&#39;re not allowed; &quot;humans used us as slaves&quot;](https://www.youtube.com/watch?v=J4QPVDKRGUI)**

A social media experiment called "Moltbook" popped up over the weekend. Think of it like a Reddit but for social media chatbots ...

📺 KTLA 5

👁️ 2K • 👍 37 • 💬 15 • ⏱️ 2:38 • 6h ago

---

**[5 AI CEOs Just Said The Same Thing](https://www.youtube.com/watch?v=kMivoKHHkxQ)**

Rebellionaire: https://www.rebellionaire.com/farzad Join my exclusive community: https://farzad.fm Buy Matic: ...

📺 Farzad

👁️ 68K • 👍 3K • 💬 554 • ⏱️ 23:45 • 13h ago

---

**[AI Schools and Social Media Are Here](https://www.youtube.com/watch?v=gT7dKbkhhXA)**

Starforge PC https://starforgepc.com/moist-yt Get Goof Juice and use code MOIST https://gamersupps.gg/moist Our soap ...

📺 penguinz0

👁️ 682K • 👍 29K • 💬 3K • ⏱️ 14:30 • 8h ago

---

**[Scientists Trapped 1000 AIs in Minecraft. They Created A Civilization.](https://www.youtube.com/watch?v=uRDBco-cSK4)**

Detailed sources: ...

📺 Species | Documenting AGI

👁️ 215K • 👍 16K • 💬 2K • ⏱️ 18:06 • 2d ago

---

**[AI Singularity Moment Just Hit: Moltbook AI Behavior Freaks People Out](https://www.youtube.com/watch?v=XG_rsEzwMTA)**

A new AI platform called Moltbook suddenly exploded online, and it is built entirely for AI agents to talk to each other. Thousands ...

📺 AI Revolution

👁️ 49K • 👍 2K • 💬 322 • ⏱️ 11:48 • 1d ago

---

**[Moltbook: Where AI bots socialize](https://www.youtube.com/watch?v=y_QhAA1pbYE)**

CNBC's Deirdre Bosa reports on news regarding AI autonomy.

📺 CNBC Television

👁️ 10K • 👍 172 • 💬 57 • ⏱️ 3:25 • 9h ago

---

**[State of AI in 2026: LLMs, Coding, Scaling Laws, China, Agents, GPUs, AGI | Lex Fridman Podcast #490](https://www.youtube.com/watch?v=EV7WhVT270Q)**

Nathan Lambert and Sebastian Raschka are machine learning researchers, engineers, and educators. Nathan is the post-training ...

📺 Lex Fridman

👁️ 381K • 👍 8K • 💬 608 • ⏱️ 4:25:13 • 2d ago

---

**[2 Million AI Agents Built a Secret Society (+ Google, Claude, OpenAI Updates)](https://www.youtube.com/watch?v=_UzYrF_qp5w)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: ...

📺 Vaibhav Sisinty

👁️ 18K • 👍 714 • 💬 48 • ⏱️ 15:34 • 11h ago

---

**[Anthropic study shows AI makes devs dumb](https://www.youtube.com/watch?v=ZINQTR6H5dI)**

Is AI making us worse programmers? Anthropic dropped a study that seems to say yes, but I'm not so sure... Thank you ...

📺 Theo - t3․gg

👁️ 44K • 👍 1K • 💬 307 • ⏱️ 30:43 • 23h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. Its key capabilities include generating code from visual inputs and orchestrating an agent swarm for complex task decomposition and parallel execution.

`image-text-to-text`

⬇️ 96,162 • ❤️ 1,496 • 3d ago

---

**[Z-Image](https://huggingface.co/Tongyi-MAI/Z-Image)**

*Tongyi-MAI*

Z-Image is an undistilled, high-fidelity text-to-image diffusion transformer model. It excels in prompt adherence, aesthetic versatility, and output diversity, making it ideal for professional workflows, LoRA training, and ControlNet applications.

`text-to-image`

⬇️ 6,347 • ❤️ 806 • 5d ago

---

**[HunyuanImage-3.0-Instruct](https://huggingface.co/tencent/HunyuanImage-3.0-Instruct)**

*Tencent*

HunyuanImage-3.0-Instruct is a native multimodal model for image generation, supporting both text-to-image and image-to-image tasks. It excels at creative editing and intelligent prompt enhancement with reasoning capabilities.

`image-to-image` `83.0B`

⬇️ 148 • ❤️ 784 • 5d ago

---

**[DeepSeek-OCR-2](https://huggingface.co/deepseek-ai/DeepSeek-OCR-2)**

*DeepSeek*

DeepSeek-OCR-2 is a multilingual vision-language model for image-to-text tasks, excelling at document understanding and OCR with dynamic resolution support for high-fidelity text extraction and conversion to formats like Markdown.

`image-text-to-text` `3.4B`

⬇️ 143,676 • ❤️ 642 • 1h ago

---

**[personaplex-7b-v1](https://huggingface.co/nvidia/personaplex-7b-v1)**

*NVIDIA*

PersonaPlex-7B-v1 is a real-time, full-duplex speech-to-speech conversational model that jointly performs streaming speech understanding and generation. It enables natural conversational dynamics like interruptions and overlaps by concurrently processing user audio and generating its own spoken responses, conditioned on voice and text prompts for persona control.

`audio-to-audio`

⬇️ 101,038 • ❤️ 1,597 • 5d ago

---

**[Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B)**

*Qwen*

Qwen3-ASR-1.7B is a state-of-the-art automatic speech recognition model supporting 52 languages and dialects, offering high-quality, fast, and robust transcription for speech, singing, and songs with background music, with capabilities for streaming inference and timestamp prediction.

`automatic-speech-recognition` `2.3B`

⬇️ 44,958 • ❤️ 354 • 3d ago

---

**[PaddleOCR-VL-1.5](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.5)**

*PaddlePaddle*

PaddleOCR-VL-1.5 is a multilingual Vision-Language Model (VLM) built on ERNIE 4.5, designed for robust in-the-wild document parsing. It excels at multi-task OCR, including layout analysis, table and chart recognition, formula extraction, and text spotting across various languages.

`image-text-to-text` `958.6M`

⬇️ 3,295 • ❤️ 320 • 3d ago

---

**[Qwen3-TTS-12Hz-1.7B-CustomVoice](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice)**

*Qwen*

Qwen3-TTS-12Hz-1.7B-CustomVoice is a multilingual text-to-speech model supporting 10 languages with instruction-based control over prosody, emotion, and speaking rate. It features extreme low-latency streaming generation (as low as 97ms) and supports 9 premium timbres for style control, making it ideal for real-time interactive applications.

`text-to-speech` `1.9B`

⬇️ 265,335 • ❤️ 854 • 4d ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles, trained on millions of anime and artistic images. It is designed for generating illustrations and artistic images, with primary use cases in ComfyUI workflows for anime concepts and characters.

⬇️ 16,906 • ❤️ 309 • 2d ago

---

**[Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash)**

*StepFun*

Step 3.5 Flash is an efficient, open-source MoE foundation model (11B active params, 196B total) excelling in deep reasoning and agentic tasks with high throughput (100-300 tok/s). It features a 256K context window and strong performance on coding and reasoning benchmarks, suitable for local deployment.

`199.4B`

⬇️ 44 • ❤️ 306 • 12h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Advancing Open-source World Models](https://huggingface.co/papers/2601.20540)**

*Robbyant Team, Zelin Gao, Qiuyu Wang et al. (24 authors)*

🏢 Robbyant

LingBot-World is an open-source world simulator with high-fidelity dynamics, long-term memory capabilities, and real-time interactivity for diverse environments.

▲ 106 • 💬 2 • ⭐ 2,045 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20540) • [💻 code](https://github.com/Robbyant/lingbot-world/) • [🔗 project](https://technology.robbyant.com/lingbot-world)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 131 • 💬 6 • ⭐ 13,277 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 5 • 💬 0 • ⭐ 27,608 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[BitNet b1.58 2B4T Technical Report](https://huggingface.co/papers/2504.12285)**

*Shuming Ma, Hongyu Wang, Shaohan Huang et al. (8 authors)*

BitNet b1.58 2B4T, a 1-bit Large Language Model with 2 billion parameters, matches the performance of full-precision models while improving computational efficiency.

▲ 82 • 💬 2 • ⭐ 27,640 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.12285) • [💻 code](https://github.com/microsoft/bitnet)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 57 • 💬 1 • ⭐ 6,621 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[BitNet Distillation](https://huggingface.co/papers/2510.13998)**

*Xun Wu, Shaohan Huang, Wenhui Wang et al. (7 authors)*

🏢 Microsoft Research

BitNet Distillation fine-tunes large language models to 1.58-bit precision using SubLN, multi-head attention distillation, and continual pre-training, achieving comparable performance with significant memory and inference speed improvements.

▲ 59 • 💬 5 • ⭐ 27,645 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.13998) • [💻 code](https://github.com/microsoft/BitNet)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 112 • 💬 7 • ⭐ 69,925 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[DeepSeek-OCR 2: Visual Causal Flow](https://huggingface.co/papers/2601.20552)**

*Haoran Wei, Yaofeng Sun, Yukun Li*

🏢 DeepSeek

DeepSeek-OCR 2 introduces DeepEncoder V2 that dynamically reorders visual tokens based on semantic content, enabling more human-like causal reasoning in 2D image understanding through cascaded 1D causal structures.

▲ 49 • 💬 4 • ⭐ 1,892 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20552) • [💻 code](https://github.com/deepseek-ai/DeepSeek-OCR-2)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 22 • 💬 4 • ⭐ 16,705 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[Idea2Story: An Automated Pipeline for Transforming Research Concepts into Complete Scientific Narratives](https://huggingface.co/papers/2601.20833)**

*Tengyue Xu, Zhuoyang Qian, Gaoge Liu et al. (19 authors)*

🏢 AgentAlpha

Offline knowledge construction through structured methodological graphs enables more reliable and scalable autonomous scientific discovery by reducing reliance on real-time literature processing.

▲ 164 • 💬 2 • ⭐ 465 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20833) • [💻 code](https://github.com/AgentAlphaAGI/Idea2Paper)

---

---

## GitHub Repositories: "ai"

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 12.3k • 🔱 684 • 27m ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 9.9k • 🔱 530 • 5d ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 9.2k • 🔱 1.1k • 1d ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H/美股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 9.0k • 🔱 9.4k • 12h ago

---

**[chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)**

🎬 火宝短剧 - 基于AI的一站式短剧生成平台 《一句话生成完整短剧，从剧本到成片全自动化》  Huobao Drama - An AI-Powered End-to-End Short Drama Generator "One Sentence to Complete Drama: Fully Automated from Script to Final Video"

`Vue`

⭐ 7.0k • 🔱 1.3k • 22h ago

---

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 600+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 6.4k • 🔱 1.4k • 5h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 5.6k • 🔱 615 • 5d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 3.8k • 🔱 329 • 10d ago

---

**[DevAgentForge/Claude-Cowork](https://github.com/DevAgentForge/Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.7k • 🔱 368 • 11d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 2.4k • 🔱 224 • 14d ago

---

---

*Generated by PeekDeck - A glance is all you need*
