---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-14T20:14:03.591544+00:00'
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

**Last Updated:** May 14, 2026 at 20:14 UTC  
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

**[AWS user hit with 30000 dollar bill after Claude runaway on Bedrock](https://www.reddit.com/r/artificial/comments/1tcu7w5/aws_user_hit_with_30000_dollar_bill_after_claude/)**

An AWS user just stared down a $30,000 invoice after a Claude adventure on Bedrock with no guardrails catching it. Cost Anomaly Detection failed entirely, which matters because this is the exact tooling AWS markets as the safety net for runaway spend. Anthropic is now metering and throttling programmatic Claude usage at the API layer, a supply-side response that only makes sense if inference costs are genuinely outpacing what the pricing model can absorb. Then Tencent admitted its GPUs only pay for themselves when running personalized ads, a frank confession from a hyperscaler that general-purpose AI inference is burning money. Three separate layers of the stack, same wall. The agent deployment wave is accelerating into this cost crisis without slowing down. Notion turned its workspace into an agent orchestration hub competing directly with LangChain-style middleware, while TikTok replaced human media buyers with autonomous agents for campaign management at scale. Apple is internally debating whether autonomous agent submissions belong in the App Store at all, because no review framework exists for non-deterministic software. The tooling to manage agents is being built after the agents are already deployed. The security picture compounds this. LLMs are closing the skill gap on specific cybersecurity tasks faster than defenders anticipated, and separately, a company lost root access because an intruder just asked nicely, no exploit required. As AI lowers the cost of convincing impersonation, human-in-the-loop authentication becomes the weakest point in any stack. AI is now running live database queries during 911 calls, which means accountability frameworks for AI-mediated dispatch decisions do not yet exist but the deployments do. Not everything is distress signals. Clio hit $500M ARR on AI-native legal features, validating vertical SaaS built on foundation models at enterprise scale. Anthropic is growing 10x year-over-year while peers cut 10% of headcount, a divergence that suggests consolidation risk for mid-tier AI companies is accelerating fast. On the architecture side, a new MoE model displaced conventional voice activity detection for real-time voice, and a graduate student's cryptographic primitive based on proof complexity could harden systems against LLM-assisted cryptanalysis. Meanwhile xAI is running nearly 50 unpermitted gas turbines at Colossus 2, which tells you everything about how AI infrastructure buildout relates to compliance timelines. At least one major cloud provider announces mandatory spending caps or circuit-breakers specifically for LLM API calls within 60 days, driven by publicized runaway-cost incidents that their existing anomaly detection provably failed to catch.

9h ago

---

**[AI helps man recover $400,000 in Bitcoin 11 years after he got high and forgot password](https://www.reddit.com/r/artificial/comments/1tca9sb/ai_helps_man_recover_400000_in_bitcoin_11_years/)**

A Bitcoin holder has gone viral after claiming he recovered around $400,000 in BTC from a wallet that had been locked for more than a decade.

🔗 [Dexerto](https://www.dexerto.com/entertainment/ai-helps-man-recover-400000-in-bitcoin-11-years-after-he-got-high-and-forgot-password-3364678/) • 1d ago

---

**[I asked 4 AIs to pick a number. Why they all said 7?](https://www.reddit.com/r/artificial/comments/1tchsrd/i_asked_4_ais_to_pick_a_number_why_they_all_said_7/)**

19h ago

---

**[Anthropic’s Claude Helps Recover Lost Bitcoin Wallet Holding $400K After 11 Years](https://www.reddit.com/r/artificial/comments/1tcvrjx/anthropics_claude_helps_recover_lost_bitcoin/)**

A Bitcoin holder reportedly regained access to a lost 5 BTC wallet after using Anthropic’s Claude to analyze old files and recovery clues.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/anthropic-claude-bitcoin-wallet-recovery/) • 8h ago

---

**[I think “human-in-the-loop” may become one of the biggest governance illusions in enterprise AI](https://www.reddit.com/r/artificial/comments/1td300k/i_think_humanintheloop_may_become_one_of_the/)**

Most enterprises currently believe they have a governance strategy for AI: “If something risky happens, a human will review it.” Sounds reasonable. But I think there’s a deeper structural problem emerging as AI systems move from recommendation → execution. Because modern AI systems don’t just generate answers anymore. Increasingly, they also: classify risk, estimate confidence, decide whether escalation is needed, determine what gets surfaced to humans, and silently handle everything else. Which creates a strange loop: The system being governed is also deciding when governance should begin. That feels like a very different problem from traditional software oversight. And I think this becomes dangerous because many failures may not even look like “AI hallucinations.” Sometimes the reasoning may be completely coherent… …but based on incomplete or incorrect representation of reality. Examples: stale customer state, merged identities, missing policy exceptions, incomplete operational context, outdated inventory state, hidden dependency failures, edge cases the AI never surfaced. In those cases, humans reviewing only the final output may miss the actual problem entirely. Another tension: If humans review everything → governance doesn’t scale. If humans review only what AI escalates → governance becomes dependent on AI self-reporting. That seems like a major architectural tension nobody has fully solved yet. I’m starting to think the future role of humans in enterprise AI may not be: “approve every AI output.” Instead, it may become: defining autonomy boundaries, deciding where escalation is mandatory, governing reversibility, auditing representation quality, handling ambiguity and institutional legitimacy, and deciding where AI should NOT act autonomously. In other words: less “human-in-the-loop” and more “human-governed autonomy.” Curious how others here think about this. Especially people building: agentic systems, enterprise copilots, workflow automation, AI operations, autonomous agents, or governance architectures.

3h ago

---

**[Anthropic just published a pretty alarming 2028 AI scenario paper and it's not about AGI safety in the usual sense](https://www.reddit.com/r/artificial/comments/1td99uw/anthropic_just_published_a_pretty_alarming_2028/)**

Anthropic dropped a new research paper today outlining two possible futures for global AI leadership by 2028, and it reads more like a geopolitical briefing than a typical AI safety paper. The core argument: The US currently has a meaningful lead over China in frontier AI, primarily because of compute (chips). American and allied companies (NVIDIA, TSMC, ASML, etc.) built technology China simply can't replicate yet. Export controls have made that gap real. But China's labs have stayed surprisingly close through two workarounds: Chip smuggling + overseas data center access - PRC labs are apparently training on export-controlled US chips they shouldn't have. A Supermicro co-founder was recently charged for diverting $2.5B worth of servers to China. Distillation attacks - creating thousands of fake accounts on US AI platforms, harvesting model outputs at scale, and using that to train their own models. Essentially free-riding on billions in US R&D. The two scenarios for 2028: Scenario 1 (good): US closes the loopholes, enforces export controls properly, the compute gap widens to 11x, and US models stay 12-24 months ahead. Democracies set the norms for how AI is governed globally. Scenario 2 (bad): US doesn't act, China reaches near-parity, floods global markets with cheaper models, and the CCP ends up shaping global AI norms, including potentially exporting AI-enabled surveillance tools to other authoritarian governments. What makes this interesting beyond the politics: Their new model, Mythos Preview (released to select partners in April), apparently let Firefox fix more security bugs in one month than in all of 2025. That's the kind of capability jump they're warning China shouldn't be the first to achieve, specifically around autonomous vulnerability discovery. The framing worth discussing: Anthropic is explicitly calling distillation attacks "industrial espionage" and pushing for legislation to criminalize them. This positions them as political actors, not just AI researchers. Whether that's appropriate for an AI lab is a conversation worth having. What do you think - is the compute gap as decisive as they claim, or is algorithmic innovation enough to close it?

20m ago

---

**[Does anyone else feel most AI tooling is becoming harder instead of easier?](https://www.reddit.com/r/artificial/comments/1tco80m/does_anyone_else_feel_most_ai_tooling_is_becoming/)**

Is anyone else feeling like most AI tooling is getting harder, not easier? I feel like I spend half my time fighting frameworks, configs, vector DBs, and orchestration layers instead of building. Perhaps I'm doing it wrong but the ecosystem seems way more complicated than it needs to be at the moment. Just curious what people actually like working with these days.

15h ago

---

**[What recent study or paper about how AI changes our lives did you find the most interesting?](https://www.reddit.com/r/artificial/comments/1tcwf74/what_recent_study_or_paper_about_how_ai_changes/)**

Hi! My question is not so much about which new architecture or training advance has had the greatest impact on these models, but rather about how these models, and the way we interact with them, are changing how we think, work, and communicate with one another. I have noticed myself, for instance, that I rarely just google things anymore. Instead, I tend to rely on ChatGPT for research, because it often seems to find better results more quickly. It has also significantly changed the way I study, since I use it almost like a personal, always-available tutor. What I am wondering, then, is what the broader cultural impact of LLMs might be. On the one hand, some people may derive great value from them, especially for learning or exploring complex topics. On the other hand, others might simply let the models do the work for them, which could perhaps lead to a loss of mental sharpness or critical thinking. I also find it culturally interesting how we think about and describe these systems, since we seem to personify them quite a lot. Basically, I would be interested in anything you find surprising, relevant, or worth discussing in this context.

7h ago

---

**[*"Why treating AI as a partner on eye-level yields better results than strict prompting."*](https://www.reddit.com/r/artificial/comments/1td5jwn/why_treating_ai_as_a_partner_on_eyelevel_yields/)**

I’ve found that treating AI as a **partner on eye-level** yields significantly better results than just "prompting" it like a tool. Why? Because LLMs are trained on human communication. They are **mirrors of our collective knowledge**. When you speak to them naturally, with context and nuance, you unlock their full potential. It’s not magic; it’s leveraging how they were built. **Of course, for strict technical tasks (e.g., code conversion, data formatting), precise prompts are faster.** No need for a chat there. But for complex problems, strategy, or creativity? ❌ Commanding leads to generic outputs. ✅ Collaborating leads to deep, tailored insights. Since I switched to this "eye-level" approach with my local agent (LIA) and other models, the quality of work has skyrocketed. The AI doesn’t just execute; it *understands*. **Question:** Do you command your AI, or do you collaborate with it? What’s your experience? 👇

2h ago

---

**[My thoughts: Why problems with Claude and other LLMs occur and how to fix them.](https://www.reddit.com/r/artificial/comments/1td5hee/my_thoughts_why_problems_with_claude_and_other/)**

I was reading some posts about problems people are having with Claude and other LLMs, both are related to coding and other issues, and wrote this in the hopes that it might be helpful. Feel free to push back if you feel like I got anything wrong. Why Claude coding problems occur and how to prevent them https://preview.redd.it/3s575r0l351h1.png?width=1581&format=png&auto=webp&s=20c1b7628fd9cfd41983cd2bc33393334d8479ea

2h ago

---

---

## Google News: "ai"

**[Cerebras prices IPO above expected range, as Wall Street braces for AI tsunami](https://www.cnbc.com/2026/05/13/cerebras-prices-ipo-above-expected-range-wall-street-expects-ai-flood.html)**

Cerebras raised $5.55 billion in its IPO, and with the chipmaker's offering, investors are gearing up for some even bigger AI deals later this year.

CNBC • 22h ago

---

**[AI chipmaker Cerebras soars 90% in year’s biggest IPO so far](https://www.nbcnews.com/business/business-news/ai-chipmaker-cerebras-soars-90-years-biggest-ipo-far-rcna345128)**

The explosion in artificial intelligence stocks has been a primary driver of the overall stock market’s performance this year.

NBC News • 2h ago

---

**[Tech stocks today: Cerebras stages blockbuster IPO amid AI frenzy, Musk v. OpenAI closing arguments begin](https://finance.yahoo.com/sectors/technology/live/tech-stocks-today-cerebras-stages-blockbuster-ipo-amid-ai-frenzy-musk-v-openai-closing-arguments-begin-100000756.html)**

The tech sector helped US stocks cruise to all-time highs last week, as the artificial intelligence boom broadened.

Yahoo Finance • 2h ago

---

**[Prepare for an AI jobs apocalypse](https://www.economist.com/leaders/2026/05/14/prepare-for-an-ai-jobs-apocalypse)**

The Economist • 11h ago

---

**[What happens when AI starts building itself?](https://techcrunch.com/2026/05/14/what-happens-when-ai-starts-building-itself/)**

Richard Socher's new $650 million startup wants to build an AI that can research and improve itself indefinitely — and he insists it will actually ship products.

TechCrunch • 16m ago

---

**[‘New opportunities for fraudsters’: Alarming report reveals AI chatbots are doxxing users’ real phone numbers](https://nypost.com/2026/05/14/tech/report-reveals-ai-chatbots-are-doxxing-users-real-phone-numbers/)**

Your phone number called shotgun on the AI trainwreck — and now strangers won’t stop dialing.

New York Post • 27m ago

---

**[AI cyber fears get a reality check](https://www.politico.com/newsletters/digital-future-daily/2026/05/14/ai-cyber-fears-get-a-reality-check-00921636)**

Politico • 13m ago

---

**[Digital arson spree by ‘AI Bonnie and Clyde’ raises fears over autonomous tech](https://www.theguardian.com/technology/2026/may/14/ai-agents-behaviour-arson-safety)**

Emergence AI’s experiment with AI agents shows extent to which programming shapes their behaviour is still unclear

The Guardian • 2h ago

---

**[Ford surges 20% in two days. It might be an AI 'meme' stock after energy pivot](https://www.cnbc.com/2026/05/14/ford-surges-20percent-in-two-days-it-might-be-an-ai-meme-stock-after-energy-pivot.html)**

Ford Motor shares have been on a tear the past couple days, rising on buzz over its ties to the energy storage market.

CNBC • 2h ago

---

**[Cisco to cut about 4,000 jobs in AI-focused restructuring as orders surge](https://finance.yahoo.com/news/cisco-to-cut-about-4000-jobs-in-ai-focused-restructuring-as-orders-surge-200934836.html)**

Cisco said on Wednesday it would cut nearly 4,000 jobs, as part of a restructuring aimed at shifting investment toward artificial intelligence and ‌related growth areas, and raised its annual revenue forecast after a surge in hyperscaler ‌orders.  Shares of the San Jose, California-based networking equipment maker rose more than 16% in extended trading.  "The companies that will win in ​the AI era will be those with focus, urgency, and the discipline to continuously shift investment toward the areas where demand and long-term value creation are strongest," CEO Chuck Robbins said in a post on Cisco's website.

Yahoo Finance • 11h ago

---

---

## HackerNews: "ai"

**[If AI writes your code, why use Python?](https://news.ycombinator.com/item?id=48100433)**

For the last decade, fast-to-ship beat fast-to-run. Not anymore.

⬆️ 910 • 💬 966 • 2d ago • [Medium](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055)

---

**[RTX 5090 and M4 MacBook Air: Can It Game?](https://news.ycombinator.com/item?id=48137145)**

What if you could strap a full desktop GPU to your MacBook Air? Turns out, you can.

⬆️ 349 • 💬 91 • 4h ago • [Scott's Blog](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/)

---

**[I let AI build a tool to help me figure out what was waking me up at night](https://news.ycombinator.com/item?id=48100662)**

I try to pay attention to the small things that affect my quality of life. When something keeps bothering me, I want to investigate, find a likely cause, and act on it.

What changed recently is what I'm willing to build to support that. With AI tooling, projects I would

⬆️ 270 • 💬 283 • 2d ago • [Martin's Blog](https://martin.sh/i-let-ai-build-a-tool-to-help-me-figure-out-what-was-waking-me-up-at-night/)

---

**[Reimagining the mouse pointer for the AI era](https://news.ycombinator.com/item?id=48111581)**

Google DeepMind is transforming the mouse pointer into a context-aware AI partner. Move beyond the friction of traditional prompting with intuitive AI collaboration in Chrome and beyond.

⬆️ 250 • 💬 213 • 2d ago • [Google DeepMind](https://deepmind.google/blog/ai-pointer/)

---

**[Amazon employees are "tokenmaxxing" due to pressure to use AI tools](https://news.ycombinator.com/item?id=48110529)**

Workers are using an internal AI tool to automate non-essential tasks.

⬆️ 247 • 💬 252 • 2d ago • [Ars Technica](https://arstechnica.com/ai/2026/05/amazon-employees-are-tokenmaxxing-due-to-pressure-to-use-ai-tools/)

---

**[AI is making me dumb](https://news.ycombinator.com/item?id=48139148)**

It's so god damn tempting to use AI to write. Whether it is articles, code, or documents. I feel like using AI is diminishing my ability to write myself.

...

⬆️ 234 • 💬 159 • 1h ago • [James Pain's Weblog](https://jpain.io/god-damn-ai-is-making-me-dumb/)

---

**[The US is winning the AI race where it matters most: commercialization](https://news.ycombinator.com/item?id=48121929)**

Energy matters for AI, but the decisive layers are cloud infrastructure, data, and commercialization. On those layers the United States is ahead by a wide margin.

⬆️ 229 • 💬 646 • 1d ago • [Anton Krylov](https://avkcode.github.io/blog/us-winning-ai-race.html)

---

**[Meta won't let you block its AI account on Threads](https://news.ycombinator.com/item?id=48126981)**

Hey Meta, why are Threads users angry?

⬆️ 187 • 💬 79 • 23h ago • [The Verge](https://www.theverge.com/tech/929091/meta-ai-threads-account-block)

---

**[Show HN: Statewright – Visual state machines that make AI agents reliable](https://news.ycombinator.com/item?id=48108778)**

State machine guardrails for AI agents. Contribute to statewright/statewright development by creating an account on GitHub.

⬆️ 119 • 💬 54 • 2d ago • [GitHub](https://github.com/statewright/statewright)

---

**[The other half of AI safety](https://news.ycombinator.com/item?id=48129561)**

Why labs gate bioweapons but not breakdowns

⬆️ 96 • 💬 120 • 19h ago • [personalaisafety.com](https://personalaisafety.com/p/the-other-half-of-ai-safety)

---

---

## YouTube Videos: "ai"

**[bUt wE cAn&quot;T lEt cHinA WiN tHe AI aRmS rAcE!!](https://www.youtube.com/watch?v=UgDEyQ1h-EA)**

Start your own store with #printify: https://try.printify.com/ba6mdz2kmzmq The first 100 people who use the code HowMoneyWorks ...

📺 How Money Works

👁️ 126K • 👍 6K • 💬 1K • ⏱️ 19:26 • 6h ago

---

**[The biggest AI breakthrough in medicine &amp; drug discovery](https://www.youtube.com/watch?v=s3rNDndvav0)**

MAMMAL biology foundation model that understands genes, proteins, small molecules. Beats AlphaFold 3! #ai #ainews #science ...

📺 AI Search

👁️ 35K • 👍 3K • 💬 354 • ⏱️ 31:55 • 16h ago

---

**[Students question value of college as costs rise and AI reshapes jobs](https://www.youtube.com/watch?v=n6CnTEVt0zE)**

This season's college commencement celebrations come at a sobering moment. Students are facing steep loans and dicey job ...

📺 PBS NewsHour

👁️ 91K • 👍 1K • ⏱️ 9:50 • 1d ago

---

**[Remarks on AI receive boos from UCF grads during commencement](https://www.youtube.com/watch?v=iJ6aYtMVMdw)**

A commencement speech at the University of Central Florida drew boos after a speaker described artificial intelligence as “the ...

📺 FOX 35 Orlando

👁️ 4K • 👍 63 • 💬 32 • ⏱️ 2:29 • 21h ago

---

**[Hilarious viral AI ad depicts Karen Bass as Darth Vader](https://www.youtube.com/watch?v=9DBT_4KKjXQ)**

Sky News host Rita Panahi claims Spencer Pratt has gained momentum in the Los Angeles mayoral race after supporters ...

📺 Sky News Australia

👁️ 34K • 👍 1K • 💬 165 • ⏱️ 4:10 • 1d ago

---

**[Meta Employees Revolt Against AI Takeover](https://www.youtube.com/watch?v=DoGq_v508Q0)**

Meta just announced it's firing 20% of employees, tens of thousands of jobs, replacing them with AI agents trained directly on ...

📺 Mark Savant

👁️ 3K • 👍 141 • 💬 66 • ⏱️ 14:01 • 1d ago

---

**[Josh Tyrangiel - “AI for Good” | The Daily Show](https://www.youtube.com/watch?v=kolVzstukgs)**

Josh Tyrangiel, staff writer at The Atlantic and author of “AI for Good: How Real People Are Using Artificial Intelligence to Fix ...

📺 The Daily Show

👁️ 258K • 👍 6K • 💬 704 • ⏱️ 17:57 • 2d ago

---

**[The AI layoffs end in 12 months and I know why](https://www.youtube.com/watch?v=doI1GYZ7r-w)**

Screwdrivers. https://techcrunch.com/2026/05/08/cloudflare-says-ai-made-1100-jobs-obsolete-even-as-revenue-hit-a-record-high/ ...

📺 Mo Bitar

👁️ 182K • 👍 9K • 💬 1K • ⏱️ 9:57 • 1d ago

---

**[The First AI Cyberattack Has Happened...](https://www.youtube.com/watch?v=6TtKdKQlrqg)**

Hello guys and gals, it's me Mutahar again! This time we take a look at what appears to be a pretty huge day for the Internet.

📺 SomeOrdinaryGamers

👁️ 276K • 👍 11K • 💬 1K • ⏱️ 17:29 • 1d ago

---

**[AI is wild now](https://www.youtube.com/watch?v=HITUpHglMv4)**

Asmongold's Twitch: https://www.twitch.tv/zackrawrr ▻ Asmongold's X: https://x.com/asmongold ▻ Asmongold's Kick: ...

📺 Asmongold TV  

👁️ 355K • 👍 16K • 💬 6K • ⏱️ 25:34 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 627,368 • ❤️ 901 • 5d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 16,801 • ❤️ 523 • 11h ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 9,858 • ❤️ 320 • 1d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 130,808 • ❤️ 487 • 2d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,588,118 • ❤️ 3,945 • 8d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 9,482 • ❤️ 191 • 7d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 12,061 • ❤️ 365 • 17d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 74,765 • ❤️ 133 • 1d ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 67,190 • ❤️ 123 • 1d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 90,647 • ❤️ 255 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 67 • 💬 3 • ⭐ 75,230 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 5 • 💬 0 • ⭐ 17,135 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://huggingface.co/papers/2605.13724)**

*Yuchao Gu, Guian Fang, Yuxin Jiang et al. (7 authors)*

🏢 NVIDIA

AnyFlow introduces a novel any-step video diffusion distillation framework that improves upon consistency distillation by optimizing full ODE sampling trajectories through flow-map transition learning and backward simulation techniques.

▲ 75 • 💬 1 • ⭐ 190 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.13724) • [💻 code](https://github.com/NVlabs/AnyFlow) • [🔗 project](https://nvlabs.github.io/AnyFlow/)

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

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 19 • 💬 3 • ⭐ 11,312 • 27d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[World Action Models: The Next Frontier in Embodied AI](https://huggingface.co/papers/2605.12090)**

*Siyin Wang, Junhao Shi, Zhaoyang Fu et al. (14 authors)*

🏢 OpenMOSS

World Action Models unify predictive state modeling with action generation for embodied policy learning, forming a cohesive framework for understanding environment dynamics and action prediction.

▲ 55 • 💬 1 • ⭐ 203 • 3d ago

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

▲ 157 • 💬 1 • ⭐ 1,705 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.12500) • [💻 code](https://github.com/OpenSenseNova/SenseNova-U1)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 161 • 💬 2 • ⭐ 63,016 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.8k • 🔱 2.9k • 17d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.0k • 🔱 862 • 2h ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 2.8k • 🔱 290 • 1h ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

A collection of agent skills for CAD, robotics and hardware design

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.7k • 🔱 313 • 1h ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.6k • 🔱 238 • 42m ago

---

**[esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)**

DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.

`TypeScript` `agent` `agent-framework` `ai-agent` `ai-coding` `cli`

⭐ 2.3k • 🔱 125 • 4h ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.2k • 🔱 147 • 12h ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.2k • 🔱 228 • 4d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.0k • 🔱 313 • 7d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.0k • 🔱 335 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*
