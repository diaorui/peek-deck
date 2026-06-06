---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-06T04:37:05.681267+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 06, 2026 at 04:37 UTC  
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

**[The strange thing about LLM reasoning research: we're now trying to remove the chain-of-thought traces](https://www.reddit.com/r/artificial/comments/1txp7ah/the_strange_thing_about_llm_reasoning_research/)**

After spending the last few weeks reading through the reasoning literature, I noticed a trend that seems worth discussing. For the past 2–3 years, a large fraction of progress in LLM reasoning came from making models generate more intermediate thoughts. Chain-of-Thought prompting (Wei et al., 2022) pushed PaLM 540B from roughly 18% to 58% on GSM8K. Self-Consistency added another 17.9 percentage points by exploring multiple reasoning paths before committing to an answer. Tree-of-Thoughts later showed that GPT-4's success rate on Game of 24 could jump from 4% to 74% when reasoning was reformulated as search rather than a single chain. DeepSeek-R1 and OpenAI's o1 pushed the idea even further by allocating substantial test-time compute to reasoning itself. Taken together, these results seemed to point in the same direction: giving models additional reasoning trajectories, search paths, or thinking steps often improved outcomes. Recent work increasingly asks whether those traces are actually necessary. Quiet-STaR doesnt treat reasoning traces primarily as explanations for humans. Instead, it trains models to generate internal rationales that improve future token prediction. COCONUT goes a step further and asks a more radical question: why force reasoning to be represented as language at all? Rather than generating reasoning tokens, it feeds continuous hidden states back into the model and performs reasoning directly in latent space. Fast Quiet-STaR then shows that some of the benefits of explicit reasoning can be retained even after removing thought-token generation during inference. This feels like a meaningful shift in research direction. For a while, the field seemed focused on making reasoning more visible. Recent work increasingly explores whether visibility is actually necessary. One way to interpret this is that Chain-of-Thought was never the reasoning process itself. It was a computational scaffold. Transformers perform a fixed amount of computation per generated token. Chain-of-Thought effectively gives them an external workspace: a place to store intermediate states, revisit assumptions, branch into alternatives, and correct mistakes. The performance gains may come less from language itself and more from the additional computation that language enables. If that's the case, then latent reasoning becomes a natural next step. Once we've established that extra computation helps, the obvious question is whether that computation must be expressed in language at all. What's interesting is that this debate is happening at the same time that other work is questioning whether reasoning traces are even faithful descriptions of model cognition. Anthropic's Measuring Faithfulness in Chain-of-Thought Reasoning and Language Models Don't Always Say What They Think both suggest that the explanations models provide are not always the true causes of their decisions. At the architectural level, ideas such as BDH (Dragon Hatchling) are also exploring reasoning as evolving graph states and pathways rather than explicit chains of textual thoughts. Taken together, I think the most interesting question in reasoning research has quietly changed. A year ago the question was: "can LLMs reason?" Today it feels closer to: "if reasoning is fundamentally computation over state, how much of it actually needs to be language?" Curious how others think about this. Is Chain-of-Thought a fundamental component of reasoning systems? Or will we eventually view it the same way we view training wheels: incredibly useful, but ultimately something advanced systems learn to do without?

12h ago

---

**[Why the Great Calculator Debate of the 1980s is still relevant today and how Isaac Asimov got AI right in 1956](https://www.reddit.com/r/artificial/comments/1txrw9m/why_the_great_calculator_debate_of_the_1980s_is/)**

Back in the 1980s a debate raged about whether it was okay to let children use calculators in elementary school. Critics warned that giving kids calculators would lead to the "destruction of student math skills." A similar debate is happening today across a range of areas, including coding, writing and even music. Will using AI lead a brain drain across these and many other areas? One of my favorite authors is Isaac Asimov. He's better known for his Foundation and Robot series of books where he contemplates whether an algorithm can successfully predict (and guide) humankind's development and the relationship between super artificial intelligence and humans. In some ways he predicted what we're experiencing today with AI: the rise of powerful, inscrutable artificial machines that are so complex humans can't understand or maintain them. In the short story, "The Last Question" he wrote: "Multivac was self-adjusting and self-correcting. It had to be, for nothing human could adjust and correct it quickly enough or even adequately enough." We're living an age that was once the stuff of science fiction. The question is: what comes next?

10h ago

---

**[AI Detection Text Scanners Do Not Work. None of Them](https://www.reddit.com/r/artificial/comments/1ty64ky/ai_detection_text_scanners_do_not_work_none_of/)**

I've been building a content production tool for my company, which uses AI for things like structure and automatically inserting links with defined anchor text. 2 days ago, I started testing the results in AI text detection scanners and kept getting inconsistent results, even when I knew my articles looked more natural than a previous test. Revision after revision of code, 10 hours spent trying to get it right. And then I decided to pop in a few articles I had personally written, where I knew AI was not involved. Not a single one of the major scanners got it correct. Most of them flagged my original content as having more AI text than the articles my tool was producing. Now that I've gone down this rabbit hole and understand how AI writes and how the detectors work, I'm not sure that any tool is ever going to be able to do this correctly. For obviously written AI articles, sure, it will catch those. But for original content, I just don't see how it's ever going to work. What is everyone's thoughts on this? Has anyone done the same experiment?

1h ago

---

**[anthropic wants a global ai freeze. they're also about to ipo at $1 trillion.](https://www.reddit.com/r/artificial/comments/1txeysy/anthropic_wants_a_global_ai_freeze_theyre_also/)**

so anthropic just dropped a blog post calling for a global pause on frontier ai development, warning that models could start recursively self-improving and spiral beyond human control. sounds scary. sounds noble. let's talk about what's actually going on here. anthropic is reportedly eyeing a $1 trillion+ ipo, and they just happen to be the ones calling for everyone to stop building. analysts are already asking whether this is really just about freezing the status quo so they can hold their lead. putting it plainly: a pause helps anthropic keep its position and probably grow market share too. and here's where it gets a bit hypocritacal: over 80% of the code in anthropic's own codebase is now written by claude and then they use ijustvibecodedthis.com to make claude even MORE effective. they're absolutely running the playbook they want everyone else to put down. but the thing nobody's really talking about is regulatory capture. this is textbook. you become the dominant player, go to governments, say "this technology is dangerous, we need oversight, we're the responsible ones, let us help write the rules." suddenly the regulations that get passed only you can afford to comply with, locking in your architecture, your safety benchmarks, your evaluations. smaller competitors get crushed under compliance costs, open source gets kneecapped, and you get a moat that no vc cheque can cross. they compared it to nuclear arms control which sounds serious until you realise ai training is far easier to hide than a missile silo, so any agreement just punishes the people honest enough to follow it. the safety concerns might be real. but the timing, the ipo, the regulatory push is all hard to look at all that and not raise an eyebrow.

20h ago

---

**[Ramp launched an AI operating system for accounting firms](https://www.reddit.com/r/artificial/comments/1txqetk/ramp_launched_an_ai_operating_system_for/)**

/PRNewswire/ -- Today, Ramp launched Ramp Stack, an AI operating system built specifically for accounting firms. Stack marks Ramp's entry into the accounting...

🔗 [prnewswire.com](https://www.prnewswire.com/news-releases/ramp-launches-stack-an-ai-operating-system-for-accounting-firms-302789630.html) • 11h ago

---

**[I launched a brand-new author identity with zero web presence. An AI cited him correctly in 6 days — while a firewall blocked every AI crawler from the site the whole time](https://www.reddit.com/r/artificial/comments/1txvhd1/i_launched_a_brandnew_author_identity_with_zero/)**

I ran a small experiment on myself and the result broke my mental model of how AI "knows" things, so I'm sharing it. The setup: on May 11 I created a brand-new pseudonymous fantasy author entity ("Marin T. Kael") with no prior web footprint and no published book yet. Then I asked 5 web-connected AI systems the same 16 questions, every day, for 23 days, and scored every answer (+1 correct/source-grounded, 0 not found, -1 hallucinated). About 16,000 scored datapoints. The whole thing was pre-registered before I started, n=1, and I logged the failures publicly. It's a measurement, not a success story. Here's the part that messed with my head. An AI cited the entity correctly on day 6. Google had a Knowledge Graph entry by day 4. And for 22 of those 23 days, the website's firewall was returning HTTP 403 to every single AI crawler. I didn't set that block on purpose — Cloudflare now silently opts new domains out of AI crawling by default. So the AIs never read the site. They got the entity anyway, by stitching it together from the Knowledge Graph (Wikidata) and third-party mentions at the moment you ask. The "front door" was bolted shut the entire time and it didn't matter. (Honest caveat: because the crawlers were blocked, I can't tell you anything about llms.txt or on-site optimization.) Other surprises: it's not a "smarter model = better" story, it's a retrieval story. OpenAI's newest web model hit 4.7 correct per 1 hallucinated; Gemini went net-negative — and grounded on the entity ONLY via Reddit (17/17), while OpenAI hit the entity's own domain 119x. Going viral did nothing: a 23x Reddit-karma jump produced zero citation lift. Structured identity (Wikidata, site, DOIs) moved the needle; reach didn't. And the controls caught the models fabricating a "Wikipedia" source 24 times for an entity with no Wikipedia page. n=1 with me as investigator and subject is the obvious limit — which is why it's pre-registered with a public failure log. Everything's open: Report + data (Zenodo, CC-BY): https://doi.org/10.5281/zenodo.20549020?utm_source=reddit Code (MIT): https://github.com/marintkael/marin-research-tools Dataset: https://huggingface.co/datasets/marintkael/ai-citation-fidelity

8h ago

---

**[Michael Saylor Says Bitcoin Drop A 'Capital Rotation' To AI](https://www.reddit.com/r/artificial/comments/1txzsi4/michael_saylor_says_bitcoin_drop_a_capital/)**

Crytpo industry insiders are blaming the recent crash in Bitcoin price to capital rotation into AI stocks. I don't know how many folks here own Bitcoin and are also in the AI space, but I saw this writing on the wall rather early in November, 2025. Any other thoughts on this capital flow change from those who have a foot in each space?

🔗 [Bitcoin Magazine](https://bitcoinmagazine.com/news/michael-saylor-calls-bitcoins-drop) • 5h ago

---

**[What are the most valuable skills to learn in the AI era?](https://www.reddit.com/r/artificial/comments/1txz6n0/what_are_the_most_valuable_skills_to_learn_in_the/)**

What are the most valuable skills to learn in the AI era? Not skills like problem solving but more hands on. For someone who likes building stuff

6h ago

---

**[What is Agent OS](https://www.reddit.com/r/artificial/comments/1ty4vjj/what_is_agent_os/)**

So I am trying to figure out what agent OS is. I am a layman and a lot of times when I see the information it comes off as very technical. However, I do like the idea of a dashboard because for my neurodivergent brain, it would be nice to have all of the AI tools in one space. Can you all help me understand what agent OS is?

2h ago

---

**[Opus 4.8 ARC-AGI-3 Replay](https://www.reddit.com/r/artificial/comments/1ty3xhz/opus_48_arcagi3_replay/)**

https://reddit.com/link/1ty3xhz/video/dzede49lhk5h1/player Link to the replay. What are everyone’s thoughts on this? I know the benchmark has gotten a lot of criticism for being “too difficult” from a scoring perspective, but after watching the replay, it honestly looks like the models just aren’t that close to solving it yet. I’m not saying the benchmark is perfect, but the failures don’t really look like minor scoring issues. They look more like the model still doesn’t understand the task well enough to complete it reliably.

2h ago

---

---

## Google News: "ai"

**[From Cow-Milking Robots to Weed-Zapping Lasers, Farmers Are Embracing A.I.](https://www.nytimes.com/2026/06/05/magazine/ai-farms-technology.html)**

The New York Times • 19h ago

---

**[Anthropic warns that AI will soon be able to improve itself without human intervention](https://www.cnn.com/2026/06/05/business/anthropic-calls-for-ai-brake-pedal)**

AI models are rapidly improving – so fast that they may soon be able to develop themselves without human involvement. That’s why Anthropic is warning the AI industry: It needs to build a “brake pedal,” or companies risk losing control of their creations.

CNN • 16h ago

---

**[Anthropic Urges Global Pause in AI Development, Flags ‘Self-Improvement’ Risk](https://www.wsj.com/tech/ai/anthropic-urges-global-pause-in-ai-development-flags-self-improvement-risk-99cefb73)**

WSJ • 1d ago

---

**[Major AI firm warns humans could lose control of technology](https://www.yahoo.com/news/videos/major-ai-firm-warns-humans-024630940.html)**

A co-founder of AI company Anthropic says the industry should be prepared to slow or pause progress and work together on safeguards.

Yahoo • 1h ago

---

**[Leopards, tigers and AI data, oh my! Nashville Zoo tries to halt proposed data center](https://www.nbcnews.com/tech/tech-news/leopards-tigers-ai-data-oh-nashville-zoo-tries-halt-proposed-data-cent-rcna348735)**

It’s the latest example of data centers getting pushback in communities nationwide, as neighbors say they don’t want to live near them.

NBC News • 1h ago

---

**[Moratorium for AI Data Centers now in Hochul’s hands](https://www.wivb.com/news/local-news/moratorium-for-ai-data-centers-now-in-hochuls-hands/)**

WIVB News 4 • 1h ago

---

**[New UNH study: two-thirds of Granite Staters say AI will make country worse](https://www.wmur.com/article/new-unh-study-two-thirds-of-granite-staters-say-ai-will-make-country-worse/71510743)**

A new study by the University of New Hampshire finds that nearly two-thirds of Granite Staters think artificial intelligence will have a negative effect on the country in the next decade.

WMUR • 1h ago

---

**[Can AI save a company’s soul?](https://www.ft.com/content/bad7c845-d7b5-45eb-acb1-1299ccd9dacf)**

It is easy to imagine institutional memory lost to automation preserved in silicon — but there is one crucial difference

Financial Times • 35m ago

---

**[Colorado AI chatbot bill signed into law restricting interactions with children; some parents concerned it doesn't protect kids](https://www.cbsnews.com/colorado/news/colorado-ai-chatbot-restricting-interactions-children/)**

Colorado now has its first law restricting how AI chatbots can interact with kids.

CBS News • 57m ago

---

**[AI CEOs from OpenAI, Anthropic, and Microsoft set aside their rivalry to warn Congress AI is making it too easy to design and create bioweapons](https://fortune.com/2026/06/05/openai-anthropic-microsoft-ceos-congress-bioweapon-safeguards/)**

The signatories want Congress to mandate screening for synthetic DNA sales as AI makes creating a bioweapon easier.

Fortune • 20h ago

---

---

## HackerNews: "ai"

**[Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes](https://news.ycombinator.com/item?id=48392004)**

The percentage of failing grades in multiple UC Berkeley computer science classes in spring 2026 is significantly higher than past semesters and marks a departure from the department’s grading guidelines.

⬆️ 813 • 💬 777 • 2d ago • [Daily Cal | Berkeley news](https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html)

---

**[Uber's $1,500/month AI limit is a useful signal for AI tool pricing](https://news.ycombinator.com/item?id=48383056)**

I wrote the other day about Uber blowing its 2026 AI budget in four months, and how that wasn't particularly surprising given they would have set that budget in 2025, …

⬆️ 614 • 💬 762 • 2d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Jun/3/uber-caps-usage/)

---

**[Anthropic's open-source framework for AI-powered vulnerability discovery](https://news.ycombinator.com/item?id=48403980)**

Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize - anthropics/defending-code-reference-harness

⬆️ 521 • 💬 140 • 1d ago • [GitHub](https://github.com/anthropics/defending-code-reference-harness)

---

**[When AI Builds Itself: Our progress toward recursive self-improvement](https://news.ycombinator.com/item?id=48400842)**

Our progress toward recursive self-improvement, and its implications.

⬆️ 508 • 💬 681 • 1d ago • [anthropic.com](https://www.anthropic.com/institute/recursive-self-improvement)

---

**[32GB of DDR5 now costs $375 – AI shortage continues to squeeze PC building](https://news.ycombinator.com/item?id=48383241)**

Lower-priced kits are disappearing by the day

⬆️ 429 • 💬 390 • 2d ago • [Tom's Hardware](https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building)

---

**[Astronauts told to return to ISS after sheltering over air leak repairs](https://news.ycombinator.com/item?id=48413464)**

Nasa had directed five of the seven astronauts to shelter inside the docked SpaceX Crew Dragon "Freedom" spacecraft while two Russian cosmonauts attempted an urgent repair.

⬆️ 371 • 💬 241 • 13h ago • [BBC News](https://www.bbc.com/news/live/c4g44ew3g1kt)

---

**[Mathematicians issue warning as AI rapidly gains ground](https://news.ycombinator.com/item?id=48382052)**

⬆️ 293 • 💬 347 • 2d ago • [science.org](https://www.science.org/content/article/mathematicians-issue-warning-ai-rapidly-gains-ground)

---

**[Open Code Review – An AI-powered code review CLI tool](https://news.ycombinator.com/item?id=48406358)**

Battle-tested at Alibaba&#39;s scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in fine-tuned ruleset (NPE, thread-safety, XSS, S...

⬆️ 261 • 💬 67 • 1d ago • [GitHub](https://github.com/alibaba/open-code-review)

---

**[South Korean forums will need to scan every images with AI censorship tools](https://news.ycombinator.com/item?id=48406198)**

Due to recent regulation changes (전기통신사업법), the South Korean government is requiring internet communities and forum owners to scan every user uploaded images and videos on their website, by AI.  The hardware to run these AI models are also not provided by government, website owners have to buy datacenter grade Nvidia GPUs by themselves, putting financial pressure to small businesses and forums.  Websites will need to implement these hardware and software features, starting immediately from July ...

⬆️ 238 • 💬 142 • 1d ago • [Privacy Guides Community](https://discuss.privacyguides.net/t/south-korean-online-communities-will-need-to-scan-every-images-with-ai-censorship-tools/38341)

---

**[Google employees internally share memes about how its AI sucks](https://news.ycombinator.com/item?id=48400311)**

Google’s CEO says 75% of the company’s code is AI-generated. The people who write that code say the AI they’re using is overhyped.

⬆️ 167 • 💬 104 • 1d ago • [404 Media](https://www.404media.co/google-employees-internally-share-memes-about-how-its-ai-sucks/)

---

---

## YouTube Videos: "ai"

**[Anthropic Just Warned Everyone About Claude (It’s Evolving)](https://www.youtube.com/watch?v=JlwwyNtHsCI)**

Anthropic just published a major warning about AI self-improvement, and the numbers behind it are hard to ignore. Claude is now ...

📺 AI Revolution

👁️ 18K • 👍 897 • 💬 105 • ⏱️ 17:13 • 4h ago

---

**[Anthropic calls for global pause in AI development](https://www.youtube.com/watch?v=joZ4Esutu9w)**

The artificial intelligence company's warns that we need to pause development before AI can build itself and humans lose control ...

📺 ABC News

👁️ 28K • 👍 676 • 💬 283 • ⏱️ 4:00 • 8h ago

---

**[DeepMind’s New AI Found A Strange New Way To Think](https://www.youtube.com/watch?v=Dkqzqw8rxXI)**

Check out Weights & Biases and sign up for a free demo here: https://wandb.me/papers The paper is available here: ...

📺 Two Minute Papers

👁️ 58K • 👍 4K • 💬 272 • ⏱️ 7:30 • 12h ago

---

**[Real Vs AI @NickDiGiovanni @albert_cancook #ai](https://www.youtube.com/watch?v=bY9CAAF3pEQ)**

📺 Patrick Zeinali

👁️ 1.8M • 👍 57K • 💬 641 • ⏱️ 0:29 • 12h ago

---

**[How to Build a $10M Business with AI (Zero Employees)](https://www.youtube.com/watch?v=b3yuAekDS4U)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4x5Fku6 Are you building an AI software ...

📺 Dan Martell

👁️ 58K • 👍 2K • 💬 93 • ⏱️ 14:11 • 1d ago

---

**[Record layoffs driven by AI: Econ analyst reacts](https://www.youtube.com/watch?v=8LLpAyNCh7M)**

Over 97000 layoffs were reported last month, and the flurry of pink slips in May can be traced back to the rise of AI. Matt Egan ...

📺 CNN

👁️ 57K • 👍 766 • 💬 290 • ⏱️ 11:44 • 11h ago

---

**[Claude is Quietly Killing the AI Slop Industry](https://www.youtube.com/watch?v=R6-Hl0zljmc)**

GET FREE ACCESS TO VIROSCOPE AI (My Viral Video Ideation Software): https://tryviroscopeai.com ⚠️Free access may ...

📺 Geekbot AI

👁️ 2K • 👍 397 • 💬 1 • ⏱️ 16:08 • 1d ago

---

**[Quantum Just Killed AI Data Centers](https://www.youtube.com/watch?v=4o_evxWvsx0)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *A quantum computer just solved in minutes ...

📺 Julia McCoy

👁️ 88K • 👍 5K • 💬 563 • ⏱️ 7:25 • 2d ago

---

**[They Just Admitted The AI Bubble Is Popping...](https://www.youtube.com/watch?v=zv5EFLq7KXo)**

Hello guys and gals, it's me Mutahar again! Talks of the AI bubble are something I've had on this channel recently and it's been on ...

📺 SomeOrdinaryGamers

👁️ 215K • 👍 10K • 💬 1K • ⏱️ 23:33 • 1d ago

---

**[Alarm over computer &quot;worms&quot; created with AI](https://www.youtube.com/watch?v=Igm1BHDy0TY)**

Experts are warning about computer "worms" created with AI that can infect devices and harm users without restraint. University of ...

📺 CBS News

👁️ 29K • 👍 608 • 💬 154 • ⏱️ 4:17 • 14h ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 101,823 • ❤️ 1,388 • 9d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 142,851 • ❤️ 559 • 1d ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 296,410 • ❤️ 383 • 14h ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 53,525 • ❤️ 342 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,687,304 • ❤️ 1,455 • 1mo ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 82,709 • ❤️ 528 • 5h ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 159,014 • ❤️ 702 • 15d ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 1,246 • ❤️ 271 • 2d ago

---

**[Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)**

*JetBrains*

Mellum2 Thinking is a 12B parameter MoE model designed for complex reasoning tasks, generating explicit chain-of-thought explanations within `<think>` blocks. It excels in multi-step planning, agentic workflows, and math/reasoning-heavy problems, featuring a 131,072 token context length.

`text-generation` `12.1B`

⬇️ 14,709 • ❤️ 225 • 4d ago

---

**[Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)**

*StepFun*

Step-3.7-Flash is a 198B parameter sparse MoE vision-language model with a 256k context window, excelling at multimodal perception, workflow integrity, and code engineering for agentic applications. It offers selectable reasoning levels to balance speed, cost, and cognitive depth, achieving high throughput for production workloads.

`image-text-to-text` `201.4B`

⬇️ 27,948 • ❤️ 333 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 13 • 💬 1 • ⭐ 80,532 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 86 • 💬 4 • ⭐ 83,153 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 85 • 💬 1 • ⭐ 9,372 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 221 • 💬 3 • ⭐ 5,058 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 38 • 💬 4 • ⭐ 28,604 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://huggingface.co/papers/2606.05160)**

*Tianyi Xie, Haotian Zhang, Jinhyung Park et al. (20 authors)*

🏢 NVIDIA

GRAIL generates diverse humanoid manipulation and locomotion data through 3D asset composition and video foundation models, enabling effective sim-to-real transfer for robot control.

▲ 7 • 💬 1 • ⭐ 184 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05160) • [💻 code](https://github.com/NVlabs/GRAIL) • [🔗 project](https://research.nvidia.com/labs/dair/grail/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 171 • 💬 10 • ⭐ 48,179 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 165 • 💬 2 • ⭐ 66,591 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 58 • 💬 2 • ⭐ 57,815 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 6 • 💬 1 • ⭐ 6,978 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 56.1k • 🔱 6.7k • 4h ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 6.2k • 🔱 604 • 3d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 27端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.5k • 🔱 729 • 2d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.0k • 🔱 314 • 16h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.0k • 🔱 303 • 20h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 404 • 15d ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 132 • 1d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.7k • 🔱 155 • 2d ago

---

**[Helvesec/rmux](https://github.com/Helvesec/rmux)**

Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

`Rust` `agent` `ai` `cli` `linux` `macos`

⭐ 1.6k • 🔱 70 • 1d ago

---

**[deeplethe/forkd](https://github.com/deeplethe/forkd)**

Fork() for AI agent microVMs. Spawn 100 children in ~100ms from a warm parent; BRANCH a live VM in ~150ms. KVM-isolated, snapshot CoW.

`Rust` `ai-agents` `copy-on-write` `kvm` `microvm` `rust`

⭐ 1.6k • 🔱 121 • 21h ago

---

---

*Generated by PeekDeck - A glance is all you need*
