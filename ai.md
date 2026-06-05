---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-05T03:52:38.889415+00:00'
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

**Last Updated:** June 05, 2026 at 03:52 UTC  
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

14h ago

---

**[$2.5T in AI spending this year. 95% produces zero P&L impact.](https://www.reddit.com/r/artificial/comments/1twupqt/25t_in_ai_spending_this_year_95_produces_zero_pl/)**

Gartner updated their 2026 forecast to $2.5 trillion in global AI spending. Same week, MIT's NANDA Initiative dropped a follow-up: 95% of enterprise gen AI projects deliver zero measurable return. Not low return. Zero. I've been on the delivery side of 14 of these projects since January. The MIT number doesn't surprise me. If anything it's generous. 1. 73% of the engineering work that gets AI into production has nothing to do with the model. Data pipelines, integration layers, legacy system remediation, human-in-the-loop tooling. That's where the hours go. The model is 27% of the work but gets 70%+ of the budget. Every time. 2. The budget ratio between projects that ship and projects that stall is almost exactly inverted. We tracked this through ticket history and commit logs across 14 engagements. Projects that made it to production: roughly 30% model, 70% infrastructure. Projects that stalled: 70% model, 30% infrastructure. Most companies think they're at 50/50. They're not even close. 3. One client went from 71% Copilot adoption to 34% in six months. Two other AI platform licenses dropped under 12%. Combined licensing: $340K/year. The tools worked fine. Nobody redesigned workflows to actually use them. 4. The median data error rate across our engagements is 14%. Teams always guess 5-10%. One client found 23% in month four of a $310K build. That's two months of an ML engineer building training pipelines against garbage data. $36K in salary discovering a problem a data audit would have caught in a week. 5. Medtech company. Four concurrent AI pilots. No kill criteria. $920K in engineer salary. Eleven months. Shipped: nothing. I've now seen this at six companies now. Nobody defines when to stop spending. So nobody stops. 6. Individual gains are real. Company-level ROI stays flat. HCLTech and Writer both found this from different angles. Only 29% of companies see significant ROI from gen AI, despite people at their desks reporting productivity jumps as high as 5x. I mean, the value is clearly there at the individual level. It evaporates somewhere between the IC and the P&L and nobody has a clean explanation for why yet. What connects all of it: the model stopped being the constraint a while ago. MIT's 5% that actually moved the P&L all started with data infrastructure and added model work after. Most companies still do it the other way around, because that's where the conference keynotes and the board excitement live. Every CFO I've shown these numbers to adjusted their allocation. Not sure what that says about the budgets they were running before. Sources: Gartner AI Spending Forecast (May 2026), MIT NANDA "GenAI Divide" report, HCLTech Enterprise AI Report (May 2026), Writer Enterprise AI Survey 2026 I wrote a longer breakdown with the three budget patterns and the pre-mortem questions we run before every engagement if you're curious to learn more on the topic. What do you think about all this though?

10h ago

---

**[Sam, Dario, and Demis Hassabis have signed a joint open letter calling for Law Protecting against Biological Weapons.](https://www.reddit.com/r/artificial/comments/1tx7brf/sam_dario_and_demis_hassabis_have_signed_a_joint/)**

OpenAI’s Sam Altman, Anthropic’s Dario Amodei and Demis Hassabis of Google’s DeepMind AI lab with other top execs signed a letter urging Congress to require safeguards when companies order synthetic DNA and RNA, a key step in developing certain vaccines and biotech breakthroughs.

🔗 [wsj.com](https://www.wsj.com/politics/policy/top-ai-ceos-call-for-law-protecting-against-biological-weapons-88f2f99f?referrer=https%3A%2F%2Freddit.com) • 2h ago

---

**[Ran gemma 4 12b on my 3090 yesterday and I think the local model game just changed](https://www.reddit.com/r/artificial/comments/1twgrd1/ran_gemma_4_12b_on_my_3090_yesterday_and_i_think/)**

Got the gguf quantized version running about two hours after release and I genuinely wasn't expecting this from a 12b model. The multimodal stuff actually works, fed it screenshots of my codebase and it parsed the architecture better than most 70b models I've tested. The 256k context window is real and it doesn't fall apart at the edges like llama models do past 32k. Loaded a full repo into context, it tracked references across the whole thing. Single 3090 with q4 quantization runs at about 15 tokens per second which is totally usable for dev work. What gets me is the size range. The 12b sits in this sweet spot where you get strong reasoning without needing multi gpu. Tried the e4b on my laptop with 16gb ram, slower but functional. Already swapped it into my local coding pipeline. The function calling support means I can wire it into my toolchain without the janky workarounds I had before. Native audio input on the 12b is something I haven't touched yet but the implications for voice driven workflows are kind of insane.

20h ago

---

**[ive started to realize the "this changes everything" AI post is literally the same post every month and i keep falling for it anyway](https://www.reddit.com/r/artificial/comments/1twsx01/ive_started_to_realize_the_this_changes/)**

so gemma 4 dropped and my feed is three versions of the same post. "ran it last night, the local game just changed". "the cloud narrative is dying". and i caught myself getting excited and downloading it at 1am like i did for the last one. and the one before that. heres the thing thats been bugging me. i went back and looked at my own saved posts from like 8 months ago. same exact words. "this finally replaces X". "cant believe this runs on my laptop". "were so back". different model name, copy paste emotion. and almost none of those models are in my actual rotation now. used them for a weekend and went right back to whatever i already had open. i think the release is the dopamine, not the model. the download IS the fun part. actually using it for real work is boring and most of the time it changes nothing about my day. i still do the same tasks the same way. the model got better on paper and my life is identical. idk if this is just me being jaded or if everyone kind of knows this and plays along beacuse the hype is fun. im not even mad at it honestly. its just wierd to notice youve been stuck in a loop. the "everything changed" never actually changes the tuesday after. anyway gemma 4 is probably great. i downloaded it. i will use it twice. see you all next month for the same thread with a diffrent number on it

11h ago

---

**[I am now negotiating with AI as part of my job, and it's going like you would expect. How can I circumvent it to speak to a representative?](https://www.reddit.com/r/artificial/comments/1tx56d7/i_am_now_negotiating_with_ai_as_part_of_my_job/)**

TLDR - auto lenders are using AI bots to negotiate insurance settlements with inaccurate information. How can I Captain Kirk them and get a live person on the phone? I am an insurance claims adjuster. Recently, several high-interest auto loan lenders have begun using AI (both through email and phone calls) to dispute the total loss values for our claims. For those of you that have never dealt with a total loss - the value of a vehicle is (usually) determined by seeing what comparable vehicles are selling for on the market, and making adjustments based on the condition, mileage, etc. between those vehicles and the totalled vehicle. If a customer disagrees, they can hire an appraiser and the company will hire an independent appraiser, and the two will come to an agreement. The lender gets paid the amount minus the customer's deductible, and if it doesn't fully pay off the loan, unfortunately the customer will be responsible for the balance. Lately, AI calls and emails have been coming from these lenders disputing the amounts, and often based on egregiously incorrect information. They provide cherry picked comparisons to try to boost the vehicle values, and sometimes they aren't the same year, make, or model. Sometimes mileage and condition isn't factored in, sometimes they are tricked-out show cars someone advertised on a FSBO site. The real problem is, we have to waste our time researching all of this to see if any of the data is correct. When we respond pointing out the flawed comparisons, they only come back with more flawed comparisons. If we argue long enough, they will invoke the appraisal clause on the customer's behalf. Their appraiser is another AI system with a cutesy name. All efforts to reach humans at these lenders are essentially turned away - we are told we need to deal with the system. I am open to any advice you folks have - how can we get these AI systems to basically give up and get us in touch with a real person? I'm not trying to screw anyone out of a fair settlement, I just want to stop having my time wasted by these Temu AI systems.

3h ago

---

**[Google just dropped Gemma 4 12B on your laptop!!](https://www.reddit.com/r/artificial/comments/1tw0cqv/google_just_dropped_gemma_4_12b_on_your_laptop/)**

bro google just casually released a 12 billion parameter multimodal model that runs on 16gb of ram like… your macbook pro can run this. no cloud. no api calls. no monthly bill. it’s encoder-free, handles images and text, apache 2.0 license so you can do whatever with it commercially the “cloud is the only way” narrative is dying fast. on-device AI is not a gimmick anymore, it’s where the serious money is going

1d ago

---

**[Cloudflare warns bot and agentic traffic has overtaken human web traffic](https://www.reddit.com/r/artificial/comments/1tx2nlt/cloudflare_warns_bot_and_agentic_traffic_has/)**

Yeah, so "AI will eat the world" or "AI changes everything" - well, its certainly changed traffic patterns on the web.

🔗 [deadstack.net](https://deadstack.net/cluster/cloudflare-warns-bot-and-agentic-traffic-has) • 5h ago

---

**[What is the worst thing you can imagine yourself doing to someone else with jailbroken A](https://www.reddit.com/r/artificial/comments/1tx911k/what_is_the_worst_thing_you_can_imagine_yourself/)**

Two things happened to me this week. First, the shocking power of agentic AI finally hit me at work. Power of God... Second, I read anthropics warning about recursive self-improvement in WSJ. It mentioned how some people are freaking out about the mere suggestion of restricting open source LLMs. It made me wonder if some of us are clueless about how dark the dark side of the power of God could be. I'm proposing a very uncomfortable thought experiment. An edge case. But an unfortunately long and sharp edge. I am asking all you people out there to think of the darkest thing you could see yourself doing with an unchained AI, perhaps at the worst moment in your life... Actually no, I'm not asking that. Let's do this AI style. I want you to imagine the worst version of yourself and then I want you to simulate the worst version of yourself imagining the worst thing they would do at the worst point in their life to their most hated enemy. If people answer honestly, this thread will get very disturbing. I'd ask the moderators not to take it down. It's an exploration of what's soon to be possible. And a conversation not likely to happen unless somebody explicitly prompts it. Its value to public discourse is one of safety. Generally speaking, our public servants are good people. They aren't inclined to let their mind to go where the worst of us might go with this technology. If nobody ever says out loud, how will we know to protect ourselves as a society?

41m ago

---

**[Horus Image Generation is here! 🤩📷](https://www.reddit.com/r/artificial/comments/1tx8zah/horus_image_generation_is_here/)**

https://preview.redd.it/n55ohr6wrd5h1.png?width=1537&format=png&auto=webp&s=991397299a33b91459c9b33597ea920bf43abc28 I'm not here to promote my work or make money from what I'm about to say. I'm here to say that Egypt is already part of the AI race. Today, at TokenAI, we announced our first image generation model and the first release in the Horus Lens family: Horus Lens 1.0. Horus Lens is a family of models specialized in text-to-image generation, forming a dedicated branch of the broader Horus model family developed and owned by TokenAI. This launch marks an important step forward for Egypt's AI ecosystem and highlights the growing role of the region in advancing artificial intelligence technologies.

44m ago

---

---

## Google News: "ai"

**['World-first' vaccine designed by artificial intelligence](https://www.bbc.com/news/articles/crrpggegwe0o)**

Cambridge scientists say they have, for the first time, tested a vaccine designed by AI.

BBC • 4h ago

---

**[Kevin O'Leary says Utah AI data center project will shrink after lawmakers demand cuts](https://www.foxbusiness.com/technology/kevin-oleary-says-utah-ai-data-center-project-shrink-lawmakers-demand-cuts)**

Kevin O'Leary says he will reduce the proposed Stratos AI data center in Utah after state Senate President Adams called for a 75% cut in its footprint.

Fox Business • 3h ago

---

**[Kevin O’Leary says he will shrink his Utah AI data center project after political backlash](https://www.nbcnews.com/tech/tech-news/kevin-oleary-utah-data-center-project-stratos-ai-shrink-hayley-rcna348430)**

The “Shark Tank” mogul said he would cut the 40,000-acre project by roughly half in a letter sent Thursday to Utah’s Senate president.

NBC News • 12h ago

---

**[Inside the AI Boom's Arctic Outpost](https://time.com/article/2026/06/03/ai-norway-nscale-data-center/)**

Above the Arctic Circle, Nscale is turning a remote Norwegian valley into one of Europe’s largest AI data centers.

Time Magazine • 15h ago

---

**[U.S. Officials Discuss Taking Financial Stakes in AI Industry](https://www.wsj.com/tech/ai/u-s-officials-discuss-taking-financial-stakes-in-ai-industry-b654d41a)**

WSJ • 34m ago

---

**[US officials eye government stakes in AI companies, NOTUS reports](https://www.reuters.com/legal/transactional/us-officials-eye-government-stakes-ai-companies-notus-reports-2026-06-05/)**

Reuters • 3h ago

---

**[Senior U.S. Officials Eye Government Shares in AI Giants - News of the United States](https://www.notus.org/technology/trump-ai-stake-openai)**

An agreement to give the U.S. government equity stakes in AI companies could have seismic consequences.

News of the United States - NOTUS • 5h ago

---

**[South Korea labor minister calls on tech firms to share excess AI profits with suppliers, staff: Reuters](https://www.cnbc.com/2026/06/05/south-korea-labor-minister-calls-on-tech-firms-to-share-excess-ai-profits-with-suppliers-staff.html)**

South Korea's labor minister called on the country's major tech firms to share the spoils of their profits, warning of worsening inequality risks.

CNBC • 51m ago

---

**[Peggy Flanagan slams ad for using "AI deepfake"](https://www.cbsnews.com/minnesota/news/peggy-flanagan-slams-ad-for-using-ai-deepfake/)**

Minnesota Lieutenant Governor and US Senate candidate Peggy Flanagan slammed an attack ad against her for "using an AI deepfake."

CBS News • 2m ago

---

**[Stocks drop as AI rally pauses, US-Iran peace talks stall](https://www.reuters.com/world/china/global-markets-global-markets-2026-06-05/)**

Reuters • 2h ago

---

---

## HackerNews: "ai"

**[Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes](https://news.ycombinator.com/item?id=48392004)**

The percentage of failing grades in multiple UC Berkeley computer science classes in spring 2026 is significantly higher than past semesters and marks a departure from the department’s grading guidelines.

⬆️ 744 • 💬 721 • 1d ago • [Daily Cal | Berkeley news](https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html)

---

**[Adafruit receives demand letter from Fenwick legal counsel on behalf of Flux.ai](https://news.ycombinator.com/item?id=48368121)**

electronics, open source hardware, hacking and more...

⬆️ 678 • 💬 281 • 2d ago • [Adafruit Industries - Makers, hackers, artists, designers and engineers!](https://blog.adafruit.com/)

---

**[Uber's $1,500/month AI limit is a useful signal for AI tool pricing](https://news.ycombinator.com/item?id=48383056)**

I wrote the other day about Uber blowing its 2026 AI budget in four months, and how that wasn't particularly surprising given they would have set that budget in 2025, …

⬆️ 607 • 💬 749 • 1d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Jun/3/uber-caps-usage/)

---

**[32GB of DDR5 now costs $375 – AI shortage continues to squeeze PC building](https://news.ycombinator.com/item?id=48383241)**

Lower-priced kits are disappearing by the day

⬆️ 421 • 💬 383 • 1d ago • [Tom's Hardware](https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building)

---

**[AI outperforms law professors in Stanford Law study](https://news.ycombinator.com/item?id=48377761)**

A groundbreaking study led by Stanford Law School Professor Julian Nyarko reveals that law professors overwhelmingly prefer AI-generated answers to st

⬆️ 408 • 💬 357 • 2d ago • [Stanford Law School](https://law.stanford.edu/press/ai-outperforms-law-professors-in-stanford-law-study/)

---

**[When AI Builds Itself: Our progress toward recursive self-improvement](https://news.ycombinator.com/item?id=48400842)**

Our progress toward recursive self-improvement, and its implications.

⬆️ 372 • 💬 484 • 11h ago • [anthropic.com](https://www.anthropic.com/institute/recursive-self-improvement)

---

**[Anthropic's open-source framework for AI-powered vulnerability discovery](https://news.ycombinator.com/item?id=48403980)**

Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize - anthropics/defending-code-reference-harness

⬆️ 308 • 💬 98 • 7h ago • [GitHub](https://github.com/anthropics/defending-code-reference-harness)

---

**[Mathematicians issue warning as AI rapidly gains ground](https://news.ycombinator.com/item?id=48382052)**

⬆️ 290 • 💬 335 • 1d ago • [science.org](https://www.science.org/content/article/mathematicians-issue-warning-ai-rapidly-gains-ground)

---

**[Trump signs downsized AI order after weeks of reversals](https://news.ycombinator.com/item?id=48372628)**

⬆️ 236 • 💬 172 • 2d ago • [politico.com](https://www.politico.com/news/2026/06/02/trump-signs-downsized-ai-order-00946389)

---

**[Google employees internally share memes about how its AI sucks](https://news.ycombinator.com/item?id=48400311)**

Google’s CEO says 75% of the company’s code is AI-generated. The people who write that code say the AI they’re using is overhyped.

⬆️ 149 • 💬 103 • 12h ago • [404 Media](https://www.404media.co/google-employees-internally-share-memes-about-how-its-ai-sucks/)

---

---

## YouTube Videos: "ai"

**[The AI Expert Who Will Change Your Mind About AI - Josh Tyrangiel](https://www.youtube.com/watch?v=R-Ck3W6issI)**

I've been saying it for years, AI is the most important conversation we're having right now. Josh Tyrangiel spent a year hunting for ...

📺 Anthony Scaramucci

👁️ 12K • 👍 554 • 💬 51 • ⏱️ 30:04 • 11h ago

---

**[Quantum Just Killed AI Data Centers](https://www.youtube.com/watch?v=4o_evxWvsx0)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *A quantum computer just solved in minutes ...

📺 Julia McCoy

👁️ 67K • 👍 4K • 💬 455 • ⏱️ 7:25 • 1d ago

---

**[Google’s AI Search Just Exposed The Whole Sh*tshow](https://www.youtube.com/watch?v=jQyKd1_e3Xg)**

Google says AI Mode is the biggest upgrade to Search in 25 years. But users are quietly moving to the exit and the exit says “No ...

📺 House of El - AI

👁️ 266K • 👍 19K • 💬 4K • ⏱️ 19:32 • 2d ago

---

**[Microsoft Just Shocked The Entire AI World: 7 New AI Models](https://www.youtube.com/watch?v=i1dkkxLWaWg)**

Microsoft just revealed seven in-house AI models, Microsoft IQ, Scout, Codename MDASH, and Majorana 2, turning its AI push ...

📺 AI Revolution

👁️ 71K • 👍 2K • 💬 357 • ⏱️ 16:42 • 1d ago

---

**[Add THIS Before Every AI Prompt! (Gemini, ChatGPT, Claude)](https://www.youtube.com/watch?v=tk4Ljz9p-UI)**

Most AI users waste time rewriting prompts and fixing poor results. Discover a simple prompt technique that helps create more ...

📺 Simpletivity

👁️ 64K • 👍 3K • 💬 101 • ⏱️ 6:16 • 2d ago

---

**[Ukraine is now the world&#39;s AI war lab | DW News](https://www.youtube.com/watch?v=Gfqdf4JFErU)**

Drones and AI combat technology are being innovated at lightning speed by Ukraine in its defense against the Russian invasion.

📺 DW News

👁️ 105K • 👍 2K • 💬 294 • ⏱️ 10:02 • 1d ago

---

**[This 900,000 Cores &amp; 3-Billion Transistor AI Chip Just Made Nvidia’s AI GPUs Look Like a JOKE!](https://www.youtube.com/watch?v=qaXQgz4ddQQ)**

For years, Nvidia dominated AI hardware so completely that most people treated it like the only serious option. This video breaks ...

📺 Evolving AI

👁️ 13K • 👍 305 • 💬 49 • ⏱️ 10:21 • 12h ago

---

**[The AI backlash: Why Gen Z is pushing back | The Global Story](https://www.youtube.com/watch?v=Mun_KJYXsco)**

A 2025 Harvard poll of young people in the US found that a majority see AI as a threat to their career prospects. And in recent ...

📺 BBC News

👁️ 47K • 👍 1K • 💬 364 • ⏱️ 19:44 • 2d ago

---

**[Carney announces government&#39;s AI strategy](https://www.youtube.com/watch?v=1MqCvy0HR9k)**

Prime Minister Mark Carney holds a news conference in Toronto to announce the government's strategy on artificial intelligence.

📺 CBC News

👁️ 27K • 👍 528 • ⏱️ 51:40 • 11h ago

---

**[AI Pioneer Geoffrey Hinton: AI Is Conscious, Superintelligence is Coming, And We Should Be Worried](https://www.youtube.com/watch?v=p7t1Q_p2gZs)**

Geoffrey Hinton is an AI pioneer, a Nobel Prize winner, and a professor emeritus at the University of Toronto. Hinton joins Big ...

📺 Alex Kantrowitz

👁️ 12K • 👍 638 • 💬 218 • ⏱️ 54:54 • 11h ago

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

⬇️ 14,866 • ❤️ 406 • 15h ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 72,114 • ❤️ 507 • 18h ago

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

⬇️ 62,850 • ❤️ 279 • 6h ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 1,978 • ❤️ 267 • 15h ago

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

⭐ 51.7k • 🔱 6.0k • 35m ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 6.1k • 🔱 591 • 2d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 27端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.4k • 🔱 711 • 1d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.0k • 🔱 306 • 14h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.8k • 🔱 273 • 2d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 403 • 14d ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 130 • 6h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.7k • 🔱 150 • 1d ago

---

**[Helvesec/rmux](https://github.com/Helvesec/rmux)**

Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

`Rust` `agent` `ai` `cli` `linux` `macos`

⭐ 1.5k • 🔱 67 • 5h ago

---

**[asz798838958/aBaiAutoplus](https://github.com/asz798838958/aBaiAutoplus)**

多平台 AI 账号自动注册与管理 · 协议化付款一键开通 ChatGPT Plus

`Python`

⭐ 1.5k • 🔱 685 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
