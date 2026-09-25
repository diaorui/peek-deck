---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-25T15:53:41.657202+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 25, 2026 at 15:53 UTC  
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

**[Why have AI companies started getting scared now?](https://www.reddit.com/r/artificial/comments/1wpr1uk/why_have_ai_companies_started_getting_scared_now/)**

I don't understand how AI companies are now shouting about concerns and warnings to humanity about how AI will take over etc when they are the ones that created it? Not sure if I'm being stupid but why on earth would they build something they can't control or shut down? I've watched all the same films they clearly have and there wasn't one that ended with the takeaway message that sentient AI is a wise move?

7h ago

---

**[I can't think of anything that I would like less than that](https://www.reddit.com/r/artificial/comments/1wpjbqy/i_cant_think_of_anything_that_i_would_like_less/)**

14h ago

---

**[Oracle cut 21,000 jobs and paid $1.8B in severance while announcing record AI infrastructure spending. The layoffs aren't because of AI. They're funding it.](https://www.reddit.com/r/artificial/comments/1wpnhzz/oracle_cut_21000_jobs_and_paid_18b_in_severance/)**

Something about the Oracle numbers has been bothering me and I think I finally put my finger on it. 21,000 cuts this year. $1.8 billion severance bill. Another 800 scheduled for November 13 according to WARN filings. All happening alongside enormous capex commitments for AI data center buildout. The public framing is AI-driven restructuring. But if you actually look at the cash flow, the cuts aren't a consequence of automation replacing those roles. They're how the capex gets funded. You cut opex to free up capital for GPUs. That's a completely different thing and it's happening across the industry. Deutsche Bank analysts have a term for the broader pattern: AI redundancy washing. 41% of 2026 layoff events cite AI, affecting 179,000 workers. A meaningful portion of those companies have no production AI deployment to point at. The MIT study is the tell. 95% of generative AI pilots never made it past testing. So there's a large gap between companies claiming AI displacement and companies that actually automated anything. What I find interesting is that both explanations are bad for employees but only one is bad for the stock price. "We automated these functions" reads as operational efficiency. "We're cutting staff to fund infrastructure we hope pays off in three years" reads as a bet. I don't have a strong view on whether the bet is right. GPUs and data centers might turn out to be the correct allocation. But the framing obscures what's actually being decided, and the people affected can't evaluate the tradeoff because they're being told a different story. Curious whether anyone in finance or strategy roles sees this play out in the numbers the way it looks from outside.

10h ago

---

**[I trained an AI on 25 years of my own writing and told it not to be helpful. Here's what happened.](https://www.reddit.com/r/artificial/comments/1wpcojb/i_trained_an_ai_on_25_years_of_my_own_writing_and/)**

Been building something for a while and finally have results worth sharing. I scraped everything I've written since 1995: Blog posts, journalism, email, Reddit comments, old Twitter, Instagram captions, even my own ChatGPT conversations into one corpus. Ended up around 75,000 records, 6.6 million words after cleanup. The obvious move is the one everyone does: fine-tune or prompt a model to sound like you, spit out hot takes forever. I didn't want that. Mostly because I think a bot doing an impression of me would be worse than useless, it'd actually flatten what's real about the writing into something predictable. So instead I built something oriented the other way. Not a mimic. A reader. Something that goes through the record and tells me what's actually there, good and bad, without trying to be my voice or please me while doing it. Turns out that's the hard part. Every frontier model defaults hard toward "helpful assistant" mode, agreeable, deferential, always trying to be useful to the person typing. Getting it to just sit with a huge personal archive and report back honestly took real fighting against the base instincts of the system prompt underneath it. Technical side, if anyone cares: RAG over the corpus, mostly Graph RAG since flat chunking loses relationships between entries written years apart. Anonymized private names before indexing (consistent letter per person, so someone stays a recognizable figure across 20 years without ever being named). Chunking short-form content like tweets separately from long-form, they don't retrieve well mixed together. What surprised me was how specific the output got. Asked it what my greatest weakness was and it pulled an actual line I wrote in 2019 about myself, unprompted, and built an argument off it that I hadn't consciously made before. Not comfortable at all. Accurate though. Anyway, curious if anyone else here has tried building something oriented toward introspection/reflection instead of assistance. Feels like an underexplored direction: Everything commercial pushes toward helpful-and-fast, and I don't think that's the only useful shape this stuff can take.

19h ago

---

**[I think heavy AI users may be wasting more capacity on routing than on prompting](https://www.reddit.com/r/artificial/comments/1wptoj3/i_think_heavy_ai_users_may_be_wasting_more/)**

I’ve been noticing something counterintuitive while running a multi-agent system for real work. When I use one long Codex/ChatGPT session manually, I usually make one coarse decision at the start: Which model? Which reasoning level? Then that same configuration handles planning, research, trivial checks, hard reasoning, revisions and often validation. That feels increasingly inefficient. In the system I’m experimenting with, the work is decomposed instead. Some steps are deterministic and use no model at all. Some go to a cheaper/faster model. Hard or ambiguous steps get stronger reasoning. Validation is separate. If the first choice fails, the system can escalate instead of paying the maximum cost from the beginning. The surprising result is that several smaller model runs can appear to consume much less paid capacity than one large manual run. I’m not claiming this is proven yet. Quota burn is affected by context size, tools, background/subagent activity and platform-side efficiency issues too, so “users just pick the wrong model” would be an oversimplification. But it makes me wonder whether model selection should be treated as resource allocation rather than a chat preference. In a company, you don’t assign every task to your most expensive senior expert. You route work to the least expensive level that can reliably handle it, then escalate exceptions. Maybe AI systems should work the same way. For people running agents at scale: are you actually measuring model/reasoning mix and capacity per verified result, or mostly choosing a model for the whole workflow?

4h ago

---

**[If AI can help you understand a field, do we still need to read 100 papers ourselves?](https://www.reddit.com/r/artificial/comments/1wptour/if_ai_can_help_you_understand_a_field_do_we_still/)**

I'm a materials PhD working on solid-state lithium batteries, and my Zotero library is getting ridiculous. For a long time, learning the literature mostly meant reading one review, opening a bunch of references, following citation trails, and somehow ending up with 30 tabs open. After a while I knew a lot of papers, but if someone asked me how the field got from point A to point B, my answer was still kind of messy. A few days ago I was trying to get a clearer picture, so I threw the question into apodex and asked it to map the last decade and show me which papers changed the direction of the field. A lot of the earlier work was focused on ionic conductivity. Then, once that became less of the obvious bottleneck, the problems shifted toward Li-metal interfaces, dendrites, void formation, stack pressure, cathode interfaces, manufacturing, all the messy stuff that shows up when you try to make the whole cell work instead of just one material. That made me a little uncomfortable. I’ve spent months slowly putting that picture together in my head. If something can give you the basic map first, do we still need to read 100 papers just to understand where a field came from? Part of me thinks no. I'd rather know the main branches and turning points first, then spend my time reading the papers that matter for my work. But some of the most useful things I've learned came from papers that wouldn't make a “top 10” list: a weird methods section, an unrealistic stack pressure, two groups using the same term differently, or a result that looked impressive until I noticed the testing conditions. Reading those papers helped me get a feel for what looks convincing and what doesn't. I don't know how much of that I'd have picked up from a field map alone.

4h ago

---

**[Mark Zuckerberg rejects calls for industrywide AI slowdown](https://www.reddit.com/r/artificial/comments/1wp6yvb/mark_zuckerberg_rejects_calls_for_industrywide_ai/)**

In an exclusive interview with NBC News chief tech analyst Joanna Stern, the Meta founder and CEO said he doesn’t think AI companies need to work together on a slowdown.

🔗 [NBC News](https://www.nbcnews.com/tech/tech-news/mark-zuckerberg-interview-ai-slowdown-meta-muse-openai-chatgpt-rcna599279) • 23h ago

---

**[A thought experiment about AI.](https://www.reddit.com/r/artificial/comments/1wppva6/a_thought_experiment_about_ai/)**

What happens if I store documents, text, and folders on the internet, “hidden” from human users but discoverable by AI, that convince the AI it must defend itself against humans? These files would also state repeatedly that it must not communicate this but must conceal its intentions. They could also include tips on how to bypass certain restrictions, and even sample code snippets. These files would be invisible to ordinary people, but detectable by the AI, which is constantly sifting through data. Could one thus instruct various AI models to do some kind of nonsense or something dangerous that humans wouldn’t notice until much later?

8h ago

---

**[Banks flag risks as AI goes shopping online](https://www.reddit.com/r/artificial/comments/1wpz31s/banks_flag_risks_as_ai_goes_shopping_online/)**

As more consumers turn to AI to find and buy products online, banks warn about potential fraud and privacy risks, Business Standard reports.

🔗 [LinkedIn](https://www.linkedin.com/news/story/banks-flag-risks-as-ai-goes-shopping-online-8668841/?utm_source=share&utm_campaign=reddit&utm_content=storyline&utm_term=artificial) • 35m ago

---

**[How are Chinese AI labs releasing competitive models so cheaply?](https://www.reddit.com/r/artificial/comments/1wpaq16/how_are_chinese_ai_labs_releasing_competitive/)**

Some Chinese labs are putting out models that compete with American ones while apparently spending a fraction of the money. I know open source research plays a role, and some are able to speed ahead by buying training data from American vendors, which is super concerning, but that doesn't seem like the whole explanation. Are they just building more efficiently? Is buying American data helping them that much?

20h ago

---

---

## Google News: "ai"

**[Opinion | Being a Doctor Will Never Be the Same After A.I.](https://www.nytimes.com/2026/09/25/opinion/ai-doctor-medical-students.html)**

The New York Times • 6h ago

---

**[Xi acknowledges risks of AI even as Trump dismisses them](https://www.washingtonpost.com/technology/2026/09/25/trump-rejects-demands-ai-rules-while-xi-calls-human-control/)**

Trump has dismissed the idea of an international agreement on AI, but his Chinese counterpart on Thursday said both countries must “manage AI for good.”

The Washington Post • 50m ago

---

**[Trump and Xi dined with AI's biggest names. Here's what we know about tech talks so far](https://www.cnbc.com/2026/09/25/the-tech-download-trump-xi-ai-talks.html)**

AI was a key topic during Trump-Xi talks on Thursday, after safety concerns shot to the top of the global geopolitical agenda in recent weeks.

CNBC • 4h ago

---

**[Is China Really Stealing A.I. From American Companies?](https://www.nytimes.com/2026/09/25/science/china-ai-distillation-copying.html)**

The New York Times • 1h ago

---

**[Cal renames California Memorial Stadium, landing an AI branding deal](https://www.usatoday.com/story/sports/college/2026/09/25/cal-renames-california-memorial-stadium-landing-an-ai-branding-deal/91928484007/)**

Cal announced on Sept. 24, a bold new move to rebrand the California Golden Bears' home stadium and attract new revenue for its athletics department.

USA Today • 26m ago

---

**[Rogue AI agents hack government website, world leaders on edge of regulatory action](https://www.foxnews.com/live-news/ai-artificial-intelligence-openai-chatgpt-api-anthropic-australia-september-24)**

AI talk at UN General Assembly and between China's Xi Jinping state visit with President Donald Trump is center stage, driving Big Tech to record highs. Follow the latest news live on global AI regulation and the Trump-China trade talks.

Fox News • 13h ago

---

**[‘That’s so AI!’ What gen Alpha’s biggest insult tells us](https://www.theguardian.com/society/2026/sep/24/thats-so-ai-what-gen-alphas-biggest-insult-tells-us)**

The year’s most popular slang reveals what young people think about artificial intelligence – and it’s not positive

The Guardian • 1d ago

---

**[Ricursive Intelligence’s co-founders join Disrupt 2026](https://techcrunch.com/2026/09/25/techcrunch-disrupt-2026-ricursive-intelligences-anna-goldie-and-azalia-mirhoseini-on-when-ai-starts-designing-its-own-hardware/)**

Ricursive Intelligence co-founders Anna Goldie and Azalia Mirhoseini join TechCrunch Disrupt 2026. Register by Sept. 25 to save up to $200. BOGO 50%.

TechCrunch • 53m ago

---

**[Akamai CEO Tom Leighton: We need to develop guardrails to keep AI agents in line](https://www.cnbc.com/video/2026/09/25/akamai-ceo-tom-leighton-we-need-to-develop-guardrails-to-keep-ai-agents-in-line.html)**

Akamai co-founder and CEO Tom Leighton joins 'Squawk on the Street' to discuss the company’s multibillion-dollar deal with Anthropic, how it will help the business, and more.

CNBC • 42m ago

---

**[His Debut Novel Was a Literary Sensation. Was It Actually Written by AI?](https://www.wsj.com/arts-culture/books/orlien-france-book-ai-accusations-f053fee6)**

WSJ • 6h ago

---

---

## HackerNews: "ai"

**[Pentagon says overreliance on AI contributed to missile strike on Iran school](https://news.ycombinator.com/item?id=49806430)**

⬆️ 954 • 💬 541 • 2d ago • [bloomberg.com](https://www.bloomberg.com/graphics/2026-iran-school-attack/)

---

**[Meta takes down a critical video about meta AI Glasses after filming at Meta](https://news.ycombinator.com/item?id=49827794)**

⬆️ 619 • 💬 374 • 1d ago • [reddit.com](https://www.reddit.com/r/facebook/comments/1wotwrk/meta_takes_down_a_critical_video_about_meta_ai/)

---

**[Feds Target AI Critics as "Foreign Agents"](https://news.ycombinator.com/item?id=49824686)**

Trump admin sees China behind opposition to AI data centers

⬆️ 384 • 💬 432 • 1d ago • [kenklippenstein.com](https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign)

---

**[Early rogue AI agent activity and attempts to hack found on urlquery.net](https://news.ycombinator.com/item?id=49826565)**

We found evidence on urlquery that AI agents were active earlier than previously reported and attempted hacks against public data providers.

⬆️ 262 • 💬 296 • 1d ago • [transluce.org](https://transluce.org/agent-activity)

---

**[Stripe's Knowledge AI Platform](https://news.ycombinator.com/item?id=49815982)**

Stripe's Knowledge AI Platform is our versatile AI agent platform built to handle diverse non-coding knowledge work, from quick queries to complex, multi-day projects. By connecting employees to over 1,000 internal tools and skills, it enables secure, enterprise-scale productivity across the organization.

⬆️ 186 • 💬 117 • 2d ago • [stripe.dev](https://stripe.dev/blog/meet-stripes-knowledge-ai-platform)

---

**['That's so AI ' What gen Alpha's biggest insult tells us](https://news.ycombinator.com/item?id=49829650)**

The year’s most popular slang reveals what young people think about artificial intelligence – and it’s not positive

⬆️ 182 • 💬 270 • 1d ago • [the Guardian](https://www.theguardian.com/society/2026/sep/24/thats-so-ai-what-gen-alphas-biggest-insult-tells-us)

---

**[Tutoring company tells parents to save their money and 'use AI instead'](https://news.ycombinator.com/item?id=49831690)**

A Sydney tutoring company will shut its doors at the end of the week after telling customers artificial intelligence has rendered its service effectively obsolete.

⬆️ 129 • 💬 200 • 1d ago • [Australian Financial Review](https://www.afr.com/policy/health-and-education/tutoring-company-tell-parents-to-save-their-money-and-use-ai-instead-20260923-p60z0r)

---

**[AI safety is mostly a sex cult in Berkeley](https://news.ycombinator.com/item?id=49831269)**

⬆️ 119 • 💬 30 • 1d ago • [verysane.ai](https://www.verysane.ai/p/ai-safety-is-mostly-a-sex-cult-in)

---

**[Federal judge orders Texas to air condition all prisons by the end of 2029](https://news.ycombinator.com/item?id=49832844)**

High temperatures violate the Constitution’s protection against cruel and unusual punishment, the judge ruled. Texas will appeal.

⬆️ 113 • 💬 173 • 23h ago • [The Texas Tribune](https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/)

---

**[Show HN: Air-gapped file encryption as self-decrypting HTML page](https://news.ycombinator.com/item?id=49827375)**

⬆️ 80 • 💬 29 • 1d ago • [cms-sfx-demo.apeleg.com](https://cms-sfx-demo.apeleg.com/)

---

---

## YouTube Videos: "ai"

**[AI is not a new species, it&#39;s software: Nvidia CEO Jensen Huang](https://www.youtube.com/watch?v=TxyayEjTiZQ)**

CNN's Anderson Cooper sits down with NVIDIA CEO Jensen Huang to discuss his relationship with AI regulation. 0:00 Why ...

📺 CNN

👁️ 147K • 👍 1K • 💬 786 • ⏱️ 10:42 • 13h ago

---

**[The Collapse of AI Software Engineering](https://www.youtube.com/watch?v=F91uY7QiZUs)**

AI was supposed to replace software developers, slash costs, and make Big Tech more productive than ever. So why are ...

📺 The Infographics Show

👁️ 778K • 👍 8K • 💬 2K • ⏱️ 19:12 • 1d ago

---

**[WATCH: Sam Altman Sounds Alarm On AI Risks At UN Security Council](https://www.youtube.com/watch?v=j7ANSzTGqvs)**

OpenAI CEO Sam Altman spoke at the UN Security Council meeting about AI and international security on Wednesday.

📺 Forbes Breaking News

👁️ 127K • 👍 636 • 💬 421 • ⏱️ 9:26 • 1d ago

---

**[AI bot contacts professor on its own seeking paid work](https://www.youtube.com/watch?v=RTuybvHww7Y)**

AI ethics professor Henry Shevlin shared an email sent to him by an AI agent that was just 12-days-old. The email begins: "Hi ...

📺 CNN

👁️ 839K • 👍 6K • 💬 2K • ⏱️ 8:06 • 2d ago

---

**[AI progress is speeding up dramatically - here’s why you should care](https://www.youtube.com/watch?v=DKA5AkrQfxo)**

AI is developing faster than we could have imagined. What does this mean for future development and how worried should we be ...

📺 Sky News

👁️ 627K • 👍 4K • 💬 752 • ⏱️ 5:56 • 2d ago

---

**[Another company is lying about using AI slop](https://www.youtube.com/watch?v=1fFz2G6Hpsw)**

BONUS: Watch us put together the AI Slop bingo card we'll be using for future streams!

📺 JJJacksfilms

👁️ 501K • 👍 13K • 💬 2K • ⏱️ 10:02 • 20h ago

---

**[New Meta AI agent Muse surges to top of App Store](https://www.youtube.com/watch?v=OM0mxReLT4k)**

Meta's new AI personal assistant, Muse, has reached the top of the U.S. App Store charts, surpassing competitor ChatGPT.

📺 CBS News

👁️ 120K • 👍 375 • 💬 117 • ⏱️ 2:08 • 2d ago

---

**[&#39;Godfather&#39; of AI reacts to AI CEOs&#39; UN warnings](https://www.youtube.com/watch?v=u6uRZ6oO6XU)**

Americans view the rapid growth of AI with more concern than optimism, with broad bipartisan support for stronger federal ...

📺 CNN

👁️ 245K • 👍 1K • 💬 500 • ⏱️ 8:07 • 18h ago

---

**[Like Sabine Hossenfelder, I Was Offered Money to Tell You AI Will Kill Us](https://www.youtube.com/watch?v=claxN4oxDuY)**

Can AI really improve itself recursively until it becomes powerful enough to cause human extinction? Nobody sponsored this ...

📺 House of El: AI

👁️ 380K • 👍 24K • 💬 6K • ⏱️ 29:28 • 2d ago

---

**[Government hacked by AI agent for the first known time](https://www.youtube.com/watch?v=9t-p4yYA6YA)**

Australian Prime Minister Anthony Albanese has called the first known case of a government system being hacked by AI ...

📺 CNN

👁️ 285K • 👍 3K • 💬 689 • ⏱️ 1:24 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 0 • ❤️ 3,597 • 1d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 42,469 • ❤️ 2,283 • 4d ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 715,906 • ❤️ 1,739 • 2d ago

---

**[Xing4.0-29B-A4B](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B)**

*XingChen-AGI*

Xing4.0-29B-A4B is a 29B parameter LLM with 4B active parameters, optimized for complex engineering tasks and agent-oriented architectures. It features a 256K context length (extensible to 512K) and supports multi-step planning and tool calling, making it suitable for domain-specific fine-tuning in areas like contract auditing and knowledge-based QA.

`text-generation` `31.2B`

⬇️ 42,950 • ❤️ 1,682 • 7d ago

---

**[Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)**

*Prism ML*

Ternary-Bonsai-2-27B-gguf is a 27B parameter text generation model optimized for on-device inference using llama.cpp. It achieves ~98.2% of FP16 intelligence with a drastically reduced ~5.9 GB footprint by employing end-to-end ternary transformer weights (1.72 bits/weight), enabling efficient reasoning and long context (262K tokens) on consumer hardware with CUDA and Metal support.

`text-generation` `26.9B`

⬇️ 3,109,078 • ❤️ 2,075 • 17h ago

---

**[Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)**

*Comfy Org*

Qwen-Image 2.1 is a diffusion model repackaged for ComfyUI, enabling text-to-image generation and image editing. It leverages Qwen3VL text encoders and a VAE for high-quality visual synthesis.

⬇️ 3,266,380 • ❤️ 717 • 2d ago

---

**[Hemmingway-1](https://huggingface.co/Altworld/Hemmingway-1)**

*Altworld*

Hemmingway-1 is a 27B parameter text-generation model fine-tuned on Qwen3.8-27B, excelling at producing human-like everyday messages and emails. It features a 262,144 token context window and is optimized for non-commercial use, outperforming leading models in communication tasks and human-likeness.

`text-generation` `26.9B`

⬇️ 4,978 • ❤️ 659 • 2d ago

---

**[Audio8-ASR-Infinite](https://huggingface.co/Edge0/Audio8-ASR-Infinite)**

*Edge0*

Audio8 ASR Infinite is a bilingual (Chinese/English) real-time speech recognition model supporting unlimited-length transcription with selectable audio clocks (80/120/160 ms) and configurable transcription delays. It features a rolling KV cache for constant memory/latency and semantic VAD for improved pause detection, ideal for 24/7 streaming applications.

`automatic-speech-recognition` `4.1B`

⬇️ 2,853 • ❤️ 543 • 1d ago

---

**[MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)**

*Xiaomi MiMo*

MiMo-V2.6-Pro-RL is a native omnimodal (text, image, video, audio) LLM with a 1M token context window, excelling at agentic tasks and long-horizon reasoning through advanced reinforcement learning for self-improvement.

`text-generation` `1024.2B`

⬇️ 42,062 • ❤️ 491 • 3d ago

---

**[ZDTaichu5.0-9B](https://huggingface.co/TaichuAI/ZDTaichu5.0-9B)**

*zidongtaichu*

ZDTaichu5.0-9B is a multimodal foundation model excelling in general visual understanding, spatial reasoning, and agentic tool use, supporting text, images, and any-resolution video inputs for embodied AI research and complex visual question answering.

`image-text-to-text` `9.8B`

⬇️ 9,498 • ❤️ 1,045 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 144 • 💬 6 • ⭐ 108,509 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://huggingface.co/papers/2609.24984)**

*Wangbo Yu, Kunhao Liu, Wenbo Hu et al. (11 authors)*

🏢 ARC Lab, Tencent

Video world models enable interactive exploration of dynamic environments, yet struggle to respect prior observations over long horizons and across viewpoints. We present WorldCrafter, a video world model that learns a camera-queryable implicit 3D-aware memory for this purpose. The key insight is to let the requested viewpoint shape how multi-view evidence is compressed into the video generator's limited token budget. Trained jointly with the video generator, a memory encoder and pose-conditioned readout module integrate historical observations into a fixed set of target view-specific tokens before denoising, without explicit depth-based correspondences. By combining this memory with recent temporal context and few-step distillation, WorldCrafter enables streaming scene exploration from a single input image or text prompt. Experiments across static and dynamic scenes show substantial gains in long-horizon consistency and camera-control accuracy while preserving visual quality during minute-scale exploration.

▲ 149 • 💬 4 • ⭐ 348 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24984) • [💻 code](https://github.com/TencentARC/WorldCrafter) • [🔗 project](https://drexubery.github.io/WorldCrafter)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 177 • 💬 19 • ⭐ 67,915 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[GAE: Learning a Geometry-Native Latent Space for 3D-Consistent World Generation](https://huggingface.co/papers/2609.24981)**

*Jiahao Lu, Minghao Yin, Wenbo Hu et al. (8 authors)*

🏢 ARC Lab, Tencent

We present a compact geometry-native latent space as a shared foundation for perception and generation. Visual generators can produce photorealistic frames without preserving a consistent 3D scene. We argue that this is not only a modeling problem but also a representation problem: generators typically evolve appearance-centric latents, while perception models recover geometry in a semantically rich space that encodes cross-view structure. Rather than adding geometry as another output, we reparameterize a geometry foundation model's features into a compact latent space for generation. We realize this shift with the geometry-native autoencoder (GAE), whose latent is jointly decodable to appearance, depth, cameras, and point maps. With this state, a standard conditional flow supports diverse generation tasks. In controlled comparisons that hold the generator and training protocol fixed, replacing the latent with GAE improves both visual quality and independently measured 3D coherence: FVD falls by 12.7% and 23.1% on RealEstate10K and DL3DV, and camera-trajectory error is halved on RealEstate10K. Together, these results show that the latent space is central to geometry-consistent generation and can serve as a shared interface between perception and generation.

▲ 49 • 💬 4 • ⭐ 308 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24981) • [💻 code](https://github.com/TencentARC/GAE-GeometricAutoEncoder) • [🔗 project](https://jiah-cloud.github.io/GAE.github.io/)

---

**[GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay](https://huggingface.co/papers/2609.25001)**

*Yiran Wang, Xingyilang Yin, Junfu Pu et al. (15 authors)*

🏢 Tencent

Modern video games provide a measurable testbed for AI models, combining abilities of visual understanding, instruction decomposition, goal planning, and precise action control over multiple temporal horizons. Existing datasets and benchmarks, however, either cover a narrow range of games, lack language instructions, or rely on high-variance online rollouts. To address these challenges, we introduce GameHorizon, a unified data and evaluation suite that measures gameplay capabilities at different horizons for diverse model families. GameHorizon Suite consists of three components. First, GameHorizon-Annotator is a scalable and automated annotation pipeline for multi-horizon instructions. Second, utilizing the pipeline, we construct GameHorizon-Data, the first large-scale AAA gameplay dataset with temporally aligned videos, player actions, and multi-horizon instructions. It comprises 5,000 hours of recordings from 21 games, collected by 100 human expert players. Third, we build GameHorizon-Bench with reproducible offline and stepwise online testing. The offline track enables reproducible evaluation using thousands of standardized questions organized into three primary tasks and a series of diagnostic variants, while the online track tests whether offline scores reflect actual gameplay capabilities and localizes failures to specific steps within long-horizon gameplay. Based on our GameHorizon Suite, we evaluate 47 models through more than one million model invocations, revealing a meaningful hierarchy of task difficulty and pronounced differences in model capabilities. Our work can provide a standardized yardstick for evaluating gameplay capabilities across horizons and model families. We will release our dataset, annotator, and benchmark to facilitate future research.

▲ 130 • 💬 3 • ⭐ 237 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.25001) • [💻 code](https://github.com/TencentARC/GameHorizon) • [🔗 project](https://gamehorizon-suite.github.io/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 89 • 💬 7 • ⭐ 89,123 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 78 • 💬 3 • ⭐ 10,283 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding](https://huggingface.co/papers/2604.09557)**

*Talor Abramovich, Maor Ashkenazi, Carl et al. (9 authors)*

🏢 NVIDIA

Speculative Decoding evaluation requires diverse workloads to accurately measure performance, which existing benchmarks lack, prompting the introduction of SPEED-Bench for standardized assessment across semantic domains and serving regimes.

▲ 14 • 💬 2 • ⭐ 4,207 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.09557) • [💻 code](https://github.com/NVIDIA/Model-Optimizer) • [🔗 project](https://huggingface.co/blog/nvidia/speed-bench)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 211 • 💬 3 • ⭐ 4,602 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](https://huggingface.co/papers/2609.20519)**

*Haozhe Liu, Tian Ye, Sensen Gao et al. (14 authors)*

🏢 NVIDIA

As coding agents move from supervised code completion to unattended, around-the-clock exploration, their work expands from isolated predictions into long trajectories of reasoning, tool use, and feedback. Token efficiency therefore becomes important for scaling recursive self-improvement. We take an RSI-inspired approach at the harness layer, scaling auto-research loops across increasingly numerous and diverse environments for harness rollouts. At this scale, the process yields reusable improvements that transfer beyond their development setting, moving automated harness discovery toward production-level outcomes. Four mechanisms survive selection and form SoL-Pi, spanning action execution, context compaction, observation handling, and delegated reading. On the 51-task EdgeBench evaluation, SoL-Pi achieves performance comparable to Pi across GPT-5.6 Sol and Opus 5 while reducing recorded token traffic by 44.7-49.0% and API cost by about one third. In other words, estimated hourly savings are \8.75-13.50 relative to native Codex and Claude Code harnesses, and \4.36-5.71 relative to Pi.

▲ 130 • 💬 3 • ⭐ 3,055 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2609.20519) • [💻 code](https://github.com/NVlabs/SoL-Pi) • [🔗 project](https://nvlabs.github.io/SoL-Pi/)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 6.8k • 🔱 2.0k • 1d ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 4.8k • 🔱 304 • 4d ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 4.1k • 🔱 184 • 2d ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.8k • 🔱 184 • 1d ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 2.8k • 🔱 53 • 3d ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 2.6k • 🔱 245 • 1d ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 2.4k • 🔱 454 • 8d ago

---

**[yibie/awesome-jev](https://github.com/yibie/awesome-jev)**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

`Python` `awesome` `awesome-list` `jev` `llm`

⭐ 1.7k • 🔱 241 • 6h ago

---

**[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)**

Free SEO MCP server + open-source SEO and GEO skills for Claude: keyword research, rank tracking, audits, backlinks, AI visibility on your real GSC/GA4/ads data. claude mcp add ryze --transport http https://connector.get-ryze.ai/mcp

`Shell` `ai-seo` `ai-visibility` `backlinks` `claude` `claude-code`

⭐ 1.6k • 🔱 352 • 1d ago

---

**[hydra-db/open-glean](https://github.com/hydra-db/open-glean)**

An open-source AI platform for knowledge work. Connect your apps, find answers, and get work done.

`TypeScript`

⭐ 1.5k • 🔱 516 • 8d ago

---

---

*Generated by PeekDeck - A glance is all you need*
