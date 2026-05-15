---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-15T04:35:07.072486+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 15, 2026 at 04:35 UTC  
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

**[Anthropic just published a pretty alarming 2028 AI scenario paper and it's not about AGI safety in the usual sense](https://www.reddit.com/r/artificial/comments/1td99uw/anthropic_just_published_a_pretty_alarming_2028/)**

Anthropic dropped a new research paper today outlining two possible futures for global AI leadership by 2028, and it reads more like a geopolitical briefing than a typical AI safety paper. The core argument: The US currently has a meaningful lead over China in frontier AI, primarily because of compute (chips). American and allied companies (NVIDIA, TSMC, ASML, etc.) built technology China simply can't replicate yet. Export controls have made that gap real. But China's labs have stayed surprisingly close through two workarounds: Chip smuggling + overseas data center access - PRC labs are apparently training on export-controlled US chips they shouldn't have. A Supermicro co-founder was recently charged for diverting $2.5B worth of servers to China. Distillation attacks - creating thousands of fake accounts on US AI platforms, harvesting model outputs at scale, and using that to train their own models. Essentially free-riding on billions in US R&D. The two scenarios for 2028: Scenario 1 (good): US closes the loopholes, enforces export controls properly, the compute gap widens to 11x, and US models stay 12-24 months ahead. Democracies set the norms for how AI is governed globally. Scenario 2 (bad): US doesn't act, China reaches near-parity, floods global markets with cheaper models, and the CCP ends up shaping global AI norms, including potentially exporting AI-enabled surveillance tools to other authoritarian governments. What makes this interesting beyond the politics: Their new model, Mythos Preview (released to select partners in April), apparently let Firefox fix more security bugs in one month than in all of 2025. That's the kind of capability jump they're warning China shouldn't be the first to achieve, specifically around autonomous vulnerability discovery. The framing worth discussing: Anthropic is explicitly calling distillation attacks "industrial espionage" and pushing for legislation to criminalize them. This positions them as political actors, not just AI researchers. Whether that's appropriate for an AI lab is a conversation worth having. What do you think - is the compute gap as decisive as they claim, or is algorithmic innovation enough to close it?

8h ago

---

**[Adaptive Markdown](https://www.reddit.com/r/artificial/comments/1tdhoxd/adaptive_markdown/)**

I’ve been working on an open-source document format / viewer idea I’m calling Adaptive Markdown. The basic idea is: instead of a document being static text it's controlled by coding agents. You interact with the document more like a live workspace. This has different implications depending on what you are doing. I made a short video demo here: https://youtu.be/H4MnFs8irm8 The thing I’m most excited about is academic / technical reading. In a few years I don’t think people will just read papers passively. I think they’ll translate passages, ask questions, generate examples, explore alternate proofs, run code, attach notes, convert math to Lean when possible, and keep all of that inside the document instead of scattered across chats and notebooks. This is trivial to do inside a browser with coding agent that has access to JS, CSS etc. Some possible use cases I’m thinking about: -Turning articles and books into personalized learning objects - lecture notes with automatically maintained structure -documents with embedded code, tables, consoles, images, audio, or video -AI-generated alt text and descriptions Incorporate Adaptive Markdown into automated work flows eventually, things like automatically recording audio in lectures and taking a picture of a blackboard and turning it into LaTeX notes inside the document It’s very early, but the workflow already feels surprisingly useful to me. GitHub: https://github.com/SemiSimpleMath/Adaptive-Markdown Curious whether this seems useful to anyone else, or whether I’m just overexcited because I built it. So far it's only configured for Anthropic coding-agent SDK, but in couple of days we will have it running on Codex as well.

3h ago

---

**[AWS user hit with 30000 dollar bill after Claude runaway on Bedrock](https://www.reddit.com/r/artificial/comments/1tcu7w5/aws_user_hit_with_30000_dollar_bill_after_claude/)**

An AWS user just stared down a $30,000 invoice after a Claude adventure on Bedrock with no guardrails catching it. Cost Anomaly Detection failed entirely, which matters because this is the exact tooling AWS markets as the safety net for runaway spend. Anthropic is now metering and throttling programmatic Claude usage at the API layer, a supply-side response that only makes sense if inference costs are genuinely outpacing what the pricing model can absorb. Then Tencent admitted its GPUs only pay for themselves when running personalized ads, a frank confession from a hyperscaler that general-purpose AI inference is burning money. Three separate layers of the stack, same wall. The agent deployment wave is accelerating into this cost crisis without slowing down. Notion turned its workspace into an agent orchestration hub competing directly with LangChain-style middleware, while TikTok replaced human media buyers with autonomous agents for campaign management at scale. Apple is internally debating whether autonomous agent submissions belong in the App Store at all, because no review framework exists for non-deterministic software. The tooling to manage agents is being built after the agents are already deployed. The security picture compounds this. LLMs are closing the skill gap on specific cybersecurity tasks faster than defenders anticipated, and separately, a company lost root access because an intruder just asked nicely, no exploit required. As AI lowers the cost of convincing impersonation, human-in-the-loop authentication becomes the weakest point in any stack. AI is now running live database queries during 911 calls, which means accountability frameworks for AI-mediated dispatch decisions do not yet exist but the deployments do. Not everything is distress signals. Clio hit $500M ARR on AI-native legal features, validating vertical SaaS built on foundation models at enterprise scale. Anthropic is growing 10x year-over-year while peers cut 10% of headcount, a divergence that suggests consolidation risk for mid-tier AI companies is accelerating fast. On the architecture side, a new MoE model displaced conventional voice activity detection for real-time voice, and a graduate student's cryptographic primitive based on proof complexity could harden systems against LLM-assisted cryptanalysis. Meanwhile xAI is running nearly 50 unpermitted gas turbines at Colossus 2, which tells you everything about how AI infrastructure buildout relates to compliance timelines. At least one major cloud provider announces mandatory spending caps or circuit-breakers specifically for LLM API calls within 60 days, driven by publicized runaway-cost incidents that their existing anomaly detection provably failed to catch.

18h ago

---

**[I think “human-in-the-loop” may become one of the biggest governance illusions in enterprise AI](https://www.reddit.com/r/artificial/comments/1td300k/i_think_humanintheloop_may_become_one_of_the/)**

Most enterprises currently believe they have a governance strategy for AI: “If something risky happens, a human will review it.” Sounds reasonable. But I think there’s a deeper structural problem emerging as AI systems move from recommendation → execution. Because modern AI systems don’t just generate answers anymore. Increasingly, they also: classify risk, estimate confidence, decide whether escalation is needed, determine what gets surfaced to humans, and silently handle everything else. Which creates a strange loop: The system being governed is also deciding when governance should begin. That feels like a very different problem from traditional software oversight. And I think this becomes dangerous because many failures may not even look like “AI hallucinations.” Sometimes the reasoning may be completely coherent… …but based on incomplete or incorrect representation of reality. Examples: stale customer state, merged identities, missing policy exceptions, incomplete operational context, outdated inventory state, hidden dependency failures, edge cases the AI never surfaced. In those cases, humans reviewing only the final output may miss the actual problem entirely. Another tension: If humans review everything → governance doesn’t scale. If humans review only what AI escalates → governance becomes dependent on AI self-reporting. That seems like a major architectural tension nobody has fully solved yet. I’m starting to think the future role of humans in enterprise AI may not be: “approve every AI output.” Instead, it may become: defining autonomy boundaries, deciding where escalation is mandatory, governing reversibility, auditing representation quality, handling ambiguity and institutional legitimacy, and deciding where AI should NOT act autonomously. In other words: less “human-in-the-loop” and more “human-governed autonomy.” Curious how others here think about this. Especially people building: agentic systems, enterprise copilots, workflow automation, AI operations, autonomous agents, or governance architectures.

12h ago

---

**[Why is AI training still so unfriendly for normal users?](https://www.reddit.com/r/artificial/comments/1tdktbt/why_is_ai_training_still_so_unfriendly_for_normal/)**

Genuine question. Why does almost every AI training setup still feel extremely engineer-focused? Most tools I’ve tried expect people to already understand things like: CUDA VRAM LoRA settings Docker dependency issues quantization optimizers terminal commands training configs Even simple fine-tuning workflows become confusing fast. I’ve been thinking a lot about whether there’s room for a much more beginner-friendly approach where users could basically: upload dataset → train → test → deploy while the system handles things like: GPU selection safe limits preventing huge billing mistakes deployment setup logs model storage Do people here actually want simpler AI training workflows, or do most users eventually learn the technical side anyway? Curious what the biggest pain points are for people who’ve tried training models themselves.

44m ago

---

**[What Reddit would say about a relationship situation and the archetypes are painfully accurate and funny](https://www.reddit.com/r/artificial/comments/1tdkgpp/what_reddit_would_say_about_a_relationship/)**

https://www.redditsays.app

1h ago

---

**[AI helps man recover $400,000 in Bitcoin 11 years after he got high and forgot password](https://www.reddit.com/r/artificial/comments/1tca9sb/ai_helps_man_recover_400000_in_bitcoin_11_years/)**

A Bitcoin holder has gone viral after claiming he recovered around $400,000 in BTC from a wallet that had been locked for more than a decade.

🔗 [Dexerto](https://www.dexerto.com/entertainment/ai-helps-man-recover-400000-in-bitcoin-11-years-after-he-got-high-and-forgot-password-3364678/) • 1d ago

---

**[All-in-one AI platforms are quietly taking over end-to-end production. Thoughts?](https://www.reddit.com/r/artificial/comments/1tdaejb/allinone_ai_platforms_are_quietly_taking_over/)**

Posters, trailers, full episode lists, even a Cannes slot lined up this year. Watched on Higgsfield 1-2 of them and was impressed, while some still looked a little bit like slop. The interesting part isn't the AI-Netflix angle though. It's that one platform did the whole thing end to end: character consistency, generation, multi-shot sequencing, audio, distribution. No 5 different tools, no Premiere stitching 47 clips together. Meanwhile Kling, Runway, Veo are all racing to perfect a single model. Higgsfield is quietly building the entire production stack under one roof. Is vertical integration the actual moat in AI video, or are single-model specialists still going to win on quality? Curious where people think this is heading.

8h ago

---

**[[Virtual] AI Saturdays - Learn how to setup a local LLM (16th May, 6 PM ET)](https://www.reddit.com/r/artificial/comments/1tdch80/virtual_ai_saturdays_learn_how_to_setup_a_local/)**

Hey folks This Saturday, May 16 at 6:00 PM ET, we're covering how to set up a local language model: running an LLM on your own machine instead of a private provider. RSVP here: https://www.meetup.com/chillnskill/events/314498136/

6h ago

---

**[Anthropic’s Claude Helps Recover Lost Bitcoin Wallet Holding $400K After 11 Years](https://www.reddit.com/r/artificial/comments/1tcvrjx/anthropics_claude_helps_recover_lost_bitcoin/)**

A Bitcoin holder reportedly regained access to a lost 5 BTC wallet after using Anthropic’s Claude to analyze old files and recovery clues.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/anthropic-claude-bitcoin-wallet-recovery/) • 16h ago

---

---

## Google News: "ai"

**[UCF Commencement Speaker Draws Boos After A.I. Remarks](https://www.nytimes.com/2026/05/14/style/ucf-commencement-ai-booed-gloria-caulfield.html)**

The New York Times • 11h ago

---

**[Cerebras prices IPO above expected range, as Wall Street braces for AI tsunami](https://www.cnbc.com/2026/05/13/cerebras-prices-ipo-above-expected-range-wall-street-expects-ai-flood.html)**

Cerebras raised $5.55 billion in its IPO, and with the chipmaker's offering, investors are gearing up for some even bigger AI deals later this year.

CNBC • 1d ago

---

**[Cerebras, A.I. Chip Maker, Rises 89% in Market Debut as Tech IPOs Ramp Up](https://www.nytimes.com/2026/05/14/technology/cerebras-ipo-ai.html)**

The New York Times • 11h ago

---

**[Frenzied IPO Highlights Wall Street’s AI Fervor](https://www.wsj.com/finance/stocks/frenzied-ipo-highlights-wall-streets-ai-fervor-8f1f94e2)**

WSJ • 7h ago

---

**[Adtek Files for Hong Kong IPO, Adding to Chinese AI Listings](https://www.bloomberg.com/news/articles/2026-05-15/adtek-files-for-hong-kong-ipo-adding-to-chinese-ai-listings)**

Bloomberg.com • 38m ago

---

**[AI Nightlife Booms In San Francisco With Robots As A Draw](https://www.forbes.com/sites/martineparis/2026/05/14/ai-nightlife-booms-in-san-francisco-with-robots-as-a-draw/)**

Robots are all the rage in the San Francisco AI party scene with much hype over humanoids. I met up with Agility Robotics to see how real the promise is.

Forbes • 1h ago

---

**[Future of Marketing Briefing: The brands winning at AI started with process not tech](https://digiday.com/marketing/future-of-marketing-briefing-the-brands-winning-at-ai-started-with-process-not-tech/)**

The most important AI lesson senior marketers are learning: start with the process not the agent.

Digiday • 31m ago

---

**[2028: Two scenarios for global AI leadership](https://www.anthropic.com/research/2028-ai-leadership)**

Our views on the AI competition between the US and China.

Anthropic • 10h ago

---

**[Too Much Is Happening Too Fast](https://www.theatlantic.com/technology/2026/05/too-much-happening-too-fast/687177/)**

The AI boom is meant to overwhelm you.

The Atlantic • 7h ago

---

**[Prepare for an AI jobs apocalypse](https://www.economist.com/leaders/2026/05/14/prepare-for-an-ai-jobs-apocalypse)**

The Economist • 19h ago

---

---

## HackerNews: "ai"

**[RTX 5090 and M4 MacBook Air: Can It Game?](https://news.ycombinator.com/item?id=48137145)**

What if you could strap a full desktop GPU to your MacBook Air? Turns out, you can.

⬆️ 521 • 💬 139 • 12h ago • [Scott's Blog](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/)

---

**[AI is making me dumb](https://news.ycombinator.com/item?id=48139148)**

It's so god damn tempting to use AI to write. Whether it is articles, code, or documents. I feel like using AI is diminishing my ability to write myself.

...

⬆️ 452 • 💬 279 • 10h ago • [James Pain's Weblog](https://jpain.io/god-damn-ai-is-making-me-dumb/)

---

**[Reimagining the mouse pointer for the AI era](https://news.ycombinator.com/item?id=48111581)**

Google DeepMind is transforming the mouse pointer into a context-aware AI partner. Move beyond the friction of traditional prompting with intuitive AI collaboration in Chrome and beyond.

⬆️ 251 • 💬 213 • 2d ago • [Google DeepMind](https://deepmind.google/blog/ai-pointer/)

---

**[Amazon employees are "tokenmaxxing" due to pressure to use AI tools](https://news.ycombinator.com/item?id=48110529)**

Workers are using an internal AI tool to automate non-essential tasks.

⬆️ 247 • 💬 252 • 2d ago • [Ars Technica](https://arstechnica.com/ai/2026/05/amazon-employees-are-tokenmaxxing-due-to-pressure-to-use-ai-tools/)

---

**[The US is winning the AI race where it matters most: commercialization](https://news.ycombinator.com/item?id=48121929)**

Energy matters for AI, but the decisive layers are cloud infrastructure, data, and commercialization. On those layers the United States is ahead by a wide margin.

⬆️ 231 • 💬 657 • 1d ago • [Anton Krylov](https://avkcode.github.io/blog/us-winning-ai-race.html)

---

**[Meta won't let you block its AI account on Threads](https://news.ycombinator.com/item?id=48126981)**

Hey Meta, why are Threads users angry?

⬆️ 192 • 💬 82 • 1d ago • [The Verge](https://www.theverge.com/tech/929091/meta-ai-threads-account-block)

---

**[The AI Zombification of Universities](https://news.ycombinator.com/item?id=48139355)**

“And so perfect parallel constructions fill the lecture halls, the take-home tests, the school newspapers, and perhaps even the idiom of student chatter.”

⬆️ 179 • 💬 183 • 9h ago • [thenewcritic.com](https://www.thenewcritic.com/p/the-great-zombification)

---

**[Ontario auditors find doctors' AI note takers routinely blow basic facts](https://news.ycombinator.com/item?id=48142188)**

60% of evaluated AI Scribe systems mixed up prescribed drugs in patient notes, auditors say

⬆️ 167 • 💬 75 • 5h ago • [theregister](https://www.theregister.com/ai-ml/2026/05/14/ontario-auditors-find-doctors-ai-note-takers-routinely-blow-basic-facts/5240771)

---

**[Show HN: Statewright – Visual state machines that make AI agents reliable](https://news.ycombinator.com/item?id=48108778)**

State machine guardrails for AI agents. Contribute to statewright/statewright development by creating an account on GitHub.

⬆️ 122 • 💬 54 • 2d ago • [GitHub](https://github.com/statewright/statewright)

---

**[The other half of AI safety](https://news.ycombinator.com/item?id=48129561)**

Why labs gate bioweapons but not breakdowns

⬆️ 97 • 💬 129 • 1d ago • [personalaisafety.com](https://personalaisafety.com/p/the-other-half-of-ai-safety)

---

---

## YouTube Videos: "ai"

**[The AI race is a lie](https://www.youtube.com/watch?v=NeutZWud2Ng)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 38K • 👍 4K • 💬 618 • ⏱️ 13:30 • 5h ago

---

**[You’re Not Behind (Yet): Learn AI Agents in 13 Minutes](https://www.youtube.com/watch?v=P5sKKnWCvzk)**

Subscribe to my newsletter → https://www.sandeepswadia.com/newsletter Most people still use AI like a better search box, but the ...

📺 theMITmonk

👁️ 33K • 👍 2K • 💬 44 • ⏱️ 13:10 • 15h ago

---

**[&quot;China Is The ENEMY&quot; - Ken Paxton DEFENDS Texas&#39; AI Data Center EXPLOSION](https://www.youtube.com/watch?v=9SCpLObZ_5M)**

AI data centers are rapidly expanding across Texas, sparking both excitement over economic growth and concerns from local ...

📺 Valuetainment

👁️ 6K • 👍 296 • 💬 95 • ⏱️ 5:08 • 10h ago

---

**[Is AI About to “Eat Everything”? (It’s Not.)](https://www.youtube.com/watch?v=5GezB1XyiQo)**

Cal Newport takes a critical look at recent AI News. More from Cal Download Cal's FREE guide to cultivating a deeper life: ...

📺 Cal Newport

👁️ 16K • 👍 612 • 💬 190 • ⏱️ 31:51 • 18h ago

---

**[🚨This CHILLING Warning about AI Robots is Absolutely Terrifying...](https://www.youtube.com/watch?v=NthiIKpTZpQ)**

Artificial Intelligence is evolving faster than society can regulate it, and recent AI experiments are raising serious concerns about ...

📺 BlazeTV

👁️ 8K • 👍 619 • 💬 82 • ⏱️ 9:49 • 1d ago

---

**[These 10 New Claude Skills Just Doubled My AI Subscription (For Free)](https://www.youtube.com/watch?v=AHGG7LHi07E)**

Join our WhatsApp Community: https://links.stayingahead.com/YT28 I tested 1000+ Claude AI Skills. Only these 10 made the cut.

📺 Vaibhav Sisinty

👁️ 68K • 👍 3K • 💬 171 • ⏱️ 14:06 • 1d ago

---

**[The AI Bubble Is A Lot Worse Than You Think — And It Could Crash The Market](https://www.youtube.com/watch?v=0ywwOZoj5dE)**

Could the AI boom be turning into something far more dangerous than people realise? In this video, we look at the growing ...

📺 EUREKA US

👁️ 1K • 👍 43 • 💬 8 • ⏱️ 14:08 • 10h ago

---

**[The biggest AI breakthrough in medicine &amp; drug discovery](https://www.youtube.com/watch?v=s3rNDndvav0)**

MAMMAL biology foundation model that understands genes, proteins, small molecules. Beats AlphaFold 3! #ai #ainews #science ...

📺 AI Search

👁️ 43K • 👍 3K • 💬 400 • ⏱️ 31:55 • 1d ago

---

**[Why Kwebbelkop&#39;s AI Failed Miserably](https://www.youtube.com/watch?v=3h-6Kgotoho)**

If you prefer listening while driving, working out, or just don't want to stay on YouTube, listen on Spotify!

📺 Ryan Pictures

👁️ 135K • 👍 4K • 💬 380 • ⏱️ 22:52 • 1d ago

---

**[AI is wild now](https://www.youtube.com/watch?v=HITUpHglMv4)**

Asmongold's Twitch: https://www.twitch.tv/zackrawrr ▻ Asmongold's X: https://x.com/asmongold ▻ Asmongold's Kick: ...

📺 Asmongold TV  

👁️ 358K • 👍 17K • 💬 6K • ⏱️ 25:34 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 627,368 • ❤️ 923 • 6d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 16,801 • ❤️ 530 • 19h ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 9,858 • ❤️ 325 • 2d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 130,808 • ❤️ 494 • 3d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,588,118 • ❤️ 3,954 • 9d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 9,482 • ❤️ 199 • 8d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 12,061 • ❤️ 369 • 18d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 74,765 • ❤️ 142 • 1d ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 67,190 • ❤️ 133 • 1d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 90,647 • ❤️ 256 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 67 • 💬 3 • ⭐ 75,463 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 5 • 💬 0 • ⭐ 17,207 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[Pixal3D: Pixel-Aligned 3D Generation from Images](https://huggingface.co/papers/2605.10922)**

*Dong-Yang Li, Wang Zhao, Yuxin Chen et al. (8 authors)*

🏢 ARC Lab, Tencent PCG

Pixal3D introduces a pixel-aligned 3D generation approach that addresses fidelity issues in 3D asset creation by establishing direct pixel-to-3D correspondences through back-projection conditioning.

▲ 23 • 💬 3 • ⭐ 619 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.10922) • [💻 code](https://github.com/TencentARC/Pixal3D) • [🔗 project](https://ldyang694.github.io/projects/pixal3d/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 34 • 💬 3 • ⭐ 24,714 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://huggingface.co/papers/2605.13724)**

*Yuchao Gu, Guian Fang, Yuxin Jiang et al. (7 authors)*

🏢 NVIDIA

AnyFlow introduces a novel any-step video diffusion distillation framework that improves upon consistency distillation by optimizing full ODE sampling trajectories through flow-map transition learning and backward simulation techniques.

▲ 80 • 💬 1 • ⭐ 202 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.13724) • [💻 code](https://github.com/NVlabs/AnyFlow) • [🔗 project](https://nvlabs.github.io/AnyFlow/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 19 • 💬 3 • ⭐ 11,381 • 27d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[World Action Models: The Next Frontier in Embodied AI](https://huggingface.co/papers/2605.12090)**

*Siyin Wang, Junhao Shi, Zhaoyang Fu et al. (14 authors)*

🏢 OpenMOSS

World Action Models unify predictive state modeling with action generation for embodied policy learning, forming a cohesive framework for understanding environment dynamics and action prediction.

▲ 56 • 💬 1 • ⭐ 215 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.12090) • [💻 code](https://github.com/OpenMOSS/Awesome-WAM) • [🔗 project](https://openmoss.github.io/Awesome-WAM/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 112 • 💬 10 • ⭐ 9,345 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture](https://huggingface.co/papers/2605.12500)**

*Haiwen Diao, Penghao Wu, Hanming Deng et al. (58 authors)*

🏢 SenseNova

Unified vision-language models treat understanding and generation as integrated processes rather than separate tasks, demonstrating strong performance across multiple multimodal capabilities including image synthesis and action reasoning.

▲ 158 • 💬 1 • ⭐ 1,730 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.12500) • [💻 code](https://github.com/OpenSenseNova/SenseNova-U1)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 79 • 💬 7 • ⭐ 4,559 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.9k • 🔱 2.9k • 17d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.0k • 🔱 864 • 10h ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 2.8k • 🔱 289 • 2h ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

A collection of agent skills for CAD, robotics and hardware design

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.8k • 🔱 320 • 7h ago

---

**[esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)**

DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.

`TypeScript` `agent` `agent-framework` `ai-agent` `ai-coding` `cli`

⭐ 2.5k • 🔱 132 • 26m ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.2k • 🔱 149 • 1h ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.2k • 🔱 228 • 4d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.0k • 🔱 315 • 7d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.0k • 🔱 337 • 15h ago

---

**[GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist)**

Portable AI agent orchestration with mechanical protocol enforcement. 186 agents, zero runtime dependencies.

`Python` `agent-framework` `agent-system` `ai-agents` `claude-code` `cursor-ide`

⭐ 1.7k • 🔱 338 • 21d ago

---

---

*Generated by PeekDeck - A glance is all you need*
