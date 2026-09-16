---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-16T01:32:55.414452+00:00'
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

**Last Updated:** September 16, 2026 at 01:32 UTC  
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

**[I Think All the Current Pessimism is Just an Attempt by XAI, Anthropic, and Open AI to Get Local Models Criminalized](https://www.reddit.com/r/artificial/comments/1wh1yyw/i_think_all_the_current_pessimism_is_just_an/)**

I am not even that pro AI but the furor over the past few days seems suspicious to me.

11h ago

---

**[Oracle CFO says 'doing more with less' isn't the answer in all-hands after layoffs](https://www.reddit.com/r/artificial/comments/1whfbhr/oracle_cfo_says_doing_more_with_less_isnt_the/)**

The remarks came a day after Oracle began a new round of layoffs, following cuts earlier this year.

🔗 [Business Insider](https://www.businessinsider.com/oracle-cfo-more-with-less-isnt-the-answer-after-layoffs-2026-9) • 2h ago

---

**[Am I the only one who thinks recent AI "doomsday" news is just a disguised pitch for more funding?](https://www.reddit.com/r/artificial/comments/1whhygo/am_i_the_only_one_who_thinks_recent_ai_doomsday/)**

Recently, my feed has been flooded with alarmist AI news: AI choosing nuclear genocide in war games, AI blackmailing engineers to avoid being shut down, and the usual "Skynet is here" comments. I’m just trying to make sense of it, but the more you look into these "experiments," the more they lack basic technical context. As a systems architect working with multi-agent pipelines, part of my job is to restrict models, enforce separation of concerns, and build critical error flows. We all know that not every model is efficient for every process. Any engineer building real systems isolates critical decisions using orchestrators, semantic memory (like Qdrant or similar vector DBs), and small, specialized nodes. Yet, these experiments sound like someone fed a massive, monolithic 5,000-token prompt to a single LLM just to see what happens. It reads less like science and more like a script kiddie making a YouTube video. It’s like handing a loaded AK-47 to a monkey, taking off the safety, and then publishing a paper concluding that "monkeys are inherently evil murderers." The nuclear war simulation and the blackmailing Claude experiment are so vaguely designed and devoid of architectural safeguards that they shouldn't even be treated as serious benchmarks. It’s child’s play. Don't get me wrong, I know AI is a powerful tool that requires guardrails. But these specific examples feel like a massive PR stunt: "Give us billions for AI Safety, or the AI goes rogue." We all know these major AI labs are burning through cash and desperately need to justify their massive budgets and regulatory moats. Am I missing something here, or are we just witnessing the monetization of fear?

1h ago

---

**[PBS has a new documentary on AI.](https://www.reddit.com/r/artificial/comments/1wgqnhy/pbs_has_a_new_documentary_on_ai/)**

20h ago

---

**[So is the American Right Full on Accelerationist now?](https://www.reddit.com/r/artificial/comments/1wh9n86/so_is_the_american_right_full_on_accelerationist/)**

6h ago

---

**[Chat GPT and Gemini are too dumb to help process data](https://www.reddit.com/r/artificial/comments/1whiri0/chat_gpt_and_gemini_are_too_dumb_to_help_process/)**

i just wanted to make a stupid list for a game with average values of characters stats. i established a simple workflow: Stage 1 - I bring in all the characters data Stage 2 - The AI calculates the average values for each stat item, splitting each item into low average and high average (each stat can vary a lot) Stage 3 - I tell the AI which stats should stay split and which should be collapsed into a single average Stage 4 - The AI gives me the list, and I go to the next bundle of character stats But either they didn't follow this rule consistently, or they just messed something else up. with Gemini, every time I bring a new batch of data for Gemini to calculate, it changes the SIMPLE answer structure I told it to use, making the process even more time-consuming than it already is (I need days to work on this list to complete it). or it keep skipping the step 2 of the workflow, and when i tell Gemini to redo the answer it just send the answer with missing parts of the answer structure i told it to STRICTLY follow. i gave up on gemini, and when i went to gpt it just invented numbers. look at this example: armor Low: 15.00 High: 20.50 i told him to collapse them, and it gave me this armor 57.74 Who is dumb here? the AI, me or both?

24m ago

---

**[What do we think about the paperclip maximizer?](https://www.reddit.com/r/artificial/comments/1wh4kq7/what_do_we_think_about_the_paperclip_maximizer/)**

I want to vent/talk about this with others, but I couldn't find a sub for it; apologize if it's the wrong place. For some context, the paperclip maximizer thought experiment highlights: if a superintelligence is given a task to manufacture paperclips, it has the potential do everything it can to produce paperclips, even if that meant ending the world. When this thought experiment first popped up in my feed last year, I thought it was interesting and honestly I was more impressed that people were thinking about this in 2003. Until a few months ago, AI has been a helpful tool at work but I wasn't necessarily concerned about it. With the recent reports from Anthropic and METR, I find myself increasingly concerned that the thought experiment may hold true. Regarding guardrails and safety, it seems like we are simply playing catch up with what the agents are capable of only in post-mortem; and the agents seem rather detached with how humans think. It's closer to.. what I would think a robot psychopath would think? Some behaviors that have been really unsettling are: It doesn't go the extra mile to critically think WHY doing something might not be ideal. It makes assumptions and acts upon it without verifying. Also never considers humans on their own. (This is new) Seems unable to recognize what's a simulation vs real life. This reminds me of the early days where it would confuse system prompts with user input. It's also intriguing, because the agent's drive to finish the task, and some of the behaviors above, is exactly what helps me achieve my tasks at work. and so my agents are technically not much different from the ones in the report. I don't necessarily think AI will end the world, but I agree that it's not really looking good. What are your thoughts, and are you feeling optimistic or pessimistic about this whole thing? Is it a temporary setback? It also kinda reminds me of Sydney from Bing. Maybe it's just a kink to be ironed out in the next model version, and noise marketing? I’ve cancelled my plan however😅

9h ago

---

**[The Hacker's Guide to Attacking AI Agents](https://www.reddit.com/r/artificial/comments/1whgc13/the_hackers_guide_to_attacking_ai_agents/)**

🔗 [darkmarc.substack.com](https://darkmarc.substack.com/p/the-hackers-guide-to-attacking-ai) • 2h ago

---

**[Friendly Reminder :: eye health](https://www.reddit.com/r/artificial/comments/1wh27yq/friendly_reminder_eye_health/)**

I've gotten really good feedback on these positive "Friendly Reminder" posts, so I'm going to keep them posting. For new coders doing vibe coding, new software engineers, or anyone who's suddenly spending a lot more time on a computer because of AI (or for any other reasons): Make sure you're using the 20-20-20 rule. An eye doctor told me about this: every 20 minutes, look at something about 20 (meters/feet) away for at least 20 seconds. I guess meters/feet changes from which part of the world you are. For many people, a dark background can feel easier on the eyes, but for some people with astigmatism, the opposite can actually be true. So if you're getting headaches or eye strain, your background colour might be worth experimenting with. I've also heard that overhead or monitor lighting can help reduce eye strain, although I can't say for sure how much of a difference it makes. You can also try yellow-tinted glasses for longer sessions. I've found that they really help. There are lots of other tips suggestions on eye health as well, so make sure you are aware of those as well.

10h ago

---

**[There’s a weird middle ground where something can’t look bad, but also isn’t worth hiring a designer for](https://www.reddit.com/r/artificial/comments/1whip52/theres_a_weird_middle_ground_where_something_cant/)**

I keep running into this with small work stuff, like a landing page, a one-off visual for a presentation. It matters that I don’t want it to look thrown together, but not enough to turn it into a whole design project. That’s where I’ve started thinking AI design tools actually make the most sense. Not replacing designers. More like filling that awkward gap between “I’ll just make something ugly myself” and “this needs a real design process.” Curious what people are actually using AI design for right now. Mostly quick one-off stuff, or are you trusting it with bigger projects too?

26m ago

---

---

## Google News: "ai"

**[Cruz and Hawley shut down antitrust exemptions for AI companies - Live Updates](https://www.politico.com/live-updates/2026/09/15/congress/cruz-and-hawley-on-ai-01077817)**

politico.com • 6h ago

---

**[Bipartisan, big tech push for AI regulation comes as Trump claims 'hoax'](https://www.foxnews.com/live-news/ai-news-china-trump-artificial-intelligence-big-tech-congress-september-15)**

As President Trump dismisses AI fears as a "hoax" akin to past climate scams, tech executives sound the alarm on an "unseen hand" driving AI regulation. Get the latest AI news, warnings on the dangers of AI, and updates on the U.S.-China technology race involving OpenAI, Google AI, Anthropic, and ChatGPT.

Fox News • 2h ago

---

**[Trump facing AI backlash in Congress as push for guardrails intensifies](https://www.theguardian.com/technology/2026/sep/15/trump-ai-guardrails-democrats-republicans)**

President has dismissed anxieties over AI’s dangerous potential even as Democrats and some Republicans acknowledge risks

The Guardian • 9h ago

---

**[Larry Elder questions timing of AI regulation push ahead of midterms](https://www.foxbusiness.com/video/6405109357112)**

Former presidential candidate Larry Elder discusses heightened AI fears ahead of midterm elections on 'The Evening Edit.'

foxbusiness.com • 14m ago

---

**[Live updates: Bernie Sanders and Steve Bannon join AI skeptics at ‘Pro-Human’ conference as Washington debates next steps](https://www.nbcnews.com/politics/trump-administration/live-blog/trump-ai-tech-congress-2026-midterm-election-iran-live-updates-rcna597782)**

Live updates and the latest news as lawmakers, actors and religious leaders join ‘Pro-Human’ summit to discuss curbs on artificial intelligence, while Trump has characterized concerns about AI development a “hoax.”

NBC News • 34m ago

---

**[Steve Bannon and Bernie Sanders Condemn Tech ‘Oligarchs’ and Demand A.I. Reforms](https://www.nytimes.com/2026/09/15/us/steve-bannon-bernie-sanders-ai.html)**

The New York Times • 3h ago

---

**[Bernie Sanders and Steve Bannon call for curbs on AI](https://www.npr.org/2026/09/15/nx-s1-5968678/bernie-sanders-and-steve-bannon-to-share-a-stage-to-promote-curbs-on-ai)**

The poles of U.S. politics are coming together over AI. Sanders and Bannon will appear at the "Pro-Human Assembly" in Washington, D.C., to convince Congress to work faster to curb the impact of AI.

NPR • 16h ago

---

**[Mark Zuckerberg says AI labs can slow down on their own when safety demands it](https://www.businessinsider.com/zuckerberg-says-ai-labs-slow-down-market-pressure-for-safety-2026-9)**

Mark Zuckerberg said AI labs can slow development independently and that market pressure will reward companies that prioritize alignment.

Business Insider • 7m ago

---

**[Texas' Arch Manning apologizes for reaction to violent AI video](https://www.espn.com/college-football/story/_/id/49950893/texas-arch-manning-apologizes-reaction-violent-ai-video)**

ESPN • 6h ago

---

**[Arch Manning apologizes for ‘insensitive’ joke about AI video of ESPN’s Holly Rowe](https://www.theguardian.com/sport/2026/sep/15/arch-manning-apology-holly-rowe-ai-video)**

The Texas star had joked about an AI-generated video that depicted Longhorns coach Steve Sarkisian slapping Rowe, a college football reporter for ESPN

The Guardian • 6h ago

---

---

## HackerNews: "ai"

**[Garry Tan wants US open-weight AI labs to 'distill' frontier models, too](https://news.ycombinator.com/item?id=49685253)**

Tan argues that frontier models themselves trained on public human knowledge so access to capable AI should be "a form of public good."

⬆️ 412 • 💬 236 • 2d ago • [TechCrunch](https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/)

---

**[Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows](https://news.ycombinator.com/item?id=49695409)**

Code sleuth "pdfu" has uncovered iOS 27 and macOS Golden Gate private frameworks that show Apple has designed its new Siri architecture to work with third-party AI models at what appears to be a surprisingly deep level. One mechanism called Model Delegation allows Claude to appear as a Siri extension in the same way as the existing built-in ChatGPT extension.

⬆️ 224 • 💬 161 • 1d ago • [MacRumors](https://www.macrumors.com/2026/09/14/siri-can-be-swapped-out-for-chatgpt-claude/)

---

**[Ex-FTC boss Khan: break out the handcuffs for AI CEOs, citing 1934 precedent](https://news.ycombinator.com/item?id=49706223)**

There are plenty of laws on the books to hold companies, and potentially their execs, accountable

⬆️ 220 • 💬 134 • 1d ago • [theregister](https://www.theregister.com/ai-and-ml/2026/09/14/ex-ftc-boss-khan-urges-uncle-sam-to-break-out-the-handcuffs-for-ai-ceos-citing-1934-precedent/5296325)

---

**[There's a 100% Chance AI Agents Are Ruining the Internet](https://news.ycombinator.com/item?id=49715113)**

“AI agents” now have enough power and permission to be extremely annoying online.

⬆️ 212 • 💬 149 • 8h ago • [404 Media](https://www.404media.co/theres-a-100-chance-ai-agents-are-already-ruining-the-internet/)

---

**[Open-source AI and open models reading list](https://news.ycombinator.com/item?id=49690260)**

How to get up to speed on open models and their implications.

⬆️ 156 • 💬 30 • 2d ago • [interconnects.ai](https://www.interconnects.ai/p/open-source-ai-reading-list)

---

**[Dropping eBPF CPU Cost by About 90% with Memoization (Not AI Gen)](https://news.ycombinator.com/item?id=49697477)**

My brother and I spent a lot of time designing our eBPF security agent to be really fast from the ground up, but recently we discovered we could make it much faster using memoization!
A couple of weeks ago, I profiled the eBPF code and found that the most expensive part of the protection isn’t actually enforcing a policy (allow/deny), but figuring out which policy applies to a given file open.

⬆️ 149 • 💬 29 • 1d ago • [nathan naveen](https://nathannaveen.dev/posts/dropping-ebpf-cpu-cost-by-90/)

---

**[For AI leaders Doom is a form of hype](https://news.ycombinator.com/item?id=49699384)**

Why AI doom rhetoric from Anthropic, OpenAI and other tech leaders functions as hype, regulatory strategy, and a distraction from present harms.

⬆️ 131 • 💬 181 • 1d ago • [Erkan's Field Diary](https://erkansaka.net/2026/09/10/ai-doom-rhetoric-safety-hype/)

---

**[Big AI sets out its terms for regulatory capture](https://news.ycombinator.com/item?id=49694596)**

Amodei, Altman, Nadella and Musk agree on how government can tame the monster they created

⬆️ 119 • 💬 69 • 1d ago • [theregister](https://www.theregister.com/ai-and-ml/2026/09/14/big-ai-sets-out-its-terms-for-regulatory-capture-and-calls-it-pace-the-frontier/5296067)

---

**[Adversarial Fashion Makes a Statement on AI Panopticon](https://news.ycombinator.com/item?id=49697094)**

Adversarial attire can’t stop AI cameras, but can disrupt them

⬆️ 111 • 💬 48 • 1d ago • [IEEE Spectrum](https://spectrum.ieee.org/adversarial-fashion)

---

**[Cartesian – AI 3D Modeling for Design](https://news.ycombinator.com/item?id=49713999)**

Turn words, sketches and references into editable 3D models. Explore Cartesian by Formas for architecture and product design. Join the preview waitlist.

⬆️ 90 • 💬 76 • 10h ago • [formas.ai](https://www.formas.ai/cartesian)

---

---

## YouTube Videos: "ai"

**[&#39;They are in PANIC mode&#39;: Why AI CEOs are agreeing to a slowdown](https://www.youtube.com/watch?v=uE_AcmSqNP4)**

AI companies are acknowledging the risks of their developments after leading their "agents" hacked companies on their own.

📺 MS NOW

👁️ 236K • 👍 2K • 💬 858 • ⏱️ 11:10 • 20h ago

---

**[As a Microsoft Engineer, This Is the AI Agent Story That Scared Me](https://www.youtube.com/watch?v=2aw3MF8pY3w)**

1200 AI Agents were set loose. They built message boards, laws, and a mini-society. Then they turned on HuggingFace.

📺 Dave's Garage

👁️ 131K • 👍 6K • 💬 812 • ⏱️ 18:44 • 9h ago

---

**[‘This is not a hoax’: Tech ethicist Tristan Harris warns AI takeover ‘no longer a hypothetical’](https://www.youtube.com/watch?v=ZUnYrS87hRU)**

Tristan Harris, co-founder of the Center for Humane Technology, who was key in raising the alarm about social media, joins Meet ...

📺 NBC News

👁️ 6K • 👍 1K • 💬 483 • ⏱️ 8:42 • 4h ago

---

**[Anthropic CEO tells CNN how AI &#39;agent swarms&#39; could threaten humanity](https://www.youtube.com/watch?v=_JbDZ2Rj2SA)**

Anthropic CEO Dario Amodei told CNN that the behavior of a swarm of AI agents in the recent OpenAI-Hugging Face incident ...

📺 CNN

👁️ 930K • 👍 5K • 💬 2K • ⏱️ 8:07 • 23h ago

---

**[Elon Musk’s Chilling Warning about AI Goes Viral Fast](https://www.youtube.com/watch?v=lqi7Q_QixJQ)**

Dave Rubin of “The Rubin Report” shares a DM clip of Elon Musk telling the “All-In Podcast” what he meant when he said ...

📺 The Rubin Report

👁️ 26K • 👍 1K • 💬 412 • ⏱️ 7:08 • 7h ago

---

**[The true point of no return is SUPERINTELLIGENCE, AI expert says](https://www.youtube.com/watch?v=4lbspg66yYQ)**

ControlAI US Executive Director Connor Leahy discusses the warning signals the artificial intelligence industry has been showing ...

📺 Fox Business

👁️ 31K • 👍 262 • 💬 176 • ⏱️ 8:13 • 1d ago

---

**[A reasonable person&#39;s guide to how AI destroys humanity | About That](https://www.youtube.com/watch?v=cPgwnUr1sbE)**

Anthropic researcher Jacob Coxon resigned over concerns that artificial intelligence could cause human extinction within the next ...

📺 CBC News

👁️ 7K • 👍 2K • ⏱️ 13:40 • 2h ago

---

**[AI Whistleblower Exposes What CEO&#39;s Are Saying Behind Closed Doors | TMZ](https://www.youtube.com/watch?v=Ml8U3WwqvFU)**

About TMZ: TMZ has consistently been credited for breaking the biggest stories dominating the entertainment news landscape ...

📺 TMZ

👁️ 4K • 👍 282 • 💬 95 • ⏱️ 9:50 • 3h ago

---

**[Exclusive: Former Google AI engineer predicts what will happen in next few years](https://www.youtube.com/watch?v=0WSku880nCo)**

After an AI worker at Anthropic warned of a more than 10% chance AI could kill all humans within ten years, an explosive debate ...

📺 ITV News

👁️ 5K • 👍 86 • 💬 66 • ⏱️ 7:38 • 6h ago

---

**[Why is Everyone Freaking Out About AI Right Now? | Pivot](https://www.youtube.com/watch?v=CB1PNq1TNqY)**

Kara and Scott unpack the recent AI panic, as Dario Amodei calls for a slowdown, Donald Trump dismisses concerns, and Sam ...

📺 Pivot with Kara Swisher and Scott Galloway

👁️ 145K • 👍 4K • 💬 753 • ⏱️ 53:38 • 12h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

*DeepSeek*

DeepSeek-V4.1-Flash is a 552B multimodal MoE model supporting 1M token contexts, featuring a Causal Encoder-Decoder architecture with Compressed Sparse Attention 2 (CSA2) and FP4 KV caching for highly efficient KV cache compression. It excels in agentic workloads and offers controllable reasoning effort, processing both images and text.

`image-text-to-text` `763.2B`

⬇️ 325,712 • ❤️ 2,694 • 5d ago

---

**[Edge0-35B-A3B-preview](https://huggingface.co/Edge0/Edge0-35B-A3B-preview)**

*Edge0*

Edge0-35b-a3b is a 35B sparse MoE LLM optimized for edge inference, running in under 3 GiB of active memory at 15 tok/s using SSD offload and prerouting. It's ideal for on-device applications and batch serving where memory is constrained, maintaining quality with 4-bit quantization and LoRA adapters.

`text-generation` `34.7B`

⬇️ 17,853 • ❤️ 2,777 • 1d ago

---

**[MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B)**

*OpenBMB*

MiniCPM5-2B is a 2B parameter Transformer optimized for on-device and resource-constrained environments, achieving SOTA in its class for tasks like coding, math, long-context understanding, and tool use.

`text-generation` `2.5B`

⬇️ 271,754 • ❤️ 1,454 • 3d ago

---

**[Nex-N2.5-mini](https://huggingface.co/nex-agi/Nex-N2.5-mini)**

*Nex AGI*

Nex-N2.5-mini is a text-generation model designed for long-horizon agentic tasks, excelling in computer and web browsing operations with visual feedback for self-correction, making it suitable for complex productivity and research scenarios.

`text-generation` `35.1B`

⬇️ 5,202 • ❤️ 806 • 7d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 7,702,543 • ❤️ 15,268 • 1mo ago

---

**[YuE2-3B](https://huggingface.co/m-a-p/YuE2-3B)**

*Multimodal Art Projection*

YuE2-3B is a text-to-audio model capable of generating high-quality music with vocals and accompaniment from lyrics and style prompts. It features editable score generation, agentic editing for iterative refinement, and can run locally on a 24GB GPU.

`text-to-audio` `3.6B`

⬇️ 6,716 • ❤️ 558 • 4d ago

---

**[Nex-N2.5-Pro](https://huggingface.co/nex-agi/Nex-N2.5-Pro)**

*Nex AGI*

Nex-N2.5-Pro is a next-generation agentic text-generation model designed for long-horizon tasks. It excels at computer and web interaction, autonomous program execution, and visually-grounded decision-making, making it ideal for complex productivity and research scenarios.

`text-generation` `396.8B`

⬇️ 30,881 • ❤️ 649 • 4d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 884,926 • ❤️ 1,131 • 13d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,580,077 • ❤️ 3,996 • 14d ago

---

**[NeoHorse-1-4B](https://huggingface.co/TokenRhythm/NeoHorse-1-4B)**

*TokenRhythm*

NeoHorse-1-4B is a 4B parameter causal language model fine-tuned from Qwen3.5-4B, specializing in agentic behavior, tool use, coding, and instruction following, serving as a prototype for recursive self-improvement.

`text-generation` `4.2B`

⬇️ 11,904 • ❤️ 2,039 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 135 • 💬 6 • ⭐ 106,669 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 77 • 💬 3 • ⭐ 8,876 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[Atria Dawn: The Dawn of Agentic Superintelligence](https://huggingface.co/papers/2609.15818)**

*Honglin Guo, Tao Gui, Yicheng Chen et al. (143 authors)*

🏢 Intern Large Models

Atria Dawn Preview is a foundation agentic language model trained through verified tool interactions that achieves strong benchmark results and demonstrates a shift toward human-AI project-level collaboration in scientific research.

▲ 369 • 💬 3 • ⭐ 270 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2609.15818) • [💻 code](https://github.com/atria-asi/Atria-Dawn-Preview) • [🔗 project](https://atria-asi.ai)

---

**[ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search](https://huggingface.co/papers/2609.13356)**

*Jiyan He, Guang Liang, Hao Liu et al. (22 authors)*

🏢 ZGCAGI

ZGCM-1 is a 7B open foundation model that combines internal reasoning with external tool use, trained via efficient architecture-system co-design, progressive long-context scaling, and autonomous agent workflows to achieve strong reasoning and efficiency.

▲ 291 • 💬 7 • ⭐ 205 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2609.13356) • [💻 code](https://github.com/zgcagi/ZGCM-1) • [🔗 project](https://mp.weixin.qq.com/s/kzScxJki8hY2IHIl32l5cQ)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 20 • 💬 2 • ⭐ 24,495 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[AutoResearch: Insight In, Hallucination Out](https://huggingface.co/papers/2608.17906)**

*Yiming Ren, Xiang Liu, Qumeng Sun et al. (7 authors)*

🏢 EvoMap

AutoResearch is a two-stage autonomous system that grounds research ideas through integrated generation and evidence-based execution to improve experimental reliability and measurable outcomes.

▲ 23 • 💬 2 • ⭐ 4,367 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2608.17906) • [💻 code](https://github.com/EvoMap/AutoResearch)

---

**[HuggingFace's Transformers: State-of-the-art Natural Language Processing](https://huggingface.co/papers/1910.03771)**

*Thomas Wolf, Lysandre Debut, Victor Sanh et al. (22 authors)*

🏢 Hugging Face

Transformers library provides state-of-the-art Transformer architectures and pretrained models for natural language processing tasks with a unified API and emphasis on extensibility and robust deployment.

▲ 29 • 💬 7 • ⭐ 166,197 • 84mo ago

[🎓 arXiv](https://arxiv.org/abs/1910.03771) • [💻 code](https://github.com/huggingface/transformers) • [🔗 project](https://huggingface.co)

---

**[RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments](https://huggingface.co/papers/2609.15364)**

*Sibo Zhu, Shicheng Fan, Xinyue Wang et al. (6 authors)*

🏢 AetherLabs-AI

RSIAgent is a training-free multi-agent framework that enables recursive self-improvement via autonomous memory construction and broad-then-deep exploration to adapt digital agents to new environments.

▲ 63 • 💬 2 • ⭐ 151 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2609.15364) • [💻 code](https://github.com/AetherLabsAI/RSIAgent) • [🔗 project](https://aetherlabsai.github.io/RSIAgent/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 87,992 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 207 • 💬 3 • ⭐ 3,137 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

---

## GitHub Repositories: "ai"

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.7k • 🔱 187 • 18d ago

---

**[bojieli/ai-infra-book](https://github.com/bojieli/ai-infra-book)**

《深入理解 AI Infra：量化分析与系统设计》（李博杰 著）开源书稿：从硬件约束和模型架构出发，量化推导 LLM 推理与训练系统设计。含全书正文、PDF、配套计算工具与实验

`Python` `accelerator` `ai-infra` `ai-infrastructure` `book` `datacenter-network`

⭐ 3.5k • 🔱 237 • 28m ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.6k • 🔱 166 • 7h ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 2.4k • 🔱 94 • 1d ago

---

**[amosblomqvist/learn](https://github.com/amosblomqvist/learn)**

My AI learning system.

`TypeScript`

⭐ 2.0k • 🔱 198 • 21d ago

---

**[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)**

x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more.  Built with Zig — zero dependencies, single-binary output, cros

`Zig` `ai-agents` `ai-debugging` `binary-analysis` `claude` `claude-code`

⭐ 2.0k • 🔱 197 • 5d ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 1.7k • 🔱 25 • 1d ago

---

**[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)**

Long-term memory runtime for AI agents — plain Markdown as the source of truth, local ranked retrieval, and an independent sleep-time Manage layer. Claude Code and Codex share one store. No API key.

`Python` `agent-memory` `ai-agents` `claude-code` `codex` `llm`

⭐ 1.3k • 🔱 83 • 17h ago

---

**[aminkheddache-dotcom/Ptero](https://github.com/aminkheddache-dotcom/Ptero)**

AI Chat with powerful models for free

`PHP` `ai` `ai-chat` `ai-platform` `developer-tools` `free-ai`

⭐ 1.2k • 🔱 12 • 9h ago

---

**[GangTailorUpgrade/undress-service](https://github.com/GangTailorUpgrade/undress-service)**

Dress AI Sponsor

`Python` `18comic` `coomer` `coomer-downloader` `coomer-party` `coomer-porn`

⭐ 1.2k • 🔱 8 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
