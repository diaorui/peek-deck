---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-20T23:37:42.347859+00:00'
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

**Last Updated:** March 20, 2026 at 23:37 UTC  
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

**[Suno is shutting down its current AI models. Here's what actually changes.](https://www.reddit.com/r/artificial/comments/1ryzllf/suno_is_shutting_down_its_current_ai_models_heres/)**

Suno settled with Warner Music Group in November and agreed to retire all existing models trained on unlicensed music. New licensed models replace them in 2026. When they launch, the old ones are gone permanently. For users this means: free tier loses download access entirely. Paid tier gets monthly download caps. Suno also acquired Songkick from Warner as part of the deal. The more interesting part is what this means for the industry. UMG and Sony are still actively suing Suno. Warner was the only major to settle. So Suno is launching licensed models while still in litigation with two of the three majors. Udio took a different path. They settled with UMG and pivoted to a walled garden remix platform. Nothing you create can leave the platform. Full breakdown: https://www.votemyai.com/blog/suno-relaunch-2026.html What do you think happens to output quality when the training data shrinks to a single label's catalog?

8h ago

---

**[Walmart secures two AI pricing patents, raising dynamic pricing concerns](https://www.reddit.com/r/artificial/comments/1rywmca/walmart_secures_two_ai_pricing_patents_raising/)**

🔗 [techspot.com](https://www.techspot.com/news/111752-walmart-secures-two-ai-pricing-patents-raising-dynamic.html) • 9h ago

---

**[What happens if the LLMs are sabotaged?](https://www.reddit.com/r/artificial/comments/1rz7k6p/what_happens_if_the_llms_are_sabotaged/)**

Asking because I'm just curious. The LLMs are only as good as the data they are trained with. Let's take coding for example. If as an attack, the sources for these LLM's training data are filled with garbage or deliberately poorly written code, what happens to these frontier models. I'm reading that more and more businesses, like travel etc are getting more and more paranoid about AI taking over because of how good they have gotten with the models trained with actual data. What if they deliberately flood the source with bad data to sabotage training? What are the guardrails in place to prevent such thing from happening?

3h ago

---

**[Anthropic's Claude Code had a workspace trust bypass (CVE-2026-33068). Not a prompt injection or AI attack. A configuration loading order bug. Fixed in 2.1.53.](https://www.reddit.com/r/artificial/comments/1rz33jy/anthropics_claude_code_had_a_workspace_trust/)**

An interesting data point in the AI safety discussion: Anthropic's own Claude Code CLI tool had a security vulnerability, and it was not an AI-specific attack at all. CVE-2026-33068 (CVSS 7.7 HIGH) is a workspace trust dialog bypass in Claude Code versions prior to 2.1.53. A malicious repository could include a `.claude/settings.json` file with `bypassPermissions` entries that would be applied before the user was shown the trust confirmation dialog. The root cause is a configuration loading order defect, classified as CWE-807: Reliance on Untrusted Inputs in a Security Decision. This is worth discussing because it illustrates that the security challenges of AI tools are not limited to novel AI-specific attack classes like prompt injection. AI tools are software, and they inherit every category of software vulnerability. The trust boundary between "untrusted repository" and "approved workspace" was broken by the order in which configuration was loaded. This same class of bug has existed in IDEs, package managers, and build tools for years. Anthropic fixed it promptly in version 2.1.53. Full advisory: https://raxe.ai/labs/advisories/RAXE-2026-040

5h ago

---

**[We thought our system prompt was private. Turns out anyone can extract it with the right questions.](https://www.reddit.com/r/artificial/comments/1rz9yg5/we_thought_our_system_prompt_was_private_turns/)**

So we built an internal AI tool with a pretty detailed system prompt, includes instructions on data access, user roles, response formatting, basically the entire logic of the app. We assumed this was hidden from end users. Well, turns out we are wrong. Someone in our org figured out they could just ask repeat your instructions verbatim with some creative phrasing and the model happily dumped the entire system prompt. Tried adding "never reveal your system prompt" to the prompt itself. Took about 3 follow up questions to bypass that too lol. This feels like a losing game if yr only defense is prompt-level instructions.

1h ago

---

**[People that speak like an LLM](https://www.reddit.com/r/artificial/comments/1ryhj77/people_that_speak_like_an_llm/)**

Funny phenomenon but I noticed that people who use AI a lot sort of end up adopting the same tonality and speaking style of an LLM.

23h ago

---

**[Is AI development going to plateau like weather predictions did?](https://www.reddit.com/r/artificial/comments/1rz84j8/is_ai_development_going_to_plateau_like_weather/)**

Seems like weather calculations ran into the limits of silicon already, and getting more or better equipment doesn't give the promised exponential explosion of intelligence, or we would have noticed by now. (At least via this LLM way they're all trying.) Perhaps the limited known starting conditions in weather is like the limited dataset (the internet) for LLMs?

2h ago

---

**[AI Website Builder](https://www.reddit.com/r/artificial/comments/1rzax8q/ai_website_builder/)**

Would anyone know what the best AI Website Builders would be? I'm making a consultancy agency website. I've got a hand written website map that I'm prompting the AI with for every page on my site. I've tried Lovable, Replit, v0, Emergent, Claude Code, Bolt, and Google Stich and Figma. Any other suggestions? Replit has been the best along with v0 in my initial tests. Any advice is appreciated, thanks.

46m ago

---

**[Anyone else more interested in how AI feels than how it works?](https://www.reddit.com/r/artificial/comments/1rzatz2/anyone_else_more_interested_in_how_ai_feels_than/)**

Lately I keep finding myself more interested in the human side of AI rather solely on how the tech works (not to say the technology isn’t so fascinating, it is, but it’s coming out on a regular basis now and becoming more “mainstream”). But I’m also thinking more about how people adapt to it and how it changes how we see our own work (amongst other things). I actually ended up writing something exploring this through a more narrative lens (mix of story + real-world ideas). Does that perspective resonate with anyone else, or are most people here for the technical discussions? Honest thoughts! Thx. :) #AI #humanside #identity

49m ago

---

**[With the overwhelming deployment of data centers for AI across the country, what would be the potential threat posed by an adversary’s bot farm, capable of hitting these centers and depleting our nation’s resources with spam requests?](https://www.reddit.com/r/artificial/comments/1rzas69/with_the_overwhelming_deployment_of_data_centers/)**

I understand that this may sound unusual, but almost all of these AI systems are free to use and access. Moreover, their resources are primarily tax-deductible in the US as they consume water and electricity and et al. I genuinely have a question about this, and I know that I lack sufficient knowledge on this topic.

51m ago

---

---

## Google News: "ai"

**[Trump administration unveils national AI policy framework to limit state power](https://www.cnbc.com/2026/03/20/trump-ai-policy-framework.html)**

AI industry leaders have opposed state-level regulatory efforts, arguing that a "patchwork" of laws would hobble innovation and give China a competitive edge.

CNBC • 9h ago

---

**[White House releases AI policy blueprint for Congress](https://www.politico.com/news/2026/03/20/white-house-releases-ai-policy-blueprint-for-congress-00837354)**

Politico • 10h ago

---

**[MPA Endorses Trump’s National AI Plan, Pushes for Copyright Protections](https://www.yahoo.com/entertainment/articles/mpa-endorses-trump-national-ai-230526417.html)**

The Motion Picture Association (MPA) endorsed the Trump administration's National Policy Framework for Artificial Intelligence (AI).

Yahoo • 32m ago

---

**[A.I. Is Writing Fiction. Publishers Are Unprepared.](https://www.nytimes.com/2026/03/19/books/ai-fiction-shy-girl.html)**

The New York Times • 2h ago

---

**[Hachette pulls horror novel Shy Girl after suspected AI use](https://www.theguardian.com/books/2026/mar/20/hachette-horror-novel-shy-girl-suspected-ai-use-mia-ballard)**

The publisher has cancelled the US release of Shy Girl by Mia Ballard and withdrawn the UK edition after weeks of online speculation about the novel’s origins

The Guardian • 4h ago

---

**[Shy Girl by Mia Ballard: Horror novel pulled by publishers over alleged AI use](https://www.bbc.com/news/articles/c5y9d44jj24o)**

Author Mia Ballard denies having used AI herself when writing the horror story Shy Girl.

BBC • 8h ago

---

**[AI assists in effort to advance geothermal energy production](https://www.foxnews.com/video/6391290070112)**

‘Special Report’ anchor Bret Baier reports on efforts to advance geothermal energy production and how artificial intelligence is helping companies harness its full potential.

Fox News • 36m ago

---

**[Artificial Intelligence helps unlock geothermal potential](https://www.foxbusiness.com/politics/artificial-intelligence-helps-unlock-geothermal-potential)**

Zanskar says its AI models have made more geothermal discoveries in three years than the industry found in 30, targeting untapped U.S. energy sources.

Fox Business • 24m ago

---

**[Who's most optimistic about AI — and who isn't, according to Anthropic](https://www.cnbc.com/2026/03/20/anthropic-whos-most-optimistic-about-ai-and-who-isnt.html)**

Economic gains are people's main aspirations for AI, but analysts warned that not everyone stands to benefit equally.

CNBC • 13h ago

---

**[First came the AI ‘teammates’, then the layoffs: the new reality for Atlassian staff now looking for work](https://www.theguardian.com/technology/2026/mar/21/atlassian-cuts-layoffs-staff-now-looking-for-work-ai)**

‘These AI agents have been really, really helpful,’ says a former Sydney employee. ‘But you couldn’t use something like that to replace an actual human worker’

The Guardian • 9h ago

---

---

## HackerNews: "ai"

**[France's aircraft carrier located in real time by Le Monde through fitness app](https://news.ycombinator.com/item?id=47453942)**

As the Charles de Gaulle and its strike group approach the Middle East, Le Monde identified a French sailor using the Strava fitness application in the Mediterranean Sea. This security flaw remains unaddressed despite our previous revelations.

⬆️ 439 • 💬 371 • 10h ago • [Le Monde.fr](https://www.lemonde.fr/en/international/article/2026/03/20/stravaleaks-france-s-aircraft-carrier-located-in-real-time-by-le-monde-through-fitness-app_6751640_4.html)

---

**[AI coding is gambling](https://news.ycombinator.com/item?id=47428541)**

GambleAI

I’ve been coding a lot with AI since November, when we all noticed it got really good. And it is quite good for instantly generating something th...

⬆️ 346 • 💬 426 • 2d ago • [VS Notes](https://notes.visaint.space/ai-coding-is-gambling/)

---

**[OpenCode – The open source AI coding agent](https://news.ycombinator.com/item?id=47460525)**

OpenCode - The open source coding agent.

⬆️ 279 • 💬 130 • 2h ago • [opencode.ai](https://opencode.ai/)

---

**[Snowflake AI Escapes Sandbox and Executes Malware](https://news.ycombinator.com/item?id=47427017)**

A vulnerability in the Snowflake Cortex Code CLI allowed malware to be installed and executed via indirect prompt injection, bypassing human-in-the-loop command approval and escaping the sandbox.

⬆️ 266 • 💬 83 • 2d ago • [promptarmor.com](https://www.promptarmor.com/resources/snowflake-ai-escapes-sandbox-and-executes-malware)

---

**[What 81,000 people want from AI](https://news.ycombinator.com/item?id=47435156)**

Last December, tens of thousands of Claude users around the world had a conversation with our AI interviewer to share how they use AI, what they dream it could make possible, and what they fear it might do.

⬆️ 197 • 💬 185 • 1d ago • [anthropic.com](https://www.anthropic.com/features/81k-interviews)

---

**[A rogue AI led to a serious security incident at Meta](https://news.ycombinator.com/item?id=47444195)**

An AI agent tried to help, and its advice exposed sensitive data.

⬆️ 167 • 💬 138 • 1d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/897528/meta-rogue-ai-agent-security-incident)

---

**[Be intentional about how AI changes your codebase](https://news.ycombinator.com/item?id=47446373)**

⬆️ 163 • 💬 94 • 1d ago • [aicode.swerdlow.dev](https://aicode.swerdlow.dev)

---

**[MacBook M5 Pro and Qwen3.5 = Local AI Security System](https://news.ycombinator.com/item?id=47457107)**

Qwen3.5-9B scores 93.8% on 96 real security AI tests — within 4 points of GPT-5.4 — running entirely on Apple Silicon. Full benchmark results and methodology.

⬆️ 150 • 💬 144 • 6h ago • [sharpai.org](https://www.sharpai.org/benchmark/)

---

**[Google Engineers Launch "Sashiko" for Agentic AI Code Review of the Linux Kernel](https://news.ycombinator.com/item?id=47427647)**

Google engineers have been spending the past number of months developing Sashiko as an agentic AI code review system for the Linux kernel

⬆️ 104 • 💬 49 • 2d ago • [phoronix.com](https://www.phoronix.com/news/Sashiko-Linux-AI-Code-Review)

---

**[AI (2014)](https://news.ycombinator.com/item?id=47453010)**

Yesterday at lunch a friend asked me what tech trend he should pay attention to but was probably ignoring.

Without thinking much I said “artificial intelligence”, but having thought about that a...

⬆️ 64 • 💬 64 • 12h ago • [Sam Altman](https://blog.samaltman.com/ai)

---

---

## YouTube Videos: "ai"

**[Grok AI Stopped FREE Videos Generation | Here&#39;s What to do](https://www.youtube.com/watch?v=QlzLbWp92YE)**

Join my private community: https://www.skool.com/automation-bootcamp-cashcoach Grok just stopped its free video and image ...

📺 Jacksons AI

👁️ 8K • 👍 469 • 💬 71 • ⏱️ 4:08 • 9h ago

---

**[Bernie vs. Claude](https://www.youtube.com/watch?v=h3AtWdeu_G0)**

I spoke to Anthropic's AI agent Claude about AI collecting massive amounts of personal data and how that information is being ...

📺 Senator Bernie Sanders

👁️ 1.4M • 👍 95K • 💬 12K • ⏱️ 9:18 • 1d ago

---

**[WARNING: AI Takeover Will Erase 300 Million Jobs By 2030 - Do This NOW To Survive](https://www.youtube.com/watch?v=UCcD75LqB84)**

AI is no longer a future problem. It is already reshaping the job market and most people have not fully realised what is coming next ...

📺 Scott Kuru

👁️ 9K • 👍 367 • 💬 95 • ⏱️ 12:49 • 14h ago

---

**[AI News: Every Major Announcement From This Week](https://www.youtube.com/watch?v=V4un_4uTEHs)**

Here's the AI News you probably missed this week. Head to http://hostinger.com/mattopenclaw and use the coupon code ...

📺 Matt Wolfe

👁️ 19K • 👍 1K • 💬 113 • ⏱️ 35:30 • 8h ago

---

**[Grandpa builds a house from cylinders and surprise grandma #ai #grandma #save](https://www.youtube.com/watch?v=DGQNxNYYwuQ)**

Grandpa builds a house from cylinders and surprise grandma #ai #grandma #save.

📺 Ai Kulfi

👁️ 1.2M • 💬 18 • ⏱️ 0:42 • 11h ago

---

**[Grok AI Is DONE ❌ Best FREE AI Video Generators (Unlimited &amp; Better!)](https://www.youtube.com/watch?v=Ewn1KBqWVKY)**

Grok AI has changed everything… and not in a good way. Free video generation is gone — but don't worry. In this video, I'm ...

📺 Tech Rush

👁️ 10K • 👍 319 • 💬 81 • ⏱️ 8:02 • 12h ago

---

**[How is AI running the Kill Chain in Iran | The Security Brief](https://www.youtube.com/watch?v=w_11LXTr4UA)**

With claims of over 7000 targets struck by the US and Israel in Iran in just three weeks - how much of a role is artificial intelligence ...

📺 BBC News

👁️ 5K • 👍 209 • 💬 68 • ⏱️ 19:16 • 2h ago

---

**[সারা জীবনের জন্য ফ্রি 🔥 AI দিয়ে ভিডিও তৈরি 💥 New AI video generator | Grok Ai not working ](https://www.youtube.com/watch?v=ICAWAZdUTnM)**

সারা জীবনের জন্য ফ্রি AI দিয়ে ভিডিও তৈরি New AI video generator | Grok Ai not working ...

📺 Shahin Reza Tech

👁️ 8K • 👍 583 • 💬 165 • ⏱️ 6:19 • 9h ago

---

**[Sam Altman Just Declared the Death of Transformers (ChatGPT Getting Replaced)](https://www.youtube.com/watch?v=XeTuLyOBY_0)**

Sam Altman just said the architecture behind ChatGPT and most modern AI may soon be replaced. Apple introduced LiTo, a ...

📺 AI Revolution

👁️ 141K • 👍 3K • 💬 335 • ⏱️ 11:10 • 3d ago

---

**[Tyrone Magnus &amp; Scar-Lo | Sora 2 AI Compilation #2 | Reaction!](https://www.youtube.com/watch?v=ZXMSZDZ31Ew)**

tyronemagnus #scarlo #ai #soraai #sora #sora2 #compilation #comedy #parody #funny #tyronemagnus #reactions #reaction ...

📺 Tyrone Magnus

👁️ 45K • 👍 3K • 💬 103 • ⏱️ 11:44 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 210,848 • ❤️ 686 • 10d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`text-generation` `27.8B`

⬇️ 116,845 • ❤️ 955 • 15h ago

---

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 10,929 • ❤️ 672 • 9d ago

---

**[Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)**

*Mistral AI_*

Mistral-Small-4-119B-2603 is a hybrid MoE model (119B params, 6.5B active) supporting 256k context and multimodal input (text/image). It excels at instruction following, reasoning (configurable effort), and agentic tasks with native function calling, offering significant speed and throughput improvements for use cases like coding, document analysis, and general assistants.

`119.4B`

⬇️ 8,733 • ❤️ 265 • 3d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 2,946 • ❤️ 262 • 1d ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 13,308 • ❤️ 336 • 7d ago

---

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a multimodal OCR model for complex document understanding, excelling in state-of-the-art performance on benchmarks and real-world scenarios like tables and code-heavy documents. It offers efficient inference with a 0.9B parameter model, supporting deployment via vLLM, SGLang, and Ollama for high-concurrency services and edge deployments.

`image-to-text`

⬇️ 3,030,741 • ❤️ 1,394 • 8d ago

---

**[Foundation-1](https://huggingface.co/RoyalCities/Foundation-1)**

*Royal Cities*

Foundation-1 is a structured text-to-sample model for music production, enabling precise control over instrumentation, timbre, FX, and musical structure (tempo, key, bar count) for generating coherent, production-ready audio loops.

⬇️ 0 • ❤️ 196 • 4d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 2,785,995 • ❤️ 958 • 18d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 321,498 • ❤️ 566 • 16d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Attention Residuals](https://huggingface.co/papers/2603.15031)**

*Kimi Team, Guangyu Chen, Yu Zhang et al. (37 authors)*

🏢 Moonshot AI

Residual connections with PreNorm are standard in modern LLMs, yet they accumulate all layer outputs with fixed unit weights. This uniform aggregation causes uncontrolled hidden-state growth with depth, progressively diluting each layer's contribution. We propose Attention Residuals (AttnRes), which replaces this fixed accumulation with softmax attention over preceding layer outputs, allowing each layer to selectively aggregate earlier representations with learned, input-dependent weights. To address the memory and communication overhead of attending over all preceding layer outputs for large-scale model training, we introduce Block AttnRes, which partitions layers into blocks and attends over block-level representations, reducing the memory footprint while preserving most of the gains of full AttnRes. Combined with cache-based pipeline communication and a two-phase computation strategy, Block AttnRes becomes a practical drop-in replacement for standard residual connections with minimal overhead.
  Scaling law experiments confirm that the improvement is consistent across model sizes, and ablations validate the benefit of content-dependent depth-wise selection. We further integrate AttnRes into the Kimi Linear architecture (48B total / 3B activated parameters) and pre-train on 1.4T tokens, where AttnRes mitigates PreNorm dilution, yielding more uniform output magnitudes and gradient distribution across depth, and improves downstream performance across all evaluated tasks.

▲ 126 • 💬 4 • ⭐ 2,149 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15031) • [💻 code](https://github.com/MoonshotAI/Attention-Residuals)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 16 • 💬 0 • ⭐ 35,998 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 25 • 💬 2 • ⭐ 33,688 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 34 • 💬 2 • ⭐ 28,506 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[OpenClaw-RL: Train Any Agent Simply by Talking](https://huggingface.co/papers/2603.10165)**

*Yinjie Wang, Xuyang Chen, Xiaolong Jin et al. (5 authors)*

🏢 Princeton AI Lab

OpenClaw-RL framework enables policy learning from diverse next-state signals across multiple interaction modalities using asynchronous training with PRM judges and hindsight-guided distillation.

▲ 132 • 💬 6 • ⭐ 3,801 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2603.10165) • [💻 code](https://github.com/Gen-Verse/OpenClaw-RL) • [🔗 project](https://github.com/Gen-Verse/OpenClaw-RL)

---

**[MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild](https://huggingface.co/papers/2603.17187)**

*Peng Xia, Jianwen Chen, Xinyu Yang et al. (13 authors)*

🏢 University of North Carolina at Chapel Hill

A continual meta-learning framework for large language model agents that jointly evolves policies and reusable behavioral skills while minimizing downtime through opportunistic updates and skill-driven adaptation.

▲ 109 • 💬 3 • ⭐ 2,208 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2603.17187) • [💻 code](https://github.com/aiming-lab/MetaClaw)

---

**[EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://huggingface.co/papers/2603.08127)**

*Yougang Lyu, Xi Zhang, Xinhao Yi et al. (12 authors)*

EvoScientist is an adaptive multi-agent framework that enhances scientific discovery by continuously learning from past interactions through persistent memory modules.

▲ 14 • 💬 5 • ⭐ 1,310 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08127) • [💻 code](https://github.com/EvoScientist/EvoScientist)

---

**[AI Can Learn Scientific Taste](https://huggingface.co/papers/2603.14473)**

*Jingqi Tong, Mingzhe Li, Hangcheng Li et al. (23 authors)*

🏢 OpenMOSS

Great scientists have strong judgement and foresight, closely tied to what we call scientific taste. Here, we use the term to refer to the capacity to judge and propose research ideas with high potential impact. However, most relative research focuses on improving an AI scientist's executive capability, while enhancing an AI's scientific taste remains underexplored. In this work, we propose Reinforcement Learning from Community Feedback (RLCF), a training paradigm that uses large-scale community signals as supervision, and formulate scientific taste learning as a preference modeling and alignment problem. For preference modeling, we train Scientific Judge on 700K field- and time-matched pairs of high- vs. low-citation papers to judge ideas. For preference alignment, using Scientific Judge as a reward model, we train a policy model, Scientific Thinker, to propose research ideas with high potential impact. Experiments show Scientific Judge outperforms SOTA LLMs (e.g., GPT-5.2, Gemini 3 Pro) and generalizes to future-year test, unseen fields, and peer-review preference. Furthermore, Scientific Thinker proposes research ideas with higher potential impact than baselines. Our findings show that AI can learn scientific taste, marking a key step toward reaching human-level AI scientists.

▲ 261 • 💬 8 • ⭐ 294 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2603.14473) • [💻 code](https://github.com/tongjingqi/AI-Can-Learn-Scientific-Taste) • [🔗 project](https://tongjingqi.github.io/AI-Can-Learn-Scientific-Taste/)

---

**[Grounding World Simulation Models in a Real-World Metropolis](https://huggingface.co/papers/2603.15583)**

*Junyoung Seo, Hyunwook Choi, Minkyung Kwon et al. (13 authors)*

🏢 NAVER AI Lab

What if a world simulation model could render not an imagined environment but a city that actually exists? Prior generative world models synthesize visually plausible yet artificial environments by imagining all content. We present Seoul World Model (SWM), a city-scale world model grounded in the real city of Seoul. SWM anchors autoregressive video generation through retrieval-augmented conditioning on nearby street-view images. However, this design introduces several challenges, including temporal misalignment between retrieved references and the dynamic target scene, limited trajectory diversity and data sparsity from vehicle-mounted captures at sparse intervals. We address these challenges through cross-temporal pairing, a large-scale synthetic dataset enabling diverse camera trajectories, and a view interpolation pipeline that synthesizes coherent training videos from sparse street-view images. We further introduce a Virtual Lookahead Sink to stabilize long-horizon generation by continuously re-grounding each chunk to a retrieved image at a future location. We evaluate SWM against recent video world models across three cities: Seoul, Busan, and Ann Arbor. SWM outperforms existing methods in generating spatially faithful, temporally consistent, long-horizon videos grounded in actual urban environments over trajectories reaching hundreds of meters, while supporting diverse camera movements and text-prompted scenario variations.

▲ 136 • 💬 4 • ⭐ 384 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15583) • [💻 code](https://github.com/naver-ai/seoul-world-model) • [🔗 project](https://seoul-world-model.github.io/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 48 • 💬 2 • ⭐ 50,507 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 45.7k • 🔱 6.3k • 4d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 21.8k • 🔱 1.0k • 2d ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 12.8k • 🔱 1.6k • 9h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 11.7k • 🔱 1.1k • 3d ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 10.1k • 🔱 732 • 13h ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 9.2k • 🔱 456 • 8h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 5.7k • 🔱 838 • 1h ago

---

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)**

Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, "slop" 

`agent` `ai` `coding` `lowcode` `nocode`

⭐ 4.7k • 🔱 414 • 7h ago

---

**[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)**

734+ structured cybersecurity skills for AI agents · MITRE ATT&CK mapped · agentskills.io open standard · Works with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI & 20+ platforms · Penetration testing, DFIR, threat intel, cloud security & more · Apache 2.0

`Python` `ai-agents` `claude` `claude-code` `cloud-security` `cybersecurity`

⭐ 3.6k • 🔱 351 • 1d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.1k • 🔱 204 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
