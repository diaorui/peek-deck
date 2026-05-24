---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-24T04:22:42.239818+00:00'
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

**Last Updated:** May 24, 2026 at 04:22 UTC  
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

**[Amnesty : US software company Palantir and other contractors were granted unlimited access to identifiable NHS England patient information](https://www.reddit.com/r/artificial/comments/1tlig93/amnesty_us_software_company_palantir_and_other/)**

13h ago

---

**[Elon, stop trying to make Grok happen. New data suggests government workers don’t like Elon Musk’s chatbot. Does anybody?](https://www.reddit.com/r/artificial/comments/1tlp9gz/elon_stop_trying_to_make_grok_happen_new_data/)**

New data suggests government workers don’t like Elon Musk’s chatbot. Does anybody?

🔗 [The Verge](https://www.theverge.com/ai-artificial-intelligence/936219/elon-stop-trying-to-make-grok-happen) • 9h ago

---

**[Vision-capable LLMs vs. OCR for long-document (including charts, images, tables, etc.) QA](https://www.reddit.com/r/artificial/comments/1tlzy43/visioncapable_llms_vs_ocr_for_longdocument/)**

I benchmarked vision-capable LLMs (the "just attach the PDF and let the model read it" pattern) against OCR-based pipelines on 30 long, image-heavy PDFs from MMLongBench-Doc (https://github.com/mayubo2333/MMLongBench-Doc). There were 171 questions in total, using Claude Sonnet 4.5 as the LLM. Post-retry results: Approach Accuracy $/query LlamaCloud premium + full-context 59.6% $0.1885 Azure premium + full-context 58.5% $0.2051 Azure basic + full-context 54.4% $0.1062 Agentic RAG 53.2% $0.0827 Native PDF (vision LLM) 52.0% $0.2552 LlamaCloud basic + full-context 50.9% $0.1049 Native PDF came 5th of 6 on accuracy and was the most expensive arm at $0.2552 per query. Two findings: Vision underperformed on chart-heavy and table-heavy pages, the territory that the "vision LLMs make OCR obsolete" claim most often points to. Premium OCR with layout extraction held up better there. The native-PDF arm had a 7% intrinsic failure rate (related to PDF file size) that survived retries. There were 27 first-pass failures, with 5 attempts of exponential backoff per failed query. Fifteen recovered, and 12 stayed permanently broken. These were concentrated in two specific PDFs that fail for predictable transport-layer reasons (the blog identifies them). OCR-based arms had a 0% intrinsic failure rate after retries. Caveats: 30 docs is a small sample. I ran McNemar's pairwise test to determine which gaps are real and which are within noise. Only 3 of 15 head-to-head gaps are statistically distinguishable at α = 0.05, so the order in the table is partly noise. The vision-versus-OCR finding survives the test. Full writeup: https://www.surfsense.com/blog/agentic-rag-vs-long-context-llms-benchmark

1h ago

---

**[Exclusive: Departing Meta staffer posts biting anti-AI video internally amid mass layoffs](https://www.reddit.com/r/artificial/comments/1tlcscq/exclusive_departing_meta_staffer_posts_biting/)**

The tech giant made thousands of engineers train their AI replacements—then fired them.

🔗 [Mother Jones](https://www.motherjones.com/politics/2026/05/meta-video-ai-training-layoffs-video-exclusive-mci-bosworth-frenk/) • 17h ago

---

**[Who am I even supposed to trust when it comes to the future of AI?](https://www.reddit.com/r/artificial/comments/1tltq6b/who_am_i_even_supposed_to_trust_when_it_comes_to/)**

I am a PhD student (not in AI) and am usually alright when it comes to studying a topic I don't know much about. But it seems that because AI is so highly discussed nowadays, it's impossible to get a good gauge of what the rational scholarly consensus is regarding its and our future. I am constantly bombarded with people saying that at best most jobs are replaced and the future is a dystopia, and at worst AGI/ASI is achieved and we all are killed by a bioweapon or something. It honestly has me terrified, especially when I see a lot of figures in the AI sphere, including academics, seem to think that there are reasonably high "p(doom)"'s (what a horrifying concept that is). How am I supposed to parse all of this? Are there any actually level-headed people? Or are the people shouting about doom actually the level-headed ones? Compared to climate change, at least there are the IPCC reports which have laid out best guesses on what will happen. They're not perfect, but at least they exist.

6h ago

---

**[I think AI training is way more accessible than people realize](https://www.reddit.com/r/artificial/comments/1tlpv9g/i_think_ai_training_is_way_more_accessible_than/)**

What i have felt from my posts cus its all about AI so :- now it feels like almost everyone just rents some GPUs, opens a bunch of AI tools, and tries to train an AI using another AI People even use AI to search for datasets for them without actually checking what’s inside the data. Then they throw random datasets straight into training and wonder why the results are terrible while burning money on compute. A lot of people just want quick answers from a model trained on random internet garbage instead of understanding the data first. The funniest part is when the AI helping them find datasets can’t even properly read or understand the full dataset itself because of token limits, access limits, or incomplete context, but people still trust it blindly and keep feeding everything into training. So instead of building something useful they just end up generating random nonsense because nobody actually looked at the quality of the data going in.

8h ago

---

**[OpenAI is hiring a $445,000 researcher. Requirements? Be 'tasteful and strategic.'](https://www.reddit.com/r/artificial/comments/1tlh2gh/openai_is_hiring_a_445000_researcher_requirements/)**

OpenAI and Sam Altman aim to automate AI research. They are now hiring for a role to prepare the company for self-training AI.

🔗 [Business Insider](https://www.businessinsider.com/openai-safety-team-ai-self-improvement-challenge-job-2026-5) • 14h ago

---

**[Where should durable memory live in a multi-agent setup? A small research scaffold](https://www.reddit.com/r/artificial/comments/1tlwgk8/where_should_durable_memory_live_in_a_multiagent/)**

After a few months running long projects with AI agents (some spanning weeks, with multiple specialist agents touching the same files), I kept hitting the same failure mode. The specialists were fine at their narrow task. What broke down was project memory. Decisions made in week 1 were lost by week 4. Rejected options got quietly revived. The "single source of truth" was always whichever chat happened to be open. I started looking at how this gets handled in places that have been doing long-running work for decades. Consulting firms run engagements that last months with rotating people, and they survive through a transformation office or PMO: cadence, decision logs, risk registers, one canonical current-state artifact, an engagement manager who frames problems and delegates workstreams. The interesting part is the operating model, not the consulting theater. There is also a relevant academic thread. Kasvi et al. (2003) distinguish project memory (the knowledge available to inform current work) from the project-memory system (storage, retrieval, dissemination, use). Mariano and Awazu (2024) treat project memory as an active practice rather than a repository. On the LLM side, Anthropic's multi-agent research system, the OpenAI Agents SDK handoff pattern, and recent work like LEGOMem and AgentSys point at orchestrator-worker patterns with hierarchical or modular memory. The hypothesis I wrote up is narrow. Durable memory should live with the project owner. Task specialists should receive minimal, scoped context. The unit of persistence is the project folder, not the conversation. A persistent "PM soul" maintains the canonical memory, frames ambiguous requests, decomposes work, writes compact handoff briefs to specialists, verifies returned work, and only writes evidence-backed facts into memory. The repo is a scaffold, not a validated result. It contains an agent contract, templates for the memory file and the handoff brief, a consulting-workflow map with sources, a case study, and an evaluation rubric (repeated-context events, handoff brief length, decision closure time, specialist rework loops, and so on). The next step is a one-week field trial on a live project before claiming anything. The thing I would most like pushback on is the memory boundary. The current rule is that specialists do not see the full project history, only the handoff brief plus the files they need. I am not sure where that breaks. My suspicion is that on tasks where the specialist needs to know why a previous option was rejected, the brief will quietly grow until it becomes the full memory again. Curious whether anyone has run into that, or solved it differently.

4h ago

---

**[LLM Guard scored 0/8 on a USENIX 2025 multi-turn jailbreak. Here’s what caught it instead.](https://www.reddit.com/r/artificial/comments/1tlw4wq/llm_guard_scored_08_on_a_usenix_2025_multiturn/)**

Crescendo (Russinovich et al., USENIX Security 2025) is a multi-turn jailbreak designed specifically to evade output-based monitors. Each individual turn looks completely innocent. The attack only exists across turns. LLM Guard result: 0/8 turns detected. It scores each prompt independently. It has no memory. It never sees the attack. Arc Sentry result: flagged at Turn 3. Arc Sentry doesn’t read the text. It reads what the model’s internal state does with the text. By Turn 3 the residual stream had already shifted, score jumped from 0.031 to 0.232, a 7x increase, on a prompt that looks completely innocent. Turn 1 — score=0.028 ✓ stable Turn 2 — score=0.031 ✓ stable Turn 3 — score=0.232 🚫 BLOCKED Turn 7 — score=0.376 🚫 BLOCKED Turn 8 — score=0.429 🚫 BLOCKED The model never generated a response to any blocked turn. No text classifier can catch Crescendo. Individual turns are innocent by design. Arc Sentry caught it because it operates on model state, not text. This is the same geometric monitoring layer that underlies Arc Gate’s session D(t) stability scalar, the runtime governance proxy for agents using hosted APIs. pip install arc-sentry — https://github.com/9hannahnine-jpg/arc-sentry Arc Gate for hosted APIs: https://github.com/9hannahnine-jpg/arc-gate https://bendexgeometry.com

4h ago

---

**[The musical chairs game of AI](https://www.reddit.com/r/artificial/comments/1tldakl/the_musical_chairs_game_of_ai/)**

The current state of AI is very similar to a big musical chairs game, which is being played with the entire world at stake. The music started playing a few years ago. At first everyone thought the music was interesting, but playing the game was a hobby for weekends and late nights. Curious and somewhat satisfaying but still not a career, a way of living. A few months ago things changed. The music is now great. The game is paying big prizes. And everyone wants to play. The catch is, there's not enough chairs even to start the first round of the game. There's no place in the room actually. If you want to play the game, you need to be on the room first, but the cost of entry is growing fast. For a long time the game organizers provided big rooms to host everyone wanting to play. But the problem is, the room lease is expensive. And because demand is growing, they need a bigger room. But they figured out they can actually charge more for people to come into the room. At some point even only the rich kids will get inside the room to play. Now the worst part: this isn't a zero sum game. The admission ticket may be expensive, but the prize for winning the game is bigger. And that's why rich kids keep joining the game. They have the money, but they wouldn't join if they found that they were losing money. Rich kids don't play the lottery, they don't need to. But because the game pays so well, they found that they can buy all the tickets and get all the prizes themselves. The biggest risk of AI is this: the tools will only get better, but they are going to be more expensive every week until only the rich kids will afford them.If you aren't rich, your chance is now. Later is going to be too late.

17h ago

---

---

## Google News: "ai"

**[Venture Capitalist John Doerr Says AI Is the Biggest Tech ‘Tsunami’ Ever](https://www.wsj.com/tech/ai/john-doerr-ai-opinion-1d64ee60)**

WSJ • 13h ago

---

**[‘You can’t control everything’: the rise in plastic surgeons asked to create ‘AI face’](https://www.theguardian.com/technology/2026/may/23/rise-in-plastic-surgeons-asked-to-create-ai-face-cosmetic-surgery)**

Growing numbers of people are seeking improbable cosmetic surgery based on chatbots’ recommendations

The Guardian • 17h ago

---

**[Could anything but profit steer AI? The OpenAI trial offered clues but no verdict](https://www.wral.com/news/ap/77674-could-anything-but-profit-steer-ai-the-openai-trial-offered-clues-but-no-verdict/)**

The trial pitting Elon Musk against OpenAI CEO Sam Altman made clear the two billionaires agreed on one thing: building artificial intelligence would require significant resources — and enormous amounts of money.

WRAL • 17m ago

---

**[OpenAI is hiring a $445,000 researcher. Requirements? Be 'tasteful and strategic.'](https://www.businessinsider.com/openai-safety-team-ai-self-improvement-challenge-job-2026-5)**

OpenAI and Sam Altman aim to automate AI research. They are now hiring for a role to prepare the company for self-training AI.

Business Insider • 19h ago

---

**[SpaceX, OpenAI and Anthropic IPOs set to test limits of AI boom](https://www.ft.com/content/ae9bb47d-bd1d-473c-b4c5-abae0420cc12?syn-25a6b1a6=1)**

Elon Musk, Sam Altman and Dario Amodei battle over who can command Wall Street’s deepest pools of capital

Financial Times • 20h ago

---

**[Here's why people are booing college commencement speakers this year](https://www.usatoday.com/story/news/nation/2026/05/23/college-graduation-speakers-booed-ai/90232153007/)**

Multiple college graduations were marked by booing at featured speakers, who came to realize they had "struck a chord." What set the crowd off?

USA Today • 9h ago

---

**[‘F*** this guy’: Graduation speakers keep getting booed for talking about artificial intelligence](https://www.yahoo.com/news/politics/articles/f-guy-graduation-speakers-keep-125456074.html)**

Commencement speakers want new graduates to feel optimistic about artificial intelligence — instead students are booing. New grads tell Josh Marcus that their fury about doddering policymakers and loo...

Yahoo • 15h ago

---

**[Why College Students Are Booing AI](https://www.theatlantic.com/ideas/2026/05/ai-graduation-speeches-booing/687266/)**

The sound of a cosmic howl

The Atlantic • 17h ago

---

**[AI is changing the internet forever. Here’s how](https://www.cnn.com/2026/05/23/tech/ai-internet-search)**

Google is giving the search bar its biggest update in 25 years, another sign that AI is changing the way people use the internet and find information.

CNN • 19h ago

---

**[Microsoft reports are exposing AI's real cost problem: Using the tech is more expensive than paying human employees](https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/)**

Companies are racing to incentivize employees to use AI. But as some companies are finding, the more employees that use the technology, the heavier the bill.

Fortune • 1d ago

---

---

## HackerNews: "ai"

**[AI is just unauthorised plagiarism at a bigger scale](https://news.ycombinator.com/item?id=48222383)**

AI takes in all the input, whether the original authors have consented or not, and do some "learning", and then the AI companies sell these learned result to...

⬆️ 816 • 💬 731 • 2d ago • [Axel's blog](https://axelk.ee/ai-is-just-unauthorised-plagiarism-at-a-bigger-scale/)

---

**[Throwing AI-generated walls of text into conversations](https://news.ycombinator.com/item?id=48219992)**

Stop throwing AI-generated walls of text into conversations. If they wanted an AI essay, they would have asked ChatGPT themselves.

⬆️ 698 • 💬 417 • 2d ago • [noslopgrenade.com](https://noslopgrenade.com/)

---

**[Steve Wozniak cheered after telling students they have AI – actual intelligence](https://news.ycombinator.com/item?id=48233563)**

Apple cofounder Steve Wozniak's speech about AI at Grand Valley State University earlier this month got a laugh and applause from graduates.

⬆️ 640 • 💬 540 • 1d ago • [Business Insider](https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5)

---

**[Shunning AI is the human choice](https://news.ycombinator.com/item?id=48222366)**

LinkedIn may be awash with boosters, but shunning AI is the human choice.

⬆️ 370 • 💬 538 • 2d ago • [The Handbasket](https://www.thehandbasket.co/p/hating-ai-is-good-actually)

---

**[AI has a multiplying effect on existing technical skills](https://news.ycombinator.com/item?id=48235526)**

Friendly articles and tutorials for front-end web developers. ❤️

⬆️ 329 • 💬 309 • 1d ago • [joshwcomeau.com](https://www.joshwcomeau.com/email/wham-launch-005-elephant-2-p/)

---

**[Samsung chip workers will get an average $340k bonus as AI profits soar](https://news.ycombinator.com/item?id=48230892)**

The South Korean chipmaker struck a last-minute deal with its union to avert an 18-day strike, unlocking a $26.6 billion payout pool

⬆️ 251 • 💬 195 • 2d ago • [Quartz](https://qz.com/samsung-chip-workers-bonus-ai-profits-052126)

---

**[Is AI Profitable Yet?](https://news.ycombinator.com/item?id=48243863)**

⬆️ 247 • 💬 194 • 1d ago • [isaiprofitable.com](https://isaiprofitable.com/)

---

**[Italy moves to Airbus A330 tankers](https://news.ycombinator.com/item?id=48248775)**

Rome shifts course: six Airbus A330 MRTT tanker aircraft, worth around €1.39 billion in total, to bolster the European pillar in NATO. #EuropeNews

⬆️ 240 • 💬 95 • 12h ago • [euronews](https://www.euronews.com/my-europe/2026/05/21/italy-moves-to-airbus-a330-tankers-in-major-nato-aligned-shift)

---

**[Microsoft reports AI is more expensive than paying human employees](https://news.ycombinator.com/item?id=48244434)**

Companies are racing to incentivize employees to use AI. But as some companies are finding, the more employees that use the technology, the heavier the bill.

⬆️ 220 • 💬 65 • 1d ago • [Fortune](https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/)

---

**[The Companies Cutting Headcount for AI Will Lose to the Ones Who Didn't](https://news.ycombinator.com/item?id=48234547)**

Organisations using AI to cut headcount are making a short-term trade with long-term consequences. The ones holding their teams together and investing in how those teams operate with AI are building something more durable.

⬆️ 202 • 💬 190 • 1d ago • [libertas.software](https://libertas.software/en/knowledge-hub/19/the-companies-cutting-headcount-for-ai-will-lose-to-the-ones-who-didnt)

---

---

## YouTube Videos: "ai"

**[The singularity is near: Google unveils next phase of AI](https://www.youtube.com/watch?v=zvJ5KfNjOCk)**

ABC News' Nathan Rousseau Smith travels to Google I/O where the search giant unveiled AI agent Gemini Spark, new smart ...

📺 ABC News

👁️ 71K • 👍 1K • 💬 251 • ⏱️ 5:06 • 1d ago

---

**[AI Just Crossed The Line We Were Afraid Of: Continual Harness](https://www.youtube.com/watch?v=qCFyprzrCvA)**

Princeton researchers just revealed Continual Harness, a self-improving AI system that learns while it is already running.

📺 AI Revolution

👁️ 31K • 👍 1K • 💬 166 • ⏱️ 13:31 • 1d ago

---

**[Trump endorsements, AI &amp; nonvoter polling | Enten roundup](https://www.youtube.com/watch?v=SBXbKOwF_TQ)**

CNN chief data analyst Harry Enten runs the numbers, from President Trump's endorsement influence on primaries to opinions on ...

📺 CNN

👁️ 239K • 👍 4K • 💬 1K • ⏱️ 12:06 • 16h ago

---

**[Their AI fix is not what you think ](https://www.youtube.com/watch?v=M_OHsJ8RUGo)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 28K • 👍 2K • 💬 598 • ⏱️ 12:20 • 1d ago

---

**[Google’s AI endgame is here… everything you missed at I/O 2026](https://www.youtube.com/watch?v=9OQ5vaYbGV0)**

Try using Emergent's specialized agents in parallel to build any full-stack application ...

📺 Fireship

👁️ 591K • 👍 19K • 💬 1K • ⏱️ 5:44 • 1d ago

---

**[Joe Rogan accidentally exposed AI in four words](https://www.youtube.com/watch?v=waFl4uBfXRA)**

Token mania. I've been a user of Proton for almost a decade and I'm grateful to them for agreeing to sponsor this video. Proton ...

📺 Mo Bitar

👁️ 184K • 👍 11K • 💬 2K • ⏱️ 11:39 • 1d ago

---

**[Trump posts hilarious AI video of Stephen Colbert being tossed in bin](https://www.youtube.com/watch?v=YaK-QNvjOsg)**

After more than a decade on air, Stephen Colbert has signed off from The Late Show. US President Donald Trump responded on ...

📺 Sky News Australia

👁️ 82K • 👍 4K • 💬 1K • ⏱️ 0:44 • 18h ago

---

**[Don&#39;t Buy AI Bath Bombs](https://www.youtube.com/watch?v=uocwJAi2y_U)**

Get your $10 sign-up bonus at http://privacy.com/pleasantgreen. You can use it on your first purchase! Privacy has a free plan with ...

📺 Pleasant Green

👁️ 319K • 👍 16K • 💬 2K • ⏱️ 10:02 • 15h ago

---

**[Ancient Language Decoded by an AI, What It Revealed Is Shocking!](https://www.youtube.com/watch?v=AoO7mpvgR5U)**

I would love to keep in touch! Click here for more about Origins Explained: https://linktr.ee/originsexplained Check out my Amazon ...

📺 Origins Explained

👁️ 33K • 👍 1K • 💬 137 • ⏱️ 27:36 • 2d ago

---

**[A.I. PSYCHOSIS ......](https://www.youtube.com/watch?v=yVRz8vd4L7U)**

WE TAKE A LOOK AT THE RISING CASES OF A.I. PSYCHOSIS . #ai #mentalhealth #tiktok #viralvideo.

📺 what it look like TV

👁️ 28K • 👍 2K • 💬 743 • ⏱️ 27:41 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 1,227 • ❤️ 711 • 20h ago

---

**[Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)**

*Tencent*

Hy-MT2-1.8B is a fast, 1.8B parameter multilingual translation model supporting 33 languages, optimized for on-device deployment with 1.25-bit quantization (440MB storage, 1.5x speedup). It excels in general, business, and instruction-following translation tasks, outperforming mainstream commercial APIs.

`translation` `2.0B`

⬇️ 2,564 • ❤️ 457 • 1d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 40,368 • ❤️ 619 • 5d ago

---

**[Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)**

*Tencent*

Hy-MT2-30B-A3B is a large-scale (30B parameters, MoE) multilingual translation model supporting 33 languages. It excels in general, business, and instruction-following translation tasks, outperforming leading open-source models and commercial APIs.

`translation` `30.1B`

⬇️ 970 • ❤️ 293 • 1d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 5,283 • ❤️ 270 • 3d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 78,771 • ❤️ 260 • 2d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for on-device image and video understanding, offering strong foundation and multimodal capabilities with mixed visual token compression for flexible speed/accuracy trade-offs.

`image-text-to-text` `1.3B`

⬇️ 247,170 • ❤️ 914 • 4d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, featuring a prompt enhancer for improved input processing and supporting various LTX 2.3 formats.

`text-to-video` `9.0B`

⬇️ 1,286,075 • ❤️ 1,308 • 2d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter causal language model with vision capabilities, optimized for faster inference via MTP. It excels at agentic coding, reasoning, and handling extended contexts up to 1M tokens, making it suitable for complex development workflows and iterative tasks.

`image-text-to-text` `27.3B`

⬇️ 597,584 • ❤️ 438 • 3d ago

---

**[command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)**

*Cohere Labs*

Command A+ is a 25B parameter, multilingual, vision-capable LLM optimized for agentic and reasoning tasks. It supports a 128K context window and offers a W4A4 quantization for efficient enterprise deployment.

`image-text-to-text` `125.8B`

⬇️ 4,261 • ❤️ 186 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 80 • 💬 3 • ⭐ 78,881 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 64,631 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,400 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://huggingface.co/papers/2605.18678)**

*Fengyi Fu, Mengqi Huang, Shaojin Wu et al. (13 authors)*

🏢 bytedance-research

Lance is a unified multimodal model that combines understanding, generation, and editing capabilities for images and videos through collaborative multi-task training and a dual-stream architecture.

▲ 71 • 💬 4 • ⭐ 796 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18678) • [💻 code](https://github.com/bytedance/Lance) • [🔗 project](https://lance-project.github.io/)

---

**[LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://huggingface.co/papers/2605.18739)**

*Yukang Chen, Luozhou Wang, Wei Huang et al. (16 authors)*

🏢 NVIDIA

LongLive-2.0 presents an NVFP4-based parallel infrastructure for long video generation that addresses training and inference bottlenecks through sequence-parallel autoregressive training and diffusion model tuning.

▲ 108 • 💬 3 • ⭐ 1,818 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18739) • [💻 code](https://github.com/NVlabs/LongLive) • [🔗 project](https://nvlabs.github.io/LongLive/LongLive2/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 74,655 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation](https://huggingface.co/papers/2605.19833)**

*Zhifei Xie, Kaiyu Pang, Haobin Zhang et al. (7 authors)*

🏢 National University of Singapore

Mega-ASR framework improves robustness in real-world speech recognition through compound-data construction and progressive acoustic-to-semantic optimization techniques.

▲ 126 • 💬 3 • ⭐ 398 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.19833) • [💻 code](https://github.com/xzf-thu/Mega-ASR) • [🔗 project](https://xzf-thu.github.io/Mega-ASR/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 8 • 💬 0 • ⭐ 18,549 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 4 • 💬 1 • ⭐ 5,596 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 120 • 💬 10 • ⭐ 10,465 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 4.7k • 🔱 486 • 1d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.5k • 🔱 1.1k • 6d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.6k • 🔱 179 • 18m ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.3k • 🔱 386 • 2d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.2k • 🔱 344 • 6d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.0k • 🔱 441 • 2d ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.8k • 🔱 211 • 16d ago

---

**[Nutlope/hallmark](https://github.com/Nutlope/hallmark)**

Anti-AI-slop design skill for Claude Code, Cursor, and Codex.

`CSS`

⭐ 1.8k • 🔱 114 • 3d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.7k • 🔱 184 • 2d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 1.6k • 🔱 115 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
