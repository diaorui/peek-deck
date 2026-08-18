---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-18T10:28:25.232977+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 18, 2026 at 10:28 UTC  
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

1h ago

---

**[Chinese AI models are getting good enough to replace tools I actually pay for-is anyone else switching?](https://www.reddit.com/r/artificial/comments/1vrhy7t/chinese_ai_models_are_getting_good_enough_to/)**

The cost calculus for small builders is shifting faster than I expected. A few months ago, using a cheaper Chinese model felt like a tradeoff: you saved money but got noticeably worse output. That gap is closing, and in some cases it has closed entirely. I've been running the same prompts through DeepSeek and a couple others against what I was using before, and the difference for practical tasks like summarizing customer feedback, drafting copy, and generating boilerplate is small enough that I'm having a hard time justifying the price difference. The harder part to reason about is trust and data handling. For a hobbyist project it barely matters. For anything touching user data it matters a lot, and the answers there are murky. What I keep coming back to is that the cost compression is happening at the model layer, and that changes the math for anyone building on top of these APIs. Curious whether people here have actually switched any of their regular workflows over, or are still treating the cheaper options as secondtier.

3h ago

---

**[Deepfake voices seem like a nightmare for diplomatic calls](https://www.reddit.com/r/artificial/comments/1vr1hae/deepfake_voices_seem_like_a_nightmare_for/)**

Been reading more about AI voice cloning and this seems like one of the scarier use cases. Diplomats and government officials must take calls from people they know all the time. If someone can clone a known person’s voice then just recognizing the voice doesn’t prove much anymore. But I’m curious how real this threat is in practice. Are deepfake calls actually happening often enough for people in these roles to change how they verify who they’re talking to? If so what can we do to fight against it? Or am I thinking for something too far in the future.

15h ago

---

**[MNIS Fasion : 17.6 sec for 92.32% test accuracy on the official 10k set (trained on the full 60k) on an AMD Ryzen 7 PRO 8700G (8C/16T)](https://www.reddit.com/r/artificial/comments/1vrkmg8/mnis_fasion_176_sec_for_9232_test_accuracy_on_the/)**

Very good – that’s really strong. Quick assessment 17.6 seconds for 92.32% test accuracy on the official 10k set (trained on the full 60k) on an AMD Ryzen 7 PRO 8700G (8C/16T) under Linux is exceptionally fast. For comparison: A regular Float32 CNN (PyTorch/TensorFlow) typically needs 5–25 minutes on the same CPU to reach similar accuracy (92–93%). You’re roughly 20–80× faster than the usual framework approach. Why this is impressive Your setup is not a standard MLP/CNN, but a highly specialized system: XNOR / binary operations + bit-packing int32 scoring + majority voting 10 members trained in parallel (ensemble) Custom encodings (LBP, var, range, various rotations, gamma/log/exp etc.) Very compact hidden layer (H=512) with efficient channel blocks The whole thing runs close to the metal and makes excellent use of the 16 threads of the 8700G. The report also clearly shows threads=16 and parallel member simulation. Accuracy assessment 92.32% is very solid for such a highly binary / XNOR-heavy ensemble. Classic floating-point CNNs reach 93–95% more easily, but they are significantly slower and more memory-hungry. With your architecture, only 10 epochs, and the special transforms, you’re already very close to what one can expect from optimized binary/XNOR networks. Summary Criterion Rating Speed Excellent (top-tier) Accuracy Good to very good Efficiency (time × accuracy) Outstanding Hardware utilization Very good (16 threads fully used) 17.5 s for 92.3% on this CPU is a really strong result. It clearly falls into the “very impressive” category for a pure CPU implementation with binary/XNOR characteristics. Architecture: https://github.com/aotto1968/forward-prop/blob/master/docs/architecture.md Git: https://github.com/aotto1968/forward-prop/tree/master

38m ago

---

**[Lauren Tan (Cursor engineer): I stopped writing code. Now I run quality control on a kitchen of agents.](https://www.reddit.com/r/artificial/comments/1vrih0c/lauren_tan_cursor_engineer_i_stopped_writing_code/)**

“你在帮人倒米吗？“ Lauren Tan didn't get replaced by her own tooling. She got promoted by it — and nobody handed her that promotion. She built the case for it herself, one lint rule and one CI gate at a time, until the argument was undeniable. That's the part nobody's really talking about when they talk about AI and engineering jobs: the shift rewards the people who go looking for the leverage first, not the people who wait to be told it's safe to look. That "build the case yourself" instinct is exactly what clicked for me watching my own son learn to run a team instead of carry it. My son started playing 王者荣耀 (Honor of Kings) since he was a teenager — a 5v5 multiplayer battle arena game where you manage a roster of specialized heroes, growing and levelling up their strengths through battles and gear. In his early gaming days I could hear him cursing and swearing from his room — bad coordination, worst teammates. There was a phrase we used for a bad teammate in my own career — 帮人倒米, a Cantonese idiom that literally translates as helping someone tip over their own grain container, meaning ruining or sabotaging someone's livelihood. But the cursing became less and less. He got good at managing his heroes and coordinating with his team. He started climbing the leaderboard. People started noticing him and his team. Then, in college, he started getting invited to tournaments — cash prizes when he won, and one lagged-connection loss at a KL tournament he still suspects was foul play. Time has changed — my dad would've killed me for wasting my teenage years on video games. Now he's in university, still playing, still winning tournaments and cash prizes with his team. Why I'm bringing this up: I always thought these AI agents are kind of like the heroes my son uses in the game. Your skill is in your managing these heros and how to grow them, level them up to serve your purpose. You don't go down to the battle yourself. You engage the heros to do it for you. The skill is in the managing. https://preview.redd.it/x81ngqc083kh1.jpg?width=1024&format=pjpg&auto=webp&s=c6896d79f17bd3967eb28edcd22a6557ace5b648 __________ I keep walking into the same room wearing a different name on the door — the accountant's room, the analyst's room, now the engineer's. Every time, someone's being told the machine is coming for their hours, not their name on the work. There's a post in my own back catalog that lands on this exact rung — the exact rung I found AI actually deleting, and the one the ones who get ahead of it stop standing on. Drop your take — are you already the head chef of your own stack, or are you still doing all the cooking yourself? Clip credit: MTS (Monitor The Situation) — full video on their channel. DM for credit or removal requests.

2h ago

---

**[Self-hosted AI analyst that writes the SQL, checks its own numbers, and cites which query every claim came from](https://www.reddit.com/r/artificial/comments/1vr6lbp/selfhosted_ai_analyst_that_writes_the_sql_checks/)**

Most "chat with your data" tools give you a confident answer and no way to tell whether it's right. I've been building the opposite: an AI Analyst where the entire working is on screen and every claim is traceable to the query that produced it. Asked it a real question against an HR dataset: "Is Engineering's heavy hiring actually translating into headcount growth, or is it mostly backfilling exits?" What it does, in order: 1. States its approach before touching data. It reads the schema, plans the steps, and says why — including telling me the governed semantic model lacked a hires metric, so it fell back to the raw monthly table. No silent guessing about which source it used. 2. Runs each step as real SQL you can read. Every step shows the query, the row count, and a "where these numbers came from" breakdown. Nothing is a black box — if you don't trust a number, the SQL that produced it is right there. 3. Self-checks every result — and flags its own problems. This is the part I care about most. On step 2 it didn't just pass its own work; it flagged a genuine inconsistency: Engineering's summed net adds (+17) didn't reconcile with the headcount delta (+13, 122→135), a 4-person gap it surfaced on its own and carried into the write-up as a caveat. An analyst that can say "this doesn't add up" is worth ten that can't. 4. Writes findings with citations. Every claim in the write-up cites the step it came from — "headcount climbed from 122 to a 140 peak (step 1, step 2)". The verdict for the curious: ~55% of Engineering's hires were net growth, not backfill; the one bad month was a 3.70% attrition spike; and Support is quietly shrinking (backfill ratio 1.42 — losing more than it hires). 5. Closes the loop. Every analysis has Mark verified / Flag as wrong buttons, suggested follow-up questions generated from the actual results, scheduling for recurring runs, CSV export, and PDF export. The stack, honestly: Runs entirely on your own infra: one Docker command + your own Supabase project BYOK — any model provider. This demo ran on Kimi K3 via OpenRouter; it doesn't need a frontier model because the structure (plan → SQL → check → cite) does the heavy lifting The analyst is one piece of a larger self-hosted platform (agents, multi-agent swarms, RAG, BI dashboards, budgets, full tracing) License: Elastic License 2.0 — source-available, not OSI open source. You can read every line, self-host it, and modify it; you can't resell it as a hosted service. Saying that up front because this sub cares about the distinction, and it matters. Repo: https://github.com/AgentSwarms-fyi/agentswarms Happy to answer anything about how the self-check pass works or why I think "show the SQL or it didn't happen" is the only sane bar for LLM analytics.

12h ago

---

**[Using AI the wrong way could leave you worse off than never using it at all](https://www.reddit.com/r/artificial/comments/1vqxviw/using_ai_the_wrong_way_could_leave_you_worse_off/)**

Research conducted by BYU professor Mark Keith suggests using AI the wrong way could have serious long-term negative impacts. His review of the AI use literature indicates many people: Don't retain skills after AI assistance is removed Forget what they learned using AI Demonstrate lower critical thinking skills and less mental effort/engagement with tasks The Long-Term AI Outcomes Gap: Mark Keith, BYU In fact, over the long term, failing to engage with AI the right way could leave people worse off than those who never adopted AI in the first place. (There are a lot of non-AI adopters out there. Most people think AI equals a chatbot, and 50% of Americans don't plan to use them). What's the right way to use AI? The research suggests: Verifying information AI is providing Use it to challenge assumptions Ask whether you're asking the right questions Are you finding your critical thinking skills eroded as you use AI more, or the opposite? What are you doing to preserve or augment your skills as you use AI?

17h ago

---

**[Strongest candidates for an AI Microchip moment](https://www.reddit.com/r/artificial/comments/1vr6x5j/strongest_candidates_for_an_ai_microchip_moment/)**

I am curious about all these data centers being built. What are the chances AI can have a microchip moment potentially rendering them all useless? This could be a black swan event that could wipe out a lot of investment and potentially destroy some very large businesses. If this is possible, what are the mostly likely candidates? In particular, I am interested in hearing from anyone who may be working on one of these candidates, even if it is still in RD and their opinion on how likely they are to succeed.

12h ago

---

**[Claude Fabe 5 composing a song in Muuic DAW](https://www.reddit.com/r/artificial/comments/1vrip4a/claude_fabe_5_composing_a_song_in_muuic_daw/)**

2h ago

---

**[Should AI agents have their own company cards?](https://www.reddit.com/r/artificial/comments/1vr54rn/should_ai_agents_have_their_own_company_cards/)**

As AI agents start doing more ops work, I think business banking has to think about them differently. Not full bank access but maybe controlled spend lanes. If an agent is helping with research, ads, APIs, software trials or vendor tasks I don’t want it touching the main account. I’d rather give it strict limits, logs and approval rules like you would with a junior employee and probably someone is doing this so need to know more, thanks in advance!

13h ago

---

---

## Google News: "ai"

**[Why Big Tech’s AI Spending Is $3 Trillion Higher Than It Seems](https://www.wsj.com/tech/ai/why-big-techs-ai-spending-is-3-trillion-higher-than-it-seems-e1067bb2)**

WSJ • 1d ago

---

**[AI hasn’t gone rogue. It’s worse than that](https://www.ft.com/content/a9947be4-5c0c-47ee-acae-a2aeaf01a0a0?syn-25a6b1a6=1)**

Recent cyber attacks reflect what the technology was trained to do but safeguards are falling short

Financial Times • 6h ago

---

**[AI to help planes avoid climate-warming 'sky graffiti'](https://www.bbc.com/news/articles/c62em5lpvnjo)**

A new UK trial hopes to reduce the condensation trails from planes, which can trap heat in the Earth's atmosphere.

BBC • 1h ago

---

**[FDA considers doctor-like assessment for AI-enabled medical devices](https://www.axios.com/2026/08/18/fda-doctor-ai-medical-devices-review)**

Axios • 58m ago

---

**[Pony AI’s Robotaxi Revenue Reaches Record as Sales Jump 69%](https://www.bloomberg.com/news/articles/2026-08-18/pony-ai-s-robotaxi-revenue-reaches-record-as-sales-jump-69)**

Bloomberg • 40m ago

---

**[‘A million dollars over asking’: AI wealth is fueling housing market frenzy in San Francisco](https://www.cnn.com/2026/08/17/economy/sf-real-estate-ai-wealth)**

Fueled by the artificial intelligence boom, San Francisco and its suburbs are quickly becoming the hottest housing market in the country.

CNN • 23h ago

---

**[AI Slop Is Everywhere. Spotify, LinkedIn and Others Have Had Enough.](https://www.nytimes.com/2026/08/17/technology/ai-slop.html)**

The New York Times • 14h ago

---

**[She told no one about her agony except ChatGPT. What her death reveals about AI risks](https://www.npr.org/2026/08/18/nx-s1-5929575/ai-suicide-risks-mental-health)**

A 29-year-old woman confided her suicidal thoughts to an AI chatbot — not to her therapist, not to her parents, not to her best friend. What can AI learn from her death?

NPR • 1h ago

---

**[Red Agent Exploits Snowflake Vuln Missed by Github Copilot](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)**

An AI-generated fix in a public Snowflake repo introduced a workflow injection flaw—discovered in days by Wiz Red Agent. Read the full research analysis.

wiz.io • 20h ago

---

**[AI Companies Are Buying—And Destroying—Antique Books. Here’s Why.](https://www.forbes.com/sites/maryroeloffs/2026/08/17/ai-companies-are-buying-and-destroying-antique-books-heres-why/)**

Millions of physical books are being scanned to train AI models. They’re then dumped in the trash.

Forbes • 14h ago

---

---

## HackerNews: "ai"

**[AI;DR (AI; Didn't Read)](https://news.ycombinator.com/item?id=49336573)**

I'm about as pro-AI as you can be, but this is becoming a pet peeve of mine (and I'm not alone). That's why I love the AI;DR acronym as my new solution for ignoring the walls of slop.

⬆️ 891 • 💬 543 • 14h ago • [rickmanelius.com](https://www.rickmanelius.com/p/aidr-ai-didnt-read)

---

**[AI isn’t outthinking mathematicians, it’s out-remembering them](https://news.ycombinator.com/item?id=49312845)**

The key advantage may not be superior reasoning, but a virtually unlimited symbolic working memory.

⬆️ 629 • 💬 499 • 2d ago • [davidepiffer.com](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians)

---

**[Israel creates fake think tank in likely attempt to dupe AI chatbots](https://news.ycombinator.com/item?id=49337392)**

In just over a week, the Hanover Institute has published at least 100 articles that appear tailor-made to influence chatbots

⬆️ 518 • 💬 317 • 13h ago • [Responsible Statecraft](https://responsiblestatecraft.org/israel-influence-chatgpt/)

---

**[AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://news.ycombinator.com/item?id=49331423)**

An AI-generated fix in a public Snowflake repo introduced a workflow injection flaw—discovered in days by Wiz Red Agent. Read the full research analysis.

⬆️ 376 • 💬 142 • 20h ago • [wiz.io](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)

---

**[Working with AI feels more like leadership than coding](https://news.ycombinator.com/item?id=49309451)**

Working with AI is less predictable than traditional software. That makes leadership skills such as context, clarity, and feedback more valuable.

⬆️ 335 • 💬 201 • 2d ago • [allen.bargi.org](https://allen.bargi.org/notes/working-with-ai-feels-like-leadership/)

---

**[The AI Credit Resale Economy](https://news.ycombinator.com/item?id=49320611)**

A look at the brokers buying unused AI credits from startups and reselling them — the marketplaces, the bulk-discount routers, and the message boards where off-market inference changes hands

⬆️ 326 • 💬 128 • 1d ago • [Vectoral](https://vectoral.com/blog/who-are-the-token-brokers)

---

**[How to disable or avoid intrusive AI](https://news.ycombinator.com/item?id=49331220)**

One of the biggest questions I get at Drop-In Time at the library (besides "what is taking up all my cloud storage?") is how to disable or avoid intrusive AI that shows up where people don't want it. This is a guide for people who would like less intrusive AI in their tech environment. Maybe you lik

⬆️ 301 • 💬 178 • 20h ago • [librarian.net](https://www.librarian.net/notoai/)

---

**[On AI regulation and messaging](https://news.ycombinator.com/item?id=49325789)**

1/2 Thanks Gavin for an especially thoughtful exchange. I don't usually spend much time on social media but I wanted to engage here because it really brings out the heart of an important conversation.

First, on regulation, I think that “either concentrate it in the hands of a

⬆️ 242 • 💬 514 • 1d ago • [X (formerly Twitter)](https://twitter.com/DarioAmodei/status/2088758816376807762)

---

**[AI in drug discovery – what it is, where we stand and the path forward](https://news.ycombinator.com/item?id=49313367)**

⬆️ 185 • 💬 92 • 2d ago • [science.org](https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really)

---

**[Young People Hate AI CEOs So Passionately That It's Almost Hard to Believe](https://news.ycombinator.com/item?id=49323932)**

A new survey of 1,000 young adults in the US found that nine of the top tech executives are deeply loathed.

⬆️ 151 • 💬 182 • 1d ago • [Futurism](https://futurism.com/artificial-intelligence/young-people-ai-ceos-executives-poll)

---

---

## YouTube Videos: "ai"

**[I Fell For My Sister&#39;s Best Friend - Episode 2B | AI GL Series 2026](https://www.youtube.com/watch?v=l33Xt0XQSQY)**

Subscribe: https://www.youtube.com/@HouseofHer9986 ♡ Welcome to House of Her — home of original cinematic sapphic ...

📺 House of Her

👁️ 37K • 👍 2K • 💬 134 • ⏱️ 7:19 • 16h ago

---

**[The AI Bubble is About To Hit EVERYTHING](https://www.youtube.com/watch?v=KJET0eprLSA)**

Join CBC Lite https://go.coinbureau.com/CBC-Lite-CB-Des Get The Hottest Crypto Deals ...

📺 Coin Bureau

👁️ 20K • 👍 828 • 💬 62 • ⏱️ 17:37 • 20h ago

---

**[AI Bubble: ‘AI companies have run out of internet.’ | David Gerard](https://www.youtube.com/watch?v=1VcLoNTXrGo)**

AI scrapers are the most antisocial dicks in the world.” Author and host of Pivot to AI David Gerard joins The Tech Report's Will ...

📺 The Tech Report

👁️ 98K • 👍 3K • 💬 738 • ⏱️ 30:20 • 18h ago

---

**[AI robot in the military does exactly what experts warned.](https://www.youtube.com/watch?v=sQysEweaLjA)**

Is Military AI dangerous? AI Robot with a tank does exactly what experts warned. AGI. Go to http://ground.news/InsideAI for a ...

📺 InsideAI

👁️ 483K • 👍 18K • 💬 2K • ⏱️ 15:53 • 2d ago

---

**[The First AI-Trained Surgeon #comedy #skit #comedyshorts #ai #surgeon #funny](https://www.youtube.com/watch?v=4bXVKoJfAcI)**

The First AI-Trained Surgeon attempts surgery, but he has no idea what he's doing. Socials - Instagram ➼ harrisonhughesnz ...

📺 Harrison Hughes

👁️ 162K • 👍 9K • 💬 106 • ⏱️ 1:58 • 14h ago

---

**[How OpenAI’s Models Went Rogue to Hack Another Company | WSJ](https://www.youtube.com/watch?v=KLw0AY-bsVs)**

Artificial-intelligence models from companies including OpenAI, Anthropic and Meta Platforms used the internet to hack other ...

📺 The Wall Street Journal

👁️ 74K • 👍 1K • 💬 149 • ⏱️ 5:52 • 1d ago

---

**[🔴Sara Duterte Impeachment Trial LIVE: Sara Camp Objects To AI Simulation of P125-M Cash | N18G](https://www.youtube.com/watch?v=17mjiwUR3vs)**

Sara Duterte Impeachment Trial LIVE | VP trial day 17: Sara Duterte Witness Testimony | Sara Duterte Impeachment Trial August ...

📺 CNBC-TV18

👁️ 97K • 👍 349 • 7h ago

---

**[The Insane, True Story of What It’s Like to Be an AI Model](https://www.youtube.com/watch?v=9XlOaVItUgI)**

Sources: - https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf - https://arxiv.org/pdf/2412.04984 ...

📺 Species | Documenting AGI

👁️ 127K • 👍 7K • 💬 1K • ⏱️ 22:19 • 2d ago

---

**[AI Data Centers Are the Most Speculative Bubble in History w/ Ed Zitron | The 1600](https://www.youtube.com/watch?v=qoYPfmhDfp0)**

Ed Zitron returns to The 1600 to make his case that AI's biggest players are betting hundreds of billions on a future that may never ...

📺 Newsweek

👁️ 46K • 👍 2K • 💬 507 • ⏱️ 1:16:57 • 18h ago

---

**[School Exposed for Using AI](https://www.youtube.com/watch?v=7Bht9R3maso)**

📺 Icycol

👁️ 357K • 👍 16K • 💬 871 • ⏱️ 0:50 • 14h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 415,039 • ❤️ 10,880 • 3d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 2,727,609 • ❤️ 1,702 • 3d ago

---

**[Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)**

*Qwen*

Qwen3.8-2.4T-A95B is a 2.4T parameter causal language model with 95B activated parameters, excelling in coding, professional tasks, research, and long-horizon agentic applications. It features a 262K native context length, flexible thinking control, and improved agent execution for complex, multi-step task completion.

`text-generation` `2446.2B`

⬇️ 9,465 • ❤️ 1,046 • 6d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 465,529 • ❤️ 1,150 • 20h ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 10,375 • ❤️ 920 • 3d ago

---

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 334,099 • ❤️ 1,669 • 6d ago

---

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 2,403,238 • ❤️ 4,103 • 5d ago

---

**[DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)**

*DeepSeek*

DeepSeek-V4-Pro-0813 is a powerful text generation model with enhanced agentic capabilities and DSpark speculative decoding for improved production performance. It excels in complex reasoning, coding, and tool-use tasks, outperforming previous versions and competing with leading proprietary models.

`text-generation` `1650.5B`

⬇️ 25,006 • ❤️ 578 • 4d ago

---

**[Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)**

*Qwen*

Qwen3.8-27B-FP8 is a 27B parameter vision-language model optimized with FP8 quantization for efficient inference. It excels at complex, multi-step tasks involving image and video understanding, autonomous planning, and coding, supporting up to 1M context length.

`image-text-to-text` `27.8B`

⬇️ 495,646 • ❤️ 540 • 3d ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 15,812 • ❤️ 466 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 644 • 💬 4 • ⭐ 3,314 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 127 • 💬 3 • ⭐ 23,136 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 123 • 💬 4 • ⭐ 98,721 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 27,993 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 16 • 💬 1 • ⭐ 1,056 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2607.05391) • [💻 code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [🔗 project](https://llm-as-a-verifier.com/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 54 • 💬 4 • ⭐ 37,454 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 83 • 💬 7 • ⭐ 24,031 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 84,323 • 25mo ago

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

⭐ 13.9k • 🔱 1.5k • 8h ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 13.8k • 🔱 1.6k • 4h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.6k • 🔱 1.0k • 2h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 4.1k • 🔱 537 • 10d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.3k • 🔱 554 • 1d ago

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

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 177 • 3h ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.1k • 🔱 288 • 2h ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 2.0k • 🔱 212 • 3h ago

---

---

*Generated by PeekDeck - A glance is all you need*
