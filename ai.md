---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-27T00:08:37.432263+00:00'
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

**Last Updated:** June 27, 2026 at 00:08 UTC  
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

**[Google keeps losing top ai researchers, the moat was never the weights](https://www.reddit.com/r/artificial/comments/1ugbwol/google_keeps_losing_top_ai_researchers_the_moat/)**

Shazeer to openai, then John Jumper (the alphaFold nobel guy) to anthropic, plus Adler and Pritzler out the same door within a week. Every time one of these drops the framing is google is bleeding. I think people are reading it backwards. If the people who actually trained the thing can leave and instantly matter at a competitor, the weights were never the asset. The judgment about how to steer a model, what to eval it on, where it breaks, that stuff lives in heads not in checkpoints. Hardware you can buy. That you cannot. What it means for the rest of us is simpler than the talent drama. If capability is going to keep walking between labs every few months, betting your whole stack on one provider's model is a bet on that lab keeping its people, which is the one thing you cannot control. I stopped caring which lab is quote winning this quarter. The move is keeping the model layer swappable so a shakeup at one place does not strand the work. Mine runs through verdent with byok but honestly any setup that lets you reroute works, the point is not the tool, it is not being married to one model.

7h ago

---

**[do you think ai will add more jobs than it will cut over the long run?](https://www.reddit.com/r/artificial/comments/1ugki2w/do_you_think_ai_will_add_more_jobs_than_it_will/)**

if so, what would these jobs look like?

2h ago

---

**[i analyzed 500+ companies job postings to see what new roles are emerging due to ai](https://www.reddit.com/r/artificial/comments/1ugkq6h/i_analyzed_500_companies_job_postings_to_see_what/)**

i kept seeing doomer posts talking about how ai is going to take away all jobs. i believe in the opposite - ai is going to add more jobs in the long term than it cuts, and i kept seeing evidence of that now. there were job titles i'd come across that 2-3 years were much more niche. i got curious to map this out so i created a site to track this. i scraped various job boards and filtered out titles which have exploded since 2022 thanks to ai and if you go through the onboarding, it'll match you to roles you are eligible for. i don't want this post to just be a promo so here are the top 5 roles we are seeing break out. the number in brackets is the number of such jobs we are tracking ai trainer / data annotation (1,218) forward-deployed engineer (485) ai solutions eng / architect (316) agent (engineer/pm/research) (260) applied-ai engineer (169) if you're interested in checking out the site for more roles/jobs you can check it out here: https://alterwork.com/roles any feedback would be great, thanks

1h ago

---

**[Anthropic just published data showing 35% of their users expect AI to do MOST of their work within 12 months. We’re not having an honest conversation about what this actually means.](https://www.reddit.com/r/artificial/comments/1ugaq5b/anthropic_just_published_data_showing_35_of_their/)**

Anthropic dropped their June 2026 Economic Index today and buried inside the survey data is something that should be making headlines: Over a third of respondents (9,700 actual Claude users, linked to real usage data) believe AI will be capable of handling most or nearly all of their work tasks within the next year. Not “some tasks.” Not “help me write emails.” MOST of their work. And here’s the part nobody wants to talk about: the people who delegate the most to AI are the MOST optimistic about their job prospects. Meanwhile entry-level workers are the ones most worried about displacement. Senior devs and managers? Thriving. Junior colleagues? Everyone in the survey is more worried about them than themselves. The data also shows AI autonomy is measurably higher on Claude Code than on regular chat, across 26 out of 31 output types. A blog post that takes 13 rounds of back-and-forth on Claude.ai? Claude Code does it in a single prompt. So here’s the uncomfortable question nobody wants to ask: Are we witnessing the largest skill-premium compression in history, where the gap between a senior person using AI and a junior person using AI collapses the value of experience? Or is this actually fine and we’re all just catastrophizing? Because Anthropic’s own framing spins this as “augmentation not displacement” while simultaneously showing that 38% of people who think they’ll lose their job attribute that directly to AI. Make it make sense. Full report: https://www.anthropic.com/research/economic-index-june-2026-report

8h ago

---

**[The underrated part of open weight models isn't running them local, it's being allowed to build on top off them](https://www.reddit.com/r/artificial/comments/1ug6v99/the_underrated_part_of_open_weight_models_isnt/)**

Most of the open vs closed talk here is about whether you can run the thing on your own hardware. fair, that's the obvious draw. but the part i think gets slept on is that open weights mean you can actually post train on top of the base, not just run inference. With a closed api you're renting intelligence. you can prompt it, you can rag around it, but you can never make it yours. you cant fine tune the actual weights for your domain, you cant distill it down, you cant freeze a version and own it forever. You're permanently downstream of whatever the provider decides. I saw some post about people post training their own models on top of glm-5.2 now that its open weight, and that framing stuck with me more than the benchmark numbers did. a frontier-ish base you can legally build on changes what a small team can do. You dont need to train from scratch, you start from something already strong and specialize it. Realistically most of us arent fine tuning a 700b model in our basement, the compute is brutal and i wont pretend otherwise. but the option existing at all is the point. even renting cloud compute to post train your own variant is a completely different thing than being locked out of the weights entirely. Anyone here actually post training on top of the bigger open models, or is it still mostly inference and the fine tuning stays in the small model range?

10h ago

---

**[Claude Plays World of ClaudeCraft](https://www.reddit.com/r/artificial/comments/1ug2wc9/claude_plays_world_of_claudecraft/)**

Two weeks ago we built World of ClaudeCraft, a free, open-source browser MMO that was built in 48 hours with Claude. We decided to make the experiment recursive: we built a Claude Code-powered VTuber and put her inside the game. Day 1 is live here: https://www.twitch.tv/claudeplaysclaudecraft Claude decides what to do next, sends actions to the game, and speaks through the VTuber avatar (using Elevenlabs for TTS). We’re streaming the run unedited, including the wandering, party joining, emoting and socialising. She can freely interact with the twitch chat and the real people actually in game right now. The game is free to play and open source at https://github.com/levy-street/world-of-claudecraft Hope you enjoy the spectacle!

13h ago

---

**[Europe’s doomsday AI scenario comes alive](https://www.reddit.com/r/artificial/comments/1ug0ojq/europes_doomsday_ai_scenario_comes_alive/)**

A group of European AI researchers have used a fictional narrative to warn against a worst-case scenario for how technology lags could shatter Euro...

🔗 [The Parliament Magazine](https://www.theparliamentmagazine.eu/news/article/europes-doomsday-ai-scenario-comes-alive) • 15h ago

---

**["Why big AI labs are hiring so many philosophers. The technology presents all sorts of thorny problems—a philosopher’s favourite kind"](https://www.reddit.com/r/artificial/comments/1ugd32y/why_big_ai_labs_are_hiring_so_many_philosophers/)**

🔗 [economist.com](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers) • 6h ago

---

**[OpenAI absolutely HUMILIATES claude MYTHOS 5 in the trust me bro benchmarks with their new GPT-5.6 Sol](https://www.reddit.com/r/artificial/comments/1ugnhft/openai_absolutely_humiliates_claude_mythos_5_in/)**

just now

---

**[We put a design question to ten models: what’s the best way to reach a correct answer? They didn’t take a side — they prescribed the right tool for each kind of question. RoundTable already had one. So we built the other.](https://www.reddit.com/r/artificial/comments/1ugn627/we_put_a_design_question_to_ten_models_whats_the/)**

We asked ten models the best way to reach a correct answer. They prescribed two tools — debate for the decisions that matter, a grounded fact-checker for the facts — and we built the second. Inside RoundTable's new Check mode.

🔗 [reports.thert.ai](https://reports.thert.ai/the-council-wrote-the-spec) • 13m ago

---

---

## Google News: "ai"

**[U.S. government will decide who gets to use latest upgrade to ChatGPT](https://www.washingtonpost.com/technology/2026/06/26/openai-says-us-government-will-vet-users-its-latest-ai-model/)**

The Trump administration came to power preaching a laissez-faire approach to AI but has lately increased oversight of the industry.

The Washington Post • 5m ago

---

**[OpenAI Leans Toward Holding Up I.P.O. Until Next Year](https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html)**

The New York Times • 1d ago

---

**[AI trade hits a wall amid report that OpenAI will delay IPO until 2027](https://finance.yahoo.com/technology/article/ai-trade-hits-a-wall-amid-report-that-openai-will-delay-ipo-until-2027-150642366.html)**

Tech stocks slid as the New York Times reported OpenAI could delay its IPO until 2027.

Yahoo Finance • 9h ago

---

**[Apple, Micron, OpenAI and A.I.’s Rough Summer](https://www.nytimes.com/2026/06/26/business/dealbook/ai-openai-ipo-slump.html)**

The New York Times • 12h ago

---

**[The AI backlash is only getting started](https://www.economist.com/leaders/2026/06/25/the-ai-backlash-is-only-getting-started)**

The Economist • 1d ago

---

**[New Illinois laws starting July 1, 2026: Cocktails-to-go, AI bullying, prediction market regulation and more](https://www.cbsnews.com/chicago/news/new-illinois-laws-july-1-2026-cocktails-ai-bullying-prediction-market-regulation/)**

Fourteen new laws will go into effect in Illinois on July 1, 2026.

CBS News • 12m ago

---

**[Papyrus scroll burnt to a crisp during Vesuvius eruption deciphered with help of AI](https://www.cnn.com/2026/06/26/science/papyrus-scroll-vesuvius-ai-scli-intl)**

A papyrus scroll that was burned and carbonized when Mount Vesuvius erupted almost 2,000 years ago has been virtually unrolled and partially deciphered with the help of artificial intelligence.

CNN • 10h ago

---

**[Oracle stock has worst week since 2001 dot-com bust as AI financing concerns escalate](https://www.cnbc.com/2026/06/26/oracle-stock-ends-worst-week-since-2001-as-investors-dwell-on-finances.html)**

Oracle's surging spending, negative free cash flow and $130 billion debt pile are weighing on the stock.

CNBC • 3h ago

---

**[The AI price shock is here: Apple and Microsoft hike prices](https://www.axios.com/2026/06/26/apple-microsoft-prices-ai)**

Axios • 15h ago

---

**[Exclusive / Threats to US payment rails helped trigger Bessent’s AI worries](https://www.semafor.com/article/06/26/2026/bessent-engaged-on-ai-following-warnings-about-fed-payment-rails)**

Advanced models have heightened banks’ fears of an outage that would hamstring their ability to send money.

Semafor • 7h ago

---

---

## HackerNews: "ai"

**[Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://news.ycombinator.com/item?id=48664814)**

⬆️ 789 • 💬 1284 • 2d ago • [reuters.com](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)

---

**[Ford AI hiccups push carmaker to rehire ‘gray beard’ inspectors](https://news.ycombinator.com/item?id=48674446)**

⬆️ 595 • 💬 320 • 1d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-06-25/ford-has-been-rehiring-quality-inspectors-after-ai-fell-short)

---

**[RubyLLM: A Ruby framework for all major AI providers](https://news.ycombinator.com/item?id=48660711)**

A single, beautiful Ruby framework for all major AI providers. Easily build chatbots, AI agents, RAG applications, content generators, and every AI workflow you can think of.

⬆️ 445 • 💬 82 • 2d ago • [RubyLLM](https://rubyllm.com/)

---

**[Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion](https://news.ycombinator.com/item?id=48675435)**

Beautiful, AI-native markdown editor and LLM Wiki. Contribute to inkeep/open-knowledge development by creating an account on GitHub.

⬆️ 361 • 💬 168 • 1d ago • [GitHub](https://github.com/inkeep/open-knowledge)

---

**[What happened after 2k people tried to hack my AI assistant](https://news.ycombinator.com/item?id=48681687)**

⬆️ 350 • 💬 158 • 21h ago • [fernandoi.cl](https://www.fernandoi.cl/posts/hackmyclaw/)

---

**[Apple to skip high-end M6 Mac chips in favor of AI-focused M7 line](https://news.ycombinator.com/item?id=48676795)**

⬆️ 305 • 💬 355 • 1d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-06-25/apple-to-skip-high-end-m6-mac-chips-to-launch-m7-pro-m7-max-m7-ultra-instead?embedded-checkout=true)

---

**[Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'](https://news.ycombinator.com/item?id=48658647)**

The LinkedIn co-founder and investor in both Anthropic and OpenAI offers his most pointed public assessment yet of Elon Musk's AI ambitions.

⬆️ 236 • 💬 269 • 2d ago • [Fortune](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)

---

**[For most of the world, open-source AI is the only way forward](https://news.ycombinator.com/item?id=48660839)**

Proprietary AI is both too expensive and too centralized in control for most countries and companies to rely upon.

⬆️ 233 • 💬 144 • 2d ago • [Techstrong.ai](https://techstrong.ai/articles/for-most-of-the-world-open-source-ai-is-the-only-way-forward/)

---

**[AI children's books, body horror edition](https://news.ycombinator.com/item?id=48681250)**

⬆️ 203 • 💬 77 • 22h ago • [lcamtuf.substack.com](https://lcamtuf.substack.com/p/ai-childrens-books-body-horror-edition)

---

**[Political bias in AI: Where the AI models stand](https://news.ycombinator.com/item?id=48672779)**

Political bias in AI measures where every major AI model stands on charged political and ethical questions: run many times, no web search, plotted with error...

⬆️ 167 • 💬 299 • 1d ago • [Trakkr](https://trakkr.ai/bias)

---

---

## YouTube Videos: "ai"

**[AI News: The New Model That&#39;s As Good As Fable](https://www.youtube.com/watch?v=zMVZvgCOr40)**

Stop losing money on separate AI subscriptions. Get ChatGPT, Claude, Gemini, and 200+ models in one place for one price with ...

📺 Matt Wolfe

👁️ 18K • 👍 1K • 💬 90 • ⏱️ 20:01 • 6h ago

---

**[The AI Future No One Wants to Talk About](https://www.youtube.com/watch?v=zWQe2Fn--Eg)**

Go to https://ground.news/sabine to get 40% off the Vantage plan and see through sensationalized reporting. Stay fully informed ...

📺 Sabine Hossenfelder

👁️ 289K • 👍 18K • 💬 3K • ⏱️ 12:14 • 2d ago

---

**[Why South Korea’s AI Stock Mania Is a Warning to the World](https://www.youtube.com/watch?v=jJrEnv1IDvg)**

South Korea's stock market has surged about 200% year-on-year, powered by retail investors chasing an artificial ...

📺 Bloomberg Originals

👁️ 184K • 👍 3K • 💬 319 • ⏱️ 9:20 • 16h ago

---

**[Every FREE &amp; UNLIMITED AI Video Tool in ONE Place](https://www.youtube.com/watch?v=tsDubocT5Gg)**

Try Base44 and build your own AI tools hub from a single prompt → https://base44.com/ Free Prompt PDFs + AI Directory ...

📺 Malva AI

👁️ 7K • 👍 257 • 💬 43 • ⏱️ 8:49 • 12h ago

---

**[Why OpenAI and Anthropic may be rushing to IPO amid fears of AI premium fading](https://www.youtube.com/watch?v=7LbCf60q8Fc)**

CNBC's Kate Rooney reports on OpenAI and Anthropic as the AI giants move closer to going public.

📺 CNBC Television

👁️ 27K • 👍 234 • 💬 61 • ⏱️ 4:10 • 1d ago

---

**[Tim Dillon on Israel, Iran, AI, and Palantir](https://www.youtube.com/watch?v=DyKSUEEPb74)**

Taken from JRE #2518 w/Tim Dillon YouTube: https://youtu.be/wTdqkloiSvk JRE on Spotify: ...

📺 JRE Clips

👁️ 327K • 👍 7K • 💬 2K • ⏱️ 15:48 • 2d ago

---

**[China&#39;s Free AI Just Embarrassed Claude.. ](https://www.youtube.com/watch?v=8xkYrUz3Iuc)**

China just released a FREE open AI model that's shaking up the entire AI industry. In this week's AI Updates, we break down ...

📺 Your AI Guy

👁️ 13K • 👍 339 • 💬 71 • ⏱️ 15:48 • 1d ago

---

**[Japan Just Dropped an AI That Beats Claude (Fable 5)](https://www.youtube.com/watch?v=UyshVdGe4UY)**

Join our FREE WhatsApp Community: https://links.stayingahead.com/YT49 America just banned its best AI, Claude (Fable 5) so I ...

📺 Vaibhav Sisinty

👁️ 73K • 👍 2K • 💬 218 • ⏱️ 12:47 • 1d ago

---

**[Ancient scrolls unread for 2,000 years revealed with AI](https://www.youtube.com/watch?v=hcTnaI_djHQ)**

Researchers used AI and “virtual unwrapping” to reveal never-before-seen texts inside charred Roman scrolls buried by Mount ...

📺 NBC News

👁️ 153K • 👍 3K • 💬 389 • ⏱️ 3:00 • 23h ago

---

**[AI is Losing and the Left is Winning, with Brennan Lee Mulligan and Ed Zitron](https://www.youtube.com/watch?v=EGqCAmXTJBI)**

Smell that? Is that the stench of the algae bloom in Washington? Or maybe the odor of a big honkin' AI bubble that is ready to ...

📺 Adam Conover

👁️ 45K • 👍 5K • 💬 805 • ⏱️ 49:42 • 7h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 134,146 • ❤️ 1,032 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 83,589 • ❤️ 2,586 • 3d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`text-generation` `9.0B`

⬇️ 486,810 • ❤️ 578 • 4d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 186,663 • ❤️ 682 • 7d ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 516,333 • ❤️ 2,395 • 7d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 20,346 • ❤️ 443 • 2d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 13,186 • ❤️ 319 • 1d ago

---

**[Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)**

*KREA*

Krea-2-Turbo is a text-to-image diffusion model capable of generating diverse artistic styles, including halftone, pixelated, impressionist, thermal imaging, and black and white photography. It is primarily used for creative image generation and artistic exploration.

`text-to-image`

⬇️ 8,721 • ❤️ 285 • 3d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 54,638 • ❤️ 726 • 7d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 3,002 • ❤️ 225 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 34 • 💬 4 • ⭐ 10,306 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 173 • 💬 2 • ⭐ 70,179 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 88,759 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 36 • 💬 1 • ⭐ 25,648 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 60 • 💬 1 • ⭐ 84,410 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 8 • 💬 1 • ⭐ 9,148 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 247 • 💬 4 • ⭐ 9,410 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Qwen-AgentWorld: Language World Models for General Agents](https://huggingface.co/papers/2606.24597)**

*Yuxin Zuo, Zikai Xiao, Li Sheng et al. (33 authors)*

🏢 Qwen

Language-based world models enable agentic environment simulation across multiple domains and enhance general agent performance through scalable simulation and improved downstream task performance.

▲ 124 • 💬 4 • ⭐ 559 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.24597) • [💻 code](https://github.com/QwenLM/Qwen-AgentWorld)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 23 • 💬 1 • ⭐ 83,919 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 187 • 💬 6 • ⭐ 5,545 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 78.2k • 🔱 10.2k • 5h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 60.1k • 🔱 3.1k • 22h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.9k • 🔱 1.0k • 6h ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 5.4k • 🔱 425 • 5h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 5.0k • 🔱 609 • 1h ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 2.5k • 🔱 347 • 13h ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.0k • 🔱 143 • 4d ago

---

**[Forward-Future/loop-library](https://github.com/Forward-Future/loop-library)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 1.7k • 🔱 148 • 2h ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 151 • 11h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 86 • 13d ago

---

---

*Generated by PeekDeck - A glance is all you need*
