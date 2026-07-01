---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-01T14:37:39.176217+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 01, 2026 at 14:37 UTC  
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

**[I have created a Chrome extension that fact checks YouTube videos as you watch](https://www.reddit.com/r/artificial/comments/1uk7t49/i_have_created_a_chrome_extension_that_fact/)**

Hi, I have been working on this for many months now and I'd really be happy for people to try it out. It is a Chrome extension called "PopUpFactCheck". It is an AI powered video fact checker. With it, you fact check any YouTube video that has captions. And you can use it, for free! You turn captions on, and sit back and watch the video as bubbles appear on the right-hand side of the video with fact checks, information, background, and other context. Great for watching politicians, news, history, and just about any content on YouTube. Claude Code was a major tool in my development, and the AI that is used is GPT 5.5. In addition, there is an extensive waterfall of sources including the TheNewsAPI, various government and public health and other APIs, social, and web search powered by DDGS and Serper. It's free, and you don't have to bring your own API keys or anything. You simply install and use. I will be looking forward to your feedback. PopUpFact Check - Chrome Web Store PopUpFactCheck - Homepage

13h ago

---

**[Are Redditors influencing AI the most?](https://www.reddit.com/r/artificial/comments/1ujuckz/are_redditors_influencing_ai_the_most/)**

21h ago

---

**[What's the best Amharic text to speech today?](https://www.reddit.com/r/artificial/comments/1ukmher/whats_the_best_amharic_text_to_speech_today/)**

I'm looking for an Amharic text-to-speech service that sounds natural enough for YouTube narration. ​I've tried a few options like elevenlabs,speechify but non of them support amharic. ​If you've used one for videos, which service gave you the best results? ​I'm fine with both paid and free recommendations.

38m ago

---

**[What's one AI feature that quietly became part of your daily routine?](https://www.reddit.com/r/artificial/comments/1ukld2m/whats_one_ai_feature_that_quietly_became_part_of/)**

Not the flashy stuff like generating images or writing essays. I'm talking about the feature you barely think about anymore because it's just become useful. For me, it's summarizing long articles and emails. I didn't expect to rely on it this much a year ago. What's yours?

1h ago

---

**[Prompt injection broke every agent system I built so I designed a gateway that separates instructions from data](https://www.reddit.com/r/artificial/comments/1ukgppw/prompt_injection_broke_every_agent_system_i_built/)**

While building agent-based systems with LLM tool use, I kept running into the same failure mode: External content (webpages, files, API responses) would eventually influence agent behavior in unintended ways. Prompt injection isn’t just a “filtering problem” it’s an architectural one. So I built Sentinel Gateway, a middleware layer that sits between agents and tools and enforces a strict separation: Instruction channel (trusted, signed, runtime-issued only) Data channel (untrusted, never executable) Any action an agent takes must be backed by a signed, scoped runtime token, which means: external content cannot escalate into instructions tool calls cannot be influenced by injected payloads agent actions are constrained to explicit permissions It’s designed around the idea that: What it currently supports FastAPI-based agent gateway Streamlit UI for inspection and control Claude sessions + external agent integration Runtime-signed tool execution tokens Audit logging of all agent actions Scheduled tasks + memory tiers Local (SQLite) or Postgres deployment

5h ago

---

**[When does using AI stop being collaboration and start being outsourcing your thinking?](https://www.reddit.com/r/artificial/comments/1ukdp8x/when_does_using_ai_stop_being_collaboration_and/)**

I've been thinking a lot lately about how I personally use AI tools in creative and professional work, and I'm genuinely curious where others draw the line. There's a real difference between using AI to brainstorm, get unstuck, or pressuretest ideas versus just outsourcing the thinking entirely. But in practice that line gets blurry fast. You start by asking for a rough outline, then you're editing its draft, then you're mostly just accepting suggestions, and somewhere in there you've lost the thread of your own voice. What I find interesting is that the most satisfying results I've had come when I treat the AI like a sparring partner rather than a ghostwriter. Push back on it, argue with it, use its output as a foil. That seems to produce something that still feels like mine. But I also wonder if that's just me rationalizing a comfort zone. Maybe the resistance to full AI collaboration is just ego, or maybe it's something worth protecting. For people who use AI regularly in creative or knowledge work, how do you think about this? Do you have explicit rules for yourself, or does it just depend on the task? Has your approach shifted over time as the models have gotten better? Curious whether others feel like the better the AI gets, the harder this question becomes.

8h ago

---

**[What evidence should AI coding agents leave before saying “done”?](https://www.reddit.com/r/artificial/comments/1ukn9k1/what_evidence_should_ai_coding_agents_leave/)**

I’m the maker of Superloopy, a small MIT-licensed workflow layer for Codex and Claude Code. I built it around a problem I kept running into with coding agents: after a long task, the final answer often sounds confident, but the human still has to reconstruct what was actually checked. The pattern I’m trying is an evidence gate before the agent can call work done: - define acceptance criteria up front - route specialized work through skills/subagents when useful - run command-backed checks where possible - save logs, screenshots, review notes, research notes, or other artifacts under `.superloopy/evidence/` - separate deterministic checks from manual/visual judgment - finish with a report that points to the actual evidence The strongest part is the command-backed gate: if a criterion has a command, Superloopy re-runs it in-process at completion, so a stale or fabricated “passed” claim should not reach the final report. Manual/visual checks still need human review, but they are called out separately instead of being mixed into a blanket “done.” Repo: https://github.com/beefiker/superloopy For people using AI coding agents: what proof do you actually want before trusting “done”? Tests/lint are obvious, but I’m curious about screenshots, visual diffs, browser traces, security scans, design checklists, or explicit “manual judgment required” sections.

8m ago

---

**[Reliability is becoming the actual axis the serious AI releases compete on, not how smart they sound](https://www.reddit.com/r/artificial/comments/1ukmtz5/reliability_is_becoming_the_actual_axis_the/)**

Stepping back from the week to week model drops, there is a shift in what the serious AI releases are even trying to sell, and it is worth understanding if you follow this space casually rather than building on it. The first wave of the generative boom competed on capability and fluency. Whose model sounds smarter, writes better, scores higher on the trivia style tests. The newer wave, especially the deep research systems aimed at real knowledge work, is competing on something less flashy and arguably more important. Can you trust the answer. The framing across several of these recent launches is that the failure that actually hurts in practice is not the model obviously making something up. It is the confident answer that looks completely right and is wrong anyway. There are public cases of that already, a law firm filing a brief with fabricated citations, a consulting report going out with invented references, all produced by systems that read as competent and stayed internally consistent. A few of the recent releases are converging on the same idea but from different angles. One approach is to grade the model's output against a rubric it never saw during generation, essentially a second pass that only knows the problem and the answer, not how the answer was reached. Another is to run multiple independent searches and flag when the sources disagree instead of blending them into one smooth paragraph. A third is to split the job entirely, a separate system that did not produce the work checks the claims against fresh sources. These are all variations on the same bet, that the check has to be a different act than the generation. Some of the newer launches are calling this failure mode pseudo correctness, an answer that passes every check the system can run on itself and is still false, and the name is useful because it points at the right fix. If you call it hallucination, you reach for "ask it to check again," which is exactly the move that does not work because the same blind spot that produced the error is doing the checking. Apodex is one of the launches articulating this most clearly, they built a separate verification team that never touches the original reasoning, and the same model goes from around 75 to around 90 on a hard web research benchmark with the independent verifier turned on, no change in weights. Other labs are doing related work, this is just one of the clearer single articulations of the shift. For a general audience the practical takeaways are pretty simple. The next competitive axis in AI is reliability, not just raw intelligence, which is good news for anyone who wants to use these tools for real decisions instead of toy questions. Be most suspicious of the answers that look polished and certain, because that is exactly the category these systems are now being built to catch. And when you evaluate any deep research tool, the question is not how good the answer reads, it is what checked it. None of this means the reliability problem is solved, benchmarks are still benchmarks and the marketing always runs ahead of reality. But the direction is healthier than the last two years of just make it bigger, and it is showing up in shipped products this year, not in white papers. Worth tracking which labs end up treating verification as the core of the system rather than a feature bolted on at the end, because that distinction is going to matter.

25m ago

---

**[We built a model that scores pitch delivery, not just the script](https://www.reddit.com/r/artificial/comments/1ukkg82/we_built_a_model_that_scores_pitch_delivery_not/)**

Transcript-based pitch scoring can't tell the difference between a confident claim and a hedged one, because the words on the page can be identical. "We're growing 40% month over month" reads the same whether you believe it or not. We built a demo that streams video to Inter-1 in real time and scores delivery signals (confidence, hesitation, energy) alongside a content score, each signal tied to the exact moment it happened. Tested it on my own pitch. Content scored 87. Delivery caught a hesitation landing right on the traction number, confidence at 50, overall dropped to 80. The technical side: video streams over WebSocket in short chunks, Inter-1 returns a typed event stream, client folds it into a live timeline while you're still talking. Read more here: https://www.interhuman.ai/blog/pitch-practice-demo

2h ago

---

**[Netflix uses AI to recreate Gene Wilder's voice for new Willy Wonka competition show](https://www.reddit.com/r/artificial/comments/1ukfejv/netflix_uses_ai_to_recreate_gene_wilders_voice/)**

His wife has given her full support towards the series

🔗 [Reality Shrine](https://thetab.com/realityshrine/2026/07/01/netflix-has-used-ai-to-recreate-gene-wilders-voice-for-new-willy-wonka-show-and-its-cursed/) • 6h ago

---

---

## Google News: "ai"

**[Employers who laid off workers citing AI are already starting to regret it](https://www.cnbc.com/2026/07/01/employers-who-laid-off-workers-for-ai-are-reversing-their-decisions.html)**

Companies are realizing artificial intelligence can't do everything after all, prompting them to rehire employees to grow their businesses

CNBC • 10h ago

---

**[Meta Is Building a Cloud Business to Sell Excess AI Compute](https://www.bloomberg.com/news/articles/2026-07-01/meta-is-building-a-cloud-business-to-sell-excess-ai-compute)**

Bloomberg.com • 2h ago

---

**[Meta pops 8% as company makes cloud push to sell excess AI compute power capacity](https://www.cnbc.com/2026/07/01/meta-stock-cloud-ai-compute.html)**

The new business is a welcome signal for some investors who have been uneasy about the company's infrastructure spending plans.

CNBC • 22m ago

---

**[Meta’s reported cloud push weighs on AI compute and data-center stocks](https://www.marketwatch.com/livecoverage/stock-market-today-dow-s-p-500-nasdaq-rally-warsh-ecb-forum/card/meta-s-reported-cloud-push-weighs-on-ai-compute-and-data-center-stocks-nLzSaO49iLgvChVjZeBJ?mod=mw_FV)**

MarketWatch • 16m ago

---

**[No console-flation: how the thirst for AI chips is sending games console prices soaring](https://www.theguardian.com/games/2026/jul/01/pushing-buttons-ai-datacentres-memory-console-prices-sony-playstation-xbox)**

AI data centres, memory scarcity and factory capacity are costing consumers –and console makers

The Guardian • 35m ago

---

**[What's next for AI and Big Tech in the second half of 2026?](https://finance.yahoo.com/video/whats-next-for-ai-and-big-tech-in-the-second-half-of-2026-141912104.html)**

Yahoo Finance Executive Editor Brian Sozzi discusses the current state of the AI "bubble" and tech trade with Slatestone Wealth Chief Market Strategist Kenny Polcari and Bianco Research President Jim Bianco.

Yahoo Finance • 18m ago

---

**[Whom is AI replacing? We deserve to know.](https://thehill.com/opinion/technology/5947906-ai-workforce-reduction-transparency/)**

Firms should be required to publicly disclose which jobs are being eliminated as soon as it happens.

The Hill • 7m ago

---

**[Claude Science, an AI workbench for scientists, is now available](https://www.anthropic.com/news/claude-science-ai-workbench)**

Anthropic • 21h ago

---

**[US removes curbs on Anthropic's latest Fable and Mythos AI models](https://www.reuters.com/business/us-lift-export-controls-anthropics-fable-ai-model-tuesday-source-says-2026-06-30/)**

Reuters • 15h ago

---

**[Anthropic says US has lifted export controls on Fable and Mythos AI models after security fears](https://www.theguardian.com/technology/2026/jul/01/anthropic-fable-mythos-ai-models-us-export-controls-lifted)**

AI company was forced last month to suspend access to its Fable 5 and Mythos 5 models for all foreign nationals

The Guardian • 12h ago

---

---

## HackerNews: "ai"

**[Professor denounces mass AI fraud on an exam at Brown](https://news.ycombinator.com/item?id=48708991)**

The renowned economist Roberto Serrano has ‘overwhelming evidence’ that his students cheated. He thinks the time has come for an in-depth debate so the technology does not signal the end of higher education

⬆️ 547 • 💬 719 • 2d ago • [EL PAÍS English](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html)

---

**[Librepods: AirPods liberated](https://news.ycombinator.com/item?id=48710232)**

AirPods liberated from Apple's ecosystem. Contribute to librepods-org/librepods development by creating an account on GitHub.

⬆️ 498 • 💬 183 • 2d ago • [GitHub](https://github.com/librepods-org/librepods)

---

**[Godot will no longer accept AI-authored code contributions](https://news.ycombinator.com/item?id=48743472)**

At risk of drowning in AI slop code, Godot is firming up its contribution requirements.

⬆️ 419 • 💬 265 • 6h ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)

---

**[Tidal AI Policy](https://news.ycombinator.com/item?id=48718840)**

⬆️ 308 • 💬 345 • 2d ago • [tidal.com](https://tidal.com/ai-policy)

---

**[Working With AI: A concrete example](https://news.ycombinator.com/item?id=48720064)**

In this essay, Carson Gross walks through a concrete bug fix in hyperscript to show where AI helped, where it fell short, and why keeping a knowledgeable human in the loop is what kept complexity in check.

⬆️ 191 • 💬 69 • 1d ago • [htmx.org](https://htmx.org/essays/working-with-ai/)

---

**[AI boom risks global financial crash, warn central bankers](https://news.ycombinator.com/item?id=48713697)**

Reversal of ‘excessive’ tech investments could have serious economic consequences, report finds

⬆️ 157 • 💬 214 • 2d ago • [The Telegraph](https://www.telegraph.co.uk/business/2026/06/28/ai-boom-risks-global-financial-crash-central-bankers-warn/)

---

**[We need tech news sources which exclude AI](https://news.ycombinator.com/item?id=48713041)**

⬆️ 139 • 💬 80 • 2d ago

---

**[EU commissioners shut down air conditioning for employees, leave theirs on](https://news.ycombinator.com/item?id=48734940)**

As Brussels bakes, the Berlaymont building’s AC stops working.

⬆️ 136 • 💬 142 • 22h ago • [POLITICO](https://www.politico.eu/article/eu-commission-heatwave-hq-forced-shut-down-air-conditioning-europe/)

---

**[Ford rehires 'gray beard' engineers after AI falls short](https://news.ycombinator.com/item?id=48710749)**

"Mistakenly we thought that by just introducing artificial intelligence ... that would produce a high-quality product.”

⬆️ 135 • 💬 3 • 2d ago • [TechCrunch](https://techcrunch.com/2026/06/28/ford-rehires-gray-beard-engineers-after-ai-falls-short/)

---

**[Reflections on software engineering in the age of AI](https://news.ycombinator.com/item?id=48708721)**

For those of you who don’t know, when I’m not writing novels, I spend my days as a software engineer, writing code. The software industry these days relies heavily on artificial intelligence. Because it has studied trillions of lines of publicly accessible source code, because code solves problems with testable right and wrong solutions, and because code is structured specifically to be understood by computers, AI has gotten very good at writing code.

⬆️ 106 • 💬 101 • 2d ago • [Andrew Diamond](https://adiamond.me/2026/06/software-engineering-in-the-age-of-ai/)

---

---

## YouTube Videos: "ai"

**[Congress Got a Private Look at AI. The Reaction Was Chilling.](https://www.youtube.com/watch?v=z9zqqsS7848)**

AI #Congress #OpenAI They saw the demo behind closed doors. They walked out shaken. Nobody will tell you what was in that ...

📺 Rod Miller

👁️ 8K • 👍 919 • 💬 218 • ⏱️ 28:59 • 1d ago

---

**[The AI Bubble Has F*cked Us (Even If It NEVER Pops)](https://www.youtube.com/watch?v=dPVEha6oqfw)**

The AI Bubble Will Is MUCH Worse Than We Thought. Contact your representative to ENSURE AI is aligned with humanity: ...

📺 Damon Cassidy

👁️ 44K • 👍 3K • 💬 511 • ⏱️ 22:06 • 14h ago

---

**[This New AI Model Changes Everything](https://www.youtube.com/watch?v=qks6dGQFd_c)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers GLM 5.2: https://z.ai/blog/glm-5.2 We would ...

📺 Two Minute Papers

👁️ 32K • 👍 2K • 💬 210 • ⏱️ 7:27 • 9h ago

---

**[Scientists Asked Grok AI How Egyptians Cut Granite — The Answer Shocked Everyone](https://www.youtube.com/watch?v=c_uBDJqclHA)**

Scientists Asked Grok AI How Egyptians Cut Granite — The Answer Shocked Everyone What if artificial intelligence could help ...

📺 Curious Explorer

👁️ 893K • 👍 3K • 💬 529 • ⏱️ 28:24 • 2d ago

---

**[Why is AI expensive all of a sudden?](https://www.youtube.com/watch?v=DDj30VWCbbY)**

ZapierPartner Sponsored by Zapier! Zapier MCP levels you up, connecting you directly to apps to automate your workflow.

📺 Alberta Tech

👁️ 92K • 👍 6K • 💬 517 • ⏱️ 9:43 • 21h ago

---

**[WTH? Trump Sends Cryptic Message! Now AI Says Trump Is DEAD!](https://www.youtube.com/watch?v=nWI15TNhKnU)**

President Trump is once again sparking a massive online reaction after posting a strange AI-style patriotic painting on Truth Social ...

📺 Lisa Haven

👁️ 8K • 👍 718 • 💬 88 • ⏱️ 8:27 • 1d ago

---

**[AI vs the Permanent Underclass: the End of Coding](https://www.youtube.com/watch?v=oTQzszSabhY)**

We told a generation to "learn to code," and then AI rugpulled everyone. Welcome to the AI singularity. [NEW] Official TechLead ...

📺 TechLead

👁️ 60K • 👍 3K • 💬 618 • ⏱️ 13:10 • 1d ago

---

**[AI has hacked the code of human civilization | Yuval Noah Harari](https://www.youtube.com/watch?v=hBtVGwuJzpk)**

Human domination relies on large-scale cooperation among strangers, which is sustained by bureaucratic systems – such as ...

📺 Yuval Noah Harari 

👁️ 97K • 👍 5K • 💬 495 • ⏱️ 46:52 • 23h ago

---

**[3 REAL Ways To Make Money With Claude AI in 2026](https://www.youtube.com/watch?v=Zvnt4S3aFJk)**

Get started with FreshBooks free 30-day trial: https://partner.freshbooks.com/KimberlyMitchell The job market is rough right now ...

📺 Kimberly Mitchell

👁️ 5K • 👍 236 • 💬 22 • ⏱️ 16:21 • 1d ago

---

**[Break ANY AI Scam Phone Call (in 30 seconds)](https://www.youtube.com/watch?v=lk3jCuITwcE)**

How to break any AI scam phone call in just a few easy steps :) ▻Try Cape: https://cape.co/kitboga 0:00 AI Scam Calls 1:29 Odd ...

📺 Kitboga

👁️ 207K • 👍 18K • 💬 2K • ⏱️ 16:56 • 15h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 630,246 • ❤️ 1,549 • 3d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,113,871 • ❤️ 1,111 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 159,967 • ❤️ 3,123 • 8d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 233,701 • ❤️ 579 • 6d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 34,371 • ❤️ 484 • 6d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 288,741 • ❤️ 908 • 12d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 191,409 • ❤️ 358 • 6d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 114,499 • ❤️ 606 • 2d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 46,677 • ❤️ 321 • 6d ago

---

**[Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)**

*DeepReinforce*

Ornith-1.0-35B is a state-of-the-art, MIT-licensed language model for agentic coding, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving training framework to generate high-quality code solutions and is optimized for single-GPU deployment.

`text-generation` `664,944`

⬇️ 135,452 • ❤️ 278 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 44 • 💬 5 • ⭐ 12,690 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 72,669 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 22 • 💬 2 • ⭐ 8,993 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 90,145 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 249 • 💬 4 • ⭐ 10,286 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 12 • 💬 1 • ⭐ 9,890 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 26,296 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 12 • 💬 2 • ⭐ 18,026 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 84,946 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 78,888 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 70.1k • 🔱 3.6k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.2k • 🔱 1.1k • 2m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 5.9k • 🔱 748 • 1m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 4.6k • 🔱 588 • 3h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.2k • 🔱 199 • 3d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.2k • 🔱 173 • 3d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 155 • 5d ago

---

**[inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)**

Beautiful, AI-native markdown editor and LLM Wiki

`TypeScript` `2nd-brain` `agent-skills` `claude` `codex` `docs`

⭐ 1.7k • 🔱 82 • 1h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 86 • 18d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.5k • 🔱 62 • 17h ago

---

---

*Generated by PeekDeck - A glance is all you need*
