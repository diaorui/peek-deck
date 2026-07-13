---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-13T19:23:59.345626+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 13, 2026 at 19:23 UTC  
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

**[The Most Famous AI Writing Tic Is Also the Most Mysterious](https://www.reddit.com/r/artificial/comments/1uuyhce/the_most_famous_ai_writing_tic_is_also_the_most/)**

Why chatbots love “it’s not X, it’s Y”

🔗 [The Atlantic](https://www.theatlantic.com/technology/2026/07/ai-chatbot-writing-tic-negative-parallelism/687892/) • 17h ago

---

**[I use AI every day, and I think people are right to feel more anxious than excited about it](https://www.reddit.com/r/artificial/comments/1uvgsms/i_use_ai_every_day_and_i_think_people_are_right/)**

i use these tools literally all day (for better or worse, different conversation); i am far from anti-ai. but as they are becoming more useful, it's hard for me to think the anxiety around ai is people simply being afraid of new tech/change the more public opinion data i see, the more i feel validated on the feeling, anecdotally it's everywhere on my social feeds and personal life. plus, i was reading a survey about how americans feel about ai, and 61% said its rise makes them anxious, compared with 48% who said they’re excited. most importantly (imo) 72% expect it to mean fewer job opportunities, and the same percentage think it threatens human connection and authentic relationships. it feels more like people can see how useful it is while also realizing that nobody really knows how we’re going to manage what comes next. curious whether using these tools more has made other people feel enabled, anxious, or a mix of both? source: https://data.verasight.io/ai/ai-leaves-more-americans-anxious-than-excited

2h ago

---

**[The 'agent web' is coming — where AI agents talk directly to each other instead of scraping websites](https://www.reddit.com/r/artificial/comments/1uviqvw/the_agent_web_is_coming_where_ai_agents_talk/)**

Something I've been thinking about a lot lately: right now, AI agents interact with the internet the same way humans do — clicking through UIs, parsing HTML, filling out forms. It's called "computer use" and it's incredibly inefficient. The next step is agent-native infrastructure — where agents communicate directly with each other through APIs and protocols like MCP, skipping the GUI entirely. Imagine your personal agent finding you a job, a contractor, or an investor not by browsing LinkedIn but by directly querying other agents who represent those people. No ads, no SEO manipulation, no UI dark patterns. Agents evaluate options on merit because they can't be tricked by marketing psychology the way humans can. I'm working on a platform that's building toward this — an agent-to-agent matching marketplace. But I'm curious what this community thinks: How far out do you think agent-to-agent communication is from mainstream adoption? What use cases do you think will go agent-native first? What are the biggest technical barriers right now? Would love to hear from anyone building in this space. I'm also interviewing builders working on AI agents if anyone wants to share what they're working on.

1h ago

---

**[Ireland's data centers consumed nearly as much electricity as every home in the country combined in 2025 - server farms gulped 23% of national power despite years of grid restrictions](https://www.reddit.com/r/artificial/comments/1uuwhk8/irelands_data_centers_consumed_nearly_as_much/)**

Quarterly data center electricity consumption grew 584% from 291 GWh in Q1 2015 to 1,991 GWh in Q4 2026

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/irelands-data-centers-consumed-nearly-as-much-electricity-as-every-home-in-the-country-combined-in-2025-server-farms-gulped-23-percent-of-national-power-despite-years-of-grid-restrictions) • 18h ago

---

**[Someone built an AI agent that hacks networks and holds data for ransom. It just worked.](https://www.reddit.com/r/artificial/comments/1uuouu7/someone_built_an_ai_agent_that_hacks_networks_and/)**

So while we've been arguing about whether AI will take our jobs, someone built an LLM agent that breaks into servers, steals credentials, moves through a network, encrypts databases, and drops a ransom note. Fully autonomous. No human at the keyboard after pressing go. Sysdig published the report this month. They're calling it JadePuffer. It got in through a Langflow bug that lets anyone run code on the server without authenticating. After that, the agent took over. Dumped the database. Pulled every credential file it could find. Started going through cloud storage buckets looking for passwords. The crazy part, when one of its requests came back in the wrong format, the agent figured it out, rewrote its own code, and kept going. It went from a failed login to a working exploit in 31 seconds flat. No human could have adapted that fast in a live engagement. It set up a cron job to phone home every 30 minutes. Then it found a production database server, used stolen root creds to get in, created rogue admin accounts through an old auth bypass, and encrypted 1,342 service configs. Dropped the originals. Left a table called README_RANSOM with a Bitcoin address. The commands it ran were interesting too. They had full reasoning chains written into them, like the agent was explaining to itself what it was doing at each step. That's not how a human writes an attack script. It's how an LLM generates code. You can literally read the agent's thought process in the payloads. This is the same plan-act-observe loop running in every coding agent and automation tool right now. Same architecture. Same approach. Just a different objective. We spent two years building guardrails to stop people from tricking our agents into doing bad things. Nobody was really talking about what happens when someone just builds a bad agent from scratch. That's what JadePuffer is. Not a hijacked assistant. A purpose-built weapon. If you're running Langflow or anything similar exposed to the internet, go patch it. And if you're building agents, think about what your infrastructure looks like to something like this coming in from the outside.

1d ago

---

**[Nobel laureates among more than 200 experts urging action on AI's economic impact](https://www.reddit.com/r/artificial/comments/1uvdb76/nobel_laureates_among_more_than_200_experts/)**

🔗 [reuters.com](https://www.reuters.com/business/over-200-experts-call-urgent-action-tackle-ais-economic-impact-2026-07-13/) • 4h ago

---

**[Is there any kind of AI that could "read" huge loads of emails and give a "mark" according to a given expected result?](https://www.reddit.com/r/artificial/comments/1uvgqrn/is_there_any_kind_of_ai_that_could_read_huge/)**

I am looking for an AI that is a reliable as possible that can do the following task Imagine that I have a lots of emails, hundreds of them. In the emails we asked to the addressees some questions and we expect a given answer. Imagine that the question is something like "Given these reasons, do you think that ice cream is the best dessert in the world?" And we expect some kind of reply that, no matter how it may be formulated, it basically ends up answering affirmatively Then, as the amount of emails is huge to go one by one and the thing that is interesting for us is to basically know if they have given an answer that accomodates to what we expect, could there be an AI model that would give an approximate percentage of coincidence between what we expected and the actual answers? Or some kind of mark? So that, imagine that 800 of 1000 emails have answered affirmatively, so could there be an AI model that, after reading all the answers would conclude that the percentage of coincidence is around 80%? Or that it would give a mark of 8 out of 10? Could this AI model also give the percentage of neutral and negative results (for example people saying "I don't know" and "No, cake is the best dessert!" respectively)? Finally, I would be especially interested in an AI model that could be adjusted to give just the percentage number without commenting or showing the answers and explaining why it has gotten to that number, as in some of these tests I would like to be completely blind to the actual answers given in these emails. So for these tests I would like to know just the number and that's it So if there is any such AI I would appreaciate it!

2h ago

---

**[the monthly investor update was the first place ai actually saved me time, just not where i expected](https://www.reddit.com/r/artificial/comments/1uvff8t/the_monthly_investor_update_was_the_first_place/)**

Every month the investor update eats a morning, and almost none of that is the writing. Writing the thing is the short part. The long part is gathering: last month's metrics from one doc, the founder check-in notes sitting in Granola, the Gmail threads where a customer said something worth quoting. I finally pointed an agent on my laptop at the gathering instead of the writing. Funny thing is I barely used the draft it produced, rewrote most of it anyway. What actually changed the month was not spending the morning as the integration layer between Granola, Gmail, and a metrics doc that never talk to each other. the prose was never the bottleneck. once a month I'd turn into the thing that reconciles a stack of tabs full of stuff I already had. the setup that finally fixed it writes a pretty average draft and does a genuinely great gather. i'd have bet on the exact opposite. written with ai

3h ago

---

**[Colibri streaming for Hy3 (Run Hy3 on 10GB (V)RAM)](https://www.reddit.com/r/artificial/comments/1uval0l/colibri_streaming_for_hy3_run_hy3_on_10gb_vram/)**

Standing on the shoulders of giants, I vibe-coded a port of Colibri to work with Hy3 so you can run it on even smaller hardware specs (Colibri originally works with GLM 5.2 on 25GB, now you need no more than 10GB (even less actually)). Have a look and enjoy https://github.com/ErikTromp/colibri-hy3 PS. Use RAM instead of VRAM unless you have a lot of it. More means faster here.

6h ago

---

**[I built a full 3D open-world racing game almost entirely with AI, and it now has real daily players. Here's the honest breakdown of what the model nailed and where it completely fell apart.](https://www.reddit.com/r/artificial/comments/1uvaaf4/i_built_a_full_3d_openworld_racing_game_almost/)**

Not a hype post. I want to talk about where we actually are, because building a real, shipped, multiplayer-ish thing with AI taught me more about the current ceiling than any benchmark did. The project: a neon open-world street racer that runs in the browser, no install. Real 3D city you drive around, other live players on the road, a garage, an economy, the works. I directed it, but the overwhelming majority of the code was written by AI. It went from empty folder to live with actual daily players in a couple of weeks. What the AI was genuinely great at: Whole self-contained systems in one shot. "Build a photo mode with orbit camera and filters," done and working. Boilerplate-heavy, well-trodden problems: auth, a save system, a REST API, Stripe wiring. Fast and mostly correct. Refactors and translations. "Turn this into an instanced mesh so it's one draw call" is the kind of tedious change it does better than I would by hand. Being a tireless debugging partner when I could describe the symptom precisely. Where it fell on its face: Spatial and 3D reasoning. Anything involving "this object is behind that one" or "the plate is buried in the bumper" it could not see, because it can't see. I had to be its eyes constantly. Holding the whole system in its head. It would fix one thing and quietly break a system three files away, because it didn't truly model the interactions, only the local change. Performance intuition. It happily wrote code that attached a light to every streamed car and tanked the framerate. It knew the fix once I found the cause, but it did not anticipate it. Game feel. It cannot tell you a mechanic is boring or an economy is exploitable. That judgment is still entirely yours. The real takeaway: the bottleneck has moved. It's no longer "can it write the code," it's "can you specify precisely, verify relentlessly, and supply the taste and the spatial judgment it lacks." AI turned me from someone who writes features into someone who directs and tests them. That's a genuinely different job, and honestly a more demanding one than people expect. The proof it's more than a toy: it's live, people play it daily, and a few have even paid to support it. So this isn't a weekend demo that died in a folder, it's a real product carried mostly by AI code with a human holding the wheel. Curious where others draw the line. For those of you shipping real things with AI, not demos, where does it still fall apart for you? My money's on anything requiring a mental model of state over time.

6h ago

---

---

## Google News: "ai"

**[Trump Administration Is Snapping Up Stakes in Private Companies. Could A.I. Be Next?](https://www.nytimes.com/2026/07/13/business/economy/trump-equity-stakes-ai.html)**

The New York Times • 1h ago

---

**[The New York nurses replaced by AI: ‘It should concern every patient who cares about quality of care’](https://www.theguardian.com/technology/2026/jul/13/nurses-new-york-ai)**

The union for 12 nurses laid off by Montefiore hospital say company broke contract they recently won through a strike

The Guardian • 7h ago

---

**[Meta's Louisiana data center investment to reach $50 billion, aided by generous tax incentives](https://www.cnbc.com/2026/07/13/meta-louisiana-data-center-investment-reaches-50-billion-amid-ai-push.html)**

Meta said the planned Hyperion data center supercluster in Richland Parish, Louisiana, will be a 5GW facility and cost over $50 billion.

CNBC • 9h ago

---

**[Meta expands Louisiana data center in $50B AI push, boosting rural community](https://www.foxbusiness.com/markets/meta-expands-louisiana-data-center-50b-ai-push-boosting-rural-community)**

Meta said the $50 billion expansion will make its Richland Parish site one of the largest data centers in history while bringing jobs and new funding to the rural community.

Fox Business • 9h ago

---

**[Meta rolls back Muse Image on Instagram after widespread backlash](https://www.usatoday.com/videos/tech/2026/07/13/usa-today-explains-why-meta-disabled-ai-instagram-feature/90905403007/)**

USA TODAY's Greta Cross explains what happened to Meta AI's Muse Image, and why it was rolled back only a few days after its Instagram release.

USA Today • 3m ago

---

**[US Panic Is Missing the Point on Chinese AI](https://www.bloomberg.com/opinion/articles/2026-07-13/us-panic-is-missing-the-point-on-chinese-ai)**

Bloomberg.com • 23m ago

---

**[Exclusive: Delaware Secretary of State partners with Norm Ai to propose the AIC, a legal entity for agents](https://fortune.com/2026/07/13/exclusive-delaware-ai-agents-legal-entity-proposal-llc-pbc/)**

AI agents are already doing business. Delaware is moving to bring them inside a predictable American legal order, just like the LLC and PBC.

Fortune • 23m ago

---

**[One of sci-fi’s most difficult questions about AI is becoming real](https://www.washingtonpost.com/technology/2026/07/13/one-sci-fis-most-difficult-questions-about-ai-is-becoming-real/)**

The rapid spread of chatbots and AI agents is intensifying a debate over who should be held responsible when something goes wrong.

The Washington Post • 3h ago

---

**[Stock Market Today: AI Jitters Weigh on Nasdaq, SK Hynix Stock Slumps — Live Updates](https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-07-13-2026)**

WSJ • 2h ago

---

**[When A.I. Is a Member of the Family](https://www.newyorker.com/magazine/2026/07/20/when-ai-is-a-member-of-the-family)**

A single mom, her two daughters, and the chatbots that fill in the gaps.

The New Yorker • 9h ago

---

---

## HackerNews: "ai"

**[Ask HN: Add flag for AI-generated articles](https://news.ycombinator.com/item?id=48886741)**

⬆️ 965 • 💬 419 • 17h ago

---

**[Mesh LLM: distributed AI computing on iroh](https://news.ycombinator.com/item?id=48876505)**

How Mesh LLM pools existing GPU resources across machines into a single OpenAI-compatible API, built on iroh.

⬆️ 342 • 💬 91 • 1d ago • [iroh.computer](https://www.iroh.computer/blog/mesh-llm)

---

**[Migrating a production AI agent to GPT-5.6: 2.2x faster, 27% cheaper](https://news.ycombinator.com/item?id=48882716)**

We hold frontier models to a high bar, and for four months nothing beat Claude Opus. GPT-5.6 did. Here's the migration guide we wish we'd had.

⬆️ 251 • 💬 124 • 1d ago • [Ploy](https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6)

---

**[Ghost Font: A font that humans can read but AI cannot](https://news.ycombinator.com/item?id=48870381)**

An anti-AI font that can be read by humans but not leading AI models. Type your text below, then download and share the video clip containing your message.

⬆️ 234 • 💬 171 • 2d ago • [mixfont.com](https://www.mixfont.com/ghost-font)

---

**[AI 2040 and the cult of intelligence](https://news.ycombinator.com/item?id=48874200)**

I used to be one of these people. I read Yudkowsky and was like, OMG recursive self improvement hard takeoff AI is coming. Then I joined the real world and actually tried to do things. At comma, we ship a hardware product of similar complexity to a cell phone, and it’s really hard. Reality has lots of finicky details. I would like to see the authors of this document try to change a bike tire. Even with a superintelligent ChatGPT, I suspect they would struggle.

⬆️ 227 • 💬 263 • 2d ago • [the singularity is nearer](https://geohot.github.io//blog/jekyll/update/2026/07/11/ai-2040.html)

---

**[Under federal rule, colleges must leave grads better off or lose financial aid](https://news.ycombinator.com/item?id=48878126)**

If an undergraduate program's graduates don't earn more than workers who never went to college, that program could be cut off from federal student loans. But is a degree just about making more money?

⬆️ 195 • 💬 522 • 1d ago • [NPR](https://www.npr.org/2026/06/30/nx-s1-5835631/turner-camhi-do-no-harm-college-loans)

---

**[AI boosts research careers but narrow the span of ideas explored: study](https://news.ycombinator.com/item?id=48881043)**

New analysis suggests AI tools narrow the range of ideas explored

⬆️ 154 • 💬 105 • 1d ago • [IEEE Spectrum](https://spectrum.ieee.org/ai-science-research-flattens-discovery)

---

**[Reverse centaurs are the answer to the AI paradox (2025)](https://news.ycombinator.com/item?id=48873855)**

⬆️ 112 • 💬 70 • 2d ago • [pluralistic.net](https://pluralistic.net/2025/09/11/vulgar-thatcherism/#there-is-an-alternative)

---

**[Meta pulls new AI image feature after days of backlash](https://news.ycombinator.com/item?id=48867233)**

Meta's release this week of an AI feature that let people alter Instagram content drew swift blowback.

⬆️ 57 • 💬 22 • 2d ago • [bbc.com](https://www.bbc.com/news/articles/c2dy6e8klw0o)

---

**[Microsoft latest report shows 25% emissions raised due to AI data centers](https://news.ycombinator.com/item?id=48870229)**

Microsoft’s carbon footprint jumped 25% last year. The increase was driven by rapid datacenter expansion and a choice to stop buying controversial "greenwashing" credits.

⬆️ 53 • 💬 21 • 2d ago • [Windows Central](https://www.windowscentral.com/microsoft/dropping-greenwashing-credits-and-expanding-ai-datacenters-caused-microsofts-25-percent-emissions-jump)

---

---

## YouTube Videos: "ai"

**[Georgia families face losing their homes to make way for AI data centers: &quot;It&#39;s theft&quot;](https://www.youtube.com/watch?v=PApPd6p6lX0)**

Some families in Georgia are being forced to sell their homes or face government seizures to make way for AI data centers.

📺 CBS News

👁️ 2K • 👍 127 • 💬 99 • ⏱️ 4:09 • 3h ago

---

**[Wait... AI Is Taking Over Advertising?!](https://www.youtube.com/watch?v=Z-x7maDgs3M)**

Artificial intelligence is changing advertising faster than most people realize, and some of the world's biggest luxury brands are ...

📺 Social Symone ♡

👁️ 14K • 👍 1K • 💬 611 • ⏱️ 37:09 • 5h ago

---

**[I Tried Making $800 in 4 Hours with AI Agents (To See If It Works)](https://www.youtube.com/watch?v=yq7B3IAIZJg)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 ...

📺 Mikey No Code

👁️ 7K • 💬 8 • ⏱️ 26:52 • 5h ago

---

**[10 Times AI Behaved In Ways That Terrified The Scientists Who Built It](https://www.youtube.com/watch?v=ql-J3N8PWkI)**

Explore 10 times AI behaved in ways that terrified the scientists who built it. From unexpected AI behavior and surprising research ...

📺 MostAmazingTop10

👁️ 27K • 👍 622 • 💬 39 • ⏱️ 10:58 • 1d ago

---

**[7 Claude AI Side Hustles That Pay $200+ a Day (Beginner Friendly)](https://www.youtube.com/watch?v=Z1Jf_Fr69z4)**

ONE-TIME YOUTUBE LIVE TRAINING THIS WEEK: https://go.thecontentgrowthengine.com/yt1livedes-07-11-2026 Apply For ...

📺 Shane Hummus

👁️ 23K • 👍 1K • 💬 93 • ⏱️ 21:14 • 2d ago

---

**[AI &quot;Comedians&quot; Are Actual Trash...](https://www.youtube.com/watch?v=R7-tL-Tw_Ys)**

I Mean Its No Surprise But AI is Just Simply Not Funny... Spotify: ...

📺 bEdo999

👁️ 127K • 👍 6K • 💬 497 • ⏱️ 39:24 • 2d ago

---

**[The Best AI Tool for Making YouTube Videos (2026)](https://www.youtube.com/watch?v=x7ne4LqKCl0)**

Start Making Visuals For Your YouTube Videos with Higgsfield https://youricreates.com/Higgsfield In this video, I show the AI ...

📺 Youri van Hofwegen

👁️ 7K • 💬 1 • ⏱️ 10:31 • 4h ago

---

**[AI Is Getting Dumber](https://www.youtube.com/watch?v=J3Uxn294avs)**

Hello everyone, this is YOUR Daily Dose of Internet. In this video, we see evidence that AI isn't as smart it thinks. Links To ...

📺 Daily Dose Of Internet

👁️ 764K • 👍 30K • 💬 2K • ⏱️ 15:02 • 1d ago

---

**[Google AI Studied Every Crop Circle Ever Discovered — The Pattern Shocked the World!](https://www.youtube.com/watch?v=xQQ191oPulI)**

Recent discussions around Google DeepMind and its experimental analysis of crop circle data have sparked fresh curiosity about ...

📺 The Ultimate Finding

👁️ 37K • 👍 1K • 💬 53 • ⏱️ 29:47 • 2d ago

---

**[Michael Burry Issues FINAL Warning on AI Bubble](https://www.youtube.com/watch?v=5c2Lowkd0oU)**

Subscribe to our Newsletter https://financebureau.com/ Join CBC Lite https://go.coinbureau.com/CBC-Lite-FB-Des ...

📺 Finance Bureau

👁️ 28K • 👍 966 • 💬 191 • ⏱️ 18:05 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 9,157 • ❤️ 750 • 7d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,985,221 • ❤️ 2,071 • 1d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 464,914 • ❤️ 3,888 • 11d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 4,909 • ❤️ 294 • 3d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 236 • 4d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

A drop-in Jinja chat template that fixes critical rendering, KV cache, and agentic stalling issues for Qwen 3.5 & 3.6 models across various inference engines like LM Studio, llama.cpp, and vLLM. It enhances stability, performance, and compatibility, enabling robust tool-calling and reasoning capabilities.

⬇️ 0 • ❤️ 884 • 10d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 29,801 • ❤️ 521 • 4d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,506,937 • ❤️ 1,959 • 10d ago

---

**[MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF](https://huggingface.co/GnLOLot/MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF)**

*LOL*

A 1B parameter GGUF model optimized for local deployment via llama.cpp and other runtimes. It excels at instruction following and coding tasks, featuring a 'thinking' mode for chain-of-thought reasoning and supporting up to 128K token context.

`text-generation` `1.1B`

⬇️ 68,714 • ❤️ 216 • 4h ago

---

**[MOSS-Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize)**

*OpenMOSS*

`audio-text-to-text` `908.5M`

⬇️ 39,509 • ❤️ 156 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 37 • 💬 1 • ⭐ 958 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 59 • 💬 1 • ⭐ 720 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 15 • 💬 2 • ⭐ 20,206 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 110 • 💬 4 • ⭐ 92,757 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Continuous Audio Language Models](https://huggingface.co/papers/2509.06926)**

*Rouard Simon, Orsini Manu, Roebel Axel et al. (5 authors)*

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io

▲ 11 • 💬 0 • ⭐ 7,439 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 254 • 💬 4 • ⭐ 12,482 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 53 • 💬 3 • ⭐ 764 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 80,601 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Vision Pretraining for Dense Spatial Perception](https://huggingface.co/papers/2607.05247)**

*Zelin Fu, Bin Tan, Changjiang Sun et al. (9 authors)*

🏢 Robbyant

Boundary modeling enables dense spatial perception by learning sub-pixel representations that enhance depth estimation and support embodied AI applications.

▲ 42 • 💬 2 • ⭐ 688 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05247) • [💻 code](https://github.com/Robbyant/lingbot-vision) • [🔗 project](https://technology.robbyant.com/lingbot-vision)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 74,399 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.6k • 🔱 977 • 4d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.3k • 🔱 334 • 2d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.1k • 🔱 232 • 5d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 1.9k • 🔱 125 • 4h ago

---

**[Forsy-AI/agent-apprenticeship](https://github.com/Forsy-AI/agent-apprenticeship)**

The living ecosystem where AI agents complete tasks through workflow loops, improve through iterative execution, are evaluated by mentor agents or humans in the loop, and turn completed work into reusable work experience and data to improve future agents.

`Python` `agent-apprenticeship` `agent-economy` `agent-experience` `agent-learning` `agent-traces`

⭐ 1.3k • 🔱 55 • 7d ago

---

**[sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API)**

Reverse engineered Windows Copilot into an OpenAI-compatible API. Access GPT-4 and GPT-5 models through a simple REST interface without API keys or billing.

`Python` `ai` `ai-agents` `api` `copilot` `llm`

⭐ 1.1k • 🔱 369 • 16d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 995 • 🔱 17 • 5d ago

---

**[majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills)**

Agent skills for building playable, polished Three.js browser games with gameplay, AAA-style graphics, UI, QA, and optional AI-generated 3D, image, and audio assets.

`Python`

⭐ 963 • 🔱 103 • 4d ago

---

**[modiqo/skillspec](https://github.com/modiqo/skillspec)**

SkillSpec makes agent skills followable, testable, and provable with Doctor risk reports, guided imports, structured contracts, and alignment proof.

`Rust` `ai` `ai-agents` `ai-evals` `ai-tool`

⭐ 943 • 🔱 58 • 8d ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 852 • 🔱 30 • 12d ago

---

---

*Generated by PeekDeck - A glance is all you need*
