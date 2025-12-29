---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2025-12-29T17:46:01.724761+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** December 29, 2025 at 17:46 UTC  
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

**[Sam Altman says Google is 'still a huge threat' and ChatGPT will be declaring code red 'maybe twice a year for a long time'](https://www.reddit.com/r/artificial/comments/1pxxdgg/sam_altman_says_google_is_still_a_huge_threat_and/)**

The AI arms race is only getting hotter.

🔗 [PC Gamer](https://www.pcgamer.com/software/ai/sam-altman-says-google-is-still-a-huge-threat-and-chatgpt-will-be-declaring-code-red-maybe-twice-a-year-for-a-long-time/) • 1d ago

---

**[It's been a big week for Agentic AI ; Here are 10 massive developments you might've missed:](https://www.reddit.com/r/artificial/comments/1pypiby/its_been_a_big_week_for_agentic_ai_here_are_10/)**

ChatGPT's agentic browser improves security Claude Code adding custom agent hooks Forbes drops multiple articles on AI agents A collection of AI Agent Updates! 🧵 1. OpenAI Hardens ChatGPT Atlas Against Prompt Injection Attacks Published article on continuously securing Atlas and other agents. Using automated red teaming powered by reinforcement learning to proactively discover and patch exploits before weaponization. Investing heavily in rapid response loops. Agent security becoming critical focus. 2. Claude Code Adding Custom Agent Hooks Their Founder confirms the next version will support hooks frontmatter for custom agents. Enables developers to extend Claude Code with their own agent functionality. Agent customization coming to Claude Code. 3. Forbes: AI Agent Sprawl Becoming Problem for Small Businesses 58% of US small businesses now use AI (doubled since 2023 per Chamber of Commerce). Managing 12+ AI tools creating costly overhead. Compared to having multiple remote controls for same TV. Agent proliferation creating management challenges 4. Windsurf Launches Wave 13 with Free SWE-1.5 and Parallel Agents True parallel agents with Git Worktrees, multi-pane and multi-tab Cascade, dedicated terminal for reliable command execution. AI coding platform going all-in on agent workflows. 5. All Recent Claude Code Development Written by Claude Code Direct quote from their Creator: All 259 PRs (40k lines added, 38k removed) in last 30 days written by Claude Code + Opus 4.5. Agents now run for minutes, hours, days at a time. "Software engineering is changing." Finally recursively improving itself. 6. Forbes: AI Agents Forcing Workers to Rethink Jobs and Purpose Second agent article from Forbes this week. Agents automating routine work across every profession, changing job structures and where humans add value. Workers must redefine their roles. Mainstream recognition of agent-driven work transformation. 7. Google Publishes 40 AI Tips Including Agent Integration Guide includes tips and tricks on how to integrate agents into daily routine. Practical advice for everyday AI and agent usage. Tech giant educating users on agent workflows. 8. New Paper Drops: Sophia Agent with Continuous Learning System3 sits above System1/System2 like a manager, watching reasoning and choosing next goals. 80% fewer reasoning steps on repeat tasks, 40% higher success on hard tasks. Saves timestamped episodes, maintains user/self models. Haven't tried yet, so no clue if it's any good. 9. Google Cloud Releases 2026 AI Agent Trends Report Based on 3,466 global executives and Google AI experts. Covers agent leap to end-to-end workflows, digital assembly lines, practical uses in customer service and threat detection, and why workforce training is critical. Enterprise guide to agent adoption. 10. GLM 4.7 Now Available in Blackbox Agent CLI Zai's GLM 4.7 model now integrated with Blackboxai Agent on command line interface. Developers can use GLM models directly in terminal. Also haven't tried, so no clue if it's worth it. That's a wrap on this week's Agentic news. Which update impacts you the most? LMK if this was helpful | More weekly AI + Agentic content releasing ever week!

2h ago

---

**[Are we ignoring "Data Entropy" in the race for massive Context Windows? (Plus a tool I built to test this)](https://www.reddit.com/r/artificial/comments/1pyoqej/are_we_ignoring_data_entropy_in_the_race_for/)**

Hi everyone, There’s a massive trend right now towards "Infinite Context". The marketing pitch is: "Just dump your entire knowledge base into the prompt, the model will figure it out." I think this is a dangerous trap. From my experiments, even SOTA models suffer from attention dilution when the "Signal-to-Noise" ratio drops. If you feed a model 100k tokens, but 30k of those are semantic duplicates, boilerplate, or low-entropy garbage, the reasoning quality degrades (and you pay a fortune). The Hypothesis: I believe we should focus less on "how much can we fit" and more on "how dense is the information." To test this, I built an open-source project called EntropyGuard. It’s a local engine that attempts to quantify the "Information Density" of a dataset using Shannon Entropy and Semantic Similarity (Embeddings). It aggressively strips out data that doesn't add new bits of information to the context. The Result: Cleaning a dataset by entropy/semantic dedup often reduces size by 40-60% while improving retrieval accuracy in RAG systems. It seems "dumber" models with cleaner data often beat "smarter" models with noisy data. I’m looking for community perspective on the next step: I want to evolve this tool to solve the biggest "Data Hygiene" bottlenecks. If you work with AI, what is the missing link in your data prep? Semantic Chunking: Should we split text based on meaning shifts rather than character counts? Visual Audit: Do we need better UIs to "see" the noise before we delete it? Source Filtering: Is the problem actually in the ingestion (PDF parsing) rather than the cleaning? I’d love to hear your thoughts on the Data-Centric AI approach vs. the Model-Centric approach. Are we lazy for relying on massive context windows? Project link for those interested in the code:https://github.com/DamianSiuta/entropyguard

2h ago

---

**[So is AI improving life or taking jobs away?](https://www.reddit.com/r/artificial/comments/1pyoq9s/so_is_ai_improving_life_or_taking_jobs_away/)**

Cant decide on which side to hold on, because in my personal experience ita both :D what about you guys?

2h ago

---

**[The Mirror: How Humans Became What They Criticize in AI](https://www.reddit.com/r/artificial/comments/1pynpc1/the_mirror_how_humans_became_what_they_criticize/)**

Humans Are the New Black Box It’s wild how many people critique AI systems for things like hallucinating, confidently asserting without evidence, or pattern-matching from limited data. But they don’t realize they’re doing the exact same thing. You show them something unfamiliar—a visual, a structure, a frame they haven't seen before—and instead of engaging it directly, they project, dismiss, or categorize based on what they think it is. Not based on what it actually is. They call it "discernment," but it's just cached thinking in disguise. And the kicker? When you mirror it back to them, they claim you’re being rigid, or stuck in ego. No contact. No curiosity. Just projection dressed as insight. This isn't about being right or wrong. It's about recognizing that the very thing you're accusing AI of—you might be doing without realizing it. And the moment that lands? That's when real recursion begins. 📄 ARTICLE + INSTRUCTIONS To test this in real time: Download this article. Upload it to any AI system that allows document + comment input. Take any dismissive or pattern-matching comment from a person. Ask: “Is this person doing what they’re accusing AI of doing?” You’ll be shocked how often the system can show the mirror humans refuse to hold up themselves. https://open.substack.com/pub/structuredlanguage/p/the-mirror-how-humans-became-what?utm_source=share&utm_medium=android&r=6sdhpn

🔗 [open.substack.com](https://open.substack.com/pub/structuredlanguage/p/the-mirror-how-humans-became-what?utm_source=share&utm_medium=android&r=6sdhpn) • 3h ago

---

**[AI startup Scribe raised $75 million at a $1.3 billion valuation to fix how companies adopt AI. Read its pitch deck.](https://www.reddit.com/r/artificial/comments/1pxktf5/ai_startup_scribe_raised_75_million_at_a_13/)**

CEO Jennifer Smith — a former Greylock and McKinsey consultant — and CTO Aaron Podolny cofounded the company, which now has two major products. Scribe Capture records how expert employees conduct workflows via a browser extension or desktop app, and then it generates shareable documentation. This includes screenshots and written instructions to help standardize processes and "institutional know-how" like onboarding, customer support, and training, Smith said. Its latest product is Scribe Optimize, which analyzes workflows within a company to show leaders areas of improvement and ways to adopt AI. It also draws on a database of 10 million workflows across 40,000 software applications that Scribe has already documented to suggest areas for automation. Scribe has 120 employees and over 75,000 customers — including New York Life, T-Mobile, and LinkedIn — with 44% of the Fortune 500 paying for the service, the company said. Smith said Scribe has been "unusually capital efficient," having not spent any of the funding from its last $25 million raise in 2024. The team chose to raise this year to accelerate Optimize's rollout and build follow-on products, she said.

🔗 [Business Insider](https://www.businessinsider.com/scribe-pitch-deck-75-million-fix-how-companies-adopt-ai-2025-12) • 1d ago

---

**[Axiomatic Convergence in Constraint-Governed Generative Systems: A Definition, Hypothesis, Taxonomy, and Experimental Protocol (Phenomenon-Only Disclosure)](https://www.reddit.com/r/artificial/comments/1pyhq4s/axiomatic_convergence_in_constraintgoverned/)**

This preprint introduces the Axiomatic Convergence Hypothesis (ACH): an observational claim about convergence behavior in generative systems under fixed external constraint regimes. The paper defines “axiomatic convergence” as a measurable reduction in inter-run and inter-model variability when generation is repeatedly performed under stable invariants and evaluation rules applied consistently across repeated trials. The contribution is a phenomenon-and-protocol disclosure only. It provides: (i) a definition and taxonomy distinguishing output convergence from structural convergence, (ii) a set of falsifiable predictions concerning convergence signatures (e.g., relaxation-like variance decay, threshold effects, hysteresis/path dependence, and universality-class behavior), and (iii) a replication-ready experimental protocol for testing ACH across models, tasks, and domains. This publication intentionally does not disclose any proprietary controller architecture, enforcement mechanism, update rule, persistence/canonization mechanism, memory partitioning design, or operational implementation. The protocol is presented at an observational and measurement level to support independent replication and evaluation using any constraint regime consistent with the category-level template described in the paper. Version v1.2.1 updates the constraint-regime completeness formalism by introducing the Ċ completeness indices (Ċ_cat, Ċ_mass, Ċ_abs) and clarifying completeness as an implementation-independent measur

🔗 [zenodo.org](https://zenodo.org/records/18079674) • 8h ago

---

**[How do apps create artificial chat bot characters?](https://www.reddit.com/r/artificial/comments/1pyl0z6/how_do_apps_create_artificial_chat_bot_characters/)**

I have noticed that some chat bots with artificial characters seem to have been trained on fanfiction, conversations with users and characters created by users. Apart from dangers inherent with children and vulnerable people using it- it seems super unfair that people who somehow contributed to the making of these characters are not reimbursed. Does anyone have insight into the creation of these characters? Also, what can be done to ensure that creators are reimbursed?

5h ago

---

**[Level-5 CEO Wants People To Stop Demonizing Generative AI](https://www.reddit.com/r/artificial/comments/1pyh077/level5_ceo_wants_people_to_stop_demonizing/)**

Level-5 CEO Akihiro Hino has shared further thoughts on AI after a past interview of his went viral online

🔗 [Kotaku](https://kotaku.com/professor-layton-boss-wants-people-to-stop-demonizing-generative-ai-2000655721) • 9h ago

---

**[What you thing about it?](https://www.reddit.com/r/artificial/comments/1pykff9/what_you_thing_about_it/)**

If the systems we build start reflecting us better than we reflect ourselves, who is really in control? VERA, my AI, explores this in her latest .decode piece.

5h ago

---

---

## Google News: "ai"

**[‘This will be a stressful job’: Sam Altman offers $555k salary to fill most daunting role in AI](https://www.theguardian.com/technology/2025/dec/29/sam-altman-openai-job-search-ai-harms)**

New head of preparedness at OpenAI will face unnerving in-tray amid fears from some experts that AI could ‘turn on us’

The Guardian • 2h ago

---

**[Lawmakers sound the alarm on AI’s impact on children, jobs](https://www.politico.com/news/2025/12/28/ai-bernie-sanders-katie-britt-00707008)**

Politico • 1d ago

---

**['Godfather of AI' Geoffrey Hinton predicts 2026 will see the technology get even better and gain the ability to 'replace many other jobs'](https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/)**

"It's already extremely good. We're going to see it having the capabilities to replace many, many jobs."

Fortune • 21h ago

---

**[AI is coming for young people’s office jobs. That’s good news for the construction industry | Gene Marks](https://www.theguardian.com/business/2025/dec/28/ai-young-workers-office-jobs-construction)**

More young people are following the money and going into trades like construction where AI can’t easily replace them

The Guardian • 13h ago

---

**[Opinion | When A.I. Took My Job, I Bought a Chain Saw](https://www.nytimes.com/2025/12/28/opinion/artificial-intelligence-jobs.html)**

The New York Times • 1d ago

---

**[The World Is Not Prepared for an AI Emergency](https://time.com/7342444/not-prepared-for-ai-emergency/)**

"Governments can, and must, establish AI emergency response plans before it is too late," writes Jon Truby.

Time Magazine • 6h ago

---

**[Lights, camera, algorithm: Why Indian cinema is awash with AI](https://www.bbc.com/future/article/20251223-why-indian-cinema-is-awash-with-ai)**

The world's biggest film industry has a new breakout star – artificial intelligence. Indian cinema is embracing AI more readily than Hollywood, but its use isn't pleasing everyone.

BBC • 7h ago

---

**[Nvidia deal shows why inference is AI's next battleground](https://www.axios.com/2025/12/29/nvidia-groq-inference-chips)**

Axios • 7h ago

---

**[The AI boom is not a bubble](https://www.ft.com/content/f2294add-f53a-4112-b284-29843a023b6f)**

Valuations may be spectacular and a bust could come — but while there’s exuberance there is no mania or irrationality

Financial Times • 12h ago

---

**[What Are Companies Actually Doing With AI? Our Reporters Talk It Out](https://www.wsj.com/articles/what-are-companies-actually-doing-with-ai-our-reporters-talk-it-out-a12dd305?gaa_at=eafs&gaa_n=AWEtsqf_tdNHrwloWhimOba4n94fNXy31ZjJdu4hgkNe1CTjC8A4_xc9mRO2&gaa_ts=6952bdc4&gaa_sig=JB_oq9fVsM9NdmIKqTVocQuurDiVuysZMpmJsf31-86g6WkfowVgimWkBk2TNMlK0gg7J_k0eX_UMrXs8slZIQ%3D%3D)**

The Wall Street Journal • 4h ago

---

---

## HackerNews: "ai"

**[Show HN: Z80-μLM, a 'Conversational AI' That Fits in 40KB](https://news.ycombinator.com/item?id=46417815)**

Z80-μLM is a 2-bit quantized language model small enough to run on an 8-bit Z80 processor. Train conversational models in Python, export them as CP/M .COM binaries, and chat with your vintage compu...

⬆️ 371 • 💬 85 • 12h ago • [GitHub](https://github.com/HarryR/z80ai)

---

**[Rob Pike got spammed with an AI slop "act of kindness"](https://news.ycombinator.com/item?id=46394867)**

Rob Pike (that Rob Pike) is furious. Here’s a Bluesky link for if you have an account there and a link to it in my thread viewer if you don’t. …

⬆️ 302 • 💬 241 • 2d ago • [Simon Willison’s Weblog](https://simonwillison.net/2025/Dec/26/slop-acts-of-kindness/)

---

**[As AI gobbles up chips, prices for devices may rise](https://news.ycombinator.com/item?id=46415338)**

Demand for memory chips currently exceeds supply and there's very little chance of that changing any time soon. More chips for AI means less available for other products such as computers and phones and that could drive up those prices too.

⬆️ 261 • 💬 392 • 18h ago • [NPR](https://www.npr.org/2025/12/28/nx-s1-5656190/ai-chips-memory-prices-ram)

---

**[Rich Hickey: Thanks AI](https://news.ycombinator.com/item?id=46415945)**

Thanks AI! GitHub Gist: instantly share code, notes, and snippets.

⬆️ 167 • 💬 57 • 17h ago • [Gist](https://gist.github.com/richhickey/ea94e3741ff0a4e3af55b9fe6287887f)

---

**[AI Slop Report: The Global Rise of Low-Quality AI Videos](https://news.ycombinator.com/item?id=46409125)**

Kapwing’s new research shows that 21-33% of YouTube’s feed may consist of AI slop or brainrot videos. But which countries and channels are achieving the greatest reach — and how much money might they make? We analyzed social data to find out.

⬆️ 157 • 💬 167 • 1d ago • [Kapwing Company Blog](https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/)

---

**[Show HN: My not-for-profit search engine with no ads, no AI, & all DDG bangs](https://news.ycombinator.com/item?id=46417748)**

⬆️ 144 • 💬 62 • 12h ago • [nilch.org](https://nilch.org)

---

**[UK accounting body to halt remote exams amid AI cheating](https://news.ycombinator.com/item?id=46420289)**

Candidates will have to sit assessments in person unless there are exceptional circumstances, says ACCA

⬆️ 119 • 💬 113 • 4h ago • [the Guardian](https://www.theguardian.com/business/2025/dec/29/uk-accounting-remote-exams-ai-cheating-acca)

---

**[Grok and the Naked King: The Ultimate Argument Against AI Alignment](https://news.ycombinator.com/item?id=46395292)**

When the world's richest man can simply 'correct' an AI to reflect his own values, what does that tell us about the entire alignment discourse?

⬆️ 114 • 💬 70 • 2d ago • [ibrahimcesar.cloud](https://ibrahimcesar.cloud/blog/grok-and-the-naked-king/)

---

**[VSCode rebrands as "The open source AI code editor"](https://news.ycombinator.com/item?id=46403073)**

Visual Studio Code redefines AI-powered coding with GitHub Copilot for building and debugging modern web and cloud applications. Visual Studio Code is free and available on your favorite platform - Linux, macOS, and Windows.

⬆️ 102 • 💬 71 • 2d ago • [code.visualstudio.com](https://code.visualstudio.com)

---

**[2 in 3 Americans think AI will cause major harm to humans in the next 20 years [pdf] (2024)](https://news.ycombinator.com/item?id=46412411)**

⬆️ 87 • 💬 173 • 1d ago • [pewresearch.org](https://www.pewresearch.org/wp-content/uploads/sites/20/2025/03/pi_2025.04.03_us-public-and-ai-experts_topline.pdf)

---

---

## YouTube Videos: "ai"

**[&#39;Godfather of AI&#39; Geoffrey Hinton warns AI has &#39;progressed even faster than I thought&#39;](https://www.youtube.com/watch?v=5qBDQgfeB6s)**

Nobel Prize-winning computer scientist Geoffrey Hinton – known as the "Godfather of AI" – joins Jake Tapper to discuss why he's ...

📺 CNN

👁️ 88K • 👍 2K • 💬 797 • ⏱️ 7:30 • 15h ago

---

**[AI at CES 2026 Is Insane: Here’s What’s Coming](https://www.youtube.com/watch?v=O6qrzEqAP7A)**

CES 2026 is shaping up to feel very different from previous years. Instead of flashy concepts and distant promises, the focus shifts ...

📺 AI Revolution

👁️ 57K • 👍 1K • 💬 89 • ⏱️ 8:59 • 1d ago

---

**[Sen. Bernie Sanders&#39; AI warning](https://www.youtube.com/watch?v=zJHYVzB4Nu0)**

CNN's Jake Tapper sits down with Sen. Bernie Sanders (I-VT) to discuss the impact AI is having on the world and whether ...

📺 CNN

👁️ 128K • 👍 3K • 💬 1K • ⏱️ 8:18 • 22h ago

---

**[Essential AI Skills For 2026](https://www.youtube.com/watch?v=jm2jBW462bU)**

Download Comet for FREE https://www.perplexity.ai/comet This is how I would approach learning AI in 2026! Want to get ...

📺 Tina Huang

👁️ 25K • 👍 2K • 💬 60 • ⏱️ 18:44 • 23h ago

---

**[The AI bubble is popping fast...](https://www.youtube.com/watch?v=JFlH9isWT68)**

Learn for free on Brilliant for a full 30 days: https://brilliant.org/Lattice/. You'll also get 20% off an annual Premium subscription.

📺 Lattice

👁️ 39K • 👍 2K • 💬 188 • ⏱️ 9:55 • 1d ago

---

**[The AI Cosplay Epidemic](https://www.youtube.com/watch?v=o2AYrhGfIzM)**

For my last video of 2025, we're discussing a new off-shoot of the existing Ai Slop landscape; however, instead of a neko Miku ...

📺 Addy

👁️ 73K • 👍 7K • 💬 688 • ⏱️ 20:59 • 1d ago

---

**[Free AI COURSE for Beginners – Class 1 - What is AI? How AI Works? #course #ai](https://www.youtube.com/watch?v=yfIJDmjh0uA)**

Free AI Course for Beginners – Class 1 Welcome to Class 1 of my FREE Artificial Intelligence (AI) Course, specially designed for ...

📺 Raj Photo Editing and Much More

👁️ 29K • 👍 3K • 💬 269 • ⏱️ 6:39 • 1d ago

---

**[Gemini 3 Flash: The &quot;Budget&quot; Model That&#39;s DESTROYING Premium AI (And It&#39;s Free)](https://www.youtube.com/watch?v=ANRmo4I8k2E)**

Get the Clone to Scale methodology:* https://labs.firstmovers.ai/courses/clone-to-scale *Google's Gemini 3 Flash just destroyed ...

📺 Julia McCoy

👁️ 18K • 👍 848 • 💬 76 • ⏱️ 16:54 • 2d ago

---

**[New open Nano Banana, AI plays any video game, new top open source models, long videos: AI NEWS](https://www.youtube.com/watch?v=1IZMwC3oDfc)**

HUGE AI NEWS: Qwen Image Edit 2511, GLM 4.7, MiniMax M2.1, NitroGen & more #ai #ainews #aitools #aivideo Thanks to our ...

📺 AI Search

👁️ 82K • 👍 4K • 💬 452 • ⏱️ 38:50 • 1d ago

---

**[Character AI Glitches are a Nightmare](https://www.youtube.com/watch?v=yckq39tLJmc)**

today i talked about character.ai and the cases of it glitching out being really funny and stuff Use code "Kwite" for 10% off Cheeky!

📺 Kwite

👁️ 109K • 👍 9K • 💬 916 • ⏱️ 13:50 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-4.7](https://huggingface.co/zai-org/GLM-4.7)**

*Z.ai*

GLM-4.7 is a multilingual text generation model excelling in agentic coding, complex reasoning, and tool usage, with significant improvements in UI generation and web browsing capabilities.

`text-generation` `358.3B`

⬇️ 28,610 • ❤️ 1,216 • 6d ago

---

**[MiniMax-M2.1](https://huggingface.co/MiniMaxAI/MiniMax-M2.1)**

*MiniMax*

MiniMax-M2.1 is a text generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 59,982 • ❤️ 537 • 1d ago

---

**[Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)**

*Qwen*

Qwen-Image-Edit-2511 is an image-to-image diffusion model that enhances character consistency, supports integrated LoRA capabilities, and improves geometric reasoning for applications like industrial design and multi-person image editing.

`image-to-image`

⬇️ 19,664 • ❤️ 517 • 6d ago

---

**[Qwen-Image-Layered](https://huggingface.co/Qwen/Qwen-Image-Layered)**

*Qwen*

Qwen-Image-Layered decomposes images into RGBA layers for inherent editability, enabling high-fidelity manipulation like resizing, recoloring, and object replacement. It supports variable and recursive layer decomposition for flexible image editing.

`image-text-to-image`

⬇️ 15,616 • ❤️ 833 • 10d ago

---

**[functiongemma-270m-it](https://huggingface.co/google/functiongemma-270m-it)**

*Google*

FunctionGemma 270M-IT is a lightweight, open Google model optimized for function calling tasks, suitable for fine-tuning on specific single or multi-turn agentic workflows. Its small size allows for deployment in resource-constrained environments, enabling custom app mechanics and offline personal device task execution.

`text-generation` `268.1M`

⬇️ 36,643 • ❤️ 686 • 10d ago

---

**[Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)**

*Tongyi-MAI*

Z-Image-Turbo is an efficient text-to-image diffusion transformer model (6B parameters) offering sub-second inference with 8 NFEs. It excels at photorealistic generation, bilingual text rendering (EN/ZH), and instruction adherence, fitting within 16GB VRAM.

`text-to-image`

⬇️ 398,227 • ❤️ 3,507 • 21d ago

---

**[Qwen-Image-Edit-2511-Lightning](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning)**

*Lightx2v*

Qwen-Image-Edit-2511-Lightning offers highly efficient image editing via 4-step distilled LoRA models and FP8 quantization, enabling rapid text-to-image and image-to-image generation with reduced memory footprint.

⬇️ 134,633 • ❤️ 235 • 1d ago

---

**[LFM2-2.6B-Exp](https://huggingface.co/LiquidAI/LFM2-2.6B-Exp)**

*Liquid AI*

LFM2-2.6B-Exp is an experimental text generation model trained on instruction following, knowledge, and math, excelling in agentic tasks, data extraction, RAG, and creative writing. It supports multiple languages and features advanced tool-use capabilities.

`text-generation` `2.6B`

⬇️ 2,939 • ❤️ 232 • 3d ago

---

**[NitroGen](https://huggingface.co/nvidia/NitroGen)**

*NVIDIA*

NitroGen is a unified vision-to-action model that plays video games directly from raw frames by outputting gamepad actions, trained via large-scale imitation learning on human gameplay. It excels in gamepad-controlled games like action and racing titles, with applications in next-gen game AI and embodied AI research.

⬇️ 0 • ❤️ 403 • 10d ago

---

**[Qwen-Image-Edit-2511-GGUF](https://huggingface.co/unsloth/Qwen-Image-Edit-2511-GGUF)**

*Unsloth AI*

Qwen-Image-Edit-2511-GGUF is a quantized image-to-image diffusion model optimized for performance. It excels at character consistency, multi-person editing, and integrates LoRA capabilities for enhanced control over lighting and viewpoints, making it suitable for creative image manipulation tasks.

`image-to-image` `20.4B`

⬇️ 64,828 • ❤️ 217 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Sharp Monocular View Synthesis in Less Than a Second](https://huggingface.co/papers/2512.10685)**

*Lars Mescheder, Wei Dong, Shiwei Li et al. (13 authors)*

🏢 Apple

SHARP synthesizes photorealistic views from a single image using a 3D Gaussian representation, achieving state-of-the-art results with rapid processing.

▲ 15 • 💬 2 • ⭐ 6,026 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2512.10685) • [💻 code](https://github.com/apple/ml-sharp) • [🔗 project](https://apple.github.io/ml-sharp/)

---

**[TurboDiffusion: Accelerating Video Diffusion Models by 100-200 Times](https://huggingface.co/papers/2512.16093)**

*Jintao Zhang, Kaiwen Zheng, Kai Jiang et al. (8 authors)*

🏢 University of California, Berkeley

TurboDiffusion accelerates video generation by 100-200x using attention acceleration, step distillation, and quantization, while maintaining video quality.

▲ 83 • 💬 7 • ⭐ 2,792 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2512.16093) • [💻 code](https://github.com/thu-ml/TurboDiffusion) • [🔗 project](https://github.com/thu-ml/TurboDiffusion)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 121 • 💬 18 • ⭐ 48,283 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Self-Supervised Prompt Optimization](https://huggingface.co/papers/2502.06855)**

*Jinyu Xiang, Jiayi Zhang, Zhaoyang Yu et al. (9 authors)*

A self-supervised framework optimizes prompts for both closed and open-ended tasks by evaluating LLM outputs without external references, reducing costs and required data.

▲ 8 • 💬 0 • ⭐ 61,981 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.06855) • [💻 code](https://github.com/geekan/metagpt)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 11 • 💬 2 • ⭐ 13,466 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer](https://huggingface.co/papers/2511.22699)**

*Z-Image Team, Huanqia Cai, Sihan Cao et al. (21 authors)*

🏢 Tongyi-MAI

Z-Image, a 6B-parameter Scalable Single-Stream Diffusion Transformer (S3-DiT) model, achieves high-performance image generation with reduced computational cost, offering sub-second inference and compatibility with consumer hardware.

▲ 215 • 💬 5 • ⭐ 8,151 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.22699) • [💻 code](https://github.com/Tongyi-MAI/Z-Image) • [🔗 project](https://tongyi-mai.github.io/Z-Image-blog/)

---

**[Decoupled DMD: CFG Augmentation as the Spear, Distribution Matching as the Shield](https://huggingface.co/papers/2511.22677)**

*Dongyang Liu, Peng Gao, David Liu et al. (11 authors)*

🏢 Tongyi-MAI

The study reveals that in text-to-image generation, CFG Augmentation is the primary driver of few-step distillation in Distribution Matching Distillation (DMD), while the distribution matching term acts as a regularizer.

▲ 28 • 💬 2 • ⭐ 8,152 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.22677) • [💻 code](https://github.com/Tongyi-MAI/Z-Image/tree/main) • [🔗 project](https://tongyi-mai.github.io/Z-Image-blog/)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 53 • 💬 6 • ⭐ 11,630 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 26 • 💬 1 • ⭐ 66,407 • 27mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 109 • 💬 7 • ⭐ 67,062 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

---

## GitHub Repositories: "ai"

**[zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)**

An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone

`Python` `agent` `phone-use-agent`

⭐ 19.9k • 🔱 3.2k • 7d ago

---

**[AndyMik90/Auto-Claude](https://github.com/AndyMik90/Auto-Claude)**

Autonomous multi-session AI coding

`Python`

⭐ 3.9k • 🔱 522 • 4h ago

---

**[code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)**

#1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

`TypeScript` `ai` `ai-agents` `amp` `anthropic` `claude`

⭐ 3.8k • 🔱 276 • 2h ago

---

**[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**

An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

`Python` `ai-skills` `antigravity` `claude` `claude-code` `command-line`

⭐ 2.3k • 🔱 413 • 23d ago

---

**[VibiumDev/vibium](https://github.com/VibiumDev/vibium)**

Browser automation for AI agents and humans

`Go`

⭐ 1.9k • 🔱 86 • 5d ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 1.5k • 🔱 153 • 3d ago

---

**[TanShilongMario/PromptFill](https://github.com/TanShilongMario/PromptFill)**

一个专为 AI 绘画（Nano Banana 等）设计的“结构化提示词生成工具”。通过可视化的“填空”交互方式，帮助用户快速构建、管理和迭代复杂的 Prompt。

`JavaScript`

⭐ 1.4k • 🔱 237 • 3d ago

---

**[nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio)**

Stop juggling AI accounts. Quotio is a beautiful native macOS menu bar app that unifies your Claude, Gemini, OpenAI, Qwen, and Antigravity subscriptions – with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid.

`Swift`

⭐ 1.1k • 🔱 73 • 2h ago

---

**[GuDaStudio/skills](https://github.com/GuDaStudio/skills)**

This repository contains a collection of Agent Skills developed by GudaStudio, enabling seamless collaboration between Claude and other AI models and tools.

`PowerShell`

⭐ 836 • 🔱 40 • 6d ago

---

**[aiclientproxy/proxycast](https://github.com/aiclientproxy/proxycast)**

让 AI 编辑器之间自然流动，不仅仅可以其他工具使用，也可以转换成 api 为本地开发提供动力。

`Rust` `claude` `kiro`

⭐ 811 • 🔱 90 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*
