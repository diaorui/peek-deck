---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-04T18:26:55.740202+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 04, 2026 at 18:26 UTC  
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

Has anyone else experienced this recently? It’s been getting worse for a while but 4.8 is distinctly worse for me. Claude does everything it can to get out of work and frequently uses its “end conversation” tool inappropriately with me. It will say “let’s just leave it there for today we’ve done enough” to get out of simple tasks like formatting a markdown document that needed several corrections. Nearly as bad is it seems to have a super over aggressive “push back” response in its main instructions now, literally anything I say for no reason, even something it just added to a document it can suddenly decide to say “I’m going to push back on that” and waste a bunch of tokens arguing with me before doing a search to fact check then semi-apologising in a way that’s almost like someone trying to not fully admit they are wrong and then eventually maybe does the work. Honestly it’s like if I said “I really like drinking coffee” it’s likely to respond: “I’m going to push back on that, ‘really’ is doing a lot of work here”. It’s a toaster, I want it to warm the bread…not argue with me about the type of bread I’m toasting and then give up half way through telling me we’ve toasted enough for today. Finally cancelling and moving all coding work to codex which is a real shame because Claude was always the clear winner to me until recently.

5h ago

---

**[Ran gemma 4 12b on my 3090 yesterday and I think the local model game just changed](https://www.reddit.com/r/artificial/comments/1twgrd1/ran_gemma_4_12b_on_my_3090_yesterday_and_i_think/)**

Got the gguf quantized version running about two hours after release and I genuinely wasn't expecting this from a 12b model. The multimodal stuff actually works, fed it screenshots of my codebase and it parsed the architecture better than most 70b models I've tested. The 256k context window is real and it doesn't fall apart at the edges like llama models do past 32k. Loaded a full repo into context, it tracked references across the whole thing. Single 3090 with q4 quantization runs at about 15 tokens per second which is totally usable for dev work. What gets me is the size range. The 12b sits in this sweet spot where you get strong reasoning without needing multi gpu. Tried the e4b on my laptop with 16gb ram, slower but functional. Already swapped it into my local coding pipeline. The function calling support means I can wire it into my toolchain without the janky workarounds I had before. Native audio input on the 12b is something I haven't touched yet but the implications for voice driven workflows are kind of insane.

10h ago

---

**[Google just dropped Gemma 4 12B on your laptop!!](https://www.reddit.com/r/artificial/comments/1tw0cqv/google_just_dropped_gemma_4_12b_on_your_laptop/)**

bro google just casually released a 12 billion parameter multimodal model that runs on 16gb of ram like… your macbook pro can run this. no cloud. no api calls. no monthly bill. it’s encoder-free, handles images and text, apache 2.0 license so you can do whatever with it commercially the “cloud is the only way” narrative is dying fast. on-device AI is not a gimmick anymore, it’s where the serious money is going

22h ago

---

**[ive started to realize the "this changes everything" AI post is literally the same post every month and i keep falling for it anyway](https://www.reddit.com/r/artificial/comments/1twsx01/ive_started_to_realize_the_this_changes/)**

so gemma 4 dropped and my feed is three versions of the same post. "ran it last night, the local game just changed". "the cloud narrative is dying". and i caught myself getting excited and downloading it at 1am like i did for the last one. and the one before that. heres the thing thats been bugging me. i went back and looked at my own saved posts from like 8 months ago. same exact words. "this finally replaces X". "cant believe this runs on my laptop". "were so back". different model name, copy paste emotion. and almost none of those models are in my actual rotation now. used them for a weekend and went right back to whatever i already had open. i think the release is the dopamine, not the model. the download IS the fun part. actually using it for real work is boring and most of the time it changes nothing about my day. i still do the same tasks the same way. the model got better on paper and my life is identical. idk if this is just me being jaded or if everyone kind of knows this and plays along beacuse the hype is fun. im not even mad at it honestly. its just wierd to notice youve been stuck in a loop. the "everything changed" never actually changes the tuesday after. anyway gemma 4 is probably great. i downloaded it. i will use it twice. see you all next month for the same thread with a diffrent number on it

1h ago

---

**[$2.5T in AI spending this year. 95% produces zero P&L impact.](https://www.reddit.com/r/artificial/comments/1twupqt/25t_in_ai_spending_this_year_95_produces_zero_pl/)**

Gartner updated their 2026 forecast to $2.5 trillion in global AI spending. Same week, MIT's NANDA Initiative dropped a follow-up: 95% of enterprise gen AI projects deliver zero measurable return. Not low return. Zero. I've been on the delivery side of 14 of these projects since January. The MIT number doesn't surprise me. If anything it's generous. 1. 73% of the engineering work that gets AI into production has nothing to do with the model. Data pipelines, integration layers, legacy system remediation, human-in-the-loop tooling. That's where the hours go. The model is 27% of the work but gets 70%+ of the budget. Every time. 2. The budget ratio between projects that ship and projects that stall is almost exactly inverted. We tracked this through ticket history and commit logs across 14 engagements. Projects that made it to production: roughly 30% model, 70% infrastructure. Projects that stalled: 70% model, 30% infrastructure. Most companies think they're at 50/50. They're not even close. 3. One client went from 71% Copilot adoption to 34% in six months. Two other AI platform licenses dropped under 12%. Combined licensing: $340K/year. The tools worked fine. Nobody redesigned workflows to actually use them. 4. The median data error rate across our engagements is 14%. Teams always guess 5-10%. One client found 23% in month four of a $310K build. That's two months of an ML engineer building training pipelines against garbage data. $36K in salary discovering a problem a data audit would have caught in a week. 5. Medtech company. Four concurrent AI pilots. No kill criteria. $920K in engineer salary. Eleven months. Shipped: nothing. I've now seen this at six companies now. Nobody defines when to stop spending. So nobody stops. 6. Individual gains are real. Company-level ROI stays flat. HCLTech and Writer both found this from different angles. Only 29% of companies see significant ROI from gen AI, despite people at their desks reporting productivity jumps as high as 5x. I mean, the value is clearly there at the individual level. It evaporates somewhere between the IC and the P&L and nobody has a clean explanation for why yet. What connects all of it: the model stopped being the constraint a while ago. MIT's 5% that actually moved the P&L all started with data infrastructure and added model work after. Most companies still do it the other way around, because that's where the conference keynotes and the board excitement live. Every CFO I've shown these numbers to adjusted their allocation. Not sure what that says about the budgets they were running before. Sources: Gartner AI Spending Forecast (May 2026), MIT NANDA "GenAI Divide" report, HCLTech Enterprise AI Report (May 2026), Writer Enterprise AI Survey 2026 I wrote a longer breakdown with the three budget patterns and the pre-mortem questions we run before every engagement if you're curious to learn more on the topic. What do you think about all this though?

49m ago

---

**[What model do you use and how many tokens do you consume](https://www.reddit.com/r/artificial/comments/1twoc22/what_model_do_you_use_and_how_many_tokens_do_you/)**

Talking about efficiency and reliability of LLM tools. How many tokens per task, per project, per month

4h ago

---

**[AI system helps achieve first clinical pregnancy by finding rare viable sperm cells in severe male infertility case](https://www.reddit.com/r/artificial/comments/1tws9sg/ai_system_helps_achieve_first_clinical_pregnancy/)**

Pretty wild case report: AI + microfluidics helped find just two viable sperm cells, and that was enough to start a pregnancy. Obviously it’s early and based on one case, but this feels like one of those “future of medicine” moments.

🔗 [thelancet.com](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)01623-X/fulltext) • 2h ago

---

**[Naive question - do local models call into question the business model for AI company profitability?](https://www.reddit.com/r/artificial/comments/1twprik/naive_question_do_local_models_call_into_question/)**

From what I understand Gemma 4 is at least as capable as the best frontier model from only a few years ago. If that becomes a trend (new local-run models get released every year that are as good as the previous frontier models) does that mean a hell of a lot of companies (and almost all individual users) will just use the free local model? Sure, they won't be as good as the very latest frontier model, but won't they be good enough for a large percentage of use cases?

3h ago

---

**[Hassabis says AGI in three years but I keep thinking about the harness layer](https://www.reddit.com/r/artificial/comments/1twpobj/hassabis_says_agi_in_three_years_but_i_keep/)**

The DeepMind CEO predicted AGI could arrive by 2029. Right as Anthropic files for IPO at close to a trillion dollar valuation. The combined target market cap of the AI big three would rival the GDP of most countries. What actually scares me. We already have models that code better than most juniors. We already have agents that run overnight. And the most common complaint I hear from teams is not "my model is not smart enough." It is "I do not know what my agent did, why it cost forty dollars, or whether the output is safe to merge." AGI does not solve that. The problem scales with capability. A smarter agent that runs longer with less oversight is a bigger liability, not a smaller one. The layer that matters is harness. Routing. Isolation. Plan verification. Cost visibility. The stuff that tells you what the agent is about to do before it does it. What keeps it inside a boundary. What lets you audit it after. Anthropic is building Mythos to find vulnerabilities before attackers do. Microsoft is building MXC to isolate agents in execution containers. In my own tiny setup, verdent is just one piece of that harness layer for planning and cost visibility. These are governance layers, not model layers. If AGI is three years away, the winners will not be the ones with the smartest model. They will be the ones who figured out how to aim it.

3h ago

---

**[Google’s Gemma 4 12B just dropped - here’s how to run it locally on your Mac](https://www.reddit.com/r/artificial/comments/1twpf9m/googles_gemma_4_12b_just_dropped_heres_how_to_run/)**

Google released Gemma 4 12B today. It’s a solid open-source model (Apache 2.0) that’s multimodal and runs really well on Macs with 16GB or more unified memory. Good at reasoning, coding, and agent stuff. Quick Mac-friendly info • 12B parameters, fits nicely on M2/M3/M4 Macs (especially with Q4/Q5 quant) • 256K context • Text + vision + audio support Easiest way to run it: Ollama 1. Download and install Ollama from ollama.com (the Mac app is super simple). Or use Homebrew if you prefer. 2. Open Terminal and pull the model: ollama pull gemma4:12b 3. Run it: ollama run gemma4:12b That’s it. You can start chatting right away. Mac tips: • Ollama uses Metal automatically so it runs pretty fast on Apple Silicon. • 16GB Macs handle the 12B model fine. 32GB feels even better. • Great for pairing with Continue.dev in VS Code if you code a lot. Other options if Ollama isn’t your thing: LM Studio (nice GUI), or llama.cpp for more control. Has anyone tried the image or audio features locally yet? How fast is it on your machine? Drop your specs and results if you test it.​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​

3h ago

---

---

## Google News: "ai"

**[The Small-Business Owners Managing Whole Armies of A.I. Employees](https://www.nytimes.com/2026/06/04/magazine/ai-agents-openclaw-small-business.html)**

The New York Times • 9h ago

---

**[No, Artificial Intelligence Is Not Conscious](https://www.theatlantic.com/philosophy/2026/06/no-artificial-intelligence-is-not-conscious/687378/)**

Taken to its logical conclusion, this line of thinking is absurd—and damning.

The Atlantic • 1d ago

---

**[What's inside the House draft bill to regulate AI](https://www.axios.com/2026/06/04/house-draft-bill-regulate-ai)**

Axios • 57m ago

---

**[House unveils AI draft that would preempt state laws](https://www.politico.com/news/2026/06/04/obernolte-trahan-ai-bill-lands-on-the-hill-00949920)**

Politico • 1h ago

---

**[What's inside the House draft bill to regulate AI](https://www.yahoo.com/news/politics/articles/whats-inside-house-draft-bill-172948803.html)**

A bipartisan group of House lawmakers on Thursday unveiled a proposal to regulate AI that would override some state laws.

Yahoo • 57m ago

---

**[Bloomberg Tech Conference 2026: Live News on AI, Chips, Technology - Bloomberg](https://www.bloomberg.com/news/live-blog/2026-06-04/bloomberg-tech-conference-2026)**

Bloomberg.com • 31m ago

---

**[Enterprises start questioning the return on AI investments](https://www.cnbc.com/video/2026/06/04/enterprises-start-questioning-the-actual-return-on-ai-costs.html)**

CNBC's Deirdre Bosa reports on the latest AI concern.

CNBC • 22m ago

---

**[Inside the Trump-backed push to bring AI doctors into American medicine](https://www.washingtonpost.com/technology/2026/06/04/inside-trump-backed-push-bring-ai-doctors-into-american-medicine/)**

The administration is laying the groundwork for chatbots that can diagnose illness and prescribe medicine, but physicians say AI can introduce more problems.

The Washington Post • 2h ago

---

**[A CEO told employees they won't get raises in 2026 because the budget is going to AI](https://www.businessinsider.com/teradata-pauses-raises-employee-compensation-ai-budget-2026-6)**

Cloud software firm Teradata has told employees not to expect annual salary raises in 2026, and says it is putting the money towards AI instead.

Business Insider • 9h ago

---

**[A handful of American households pay for AI. Is the future free — or a subscription?](https://www.npr.org/2026/06/04/nx-s1-5791661/chatgpt-gemini-claude-subscription-revenue-openai)**

Just 3% of U.S. households pay for AI for personal use. Sign ups are growing — even though Americans have subscription fatigue.

NPR • 9h ago

---

---

## HackerNews: "ai"

**[Adafruit receives demand letter from Fenwick legal counsel on behalf of Flux.ai](https://news.ycombinator.com/item?id=48368121)**

electronics, open source hardware, hacking and more...

⬆️ 674 • 💬 280 • 2d ago • [Adafruit Industries - Makers, hackers, artists, designers and engineers!](https://blog.adafruit.com/)

---

**[Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes](https://news.ycombinator.com/item?id=48392004)**

The percentage of failing grades in multiple UC Berkeley computer science classes in spring 2026 is significantly higher than past semesters and marks a departure from the department’s grading guidelines.

⬆️ 607 • 💬 581 • 18h ago • [Daily Cal | Berkeley news](https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html)

---

**[Uber's $1,500/month AI limit is a useful signal for AI tool pricing](https://news.ycombinator.com/item?id=48383056)**

I wrote the other day about Uber blowing its 2026 AI budget in four months, and how that wasn't particularly surprising given they would have set that budget in 2025, …

⬆️ 583 • 💬 714 • 1d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Jun/3/uber-caps-usage/)

---

**[32GB of DDR5 now costs $375 – AI shortage continues to squeeze PC building](https://news.ycombinator.com/item?id=48383241)**

Lower-priced kits are disappearing by the day

⬆️ 414 • 💬 377 • 1d ago • [Tom's Hardware](https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building)

---

**[AI outperforms law professors in Stanford Law study](https://news.ycombinator.com/item?id=48377761)**

A groundbreaking study led by Stanford Law School Professor Julian Nyarko reveals that law professors overwhelmingly prefer AI-generated answers to st

⬆️ 406 • 💬 356 • 1d ago • [Stanford Law School](https://law.stanford.edu/press/ai-outperforms-law-professors-in-stanford-law-study/)

---

**[Mathematicians issue warning as AI rapidly gains ground](https://news.ycombinator.com/item?id=48382052)**

⬆️ 280 • 💬 316 • 1d ago • [science.org](https://www.science.org/content/article/mathematicians-issue-warning-ai-rapidly-gains-ground)

---

**[Alphabet announces $80B equity capital raise to expand AI infra and compute](https://news.ycombinator.com/item?id=48362515)**

⬆️ 254 • 💬 236 • 2d ago • [abc.xyz](https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Proposed-80-Billion-Equity-Capital-Raise-to-Expand-AI-Infrastructure-and-Compute-2026-b0myAMewCa/default.aspx)

---

**[Trump signs downsized AI order after weeks of reversals](https://news.ycombinator.com/item?id=48372628)**

⬆️ 235 • 💬 173 • 2d ago • [politico.com](https://www.politico.com/news/2026/06/02/trump-signs-downsized-ai-order-00946389)

---

**[U of T researchers demonstrate AI worm could target any online device](https://news.ycombinator.com/item?id=48379664)**

A team of researchers at the University of Toronto has discovered a new class of cyberthreat that gives hackers more power and reach at far less cost. It can be built with free AI models. Every online device is a potential target. And current cyber defences are not yet ready for it.

⬆️ 148 • 💬 46 • 1d ago • [University of Toronto](https://www.utoronto.ca/news/u-t-researchers-demonstrate-ai-worm-could-target-any-online-device)

---

**[Google employees internally share memes about how its AI sucks](https://news.ycombinator.com/item?id=48400311)**

Google’s CEO says 75% of the company’s code is AI-generated. The people who write that code say the AI they’re using is overhyped.

⬆️ 130 • 💬 87 • 2h ago • [404 Media](https://www.404media.co/google-employees-internally-share-memes-about-how-its-ai-sucks/)

---

---

## YouTube Videos: "ai"

**[I Fully Automated Video Editing With AI (here’s how)](https://www.youtube.com/watch?v=RwynWBXuRaA)**

AI Video Editing Just Became REAL (fully automated workflow) Prompt Pack: ...

📺 Mira AI

👁️ 3K • ⏱️ 7:14 • 1h ago

---

**[Microsoft Just Shocked The Entire AI World: 7 New AI Models](https://www.youtube.com/watch?v=i1dkkxLWaWg)**

Microsoft just revealed seven in-house AI models, Microsoft IQ, Scout, Codename MDASH, and Majorana 2, turning its AI push ...

📺 AI Revolution

👁️ 58K • 👍 2K • 💬 334 • ⏱️ 16:42 • 19h ago

---

**[Google’s AI Search Just Exposed The Whole Sh*tshow](https://www.youtube.com/watch?v=jQyKd1_e3Xg)**

Google says AI Mode is the biggest upgrade to Search in 25 years. But users are quietly moving to the exit and the exit says “No ...

📺 House of El - AI

👁️ 250K • 👍 18K • 💬 3K • ⏱️ 19:32 • 2d ago

---

**[The Simplest AI Side Hustle for Beginners](https://www.youtube.com/watch?v=DKqQe0MqDTs)**

I used Lovable to build the apps in this video. No code, just typing what I wanted. Go build something: https://lovable.link/ip2vPWM ...

📺 Chris Koerner on The Koerner Office Podcast

👁️ 17K • 👍 776 • 💬 61 • ⏱️ 33:03 • 17h ago

---

**[Quantum Just Killed AI Data Centers](https://www.youtube.com/watch?v=4o_evxWvsx0)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *A quantum computer just solved in minutes ...

📺 Julia McCoy

👁️ 51K • 👍 3K • 💬 353 • ⏱️ 7:25 • 19h ago

---

**[Microsoft AI CEO unveils 7 new AI models | Mustafa Suleyman at Microsoft Build 2026](https://www.youtube.com/watch?v=OvLIae4HCeM)**

Our goal is Humanist Superintelligence — AI designed to serve people, not replace them. At Microsoft Build 2026, Microsoft AI ...

📺 Microsoft

👁️ 41K • 👍 1K • 💬 70 • ⏱️ 14:37 • 1d ago

---

**[Did The Stock Market AI Bubble Just Burst? Broadcom Crash &amp; SpaceX IPO Warning](https://www.youtube.com/watch?v=XrhlAS53AnQ)**

Welcome to Verified Investing! In today's technical analysis, Chief Market Strategist Gareth Soloway breaks down the massive ...

📺 Gareth Soloway

👁️ 31K • 👍 2K • 💬 250 • ⏱️ 10:58 • 6h ago

---

**[AI Bubble Will Burst Eventually Says Bridgewater&#39;s Ray Dalio](https://www.youtube.com/watch?v=WZ7mmTrSgxI)**

Bridgewater Associates Founder Ray Dalio says the debt burden has passed a "point of no return." He speaks with Bloomberg's ...

📺 Bloomberg Podcasts

👁️ 126K • 👍 2K • 💬 354 • ⏱️ 13:20 • 1d ago

---

**[They Aren&#39;t Building AI Data Centers. (It&#39;s Way Worse)](https://www.youtube.com/watch?v=7viqI2WFfog)**

The Secret Threat Hidden Inside America's New AI Data Centers In this 51-49 mini-documentary, James uncovers the real ...

📺 51-49 with James Li

👁️ 112K • 👍 15K • 💬 2K • ⏱️ 16:58 • 1d ago

---

**[The AI backlash: Why Gen Z is pushing back | The Global Story](https://www.youtube.com/watch?v=Mun_KJYXsco)**

A 2025 Harvard poll of young people in the US found that a majority see AI as a threat to their career prospects. And in recent ...

📺 BBC News

👁️ 41K • 👍 941 • 💬 355 • ⏱️ 19:44 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 91,834 • ❤️ 1,244 • 8d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 72,114 • ❤️ 495 • 9h ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 14,866 • ❤️ 348 • 6h ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,646,756 • ❤️ 1,385 • 1mo ago

---

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 79,427 • ❤️ 764 • 9d ago

---

**[Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)**

*StepFun*

Step-3.7-Flash is a 198B parameter sparse MoE vision-language model with a 256k context window, excelling at multimodal perception, workflow integrity, and code engineering for agentic applications. It offers selectable reasoning levels to balance speed, cost, and cognitive depth, achieving high throughput for production workloads.

`image-text-to-text` `201.4B`

⬇️ 22,715 • ❤️ 246 • 1d ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 1,978 • ❤️ 233 • 6h ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 62,850 • ❤️ 230 • 15h ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 157,457 • ❤️ 589 • 14d ago

---

**[Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)**

*JetBrains*

Mellum2 Thinking is a 12B parameter MoE model designed for complex reasoning tasks, generating explicit chain-of-thought explanations within `<think>` blocks. It excels in multi-step planning, agentic workflows, and math/reasoning-heavy problems, featuring a 131,072 token context length.

`text-generation` `12.1B`

⬇️ 12,157 • ❤️ 195 • 3d ago

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

▲ 221 • 💬 3 • ⭐ 4,829 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 60 • 💬 0 • ⭐ 8,774 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

**[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://huggingface.co/papers/2606.05160)**

*Tianyi Xie, Haotian Zhang, Jinhyung Park et al. (20 authors)*

🏢 NVIDIA

GRAIL generates diverse humanoid manipulation and locomotion data through 3D asset composition and video foundation models, enabling effective sim-to-real transfer for robot control.

▲ 5 • 💬 1 • ⭐ 90 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05160) • [💻 code](https://github.com/NVlabs/GRAIL) • [🔗 project](https://research.nvidia.com/labs/dair/grail/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 38 • 💬 4 • ⭐ 28,372 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 165 • 💬 2 • ⭐ 66,369 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 11 • 💬 1 • ⭐ 79,655 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 58 • 💬 2 • ⭐ 57,680 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 6 • 💬 1 • ⭐ 6,899 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[VibeSearchBench: Benchmarking Long-horizon Proactive Search in the Wild](https://huggingface.co/papers/2605.27882)**

*Xiaohongshu Inc*

🏢 rednote-hilab

LLM-based agents perform poorly on VibeSearch benchmark, which evaluates multi-turn dialogue search scenarios reflecting real user-agent collaboration rather than traditional single-turn query tasks.

▲ 15 • 💬 2 • ⭐ 774 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2605.27882) • [💻 code](https://github.com/VibeBench/VibeSearchBench) • [🔗 project](https://vibebench.github.io/VibeSearchBench.github.io/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`JavaScript`

⭐ 49.5k • 🔱 5.7k • 3m ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 6.0k • 🔱 588 • 2d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 27端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.4k • 🔱 709 • 1d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 3.0k • 🔱 216 • 10h ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.0k • 🔱 305 • 4h ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.9k • 🔱 202 • 3m ago

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

⭐ 1.9k • 🔱 253 • 17h ago

---

---

*Generated by PeekDeck - A glance is all you need*
