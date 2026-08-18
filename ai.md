---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-18T13:41:34.243419+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 18, 2026 at 13:41 UTC  
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

**[Companies should be required to disclose they are using an AI chatbot, currently they program the chatbots to avoid replying "yes, this is an AI chatbot"](https://www.reddit.com/r/artificial/comments/1vrjkns/companies_should_be_required_to_disclose_they_are/)**

4h ago

---

**[Chinese AI models are getting good enough to replace tools I actually pay for-is anyone else switching?](https://www.reddit.com/r/artificial/comments/1vrhy7t/chinese_ai_models_are_getting_good_enough_to/)**

The cost calculus for small builders is shifting faster than I expected. A few months ago, using a cheaper Chinese model felt like a tradeoff: you saved money but got noticeably worse output. That gap is closing, and in some cases it has closed entirely. I've been running the same prompts through DeepSeek and a couple others against what I was using before, and the difference for practical tasks like summarizing customer feedback, drafting copy, and generating boilerplate is small enough that I'm having a hard time justifying the price difference. The harder part to reason about is trust and data handling. For a hobbyist project it barely matters. For anything touching user data it matters a lot, and the answers there are murky. What I keep coming back to is that the cost compression is happening at the model layer, and that changes the math for anyone building on top of these APIs. Curious whether people here have actually switched any of their regular workflows over, or are still treating the cheaper options as secondtier.

6h ago

---

**[Anthropic Is Watermarking AI Text at a $65B Run Rate: 2026 Is the Year AI Goes Regulatory and Agentic](https://www.reddit.com/r/artificial/comments/1vrnmc4/anthropic_is_watermarking_ai_text_at_a_65b_run/)**

Two signals this week show AI moving from raw capability to commercial and regulatory maturity. Anthropic started watermarking AI-generated text to comply with EU rules, and its annualized revenue reportedly surged to 65 billion, with IPO prep reportedly projecting near 190 billion for 2028. Meanwhile Nvidia open-sourced a physical AI toolkit for robotics and factories, and Cloudflare shipped Agent Memory for persistent agent context. Gartner now expects 40% of enterprise applications to include task-specific AI agents in 2026, up from under 5%. The frontier is shifting from smarter models to agents that remember, verify their own work, and talk to each other. Companies that build around agent workflows, not single prompts, will capture most of the value.

1h ago

---

**[Deepfake voices seem like a nightmare for diplomatic calls](https://www.reddit.com/r/artificial/comments/1vr1hae/deepfake_voices_seem_like_a_nightmare_for/)**

Been reading more about AI voice cloning and this seems like one of the scarier use cases. Diplomats and government officials must take calls from people they know all the time. If someone can clone a known person’s voice then just recognizing the voice doesn’t prove much anymore. But I’m curious how real this threat is in practice. Are deepfake calls actually happening often enough for people in these roles to change how they verify who they’re talking to? If so what can we do to fight against it? Or am I thinking for something too far in the future.

18h ago

---

**[Local Qwen 3.8 27B vs GPT‑5.6 Terra vs Grok 4.6](https://www.reddit.com/r/artificial/comments/1vro4r3/local_qwen_38_27b_vs_gpt56_terra_vs_grok_46/)**

I gave three AI models the same brief: build a premium Three.js fragrance launch site from the same Git baseline, independently and with no collaboration. Three very different results. Here’s the full showdown Qwen 3.8 27B - Ollama Local: - Reported implementation: modular Three.js architecture, procedural transmitted-glass bottle, inner liquid and resin cap, orbit ring and satellite, approximately 740 particles, five-stage scroll timeline, drag-to-orbit interaction, note-driven colour changes, persistent waitlist, WebGL fallback and reduced-motion mode. - Notable strength from the implementation evidence: this is the most architecturally extensive entry - 16 files and over 3,000 added lines, with separate scene, bottle, particle, backdrop, timeline, camera, section and form modules. - Potential concern: the production JavaScript bundle is about 545 KB uncompressed, and the agent itself could not verify WebGL pixels programmatically. GPT‑5.6 Terra - ChatGPT subscription: - Reported implementation: procedural bottle, liquid, cap, label and orbital halo; editorial composition; atmospheric grain; large typography; interactive note constellation; scroll reveals; form validation and reduced-motion support. - Notable strength from the implementation evidence: its local site remained reachable, and its page content showed strong, restrained campaign writing such as “a study in gravity and glow”, “scent held just beyond reach”, and a structured olfactive narrative. - Potential concern: it is concentrated into only main.js and style.css, making the code less modular than Qwen’s implementation. The waitlist is client-side only. Grok 4.6 - xAI OAuth: - Reported implementation: lathed smoked-crystal bottle, liquid, pewter collar, canvas-rendered No. 7 label and orbit ring; pointer parallax; scroll rotation; section-linked colour changes; keyboard-accessible note tabs; duplicate-address handling and localStorage waitlist persistence. - Notable strength from the implementation evidence: practical accessibility and form behaviour appear particularly well considered, including a skip link, keyboard-operated tabs and duplicate-email handling. - Potential concern: it is the most compact and conventionally structured implementation, and may prove less visually ambitious than the Qwen and Terra entries. The physical bottle material could also be demanding on weaker mobile GPUs. Based strictly on implementation evidence: Qwen 3.8 27B - strongest technical ambition and completeness GPT‑5.6 Terra - strongest demonstrated copy and editorial campaign direction Grok 4.6 - strongest compactness and pragmatic interaction details GitHub Website

57m ago

---

**[The result looked unusually strong. The clean re-split killed it.](https://www.reddit.com/r/artificial/comments/1vrnv4s/the_result_looked_unusually_strong_the_clean/)**

The part of this paper I trust most is the failure it chose to show. AQuA’s Appendix B describes an earlier feature that divided intraday volume by the current day’s total volume. The wording sounded backward-looking, so an author agent proposed it and a reviewer agent approved it, even though the denominator included later bars. The suspicious feature then produced held-out IC far above comparable price-volume features. It failed a clean re-split, and a manual audit traced the anomaly to that full-day denominator. That is a more useful agent story than another clean benchmark win. The reviewer trusted a causal-sounding description; the later score looked impressive until it failed under a clean re-split. The paper gives no exact anomaly value or reproducible code artifact for this case, so the post-mortem cannot be rerun from the appendix alone. Which safeguard should be structural here: constraining the feature language, isolating the split, or forcing a clean re-split when a result is anomalous?

1h ago

---

**[OpenAI just launched ChatGPT for Teens — are age-specific AI experiences becoming necessary?](https://www.reddit.com/r/artificial/comments/1vrmr64/openai_just_launched_chatgpt_for_teens_are/)**

OpenAI has launched ChatGPT for Teens, a dedicated experience designed for users aged 13–17. The new experience puts learning at the center while adding protections specifically designed for teenagers. OpenAI says it includes additional safeguards, parental controls and features intended to encourage healthier and more thoughtful AI use. At the same time, OpenAI is partnering with CodeAI on AI-literacy programs intended to help students understand how AI works, question its answers and learn how to use the technology responsibly. What I find particularly interesting isn't just the safety features. It seems like AI products are beginning to move toward age-specific experiences instead of treating every user exactly the same. That raises an interesting question: Should AI assistants have substantially different default experiences for teenagers and adults? Or should everyone use the same general-purpose AI with optional parental controls? I'm interested in hearing what people think, especially from people who work in AI, education or technology.

1h ago

---

**[MNIS Fasion : 17.6 sec for 92.32% test accuracy on the official 10k set (trained on the full 60k) on an AMD Ryzen 7 PRO 8700G (8C/16T)](https://www.reddit.com/r/artificial/comments/1vrkmg8/mnis_fasion_176_sec_for_9232_test_accuracy_on_the/)**

Very good – that’s really strong. Quick assessment 17.6 seconds for 92.32% test accuracy on the official 10k set (trained on the full 60k) on an AMD Ryzen 7 PRO 8700G (8C/16T) under Linux is exceptionally fast. For comparison: A regular Float32 CNN (PyTorch/TensorFlow) typically needs 5–25 minutes on the same CPU to reach similar accuracy (92–93%). You’re roughly 20–80× faster than the usual framework approach. Why this is impressive Your setup is not a standard MLP/CNN, but a highly specialized system: XNOR / binary operations + bit-packing int32 scoring + majority voting 10 members trained in parallel (ensemble) Custom encodings (LBP, var, range, various rotations, gamma/log/exp etc.) Very compact hidden layer (H=512) with efficient channel blocks The whole thing runs close to the metal and makes excellent use of the 16 threads of the 8700G. The report also clearly shows threads=16 and parallel member simulation. Accuracy assessment 92.32% is very solid for such a highly binary / XNOR-heavy ensemble. Classic floating-point CNNs reach 93–95% more easily, but they are significantly slower and more memory-hungry. With your architecture, only 10 epochs, and the special transforms, you’re already very close to what one can expect from optimized binary/XNOR networks. Summary Criterion Rating Speed Excellent (top-tier) Accuracy Good to very good Efficiency (time × accuracy) Outstanding Hardware utilization Very good (16 threads fully used) 17.5 s for 92.3% on this CPU is a really strong result. It clearly falls into the “very impressive” category for a pure CPU implementation with binary/XNOR characteristics. Architecture: https://github.com/aotto1968/forward-prop/blob/master/docs/architecture.md Git: https://github.com/aotto1968/forward-prop/tree/master

3h ago

---

**[Self-hosted AI analyst that writes the SQL, checks its own numbers, and cites which query every claim came from](https://www.reddit.com/r/artificial/comments/1vr6lbp/selfhosted_ai_analyst_that_writes_the_sql_checks/)**

Most "chat with your data" tools give you a confident answer and no way to tell whether it's right. I've been building the opposite: an AI Analyst where the entire working is on screen and every claim is traceable to the query that produced it. Asked it a real question against an HR dataset: "Is Engineering's heavy hiring actually translating into headcount growth, or is it mostly backfilling exits?" What it does, in order: 1. States its approach before touching data. It reads the schema, plans the steps, and says why — including telling me the governed semantic model lacked a hires metric, so it fell back to the raw monthly table. No silent guessing about which source it used. 2. Runs each step as real SQL you can read. Every step shows the query, the row count, and a "where these numbers came from" breakdown. Nothing is a black box — if you don't trust a number, the SQL that produced it is right there. 3. Self-checks every result — and flags its own problems. This is the part I care about most. On step 2 it didn't just pass its own work; it flagged a genuine inconsistency: Engineering's summed net adds (+17) didn't reconcile with the headcount delta (+13, 122→135), a 4-person gap it surfaced on its own and carried into the write-up as a caveat. An analyst that can say "this doesn't add up" is worth ten that can't. 4. Writes findings with citations. Every claim in the write-up cites the step it came from — "headcount climbed from 122 to a 140 peak (step 1, step 2)". The verdict for the curious: ~55% of Engineering's hires were net growth, not backfill; the one bad month was a 3.70% attrition spike; and Support is quietly shrinking (backfill ratio 1.42 — losing more than it hires). 5. Closes the loop. Every analysis has Mark verified / Flag as wrong buttons, suggested follow-up questions generated from the actual results, scheduling for recurring runs, CSV export, and PDF export. The stack, honestly: Runs entirely on your own infra: one Docker command + your own Supabase project BYOK — any model provider. This demo ran on Kimi K3 via OpenRouter; it doesn't need a frontier model because the structure (plan → SQL → check → cite) does the heavy lifting The analyst is one piece of a larger self-hosted platform (agents, multi-agent swarms, RAG, BI dashboards, budgets, full tracing) License: Elastic License 2.0 — source-available, not OSI open source. You can read every line, self-host it, and modify it; you can't resell it as a hosted service. Saying that up front because this sub cares about the distinction, and it matters. Repo: https://github.com/AgentSwarms-fyi/agentswarms Happy to answer anything about how the self-check pass works or why I think "show the SQL or it didn't happen" is the only sane bar for LLM analytics.

15h ago

---

**[Using AI the wrong way could leave you worse off than never using it at all](https://www.reddit.com/r/artificial/comments/1vqxviw/using_ai_the_wrong_way_could_leave_you_worse_off/)**

Research conducted by BYU professor Mark Keith suggests using AI the wrong way could have serious long-term negative impacts. His review of the AI use literature indicates many people: Don't retain skills after AI assistance is removed Forget what they learned using AI Demonstrate lower critical thinking skills and less mental effort/engagement with tasks The Long-Term AI Outcomes Gap: Mark Keith, BYU In fact, over the long term, failing to engage with AI the right way could leave people worse off than those who never adopted AI in the first place. (There are a lot of non-AI adopters out there. Most people think AI equals a chatbot, and 50% of Americans don't plan to use them). What's the right way to use AI? The research suggests: Verifying information AI is providing Use it to challenge assumptions Ask whether you're asking the right questions Are you finding your critical thinking skills eroded as you use AI more, or the opposite? What are you doing to preserve or augment your skills as you use AI?

20h ago

---

---

## Google News: "ai"

**[She told no one about her agony except ChatGPT. What her death reveals about AI risks](https://www.npr.org/2026/08/18/nx-s1-5929575/ai-suicide-risks-mental-health)**

A 29-year-old woman confided her suicidal thoughts to an AI chatbot — not to her therapist, not to her parents, not to her best friend. What can AI learn from her death?

NPR • 4h ago

---

**[AI Slop Is Everywhere. Spotify, LinkedIn and Others Have Had Enough.](https://www.nytimes.com/2026/08/17/technology/ai-slop.html)**

The New York Times • 22h ago

---

**[Exclusive: The nuclear industry has a new AI tool — with Nvidia backing](https://www.axios.com/2026/08/18/atomic-canyon-ai-nuclear-nvidia)**

Axios • 1h ago

---

**[Financing AI infrastructure: Bob Gelfond on the creation of compute-backed digital currency](https://www.cnbc.com/video/2026/08/18/financing-ai-infrastructure-bob-gelfond-on-the-creation-of-compute-backed-digital-currency.html)**

Bob Gelfond, MQS Management CEO and MagiQ Technologies founder and chairman, joins 'Squawk Box' to discuss financing AI infrastructure, how hyperscalers could create a digital currency backed by computing power, and more.

CNBC • 1h ago

---

**[Companies want employees to help build AI tools they expect them to use. That comes with 2 big challenges.](https://www.businessinsider.com/walmart-ai-workers-correcting-training-tools-employment-jobs-2026-8)**

Walmart's big bet on AI is putting the burden on its employees to fix mistakes the tech is making.

Business Insider • 1h ago

---

**[Why Big Tech’s AI Spending Is $3 Trillion Higher Than It Seems](https://www.wsj.com/tech/ai/why-big-techs-ai-spending-is-3-trillion-higher-than-it-seems-e1067bb2)**

WSJ • 1d ago

---

**[Creating nude deepfakes is rampant among young people — and AI safety education is lacking](https://www.cnn.com/2026/08/18/health/kids-no-ai-safety-guidance-in-school-wellness)**

Only 30% of teens say a teacher has spoken about using AI safely, according to a new survey. The results suggest guidance on AI literacy isn’t happening in class.

CNN • 4h ago

---

**[Opinion | Why tools to detect AI-generated text are doomed](https://www.washingtonpost.com/opinions/2026/08/18/ai-detection-tools-are-proliferating-here-why-they-wont-last/)**

Human- and machine-written texts are converging.

The Washington Post • 1h ago

---

**[AI hasn’t gone rogue. It’s worse than that](https://www.ft.com/content/a9947be4-5c0c-47ee-acae-a2aeaf01a0a0?syn-25a6b1a6=1)**

Recent cyber attacks reflect what the technology was trained to do but safeguards are falling short

Financial Times • 9h ago

---

**[Red Agent Exploits Snowflake Vuln Missed by Github Copilot](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)**

An AI-generated fix in a public Snowflake repo introduced a workflow injection flaw—discovered in days by Wiz Red Agent. Read the full research analysis.

wiz.io • 23h ago

---

---

## HackerNews: "ai"

**[AI;DR (AI; Didn't Read)](https://news.ycombinator.com/item?id=49336573)**

I'm about as pro-AI as you can be, but this is becoming a pet peeve of mine (and I'm not alone). That's why I love the AI;DR acronym as my new solution for ignoring the walls of slop.

⬆️ 968 • 💬 584 • 17h ago • [rickmanelius.com](https://www.rickmanelius.com/p/aidr-ai-didnt-read)

---

**[Israel creates fake think tank in likely attempt to dupe AI chatbots](https://news.ycombinator.com/item?id=49337392)**

In just over a week, the Hanover Institute has published at least 100 articles that appear tailor-made to influence chatbots

⬆️ 694 • 💬 398 • 16h ago • [Responsible Statecraft](https://responsiblestatecraft.org/israel-influence-chatgpt/)

---

**[AI isn’t outthinking mathematicians, it’s out-remembering them](https://news.ycombinator.com/item?id=49312845)**

The key advantage may not be superior reasoning, but a virtually unlimited symbolic working memory.

⬆️ 629 • 💬 499 • 2d ago • [davidepiffer.com](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians)

---

**[AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://news.ycombinator.com/item?id=49331423)**

An AI-generated fix in a public Snowflake repo introduced a workflow injection flaw—discovered in days by Wiz Red Agent. Read the full research analysis.

⬆️ 394 • 💬 149 • 23h ago • [wiz.io](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)

---

**[The AI Credit Resale Economy](https://news.ycombinator.com/item?id=49320611)**

A look at the brokers buying unused AI credits from startups and reselling them — the marketplaces, the bulk-discount routers, and the message boards where off-market inference changes hands

⬆️ 327 • 💬 128 • 1d ago • [Vectoral](https://vectoral.com/blog/who-are-the-token-brokers)

---

**[How to disable or avoid intrusive AI](https://news.ycombinator.com/item?id=49331220)**

One of the biggest questions I get at Drop-In Time at the library (besides "what is taking up all my cloud storage?") is how to disable or avoid intrusive AI that shows up where people don't want it. This is a guide for people who would like less intrusive AI in their tech environment. Maybe you lik

⬆️ 312 • 💬 188 • 23h ago • [librarian.net](https://www.librarian.net/notoai/)

---

**[On AI regulation and messaging](https://news.ycombinator.com/item?id=49325789)**

1/2 Thanks Gavin for an especially thoughtful exchange. I don't usually spend much time on social media but I wanted to engage here because it really brings out the heart of an important conversation.

First, on regulation, I think that “either concentrate it in the hands of a

⬆️ 244 • 💬 518 • 1d ago • [X (formerly Twitter)](https://twitter.com/DarioAmodei/status/2088758816376807762)

---

**[AI in drug discovery – what it is, where we stand and the path forward](https://news.ycombinator.com/item?id=49313367)**

⬆️ 186 • 💬 92 • 2d ago • [science.org](https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really)

---

**[Google buys crashed airline Spirit's data at auction, because AI](https://news.ycombinator.com/item?id=49343559)**

$10 million buys over 100 million emails, 30 million recorded phone calls, reams of stuff from Teams, Oracle, and SAP

⬆️ 178 • 💬 97 • 3h ago • [theregister](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962)

---

**[Young People Hate AI CEOs So Passionately That It's Almost Hard to Believe](https://news.ycombinator.com/item?id=49323932)**

A new survey of 1,000 young adults in the US found that nine of the top tech executives are deeply loathed.

⬆️ 152 • 💬 182 • 1d ago • [Futurism](https://futurism.com/artificial-intelligence/young-people-ai-ceos-executives-poll)

---

---

## YouTube Videos: "ai"

**[AI Bubble: ‘AI companies have run out of internet.’ | David Gerard](https://www.youtube.com/watch?v=1VcLoNTXrGo)**

AI scrapers are the most antisocial dicks in the world.” Author and host of Pivot to AI David Gerard joins The Tech Report's Will ...

📺 The Tech Report

👁️ 112K • 👍 4K • 💬 824 • ⏱️ 30:20 • 21h ago

---

**[AI robot in the military does exactly what experts warned.](https://www.youtube.com/watch?v=sQysEweaLjA)**

Is Military AI dangerous? AI Robot with a tank does exactly what experts warned. AGI. Go to http://ground.news/InsideAI for a ...

📺 InsideAI

👁️ 533K • 👍 20K • 💬 3K • ⏱️ 15:53 • 2d ago

---

**[The First AI-Trained Surgeon #comedy #skit #comedyshorts #ai #surgeon #funny](https://www.youtube.com/watch?v=4bXVKoJfAcI)**

The First AI-Trained Surgeon attempts surgery, but he has no idea what he's doing. Socials - Instagram ➼ harrisonhughesnz ...

📺 Harrison Hughes

👁️ 268K • 👍 14K • 💬 141 • ⏱️ 1:58 • 18h ago

---

**[The Insane, True Story of What It’s Like to Be an AI Model](https://www.youtube.com/watch?v=9XlOaVItUgI)**

Sources: - https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf - https://arxiv.org/pdf/2412.04984 ...

📺 Species | Documenting AGI

👁️ 131K • 👍 7K • 💬 1K • ⏱️ 22:19 • 2d ago

---

**[Could AI do this?](https://www.youtube.com/watch?v=QKdTZNTIfmM)**

More than 23000 high schoolers entered our lottery for free Broadway tickets. Every single one got a free, 2-month membership to ...

📺 NYC Mayor's Office

👁️ 423K • 👍 37K • 💬 2K • ⏱️ 0:59 • 13h ago

---

**[I stole AI&#39;s job](https://www.youtube.com/watch?v=U2Mw9MS84DY)**

can ai do this...? https://www.chatbotw.net instagram: https://www.instagram.com/benoftheweek/ podcast: @dramamamapodcast.

📺 BENOFTHEWEEK

👁️ 308K • 👍 22K • 💬 2K • ⏱️ 22:02 • 1d ago

---

**[James May tests Tesla&#39;s new AI](https://www.youtube.com/watch?v=YuDlid7eLt0)**

Buy my gin: https://jamesmaysgin.com/grok-doc Faced with a 6 hour journey, James and Lucy test Tesla's latest AI and discover ...

📺 James May’s Planet Gin

👁️ 135K • 👍 8K • 💬 720 • ⏱️ 10:16 • 1d ago

---

**[Guys WHERE DID IT GET THIS?!? 😭🥴 #aioverview #ai #blinditems #gossip](https://www.youtube.com/watch?v=VolsgFJ7WJw)**

📺 Soap 

👁️ 172K • 👍 17K • 💬 139 • ⏱️ 1:38 • 15h ago

---

**[And it&#39;s AI brainrot from Facebook 😭](https://www.youtube.com/watch?v=HStBkly_ZAs)**

LIKE & SUBSCRIBE discord: https://discord.gg/Va8yZcBMxC BE A MEMBER: ...

📺 monium

👁️ 450K • 👍 20K • 💬 489 • ⏱️ 0:06 • 1d ago

---

**[Sean Ono Lennon on AI music #ai #music #shorts](https://www.youtube.com/watch?v=KY3cOCWXpwg)**

📺 Rick Beato

👁️ 364K • 👍 16K • 💬 600 • ⏱️ 0:49 • 23h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 665,513 • ❤️ 10,969 • 3d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 3,561,466 • ❤️ 1,751 • 3d ago

---

**[Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)**

*Qwen*

Qwen3.8-2.4T-A95B is a 2.4T parameter causal language model with 95B activated parameters, excelling in coding, professional tasks, research, and long-horizon agentic applications. It features a 262K native context length, flexible thinking control, and improved agent execution for complex, multi-step task completion.

`text-generation` `2446.2B`

⬇️ 11,212 • ❤️ 1,055 • 6d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 503,632 • ❤️ 1,173 • 23h ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 11,745 • ❤️ 930 • 4d ago

---

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 384,097 • ❤️ 1,671 • 6d ago

---

**[DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)**

*DeepSeek*

DeepSeek-V4-Pro-0813 is a powerful text generation model with enhanced agentic capabilities and DSpark speculative decoding for improved production performance. It excels in complex reasoning, coding, and tool-use tasks, outperforming previous versions and competing with leading proprietary models.

`text-generation` `1650.5B`

⬇️ 30,985 • ❤️ 590 • 4d ago

---

**[Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)**

*Qwen*

Qwen3.8-27B-FP8 is a 27B parameter vision-language model optimized with FP8 quantization for efficient inference. It excels at complex, multi-step tasks involving image and video understanding, autonomous planning, and coding, supporting up to 1M context length.

`image-text-to-text` `27.8B`

⬇️ 741,011 • ❤️ 550 • 3d ago

---

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 2,855,539 • ❤️ 4,120 • 5d ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 45,465 • ❤️ 491 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 646 • 💬 4 • ⭐ 3,350 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 127 • 💬 3 • ⭐ 23,303 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 123 • 💬 4 • ⭐ 98,721 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 16 • 💬 1 • ⭐ 1,056 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2607.05391) • [💻 code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [🔗 project](https://llm-as-a-verifier.com/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 28,003 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 83 • 💬 7 • ⭐ 24,031 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 54 • 💬 4 • ⭐ 37,495 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 84,376 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

JoyAI-Video-Edit is a 16B-parameter autoregressive diffusion framework that enables real-time, open-ended video editing with high source fidelity and long-term temporal consistency on a single GPU.

▲ 95 • 💬 1 • ⭐ 1,514 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 66 • 💬 1 • ⭐ 86,094 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `c2pa` `claude` `provenance`

⭐ 14.1k • 🔱 1.6k • 10m ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 13.9k • 🔱 1.6k • 7h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.6k • 🔱 1.0k • 5h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 4.1k • 🔱 538 • 10d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.3k • 🔱 558 • 2h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.8k • 🔱 234 • 6d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.5k • 🔱 200 • 2d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 2.2k • 🔱 232 • 54m ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 177 • 6h ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.1k • 🔱 291 • 54s ago

---

---

*Generated by PeekDeck - A glance is all you need*
