---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-16T00:11:40.027184+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 16, 2026 at 00:11 UTC  
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

**[Export-banned Nvidia chips are behind China's most powerful AI models — uh-oh, Jensen! | TechCrunch](https://www.reddit.com/r/artificial/comments/1xx4t46/exportbanned_nvidia_chips_are_behind_chinas_most/)**

New research shows the most advanced AI models from China were trained on banned Nvidia chips.

🔗 [TechCrunch](https://techcrunch.com/2026/11/13/export-banned-nvidia-chips-are-behind-chinas-most-powerful-ai-models-uh-oh-jensen/) • 4h ago

---

**[built a fact-checker that catches politicians lying in real-time](https://www.reddit.com/r/artificial/comments/1xwmtff/built_a_factchecker_that_catches_politicians/)**

I've embarrassingly been working on this project for 2 years so wanted to finally share (as I saw others posting Youtube-only versions). on Youtube it transcribes text to identify checkable claims -> web search retrieves sources to base Claude's verdict on, to avoid hallucinated sources. it's a free Chrome extension, and works on news or social media sites as well. let me know what would make this something you'd use, or what else you'd like to see! Edit 2: LogicLens - Chrome Webstore Or iOS if you don't use Chrome (Google = :/). Edit: I realized someone not following could misread the video (here Biden is telling the truth, and Trump was lying, but the Trump section is before I started the recording).

19h ago

---

**[Are AI leaderboards even worth taking seriously anymore?](https://www.reddit.com/r/artificial/comments/1xwwdhv/are_ai_leaderboards_even_worth_taking_seriously/)**

Every time a new AI leaderboard drops theres suddenly a different model being called the best in the world and then you check another benchmark and the rankings are completely different. Gemini has been doing well in general chat rankings while Claude has been strong in coding, so apparently the best AI depends on which website you happen to open that morning. Kalshi even has a market on which AI model finishes November at number one and it got me thinking about how much these rankings actually reflect what people use every day. I mean a model can score high on some benchmark and still give you a garbage answer to a basic question. At this point I’d rather hear from people who use these tools for actual work instead of another company announcing it beat everyone by three points on some test. Has anyone here switched their main AI because of these rankings or are we just watching companies fight over numbers that barely change the experience?

10h ago

---

**[Weight-space programming: an LLM edited another model's weights directly and lifted its math score from 7.9% to 48.1%](https://www.reddit.com/r/artificial/comments/1xx4kit/weightspace_programming_an_llm_edited_another/)**

MIT researchers (Rikiya Takehi, Jayden Teoh, Alex Zhang, Omar Khattab) had OpenAI's GPT-6 Astra edit the weights of a small Qwen model directly -- no gradient descent, no training data. Astra found the pattern behind the model's habit of repeating itself until it ran out of context, and removed it. The edit touched about 0.016% of the weights; the model's math score went from 7.9% to 48.1%. Three papers on the method landed on arXiv on November 6 (e.g. arXiv:2611.09382). Other demonstrations from the same batch: editing only 1,023 parameters improved an LLM by 29.45 points on MATH-500; Astra debugged robot policies by editing 65 token-embedding rows; and a Breakout-playing network built from the game's rules, with no training at all, outscored one trained for 500 million steps (517.4 vs 25.3). Some important caveats: the gain came mostly from fixing a bad habit, not from adding math knowledge -- before the edit 93% of the model's math answers hit the length limit, after it 33.1%. On a small Gemma model that rarely repeated itself, there was no established math gain. The original claim also drew a detailed rebuttal (Matthew Honnibal argued it was overstated), though Simon Willison then reproduced weight editing locally with Qwen 3.8 27B on his laptop. Independent reproduction of the headline results is still pending. What interests me most is the framing: this is model repair by direct surgery rather than training. If it generalizes, debugging a model could start to look like debugging code -- find the weights responsible, patch them, verify. But it also raises the question of how much of a model's capability is locked up behind fixable quirks rather than missing knowledge. Where do you think this goes? A practical tool for model maintenance, a narrow trick that only works on pathological repetition, or the start of something bigger?

4h ago

---

**[made up 9 software brands and asked chatgpt and google ai mode for each one's price and founder, to see if they'd invent answers. 18 answers, none invented](https://www.reddit.com/r/artificial/comments/1xwzvr9/made_up_9_software_brands_and_asked_chatgpt_and/)**

Everyone's complaining ai just makes stuff up (commonly: "hallucinates") and in public scoreboards they range from 1.8% to 77% based on what they're testing, etc. so we wondered if either one of them would invent something in a simple, verifiable question. We made up 9 names of software companies (zero product found with a google search for any of them) and Oct 19th queried both chatgpt and google ai mode (ie: google's chat answers) for the price and founder of each 18 answers, 0 made up Chatgpt couldn't verify it existed and asked for a website every time google ai mode said it didn't exist, and often suggested another product that existed (similar name), including one cosplay-design company, thimble forge. so we started with 10 names. cut 1 out. chatgpt found an hr document product called corvanta and ai mode found a brand of ambulance software. so, the name existed. taken by someone. and then with the real companies (26 of them). asked for founding year and HQ. checked on wikipedia. each question asked both. famous companies - 19/20. mid sized - 14/14. lesser known - 14/18. 5 missed - all sources that were contradicting. both engines - lexalytics = amherst. chatgpt cited its linkedin. wikipedia - boston. dbmaestro = chatgpt - 2008. came from israeli startup database. wikipedia + ai mode - 2012 and we asked for the price of the most affordable paid plan for 8 saas tools. checked vs vendor pricing page for the day. 16/16 - headline price (the price that's shown first on the page). misses were in price for monthly billing. when there was a toggle monthly/annual. capsule crm. small biz crm. chatgpt - $22 monthly. sourced from 2 sites with reviews. ai mode - $21. vendor page shows annual by default. and chatgpt showed insightly = $35 on monthly. could not find it on the pricing page. all plans are billed annually. They chose a side when sources were different on basic facts (with internet access). They didn't make up their own. It's not the same as what the public scoreboards test (document summarization or deep questions without documents), which is why those numbers swing so much. One question. One us location. One day. One correct answer per question. We didn't try more complex things (like product integrations or a comparison of two tools.) Anyone have a fantasy name that'll make either of them go along?

7h ago

---

**[Question about governments bailouts](https://www.reddit.com/r/artificial/comments/1xxaco3/question_about_governments_bailouts/)**

29m ago

---

**[Meituan open-sourced LongCat-2.5, a 1.6T agent model, and the only deploy guide is for Huawei NPUs, not Nvidia](https://www.reddit.com/r/artificial/comments/1xwx2hc/meituan_opensourced_longcat25_a_16t_agent_model/)**

Meituan just released the LongCat-2.5 weights under MIT: 1.6T total parameters, about 48B active per token, with text, image and video input. On their own table it scores 88.4 on Terminal Bench v2.1, right next to Claude Opus 5 at 89.1. On the harder Terminal Bench v4.0 the gap opens up: 38.5 vs 53.9 for Opus 5. The catch if you want to self-host is that the model card only documents NPU deployment, with no Nvidia path yet. As someone who builds small web projects, what I care about is that the API speaks both OpenAI and Anthropic formats, so testing it inside an existing agent setup is cheap. Has anyone run it in a real coding agent loop yet, and does it hold up outside the benchmarks? Source: https://huggingface.co/meituan-longcat/LongCat-2.5

9h ago

---

**[Building with AI is now easier but trust takes further testing.](https://www.reddit.com/r/artificial/comments/1xwwrm0/building_with_ai_is_now_easier_but_trust_takes/)**

I think this is a subject that should be discussed in detail, with more and more builders shipping products with AI who’s is actually testing them?

🔗 [CrashTest AI](https://crashtestingai.com/lab-notes/building-is-easier-trust-is-harder/) • 9h ago

---

**[Anthropic rebuilds Claude Code Projects around a coordinator and parallel worker threads - each thread is a full cloud session on its own branch](https://www.reddit.com/r/artificial/comments/1xwj3v0/anthropic_rebuilds_claude_code_projects_around_a/)**

Anthropic posted an update on Nov 14 rebuilding Claude Projects from a folder of files into a coordinated set of working sessions. You describe the work in one conversation; a coordinator scopes it, delegates it to parallel threads, reviews the outputs and assembles the result. Each thread is a Claude Code cloud session with its own copy of the repo and its own Git branch, and it can split its task further into subagents, loops or workflows. The work keeps going after you close your laptop, and you can steer it from your phone. It is a public beta rolling out gradually to select Pro/Max/Ultra subscribers who use Claude Code cloud sessions; Team and Enterprise plans do not have it yet, and there is a waitlist for everyone else. Anthropic is upfront about the limits: threads run only in the cloud for now (local code and VPN support is coming 'very soon'), several parallel sessions burn through usage limits faster, and if two threads touch the same code it surfaces as an ordinary merge conflict in a PR. Sources: Anthropic's product post (claude.com/blog/projects-redesigned) and the Projects docs (code.claude.com/docs/en/claude-projects). What I am curious about: does parallelizing agents actually speed up real work, or does it just move the bottleneck to review and merge conflicts? Has anyone here tried the beta?

22h ago

---

**[NVidea Drivers for Linux](https://www.reddit.com/r/artificial/comments/1xx6k88/nvidea_drivers_for_linux/)**

Why hasn't anyone reverse-engineered the proprietary NVIDIA drivers for Linux yet, to improve them and make them open source?

3h ago

---

---

## Google News: "ai"

**[How Jensen Huang Built the Backdoor Route That Keeps Beijing in the AI Race](https://www.wsj.com/tech/jensen-huang-backdoor-ai-data-centers-a5e4499d)**

WSJ • 14h ago

---

**[‘Jensen Huang lost his mind’: how AI’s smartest man fell for the world’s oldest trick](https://www.theguardian.com/technology/2026/nov/14/jensen-huang-affair-nvidia-nightmare)**

Jensen Huang’s affair with a suspected spy is Silicon Valley’s worst nightmare come true

The Guardian • 5h ago

---

**[Jensen Huang: Silicon Valley experts analyze how recent Nvidia scandals could impact AI ecosystem](https://abc7news.com/post/jensen-huang-silicon-valley-experts-analyze-how-recent-nvidia-scandals-could-impact-ai-ecosystem/20042732/)**

Nvidia is known as a global leader in making advanced AI chips. But many experts point out that Nvidia is also the bank that funds a lot of AI startups in Silicon Valley, and they are watching to see how the recent scandal may impact the AI ecosystem.

ABC7 Bay Area • 44m ago

---

**[160 questions, only one wrong: top scorer in South Korea tax exam admits AI cheating](https://www.theguardian.com/technology/2026/nov/15/ai-cheating-south-korea-college-entrance-exam)**

Fears for national college entrance exam next week as test taker admits sending photos of questions to AI tool

The Guardian • 4h ago

---

**[153-Year-Old Builder Taisei Sets Up Fund to Invest in AI and Robotics](https://www.bloomberg.com/news/articles/2026-11-15/taisei-launches-150-million-ai-robotics-fund-with-pegasus-tech-ventures)**

Bloomberg.com • 1h ago

---

**["Gotcha," the reporter quipped. "Don't trust AI." …](https://sports.yahoo.com/articles/gotcha-reporter-quipped-dont-trust-223655365.html)**

"Gotcha," the reporter quipped. "Don't trust AI." …

Yahoo Sports • 1h ago

---

**[Is everything just broken? Grounded jets, Microsoft outage, AI chaos have some wondering](https://www.latimes.com/world-nation/story/2026-11-15/grounded-jets-microsoft-outage-ai-chaos-is-everything-broken)**

After the Silicon Valley chaos spurred by reports of an AI billionaire's affair with a suspected Chinese spy and the Microsoft outage that upended millions of workers' days, Friday's air travel ground stop across the U.S. had many people feeling that something was up.

Los Angeles Times • 1h ago

---

**[Anthropic’s IPO lands as the embattled AI trade looks for a much-needed bright spot](https://www.cnbc.com/2026/11/15/anthropic-ipo-is-make-or-break-for-the-technology-industry.html)**

Anthropic's IPO has outsized importance in the tech industry, which is heavily invested in the AI lab and is desperate for some positive momentum.

CNBC • 12h ago

---

**[The SpaceX IPO Had Musk’s Star Power. Anthropic’s Has FOMO.](https://www.wsj.com/finance/stocks/the-individual-investors-who-are-hot-on-anthropics-ipo-but-cool-on-ai-461f89b4)**

WSJ • 13h ago

---

**[Anthropic’s giant IPO puts the heat on OpenAI](https://www.economist.com/business/2026/11/15/anthropics-giant-ipo-puts-the-heat-on-openai)**

The Economist • 4h ago

---

---

## HackerNews: "ai"

**[Nvidia allegedly engineered scarcity by funding AI startups to buy its GPUs](https://news.ycombinator.com/item?id=50493251)**

Following the departure of now-former NVIDIA CEO, Jensen Huang, a new report by The Wall Street Journal (via Wccftech) has emerged alleging that NVIDIA artificially inflated the ongoing GPU and memory shortage by investing in AI startups that would go on to buy NVIDIA GPUs and build data centers....

⬆️ 1098 • 💬 646 • 1d ago • [TechPowerUp](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus)

---

**[All AI-generated code should be Open Source](https://news.ycombinator.com/item?id=50507303)**

All code generated with help from AI should be Open Source or on Creative Commons Zero (CC0) license.

⬆️ 1054 • 💬 577 • 9h ago • [Jakub T. Jankiewicz Blog](https://jakub.jankiewicz.org/blog/ai-code-open-source/)

---

**[Elevated errors on claude.ai, Claude Code, and platform.claude.com](https://news.ycombinator.com/item?id=50481187)**

Claude's Status Page - Elevated errors on claude.ai, Claude Code, and platform.claude.com.

⬆️ 493 • 💬 390 • 2d ago • [status.claude.com](https://status.claude.com/incidents/nn11wk485zfn)

---

**[Jonathan Blow – If AI solved coding, why is my software still the same? [video]](https://news.ycombinator.com/item?id=50484658)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 482 • 💬 724 • 2d ago • [youtube.com](https://www.youtube.com/watch?v=IRK8h67ol7Q)

---

**[AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems](https://news.ycombinator.com/item?id=50486748)**

Kurt Gödel left 1,009 pages of densely written text – much of it in an obsolete shorthand – which is now said to contain hundreds of proved theorems

⬆️ 438 • 💬 110 • 2d ago • [the Guardian](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths)

---

**[AI is destroying the trust between writers and readers](https://news.ycombinator.com/item?id=50481870)**

⬆️ 369 • 💬 234 • 2d ago • [theatlantic.com](https://www.theatlantic.com/books/2026/11/ai-literary-scams-amazon/689391/)

---

**[Live airband on all frequencies from KORS. Victoria, CA also ground stopped](https://news.ycombinator.com/item?id=50490593)**

Every aviation radio transmission heard from Orcas Island, WA: live, transcribed, and archived. Listen to all channels at once, pick your own, or rewind to any moment.

⬆️ 293 • 💬 70 • 2d ago • [orcasairband.com](https://orcasairband.com/)

---

**[No AI Slop: A Manifesto](https://news.ycombinator.com/item?id=50488769)**

The No AI Slop Manifesto, from the speakers and attendees of AIE Code Summit 2026.

⬆️ 222 • 💬 133 • 2d ago • [slopmanifesto.com](https://www.slopmanifesto.com/)

---

**[All US airports are currently ground stopped](https://news.ycombinator.com/item?id=50489652)**

Issued by the FAA just moments ago, ALL US airports are currently ground stopped. This means NO flights may depart for US airports. Flights already in the air will be allowed to land. This is related to an FAA equipment outage.

⬆️ 213 • 💬 44 • 2d ago • [X (formerly Twitter)](https://twitter.com/flightradar24/status/2121347654714077605)

---

**[Why is Google cutting off Search from AI-free schools? Here are some theories](https://news.ycombinator.com/item?id=50484960)**

⬆️ 195 • 💬 196 • 2d ago • [text.npr.org](https://text.npr.org/nx-s1-6029408)

---

---

## YouTube Videos: "ai"

**[The AI Bubble Bursts Tomorrow. Here&#39;s What Happens.](https://www.youtube.com/watch?v=u-Shem6Qe2g)**

In three months, Alphabet spent $51 billion on data centers, servers and chips, more than its business brought in. Meta is in the ...

📺 The Bigger Board

👁️ 16K • 👍 316 • 💬 92 • ⏱️ 22:58 • 7h ago

---

**[The AI Layoff Apocalypse](https://www.youtube.com/watch?v=gIM1PcaUSI8)**

Upgrade Your Workspace with HBADA E3 Ultra. Discover the new HBADA E3 Ultra Ergonomic Chair, designed to bring comfort ...

📺 Cole Hastings

👁️ 54K • 👍 689 • 💬 208 • ⏱️ 19:40 • 7h ago

---

**[Musk Makes MASSIVE AI Move After Midterm Disaster](https://www.youtube.com/watch?v=FaErjxv_nlE)**

Elon Musk wants to pour more than $74 billion into building data centers in Arizona and Texas. Keith Edwards, John Iadarola and ...

📺 The Young Turks

👁️ 149K • 👍 2K • 💬 520 • ⏱️ 16:37 • 1d ago

---

**[Finally! China Just Dropped NEW FREE AI Video Tools to Challenge Higgsfield!](https://www.youtube.com/watch?v=UJ0Qh4BCzok)**

WANT ALL 3 TOOLS + MY EXACT PROMPTS? Join my Discord community to get access to all three platforms, the exact prompts ...

📺 Becky the Ai Girl

👁️ 2K • 👍 70 • 💬 6 • ⏱️ 13:00 • 7h ago

---

**[I Made VIRAL 3D Animation Videos Using ONLY Claude AI (FREE Plugin)](https://www.youtube.com/watch?v=Gu9lO8oqGYU)**

What if you could create viral 3D stickman animations using AI, even with no animation experience? In this tutorial, I'll show you ...

📺 Jacksons AI

👁️ 47K • 👍 1K • 💬 982 • ⏱️ 25:20 • 21h ago

---

**[Recursive self-improvement has started](https://www.youtube.com/watch?v=1NHPDzpfR6Y)**

If you asked me earlier this year how far away we are from superintelligence, I'd probably have said at least the better part of a ...

📺 Dwarkesh Patel

👁️ 571K • 👍 9K • 💬 2K • ⏱️ 44:27 • 2d ago

---

**[AI Closes In on the Riemann Hypothesis | World Science Festival](https://www.youtube.com/watch?v=ljFZfYZLHj8)**

AI just took an unprecedented step toward solving what is arguably math's most towering problem: to prove the Riemann ...

📺 World Science Festival

👁️ 283K • 👍 3K • 💬 388 • ⏱️ 1:31:50 • 2d ago

---

**[I Read 130 Studies on AI Jobs: Here Is What They Didn&#39;t Tell You](https://www.youtube.com/watch?v=0U4r8zRwpMs)**

Thanks to Monarch for partnering with me! Start your free trial and get 50% off your first year of total money clarity using my link ...

📺 Brendan Dell 

👁️ 71K • 👍 1K • 💬 394 • ⏱️ 29:51 • 1d ago

---

**[AI News: Things Will Never Be The Same](https://www.youtube.com/watch?v=G_Jrexy_5Bg)**

Try @OpenAI Decisions API here: https://developers.openai.com/api/docs/guides/decisions Here's the AI news from one of the ...

📺 Matt Wolfe

👁️ 152K • 👍 2K • 💬 262 • ⏱️ 27:11 • 2d ago

---

**[My Pet Is the WOLF KING?! He Was Cursed Into a Puppy… Until TRUE LOVE Changed Everything!#AIStory](https://www.youtube.com/watch?v=jRa3_WZYDdY)**

If you enjoy billionaire stories, mafia dramas, CEO revenge, action thrillers, and cinematic AI storytelling, you're in the right place.

📺 Nov Drama

👁️ 224K • 👍 5K • 💬 170 • ⏱️ 1:41:19 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)**

*Colonel Panic*

`text-generation` `9.4B`

⬇️ 27,037 • ❤️ 7,528 • 3d ago

---

**[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)**

*MiniMax*

`text-to-image`

⬇️ 571,067 • ❤️ 1,182 • 3d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,547,772 • ❤️ 20,118 • 8d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 2,754,355 • ❤️ 12,057 • 1mo ago

---

**[MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image)**

*Comfy Org*

`text-to-image`

⬇️ 1,973,388 • ❤️ 411 • 4d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

`image-text-to-text` `26.9B`

⬇️ 1,708,637 • ❤️ 3,168 • 2d ago

---

**[ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini)**

*Zyphra*

`text-to-speech` `886.3M`

⬇️ 39,862 • ❤️ 392 • 1d ago

---

**[Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small)**

*Thinking Machines Lab*

`image-text-to-text` `594.1B`

⬇️ 7,329 • ❤️ 343 • 18h ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

`27.3B`

⬇️ 6,566,295 • ❤️ 5,998 • 3d ago

---

**[idol](https://huggingface.co/speridlabs/idol)**

*speridlabs*

Idol is an image-to-3D model that generates a 3D Gaussian splat representation from a single input image. It supports both real photographs and synthetic renders, producing up to 1,048,576 Gaussians in under 2 seconds on consumer GPUs, ideal for rapid 3D asset creation.

`image-to-3d`

⬇️ 33,423 • ❤️ 2,364 • 17d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 31 • 💬 9 • ⭐ 11,685 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 166 • 💬 6 • ⭐ 122,697 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 3 • 💬 0 • ⭐ 801 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 16 • 💬 2 • ⭐ 6,243 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 70 • 💬 4 • ⭐ 23,945 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**

*Bing Han, Yichuan Peng, Haoyu Dong et al. (19 authors)*

🏢 Robbyant

LingBot-Touch is a tactile foundation model that learns a unified, extensible representation across heterogeneous tactile sensors, yielding plug-and-play tactile tokens that consistently enhance manipulation policies such as diffusion policy and VLA models.

▲ 104 • 💬 2 • ⭐ 605 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2611.12806) • [💻 code](https://github.com/Robbyant/lingbot-touch) • [🔗 project](https://technology.robbyant.com/lingbot-touch)

---

**[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**

*Lorenz K. Muller, Philippe Bich, Chiara Boretti et al. (6 authors)*

🏢 HUAWEI Computing Systems Lab

MACaQ is an MXFP4 W4A4 post-training quantization method that quantizes each linear layer independently using online activation transforms and Hessian-aware refinement, reducing cost while preserving accuracy across language and diffusion models.

▲ 30 • 💬 2 • ⭐ 300 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2611.10649) • [💻 code](https://github.com/huawei-csl/MACaQ) • [🔗 project](https://huawei-csl.com/blog/macaq/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 77 • 💬 1 • ⭐ 86,094 • 38mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 65 • 💬 5 • ⭐ 47,844 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[e-means: outperforming k-means (in one-tenth the epochs)](https://huggingface.co/papers/2611.09501)**

*Swann Bessa, Pierre-Emmanuel Mazaré, Gergely Szilvasy et al. (7 authors)*

🏢 Meta

Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning machinery and new insights. We also establish scaling laws on how decay rate and batch size impact final performance. This gives us a formulaic rule to fix them for multiple problem sizes and embedding datasets, without the need for any hyperparameter sweep. The resulting clustering algorithm, coined e-means, is much faster than Lloyd k-means and converges to lower losses, frequently even beating k-means++. On a wide array of embeddings datasets, it beats the loss of Lloyd k-means at 25 epochs in 1.4 to 2.6 epochs, which translates to 10-45x GPU wall-clock speedups compared to state-of-the-art k-means implementations. As an example, e-means partitions DINO10B, a dataset of 10 billion DINO embeddings, into 16 million clusters in only 2.5 epochs, reaching a loss below Lloyd's at 25 epochs.

▲ 13 • 💬 3 • ⭐ 41,706 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2611.09501) • [💻 code](https://github.com/facebookresearch/faiss) • [🔗 project](https://e-means.github.io/)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 19.7k • 🔱 2.0k • 17d ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 16.7k • 🔱 971 • 23h ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 9.2k • 🔱 1.4k • 15h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 8.7k • 🔱 2.0k • 4h ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 8.1k • 🔱 706 • 5h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.0k • 🔱 1.8k • 11d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 5.8k • 🔱 714 • 6h ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 4.3k • 🔱 113 • 6m ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 4.1k • 🔱 60 • 4h ago

---

**[benjitaylor/skills](https://github.com/benjitaylor/skills)**

Skills for AI coding agents.

`TypeScript`

⭐ 3.4k • 🔱 229 • 10d ago

---

---

*Generated by PeekDeck - A glance is all you need*
