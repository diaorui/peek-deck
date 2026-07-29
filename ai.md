---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-29T09:37:32.250316+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 29, 2026 at 09:37 UTC  
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

**[1,178 employees of frontier AI companies have signed to "Pace the frontier AI development"](https://www.reddit.com/r/artificial/comments/1v9lrad/1178_employees_of_frontier_ai_companies_have/)**

Pacing the Frontier A statement from 1,178 employees of frontier AI companies https://www.pacingthefrontier.com/ What do you think about this? Share your views. I'm conflicted.

5h ago

---

**[AI Companies Are Buying Antique Books, Ingesting Their Contents to Train Models, and Then Destroying Them at Incredible Scale, Even If Almost No Copies Remain](https://www.reddit.com/r/artificial/comments/1v8ilsm/ai_companies_are_buying_antique_books_ingesting/)**

Source AI companies are literally destroying physical books to train their models. Using hydraulic cutting machines, they rip pages from used books, scan them with industrial equipment, and feed them into their AI systems. This practice, protected by the first-sale doctrine and fair use, has now become so widespread that book sellers are cashing in on the AI boom. Rare and out-of-print books are being pulped, raising serious ethical and cultural concerns about the cost of AI progress.

🔗 [Futurism](https://futurism.com/artificial-intelligence/ai-companies-destroying-rare-books) • 1d ago

---

**[How I made small local AI models stop breaking JSON - a grammar-based approach](https://www.reddit.com/r/artificial/comments/1v9r73b/how_i_made_small_local_ai_models_stop_breaking/)**

I wrote a post about a specific problem with running AI agents on local models: they're unreliable with structured output. You ask for JSON, they mostly deliver, but then they forget a closing brace, invent a tool name, or add a paragraph of text after the JSON object. Hosted APIs like OpenAI handle this server-side. Locally, you're on your own. My approach: llama.cpp supports GBNF grammars that constrain which tokens the model can produce. I wrote a compiler that turns each tool's schema into grammar rules, so the model's output is constrained at every token position. It literally cannot produce malformed JSON. Then I narrow the grammar per-turn so the model only sees the 3-5 tools that are relevant instead of all 50. The post is a deep dive with real code from the project (Eris, a local agent in Rust that uses your Markdown notes as memory, runs entirely on your machine). https://eris-system.dev/blog/gbnf-grammars Repo: https://github.com/janpauldahlke/eris (Apache 2.0) ps. i wanted to share how i solve the problem, it is related to my project, but not self advertisement.

5m ago

---

**[IS AI destroying companies and putting people out of jobs?](https://www.reddit.com/r/artificial/comments/1v9qla8/is_ai_destroying_companies_and_putting_people_out/)**

Let’s discuss this.

39m ago

---

**[~1,400 years ago, scholars built a rigorous system to verify who you can trust. I rebuilt it as a trust layer for AI agents.](https://www.reddit.com/r/artificial/comments/1v9qdpe/1400_years_ago_scholars_built_a_rigorous_system/)**

I wrote this and just put it on arXiv, sharing for the discussion. When statements spread through long chains of people — some reliable, some not — you can't trust a claim just because it sounds right. Islamic scholars faced this centuries ago and built one of history's most rigorous systems for verifying transmitted knowledge: every claim carries its full chain of transmitters (isnād), every transmitter is graded on integrity and precision (rijāl), the chain is only as strong as its weakest link, independent chains raise confidence, and even a flawless chain doesn't excuse a flawed message. Now look at AI in 2026. An answer passes through a scraper, an extractor, several models, a synthesizer. Some links are reliable, some aren't — and when they fail, they fail silently. A confident, fluent answer that's quietly wrong. Everyone is racing to verify the agent: its identity, its permissions, its access. Almost no one is verifying the claim: whether what it said is true and independently corroborated. So I took that centuries-old methodology and rebuilt it as a trust layer for multi-agent AI. I call it ISNAD. Everyone verifies the agent; ISNAD verifies the claim. The rigor belongs to twelve centuries of scholars — the transfer to AI is mine. I also wrote the failures into the paper: some mechanisms are validated, others aren't yet, and I said so in detail. A trust framework that hides its weaknesses is a contradiction in terms. Paper: https://arxiv.org/abs/2607.24117 Code: https://github.com/alizahidraja/isnad Agree or disagree, I'd love to hear it.

51m ago

---

**[Using Claude Mythos Preview, researchers at Anthropic have discovered improved ways to attack cryptographic algorithms (the mathematical methods used to keep online data private)](https://www.reddit.com/r/artificial/comments/1v99cuk/using_claude_mythos_preview_researchers_at/)**

Anthropic researchers find weaknesses in cryptographic algorithms with Claude Mythos Preview

🔗 [anthropic.com](https://www.anthropic.com/research/discovering-cryptographic-weaknesses) • 13h ago

---

**[Scanned 5 DTC Brands in 50 Seconds. None of Them Are Ready for AI Shopping Agents.](https://www.reddit.com/r/artificial/comments/1v9mvb1/scanned_5_dtc_brands_in_50_seconds_none_of_them/)**

We built a free, static-only scanner — 18 checks, no API calls, just HTML analysis. Then we pointed it at five brands that obsess over customer experience: Glossier, Allbirds, Gymshark, Drunk Elephant, and Brooklinen. https://preview.redd.it/jvc3yi9xt3gh1.png?width=907&format=png&auto=webp&s=6b3eec8215adceb05c557e3818b802e8fde8ef0c Every brand has clean structured data. Prices are server-rendered. No prompt injection. Robots.txt is open. The data layer works. But the moment an agent tries to do something — pick a size, add to cart, search for another product — it hits a wall of custom JavaScript that has no semantic meaning. Gymshark is the most striking. Three million monthly visits, Gen Z audience (the demographic most likely to use AI shopping agents), and their homepage has no search form an agent can find. The size picker is invisible to non-browser clients. The cart API returns nothing. An agent trying to buy a $30 t-shirt would fail at every interaction step. The revenue math is uncomfortable. If 5-15% of traffic is AI-referred (Gartner's 2027 projection), and these agents convert at 2-4% when they work, these five brands are collectively leaving $82,000 to $491,000 per month on the table. Not because their products are bad or their pages are ugly — because their size pickers use <div> instead of <select>. The fix is boring. Semantic HTML. A 20-line llms.txt file. Re-enabling the Shopify cart API that was on by default. The brands scoring highest in our 17-brand leaderboard (Kylie Cosmetics: 100, Framebridge: 96) aren't doing anything exotic. They're just using <select> elements and standard forms. The gap between "a beautiful page" and "a page agents can shop" is about a day of developer time. The question is which brands close it first. Scanned July 2026 with https://github.com/monkrus/agent-a. 18 static checks. Scanner is open source.

4h ago

---

**[The world's best mathematician won his prize this week and immediately announced he's leaving academia for OpenAI. That landed differently than I expected.](https://www.reddit.com/r/artificial/comments/1v8aeto/the_worlds_best_mathematician_won_his_prize_this/)**

I've been thinking about this one all weekend and I keep coming back to the same thing. Jacob Tsimerman just won the Fields Medal. If you're not familiar, it's the highest honor in mathematics, only awarded every four years, roughly the Nobel Prize of the field. He got it for solving a problem that had been open for nearly 40 years. And then, at the press conference, on the same day, he announced he's leaving his university position to join OpenAI's safety team. His exact words were: "The math profession as we know it now, I don't think it will exist the way it exists right now." I've seen a lot of AI announcements. That one hit differently. This isn't someone pivoting because they couldn't make it in academia. This is the person who just stood at the top of the field saying the field itself is changing underneath him. Then there's the infrastructure story. NVIDIA is in talks to backstop $250 billion in financing for a 10-gigawatt OpenAI data center in southern Ohio, built on a decommissioned uranium enrichment site. The total cost including chips could exceed $500 billion. That's not a software company. That's an energy company pretending to be a software company. And Kimi K3 weights dropped on July 26, a day early. 2.8 trillion parameters, 1 million token context, free to download from Hugging Face. The largest open model ever released. Anyone can run it now. Three things in one week. Talent, capital, and capability all moving at the same time. The Tsimerman thing is the one I can't stop thinking about though. What's your read on it?

1d ago

---

**[Will AI literacy become a basic workplace skill?](https://www.reddit.com/r/artificial/comments/1v8vu55/will_ai_literacy_become_a_basic_workplace_skill/)**

A few years ago, knowing how to use a computer was a big advantage. Today, it’s expected. I feel AI might follow a similar path. Knowing how to use AI tools effectively could become a basic skill across many jobs. Not everyone needs to build AI models but understanding how to use them, verify outputs and improve workflows might become important. Do you think AI skills will become a normal requirement in the workplace or is the hype bigger than the actual impact?

22h ago

---

**[AI coding tools are saving me hours but I genuinely can't tell if I'm getting dumber](https://www.reddit.com/r/artificial/comments/1v98szp/ai_coding_tools_are_saving_me_hours_but_i/)**

AI coding tools are saving me hours but I genuinely can't tell if I'm getting dumber Running a bootstrapped SaaS solo while also being home with a kid most of the day means my actual focused coding time is maybe 90 minutes if I'm lucky. So I leaned hard into Cursor and Claude to ship faster. And it's working, kind of. The thing I keep sitting with: I'm shipping features I would have spent days on. But when something breaks in a weird way, there are moments where I have to really dig to understand what the AI wrote and why. That used to not happen. I'd write it, I'd know it. There's a version of this that's fine, maybe even good. Nobody handrolls SQL joins and loses sleep over it. But there's another version where I'm slowly losing the ability to debug my own product at a fundamental level, which for a solo founder is a pretty bad place to end up. The cost/benefit math feels obvious day to day. Zoom out six months and I'm less sure. Curious whether others running small technical products have hit this wall or if I'm just being paranoid about a tool that's clearly net positive. Also wondering if this is skill atrophy or just a different skill now. Alt titles: Anyone else feel like AI coding tools are making you faster but less sharp? | Solo technical founders: are you actually understanding what AI writes for you? | Is AIassisted coding a longterm liability for small teams or am I overthinking it?

14h ago

---

---

## Google News: "ai"

**[Mark Zuckerberg says US should not ban Chinese AI](https://www.ft.com/content/af4fa147-7fdd-42eb-8eb2-3f624a89a4e4?syn-25a6b1a6=1)**

Meta chief warns against ‘regulatory capture’ of American rules on the technology

Financial Times • 7h ago

---

**[Mark Zuckerberg Blasts Centralization of A.I. Power](https://www.nytimes.com/2026/07/28/technology/mark-zuckerberg-meta-ai.html)**

The New York Times • 8h ago

---

**[Opinion | The AI Future Is for Everyone](https://www.wsj.com/opinion/the-ai-future-is-for-everyone-a0c24e20)**

WSJ • 16h ago

---

**[Employees at the world’s biggest AI companies are calling for a slowdown in AI development](https://www.cnn.com/2026/07/28/tech/ai-development-tech-employees-open-letter)**

Top staffers from the biggest AI and technology companies urged the US government to slow the pace of artificial intelligence development so that safety and security measures can catch up in an open letter.

CNN • 10h ago

---

**[More than 1,000 AI workers urge safeguards to slow AI development](https://www.yahoo.com/news/science/articles/more-1-000-ai-workers-090334137.html)**

More than 1,000 employees at leading artificial intelligence (AI) companies have signed an open letter calling for safeguards that would allow the rapid advance of AI to be slowed if necessary. They w...

Yahoo • 33m ago

---

**[AI industry slowdown may be needed after security scare, leaders warn](https://techxplore.com/news/2026-07-ai-industry-slowdown-leaders.html)**

Tech Xplore • 57m ago

---

**[UBS CEO says the AI pullback is healthy — but there’s a bigger risk investors should watch](https://www.cnbc.com/2026/07/29/ubs-earnings-ai-correction-stocks-swiss-bank.html)**

The Swiss banking gian reported pre-tax profits of $3.6 billion for the quarter, as CEO Sergio Ermotti warned of geopolitical volatility ahead.

CNBC • 1h ago

---

**[New York school pauses plan to deploy humanlike AI robot teacher after backlash](https://www.npr.org/2026/07/29/g-s1-136072/ai-robot-teacher)**

A school district in upstate New York is pausing plans to deploy an AI-powered, humanoid robot in the classroom after state education officials, teachers and local residents raised concerns.

NPR • 12m ago

---

**[Trump administration bans new Chinese humanoid robots](https://www.bbc.com/news/articles/cp9e2ex3ekyo)**

The US and China are locked in a race to the lead the world in robotics and artificial intelligence.

BBC • 7h ago

---

**[Trump administration bans new Chinese humanoid robots, to protect US AI buildout](https://www.reuters.com/world/trump-administration-ban-new-chinese-robots-inverters-protecting-us-ai-buildout-2026-07-28/)**

Reuters • 13h ago

---

---

## HackerNews: "ai"

**[US citizen charged after GrapheneOS phone wipes during airport search](https://news.ycombinator.com/item?id=49063022)**

The case centers on Tunick's use of GrapheneOS, an open-source operating system that works on Google Pixel phones and lets users enter a passcode to wipe a...

⬆️ 1318 • 💬 1105 • 2d ago • [TechSpot](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html)

---

**[AI companies are shredding rare books](https://news.ycombinator.com/item?id=49068738)**

🦔AI companies are bulk-buying rare books, scanning them through high-speed machines that cut the spines off, and shredding the originals. A service called ISBNdb facilitates orders of up to a million books and keeps buyers anonymous. Pre-2022 books are premium because they're

⬆️ 788 • 💬 508 • 1d ago • [X (formerly Twitter)](https://twitter.com/HedgieMarkets/status/2081534588485296565)

---

**[London Gatwick has launched a robotic airport parking service](https://news.ycombinator.com/item?id=49058669)**

London Gatwick is the first UK airport to launch robotic parking. Passengers can keep their keys while autonomous robots park their cars.

⬆️ 291 • 💬 270 • 2d ago • [AGN](https://aerospaceglobalnews.com/news/gatwick-airport-robotic-parking-stanley-robotics/)

---

**[AI companies spend record sums on Washington lobbying](https://news.ycombinator.com/item?id=49069939)**

Rising expenditure from OpenAI, Anthropic, Google and Microsoft reflects growing battle over federal policy

⬆️ 275 • 💬 144 • 1d ago • [ft.com](https://www.ft.com/content/d8a5f95e-3b6d-463a-a848-c9ef8e2394db)

---

**[Apple Will 'Watch Everything Burn' When the AI Bubble Bursts](https://news.ycombinator.com/item?id=49070427)**

Memory prices have doubled, Macs and iPads have gone up, and iPhones are expected to follow. Ed Zitron – who writes the Where's Your Ed At newsletter, hosts the Better Offline podcast, and has been described by Politico as the AI boom's most "acerbic gadfly" – has spent years arguing the buildout driving those costs will never pay for itself. We asked him what happens to Apple if he's right. You've been calling AI a bubble since before it was fashionable.

⬆️ 251 • 💬 352 • 1d ago • [MacRumors](https://www.macrumors.com/2026/07/27/ed-zitron-apple-watch-it-burn-ai-bubble-bursts/)

---

**[The New AI Superpowers: Focus and Followthrough](https://news.ycombinator.com/item?id=49057877)**

Burnout is on the rise again, with an ironic twist.

⬆️ 215 • 💬 78 • 2d ago • [rickmanelius.com](https://www.rickmanelius.com/p/the-new-ai-superpowers-focus-and)

---

**[LearnVector – Andrew Ng's AI company building one‑to‑one learning experiences](https://news.ycombinator.com/item?id=49092499)**

A new AI company from Andrew Ng, with a $100M investment from Coursera — building one-to-one learning that stays with you until you've mastered new skills.

⬆️ 180 • 💬 108 • 7h ago • [LearnVector](https://learnvector.ai/)

---

**[Terence Tao: Mathematics in the Age of AI [pdf]](https://news.ycombinator.com/item?id=49056620)**

⬆️ 163 • 💬 64 • 2d ago • [teorth.github.io](https://teorth.github.io/tao-web/slides/age-of-ai-icm-2026.pdf)

---

**[Google's Beyond Zero: Enterprise Security for the AI Era](https://news.ycombinator.com/item?id=49081644)**

⬆️ 151 • 💬 77 • 23h ago • [spawn-queue.acm.org](https://spawn-queue.acm.org/doi/10.1145/3819083)

---

**[Show HN: Formally verified 3D CSG: Trust 93 lines spec, not 1000 lines AI code](https://news.ycombinator.com/item?id=49083239)**

Formally verified 3D mesh intersection - trust 93 lines of spec, not 1000+ lines of AI-written code - schildep/verified-3d-mesh-intersection

⬆️ 109 • 💬 48 • 20h ago • [GitHub](https://github.com/schildep/verified-3d-mesh-intersection)

---

---

## YouTube Videos: "ai"

**[China’s Double Export Ban Sends a Terrifying Warning - US AI Panic Begins](https://www.youtube.com/watch?v=LPHgLREKtbA)**

Buy Gold & Silver At A Discount: https://bit.ly/IPM-Sean-Foo-Gold - Just use the code: SEANFOO at checkout In a dual move, ...

📺 Sean Foo

👁️ 72K • 👍 5K • 💬 490 • ⏱️ 14:46 • 1d ago

---

**[Top AI employees issue &#39;extinction risk&#39; warning about artificial intelligence | CUOMO](https://www.youtube.com/watch?v=K0jrkQalga0)**

Chris Cuomo opens "The Future Is Now" after being momentarily replaced by a robot with a preview of NewsNation's 'The Future ...

📺 NewsNation

👁️ 6K • 👍 132 • 💬 36 • ⏱️ 5:07 • 8h ago

---

**[BEYOND HUMAN CONTROL?: Palantir CEO on AI risks and why US can’t follow Europe](https://www.youtube.com/watch?v=zVp3gGEyqQE)**

Palantir CEO Alex Karp discusses open-weight artificial intelligence models, how he believes the technology should be regulated ...

📺 Fox Business

👁️ 79K • 👍 1K • 💬 221 • ⏱️ 13:22 • 1d ago

---

**[The AI data center secret just got out](https://www.youtube.com/watch?v=ShbBUi6rcgI)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 202K • 👍 9K • 💬 2K • ⏱️ 16:17 • 1d ago

---

**[AI Layoffs Have Completely BACKFIRED](https://www.youtube.com/watch?v=UU4ogejP-Ms)**

Replacing Humans With AI Has Been A Complete Disaster Get 20% off DeleteMe by going to ...

📺 Damon Cassidy

👁️ 86K • 👍 4K • 💬 739 • ⏱️ 21:32 • 9h ago

---

**[AI Whistleblower: The World Will Change Horribly In The Next 12 Months](https://www.youtube.com/watch?v=VX0GU7gyIOU)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Daniel Kokotajlo, a former OpenAI ...

📺 Neural Nutshell

👁️ 44K • 👍 1K • 💬 382 • ⏱️ 15:25 • 1d ago

---

**[OpenAI Shocks The World With GENIE... Almost Unlimited AI Power](https://www.youtube.com/watch?v=vfSplCaxHzM)**

Sam Altman says OpenAI's ultimate AI could work like a genie that grants any wish. Meanwhile, its most powerful model is ...

📺 AI Revolution

👁️ 49K • 👍 2K • 💬 272 • ⏱️ 13:07 • 1d ago

---

**[Why the AI crash is going viral](https://www.youtube.com/watch?v=iR0P6eVqpy8)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 259K • 👍 10K • 💬 2K • ⏱️ 15:38 • 1d ago

---

**[10 Times AI Said Things That Scientists Still Can&#39;t Explain](https://www.youtube.com/watch?v=mH4NmqSl2FE)**

Artificial intelligence has produced responses so strange and unexpected that even the researchers who built these systems ...

📺 MostAmazingTop10

👁️ 89K • 👍 2K • 💬 162 • ⏱️ 8:49 • 1d ago

---

**[South Korea&#39;s AI bubble just crashed](https://www.youtube.com/watch?v=8tZt85X4DjA)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 250K • 👍 10K • 💬 1K • ⏱️ 14:58 • 20h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 99,214 • ❤️ 8,344 • 1d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,694,935 • ❤️ 3,460 • 5h ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 736,692 • ❤️ 877 • 1h ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 4,804 • ❤️ 682 • 1d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 67,286 • ❤️ 805 • 1d ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 18,933 • ❤️ 535 • 20h ago

---

**[Mage-Flow](https://huggingface.co/microsoft/Mage-Flow)**

*Microsoft*

Mage-Flow is a 4B-scale text-to-image generation and instruction-based image editing model, featuring an efficient native-resolution generation stack (512-2048px) with competitive quality and low latency. It excels at both generating novel images from text and performing versatile image edits, including semantic changes and restoration, with variants for base, RL-aligned, and fast Turbo inference.

`text-to-image` `4.1B`

⬇️ 2,007 • ❤️ 430 • 6d ago

---

**[KAT-Coder-V2.5-Dev](https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev)**

*Kwaipilot*

KAT-Coder-V2.5-Dev is a 35B parameter Mixture-of-Experts (MoE) text-generation model specialized for agentic coding tasks, achieving State-of-the-Art performance on benchmarks like SWE-bench.

`text-generation` `34.7B`

⬇️ 6,275 • ❤️ 295 • 1d ago

---

**[Inflect-Micro-v2](https://huggingface.co/owensong/Inflect-Micro-v2)**

*Owen Song*

Inflect-Micro-v2 is a compact, fixed-voice English text-to-speech model (under 10M parameters) optimized for local, deterministic waveform synthesis. It supports long-text handling and runs efficiently on CPU or CUDA, making it suitable for edge AI applications.

`text-to-speech`

⬇️ 645 • ❤️ 276 • 1d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 1,267,198 • ❤️ 4,617 • 27d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 307 • 💬 5 • ⭐ 3,654 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 72 • 💬 5 • ⭐ 20,112 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 50 • 💬 4 • ⭐ 34,867 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 37 • 💬 3 • ⭐ 15,788 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 175 • 💬 10 • ⭐ 51,013 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 264 • 💬 5 • ⭐ 15,259 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 117 • 💬 4 • ⭐ 94,884 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 82,438 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 76,064 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[JarvisHub: An Open Harness for Canvas-Native Multimodal Creative Agents](https://huggingface.co/papers/2607.23588)**

*Yunlong Lin, Zixu Lin, Zhaohu Xing et al. (26 authors)*

Creative AI is moving from single-step asset generation toward long-horizon multimodal production. Although recent generative models can synthesize high-quality images, videos, audio clips, UI elements, storyboards, slides, and other creative assets, real-world creative work requires more than isolated prompt-output interactions. It involves references, drafts, alternatives, edits, failed attempts, version relations, tool actions, evaluation signals, and human feedback, which together form an evolving project state. Existing prompt-based, chat-based, and node-based generation systems only partially support this state, as they often discard intermediate context, rely on linear conversations, or require manually specified workflows. Recent commercial systems indicate a shift toward agent-assisted creative production, but their closed architectures make it difficult to study how agents represent context, choose tools, revise artifacts, recover from failures, and maintain consistency over time. To address this gap, we introduce JarvisHub, a canvas-native creative agent harness for long-horizon multimodal creation. JarvisHub treats an editable canvas as the user workspace, the agent's external memory, action space, and shared project state, representing multimodal artifacts, dependencies, versions, and feedback as typed canvas nodes and links. Through a three-layer architecture of canvas state, protocol bridge, and agent runtime, JarvisHub enables agents to act within an inspectable and editable creative state. This design moves creative agents beyond isolated tool use toward sustained, human-steerable creative automation, where agents can progressively plan, generate, revise, and organize multimodal projects while users remain able to inspect, guide, and intervene throughout the process.

▲ 113 • 💬 2 • ⭐ 85 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.23588) • [💻 code](https://github.com/LYL1015/JarvisHub) • [🔗 project](https://www.jarvishub.site/)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.3k • 🔱 1.1k • 1d ago

---

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

`Python`

⭐ 3.3k • 🔱 264 • 2d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.9k • 🔱 403 • 11m ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.6k • 🔱 305 • 20d ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 2.6k • 🔱 223 • 1d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 2.2k • 🔱 239 • 3d ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.8k • 🔱 202 • 1d ago

---

**[MIgHTy-alIeN/MEV-Arbitrage-Bot](https://github.com/MIgHTy-alIeN/MEV-Arbitrage-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 1.6k • 🔱 1.1k • 1m ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.5k • 🔱 115 • 7d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs — six tuned states, two sizes, auto dark/light

`TypeScript`

⭐ 1.2k • 🔱 94 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
