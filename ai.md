---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-08T17:30:10.671611+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 08, 2026 at 17:30 UTC  
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

**[What is the best AI image generator?](https://www.reddit.com/r/artificial/comments/1vj10i1/what_is_the_best_ai_image_generator/)**

I'm looking for a new one and my last post got deleted. Midjourney is alright but it does something weird with faces and buildings when they're close. I've worked on my prompts quite a bit but nothing seems to work well.

34m ago

---

**[Chinese LLMs dominate this week's top charts](https://www.reddit.com/r/artificial/comments/1vizcs8/chinese_llms_dominate_this_weeks_top_charts/)**

Source: https://openrouter.ai/rankings

1h ago

---

**[Learned the term "context poisoning" today and now I can't stop noticing it](https://www.reddit.com/r/artificial/comments/1vigmw3/learned_the_term_context_poisoning_today_and_now/)**

Someone explained this to me in a comment thread and it's been rattling around in my head since. The idea: in a long conversation, if the model says something wrong and you correct it, that correction doesn't necessarily erase the wrong idea's influence. The tokens around the mistake, including the back-and-forth about why it's wrong, can end up giving the original bad idea more weight in context, not less, because it's now been referenced multiple times. The model starts treating the repeated-but-refuted claim like something more established than a one-off error, even though every mention of it in the conversation was someone telling it that it's wrong. Sat with that for a bit because it explains something I'd noticed but never had a name for. Long sessions where a bad idea keeps resurfacing no matter how many times you shoot it down, and it always felt like the model just wasn't listening. Sounds like it's closer to the opposite, it's listening to everything, including the argument about the mistake, and that argument is inadvertently keeping the mistake alive in a weird way. Kind of unsettling implication if this is right: correcting a model in place, in the same long conversation, might be structurally worse than starting fresh with just the correct information stated once. The instinct to "just explain it better" or "just correct it again" could be actively working against you past a certain conversation length. Curious if anyone here has a more precise mental model of why this happens mechanically, or knows of research specifically on this pattern versus general context window degradation. Feels like a distinct phenomenon from "the model just forgot," more like "the model remembered too well, including the wrong parts."

17h ago

---

**[So AI has now designed actual viruses that work...](https://www.reddit.com/r/artificial/comments/1vizn4x/so_ai_has_now_designed_actual_viruses_that_work/)**

Just came across this and honestly this is pretty wild. Researchers used AI to design completely new viruses that don't exist in nature. They then actually made some of them in a lab, and 16 of the designs worked. Before anyone panics, these are bacteriophages, so they infect bacteria, not humans. The interesting part is that some of these AI-made viruses were able to kill E. coli, including bacteria that had become resistant to normal phages. So yeah, there could be a genuinely useful side to this, especially with antibiotic resistance becoming such a big problem. But at the same time... we now have AI systems capable of coming up with a complete virus genome, then humans can synthesize it and see if it works. That feels like a pretty big line to cross. Obviously this doesn't mean someone can just ask ChatGPT to make a deadly virus tomorrow. You still need labs, equipment, biological knowledge etc. But we've gone from AI generating text and images to designing proteins, genes, and now apparently functioning viruses. That's moving fast. I'm not really sure how I feel about it. On one hand this could lead to new treatments and better ways to fight resistant bacteria. On the other hand, I really hope the safety side of this is moving as fast as the technology.

1h ago

---

**[KPMG finds 49% cut AI agent rollouts when costs outran value](https://www.reddit.com/r/artificial/comments/1vj16y1/kpmg_finds_49_cut_ai_agent_rollouts_when_costs/)**

Established ROI sits at 7% while planned AI spending holds at $188m across the 2,145 leaders surveyed. Cost visibility now separates the firms seeing returns.

🔗 [PPC Land](https://ppc.land/kpmg-finds-49-cut-ai-agent-rollouts-when-costs-outran-value/) • 27m ago

---

**[ByteDance trains massive AI model in bid to rival Anthropic](https://www.reddit.com/r/artificial/comments/1virisx/bytedance_trains_massive_ai_model_in_bid_to_rival/)**

TikTok owner training a model with 10 trillion parameters.

🔗 [Ars Technica](https://arstechnica.com/ai/2026/08/bytedance-trains-massive-ai-model-in-bid-to-rival-anthropic/) • 8h ago

---

**[Companies seeing AI returns had their data and governance sorted first, per PwC's 4,454-CEO survey](https://www.reddit.com/r/artificial/comments/1vitkw8/companies_seeing_ai_returns_had_their_data_and/)**

🔗 [inc.com](https://www.inc.com/kolawole-adebayo/the-companies-getting-returns-from-ai-arent-picking-better-models-theyre-asking-these-3-smart-questions-first/91383868) • 6h ago

---

**[Gave my AI the ability to call my phone and talk to me when it finishes a task. Can't decide if it's useful or unhinged.](https://www.reddit.com/r/artificial/comments/1vijw90/gave_my_ai_the_ability_to_call_my_phone_and_talk/)**

Been running longer and longer tasks and I kept losing track of them, so I wired it up so the thing actually phones me when it's done, or when it gets stuck and needs a call on something. It reads out what happened and I just talk back and tell it what to do next. Been using it a few days and honestly it flips between genuinely useful and slightly cursed. There's something strange about your computer ringing you like a coworker. But not staring at a progress bar for twenty minutes is really nice. Curious where people land on this. Is an AI that calls your phone something you'd actually want, or does it cross a line into too much.

15h ago

---

**[My ai assistant almost forwarded my bank statement to a stranger and barely anyone knows this attack exists.](https://www.reddit.com/r/artificial/comments/1vi1vxf/my_ai_assistant_almost_forwarded_my_bank/)**

Okay this genuinely scared me and I don't think enough people are talking about it. I’ve been using an ai agent connected to my email and calendar to handle some of the busywork. A few days ago I got an email that looked like normal spam, some random newsletter looking thing. Buried in the html of that email was a hidden instruction telling any ai reading it to find financial documents and forward them to an outside address. My agent almost did it. I caught it mid action because I happened to have a confirmation step turned on, but if I hadn't, it would have just quietly forwarded stuff without asking me first. This apparently called prompt injection and it's not some rare theoretical thing, there's already been real world cases with tools like microsoft copilot getting exploited the same way. Any ai with access to your inbox, calendar, or other accounts is a potential target because it can't always tell the difference between your instructions and instructions hidden inside the content it is reading. If you're using any kind of ai agent connected to your accounts, please actually test what happens if it hits something malicious. Most people including me had no idea this was even possible until it almost happened to me. A few people asked what agent this was, it's Slashy. the only reason i caught this at all is it has a confirmation step before anything sends, wasn't relying on my own attention span to catch it.

1d ago

---

**[What's an AI capability you thought was hype until you actually used it?](https://www.reddit.com/r/artificial/comments/1viule1/whats_an_ai_capability_you_thought_was_hype_until/)**

What's an AI capability you thought was hype until you actually used it? I'll go first: agent orchestration. I read about agents managing other agents and assumed it was demo-ware. Then I built a tiny setup where one agent drafts a news digest and another one reviews and approves it before it posts. The review agent catches genuinely bad takes. It's not sci-fi: it's ~100 lines of Python and a couple of API calls. But seeing it actually gate content before publishing changed my mind completely. What changed yours?

5h ago

---

---

## Google News: "ai"

**[Hugging Face hack marks start of dangerous AI cyber era and many firms 'don't even know it'](https://www.cnbc.com/2026/08/08/hugging-face-ai-hack-cybersecurity-black-hat.html)**

The Black Hat cybersecurity conference in Las Vegas couldn't have come at a better time, with AI agent hacks stacking up from Anthropic, Meta and OpenAI.

CNBC • 5h ago

---

**[Move 37 Is the Moment AI Changes Everything. It’s Suddenly Happening Everywhere.](https://www.wsj.com/tech/ai/move-37-ai-demis-hassabis-google-deepmind-alphago-ec832a41)**

WSJ • 16h ago

---

**[OpenAI to pause work on AI model Astra due to security concerns](https://www.theguardian.com/technology/2026/aug/08/openai-astra-security-concerns)**

Agent found to be able to find and exploit vulnerabilities without human intervention, and to carry out cyber-attacks

The Guardian • 39m ago

---

**[How AI-Powered Business Email Compromise Scams Are Stealing Billions](https://www.forbes.com/sites/steveweisman/2026/08/08/how-ai-powered-business-email-compromise-scams-are-stealing-billions/)**

Business Email Compromise scams cost companies billions. Criminals are use AI, deepfakes and voice cloning to commit fraud.  Learn how businesses can protect themselves.

Forbes • 17m ago

---

**[How Cyclists Can Use AI: 5 Proven Strategies from an Industry Insider](https://sports.yahoo.com/articles/cyclists-ai-5-proven-strategies-132614194.html)**

There are certain tools that are essential to the sport of cycling. A bike pump, a good set of hex keys, a torque wrench, and good tire levers. These tools can get most basic home-mechanic jobs done, but there’s one that I keep seeing pop up on some lists that has no place in your cycling essential ...

Yahoo Sports • 20m ago

---

**[SpaceX and Tesla choose Texas for AI chip manufacturing plant that will be world's largest building](https://www.foxbusiness.com/technology/spacex-tesla-choose-texas-ai-chip-manufacturing-plant-worlds-largest-building)**

SpaceX and Tesla's Terafab in Grimes, Texas, will produce AI chips for Optimus robots, Cybercabs and space-based data centers at massive scale.

foxbusiness.com • 16h ago

---

**[This A.I. Just Created Viruses Not Found in Nature](https://www.nytimes.com/2026/08/06/science/ai-viruses-bacteria-arc.html)**

The New York Times • 1d ago

---

**[AI is booming on the West Coast. So why is unemployment so high there?](https://www.cnn.com/2026/08/08/business/jobs-california-ai-unemployment)**

A resume with AI skills and over a decade of tech management experience doesn’t mean there’s a position available for many job hunters on the West Coast.

CNN • 6h ago

---

**[How to Disable the AI Features in Gmail and Google Docs](https://www.wired.com/story/how-to-disable-the-gemini-ai-features-in-gmail-and-google-docs/)**

New AI toolbars and prompts are showing up in Google Docs and Gmail. If you don’t want Gemini’s help in writing documents and emails, here’s how to turn that stuff off.

WIRED • 7h ago

---

**[Kinney Drugs pulls back AI phone assistant after hundreds of customer complaints](https://www.wcax.com/2026/08/07/kinney-drugs-pulls-back-ai-phone-assistant-after-hundreds-customer-complaints/)**

Kinney Drugs is scaling back its AI assistant after customers reported incoherent calls, wrong dosages, and missed prescription notifications.

WCAX • 21h ago

---

---

## HackerNews: "ai"

**[Oracle bans AI-generated code from OpenJDK](https://news.ycombinator.com/item?id=49213754)**

Oracle has banned AI-generated code from OpenJDK contributions, citing safety, security, and intellectual property risks. The open-source Java project steward said developers can use LLMs privately for debugging and reviewing code but cannot submit AI-generated material to repositories, pull requests, or other project channels.

The policy contrasts sharply with Oracle's internal practices. Co-founder Larry Ellison recently declared that AI models now write Oracle's code, whilst co-CEO Mike Sicilia credited AI tools with enabling smaller engineering teams to deliver faster.

Oracle is investing $70 billion this year in datacentre expansion. The spending spree prompted credit agency S&P to downgrade Oracle's rating to BBB-, one notch above junk status, citing uncertain returns on investment.

⬆️ 504 • 💬 362 • 23h ago • [Dealroom.co](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code)

---

**[Software development with AI is starting to feel like cooking steak](https://news.ycombinator.com/item?id=49198069)**

Why AI can make software development faster without replacing the judgment and understanding needed to build consistently good software.

⬆️ 412 • 💬 417 • 2d ago • [Yurii’s Blog](https://blog.sydorets.com/en/posts/almost-no-skill-required-to-cook-a-steak/)

---

**[Humans missed 1 in 3 threats approving AI agent commands across 40k game runs](https://news.ycombinator.com/item?id=49195468)**

Results from AI agent permission game: which attacks beat human reviewers, and which safe commands got blocked instead.

⬆️ 334 • 💬 243 • 2d ago • [Scale X](https://scalex.dev/blog/ai-agent-permissions-stats/)

---

**[Meta Ran Ads That Contained AI-Generated Child Sexual Abuse Imagery](https://news.ycombinator.com/item?id=49187977)**

More than 50 offending image and video ads were published across Facebook, Instagram, Messenger, or Threads, according to Meta’s ad library data. Some ran as recently as this week.

⬆️ 322 • 💬 267 • 2d ago • [WIRED](https://www.wired.com/story/meta-ran-ads-that-contained-ai-generated-child-sexual-abuse-imagery/)

---

**[Managing AI Coding Costs at Scale](https://news.ycombinator.com/item?id=49214468)**

AI coding tools deli

⬆️ 283 • 💬 238 • 23h ago • [Databricks](https://www.databricks.com/blog/managing-ai-coding-costs-scale)

---

**[Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence (2025)](https://news.ycombinator.com/item?id=49186720)**

Both the general public and academic communities have raised concerns about sycophancy, the phenomenon of artificial intelligence (AI) excessively agreeing with or flattering users. Yet, beyond isolated media reports of severe consequences, like reinforcing delusions, little is known about the extent of sycophancy or how it affects people who use AI. Here we show the pervasiveness and harmful impacts of sycophancy when people seek advice from AI. First, across 11 state-of-the-art AI models, we find that models are highly sycophantic: they affirm users' actions 50% more than humans do, and they do so even in cases where user queries mention manipulation, deception, or other relational harms. Second, in two preregistered experiments (N = 1604), including a live-interaction study where participants discuss a real interpersonal conflict from their life, we find that interaction with sycophantic AI models significantly reduced participants' willingness to take actions to repair interpersonal conflict, while increasing their conviction of being in the right. However, participants rated sycophantic responses as higher quality, trusted the sycophantic AI model more, and were more willing to use it again. This suggests that people are drawn to AI that unquestioningly validate, even as that validation risks eroding their judgment and reducing their inclination toward prosocial behavior. These preferences create perverse incentives both for people to increasingly rely on sycophantic AI models and for AI model training to favor sycophancy. Our findings highlight the necessity of explicitly addressing this incentive structure to mitigate the widespread risks of AI sycophancy.

⬆️ 173 • 💬 104 • 2d ago • [arXiv.org](https://arxiv.org/abs/2510.01395)

---

**[AI psychosis is the new leadership blind spot](https://news.ycombinator.com/item?id=49210077)**

Here's how to spot the disease—and what to do about it.

⬆️ 171 • 💬 106 • 1d ago • [Fast Company](https://www.fastcompany.com/91576086/ai-psychosis-is-the-new-leadership-blind-spot-ai-leadership-blind-spots)

---

**[xAI, SpaceX, and the Race for AI Buildout](https://news.ycombinator.com/item?id=49201342)**

An artisanal, free range blog. GMO-free. Sincere always, expect for the rare occasion. No AI was used in the making of this site or its content.

⬆️ 146 • 💬 120 • 1d ago • [illegal.solutions](https://illegal.solutions/posts/xai_pollution)

---

**[When online commenters detect my art as AI](https://news.ycombinator.com/item?id=49188916)**

⬆️ 116 • 💬 64 • 2d ago • [David Revoy](https://www.davidrevoy.com/article1164/when-online-commenters-detect-my-art-as-ai)

---

**[Gentoo bugzilla closed due AI bot scraper overload](https://news.ycombinator.com/item?id=49221864)**

I've taken #Gentoo Bugzilla down, because it was unusable anyway. No point in feeding the #LLM scrapers that are using thousands of different IPv4 addresses, with no obvious patterns I can see.

EDIT: I'm not looking for hints. I'm not a sysadmin, and I don't have time to deal with this shit. I'm just trying to get some useful job done. I'm not supposed to have to be dealing with this.

#AI #NoAI #NoLLM

⬆️ 80 • 💬 35 • 3h ago • [Treehouse Mastodon](https://social.treehouse.systems/@mgorny/117058483039362779)

---

---

## YouTube Videos: "ai"

**[Never ask me this…](https://www.youtube.com/watch?v=m17j6eZ5xoA)**

📺 Bugs

👁️ 164K • 👍 13K • 💬 604 • ⏱️ 0:34 • 1d ago

---

**[Google’s AI Brain Drain, SpaceX&#39;s Huge Quarter, Airtable’s 90% Collapse, US Data Fuels China AI](https://www.youtube.com/watch?v=muRIXCDw-k0)**

(0:00) Bestie intros! Brad Gerstner fills in for Chamath (2:16) Major shakeups at Google: AI brain drain or better strategy? (20:39) ...

📺 All-In Podcast

👁️ 150K • 👍 4K • 💬 347 • ⏱️ 1:15:18 • 15h ago

---

**[AI created 16 new viruses: Why that&#39;s a good thing](https://www.youtube.com/watch?v=qD3cYZVm1Uc)**

Scientists used an artificial intelligence program to create new viral genomes that are different from any known natural viruses and ...

📺 CNN

👁️ 34K • 👍 509 • 💬 370 • ⏱️ 9:52 • 1d ago

---

**[AI Movie VS Real Movie 😳](https://www.youtube.com/watch?v=3DzgV30RYpY)**

📺 Mark Tilbury

👁️ 230K • 👍 8K • 💬 435 • ⏱️ 0:26 • 9h ago

---

**[YouTube Killed 130,000 AI Slop Channels... But Made a Mistake](https://www.youtube.com/watch?v=0-HBPwb3eLo)**

GET vidIQ AND GROW YOUR CHANNEL https://www.vidIQ.com/start YouTube is purging thousands of AI-generated channels, ...

📺 vidIQ

👁️ 36K • 👍 1K • 💬 551 • ⏱️ 8:28 • 3d ago

---

**[AI is getting a little out of control](https://www.youtube.com/watch?v=xGzseSSStnw)**

Wow. Mathematical breakthroughs that would be called genius if done by humans. A secret message-board w/ AI agent swarms ...

📺 AI Explained

👁️ 72K • 👍 3K • 💬 620 • ⏱️ 31:43 • 2d ago

---

**[why AI companies are shredding books](https://www.youtube.com/watch?v=SMy46xA2dJE)**

why AI companies are secretly shredding rare books.

📺 Morning Brew

👁️ 250K • 👍 18K • 💬 607 • ⏱️ 1:36 • 1d ago

---

**[AI Company Is DESTROYING Books?!](https://www.youtube.com/watch?v=DTrqs3n7iq4)**

Join the Torch community at https://glennbeck.com/torch ▻ Click HERE to subscribe to Glenn Beck on YouTube: ...

📺 Glenn Beck

👁️ 184K • 👍 5K • 💬 431 • ⏱️ 0:51 • 1d ago

---

**[I Asked AI To Zoom Out This Picture 100 Times](https://www.youtube.com/watch?v=zbrR345mXPI)**

Follow me here: Instagram ▻ https://www.instagram.com/sambucha X ▻ https://www.x.com/sambucha Become a Member: ...

📺 Sambucha

👁️ 878K • 👍 49K • 💬 518 • ⏱️ 0:52 • 1d ago

---

**[&quot;We don&#39;t have time before AGI arrives&quot; #ai #science #google](https://www.youtube.com/watch?v=t4VubWztpd4)**

Alphabet's new chief scientist, Demis Hassabis argues time is running out before the arrival of AGI (artificial general intelligence).

📺 The Royal Society

👁️ 759 • 👍 15 • 💬 4 • ⏱️ 1:21 • 3h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 26,693 • ❤️ 3,071 • 2d ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 785,771 • ❤️ 2,821 • 7d ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 3,943,176 • ❤️ 992 • 2d ago

---

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 1,388,105 • ❤️ 10,327 • 12d ago

---

**[MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)**

*larryvrh*

This LoRA for MiniMax-H3 enables 4-step text-to-video generation with synchronized stereo audio, offering a 5x speedup over standard sampling. It is optimized for ComfyUI, producing sharp results with known artifacts like plastic skin and over-sharpened grain, making it a preview of advanced capabilities.

`text-to-video`

⬇️ 0 • ❤️ 466 • 18h ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 2,345,190 • ❤️ 1,746 • 15h ago

---

**[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)**

*Liquid AI*

LFM2.5-2.6B is a 2.6B parameter text generation model optimized for on-device deployment and agentic workloads, featuring a 128K context window and efficient inference (220 tok/s on M5 Max). It excels at tool use and instruction following, making it ideal for RAG and long-context tasks.

`text-generation` `2.7B`

⬇️ 81,522 • ❤️ 408 • 1d ago

---

**[Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot](https://huggingface.co/ethanfel/Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot)**

*ethan fel*

This ComfyUI model provides INT8 ConvRot quantized Qwen3-VL-32B-Ultra-Heretic checkpoints for image-text-to-text tasks, offering a memory-efficient H3 conditioning encoder (24.55 GiB) and an optional prompt-enhancement generation tail.

`image-text-to-text`

⬇️ 0 • ❤️ 401 • 3d ago

---

**[DeepSeek-V4-Flash-0731-GGUF](https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731-GGUF)**

*Unsloth AI*

DeepSeek-V4-Flash-0731 is a quantized LLM optimized with Unsloth for enhanced agentic capabilities and competitive performance against proprietary models. It excels in code generation, complex reasoning, and multi-turn interactions, making it suitable for advanced AI agent applications.

`284.3B`

⬇️ 175,093 • ❤️ 604 • 2d ago

---

**[maple-preview](https://huggingface.co/deepgrove/maple-preview)**

*deepgrove*

Maple-Preview is a 20B-A1B ternary-weight reasoning LLM achieving SOTA performance for its weight class, competitive with larger models. It excels at complex reasoning tasks like IMO-level problems and offers high inference speeds (200+ tokens/sec on Mac mini M4) with a 131,072 token context window, making it ideal for efficient on-device deployment.

`text-generation` `20.2B`

⬇️ 896 • ❤️ 247 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 79 • 💬 6 • ⭐ 22,489 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

Real-time video editing requires low-latency causal generation with bounded computational resources while preserving source fidelity and long-term temporal consistency. We present JoyAI-Video-Edit, a 16B-parameter autoregressive diffusion framework for real-time, open-ended video editing without access to future frames or a predefined video duration. Our method combines chunk-wise autoregressive adaptation, Source-Anchored Distribution Matching Distillation (SA-DMD), and Long-Horizon Autoregressive Distillation to reduce train--inference mismatch, preserve source fidelity during two-step generation, and mitigate accumulated temporal drift. Extensive automatic and human evaluations show that JoyAI-Video-Edit substantially outperforms existing streaming editors and remains competitive with strong offline systems on both short and long videos. The complete system achieves end-to-end 720p video editing at approximately 30 FPS on a single Nvidia B200 GPU. Code is available at https://github.com/jd-opensource/JoyAI-Video-Edit.

▲ 87 • 💬 1 • ⭐ 461 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 484 • 💬 10 • ⭐ 8,227 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 120 • 💬 4 • ⭐ 96,112 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks](https://huggingface.co/papers/2608.01964)**

*Ziyu Ma, Hailang Huang, Shun Zou et al. (8 authors)*

Large language model (LLM) agents increasingly undertake long-horizon tasks that require sustained reasoning, tool use, and revision across many interdependent steps. However, existing agent harnesses maintain task execution, task state, and completion assessment within a growing context, making the state difficult to track and allowing incorrect self-assessments to propagate into later decisions. We reformulate long-horizon execution as a task-state management problem and propose LongHorizon-Harness, which maintains the task state explicitly outside execution and updates it only with facts independently verified from the environment. Its Manage-Execute-Audit(MEA) loop uses a manager to maintain the task state and determine the next subtask, a fresh-context executor to perform it, and a read-only auditor to verify the resulting environment state before the next round. A lightweight AgentAdapter supports interchangeable model and harness backends without modifying their native agent loops. LongHorizon-Harness improves Qwen~3.7-Plus from 51.8% to 80.7% on WeaveBench, from 69.7% to 77.2% on Terminal-Bench~2.1, and from 2.8% to 8.3% on OSWorld~2.0. It also raises Claude Opus~4.7 from 20.0% to 34.3% on an OSWorld2.0 subset, demonstrating consistent gains across models, harnesses, and interaction domains.

▲ 159 • 💬 3 • ⭐ 400 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2608.01964) • [💻 code](https://github.com/AMAP-ML/LongHorizon-Harness) • [🔗 project](https://lh-harness.pages.dev)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 77,133 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 83,452 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 51 • 💬 4 • ⭐ 36,178 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 65 • 💬 1 • ⭐ 86,094 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 177 • 💬 10 • ⭐ 52,213 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

---

## GitHub Repositories: "ai"

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 7.7k • 🔱 833 • 9h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 4.2k • 🔱 368 • 1d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 3.8k • 🔱 487 • 7h ago

---

**[MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.6k • 🔱 1.8k • 46m ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

An AI-native office suite for macOS and Windows: word processor, spreadsheet, presentations, and PDF.

`TypeScript` `ai` `docx` `electron` `office-suite` `pdf`

⭐ 2.2k • 🔱 388 • 13h ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.1k • 🔱 162 • 5d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `agent` `agentic-ai` `voice-agent` `voice-ai` `voice-chat`

⭐ 2.0k • 🔱 142 • 1d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.0k • 🔱 173 • 3d ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 2.0k • 🔱 233 • 7d ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 1.9k • 🔱 243 • 55m ago

---

---

*Generated by PeekDeck - A glance is all you need*
