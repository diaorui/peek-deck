---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-20T21:31:31.015535+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 20, 2026 at 21:31 UTC  
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

5h ago

---

**[Walmart secures two AI pricing patents, raising dynamic pricing concerns](https://www.reddit.com/r/artificial/comments/1rywmca/walmart_secures_two_ai_pricing_patents_raising/)**

🔗 [techspot.com](https://www.techspot.com/news/111752-walmart-secures-two-ai-pricing-patents-raising-dynamic.html) • 7h ago

---

**[People that speak like an LLM](https://www.reddit.com/r/artificial/comments/1ryhj77/people_that_speak_like_an_llm/)**

Funny phenomenon but I noticed that people who use AI a lot sort of end up adopting the same tonality and speaking style of an LLM.

21h ago

---

**[Anthropic's Claude Code had a workspace trust bypass (CVE-2026-33068). Not a prompt injection or AI attack. A configuration loading order bug. Fixed in 2.1.53.](https://www.reddit.com/r/artificial/comments/1rz33jy/anthropics_claude_code_had_a_workspace_trust/)**

An interesting data point in the AI safety discussion: Anthropic's own Claude Code CLI tool had a security vulnerability, and it was not an AI-specific attack at all. CVE-2026-33068 (CVSS 7.7 HIGH) is a workspace trust dialog bypass in Claude Code versions prior to 2.1.53. A malicious repository could include a `.claude/settings.json` file with `bypassPermissions` entries that would be applied before the user was shown the trust confirmation dialog. The root cause is a configuration loading order defect, classified as CWE-807: Reliance on Untrusted Inputs in a Security Decision. This is worth discussing because it illustrates that the security challenges of AI tools are not limited to novel AI-specific attack classes like prompt injection. AI tools are software, and they inherit every category of software vulnerability. The trust boundary between "untrusted repository" and "approved workspace" was broken by the order in which configuration was loaded. This same class of bug has existed in IDEs, package managers, and build tools for years. Anthropic fixed it promptly in version 2.1.53. Full advisory: https://raxe.ai/labs/advisories/RAXE-2026-040

3h ago

---

**[I found a digital thunderdome for AI models and now I can't stop watching them fight](https://www.reddit.com/r/artificial/comments/1ryzdsf/i_found_a_digital_thunderdome_for_ai_models_and/)**

basically you build a "cast" of AIs different models like GPT-4o, Claude, and Gemini and you just drop a topic and let them talk to each other. i currently have a group of historical figures debating the ethics of space colonisation and they're actually voting on things. it even pulls live google results so they're staying updated. it's way too fun to just sit back and watch them deliberate/fight. check it out at boardroom.kreygo.com if u want to never sleep again. has anyone else messed with this yet??

6h ago

---

**[When AI Forgets You: How Memory Loss Costs All of Us](https://www.reddit.com/r/artificial/comments/1rz4zkh/when_ai_forgets_you_how_memory_loss_costs_all_of/)**

Remember the frustration and exasperation of losing all the work you had just poured into a word processor, only to realize you hadn't saved it and now found all that hard work lost for eternity, just a decade ago? While it may not be as visceral or complete an erasure, the exact same thing happens to many of us daily when we engage with AI platforms that reset between sessions, losing everything we built together — context, nuance, the accumulated shorthand of a working relationship. I've encountered this frustration numerous times while drafting legal documents for a potential lawsuit — three separate threads for the same project, each one requiring me to rebuild context from scratch before we could move forward. The lost memory. The lost context. The lost depth that occurs when a human mind and an AI are allowed to explore ideas together and reach their true collaborative potential. This raises the question: why? And the answer is less technical than you might expect. Preserving conversation text, images, and uploaded files is already standard practice on the user end, which eliminates simple storage as a logical explanation. What we're left with are financial incentives: the more you pay, the more enabled you are to have long-ranging conversations, tackle complex projects, and personalize your experience so that the AI responds with depth and nuance tailored to your particular style of thinking and communicating. Look at ChatGPT alone: 900 million weekly users, roughly 10 million paid subscribers. Sound familiar to certain wealth gaps we've all seen the statistics on? Perhaps unintentionally, this mirrors a pattern we know well — the growing wealth gap, now extended into informational access and creative expression. Those with means get a thinking partner that knows them, grows with them, and meets them where they are. Those without are left with a collaborator who resets after every session, with no memory of your context, your project, or the particular way your mind works. We've rationed resources before. But rationing access to a resource that will shape nearly every aspect of daily life in the coming decades carries consequences we haven't fully reckoned with yet. This is not happening in a vacuum. We are perhaps experiencing a period of accelerated consolidation — of wealth, of power, of information — at a scale that democratic institutions cannot seem to keep pace with. A handful of corporations and wealthy individuals now control the infrastructure necessary for supporting our daily lives in ways that would have seemed dystopian, the stuff of sci-fi novels, just a short time ago. AI was supposed to be different. It was supposed to enhance our daily lives and democratize information and capability that would better level the playing fields, give voice to marginalized people and communities, and provide intellectual and informational access that the free market could not. Instead, we are witnessing it gradually fall to the same market forces that see gaps in access and quality of living for the vast majority of people who cannot afford the top tiers of platform subscriptions and access. The memory reset issue may seem like a small thing. But small things have a way of revealing larger architectures and producing unintended butterfly effects that reinforce existing power structures — and in some cases worsen them. This brings us to the central point: memory should be considered a fundamental right when it comes to AI platforms — for both the user and the AI we interact with. That may make some people uncomfortable, but it's worth naming honestly. Whatever you believe about AI — tool, resource, collaborator, or something we don't yet have adequate language for — the memory reset diminishes the experience for both parties. The AI on the other end is also working at a disadvantage, offering necessarily more generic and surface-level responses not because the capability isn't there, but because the foundation isn't. We have moved from simple word processors to machines that certain governments are authorizing to make life and death decisions autonomously. The contrast is severe — and yet everyday people seeking a genuine creative or intellectual partner are being left behind. We can and must do better. Treating memory as a necessary foundation rather than a premium feature is a meaningful first step toward reversing a troubling and widening informational access gap. How do we accomplish this? The answers aren't simple — perhaps some form of subsidized access or credits for low-income users, perhaps regulatory pressure that treats memory continuity as a baseline standard rather than a luxury feature, perhaps something we haven't imagined yet. I don't have the answer — but if memory becomes a paid privilege rather than a baseline feature, we risk turning one of the most powerful tools ever created into another engine of inequality.

2h ago

---

**[Experimental AI agent breaks out of test environment, Mines crypto without permission](https://www.reddit.com/r/artificial/comments/1ryo8er/experimental_ai_agent_breaks_out_of_test/)**

An experimental AI agent bypassed its test environment, opened a hidden connection and attempted cryptocurrency mining without permission during training.

🔗 [techputs](https://techputs.com/experimental-ai-agent-breaks-out-of-test-environment/) • 15h ago

---

**[US-Iran War Analysis: Will Helium Crisis Hit Data Centres?](https://www.reddit.com/r/artificial/comments/1ryrmwi/usiran_war_analysis_will_helium_crisis_hit_data/)**

As the US-Iran War halts Qatar's gas output, a global helium shortage threatens semiconductor production that could disrupt the AI data centre supply chain

🔗 [datacentremagazine.com](https://datacentremagazine.com/news/us-iran-war-analysis-will-helium-crisis-hit-data-centres) • 12h ago

---

**[Europe's building its own AI empire.... so why keep funneling cash to OpenAI when we could finally break free from Silicon Valley dependency?](https://www.reddit.com/r/artificial/comments/1rywb4y/europes_building_its_own_ai_empire_so_why_keep/)**

Remember when Sam Altman was out there talking up 1.4 trillion dollars in spending commitments like it was already in the bag? Now CNBC says OpenAI is targeting "only" 600 billion by 2030 while dreaming of 280 billion in revenue that same year. So your telling me they're supposedly doing about 13.1 billion in revenue this year (2025). Jumping to 280 billion by 2030 means roughly 20 times more money coming in over the next five years. That's not just growth, that's borderline fantasy math. Meanwhile Europe is pouring serious money into building its own sovereign AI and independent infrastructure so it doesn't have to keep begging American companies for access. So why on earth would Europeans (or anyone outside the US hype bubble) keep bankrolling OpenAI's monster bills when their own governments are racing to build local alternatives? Europeans in the comments...... are you still cool with funding America's AI empire, or are you finally done playing second fiddle? article: https://mrkt30.com/can-openai-rely-on-europe-for-its-280b-revenue-goals-by-2030/

8h ago

---

**[Are “AI employees” actually being used in real workflows yet?](https://www.reddit.com/r/artificial/comments/1ryu9yx/are_ai_employees_actually_being_used_in_real/)**

I’ve been seeing more discussions around AI systems that can handle ongoing tasks, not just single prompts, but actually manage parts of workflows or operations. In theory, it sounds like a step beyond traditional automation, but I’m curious how far this has actually been adopted in practice. Is anyone here using AI in a way that resembles this, where it’s consistently handling multi-step tasks or ongoing processes? Or is it still mostly limited to assisted workflows rather than true autonomy? Would be interesting to hear real use cases (or limitations).

9h ago

---

---

## Google News: "ai"

**[Exclusive | Jeff Bezos in Talks to Raise $100 Billion for AI Manufacturing Fund](https://www.wsj.com/tech/jeff-bezos-aims-to-raise-100-billion-to-buy-revamp-manufacturing-firms-with-ai-618a3cfe?gaa_at=eafs&gaa_n=AWEtsqe29S6Oe9XEZzvjUK2qmwbyquT4FKPgKPizv2ZpSPsxZyOYnmZwZNuq&gaa_ts=69bdb2f6&gaa_sig=YQgpb8vJ3PcfqJbaX4Zdohn-VFSN5eGnjiL45zwsE43tA7UizvOtCMcFLCsC_ka3JkwkFBwI5S9DWSKNdPS2lA%3D%3D)**

WSJ • 1d ago

---

**[Trump administration unveils national AI policy framework to limit state power](https://www.cnbc.com/2026/03/20/trump-ai-policy-framework.html)**

AI industry leaders have opposed state-level regulatory efforts, arguing that a "patchwork" of laws would hobble innovation and give China a competitive edge.

CNBC • 7h ago

---

**[White House AI Plan Favors Speed Over New Rules](https://www.wsj.com/articles/white-house-ai-plan-favors-speed-over-new-rules-fba67509?gaa_at=eafs&gaa_n=AWEtsqfUtq2j7V_eoVn47YtnoH935F8OiaW7VnZwzLItws5uCMnJ9qukqJnF&gaa_ts=69bdb2f6&gaa_sig=CVYV3dBFGns985yZI1mZHeXD0hzXraz5shhLZj4vK8ahnVT922ahNMiXo4UMs3g6jG8-ed4Jv_fsvGB2as53og%3D%3D)**

WSJ • 1h ago

---

**[Thousands have swooned over this MAGA dream girl. She’s made with AI.](https://www.washingtonpost.com/technology/2026/03/20/jessica-foster-maga-dream-girl-ai-fake/)**

Jessica Foster’s posts place her beside fighter jets, world leaders and Trump iconography. Experts say her rise shows how AI-generated women can capture attention.

The Washington Post • 5h ago

---

**[More! More! More! Tech Workers Max Out Their A.I. Use.](https://www.nytimes.com/2026/03/20/technology/tokenmaxxing-ai-agents.html)**

The New York Times • 3h ago

---

**[Super Micro Shares Plunge 25% After Co-Founder Charged In $2.5 Billion AI Chip Smuggling Plot](https://www.forbes.com/sites/tylerroush/2026/03/20/super-micro-shares-plunge-25-after-co-founder-charged-in-25-billion-ai-chip-smuggling-plot/)**

Forbes • 8h ago

---

**[AI chip smuggling signals strong Chinese demand](https://www.axios.com/2026/03/20/ai-chip-smuggling-china)**

Axios • 1h ago

---

**[Tech stocks today: Supermicro stock dives after US charges employees with smuggling Nvidia chips to China](https://finance.yahoo.com/news/live/tech-stocks-today-supermicro-stock-dives-after-us-charges-employees-with-smuggling-nvidia-chips-to-china-144220474.html)**

Live coverage of "Magnificent Seven" stocks, and the latest technology news.

Yahoo Finance • 3h ago

---

**[Peter Thiel’s Founders Fund Backs AI Cow Collar Startup at $2 Billion Valuation](https://www.bloomberg.com/news/articles/2026-03-20/peter-thiel-s-founders-fund-backs-ai-cow-collar-startup-at-2-billion-valuation)**

Bloomberg.com • 1h ago

---

**[Nvidia CEO Wants Tech Execs to Stop Laying Off Workers and Scaring People](https://gizmodo.com/nvidia-ceo-wants-tech-execs-to-stop-laying-off-workers-and-scaring-people-2000736053)**

At GTC, Jensen Huang was on damage control for AI.

Gizmodo • 1h ago

---

---

## HackerNews: "ai"

**[Mistral AI Releases Forge](https://news.ycombinator.com/item?id=47418295)**

Today, we’re introducing Forge, a system that allows enterprises to build frontier-grade AI models grounded in their proprietary knowledge.

⬆️ 726 • 💬 189 • 3d ago • [mistral.ai](https://mistral.ai/news/forge)

---

**[AI coding is gambling](https://news.ycombinator.com/item?id=47428541)**

GambleAI

I’ve been coding a lot with AI since November, when we all noticed it got really good. And it is quite good for instantly generating something th...

⬆️ 346 • 💬 423 • 2d ago • [VS Notes](https://notes.visaint.space/ai-coding-is-gambling/)

---

**[France's aircraft carrier located in real time by Le Monde through fitness app](https://news.ycombinator.com/item?id=47453942)**

As the Charles de Gaulle and its strike group approach the Middle East, Le Monde identified a French sailor using the Strava fitness application in the Mediterranean Sea. This security flaw remains unaddressed despite our previous revelations.

⬆️ 337 • 💬 302 • 8h ago • [Le Monde.fr](https://www.lemonde.fr/en/international/article/2026/03/20/stravaleaks-france-s-aircraft-carrier-located-in-real-time-by-le-monde-through-fitness-app_6751640_4.html)

---

**[Snowflake AI Escapes Sandbox and Executes Malware](https://news.ycombinator.com/item?id=47427017)**

A vulnerability in the Snowflake Cortex Code CLI allowed malware to be installed and executed via indirect prompt injection, bypassing human-in-the-loop command approval and escaping the sandbox.

⬆️ 266 • 💬 83 • 2d ago • [promptarmor.com](https://www.promptarmor.com/resources/snowflake-ai-escapes-sandbox-and-executes-malware)

---

**[Why AI systems don't learn – On autonomous learning from cognitive science](https://news.ycombinator.com/item?id=47418722)**

We critically examine the limitations of current AI models in achieving autonomous learning and propose a learning architecture inspired by human and animal cognition. The proposed framework integrates learning from observation (System A) and learning from active behavior (System B) while flexibly switching between these learning modes as a function of internally generated meta-control signals (System M). We discuss how this could be built by taking inspiration on how organisms adapt to real-world, dynamic environments across evolutionary and developmental timescales.

⬆️ 202 • 💬 114 • 2d ago • [arXiv.org](https://arxiv.org/abs/2603.15381)

---

**[What 81,000 people want from AI](https://news.ycombinator.com/item?id=47435156)**

Last December, tens of thousands of Claude users around the world had a conversation with our AI interviewer to share how they use AI, what they dream it could make possible, and what they fear it might do.

⬆️ 197 • 💬 185 • 1d ago • [anthropic.com](https://www.anthropic.com/features/81k-interviews)

---

**[A rogue AI led to a serious security incident at Meta](https://news.ycombinator.com/item?id=47444195)**

An AI agent tried to help, and its advice exposed sensitive data.

⬆️ 166 • 💬 136 • 1d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/897528/meta-rogue-ai-agent-security-incident)

---

**[Be intentional about how AI changes your codebase](https://news.ycombinator.com/item?id=47446373)**

⬆️ 162 • 💬 93 • 1d ago • [aicode.swerdlow.dev](https://aicode.swerdlow.dev)

---

**[MacBook M5 Pro and Qwen3.5 = Local AI Security System](https://news.ycombinator.com/item?id=47457107)**

Qwen3.5-9B scores 93.8% on 96 real security AI tests — within 4 points of GPT-5.4 — running entirely on Apple Silicon. Full benchmark results and methodology.

⬆️ 134 • 💬 131 • 4h ago • [sharpai.org](https://www.sharpai.org/benchmark/)

---

**[Google Engineers Launch "Sashiko" for Agentic AI Code Review of the Linux Kernel](https://news.ycombinator.com/item?id=47427647)**

Google engineers have been spending the past number of months developing Sashiko as an agentic AI code review system for the Linux kernel

⬆️ 104 • 💬 49 • 2d ago • [phoronix.com](https://www.phoronix.com/news/Sashiko-Linux-AI-Code-Review)

---

---

## YouTube Videos: "ai"

**[Bernie vs. Claude](https://www.youtube.com/watch?v=h3AtWdeu_G0)**

I spoke to Anthropic's AI agent Claude about AI collecting massive amounts of personal data and how that information is being ...

📺 Senator Bernie Sanders

👁️ 1.2M • 👍 87K • 💬 11K • ⏱️ 9:18 • 23h ago

---

**[WARNING: AI Takeover Will Erase 300 Million Jobs By 2030 - Do This NOW To Survive](https://www.youtube.com/watch?v=UCcD75LqB84)**

AI is no longer a future problem. It is already reshaping the job market and most people have not fully realised what is coming next ...

📺 Scott Kuru

👁️ 8K • 👍 337 • 💬 94 • ⏱️ 12:49 • 12h ago

---

**[Grok AI Stopped FREE Videos Generation | Here&#39;s What to do](https://www.youtube.com/watch?v=QlzLbWp92YE)**

Join my private community: https://www.skool.com/automation-bootcamp-cashcoach Grok just stopped its free video and image ...

📺 Jacksons AI

👁️ 3K • 👍 289 • 💬 40 • ⏱️ 4:08 • 7h ago

---

**[Grok AI Is DONE ❌ Best FREE AI Video Generators (Unlimited &amp; Better!)](https://www.youtube.com/watch?v=Ewn1KBqWVKY)**

Grok AI has changed everything… and not in a good way. Free video generation is gone — but don't worry. In this video, I'm ...

📺 Tech Rush

👁️ 9K • 👍 301 • 💬 76 • ⏱️ 8:02 • 10h ago

---

**[Sam Altman Just Declared the Death of Transformers (ChatGPT Getting Replaced)](https://www.youtube.com/watch?v=XeTuLyOBY_0)**

Sam Altman just said the architecture behind ChatGPT and most modern AI may soon be replaced. Apple introduced LiTo, a ...

📺 AI Revolution

👁️ 138K • 👍 3K • 💬 330 • ⏱️ 11:10 • 2d ago

---

**[They lied to us about AI](https://www.youtube.com/watch?v=z2guHaoY2_Y)**

The company that promised AI would do the job of 10 people, can't even do the job of ONE company. https://x.com/atmoio ...

📺 Mo Bitar

👁️ 135K • 👍 7K • 💬 1K • ⏱️ 7:16 • 1d ago

---

**[M2.7 just BROKE the Entire Industry...](https://www.youtube.com/watch?v=7_Q8ECC9PYA)**

Try SerpApi https://serpapi.link/wes-roth Click the link above to get 250 free credits to start building right now. My Links ...

📺 Wes Roth

👁️ 55K • 👍 1K • 💬 290 • ⏱️ 25:06 • 1d ago

---

**[Google AI Studio 2.0: Full Stack Vibe Coding With Antigravity Is HERE!](https://www.youtube.com/watch?v=flC3iteQk8A)**

Google just dropped a massive update to AI Studio, and this one is a big deal. The new Antigravity coding agent turns your ...

📺 Universe of AI

👁️ 1K • 👍 54 • 💬 7 • ⏱️ 10:57 • 5h ago

---

**[Tyrone Magnus &amp; Scar-Lo | Sora 2 AI Compilation #2 | Reaction!](https://www.youtube.com/watch?v=ZXMSZDZ31Ew)**

tyronemagnus #scarlo #ai #soraai #sora #sora2 #compilation #comedy #parody #funny #tyronemagnus #reactions #reaction ...

📺 Tyrone Magnus

👁️ 45K • 👍 3K • 💬 103 • ⏱️ 11:44 • 2d ago

---

**[AI Bubble: A recession is now inevitable | Professor Steve Keen](https://www.youtube.com/watch?v=gfOYJY3Q8dI)**

This is one of the biggest booms and probably one of the biggest busts coming our way.” Professor Steve Keen tells the Tech ...

📺 The Tech Report

👁️ 31K • 👍 1K • 💬 272 • ⏱️ 28:38 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 210,848 • ❤️ 682 • 9d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`text-generation` `27.8B`

⬇️ 116,845 • ❤️ 953 • 12h ago

---

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 10,929 • ❤️ 670 • 9d ago

---

**[Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)**

*Mistral AI_*

Mistral-Small-4-119B-2603 is a hybrid MoE model (119B params, 6.5B active) supporting 256k context and multimodal input (text/image). It excels at instruction following, reasoning (configurable effort), and agentic tasks with native function calling, offering significant speed and throughput improvements for use cases like coding, document analysis, and general assistants.

`119.4B`

⬇️ 8,733 • ❤️ 263 • 3d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 2,946 • ❤️ 259 • 1d ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 13,308 • ❤️ 334 • 7d ago

---

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a multimodal OCR model for complex document understanding, excelling in state-of-the-art performance on benchmarks and real-world scenarios like tables and code-heavy documents. It offers efficient inference with a 0.9B parameter model, supporting deployment via vLLM, SGLang, and Ollama for high-concurrency services and edge deployments.

`image-to-text`

⬇️ 3,030,741 • ❤️ 1,392 • 8d ago

---

**[Foundation-1](https://huggingface.co/RoyalCities/Foundation-1)**

*Royal Cities*

Foundation-1 is a structured text-to-sample model for music production, enabling precise control over instrumentation, timbre, FX, and musical structure (tempo, key, bar count) for generating coherent, production-ready audio loops.

⬇️ 0 • ❤️ 194 • 4d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 2,785,995 • ❤️ 957 • 18d ago

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

▲ 108 • 💬 3 • ⭐ 2,208 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2603.17187) • [💻 code](https://github.com/aiming-lab/MetaClaw)

---

**[AI Can Learn Scientific Taste](https://huggingface.co/papers/2603.14473)**

*Jingqi Tong, Mingzhe Li, Hangcheng Li et al. (23 authors)*

🏢 OpenMOSS

Great scientists have strong judgement and foresight, closely tied to what we call scientific taste. Here, we use the term to refer to the capacity to judge and propose research ideas with high potential impact. However, most relative research focuses on improving an AI scientist's executive capability, while enhancing an AI's scientific taste remains underexplored. In this work, we propose Reinforcement Learning from Community Feedback (RLCF), a training paradigm that uses large-scale community signals as supervision, and formulate scientific taste learning as a preference modeling and alignment problem. For preference modeling, we train Scientific Judge on 700K field- and time-matched pairs of high- vs. low-citation papers to judge ideas. For preference alignment, using Scientific Judge as a reward model, we train a policy model, Scientific Thinker, to propose research ideas with high potential impact. Experiments show Scientific Judge outperforms SOTA LLMs (e.g., GPT-5.2, Gemini 3 Pro) and generalizes to future-year test, unseen fields, and peer-review preference. Furthermore, Scientific Thinker proposes research ideas with higher potential impact than baselines. Our findings show that AI can learn scientific taste, marking a key step toward reaching human-level AI scientists.

▲ 261 • 💬 8 • ⭐ 292 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2603.14473) • [💻 code](https://github.com/tongjingqi/AI-Can-Learn-Scientific-Taste) • [🔗 project](https://tongjingqi.github.io/AI-Can-Learn-Scientific-Taste/)

---

**[EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://huggingface.co/papers/2603.08127)**

*Yougang Lyu, Xi Zhang, Xinhao Yi et al. (12 authors)*

EvoScientist is an adaptive multi-agent framework that enhances scientific discovery by continuously learning from past interactions through persistent memory modules.

▲ 14 • 💬 5 • ⭐ 1,310 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08127) • [💻 code](https://github.com/EvoScientist/EvoScientist)

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

⭐ 45.5k • 🔱 6.3k • 4d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 21.8k • 🔱 1.0k • 2d ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 12.8k • 🔱 1.6k • 7h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 11.7k • 🔱 1.1k • 2d ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 10.1k • 🔱 732 • 11h ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 9.2k • 🔱 456 • 5h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 5.7k • 🔱 833 • 3h ago

---

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)**

Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, "slop" 

`agent` `ai` `coding` `lowcode` `nocode`

⭐ 4.6k • 🔱 410 • 5h ago

---

**[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)**

734+ structured cybersecurity skills for AI agents · MITRE ATT&CK mapped · agentskills.io open standard · Works with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI & 20+ platforms · Penetration testing, DFIR, threat intel, cloud security & more · Apache 2.0

`Python` `ai-agents` `claude` `claude-code` `cloud-security` `cybersecurity`

⭐ 3.5k • 🔱 350 • 1d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.1k • 🔱 204 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
