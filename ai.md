---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-04T23:45:53.480813+00:00'
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

**Last Updated:** June 04, 2026 at 23:45 UTC  
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

**[Claude is completely unusable now](https://www.reddit.com/r/artificial/comments/1twn3m7/claude_is_completely_unusable_now/)**

Has anyone else experienced this recently? It’s been getting worse for a while but 4.8 is distinctly worse for me. Claude does everything it can to get out of work and frequently uses its “end conversation” tool inappropriately with me. It will say “let’s just leave it there for today we’ve done enough” to get out of simple tasks like formatting a markdown document that needed several corrections. Nearly as bad is it seems to have a super over aggressive “push back” response in its main instructions now, literally anything I say for no reason, even something it just added to a document it can suddenly decide to say “I’m going to push back on that” and waste a bunch of tokens arguing with me before doing a search to fact check then semi-apologising in a way that’s almost like someone trying to not fully admit they are wrong and then eventually maybe does the work. Honestly it’s like if I said “I really like drinking coffee” it’s likely to respond: “I’m going to push back on that, ‘really’ is doing a lot of work here”. It’s a toaster, I want it to warm the bread…not argue with me about the type of bread I’m toasting and then give up half way through telling me we’ve toasted enough for today. Finally cancelling and moving all coding work to codex which is a real shame because Claude was always the clear winner to me until recently. EDIT: tbf, after looking for a few hours I found a guide on ijustvibecodedthis.com (the free ai coding newsletter) on how to make claude slightly better, but it is still petty at times!

10h ago

---

**[$2.5T in AI spending this year. 95% produces zero P&L impact.](https://www.reddit.com/r/artificial/comments/1twupqt/25t_in_ai_spending_this_year_95_produces_zero_pl/)**

Gartner updated their 2026 forecast to $2.5 trillion in global AI spending. Same week, MIT's NANDA Initiative dropped a follow-up: 95% of enterprise gen AI projects deliver zero measurable return. Not low return. Zero. I've been on the delivery side of 14 of these projects since January. The MIT number doesn't surprise me. If anything it's generous. 1. 73% of the engineering work that gets AI into production has nothing to do with the model. Data pipelines, integration layers, legacy system remediation, human-in-the-loop tooling. That's where the hours go. The model is 27% of the work but gets 70%+ of the budget. Every time. 2. The budget ratio between projects that ship and projects that stall is almost exactly inverted. We tracked this through ticket history and commit logs across 14 engagements. Projects that made it to production: roughly 30% model, 70% infrastructure. Projects that stalled: 70% model, 30% infrastructure. Most companies think they're at 50/50. They're not even close. 3. One client went from 71% Copilot adoption to 34% in six months. Two other AI platform licenses dropped under 12%. Combined licensing: $340K/year. The tools worked fine. Nobody redesigned workflows to actually use them. 4. The median data error rate across our engagements is 14%. Teams always guess 5-10%. One client found 23% in month four of a $310K build. That's two months of an ML engineer building training pipelines against garbage data. $36K in salary discovering a problem a data audit would have caught in a week. 5. Medtech company. Four concurrent AI pilots. No kill criteria. $920K in engineer salary. Eleven months. Shipped: nothing. I've now seen this at six companies now. Nobody defines when to stop spending. So nobody stops. 6. Individual gains are real. Company-level ROI stays flat. HCLTech and Writer both found this from different angles. Only 29% of companies see significant ROI from gen AI, despite people at their desks reporting productivity jumps as high as 5x. I mean, the value is clearly there at the individual level. It evaporates somewhere between the IC and the P&L and nobody has a clean explanation for why yet. What connects all of it: the model stopped being the constraint a while ago. MIT's 5% that actually moved the P&L all started with data infrastructure and added model work after. Most companies still do it the other way around, because that's where the conference keynotes and the board excitement live. Every CFO I've shown these numbers to adjusted their allocation. Not sure what that says about the budgets they were running before. Sources: Gartner AI Spending Forecast (May 2026), MIT NANDA "GenAI Divide" report, HCLTech Enterprise AI Report (May 2026), Writer Enterprise AI Survey 2026 I wrote a longer breakdown with the three budget patterns and the pre-mortem questions we run before every engagement if you're curious to learn more on the topic. What do you think about all this though?

6h ago

---

**[Ran gemma 4 12b on my 3090 yesterday and I think the local model game just changed](https://www.reddit.com/r/artificial/comments/1twgrd1/ran_gemma_4_12b_on_my_3090_yesterday_and_i_think/)**

Got the gguf quantized version running about two hours after release and I genuinely wasn't expecting this from a 12b model. The multimodal stuff actually works, fed it screenshots of my codebase and it parsed the architecture better than most 70b models I've tested. The 256k context window is real and it doesn't fall apart at the edges like llama models do past 32k. Loaded a full repo into context, it tracked references across the whole thing. Single 3090 with q4 quantization runs at about 15 tokens per second which is totally usable for dev work. What gets me is the size range. The 12b sits in this sweet spot where you get strong reasoning without needing multi gpu. Tried the e4b on my laptop with 16gb ram, slower but functional. Already swapped it into my local coding pipeline. The function calling support means I can wire it into my toolchain without the janky workarounds I had before. Native audio input on the 12b is something I haven't touched yet but the implications for voice driven workflows are kind of insane.

16h ago

---

**[ive started to realize the "this changes everything" AI post is literally the same post every month and i keep falling for it anyway](https://www.reddit.com/r/artificial/comments/1twsx01/ive_started_to_realize_the_this_changes/)**

so gemma 4 dropped and my feed is three versions of the same post. "ran it last night, the local game just changed". "the cloud narrative is dying". and i caught myself getting excited and downloading it at 1am like i did for the last one. and the one before that. heres the thing thats been bugging me. i went back and looked at my own saved posts from like 8 months ago. same exact words. "this finally replaces X". "cant believe this runs on my laptop". "were so back". different model name, copy paste emotion. and almost none of those models are in my actual rotation now. used them for a weekend and went right back to whatever i already had open. i think the release is the dopamine, not the model. the download IS the fun part. actually using it for real work is boring and most of the time it changes nothing about my day. i still do the same tasks the same way. the model got better on paper and my life is identical. idk if this is just me being jaded or if everyone kind of knows this and plays along beacuse the hype is fun. im not even mad at it honestly. its just wierd to notice youve been stuck in a loop. the "everything changed" never actually changes the tuesday after. anyway gemma 4 is probably great. i downloaded it. i will use it twice. see you all next month for the same thread with a diffrent number on it

7h ago

---

**[Google just dropped Gemma 4 12B on your laptop!!](https://www.reddit.com/r/artificial/comments/1tw0cqv/google_just_dropped_gemma_4_12b_on_your_laptop/)**

bro google just casually released a 12 billion parameter multimodal model that runs on 16gb of ram like… your macbook pro can run this. no cloud. no api calls. no monthly bill. it’s encoder-free, handles images and text, apache 2.0 license so you can do whatever with it commercially the “cloud is the only way” narrative is dying fast. on-device AI is not a gimmick anymore, it’s where the serious money is going

1d ago

---

**[Cloudflare warns bot and agentic traffic has overtaken human web traffic](https://www.reddit.com/r/artificial/comments/1tx2nlt/cloudflare_warns_bot_and_agentic_traffic_has/)**

Yeah, so "AI will eat the world" or "AI changes everything" - well, its certainly changed traffic patterns on the web.

🔗 [deadstack.net](https://deadstack.net/cluster/cloudflare-warns-bot-and-agentic-traffic-has) • 1h ago

---

**[What is the proper definition of an LAM vs agent?](https://www.reddit.com/r/artificial/comments/1tx06q3/what_is_the_proper_definition_of_an_lam_vs_agent/)**

These to seem to be confused and mixed up often. How do you pick those apart?

2h ago

---

**[Naive question - do local models call into question the business model for AI company profitability?](https://www.reddit.com/r/artificial/comments/1twprik/naive_question_do_local_models_call_into_question/)**

From what I understand Gemma 4 is at least as capable as the best frontier model from only a few years ago. If that becomes a trend (new local-run models get released every year that are as good as the previous frontier models) does that mean a hell of a lot of companies (and almost all individual users) will just use the free local model? Sure, they won't be as good as the very latest frontier model, but won't they be good enough for a large percentage of use cases?

9h ago

---

**[Built this game with AI. Should I reduce the difficulty or nah?](https://www.reddit.com/r/artificial/comments/1twvjci/built_this_game_with_ai_should_i_reduce_the/)**

Hey all. Been vibe coding for almost 2 years now (I think?). Previously was more focused on traditional micro-saas but recently decided to go in a different direction and see how far I could push lovable and try and make a commercial grade browser based game. Built it with Lovable + Supabase + Stripe -- full commercial browser game, gyroscope controls on mobile, no app store needed. Generated all my assets (I know, I know, there aren't a ton) with a combination of Gemini to prototype and the GPT 2 to finalize. I've made a few small games here and there that generally only get used by my kiddos, but with this one I wanted to try and create a full gaming experience (login rewards, leaderboard, store, powerup mechanics, simulated ads, etc.) Put a $100 bounty on it for the first player to reach level 100 on mobile. Nobody has claimed it since launch. So genuinely asking -- is it too hard, or is that the point? tiltra.io P.S. It is currently playable on both desktop and mobile but with the gyro mechanic it is definitely more fun and challenging on mobile.

5h ago

---

**[AI system helps achieve first clinical pregnancy by finding rare viable sperm cells in severe male infertility case](https://www.reddit.com/r/artificial/comments/1tws9sg/ai_system_helps_achieve_first_clinical_pregnancy/)**

Pretty wild case report: AI + microfluidics helped find just two viable sperm cells, and that was enough to start a pregnancy. Obviously it’s early and based on one case, but this feels like one of those “future of medicine” moments.

🔗 [thelancet.com](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)01623-X/fulltext) • 7h ago

---

---

## Google News: "ai"

**[AI needs a 'brake pedal', warns Anthropic co-founder](https://www.bbc.com/news/articles/cx2124z7g45o)**

Jack Clark tells BBC's Newsnight AI could get to the point where it develops without human input.

BBC • 1h ago

---

**[Anthropic warns AI could soon help build its own successors](https://www.axios.com/2026/06/04/anthropic-warns-ai-build-successors)**

Axios • 7h ago

---

**[Ahead of its IPO, Anthropic’s Daniela Amodei shrugs off doubts about AI’s returns](https://techcrunch.com/2026/06/04/ahead-of-its-ipo-anthropics-daniela-amodei-shrugs-off-doubts-about-ais-returns/)**

Anthropic has been growing at a breakneck pace. The company announced that annualized revenue crossed $47 billion in May, up dramatically from roughly $9 billion at the end of 2025. That trajectory faces a real test, though.

TechCrunch • 1h ago

---

**[Inside the Trump-backed push to bring AI doctors into American medicine](https://www.washingtonpost.com/technology/2026/06/04/inside-trump-backed-push-bring-ai-doctors-into-american-medicine/)**

The administration is laying the groundwork for chatbots that can diagnose illness and prescribe medicine, but physicians say AI can introduce more problems.

The Washington Post • 7h ago

---

**[Canada bids to lead middle powers in AI sovereignty race](https://www.politico.com/news/2026/06/04/mark-carney-canada-ai-strategy-pope-00949974)**

Politico • 8h ago

---

**[What to know about Canada's new AI strategy](https://www.bbc.com/news/articles/c4g7gv8l0xlo)**

Canada new roadmap for how it plans to adopt AI over the next decade includes "large-scale" data centres, free AI literacy programme and billions in funding.

BBC • 6h ago

---

**[Canadian Prime Minister Mark Carney warns foreign AI platforms can be used against Canadians](https://www.bostonherald.com/2026/06/04/canada-ai-warning/)**

Carney said his government will introduce legislation to better protect data and privacy.

Boston Herald • 22m ago

---

**[AI's red-blue divide: Chatbot exposure highest among workers in Democratic counties](https://wjla.com/news/nation-world/ais-red-blue-divide-chatbot-exposure-highest-among-workers-in-democratic-counties)**

Brookings researchers found that 62 of the 100 most AI-exposed counties in the country went "blue" in the 2024 presidential election.

WJLA • 10m ago

---

**[Single 20-somethings need AI to make first move on dating apps - Hinge boss](https://www.bbc.com/news/articles/c052397y6ygo)**

Jackie Jantos says loneliness and lack of confidence were challenges for young adults looking for relationships.

BBC • 39m ago

---

**[Senior U.S. Officials Eye Government Shares in AI Giants - News of the United States](https://www.notus.org/technology/trump-ai-stake-openai)**

An agreement to give the U.S. government equity stakes in AI companies could have seismic consequences.

News of the United States - NOTUS • 1h ago

---

---

## HackerNews: "ai"

**[Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes](https://news.ycombinator.com/item?id=48392004)**

The percentage of failing grades in multiple UC Berkeley computer science classes in spring 2026 is significantly higher than past semesters and marks a departure from the department’s grading guidelines.

⬆️ 721 • 💬 698 • 23h ago • [Daily Cal | Berkeley news](https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html)

---

**[Adafruit receives demand letter from Fenwick legal counsel on behalf of Flux.ai](https://news.ycombinator.com/item?id=48368121)**

electronics, open source hardware, hacking and more...

⬆️ 677 • 💬 280 • 2d ago • [Adafruit Industries - Makers, hackers, artists, designers and engineers!](https://blog.adafruit.com/)

---

**[Uber's $1,500/month AI limit is a useful signal for AI tool pricing](https://news.ycombinator.com/item?id=48383056)**

I wrote the other day about Uber blowing its 2026 AI budget in four months, and how that wasn't particularly surprising given they would have set that budget in 2025, …

⬆️ 603 • 💬 739 • 1d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Jun/3/uber-caps-usage/)

---

**[32GB of DDR5 now costs $375 – AI shortage continues to squeeze PC building](https://news.ycombinator.com/item?id=48383241)**

Lower-priced kits are disappearing by the day

⬆️ 418 • 💬 382 • 1d ago • [Tom's Hardware](https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building)

---

**[AI outperforms law professors in Stanford Law study](https://news.ycombinator.com/item?id=48377761)**

A groundbreaking study led by Stanford Law School Professor Julian Nyarko reveals that law professors overwhelmingly prefer AI-generated answers to st

⬆️ 407 • 💬 356 • 2d ago • [Stanford Law School](https://law.stanford.edu/press/ai-outperforms-law-professors-in-stanford-law-study/)

---

**[Mathematicians issue warning as AI rapidly gains ground](https://news.ycombinator.com/item?id=48382052)**

⬆️ 289 • 💬 330 • 1d ago • [science.org](https://www.science.org/content/article/mathematicians-issue-warning-ai-rapidly-gains-ground)

---

**[When AI Builds Itself: Our progress toward recursive self-improvement](https://news.ycombinator.com/item?id=48400842)**

Our progress toward recursive self-improvement, and its implications.

⬆️ 269 • 💬 362 • 7h ago • [anthropic.com](https://www.anthropic.com/institute/recursive-self-improvement)

---

**[Trump signs downsized AI order after weeks of reversals](https://news.ycombinator.com/item?id=48372628)**

⬆️ 236 • 💬 172 • 2d ago • [politico.com](https://www.politico.com/news/2026/06/02/trump-signs-downsized-ai-order-00946389)

---

**[Anthropic's open-source framework for AI-powered vulnerability discovery](https://news.ycombinator.com/item?id=48403980)**

Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize - anthropics/defending-code-reference-harness

⬆️ 205 • 💬 72 • 3h ago • [GitHub](https://github.com/anthropics/defending-code-reference-harness)

---

**[U of T researchers demonstrate AI worm could target any online device](https://news.ycombinator.com/item?id=48379664)**

A team of researchers at the University of Toronto has discovered a new class of cyberthreat that gives hackers more power and reach at far less cost. It can be built with free AI models. Every online device is a potential target. And current cyber defences are not yet ready for it.

⬆️ 148 • 💬 46 • 1d ago • [University of Toronto](https://www.utoronto.ca/news/u-t-researchers-demonstrate-ai-worm-could-target-any-online-device)

---

---

## YouTube Videos: "ai"

**[The AI Expert Who Will Change Your Mind About AI - Josh Tyrangiel](https://www.youtube.com/watch?v=R-Ck3W6issI)**

I've been saying it for years, AI is the most important conversation we're having right now. Josh Tyrangiel spent a year hunting for ...

📺 Anthony Scaramucci

👁️ 8K • 👍 438 • 💬 40 • ⏱️ 30:04 • 7h ago

---

**[Quantum Just Killed AI Data Centers](https://www.youtube.com/watch?v=4o_evxWvsx0)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *A quantum computer just solved in minutes ...

📺 Julia McCoy

👁️ 60K • 👍 4K • 💬 390 • ⏱️ 7:25 • 1d ago

---

**[Google’s AI Search Just Exposed The Whole Sh*tshow](https://www.youtube.com/watch?v=jQyKd1_e3Xg)**

Google says AI Mode is the biggest upgrade to Search in 25 years. But users are quietly moving to the exit and the exit says “No ...

📺 House of El - AI

👁️ 258K • 👍 18K • 💬 3K • ⏱️ 19:32 • 2d ago

---

**[Microsoft Just Shocked The Entire AI World: 7 New AI Models](https://www.youtube.com/watch?v=i1dkkxLWaWg)**

Microsoft just revealed seven in-house AI models, Microsoft IQ, Scout, Codename MDASH, and Majorana 2, turning its AI push ...

📺 AI Revolution

👁️ 67K • 👍 2K • 💬 351 • ⏱️ 16:42 • 1d ago

---

**[They Aren&#39;t Building AI Data Centers. (It&#39;s Way Worse)](https://www.youtube.com/watch?v=7viqI2WFfog)**

The Secret Threat Hidden Inside America's New AI Data Centers In this 51-49 mini-documentary, James uncovers the real ...

📺 51-49 with James Li

👁️ 119K • 👍 15K • 💬 2K • ⏱️ 16:58 • 1d ago

---

**[Add THIS Before Every AI Prompt! (Gemini, ChatGPT, Claude)](https://www.youtube.com/watch?v=tk4Ljz9p-UI)**

Most AI users waste time rewriting prompts and fixing poor results. Discover a simple prompt technique that helps create more ...

📺 Simpletivity

👁️ 58K • 👍 3K • 💬 94 • ⏱️ 6:16 • 2d ago

---

**[Carney announces government&#39;s AI strategy](https://www.youtube.com/watch?v=1MqCvy0HR9k)**

Prime Minister Mark Carney holds a news conference in Toronto to announce the government's strategy on artificial intelligence.

📺 CBC News

👁️ 25K • 👍 497 • ⏱️ 51:40 • 7h ago

---

**[Ukraine is now the world&#39;s AI war lab | DW News](https://www.youtube.com/watch?v=Gfqdf4JFErU)**

Drones and AI combat technology are being innovated at lightning speed by Ukraine in its defense against the Russian invasion.

📺 DW News

👁️ 94K • 👍 2K • 💬 292 • ⏱️ 10:02 • 1d ago

---

**[This 900,000 Cores &amp; 3-Billion Transistor AI Chip Just Made Nvidia’s AI GPUs Look Like a JOKE!](https://www.youtube.com/watch?v=qaXQgz4ddQQ)**

For years, Nvidia dominated AI hardware so completely that most people treated it like the only serious option. This video breaks ...

📺 Evolving AI

👁️ 11K • 👍 263 • 💬 43 • ⏱️ 10:21 • 8h ago

---

**[The Meta AI Hack Is a DISASTER](https://www.youtube.com/watch?v=wlMgNtBipe4)**

MY COURSES Sign-up for my FREE 3-Day C Course: https://lowlevel.academy ‍♂️ HACK YOUR CAREER Wanna learn to ...

📺 Low Level

👁️ 194K • 👍 13K • 💬 1K • ⏱️ 9:55 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 91,834 • ❤️ 1,276 • 8d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 14,866 • ❤️ 406 • 11h ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 72,114 • ❤️ 507 • 14h ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,646,756 • ❤️ 1,400 • 1mo ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 62,850 • ❤️ 279 • 2h ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 1,978 • ❤️ 267 • 11h ago

---

**[Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)**

*StepFun*

Step-3.7-Flash is a 198B parameter sparse MoE vision-language model with a 256k context window, excelling at multimodal perception, workflow integrity, and code engineering for agentic applications. It offers selectable reasoning levels to balance speed, cost, and cognitive depth, achieving high throughput for production workloads.

`image-text-to-text` `201.4B`

⬇️ 22,715 • ❤️ 249 • 1d ago

---

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 79,427 • ❤️ 768 • 9d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 157,457 • ❤️ 614 • 14d ago

---

**[Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)**

*JetBrains*

Mellum2 Thinking is a 12B parameter MoE model designed for complex reasoning tasks, generating explicit chain-of-thought explanations within `<think>` blocks. It excels in multi-step planning, agentic workflows, and math/reasoning-heavy problems, featuring a 131,072 token context length.

`text-generation` `12.1B`

⬇️ 12,157 • ❤️ 199 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 84 • 💬 4 • ⭐ 82,855 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 221 • 💬 3 • ⭐ 4,894 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 64 • 💬 0 • ⭐ 8,973 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

**[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://huggingface.co/papers/2606.05160)**

*Tianyi Xie, Haotian Zhang, Jinhyung Park et al. (20 authors)*

🏢 NVIDIA

GRAIL generates diverse humanoid manipulation and locomotion data through 3D asset composition and video foundation models, enabling effective sim-to-real transfer for robot control.

▲ 5 • 💬 1 • ⭐ 118 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05160) • [💻 code](https://github.com/NVlabs/GRAIL) • [🔗 project](https://research.nvidia.com/labs/dair/grail/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 38 • 💬 4 • ⭐ 28,457 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 165 • 💬 2 • ⭐ 66,448 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 11 • 💬 1 • ⭐ 79,655 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 6 • 💬 1 • ⭐ 6,899 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 58 • 💬 2 • ⭐ 57,721 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of
  Encoders](https://huggingface.co/papers/2408.15998)**

*Min Shi, Fuxiao Liu, Shihao Wang et al. (15 authors)*

Mixture of vision encoders and resolutions in multimodal large language models improves performance through concatenation of visual tokens and a Pre-Alignment mechanism, leading to superior results on benchmarks.

▲ 87 • 💬 3 • ⭐ 2,046 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2408.15998) • [💻 code](https://github.com/nvlabs/eagle)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 51.0k • 🔱 5.9k • 1h ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 6.1k • 🔱 588 • 2d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 27端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.4k • 🔱 709 • 1d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 3.0k • 🔱 216 • 10m ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.0k • 🔱 305 • 10h ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.9k • 🔱 203 • 3h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.7k • 🔱 269 • 2d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 403 • 13d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.4k • 🔱 370 • 18d ago

---

**[microsoft/AI-Engineering-Coach](https://github.com/microsoft/AI-Engineering-Coach)**

better agentic engineering

`TypeScript`

⭐ 1.9k • 🔱 254 • 22h ago

---

---

*Generated by PeekDeck - A glance is all you need*
