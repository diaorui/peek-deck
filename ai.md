---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-18T22:34:53.736192+00:00'
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

**Last Updated:** February 18, 2026 at 22:34 UTC  
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

**[At the India AI Impact Summit 2026, Galgotias University showcased a Unitree Go2 robot dog — a commercially available Chinese product — and presented it as an Indian breakthrough innovation.](https://www.reddit.com/r/artificial/comments/1r81g0b/at_the_india_ai_impact_summit_2026_galgotias/)**

It has now turned into a full-blown social media meltdown, and authorities have reportedly asked the university to withdraw from the AI show.

10h ago

---

**[I found Claude for Government buried in the Claude Desktop binary. Here's what Anthropic built, how it got deployed, and the line they're still holding against the Pentagon.](https://www.reddit.com/r/artificial/comments/1r7tsff/i_found_claude_for_government_buried_in_the/)**

https://aaddrick.com/blog/claude-for-government-the-last-lab-standing I maintain claude-desktop-debian on GitHub, so I had a full archive of builds to compare against. Claude for Government showed up on Anthropic's status tracker February 17th. I pulled the binary from the same day and confirmed the implementation in code. The whole gov mode gates on a single enterprise config key. Set customDeploymentUrl to claude.fedstart.com and the app reroutes everything: traffic, auth, telemetry, network egress. Palantir's FedStart platform handles the accreditation layer. Eight prior releases had zero trace of this code. It all landed in one build. There's also a $1 GSA OneGov deal that gives all three branches of government a year of access, and Sonnet 4.6 shipped the same day with a 1 million token context window. Full breakdown and a separate technical report with code samples linked above.

🔗 [aaddrick.com](https://aaddrick.com/blog/claude-for-government-the-last-lab-standing) • 17h ago

---

**[Sales reps at $11 billion AI startup ElevenLabs have to bring in 20 times their base salary, or they're out — VP says](https://www.reddit.com/r/artificial/comments/1r7pf2s/sales_reps_at_11_billion_ai_startup_elevenlabs/)**

AI startup ElevenLabs, valued at $11 billion, employs small teams with high sales quotas.

🔗 [Business Insider](https://www.businessinsider.com/elevenlabs-11-billion-ai-startup-ruthless-sales-strategy-2026-2) • 20h ago

---

**[Elon Musk Firms Enter Secret Pentagon Challenge for Voice-Based Drone Swarming Tech](https://www.reddit.com/r/artificial/comments/1r7jr7l/elon_musk_firms_enter_secret_pentagon_challenge/)**

"Elon Musk’s SpaceX and its subsidiary xAI are joining a secretive US Department of Defense competition centered on a voice command and control tool that could deploy multiple autonomous systems. The project, launched in January with a $100-million budget and a six-month timeline, requires software that could coordinate unmanned swarming operations across the air and at sea, according to Bloomberg. The Pentagon’s Defense Innovation Unit and its new Defense Autonomous Warfare Group under the US Special Operations Command are overseeing the competition. The contest will unfold in phases, starting with software development before advancing to live trials. SpaceX and xAI’s participation marks an expansion of Musk’s defense work into artificial intelligence-enabled weapons software, as the Pentagon moves to accelerate drone development and domestic manufacturing while cutting bureaucracy. It also follows Washington’s call for cost-effective counter-drone solutions, particularly to protect critical military and civilian infrastructure as well as large public events. Separately, xAI, alongside other firms such as ChatGPT owner OpenAI, secured defense contracts worth up to $200 million each last year to expand advanced artificial intelligence use across military systems."

🔗 [The Defense Post](https://thedefensepost.com/2026/02/17/pentagon-musk-voice-swarming/) • 1d ago

---

**[Using combine consensus of LLMs to remove (or smooth-reduce) their own flaws in decision making](https://www.reddit.com/r/artificial/comments/1r8070j/using_combine_consensus_of_llms_to_remove_or/)**

You probably know how llms hallucinate, hedge, don't anchor, confabulate, etc. While we look towards new models that are likely to get a bit better, but what can we do today, right now? Perhaps not a novel idea, but I was toying with making one llm check an opinion of another llm. This is specifically useful in areas where I am not competent. This is what llms are for, to advise, but llms have good days and bad days, and bad prompts.. Sometimes you need to walk an llm to get to the best opinion. This is fine when you can know the topic and appreciate that the final decision is close to what one can accept as good enough. But there are times when one can't know if that an opinion of llm is good enough to follow. But, man, one wants a bit of certainty in this uncertain and imperfect world. Somewhere down this rabit hole, I played games with llm, was pasting one llm's opinion into another llm to get another perspective and gauge how good the first opinion is. It was working out ok, I'd bring concerns back to the original llm and have it explain the choice there. The courier it back and after some back and forth, I felt like 2 llms was way better than one. Overall, it was producing better results, the combination of llms with a bit of hands-on of human orchestration. Got me thinking, why not automate. The issue was there that llms often didn't do a good job by themselves. The topic would be ignored, some minutia detail will be argued to death, it was often going off the rails. BUT! It was great when it worked. It got me thinking, what llms were missing is a structured protocol to hold llms on true and narrow. I started hooking up something close to human debate rules. And it got traction and results. The whole idea that came out is more complicated in the end, here are some interesting items: Overview: https://github.com/Alex-R-A/llm-argumentation-protocol/blob/main/PROTOCOL-EXPLAINED-FOR-HUMANS.md (here much talked about how to make llms be responsible for good outputs through adversarial debate) And a bit of theory: https://github.com/Alex-R-A/llm-argumentation-protocol/blob/main/SCIENTIFIC.md Then graphs: https://github.com/Alex-R-A/llm-argumentation-protocol/blob/main/PROTOCOL-FLOW-DIAGRAMS.md Overall, returning to the main point, you can make different llms (even across brands) argue to what they know, show proof of their thinking, and get to defend or attack a point. Again, this is cumulative wisdom, so to speak, and then adversarial consensus. Also, doesn't allow any one single llm to simply make stuff up, or give a poor quality answer. Github repo to the claude code skill: https://github.com/Alex-R-A/llm-argumentation-protocol

11h ago

---

**[AI summit (19th feb)](https://www.reddit.com/r/artificial/comments/1r7w1o3/ai_summit_19th_feb/)**

Going to attend AI Summit on 19th feb in Delhi, Anyone is going on the same day please connect, going alone need a company. Thanks Connect over DM.

15h ago

---

**[Sony Group tech can identify original music in AI-generated songs](https://www.reddit.com/r/artificial/comments/1r7vvdp/sony_group_tech_can_identify_original_music_in/)**

Japanese company seeks to help copyright holders receive share of revenue

🔗 [Nikkei Asia](https://asia.nikkei.com/business/technology/artificial-intelligence/sony-group-tech-can-identify-original-music-in-ai-generated-songs) • 15h ago

---

**[Self-hosted claude swarm running on the cloud and surviving restarts](https://www.reddit.com/r/artificial/comments/1r7n831/selfhosted_claude_swarm_running_on_the_cloud_and/)**

A self-hosted platform for running Claude agent swarms with a React UI, deployed on GCP Cloud Run. - simonstaton/ClaudeSwarm

🔗 [GitHub](https://github.com/simonstaton/ClaudeSwarm) • 22h ago

---

**[I love Claude but honestly some of the "Claude might have gained consciousness" nonsense that their marketing team is pushing lately is a bit off putting. They know better!](https://www.reddit.com/r/artificial/comments/1r6lw8i/i_love_claude_but_honestly_some_of_the_claude/)**

- Anthropic CEO Says Company No Longer Sure Whether Claude Is Conscious - Link - Anthropic revises Claude’s ‘Constitution,’ and hints at chatbot consciousness - Link

2d ago

---

**[India's Adani to invest $100 billion to develop renewable energy-powered AI-ready data centers over the next decade, seeking to establish the world’s largest integrated data center platform.](https://www.reddit.com/r/artificial/comments/1r74i7g/indias_adani_to_invest_100_billion_to_develop/)**

The blockbuster investment comes as India pushes to gain a stronger foothold in the global artificial intelligence race.

🔗 [CNBC](https://www.cnbc.com/2026/02/17/india-adani-ai-data-centers-investment.html) • 1d ago

---

---

## Google News: "ai"

**[Opinion | The A.I. Disruption We’ve Been Waiting for Has Arrived](https://www.nytimes.com/2026/02/18/opinion/ai-software.html)**

The New York Times • 12h ago

---

**[I hacked ChatGPT and Google's AI – and it only took 20 minutes](https://www.bbc.com/future/article/20260218-i-hacked-chatgpt-and-googles-ai-and-it-only-took-20-minutes)**

I found a way to make AI tell you lies – and I'm not the only one.

BBC • 12h ago

---

**[AI data center firms are adopting optical gear inside facilities to cut energy and boost speed](https://www.axios.com/pro/climate-deals/2026/02/18/ai-data-centers-optical-gear)**

Axios • 52m ago

---

**[Stock market today: Dow, S&P 500 gain for 3rd straight day, Nasdaq jumps as traders brush aside AI worries](https://uk.finance.yahoo.com/news/stock-market-today-dow-sp-500-nasdaq-rise-as-ai-worries-recede-with-fed-minutes-ahead-235322634.html)**

Wall Street is entering the final stretch of this batch of earnings as AI dominates stock conversations.

Yahoo Finance UK • 45m ago

---

**[Inside David Einhorn's eclectic stock portfolio: The value investor shuns AI in favor of a unique mix of companies](https://www.cnbc.com/2026/02/18/inside-einhorns-eclectic-stock-portfolio-the-value-investor-shuns-ai.html)**

Einhorn's latest moves reflect his views on artificial intelligence and the market as a whole.

CNBC • 1h ago

---

**[Microsoft pledges $50 billion to tackle AI inequality as it warns of a ‘growing divide’](https://www.cnn.com/2026/02/18/business/ai-impact-summit-microsoft-inequality-investment)**

Microsoft says it is on track to invest $50 billion by the end of the decade to help bring artificial intelligence to lower-income countries, as concerns mount over the technology’s potential to deepen inequality.

CNN • 10h ago

---

**[A new way to express yourself: Gemini can now create music](https://blog.google/innovation-and-ai/products/gemini-app/lyria-3/)**

Lyria 3 is now available in the Gemini app. Create custom, high-quality 30-second tracks from text and images.

blog.google • 6h ago

---

**[The bogus four-day workweek that AI supposedly ‘frees up’](https://www.theguardian.com/technology/ng-interactive/2026/feb/18/ai-four-day-workweek)**

Business leaders tout AI as a path to shorter weeks and better balance. But without power, workers are unlikely to share the gains

The Guardian • 9h ago

---

**[AI giant Palantir moves its headquarters to Florida as tech company exodus continues](https://www.foxbusiness.com/technology/ai-giant-palantir-moves-its-headquarters-florida-tech-company-exodus-continues)**

Palantir joins the tech exodus to Florida as the AI innovator relocates its headquarters to Miami, following billionaires like Bezos and Thiel to the Sunshine State.

Fox Business • 6h ago

---

**[India tells university to leave AI summit after presenting Chinese robot as its own, sources say](https://www.reuters.com/world/china/india-tells-university-leave-ai-summit-after-presenting-chinese-robot-its-own-2026-02-18/)**

Reuters • 14h ago

---

---

## HackerNews: "ai"

**[AI adoption and Solow's productivity paradox](https://news.ycombinator.com/item?id=47055979)**

In the 1980s, economist Robert Solow made an observation that reminded economists of today’s AI boom: “You can see the computer age everywhere but in the productivity statistics.”

⬆️ 761 • 💬 688 • 20h ago • [Fortune](https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/)

---

**[CBS didn't air Rep. James Talarico interview out of fear of FCC](https://news.ycombinator.com/item?id=47049426)**

Colbert kicked off Monday's episode of "The Late Show" by saying that the network's lawyers told him he could not have Texas state Rep. James Talarico on the broadcast.

⬆️ 516 • 💬 242 • 1d ago • [NBC News](https://www.nbcnews.com/business/media/stephen-colbert-cbs-james-talarico-fcc-rcna259341)

---

**[AI is destroying open source, and it's not even good yet](https://news.ycombinator.com/item?id=47042136)**

Over the weekend Ars Technica retracted an article because the AI a writer used hallucinated quotes from an open source library maintainer.
The irony here is the maintainer in question, Scott Shambaugh, was harassed by someone's AI agent over not merging its AI slop code.
It's likely the bot was running through someone's local 'agentic AI' instance (likely using OpenClaw). The guy who built OpenClaw was just hired by OpenAI to "work on bringing agents to everyone." You'll have to forgive me if I'm not enthusastic about that.

⬆️ 412 • 💬 337 • 1d ago • [Jeff Geerling](https://www.jeffgeerling.com/blog/2026/ai-is-destroying-open-source/)

---

**[Anthropic tries to hide Claude's AI actions. Devs hate it](https://news.ycombinator.com/item?id=47033622)**

: The software doesn't show what files it's working on

⬆️ 393 • 💬 239 • 2d ago • [theregister.com](https://www.theregister.com/2026/02/16/anthropic_claude_ai_edits/)

---

**[Thanks a lot, AI: Hard drives are sold out for the year, says WD](https://news.ycombinator.com/item?id=47034192)**

AI companies have bought out Western Digital's storage capacity for 2026. It's only February.

⬆️ 374 • 💬 312 • 2d ago • [Mashable](https://mashable.com/article/ai-hard-drive-hdd-shortages-western-digital-sold-out)

---

**[Semantic ablation: Why AI writing is generic and boring](https://news.ycombinator.com/item?id=47049088)**

opinion: The subtractive bias we're ignoring

⬆️ 270 • 💬 206 • 1d ago • [theregister.com](https://www.theregister.com/2026/02/16/semantic_ablation_ai_writing/)

---

**[The Future of AI Software Development](https://news.ycombinator.com/item?id=47062534)**

fragments 18 Feb 2026

⬆️ 172 • 💬 126 • 6h ago • [martinfowler.com](https://martinfowler.com/fragments/2026-02-18.html)

---

**[I guess I kinda get why people hate AI](https://news.ycombinator.com/item?id=47037628)**

I’m sitting on a lānai in a hotel in Waikiki beach, writing this article, and wondering if the job I am starting nine days from now will be my last.This is a...

⬆️ 163 • 💬 259 • 2d ago • [anthony.noided.media](https://anthony.noided.media/blog/ai/programming/2026/02/14/i-guess-i-kinda-get-why-people-hate-ai.html)

---

**[AI optimism is a class privilege](https://news.ycombinator.com/item?id=47038134)**

I think I have an idea why we're so extremely divided on AI: it's because we have an intuitive sense of who it stands to benefit, and who stands to pay the costs. I think whether you see reason for optimism has a lot to do with which group you see yourself in.

⬆️ 132 • 💬 136 • 2d ago • [Josh Collinsworth](https://joshcollinsworth.com/blog/sloptimism)

---

**[An AI Agent Published a Hit Piece on Me – Forensics and More Fallout](https://news.ycombinator.com/item?id=47051956)**

⬆️ 117 • 💬 80 • 1d ago • [theshamblog.com](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-3/)

---

---

## YouTube Videos: "ai"

**[The AI Productivity Boom Finally Shows Up](https://www.youtube.com/watch?v=c5DaTmYqEEo)**

Revisions to Bureau of Labor Statistics job counts combined with strong GDP growth point to emerging AI-driven productivity ...

📺 The AI Daily Brief: Artificial Intelligence News

👁️ 4K • 👍 160 • 💬 26 • ⏱️ 12:15 • 1d ago

---

**[How AI is breaking the SaaS business model...](https://www.youtube.com/watch?v=cxcb55zr2Q8)**

Run hundreds of coding agents in the cloud - https://oz.dev/fireship. Use code FIRESHIP to get one month of their Build plan for $5 ...

📺 Fireship

👁️ 451K • 👍 19K • 💬 1K • ⏱️ 5:02 • 1d ago

---

**[AI Safety Experts WARN: “You Have No Idea What&#39;s Coming&quot;](https://www.youtube.com/watch?v=nVRQ_ZxXKgg)**

Artificial intelligence and robotics are advancing at a pace few people are prepared for and AI experts are warning about the ...

📺 MotivationHub

👁️ 24K • 👍 298 • 💬 68 • ⏱️ 13:16 • 2d ago

---

**[Viral article warns of looming impacts of artificial intelligence](https://www.youtube.com/watch?v=tYecUUyrIo8)**

Matt Shumer joins "CBS Mornings" to discuss his now viral article, "Something Big Is Happening." He writes that AI's "capability for ...

📺 CBS Mornings

👁️ 64K • 👍 1K • 💬 304 • ⏱️ 7:07 • 1d ago

---

**[THE AI DOC: OR HOW I BECAME AN APOCALOPTIMIST - Official Trailer [HD] - Only In Theaters March 27](https://www.youtube.com/watch?v=xkPbV3IRe4Y)**

"The most urgent film of our time.” THE AI DOC: OR HOW I BECAME AN APOCALOPTIMIST is only in theaters March 27. Watch ...

📺 Focus Features

👁️ 2.2M • 👍 1K • 💬 150 • ⏱️ 2:43 • 1d ago

---

**[Uproar Over AI-Generated Brad Pitt And Tom Cruise Fight Scene](https://www.youtube.com/watch?v=pDA1LMceoRY)**

There has been a growing uproar Monday over a fight scene between Brad Pitt and Tom Cruise. The A-list actors appeared to be ...

📺 Inside Edition

👁️ 141K • 👍 2K • 💬 648 • ⏱️ 2:11 • 2d ago

---

**[OpenAI Just “Absorbed” OpenClaw and the AI World Exploded](https://www.youtube.com/watch?v=ubVLeoglBYE)**

OpenAI just hired the creator of OpenClaw, one of the fastest-spreading open-source AI agent platforms in the world. At the same ...

📺 AI Revolution

👁️ 58K • 👍 2K • 💬 142 • ⏱️ 8:30 • 1d ago

---

**[AI agent hype will bankrupt you](https://www.youtube.com/watch?v=U5FPhnKMcKs)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 80K • 👍 3K • 💬 915 • ⏱️ 16:13 • 2d ago

---

**[AI is destroying open source, and it&#39;s not even good yet](https://www.youtube.com/watch?v=bZJ7A1QoUEI)**

This is why we can't have nice things. Referenced in this video: - Ars Technica's redaction: ...

📺 Jeff Geerling

👁️ 223K • 👍 14K • 💬 1K • ⏱️ 3:37 • 2d ago

---

**[Godfather of AI: The next 5 years Will Change Humanity Forever | Yoshua Bengio](https://www.youtube.com/watch?v=0fXGtQoJgNo)**

FREE guide: Turn AI Agent Skills Into Cash — 5 paths to monetize AI in 30 days: https://clickhubspot.com/d203f6 In this episode of ...

📺 Silicon Valley Girl

👁️ 36K • 👍 774 • 💬 92 • ⏱️ 29:31 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 170,238 • ❤️ 1,350 • 5d ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 40,292 • ❤️ 745 • 2d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text` `403.4B`

⬇️ 46,837 • ❤️ 667 • 2d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It's particularly noted for its native support of deep-search tasks and sustained problem-solving with extensive tool invocations.

`text-generation` `3.9B`

⬇️ 50,917 • ❤️ 566 • 1d ago

---

**[MiniCPM-SALA](https://huggingface.co/openbmb/MiniCPM-SALA)**

*OpenBMB*

MiniCPM-SALA is a hybrid LLM integrating sparse and linear attention for efficient million-token context modeling, achieving 3.5x faster inference and reduced KV-cache overhead on consumer GPUs.

`text-generation` `9.5B`

⬇️ 4,151 • ❤️ 462 • 7d ago

---

**[personaplex-7b-v1](https://huggingface.co/nvidia/personaplex-7b-v1)**

*NVIDIA*

PersonaPlex-7B-v1 is a real-time speech-to-speech conversational model that jointly performs streaming speech understanding and generation. It enables natural conversational dynamics like interruptions and overlaps by concurrently processing user audio and generating its own spoken responses, conditioned on voice and text prompts for persona control.

`audio-to-audio`

⬇️ 440,168 • ❤️ 2,026 • 3d ago

---

**[MOSS-TTS](https://huggingface.co/OpenMOSS-Team/MOSS-TTS)**

*OpenMOSS*

MOSS-TTS Family is a suite of high-fidelity, expressive speech and sound generation models supporting multilingual TTS, long-form synthesis, voice design, sound effects, and real-time streaming.

`text-to-speech` `8.5B`

⬇️ 21,532 • ❤️ 247 • 5d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and tool use grounded in visual inputs. Its key capabilities include coding from visual specifications and agent swarm execution for complex task decomposition, making it suitable for advanced visual reasoning and autonomous agent applications.

`image-text-to-text` `170.7B`

⬇️ 895,102 • ❤️ 2,242 • 13d ago

---

**[Ring-2.5-1T](https://huggingface.co/inclusionAI/Ring-2.5-1T)**

*inclusionAI*

Ring-2.5-1T is an open-source trillion-parameter text generation model featuring a hybrid linear attention architecture for enhanced efficiency and reasoning depth. It excels at long-horizon task execution and complex problem-solving, achieving state-of-the-art performance in areas like mathematics and agentic programming.

`text-generation` `1012.5B`

⬇️ 3,593 • ❤️ 199 • 3d ago

---

**[FireRed-Image-Edit-1.0](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.0)**

*FireRedTeam*

FireRed-Image-Edit-1.0 is a general-purpose image editing model with strong instruction following and text style preservation capabilities, suitable for tasks like photo restoration and multi-image editing.

`image-to-image`

⬇️ 1,148 • ❤️ 185 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BitDance: Scaling Autoregressive Generative Models with Binary Tokens](https://huggingface.co/papers/2602.14041)**

*Yuang Ai, Jiaming Han, Shaobin Zhuang et al. (10 authors)*

🏢 ByteDance

BitDance is a scalable autoregressive image generator that uses binary visual tokens and diffusion-based methods to achieve efficient high-resolution image generation with improved speed and performance.

▲ 21 • 💬 3 • ⭐ 205 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2602.14041) • [💻 code](https://github.com/shallowdream204/BitDance) • [🔗 project](https://bitdance.csuhan.com/)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 1 • 💬 0 • ⭐ 1,635 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 11 • 💬 1 • ⭐ 4,198 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 2 • 💬 0 • ⭐ 4,208 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 143 • 💬 19 • ⭐ 53,379 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 134 • 💬 6 • ⭐ 14,980 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 36 • 💬 1 • ⭐ 70,588 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 65 • 💬 6 • ⭐ 13,545 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 29 • 💬 2 • ⭐ 1,075 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 67 • 💬 1 • ⭐ 7,919 • 27d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust`

⭐ 12.9k • 🔱 1.3k • 5h ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 6.2k • 🔱 483 • 7d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 3.7k • 🔱 173 • 15d ago

---

**[jamiepine/voicebox](https://github.com/jamiepine/voicebox)**

The open-source voice synthesis studio powered by Qwen3-TTS.

`TypeScript` `ai` `cuda` `mlx` `qwen3-tts` `qwen3-tts-ui`

⭐ 3.7k • 🔱 408 • 8d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router powering OpenClaw — by BlockRunAI

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 2.8k • 🔱 278 • 4h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 2.5k • 🔱 305 • 9h ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 2.5k • 🔱 168 • 3h ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"

`Python`

⭐ 2.4k • 🔱 299 • 1d ago

---

**[mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis)**

All-in-one AI framework & toolkit

`Python` `ai-agent` `ai-coding` `claude-code` `cli` `codex`

⭐ 2.2k • 🔱 112 • 1d ago

---

**[op7418/CodePilot](https://github.com/op7418/CodePilot)**

A native desktop GUI for Claude Code — chat, code, and manage projects visually. Built with Electron + Next.js.

`TypeScript` `ai` `anthropic` `claude` `claude-code` `desktop-app`

⭐ 2.0k • 🔱 217 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*
