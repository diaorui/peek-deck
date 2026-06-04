---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-04T16:00:45.201951+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 04, 2026 at 16:00 UTC  
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

2h ago

---

**[Ran gemma 4 12b on my 3090 yesterday and I think the local model game just changed](https://www.reddit.com/r/artificial/comments/1twgrd1/ran_gemma_4_12b_on_my_3090_yesterday_and_i_think/)**

Got the gguf quantized version running about two hours after release and I genuinely wasn't expecting this from a 12b model. The multimodal stuff actually works, fed it screenshots of my codebase and it parsed the architecture better than most 70b models I've tested. The 256k context window is real and it doesn't fall apart at the edges like llama models do past 32k. Loaded a full repo into context, it tracked references across the whole thing. Single 3090 with q4 quantization runs at about 15 tokens per second which is totally usable for dev work. What gets me is the size range. The 12b sits in this sweet spot where you get strong reasoning without needing multi gpu. Tried the e4b on my laptop with 16gb ram, slower but functional. Already swapped it into my local coding pipeline. The function calling support means I can wire it into my toolchain without the janky workarounds I had before. Native audio input on the 12b is something I haven't touched yet but the implications for voice driven workflows are kind of insane.

8h ago

---

**[Google just dropped Gemma 4 12B on your laptop!!](https://www.reddit.com/r/artificial/comments/1tw0cqv/google_just_dropped_gemma_4_12b_on_your_laptop/)**

bro google just casually released a 12 billion parameter multimodal model that runs on 16gb of ram like… your macbook pro can run this. no cloud. no api calls. no monthly bill. it’s encoder-free, handles images and text, apache 2.0 license so you can do whatever with it commercially the “cloud is the only way” narrative is dying fast. on-device AI is not a gimmick anymore, it’s where the serious money is going

20h ago

---

**[Hassabis says AGI in three years but I keep thinking about the harness layer](https://www.reddit.com/r/artificial/comments/1twpobj/hassabis_says_agi_in_three_years_but_i_keep/)**

The DeepMind CEO predicted AGI could arrive by 2029. Right as Anthropic files for IPO at close to a trillion dollar valuation. The combined target market cap of the AI big three would rival the GDP of most countries. What actually scares me. We already have models that code better than most juniors. We already have agents that run overnight. And the most common complaint I hear from teams is not "my model is not smart enough." It is "I do not know what my agent did, why it cost forty dollars, or whether the output is safe to merge." AGI does not solve that. The problem scales with capability. A smarter agent that runs longer with less oversight is a bigger liability, not a smaller one. The layer that matters is harness. Routing. Isolation. Plan verification. Cost visibility. The stuff that tells you what the agent is about to do before it does it. What keeps it inside a boundary. What lets you audit it after. Anthropic is building Mythos to find vulnerabilities before attackers do. Microsoft is building MXC to isolate agents in execution containers. In my own tiny setup, verdent is just one piece of that harness layer for planning and cost visibility. These are governance layers, not model layers. If AGI is three years away, the winners will not be the ones with the smartest model. They will be the ones who figured out how to aim it.

1h ago

---

**[What model do you use and how many tokens do you consume](https://www.reddit.com/r/artificial/comments/1twoc22/what_model_do_you_use_and_how_many_tokens_do_you/)**

Talking about efficiency and reliability of LLM tools. How many tokens per task, per project, per month

2h ago

---

**[Companies Are Using Reddit to Manipulate ChatGPT and Google AI Search. Peptide companies have been doing AI-engine optimization by spamming the biohackers subreddit to manipulate ChatGPT and Google.](https://www.reddit.com/r/artificial/comments/1tw6hb9/companies_are_using_reddit_to_manipulate_chatgpt/)**

Peptide companies have been doing AI-engine optimization by spamming the biohackers subreddit to manipulate ChatGPT and Google.

🔗 [404 Media](https://www.404media.co/companies-are-using-reddit-to-manipulate-chatgpt-and-google-ai-search/) • 16h ago

---

**[The AI war is moving from models to machines and I don’t think enough people are talking about it](https://www.reddit.com/r/artificial/comments/1twqwoq/the_ai_war_is_moving_from_models_to_machines_and/)**

okay so I’ve been thinking about this for a while and finally wrote it out properly everyone’s still arguing about benchmarks and which model is smarter but like… that’s starting to feel like the wrong fight? the more interesting question is where the model actually runs. on your device, in a cloud DC, on some edge hardware, inside enterprise infrastructure. that placement question is quietly becoming more important than the model quality question a few things that got me thinking about this recently: microsoft’s project solara is not a laptop. it’s basically a concept for hardware built around agents from the ground up, and they’re reportedly doing it on android not windows which says a lot about what they think “agent-native” actually needs to look like nvidia pushing local inference via RTX spark is interesting because it basically challenges the assumption that anything serious has to live in the cloud. latency, privacy, enterprise control requirements, there are real reasons to want compute closer to the user bytedance apparently building custom CPUs is the one that really made me stop. because agentic workloads aren’t just GPU jobs. agents call tools, manage state, orchestrate steps, interact with software systems. that’s a different workload profile entirely and big companies are starting to customize silicon around it anyway I wrote the whole thing up for towards AI if anyone wants to read it. not trying to just drop a link, genuinely curious if people here think the infrastructure angle is getting underplayed or if I’m reading too much into it [link in comments]

35m ago

---

**[Naive question - do local models call into question the business model for AI company profitability?](https://www.reddit.com/r/artificial/comments/1twprik/naive_question_do_local_models_call_into_question/)**

From what I understand Gemma 4 is at least as capable as the best frontier model from only a few years ago. If that becomes a trend (new local-run models get released every year that are as good as the previous frontier models) does that mean a hell of a lot of companies (and almost all individual users) will just use the free local model? Sure, they won't be as good as the very latest frontier model, but won't they be good enough for a large percentage of use cases?

1h ago

---

**[Google’s Gemma 4 12B just dropped - here’s how to run it locally on your Mac](https://www.reddit.com/r/artificial/comments/1twpf9m/googles_gemma_4_12b_just_dropped_heres_how_to_run/)**

Google released Gemma 4 12B today. It’s a solid open-source model (Apache 2.0) that’s multimodal and runs really well on Macs with 16GB or more unified memory. Good at reasoning, coding, and agent stuff. Quick Mac-friendly info • 12B parameters, fits nicely on M2/M3/M4 Macs (especially with Q4/Q5 quant) • 256K context • Text + vision + audio support Easiest way to run it: Ollama 1. Download and install Ollama from ollama.com (the Mac app is super simple). Or use Homebrew if you prefer. 2. Open Terminal and pull the model: ollama pull gemma4:12b 3. Run it: ollama run gemma4:12b That’s it. You can start chatting right away. Mac tips: • Ollama uses Metal automatically so it runs pretty fast on Apple Silicon. • 16GB Macs handle the 12B model fine. 32GB feels even better. • Great for pairing with Continue.dev in VS Code if you code a lot. Other options if Ollama isn’t your thing: LM Studio (nice GUI), or llama.cpp for more control. Has anyone tried the image or audio features locally yet? How fast is it on your machine? Drop your specs and results if you test it.​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​

1h ago

---

**[Companies are letting AI gains go to waste, study says](https://www.reddit.com/r/artificial/comments/1tw5v4v/companies_are_letting_ai_gains_go_to_waste_study/)**

A recent study by Boston Consulting Group highlights a significant increase in employee adoption of AI tools, with 74% of non-managerial white-collar workers using them regularly. More than 4 in 10 of those professionals report that artificial intelligence saves them at least a day's worth of time every week. However, many companies face challenges converting those efficiency gains into measurable value, and the technology's impact varies across industries. When it comes to AI, according to the study's authors, "strategy matters more than tools."

🔗 [LinkedIn](https://www.linkedin.com/news/story/companies-are-letting-ai-efficiencies-go-to-waste-study-8914154/?utm_source=share&utm_campaign=reddit&utm_content=storyline&utm_term=artificial) • 16h ago

---

---

## Google News: "ai"

**[The Small-Business Owners Managing Whole Armies of A.I. Employees](https://www.nytimes.com/2026/06/04/magazine/ai-agents-openclaw-small-business.html)**

The New York Times • 6h ago

---

**[No, Artificial Intelligence Is Not Conscious](https://www.theatlantic.com/philosophy/2026/06/no-artificial-intelligence-is-not-conscious/687378/)**

Taken to its logical conclusion, this line of thinking is absurd—and damning.

The Atlantic • 23h ago

---

**[Broadcom stock sinks in after hours as AI chip forecast disappoints](https://finance.yahoo.com/markets/article/broadcom-stock-sinks-in-after-hours-as-ai-chip-forecast-disappoints-165602504.html)**

Broadcom shares sank in after-hours following the chipmaker's quarterly results.

Yahoo Finance • 5h ago

---

**[Broadcom stock plunges on weak software sales, unchanged AI chip forecast for the year](https://www.cnbc.com/2026/06/03/broadcom-avgo-earnings-report-q2-2026.html)**

Broadcom reported fiscal second-quarter results on Wednesday and missed estimates for revenue.

CNBC • 19h ago

---

**[Broadcom Is Drowning in AI Orders. Why Aren’t Investors Impressed?](https://www.trefis.com/stock/avgo/articles/601481/broadcom-is-drowning-in-ai-orders-why-arent-investors-impressed/2026-06-04)**

Broadcom (AVGO)'s stock took a 14.0% haircut before the market even opened on Thursday. You'd think the company had just guided to a collapse. Instead, the CEO was talking about “accelerating growth in AI semiconductor revenue” and demand that is “simply insatiable.

Trefis • 51m ago

---

**[Indeed's CMO wants marketers to get AI-smart without losing the human touch](https://www.businessinsider.com/indeeds-cmo-says-ai-powers-hyper-targeting-and-sales-strategy-2026-6)**

As Indeed launches a new brand campaign, CMO James Whitemore talks about smart uses of AI, and the importance of fandom

Business Insider • 12m ago

---

**[Inside the Trump-backed push to bring AI doctors into American medicine](https://www.washingtonpost.com/technology/2026/06/04/inside-trump-backed-push-bring-ai-doctors-into-american-medicine/)**

The administration is laying the groundwork for chatbots that can diagnose illness and prescribe medicine, but physicians say AI can introduce more problems.

The Washington Post • 10m ago

---

**[Samsung Introduces Next-Gen Galaxy Watch Features for AI-Powered Everyday Health Companion](https://news.samsung.com/uk/samsung-introduces-next-gen-galaxy-watch-features-for-ai-powered-everyday-health-companion)**

New update transforms the user experience from passive tracking to proactive guidance with a suite of personalised, intuitive daily insights

samsung.com • 16h ago

---

**[Amazon engineers in Seattle slam employer for building AI data centers while laying off 30,000 staffers](https://www.cnbc.com/2026/06/03/amazon-engineers-in-seattle-slam-employer-for-ai-data-amid-layoffs.html)**

Amazon engineers called out their employer for conducting mass layoffs while it commits to spending $200 billion this year on AI infrastructure.

CNBC • 16h ago

---

**[AI is ushering in a new era of colonialism](https://www.axios.com/2026/06/04/ai-data-extraction-colonialism)**

Axios • 6h ago

---

---

## HackerNews: "ai"

**[Adafruit receives demand letter from Fenwick legal counsel on behalf of Flux.ai](https://news.ycombinator.com/item?id=48368121)**

electronics, open source hardware, hacking and more...

⬆️ 674 • 💬 280 • 2d ago • [Adafruit Industries - Makers, hackers, artists, designers and engineers!](https://blog.adafruit.com/)

---

**[Uber's $1,500/month AI limit is a useful signal for AI tool pricing](https://news.ycombinator.com/item?id=48383056)**

I wrote the other day about Uber blowing its 2026 AI budget in four months, and how that wasn't particularly surprising given they would have set that budget in 2025, …

⬆️ 559 • 💬 683 • 1d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Jun/3/uber-caps-usage/)

---

**[Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes](https://news.ycombinator.com/item?id=48392004)**

The percentage of failing grades in multiple UC Berkeley computer science classes in spring 2026 is significantly higher than past semesters and marks a departure from the department’s grading guidelines.

⬆️ 552 • 💬 509 • 15h ago • [Daily Cal | Berkeley news](https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html)

---

**[AI Agent Guidelines for CS336 at Stanford](https://news.ycombinator.com/item?id=48359232)**

Student version of Assignment 1 for Stanford CS336 - Language Modeling From Scratch - stanford-cs336/assignment1-basics

⬆️ 499 • 💬 153 • 2d ago • [GitHub](https://github.com/stanford-cs336/assignment1-basics/blob/main/CLAUDE.md)

---

**[32GB of DDR5 now costs $375 – AI shortage continues to squeeze PC building](https://news.ycombinator.com/item?id=48383241)**

Lower-priced kits are disappearing by the day

⬆️ 413 • 💬 370 • 1d ago • [Tom's Hardware](https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building)

---

**[AI outperforms law professors in Stanford Law study](https://news.ycombinator.com/item?id=48377761)**

A groundbreaking study led by Stanford Law School Professor Julian Nyarko reveals that law professors overwhelmingly prefer AI-generated answers to st

⬆️ 406 • 💬 356 • 1d ago • [Stanford Law School](https://law.stanford.edu/press/ai-outperforms-law-professors-in-stanford-law-study/)

---

**[DuckDuckGo makes its 'no-AI' search engine easier to access as its traffic booms](https://news.ycombinator.com/item?id=48359130)**

Alternative search engine DuckDuckGo launches 'no AI' web extensions for Chrome and Firefox users.

⬆️ 309 • 💬 150 • 2d ago • [TechCrunch](https://techcrunch.com/2026/06/01/duckduckgo-makes-its-no-ai-search-engine-easier-to-access-as-its-traffic-booms/)

---

**[Mathematicians issue warning as AI rapidly gains ground](https://news.ycombinator.com/item?id=48382052)**

⬆️ 271 • 💬 310 • 1d ago • [science.org](https://www.science.org/content/article/mathematicians-issue-warning-ai-rapidly-gains-ground)

---

**[Florida sues OpenAI and Sam Altman over AI risks](https://news.ycombinator.com/item?id=48358667)**

⬆️ 268 • 💬 194 • 2d ago • [politico.com](https://www.politico.com/news/2026/06/01/openai-hit-with-florida-lawsuit-00944215)

---

**[Alphabet announces $80B equity capital raise to expand AI infra and compute](https://news.ycombinator.com/item?id=48362515)**

⬆️ 254 • 💬 236 • 2d ago • [abc.xyz](https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Proposed-80-Billion-Equity-Capital-Raise-to-Expand-AI-Infrastructure-and-Compute-2026-b0myAMewCa/default.aspx)

---

---

## YouTube Videos: "ai"

**[Best AI Video Agents in 2026 (Most Realistic)](https://www.youtube.com/watch?v=uQulSf5Mci0)**

Best AI Video Agents in 2026 Use The Best AI Video Agent https://youricreates.com/higgsfield-agent In this video, I compare ...

📺 Youri van Hofwegen

👁️ 4K • ⏱️ 8:11 • 1h ago

---

**[Quantum Just Killed AI Data Centers](https://www.youtube.com/watch?v=4o_evxWvsx0)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *A quantum computer just solved in minutes ...

📺 Julia McCoy

👁️ 46K • 👍 3K • 💬 312 • ⏱️ 7:25 • 17h ago

---

**[Microsoft Just Shocked The Entire AI World: 7 New AI Models](https://www.youtube.com/watch?v=i1dkkxLWaWg)**

Microsoft just revealed seven in-house AI models, Microsoft IQ, Scout, Codename MDASH, and Majorana 2, turning its AI push ...

📺 AI Revolution

👁️ 53K • 👍 2K • 💬 313 • ⏱️ 16:42 • 17h ago

---

**[The Easiest Way To Make AI Influencers That Stay Consistent](https://www.youtube.com/watch?v=jZJjop9VsxQ)**

Learn How To create AI Influencers with this new free AI tool Tool you need: https://higgsfield.ai?fpr=dankieft&fp_sid=dash In this ...

📺 Dan Kieft

👁️ 5K • 💬 9 • ⏱️ 15:15 • 1h ago

---

**[Google’s AI Search Just Exposed The Whole Sh*tshow](https://www.youtube.com/watch?v=jQyKd1_e3Xg)**

Google says AI Mode is the biggest upgrade to Search in 25 years. But users are quietly moving to the exit and the exit says “No ...

📺 House of El - AI

👁️ 245K • 👍 17K • 💬 3K • ⏱️ 19:32 • 2d ago

---

**[Did The Stock Market AI Bubble Just Burst? Broadcom Crash &amp; SpaceX IPO Warning](https://www.youtube.com/watch?v=XrhlAS53AnQ)**

Welcome to Verified Investing! In today's technical analysis, Chief Market Strategist Gareth Soloway breaks down the massive ...

📺 Gareth Soloway

👁️ 23K • 👍 2K • 💬 229 • ⏱️ 10:58 • 4h ago

---

**[They Aren&#39;t Building AI Data Centers. (It&#39;s Way Worse)](https://www.youtube.com/watch?v=7viqI2WFfog)**

The Secret Threat Hidden Inside America's New AI Data Centers In this 51-49 mini-documentary, James uncovers the real ...

📺 51-49 with James Li

👁️ 110K • 👍 15K • 💬 2K • ⏱️ 16:58 • 1d ago

---

**[Godfather of AI WARNS: We Cannot Stop What&#39;s Coming](https://www.youtube.com/watch?v=u30XUzgNhQw)**

Geoffrey Hinton, the Nobel Prize-winning scientist widely known as the Godfather of AI, says the race to build more powerful ...

📺 Neural Nutshell

👁️ 17K • 👍 389 • 💬 124 • ⏱️ 19:43 • 23h ago

---

**[AI Bubble Will Burst Eventually Says Bridgewater&#39;s Ray Dalio](https://www.youtube.com/watch?v=WZ7mmTrSgxI)**

Bridgewater Associates Founder Ray Dalio says the debt burden has passed a "point of no return." He speaks with Bloomberg's ...

📺 Bloomberg Podcasts

👁️ 119K • 👍 2K • 💬 341 • ⏱️ 13:20 • 23h ago

---

**[Add THIS Before Every AI Prompt! (Gemini, ChatGPT, Claude)](https://www.youtube.com/watch?v=tk4Ljz9p-UI)**

Most AI users waste time rewriting prompts and fixing poor results. Discover a simple prompt technique that helps create more ...

📺 Simpletivity

👁️ 48K • 👍 2K • 💬 89 • ⏱️ 6:16 • 2d ago

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

⬇️ 72,114 • ❤️ 495 • 7h ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 14,866 • ❤️ 348 • 4h ago

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

⬇️ 1,978 • ❤️ 233 • 4h ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 62,850 • ❤️ 230 • 13h ago

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

⭐ 48.8k • 🔱 5.6k • 4m ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 6.0k • 🔱 588 • 2d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 27端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.4k • 🔱 707 • 1d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 3.0k • 🔱 216 • 8h ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.0k • 🔱 303 • 2h ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.8k • 🔱 200 • 1h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.7k • 🔱 268 • 2d ago

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

⭐ 1.9k • 🔱 253 • 14h ago

---

---

*Generated by PeekDeck - A glance is all you need*
