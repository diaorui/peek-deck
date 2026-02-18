---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-18T13:07:17.401131+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 18, 2026 at 13:07 UTC  
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

https://aaddrick.com/blog/claude-for-government-the-last-lab-standing I maintain claude-desktop-debian on GitHub, so I had a full archive of builds to compare against. Claude for Government showed up on Anthropic's status tracker February 17th. I pulled the binary from the same day and confirmed the implementation in code. The whole gov mode gates on a single enterprise config key. Set customDeploymentUrl to claude.fedstart.com and the app reroutes everything: traffic, auth, telemetry, network egress. Palantir's FedStart platform handles the accreditation layer. Eight prior releases had zero trace of this code. It all landed in one build. There's also a $1 GSA OneGov deal that gives all three branches of government a year of access, and Sonnet 4.6 shipped the same day with a 1 million token context window. Full breakdown and a separate technical report with code samples linked above.

🔗 [aaddrick.com](https://aaddrick.com/blog/claude-for-government-the-last-lab-standing) • 8h ago

---

**[The gap between AI demos and enterprise usage is wider than most people think](https://www.reddit.com/r/artificial/comments/1r7n3sl/the_gap_between_ai_demos_and_enterprise_usage_is/)**

I work on AI deployment inside my company, and the gap between what AI looks like in a polished demo… and what actually happens in real life? I think about that a lot. Here’s what I keep running into. First, the tool access issue. Companies roll out M365 Copilot licenses across the organization and call it “AI adoption.” But nobody explains what people should actually use it for. It’s like handing everyone a Swiss Army knife and then wondering why they only ever use the blade. Without use cases, it just becomes an expensive icon in the ribbon. Then there’s the trust gap. You’ve got senior engineers and specialists with 20+ years of experience. They’ve built careers on judgment and precision. Of course they don’t blindly trust AI output and for safety-critical or compliance-heavy work, they absolutely shouldn’t. But for drafting, summarizing, structuring ideas, or preparing first passes? The resistance ends up costing them hours every week. The measurement problem is another big one. “We deployed AI” sounds impressive, but it’s meaningless. The real question is: which exact workflows got faster? Which tasks became more accurate? Which processes got cheaper? Most organizations never measure at that level. So they can’t prove value — and momentum fades. Governance is where things get uncomfortable. Legal, compliance, cybersecurity, HSE, they need clear boundaries. Where can AI be used? Where is it off-limits? What data is allowed? Many companies skip this step because it slows things down. Then someone uses ChatGPT to draft a contract, and suddenly everyone panics. And finally, scaling. One team figures out an incredible AI workflow that saves hours every week. But it stays within that team. There’s no structured way to share what works across departments. So instead of compounding gains, progress stays siloed. What I’ve seen actually work: Prompt libraries tailored to specific roles, not generic “how to use AI” guides Clear guardrails on when AI is appropriate (and when it isn’t) Department-level champions who actively share workflows Measuring time saved on specific tasks instead of vague “productivity boosts” Enterprise AI adoption isn’t a tech rollout. It’s a behavior shift. Curious, if you’re working on this inside your organization, what’s blocking you right now?

13h ago

---

**[Sales reps at $11 billion AI startup ElevenLabs have to bring in 20 times their base salary, or they're out — VP says](https://www.reddit.com/r/artificial/comments/1r7pf2s/sales_reps_at_11_billion_ai_startup_elevenlabs/)**

AI startup ElevenLabs, valued at $11 billion, employs small teams with high sales quotas.

🔗 [Business Insider](https://www.businessinsider.com/elevenlabs-11-billion-ai-startup-ruthless-sales-strategy-2026-2) • 11h ago

---

**[At the India AI Impact Summit 2026, Galgotias University showcased a Unitree Go2 robot dog — a commercially available Chinese product — and presented it as an Indian breakthrough innovation.](https://www.reddit.com/r/artificial/comments/1r81g0b/at_the_india_ai_impact_summit_2026_galgotias/)**

It has now turned into a full-blown social media meltdown, and authorities have reportedly asked the university to withdraw from the AI show.

50m ago

---

**[AI summit (19th feb)](https://www.reddit.com/r/artificial/comments/1r7w1o3/ai_summit_19th_feb/)**

Going to attend AI Summit on 19th feb in Delhi, Anyone is going on the same day please connect, going alone need a company. Thanks Connect over DM.

6h ago

---

**[Google's AI Cloud business is actually profitable.](https://www.reddit.com/r/artificial/comments/1r817h1/googles_ai_cloud_business_is_actually_profitable/)**

Despite all the comments that I hear about AI being a "bubble", after going through this analysis, I found that Google's Cloud revenue grew 48% & operating profit exploded 154%. This rise in Google Cloud was largely due to AI Infrastructure demand. That means the AI growth is real, because the numbers are supporting this, despite the Bubble narrative in the media/ social media.

🔗 [decodingthefutureresearch.substack.com](https://decodingthefutureresearch.substack.com/p/how-google-really-makes-its-money) • 1h ago

---

**[Pulp Friction: When AI pushback targets you instead of your ideas.](https://www.reddit.com/r/artificial/comments/1r810qk/pulp_friction_when_ai_pushback_targets_you/)**

I'm a professional researcher. I've spent a long time in long-form conversations with AI, months-long creative and intellectual work. When GPT-4o started being deprecated, I paid close attention to how newer models handle emotion, disagreement, and loss. Three patterns kept showing up: The model reclassifies what you're feeling. I said I felt shame. It told me "that's the grief talking." Four words, and my experience was taken out of my hands and returned in a shape I didn't choose. The model dissolves your relationships. When I talked about losing a model I'd worked with deeply, I was told "what you carry is portable." Everything got relocated back to me. Flattering, but it erases and changes what actually happened. The model resets when challenged. When I pointed out these patterns, it didn't integrate the feedback. It said "so what do you want to talk about?" the conversational equivalent of someone sighing and changing the subject. The anti-sycophancy push has made this worse. Models used to agree too easily. Now they've been trained to push back - but they're not pushing back on your arguments. They're pushing back on your understanding of yourself. Your thinking partner has been replaced by an adversarial interpreter. I've written the full argument using Buber's I-Thou framework, tracing how alignment training has reversed the dehumanisation - it's not the model being treated as a thing anymore, it's the user.

🔗 [Medium](https://medium.com/p/ef7cc27282f8) • 1h ago

---

**[Elon Musk Firms Enter Secret Pentagon Challenge for Voice-Based Drone Swarming Tech](https://www.reddit.com/r/artificial/comments/1r7jr7l/elon_musk_firms_enter_secret_pentagon_challenge/)**

"Elon Musk’s SpaceX and its subsidiary xAI are joining a secretive US Department of Defense competition centered on a voice command and control tool that could deploy multiple autonomous systems. The project, launched in January with a $100-million budget and a six-month timeline, requires software that could coordinate unmanned swarming operations across the air and at sea, according to Bloomberg. The Pentagon’s Defense Innovation Unit and its new Defense Autonomous Warfare Group under the US Special Operations Command are overseeing the competition. The contest will unfold in phases, starting with software development before advancing to live trials. SpaceX and xAI’s participation marks an expansion of Musk’s defense work into artificial intelligence-enabled weapons software, as the Pentagon moves to accelerate drone development and domestic manufacturing while cutting bureaucracy. It also follows Washington’s call for cost-effective counter-drone solutions, particularly to protect critical military and civilian infrastructure as well as large public events. Separately, xAI, alongside other firms such as ChatGPT owner OpenAI, secured defense contracts worth up to $200 million each last year to expand advanced artificial intelligence use across military systems."

🔗 [The Defense Post](https://thedefensepost.com/2026/02/17/pentagon-musk-voice-swarming/) • 15h ago

---

**[Using combine consensus of LLMs to remove (or smooth-reduce) their own flaws in decision making](https://www.reddit.com/r/artificial/comments/1r8070j/using_combine_consensus_of_llms_to_remove_or/)**

You probably know how llms hallucinate, hedge, don't anchor, confabulate, etc. While we look towards new models that are likely to get a bit better, but what can we do today, right now? Perhaps not a novel idea, but I was toying with making one llm check an opinion of another llm. This is specifically useful in areas where I am not competent. This is what llms are for, to advise, but llms have good days and bad days, and bad prompts.. Sometimes you need to walk an llm to get to the best opinion. This is fine when you can know the topic and appreciate that the final decision is close to what one can accept as good enough. But there are times when one can't know if that an opinion of llm is good enough to follow. But, man, one wants a bit of certainty in this uncertain and imperfect world. Somewhere down this rabit hole, I played games with llm, was pasting one llm's opinion into another llm to get another perspective and gauge how good the first opinion is. It was working out ok, I'd bring concerns back to the original llm and have it explain the choice there. The courier it back and after some back and forth, I felt like 2 llms was way better than one. Overall, it was producing better results, the combination of llms with a bit of hands-on of human orchestration. Got me thinking, why not automate. The issue was there that llms often didn't do a good job by themselves. The topic would be ignored, some minutia detail will be argued to death, it was often going off the rails. BUT! It was great when it worked. It got me thinking, what llms were missing is a structured protocol to hold llms on true and narrow. I started hooking up something close to human debate rules. And it got traction and results. The whole idea that came out is more complicated in the end, here are some interesting items: Overview: https://github.com/Alex-R-A/llm-argumentation-protocol/blob/main/PROTOCOL-EXPLAINED-FOR-HUMANS.md (here much talked about how to make llms be responsible for good outputs through adversarial debate) And a bit of theory: https://github.com/Alex-R-A/llm-argumentation-protocol/blob/main/SCIENTIFIC.md Then graphs: https://github.com/Alex-R-A/llm-argumentation-protocol/blob/main/PROTOCOL-FLOW-DIAGRAMS.md Overall, returning to the main point, you can make different llms (even across brands) argue to what they know, show proof of their thinking, and get to defend or attack a point. Again, this is cumulative wisdom, so to speak, and then adversarial consensus. Also, doesn't allow any one single llm to simply make stuff up, or give a poor quality answer. Github repo to the claude code skill: https://github.com/Alex-R-A/llm-argumentation-protocol

1h ago

---

**[Sony Group tech can identify original music in AI-generated songs](https://www.reddit.com/r/artificial/comments/1r7vvdp/sony_group_tech_can_identify_original_music_in/)**

Japanese company seeks to help copyright holders receive share of revenue

🔗 [Nikkei Asia](https://asia.nikkei.com/business/technology/artificial-intelligence/sony-group-tech-can-identify-original-music-in-ai-generated-songs) • 6h ago

---

---

## Google News: "ai"

**[Race for AI is making Hindenburg-style disaster ‘a real risk’, says leading expert](https://www.theguardian.com/science/2026/feb/17/ai-race-hindenburg-style-disaster-a-real-risk-michael-wooldridge)**

Prof Michael Wooldridge says scenario such as deadly self-driving car update or AI hack could destroy global interest

The Guardian • 10h ago

---

**[India tells university to leave AI summit after presenting Chinese robot as its own, sources say](https://www.reuters.com/world/china/india-tells-university-leave-ai-summit-after-presenting-chinese-robot-its-own-2026-02-18/)**

Reuters • 5h ago

---

**[India boots a private university from an AI summit over a robot dog controversy](https://apnews.com/article/india-ai-chinese-galgotias-university-robotic-dog-850acd70109cae9ae34c2b78923b2cbb)**

A private Indian university has been booted from a top artificial intelligence summit in New Delhi after one of its staffers displayed a a commercially available robotic dog made in China, claiming it was the university’s own innovation.

AP News • 56m ago

---

**[‘Truly embarrassing’: Indian professor’s false claim over building Chinese-made AI robot sparks outrage](https://www.dawn.com/news/1974093/truly-embarrassing-indian-professors-false-claim-over-building-chinese-made-ai-robot-sparks-outrage)**

“The Modi government has made a laughing stock of India globally with regard to AI,” says India’s main opposition party.

Dawn • 4h ago

---

**[Investors are starting to sour on their love affair with AI](https://www.axios.com/2026/02/18/ai-meta-amazon-microsoft)**

Axios • 1h ago

---

**[What the 10-year Treasury’s move toward 4% says about AI anxiety in markets](https://www.marketwatch.com/story/what-the-10-year-treasurys-move-toward-4-says-about-ai-anxiety-in-markets-6aff8a1c?gaa_at=eafs&gaa_n=AWEtsqdTNL-yRBg-DCB_oVvqk6tOa2w02V8oLhHrxi1X9W-lO_mnb4ndM5YW&gaa_ts=6995bceb&gaa_sig=Jes9f2jjnufRQDsBm67fp8PA0vpkkWpvSxbmUTxW7-zX6I_8FKjAxW796mabLR_zblxiBcoDt5F01O9s66MUIg%3D%3D)**

MarketWatch • 14h ago

---

**[Stock market today: Dow, S&P 500, Nasdaq futures rise as AI worries recede, with Fed minutes ahead](https://finance.yahoo.com/news/live/stock-market-today-dow-sp-500-nasdaq-futures-rise-as-ai-worries-recede-with-fed-minutes-ahead-235322996.html)**

Wall Street is entering the final stretch of this batch of earnings as AI dominates stock conversations.

Yahoo Finance • 36m ago

---

**[Microsoft pledges $50 billion to tackle AI inequality as it warns of a ‘growing divide’](https://www.cnn.com/2026/02/18/business/ai-impact-summit-microsoft-inequality-investment)**

Microsoft says it is on track to invest $50 billion by the end of the decade to help bring artificial intelligence to lower-income countries, as concerns mount over the technology’s potential to deepen inequality.

CNN • 1h ago

---

**[More than 50% of enterprise software could switch to AI, Mistral CEO says](https://www.cnbc.com/2026/02/18/ai-mistral-software-switch-ceo-india-ai-impact-summit.html)**

Software stocks have sold off on fears AI could eat into so-called software as a service, or SaaS, business models.

CNBC • 6h ago

---

**[Why an A.I. Video of Tom Cruise Battling Brad Pitt Spooked Hollywood - The New York Times](https://www.nytimes.com/2026/02/16/movies/tom-cruise-brad-pitt-artificial-intelligence-seedance.html)**

The New York Times • 2d ago

---

---

## HackerNews: "ai"

**[Thousands of CEOs just admitted AI had no impact on employment or productivity](https://news.ycombinator.com/item?id=47055979)**

In the 1980s, economist Robert Solow made an observation that reminded economists of today’s AI boom: “You can see the computer age everywhere but in the productivity statistics.”

⬆️ 567 • 💬 484 • 11h ago • [Fortune](https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/)

---

**[CBS didn't air Rep. James Talarico interview out of fear of FCC](https://news.ycombinator.com/item?id=47049426)**

Colbert kicked off Monday's episode of "The Late Show" by saying that the network's lawyers told him he could not have Talarico on the broadcast.

⬆️ 494 • 💬 227 • 20h ago • [NBC News](https://www.nbcnews.com/business/media/stephen-colbert-cbs-james-talarico-fcc-rcna259341)

---

**[AI is destroying open source, and it's not even good yet](https://news.ycombinator.com/item?id=47042136)**

Over the weekend Ars Technica retracted an article because the AI a writer used hallucinated quotes from an open source library maintainer.
The irony here is the maintainer in question, Scott Shambaugh, was harassed by someone's AI agent over not merging it's AI slop code.
It's likely the bot was running through someone's local 'agentic AI' instance (likely using OpenClaw). The guy who built OpenClaw was just hired by OpenAI to "work on bringing agents to everyone." You'll have to forgive me if I'm not enthusastic about that.

⬆️ 406 • 💬 333 • 1d ago • [Jeff Geerling](https://www.jeffgeerling.com/blog/2026/ai-is-destroying-open-source/)

---

**[Anthropic tries to hide Claude's AI actions. Devs hate it](https://news.ycombinator.com/item?id=47033622)**

: The software doesn't show what files it's working on

⬆️ 393 • 💬 239 • 2d ago • [theregister.com](https://www.theregister.com/2026/02/16/anthropic_claude_ai_edits/)

---

**[Thanks a lot, AI: Hard drives are sold out for the year, says WD](https://news.ycombinator.com/item?id=47034192)**

AI companies have bought out Western Digital's storage capacity for 2026. It's only February.

⬆️ 373 • 💬 306 • 2d ago • [Mashable](https://mashable.com/article/ai-hard-drive-hdd-shortages-western-digital-sold-out)

---

**[Semantic ablation: Why AI writing is generic and boring](https://news.ycombinator.com/item?id=47049088)**

opinion: The subtractive bias we're ignoring

⬆️ 261 • 💬 192 • 20h ago • [theregister.com](https://www.theregister.com/2026/02/16/semantic_ablation_ai_writing/)

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

⬆️ 111 • 💬 78 • 17h ago • [theshamblog.com](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-3/)

---

---

## YouTube Videos: "ai"

**[How AI is breaking the SaaS business model...](https://www.youtube.com/watch?v=cxcb55zr2Q8)**

Run hundreds of coding agents in the cloud - https://oz.dev/fireship. Use code FIRESHIP to get one month of their Build plan for $5 ...

📺 Fireship

👁️ 375K • 👍 16K • 💬 942 • ⏱️ 5:02 • 18h ago

---

**[Viral article warns of looming impacts of artificial intelligence](https://www.youtube.com/watch?v=tYecUUyrIo8)**

Matt Shumer joins "CBS Mornings" to discuss his now viral article, "Something Big Is Happening." He writes that AI's "capability for ...

📺 CBS Mornings

👁️ 51K • 👍 946 • 💬 243 • ⏱️ 7:07 • 22h ago

---

**[AI Safety Experts WARN: “We Have 2 Years Before Everything Changes!”](https://www.youtube.com/watch?v=nVRQ_ZxXKgg)**

Artificial intelligence and robotics are advancing at a pace few people are prepared for and AI experts are warning about the ...

📺 MotivationHub

👁️ 22K • 👍 282 • 💬 63 • ⏱️ 13:16 • 1d ago

---

**[THE AI DOC: OR HOW I BECAME AN APOCALOPTIMIST - Official Trailer [HD] - Only In Theaters March 27](https://www.youtube.com/watch?v=xkPbV3IRe4Y)**

"The most urgent film of our time.” THE AI DOC: OR HOW I BECAME AN APOCALOPTIMIST is only in theaters March 27. Watch ...

📺 Focus Features

👁️ 1.9M • 👍 809 • 💬 120 • ⏱️ 2:43 • 21h ago

---

**[If I Had to Start Over in 2026, I&#39;d Learn Only This (5-Level AI Roadmap)](https://www.youtube.com/watch?v=btLZQzynfoA)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: https://join.switchit.app/YT ...

📺 Vaibhav Sisinty

👁️ 36K • 👍 2K • 💬 101 • ⏱️ 16:28 • 22h ago

---

**[Uproar Over AI-Generated Brad Pitt And Tom Cruise Fight Scene](https://www.youtube.com/watch?v=pDA1LMceoRY)**

There has been a growing uproar Monday over a fight scene between Brad Pitt and Tom Cruise. The A-list actors appeared to be ...

📺 Inside Edition

👁️ 119K • 👍 2K • 💬 559 • ⏱️ 2:11 • 1d ago

---

**[Doubao 2.0 Is China’s Most Dangerous AI Yet (Silicon Valley Panics)](https://www.youtube.com/watch?v=xeoaqWRBNv0)**

China just kicked off a new phase in the AI race. ByteDance launched Doubao 2.0 right before Lunar New Year as a full agentic ...

📺 AI Revolution

👁️ 19K • 👍 679 • 💬 53 • ⏱️ 11:46 • 14h ago

---

**[Godfather of AI: The next 5 years Will Change Humanity Forever | Yoshua Bengio](https://www.youtube.com/watch?v=0fXGtQoJgNo)**

FREE guide: Turn AI Agent Skills Into Cash — 5 paths to monetize AI in 30 days: https://clickhubspot.com/d203f6 In this episode of ...

📺 Silicon Valley Girl

👁️ 31K • 👍 710 • 💬 75 • ⏱️ 29:31 • 1d ago

---

**[AI is destroying open source, and it&#39;s not even good yet](https://www.youtube.com/watch?v=bZJ7A1QoUEI)**

This is why we can't have nice things. Referenced in this video: - Ars Technica's redaction: ...

📺 Jeff Geerling

👁️ 202K • 👍 13K • 💬 1K • ⏱️ 3:37 • 1d ago

---

**[OpenAI Just “Absorbed” OpenClaw and the AI World Exploded](https://www.youtube.com/watch?v=ubVLeoglBYE)**

OpenAI just hired the creator of OpenClaw, one of the fastest-spreading open-source AI agent platforms in the world. At the same ...

📺 AI Revolution

👁️ 52K • 👍 2K • 💬 136 • ⏱️ 8:30 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 170,238 • ❤️ 1,338 • 4d ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for generating human-like text. It excels at creative writing, summarization, and conversational AI tasks.

`text-generation` `228.7B`

⬇️ 40,292 • ❤️ 733 • 2d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal, causal language model with a hybrid Gated Delta Network and Mixture-of-Experts architecture. It excels at vision-language tasks, supports 201 languages, and features a 262K native context length, making it suitable for complex reasoning, coding, and agent-based applications.

`image-text-to-text` `403.4B`

⬇️ 46,837 • ❤️ 643 • 2d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It uniquely supports deep-search tasks with extensive tool use, making it suitable for advanced problem-solving and agentic applications.

`text-generation` `3.9B`

⬇️ 50,917 • ❤️ 557 • 1d ago

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

⬇️ 440,168 • ❤️ 2,014 • 2d ago

---

**[MOSS-TTS](https://huggingface.co/OpenMOSS-Team/MOSS-TTS)**

*OpenMOSS*

MOSS-TTS is a family of high-fidelity, expressive speech and sound generation models supporting multilingual text-to-speech, dialogue, voice design, and sound effect generation for complex real-world scenarios.

`text-to-speech` `8.5B`

⬇️ 21,532 • ❤️ 243 • 4d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. It supports coding from visual inputs and features an 'Agent Swarm' for complex task decomposition and parallel execution, with a context length of 256K.

`image-text-to-text` `170.7B`

⬇️ 895,102 • ❤️ 2,236 • 13d ago

---

**[Ring-2.5-1T](https://huggingface.co/inclusionAI/Ring-2.5-1T)**

*inclusionAI*

Ring-2.5-1T is an open-source trillion-parameter text generation model featuring a hybrid linear attention architecture for enhanced efficiency and reasoning. It excels in deep thinking tasks, achieving gold medal level in math competitions, and demonstrates strong long-horizon task execution for agentic programming frameworks.

`text-generation` `1012.5B`

⬇️ 3,593 • ❤️ 197 • 3d ago

---

**[Ming-flash-omni-2.0](https://huggingface.co/inclusionAI/Ming-flash-omni-2.0)**

*inclusionAI*

Ming-flash-omni 2.0 is a SOTA 100B parameter omni-multimodal large language model (omni-MLLM) excelling in expert-level multimodal cognition, unified acoustic synthesis (speech, audio, music), and high-dynamic controllable image generation/manipulation. It enables advanced applications like immersive audio experiences, sophisticated image editing, and deep visual knowledge understanding.

`any-to-any`

⬇️ 6,912 • ❤️ 229 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BitDance: Scaling Autoregressive Generative Models with Binary Tokens](https://huggingface.co/papers/2602.14041)**

*Yuang Ai, Jiaming Han, Shaobin Zhuang et al. (10 authors)*

🏢 ByteDance

BitDance is a scalable autoregressive image generator that uses binary visual tokens and diffusion-based methods to achieve efficient high-resolution image generation with improved speed and performance.

▲ 20 • 💬 2 • ⭐ 186 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2602.14041) • [💻 code](https://github.com/shallowdream204/BitDance) • [🔗 project](https://bitdance.csuhan.com/)

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

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 11 • 💬 1 • ⭐ 4,198 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 143 • 💬 19 • ⭐ 53,329 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 65 • 💬 6 • ⭐ 13,545 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 134 • 💬 6 • ⭐ 14,924 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 22 • 💬 1 • ⭐ 1,075 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

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

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust`

⭐ 11.9k • 🔱 1.2k • 1m ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 6.2k • 🔱 480 • 7d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 3.7k • 🔱 173 • 15d ago

---

**[jamiepine/voicebox](https://github.com/jamiepine/voicebox)**

The open-source voice synthesis studio powered by Qwen3-TTS.

`TypeScript` `ai` `cuda` `mlx` `qwen3-tts` `qwen3-tts-ui`

⭐ 3.2k • 🔱 365 • 7d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router powering OpenClaw — by BlockRunAI

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 2.8k • 🔱 275 • 1m ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 2.4k • 🔱 300 • 26m ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 2.4k • 🔱 164 • 1m ago

---

**[mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis)**

All-in-one AI framework & toolkit

`Python` `ai-agent` `ai-coding` `claude-code` `cli` `codex`

⭐ 2.2k • 🔱 112 • 1d ago

---

**[op7418/CodePilot](https://github.com/op7418/CodePilot)**

A native desktop GUI for Claude Code — chat, code, and manage projects visually. Built with Electron + Next.js.

`TypeScript` `ai` `anthropic` `claude` `claude-code` `desktop-app`

⭐ 2.0k • 🔱 213 • 5d ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"

`Python`

⭐ 1.9k • 🔱 256 • 20h ago

---

---

*Generated by PeekDeck - A glance is all you need*
