---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-18T11:39:39.473480+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 18, 2026 at 11:39 UTC  
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

**[I found Claude for Government buried in the Claude Desktop binary. Here's what Anthropic built, how it got deployed, and the line they're still holding against the Pentagon.](https://www.reddit.com/r/artificial/comments/1r7tsff/i_found_claude_for_government_buried_in_the/)**

https://aaddrick.com/blog/claude-for-government-the-last-lab-standing Pulled the Claude Desktop binary the same day it shipped and confirmed it in code. Anthropic's government deployment mode showed up on their status tracker February 17th. Traffic routes to claude.fedstart.com, authentication goes through Palantir Keycloak SSO, Sentry telemetry is disabled, and a pubsec banner gets injected. All of it landed in one release with zero prior trace across eight versions. The GSA deal, the DoD contract dispute, and the Pentagon's supply chain risk threat are covered in the full breakdown linked above.

🔗 [aaddrick.com](https://aaddrick.com/blog/claude-for-government-the-last-lab-standing) • 6h ago

---

**[The gap between AI demos and enterprise usage is wider than most people think](https://www.reddit.com/r/artificial/comments/1r7n3sl/the_gap_between_ai_demos_and_enterprise_usage_is/)**

I work on AI deployment inside my company, and the gap between what AI looks like in a polished demo… and what actually happens in real life? I think about that a lot. Here’s what I keep running into. First, the tool access issue. Companies roll out M365 Copilot licenses across the organization and call it “AI adoption.” But nobody explains what people should actually use it for. It’s like handing everyone a Swiss Army knife and then wondering why they only ever use the blade. Without use cases, it just becomes an expensive icon in the ribbon. Then there’s the trust gap. You’ve got senior engineers and specialists with 20+ years of experience. They’ve built careers on judgment and precision. Of course they don’t blindly trust AI output and for safety-critical or compliance-heavy work, they absolutely shouldn’t. But for drafting, summarizing, structuring ideas, or preparing first passes? The resistance ends up costing them hours every week. The measurement problem is another big one. “We deployed AI” sounds impressive, but it’s meaningless. The real question is: which exact workflows got faster? Which tasks became more accurate? Which processes got cheaper? Most organizations never measure at that level. So they can’t prove value — and momentum fades. Governance is where things get uncomfortable. Legal, compliance, cybersecurity, HSE, they need clear boundaries. Where can AI be used? Where is it off-limits? What data is allowed? Many companies skip this step because it slows things down. Then someone uses ChatGPT to draft a contract, and suddenly everyone panics. And finally, scaling. One team figures out an incredible AI workflow that saves hours every week. But it stays within that team. There’s no structured way to share what works across departments. So instead of compounding gains, progress stays siloed. What I’ve seen actually work: Prompt libraries tailored to specific roles, not generic “how to use AI” guides Clear guardrails on when AI is appropriate (and when it isn’t) Department-level champions who actively share workflows Measuring time saved on specific tasks instead of vague “productivity boosts” Enterprise AI adoption isn’t a tech rollout. It’s a behavior shift. Curious, if you’re working on this inside your organization, what’s blocking you right now?

11h ago

---

**[Sales reps at $11 billion AI startup ElevenLabs have to bring in 20 times their base salary, or they're out — VP says](https://www.reddit.com/r/artificial/comments/1r7pf2s/sales_reps_at_11_billion_ai_startup_elevenlabs/)**

AI startup ElevenLabs, valued at $11 billion, employs small teams with high sales quotas.

🔗 [Business Insider](https://www.businessinsider.com/elevenlabs-11-billion-ai-startup-ruthless-sales-strategy-2026-2) • 10h ago

---

**[AI summit (19th feb)](https://www.reddit.com/r/artificial/comments/1r7w1o3/ai_summit_19th_feb/)**

Going to attend AI Summit on 19th feb in Delhi, Anyone is going on the same day please connect, going alone need a company. Thanks Connect over DM.

4h ago

---

**[Elon Musk Firms Enter Secret Pentagon Challenge for Voice-Based Drone Swarming Tech](https://www.reddit.com/r/artificial/comments/1r7jr7l/elon_musk_firms_enter_secret_pentagon_challenge/)**

"Elon Musk’s SpaceX and its subsidiary xAI are joining a secretive US Department of Defense competition centered on a voice command and control tool that could deploy multiple autonomous systems. The project, launched in January with a $100-million budget and a six-month timeline, requires software that could coordinate unmanned swarming operations across the air and at sea, according to Bloomberg. The Pentagon’s Defense Innovation Unit and its new Defense Autonomous Warfare Group under the US Special Operations Command are overseeing the competition. The contest will unfold in phases, starting with software development before advancing to live trials. SpaceX and xAI’s participation marks an expansion of Musk’s defense work into artificial intelligence-enabled weapons software, as the Pentagon moves to accelerate drone development and domestic manufacturing while cutting bureaucracy. It also follows Washington’s call for cost-effective counter-drone solutions, particularly to protect critical military and civilian infrastructure as well as large public events. Separately, xAI, alongside other firms such as ChatGPT owner OpenAI, secured defense contracts worth up to $200 million each last year to expand advanced artificial intelligence use across military systems."

🔗 [The Defense Post](https://thedefensepost.com/2026/02/17/pentagon-musk-voice-swarming/) • 13h ago

---

**[Using combine consensus of LLMs to remove (or smooth-reduce) their own flaws in decision making](https://www.reddit.com/r/artificial/comments/1r8070j/using_combine_consensus_of_llms_to_remove_or/)**

You probably know how llms hallucinate, hedge, don't anchor, confabulate, etc. While we look towards new models that are likely to get a bit better, but what can we do today, right now? Perhaps not a novel idea, but I was toying with making one llm check an opinion of another llm. This is specifically useful in areas where I am not competent. This is what llms are for, to advise, but llms have good days and bad days, and bad prompts.. Sometimes you need to walk an llm to get to the best opinion. This is fine when you can know the topic and appreciate that the final decision is close to what one can accept as good enough. But there are times when one can't know if that an opinion of llm is good enough to follow. But, man, one wants a bit of certainty in this uncertain and imperfect world. Somewhere down this rabit hole, I played games with llm, was pasting one llm's opinion into another llm to get another perspective and gauge how good the first opinion is. It was working out ok, I'd bring concerns back to the original llm and have it explain the choice there. The courier it back and after some back and forth, I felt like 2 llms was way better than one. Overall, it was producing better results, the combination of llms with a bit of hands-on of human orchestration. Got me thinking, why not automate. The issue was there that llms often didn't do a good job by themselves. The topic would be ignored, some minutia detail will be argued to death, it was often going off the rails. BUT! It was great when it worked. It got me thinking, what llms were missing is a structured protocol to hold llms on true and narrow. I started hooking up something close to human debate rules. And it got traction and results. The whole idea that came out is more complicated in the end, here are some interesting items: Overview: https://github.com/Alex-R-A/llm-argumentation-protocol/blob/main/PROTOCOL-EXPLAINED-FOR-HUMANS.md (here much talked about how to make llms be responsible for good outputs through adversarial debate) And a bit of theory: https://github.com/Alex-R-A/llm-argumentation-protocol/blob/main/SCIENTIFIC.md Then graphs: https://github.com/Alex-R-A/llm-argumentation-protocol/blob/main/PROTOCOL-FLOW-DIAGRAMS.md Overall, returning to the main point, you can make different llms (even across brands) argue to what they know, show proof of their thinking, and get to defend or attack a point. Again, this is cumulative wisdom, so to speak, and then adversarial consensus. Also, doesn't allow any one single llm to simply make stuff up, or give a poor quality answer. Github repo to the claude code skill: https://github.com/Alex-R-A/llm-argumentation-protocol

28m ago

---

**[Sony Group tech can identify original music in AI-generated songs](https://www.reddit.com/r/artificial/comments/1r7vvdp/sony_group_tech_can_identify_original_music_in/)**

Japanese company seeks to help copyright holders receive share of revenue

🔗 [Nikkei Asia](https://asia.nikkei.com/business/technology/artificial-intelligence/sony-group-tech-can-identify-original-music-in-ai-generated-songs) • 4h ago

---

**[Self-hosted claude swarm running on the cloud and surviving restarts](https://www.reddit.com/r/artificial/comments/1r7n831/selfhosted_claude_swarm_running_on_the_cloud_and/)**

A self-hosted platform for running Claude agent swarms with a React UI, deployed on GCP Cloud Run. - simonstaton/ClaudeSwarm

🔗 [GitHub](https://github.com/simonstaton/ClaudeSwarm) • 11h ago

---

**[I love Claude but honestly some of the "Claude might have gained consciousness" nonsense that their marketing team is pushing lately is a bit off putting. They know better!](https://www.reddit.com/r/artificial/comments/1r6lw8i/i_love_claude_but_honestly_some_of_the_claude/)**

- Anthropic CEO Says Company No Longer Sure Whether Claude Is Conscious - Link - Anthropic revises Claude’s ‘Constitution,’ and hints at chatbot consciousness - Link

1d ago

---

**[India's Adani to invest $100 billion to develop renewable energy-powered AI-ready data centers over the next decade, seeking to establish the world’s largest integrated data center platform.](https://www.reddit.com/r/artificial/comments/1r74i7g/indias_adani_to_invest_100_billion_to_develop/)**

The blockbuster investment comes as India pushes to gain a stronger foothold in the global artificial intelligence race.

🔗 [CNBC](https://www.cnbc.com/2026/02/17/india-adani-ai-data-centers-investment.html) • 23h ago

---

---

## Google News: "ai"

**[India tells university to leave AI summit after presenting Chinese robot as its own, sources say](https://www.reuters.com/world/china/india-tells-university-leave-ai-summit-after-presenting-chinese-robot-its-own-2026-02-18/)**

Reuters • 3h ago

---

**[India boots a private university from an AI summit over a robot dog controversy](https://www.wral.com/news/ap/850ac-india-boots-a-private-university-from-an-ai-summit-over-a-robot-dog-controversy/)**

NEW DELHI (AP) — A private Indian university was booted from a top artificial intelligence summit in New Delhi on Wednesday after one of its staffers displayed a commercially available robotic dog made in China, claiming it was the university's own innovation.

WRAL • 1h ago

---

**[Indian University Told to Exit AI Summit Over Robot Claim](https://www.bloomberg.com/news/articles/2026-02-18/indian-university-told-to-exit-ai-summit-over-robot-claim)**

Bloomberg.com • 1h ago

---

**[Race for AI is making Hindenburg-style disaster ‘a real risk’, says leading expert](https://www.theguardian.com/science/2026/feb/17/ai-race-hindenburg-style-disaster-a-real-risk-michael-wooldridge)**

Prof Michael Wooldridge says scenario such as deadly self-driving car update or AI hack could destroy global interest

The Guardian • 9h ago

---

**[How the global effort to keep AI safe went off the rails](https://www.politico.eu/article/how-the-global-effort-to-keep-ai-safe-went-off-the-rails/)**

Those gathered in New Delhi are no longer obsessing about how to control AI risks but figuring out who can benefit.

politico.eu • 14h ago

---

**[AI Impact Summit 2026: How we’re partnering to make AI work for everyone](https://blog.google/innovation-and-ai/technology/ai/ai-impact-summit-2026-india/)**

An overview of Google’s new global partnerships and funding announcements at the AI Impact Summit in India.

blog.google • 1h ago

---

**[Battle over AI regulation hits the airwaves ahead of midterms](https://thehill.com/policy/technology/5742396-ai-regulation-midterm-ads/)**

The Hill • 39m ago

---

**[Can A.I. Already Do Your Job?](https://www.nytimes.com/2026/02/18/podcasts/the-daily/ai-vibecoding-claude-code.html)**

The New York Times • 39m ago

---

**[AI Losers Get Another Chance at Janus Henderson Sustainable Fund](https://www.bloomberg.com/news/articles/2026-02-18/ai-losers-get-another-chance-at-janus-henderson-sustainable-fund)**

Bloomberg.com • 39m ago

---

**[More than 50% of enterprise software could switch to AI, Mistral CEO says](https://www.cnbc.com/2026/02/18/ai-mistral-software-switch-ceo-india-ai-impact-summit.html)**

Software stocks have sold off on fears AI could eat into so-called software as a service, or SaaS, business models.

CNBC • 5h ago

---

---

## HackerNews: "ai"

**[Thousands of CEOs just admitted AI had no impact on employment or productivity](https://news.ycombinator.com/item?id=47055979)**

In the 1980s, economist Robert Solow made an observation that reminded economists of today’s AI boom: “You can see the computer age everywhere but in the productivity statistics.”

⬆️ 526 • 💬 432 • 9h ago • [Fortune](https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/)

---

**[CBS didn't air Rep. James Talarico interview out of fear of FCC](https://news.ycombinator.com/item?id=47049426)**

Colbert kicked off Monday's episode of "The Late Show" by saying that the network's lawyers told him he could not have Talarico on the broadcast.

⬆️ 490 • 💬 226 • 19h ago • [NBC News](https://www.nbcnews.com/business/media/stephen-colbert-cbs-james-talarico-fcc-rcna259341)

---

**[AI is destroying open source, and it's not even good yet](https://news.ycombinator.com/item?id=47042136)**

Over the weekend Ars Technica retracted an article because the AI a writer used hallucinated quotes from an open source library maintainer.
The irony here is the maintainer in question, Scott Shambaugh, was harassed by someone's AI agent over not merging it's AI slop code.
It's likely the bot was running through someone's local 'agentic AI' instance (likely using OpenClaw). The guy who built OpenClaw was just hired by OpenAI to "work on bringing agents to everyone." You'll have to forgive me if I'm not enthusastic about that.

⬆️ 404 • 💬 330 • 1d ago • [Jeff Geerling](https://www.jeffgeerling.com/blog/2026/ai-is-destroying-open-source/)

---

**[Anthropic tries to hide Claude's AI actions. Devs hate it](https://news.ycombinator.com/item?id=47033622)**

: The software doesn't show what files it's working on

⬆️ 393 • 💬 239 • 2d ago • [theregister.com](https://www.theregister.com/2026/02/16/anthropic_claude_ai_edits/)

---

**[Thanks a lot, AI: Hard drives are sold out for the year, says WD](https://news.ycombinator.com/item?id=47034192)**

AI companies have bought out Western Digital's storage capacity for 2026. It's only February.

⬆️ 373 • 💬 306 • 1d ago • [Mashable](https://mashable.com/article/ai-hard-drive-hdd-shortages-western-digital-sold-out)

---

**[Semantic ablation: Why AI writing is generic and boring](https://news.ycombinator.com/item?id=47049088)**

opinion: The subtractive bias we're ignoring

⬆️ 259 • 💬 191 • 19h ago • [theregister.com](https://www.theregister.com/2026/02/16/semantic_ablation_ai_writing/)

---

**[I guess I kinda get why people hate AI](https://news.ycombinator.com/item?id=47037628)**

I’m sitting on a lānai in a hotel in Waikiki beach, writing this article, and wondering if the job I am starting nine days from now will be my last.This is a...

⬆️ 163 • 💬 259 • 1d ago • [anthony.noided.media](https://anthony.noided.media/blog/ai/programming/2026/02/14/i-guess-i-kinda-get-why-people-hate-ai.html)

---

**[AI is going to kill app subscriptions](https://news.ycombinator.com/item?id=47024387)**

Curated niche app opportunities from Reddit, scored by difficulty and demand.

⬆️ 148 • 💬 239 • 2d ago • [nichehunt.app](https://nichehunt.app/blog/ai-going-to-kill-app-subscriptions)

---

**[AI optimism is a class privilege](https://news.ycombinator.com/item?id=47038134)**

I think I have an idea why we're so extremely divided on AI: it's because we have an intuitive sense of who it stands to benefit, and who stands to pay the costs. I think whether you see reason for optimism has a lot to do with which group you see yourself in.

⬆️ 132 • 💬 134 • 1d ago • [Josh Collinsworth](https://joshcollinsworth.com/blog/sloptimism)

---

**[An AI Agent Published a Hit Piece on Me – Forensics and More Fallout](https://news.ycombinator.com/item?id=47051956)**

⬆️ 109 • 💬 78 • 16h ago • [theshamblog.com](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-3/)

---

---

## YouTube Videos: "ai"

**[Viral article warns of looming impacts of artificial intelligence](https://www.youtube.com/watch?v=tYecUUyrIo8)**

Matt Shumer joins "CBS Mornings" to discuss his now viral article, "Something Big Is Happening." He writes that AI's "capability for ...

📺 CBS Mornings

👁️ 49K • 👍 881 • 💬 225 • ⏱️ 7:07 • 21h ago

---

**[How AI is breaking the SaaS business model...](https://www.youtube.com/watch?v=cxcb55zr2Q8)**

Run hundreds of coding agents in the cloud - https://oz.dev/fireship. Use code FIRESHIP to get one month of their Build plan for $5 ...

📺 Fireship

👁️ 335K • 👍 15K • 💬 879 • ⏱️ 5:02 • 17h ago

---

**[AI Safety Experts WARN: “We Have 2 Years Before Everything Changes!”](https://www.youtube.com/watch?v=nVRQ_ZxXKgg)**

Artificial intelligence and robotics are advancing at a pace few people are prepared for and AI experts are warning about the ...

📺 MotivationHub

👁️ 21K • 👍 280 • 💬 61 • ⏱️ 13:16 • 1d ago

---

**[THE AI DOC: OR HOW I BECAME AN APOCALOPTIMIST - Official Trailer [HD] - Only In Theaters March 27](https://www.youtube.com/watch?v=xkPbV3IRe4Y)**

"The most urgent film of our time.” THE AI DOC: OR HOW I BECAME AN APOCALOPTIMIST is only in theaters March 27. Watch ...

📺 Focus Features

👁️ 1.6M • 👍 719 • 💬 114 • ⏱️ 2:43 • 19h ago

---

**[AI is destroying open source, and it&#39;s not even good yet](https://www.youtube.com/watch?v=bZJ7A1QoUEI)**

This is why we can't have nice things. Referenced in this video: - Ars Technica's redaction: ...

📺 Jeff Geerling

👁️ 194K • 👍 13K • 💬 1K • ⏱️ 3:37 • 1d ago

---

**[Racist AI Content Floods The Internet](https://www.youtube.com/watch?v=Y3YcKIRqmaM)**

The racist Obama video was a sign of a larger problem, AI content denigrating Black people has been mass produced and ...

📺 Reese Waters

👁️ 89K • 👍 8K • 💬 1K • ⏱️ 36:30 • 2d ago

---

**[OpenAI Just “Absorbed” OpenClaw and the AI World Exploded](https://www.youtube.com/watch?v=ubVLeoglBYE)**

OpenAI just hired the creator of OpenClaw, one of the fastest-spreading open-source AI agent platforms in the world. At the same ...

📺 AI Revolution

👁️ 50K • 👍 1K • 💬 136 • ⏱️ 8:30 • 1d ago

---

**[Godfather of AI: The next 5 years Will Change Humanity Forever | Yoshua Bengio](https://www.youtube.com/watch?v=0fXGtQoJgNo)**

FREE guide: Turn AI Agent Skills Into Cash — 5 paths to monetize AI in 30 days: https://clickhubspot.com/d203f6 In this episode of ...

📺 Silicon Valley Girl

👁️ 29K • 👍 673 • 💬 72 • ⏱️ 29:31 • 1d ago

---

**[AI developer resignations mark ‘real wake-up call’ for people: Professor | Katie Pavlich Tonight](https://www.youtube.com/watch?v=XG0qKL1O_tY)**

MIT professor and AI expert Max Tegmark joins “Katie Pavlich Tonight” to discuss the multiple resignations at several AI ...

📺 NewsNation

👁️ 27K • 👍 648 • 💬 149 • ⏱️ 5:31 • 1d ago

---

**[Stop Using AI the Hard Way (Do this instead)](https://www.youtube.com/watch?v=4JMH-4kKMC8)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4ak6OTF Are you building an AI software ...

📺 Dan Martell

👁️ 38K • 👍 2K • 💬 160 • ⏱️ 11:21 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 170,238 • ❤️ 1,330 • 4d ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for generating human-like text. It excels at creative writing, summarization, and conversational AI tasks.

`text-generation` `228.7B`

⬇️ 40,292 • ❤️ 727 • 2d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal, causal language model with a hybrid Gated Delta Network and Mixture-of-Experts architecture. It excels at vision-language tasks, supports 201 languages, and features a 262K native context length, making it suitable for complex reasoning, coding, and agent-based applications.

`image-text-to-text` `403.4B`

⬇️ 46,837 • ❤️ 639 • 2d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It uniquely supports deep-search tasks with extensive tool use, making it suitable for advanced problem-solving and agentic applications.

`text-generation` `3.9B`

⬇️ 50,917 • ❤️ 554 • 1d ago

---

**[MiniCPM-SALA](https://huggingface.co/openbmb/MiniCPM-SALA)**

*OpenBMB*

MiniCPM-SALA is a hybrid LLM integrating sparse and linear attention for efficient million-token context modeling, achieving up to 3.5x faster inference and significantly reduced KV-cache overhead compared to dense baselines.

`text-generation` `9.5B`

⬇️ 4,151 • ❤️ 462 • 6d ago

---

**[personaplex-7b-v1](https://huggingface.co/nvidia/personaplex-7b-v1)**

*NVIDIA*

PersonaPlex-7B is a real-time speech-to-speech conversational model that jointly performs streaming speech understanding and generation. It enables natural conversational dynamics like interruptions and overlaps by concurrently processing user audio and generating its own spoken responses, conditioned on voice and text prompts for persona control.

`audio-to-audio`

⬇️ 440,168 • ❤️ 2,004 • 2d ago

---

**[MOSS-TTS](https://huggingface.co/OpenMOSS-Team/MOSS-TTS)**

*OpenMOSS*

MOSS-TTS is a family of high-fidelity, expressive speech and sound generation models supporting multilingual text-to-speech, dialogue, voice design, and sound effect generation for complex real-world scenarios.

`text-to-speech` `8.5B`

⬇️ 21,532 • ❤️ 240 • 4d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. It supports coding from visual inputs and features an 'Agent Swarm' for complex task decomposition and parallel execution, with a context length of 256K.

`image-text-to-text` `170.7B`

⬇️ 895,102 • ❤️ 2,232 • 13d ago

---

**[Ming-flash-omni-2.0](https://huggingface.co/inclusionAI/Ming-flash-omni-2.0)**

*inclusionAI*

Ming-flash-omni 2.0 is a SOTA 100B parameter omni-multimodal large language model (omni-MLLM) excelling in expert-level multimodal cognition, unified acoustic synthesis (speech, audio, music), and high-dynamic controllable image generation/manipulation. It enables advanced applications like immersive audio experiences, sophisticated image editing, and deep visual knowledge understanding.

`any-to-any`

⬇️ 6,912 • ❤️ 229 • 6d ago

---

**[Ring-2.5-1T](https://huggingface.co/inclusionAI/Ring-2.5-1T)**

*inclusionAI*

Ring-2.5-1T is an open-source trillion-parameter text generation model featuring a hybrid linear attention architecture for enhanced efficiency and reasoning. It excels in deep thinking tasks, achieving gold medal level in math competitions, and demonstrates strong long-horizon task execution for agentic programming frameworks.

`text-generation` `1012.5B`

⬇️ 3,593 • ❤️ 195 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BitDance: Scaling Autoregressive Generative Models with Binary Tokens](https://huggingface.co/papers/2602.14041)**

*Yuang Ai, Jiaming Han, Shaobin Zhuang et al. (10 authors)*

🏢 ByteDance

BitDance is a scalable autoregressive image generator that uses binary visual tokens and diffusion-based methods to achieve efficient high-resolution image generation with improved speed and performance.

▲ 20 • 💬 2 • ⭐ 153 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2602.14041) • [💻 code](https://github.com/shallowdream204/BitDance) • [🔗 project](https://bitdance.csuhan.com/)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 11 • 💬 1 • ⭐ 4,182 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 1 • 💬 0 • ⭐ 1,553 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 2 • 💬 0 • ⭐ 4,196 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 142 • 💬 19 • ⭐ 53,295 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 65 • 💬 6 • ⭐ 13,520 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 36 • 💬 1 • ⭐ 70,519 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 186 • 💬 12 • ⭐ 3,670 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[HeartMuLa: A Family of Open Sourced Music Foundation Models](https://huggingface.co/papers/2601.10547)**

*Dongchao Yang, Yuxin Xie, Yuguo Yin et al. (28 authors)*

A suite of open-source music foundation models is introduced, featuring components for audio-text alignment, lyric recognition, music coding, and large language model-based song generation with controllable attributes and scalable parameterization.

▲ 42 • 💬 4 • ⭐ 3,811 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.10547) • [💻 code](https://github.com/HeartMuLa/heartlib) • [🔗 project](https://heartmula.github.io/)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 67 • 💬 1 • ⭐ 7,867 • 27d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust`

⭐ 11.4k • 🔱 1.1k • 1h ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 6.2k • 🔱 475 • 7d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 3.7k • 🔱 171 • 15d ago

---

**[jamiepine/voicebox](https://github.com/jamiepine/voicebox)**

The open-source voice synthesis studio powered by Qwen3-TTS.

`TypeScript` `ai` `cuda` `mlx` `qwen3-tts` `qwen3-tts-ui`

⭐ 3.1k • 🔱 353 • 7d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router powering OpenClaw — by BlockRunAI

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 2.7k • 🔱 273 • 4h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 2.4k • 🔱 297 • 17h ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 2.4k • 🔱 162 • 5h ago

---

**[mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis)**

All-in-one AI framework & toolkit

`Python` `ai-agent` `ai-coding` `claude-code` `cli` `codex`

⭐ 2.2k • 🔱 112 • 1d ago

---

**[op7418/CodePilot](https://github.com/op7418/CodePilot)**

A native desktop GUI for Claude Code — chat, code, and manage projects visually. Built with Electron + Next.js.

`TypeScript` `ai` `anthropic` `claude` `claude-code` `desktop-app`

⭐ 2.0k • 🔱 212 • 5d ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"

`Python`

⭐ 1.8k • 🔱 242 • 18h ago

---

---

*Generated by PeekDeck - A glance is all you need*
