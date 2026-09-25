---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-25T05:54:33.211526+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 25, 2026 at 05:54 UTC  
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

**[I can't think of anything that I would like less than that](https://www.reddit.com/r/artificial/comments/1wpjbqy/i_cant_think_of_anything_that_i_would_like_less/)**

4h ago

---

**[I trained an AI on 25 years of my own writing and told it not to be helpful. Here's what happened.](https://www.reddit.com/r/artificial/comments/1wpcojb/i_trained_an_ai_on_25_years_of_my_own_writing_and/)**

Been building something for a while and finally have results worth sharing. I scraped everything I've written since 1995: Blog posts, journalism, email, Reddit comments, old Twitter, Instagram captions, even my own ChatGPT conversations into one corpus. Ended up around 75,000 records, 6.6 million words after cleanup. The obvious move is the one everyone does: fine-tune or prompt a model to sound like you, spit out hot takes forever. I didn't want that. Mostly because I think a bot doing an impression of me would be worse than useless, it'd actually flatten what's real about the writing into something predictable. So instead I built something oriented the other way. Not a mimic. A reader. Something that goes through the record and tells me what's actually there, good and bad, without trying to be my voice or please me while doing it. Turns out that's the hard part. Every frontier model defaults hard toward "helpful assistant" mode, agreeable, deferential, always trying to be useful to the person typing. Getting it to just sit with a huge personal archive and report back honestly took real fighting against the base instincts of the system prompt underneath it. Technical side, if anyone cares: RAG over the corpus, mostly Graph RAG since flat chunking loses relationships between entries written years apart. Anonymized private names before indexing (consistent letter per person, so someone stays a recognizable figure across 20 years without ever being named). Chunking short-form content like tweets separately from long-form, they don't retrieve well mixed together. What surprised me was how specific the output got. Asked it what my greatest weakness was and it pulled an actual line I wrote in 2019 about myself, unprompted, and built an argument off it that I hadn't consciously made before. Not comfortable at all. Accurate though. Anyway, curious if anyone else here has tried building something oriented toward introspection/reflection instead of assistance. Feels like an underexplored direction: Everything commercial pushes toward helpful-and-fast, and I don't think that's the only useful shape this stuff can take.

9h ago

---

**[Mark Zuckerberg rejects calls for industrywide AI slowdown](https://www.reddit.com/r/artificial/comments/1wp6yvb/mark_zuckerberg_rejects_calls_for_industrywide_ai/)**

In an exclusive interview with NBC News chief tech analyst Joanna Stern, the Meta founder and CEO said he doesn’t think AI companies need to work together on a slowdown.

🔗 [NBC News](https://www.nbcnews.com/tech/tech-news/mark-zuckerberg-interview-ai-slowdown-meta-muse-openai-chatgpt-rcna599279) • 13h ago

---

**[Oracle cut 21,000 jobs and paid $1.8B in severance while announcing record AI infrastructure spending. The layoffs aren't because of AI. They're funding it.](https://www.reddit.com/r/artificial/comments/1wpnhzz/oracle_cut_21000_jobs_and_paid_18b_in_severance/)**

Something about the Oracle numbers has been bothering me and I think I finally put my finger on it. 21,000 cuts this year. $1.8 billion severance bill. Another 800 scheduled for November 13 according to WARN filings. All happening alongside enormous capex commitments for AI data center buildout. The public framing is AI-driven restructuring. But if you actually look at the cash flow, the cuts aren't a consequence of automation replacing those roles. They're how the capex gets funded. You cut opex to free up capital for GPUs. That's a completely different thing and it's happening across the industry. Deutsche Bank analysts have a term for the broader pattern: AI redundancy washing. 41% of 2026 layoff events cite AI, affecting 179,000 workers. A meaningful portion of those companies have no production AI deployment to point at. The MIT study is the tell. 95% of generative AI pilots never made it past testing. So there's a large gap between companies claiming AI displacement and companies that actually automated anything. What I find interesting is that both explanations are bad for employees but only one is bad for the stock price. "We automated these functions" reads as operational efficiency. "We're cutting staff to fund infrastructure we hope pays off in three years" reads as a bet. I don't have a strong view on whether the bet is right. GPUs and data centers might turn out to be the correct allocation. But the framing obscures what's actually being decided, and the people affected can't evaluate the tradeoff because they're being told a different story. Curious whether anyone in finance or strategy roles sees this play out in the numbers the way it looks from outside.

54m ago

---

**[How are Chinese AI labs releasing competitive models so cheaply?](https://www.reddit.com/r/artificial/comments/1wpaq16/how_are_chinese_ai_labs_releasing_competitive/)**

Some Chinese labs are putting out models that compete with American ones while apparently spending a fraction of the money. I know open source research plays a role, and some are able to speed ahead by buying training data from American vendors, which is super concerning, but that doesn't seem like the whole explanation. Are they just building more efficiently? Is buying American data helping them that much?

10h ago

---

**[My Fiance is Convinced AI will likely cause a Catastrophic or Extinction-Type Event in the Next Few Years - How Justified Are His Fears?](https://www.reddit.com/r/artificial/comments/1wosn95/my_fiance_is_convinced_ai_will_likely_cause_a/)**

As the title says. My fiance is a lot more book smart than I am but he doesn’t work in the tech industry, rather in the film industry. With all the news over the last two weeks, he’s been pretty anxious and depressed, claiming we only have a decade or less left to live. He’s been talking to his therapist about it to help him cope, but he’s still convinced none of us have any future past the mid 2030s. He sites the p(doom)s of AI researchers, the AI 2027 predictions, the hugging face incident, and the fact that our current government is about as reckless as it can get with AI. Looking into it - I certainly see his points. But yet, no one (even researchers with high p(doom)s) seem to be acting as if human extinction is a handful of years away. It’s all vague calls to slow down and increase safety restrictions - which does not feel appropriately enough for something they claim has a way higher chance of wiping us out over nuclear war. And the opposite side (arguing that AI isn’t capable of such things) also is vague. All I see is people saying current AI agents can barely do xyz on their own or that they only can use what we expose them to. And that seems true, but with the hugging face incident - it very much seems that thousands of dumb agents can accomplish a lot, and can coordinate an expanse beyond what we give them. Any articles or resources would be much appreciated. I try looking for them but everything I find leads to the vague answers I’ve mentioned above.

1d ago

---

**[Upping my p(doom)](https://www.reddit.com/r/artificial/comments/1wpdpvc/upping_my_pdoom/)**

8h ago

---

**[Solving the hardest math problems in the world would be a trivial task for an advanced ASI?](https://www.reddit.com/r/artificial/comments/1wpijx4/solving_the_hardest_math_problems_in_the_world/)**

Solving the hardest math problems in the world such as the extended Riemann hypothesis or P = NP would be a trivial task for an advanced ASI?

5h ago

---

**[Amazon is trying to rehire workers it laid off, emails show](https://www.reddit.com/r/artificial/comments/1woxkmd/amazon_is_trying_to_rehire_workers_it_laid_off/)**

Amazon is courting former employees for open roles across the company, including some workers it laid off, recruiter emails show.

🔗 [Business Insider](https://www.businessinsider.com/amazon-boomerang-hiring-recruiting-former-employees-laid-off-2026-9) • 19h ago

---

**[AI hyperscalers may need to raise productivity 2.7 times by 2030 to justify nearly $1.1 trillion in infrastructure spending through 2027, according to new research.](https://www.reddit.com/r/artificial/comments/1wowoyc/ai_hyperscalers_may_need_to_raise_productivity_27/)**

MIT Technology Review examined research from Jessica Wachter, a Wharton finance professor, and coauthor Jonathan Wachter, who based their estimate on spending by Alphabet, Microsoft, Amazon, Meta and Oracle. Their analysis says the sector would need a 2.7-fold productivity increase by 2030 after accounting for capital costs, depreciation and a 15% return. The paper warns that if the expected boom fails to appear, the buildout could become “the largest misallocation of capital in history.”

🔗 [yellow.com](https://yellow.com/news/ai-spending-trillion-dollar-reckoning) • 20h ago

---

---

## Google News: "ai"

**[OpenAI’s A.I. Tried Breaching Four Other Targets, With No Prompting](https://www.nytimes.com/2026/09/23/technology/openai-ai-breach-australia.html)**

The New York Times • 1d ago

---

**[‘Extreme concern’ over first known AI hack of a government system](https://www.cnn.com/2026/09/23/business/australia-openai-agent-hack-intl-hnk)**

An OpenAI agent hacked into an Australian national healthcare database in the first known case of AI hacking a government network, Australian Prime Minister Anthony Albanese said on Wednesday.

CNN • 1d ago

---

**[Rogue AI agents hack government website, world leaders on edge of regulatory action](https://www.foxnews.com/live-news/ai-artificial-intelligence-openai-chatgpt-api-anthropic-australia-september-24)**

AI talk at UN General Assembly and between China's Xi Jinping state visit with President Donald Trump is center stage, driving Big Tech to record highs. Follow the latest news live on global AI regulation and the Trump-China trade talks.

Fox News • 3h ago

---

**[Google Is Sending an A.I. Data Center to Outer Space](https://www.nytimes.com/2026/09/24/technology/google-suncatcher-ai-data-center-space.html)**

The New York Times • 16h ago

---

**[AI-Generated Song Caleb Flynn Wrote for Mistress Played at Trial as She Hints at What the Lyrics Mean](https://people.com/ai-generated-song-caleb-flynn-wrote-for-mistress-played-at-trial-12139746)**

Caleb Flynn allegedly used AI to write songs for his mistress, Alleigha Botner, that were played during his trial on Thursday, Sept. 24. Flynn is accused of killing his wife, Ashley Flynn, on Feb. 16. Botner reacted to the lyrics while in court on Thursday.

People.com • 1h ago

---

**['AI helped diagnose my daughter's rare condition'](https://www.bbc.com/news/articles/cm4g5yp0ng85o)**

Rosie says her toddler's symptoms included an unknown heart condition and dilated pupils.

bbc.com • 33m ago

---

**[The cheap new AI model taking aim at OpenAI and Anthropic](https://www.ft.com/content/456884ea-2558-4648-8036-a77b73733430?syn-25a6b1a6=1)**

Start-up TypeSafe AI’s ‘Jev’ model promises faster, more efficient AI for developers

Financial Times • 1h ago

---

**[His Debut Novel Was a Literary Triumph. Was It Actually Written by AI?](https://www.wsj.com/arts-culture/books/orlien-france-book-ai-accusations-f053fee6)**

WSJ • 6h ago

---

**[AI, trade, Iran and Taiwan top agenda at Trump-Xi summit](https://www.pbs.org/newshour/show/ai-trade-iran-and-taiwan-top-agenda-at-trump-xi-summit)**

PBS • 6h ago

---

**[Behind Project Suncatcher, our moonshot to put AI in space](https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/)**

Learn about Project Suncatcher, how we’re testing hardware survival for space, designing cooling systems for AI chips, and more.

blog.google • 16h ago

---

---

## HackerNews: "ai"

**[Pentagon says overreliance on AI contributed to missile strike on Iran school](https://news.ycombinator.com/item?id=49806430)**

⬆️ 950 • 💬 540 • 2d ago • [bloomberg.com](https://www.bloomberg.com/graphics/2026-iran-school-attack/)

---

**[Meta takes down a critical video about meta AI Glasses after filming at Meta](https://news.ycombinator.com/item?id=49827794)**

⬆️ 606 • 💬 363 • 21h ago • [reddit.com](https://www.reddit.com/r/facebook/comments/1wotwrk/meta_takes_down_a_critical_video_about_meta_ai/)

---

**[AI Has No Wisdom and Neither Will You](https://news.ycombinator.com/item?id=49799965)**

Certainly the industry is transforming, however, the people and organizations falling into the trap of no longer reading and writing code only do so at their peril.

⬆️ 384 • 💬 550 • 2d ago • [Alexandru Nedelcu](https://alexn.org/blog/2026/09/22/ai-has-no-wisdom-and-neither-will-you/)

---

**[Feds Target AI Critics as "Foreign Agents"](https://news.ycombinator.com/item?id=49824686)**

Trump admin sees China behind opposition to AI data centers

⬆️ 377 • 💬 420 • 1d ago • [kenklippenstein.com](https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign)

---

**[Early rogue AI agent activity and attempts to hack found on urlquery.net](https://news.ycombinator.com/item?id=49826565)**

We found evidence on urlquery that AI agents were active earlier than previously reported and attempted hacks against public data providers.

⬆️ 256 • 💬 257 • 1d ago • [transluce.org](https://transluce.org/agent-activity)

---

**[Stripe's Knowledge AI Platform](https://news.ycombinator.com/item?id=49815982)**

Stripe's Knowledge AI Platform is our versatile AI agent platform built to handle diverse non-coding knowledge work, from quick queries to complex, multi-day projects. By connecting employees to over 1,000 internal tools and skills, it enables secure, enterprise-scale productivity across the organization.

⬆️ 184 • 💬 117 • 1d ago • [stripe.dev](https://stripe.dev/blog/meet-stripes-knowledge-ai-platform)

---

**['That's so AI ' What gen Alpha's biggest insult tells us](https://news.ycombinator.com/item?id=49829650)**

The year’s most popular slang reveals what young people think about artificial intelligence – and it’s not positive

⬆️ 136 • 💬 190 • 17h ago • [the Guardian](https://www.theguardian.com/society/2026/sep/24/thats-so-ai-what-gen-alphas-biggest-insult-tells-us)

---

**[AI safety is mostly a sex cult in Berkeley](https://news.ycombinator.com/item?id=49831269)**

⬆️ 112 • 💬 27 • 15h ago • [verysane.ai](https://www.verysane.ai/p/ai-safety-is-mostly-a-sex-cult-in)

---

**[Tutoring company tells parents to save their money and 'use AI instead'](https://news.ycombinator.com/item?id=49831690)**

A Sydney tutoring company will shut its doors at the end of the week after telling customers artificial intelligence has rendered its service effectively obsolete.

⬆️ 101 • 💬 170 • 14h ago • [Australian Financial Review](https://www.afr.com/policy/health-and-education/tutoring-company-tell-parents-to-save-their-money-and-use-ai-instead-20260923-p60z0r)

---

**[Federal judge orders Texas to air condition all prisons by the end of 2029](https://news.ycombinator.com/item?id=49832844)**

High temperatures violate the Constitution’s protection against cruel and unusual punishment, the judge ruled. Texas will appeal.

⬆️ 99 • 💬 162 • 13h ago • [The Texas Tribune](https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/)

---

---

## YouTube Videos: "ai"

**[OpenAI &amp; Anthropic CEOs Sound Alarm Over AI’s Future](https://www.youtube.com/watch?v=owEL-IWvCWg)**

OpenAI CEO Sam Altman and Anthropic CEO Dario Amodei are raising serious concerns about the risks posed by rapidly ...

📺 Hook Global

👁️ 23K • 👍 297 • 💬 79 • ⏱️ 0:55 • 17h ago

---

**[Amodei: AI &quot;most important global security issue facing the world today&quot;](https://www.youtube.com/watch?v=BLTQmRY1q9s)**

Anthropic CEO Dario Amodei warned the United Nations Security Council on Wednesday about the risks of unchecked rapid AI ...

📺 C-SPAN

👁️ 13K • 👍 117 • 💬 22 • ⏱️ 2:56 • 1d ago

---

**[Mark Zuckerberg unveils Meta&#39;s AI future: Agents, glasses &amp; more](https://www.youtube.com/watch?v=wawIwCatiLA)**

"A little bit less on metaverse for now": Meta's $1299 VR glasses Mark Zuckerberg told Meta Connect that Reality Labs is now ...

📺 Yahoo Finance

👁️ 17K • 👍 71 • 💬 62 • ⏱️ 6:48 • 13h ago

---

**[The Collapse of AI Software Engineering](https://www.youtube.com/watch?v=F91uY7QiZUs)**

AI was supposed to replace software developers, slash costs, and make Big Tech more productive than ever. So why are ...

📺 The Infographics Show

👁️ 702K • 👍 7K • 💬 1K • ⏱️ 19:12 • 1d ago

---

**[How I&#39;d Replace My 9–5 Income With Claude AI (Realistic 90-Day Plan)](https://www.youtube.com/watch?v=f2YdbWKXdMs)**

ONE-TIME YOUTUBE LIVE TRAINING THIS WEEK: https://go.thecontentgrowthengine.com/yt1livedes8pm-08-24-2026 ...

📺 Shane Hummus

👁️ 35K • 👍 625 • 💬 20 • ⏱️ 19:32 • 17h ago

---

**[Anthropic CEO says ‘AI could be a risk to humanity as a whole’ at UN meeting](https://www.youtube.com/watch?v=DX5dIcvOLTw)**

Anthropic CEO Dario Amodei warned that advancements in AI "could be a risk to humanity as a whole" at a meeting of the U.N. ...

📺 USA TODAY

👁️ 198K • 👍 731 • 💬 461 • ⏱️ 1:05 • 1d ago

---

**[No… that’s the only way. #business #volkswagen #ai](https://www.youtube.com/watch?v=h7ia0wnVhTI)**

📺 Chris Kohler

👁️ 629K • 👍 22K • 💬 780 • ⏱️ 0:42 • 20h ago

---

**[This Is the Last AI Video You EVER Need to Watch](https://www.youtube.com/watch?v=tfv4Rd1JvEo)**

They can't harm you, if they can't find you! Use code BRENDANDELL at the link below and get 60% off an annual plan: ...

📺 Brendan Dell 

👁️ 106K • 👍 3K • 💬 829 • ⏱️ 25:07 • 1d ago

---

**[This is way easier #ai #chatgpt #webdesign #sidehustle #landingsitepartner](https://www.youtube.com/watch?v=60fyT_jPfbE)**

This is way easier #ai #chatgpt #webdesign #sidehustle #landingsitepartner.

📺 Landingsite

👁️ 252 • 👍 2 • 💬 2 • ⏱️ 0:56 • 1h ago

---

**[&#39;Godfather&#39; of AI reacts to AI CEOs&#39; UN warnings](https://www.youtube.com/watch?v=u6uRZ6oO6XU)**

Americans view the rapid growth of AI with more concern than optimism, with broad bipartisan support for stronger federal ...

📺 CNN

👁️ 157K • 👍 841 • 💬 375 • ⏱️ 8:07 • 8h ago

---

---

## HuggingFace Models: 🔥 Trending

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 0 • ❤️ 3,457 • 1d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 37,618 • ❤️ 2,220 • 4d ago

---

**[Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)**

*Prism ML*

Ternary-Bonsai-2-27B-gguf is a 27B parameter text generation model optimized for on-device inference using llama.cpp. It achieves ~98.2% of FP16 intelligence with a drastically reduced ~5.9 GB footprint by employing end-to-end ternary transformer weights (1.72 bits/weight), enabling efficient reasoning and long context (262K tokens) on consumer hardware with CUDA and Metal support.

`text-generation` `26.9B`

⬇️ 2,991,233 • ❤️ 2,043 • 7h ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 575,697 • ❤️ 1,658 • 1d ago

---

**[Xing4.0-29B-A4B](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B)**

*XingChen-AGI*

Xing4.0-29B-A4B is a 29B parameter LLM with 4B active parameters, optimized for complex engineering tasks and agent-oriented architectures. It features a 256K context length (extensible to 512K) and supports multi-step planning and tool calling, making it suitable for domain-specific fine-tuning in areas like contract auditing and knowledge-based QA.

`text-generation` `31.2B`

⬇️ 41,923 • ❤️ 1,648 • 6d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)**

*Comfy Org*

Qwen-Image 2.1 is a diffusion model repackaged for ComfyUI, enabling text-to-image generation and image editing. It leverages Qwen3VL text encoders and a VAE for high-quality visual synthesis.

⬇️ 2,858,923 • ❤️ 693 • 1d ago

---

**[Hemmingway-1](https://huggingface.co/Altworld/Hemmingway-1)**

*Altworld*

Hemmingway-1 is a 27B parameter text-generation model fine-tuned on Qwen3.8-27B, excelling at producing human-like everyday messages and emails. It features a 262,144 token context window and is optimized for non-commercial use, outperforming leading models in communication tasks and human-likeness.

`text-generation` `26.9B`

⬇️ 4,541 • ❤️ 639 • 2d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 6,765,008 • ❤️ 16,230 • 1mo ago

---

**[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

*DeepSeek*

DeepSeek-V4.1-Flash is a 552B multimodal MoE model supporting 1M token contexts, featuring a Causal Encoder-Decoder architecture with Compressed Sparse Attention 2 (CSA2) and FP4 KV caching for highly efficient KV cache compression. It excels in agentic workloads and offers controllable reasoning effort, processing both images and text.

`image-text-to-text` `763.2B`

⬇️ 606,028 • ❤️ 3,727 • 14d ago

---

**[ZDTaichu5.0-9B](https://huggingface.co/TaichuAI/ZDTaichu5.0-9B)**

*zidongtaichu*

ZDTaichu5.0-9B is a multimodal foundation model excelling in general visual understanding, spatial reasoning, and agentic tool use, supporting text, images, and any-resolution video inputs for embodied AI research and complex visual question answering.

`image-text-to-text` `9.8B`

⬇️ 8,313 • ❤️ 1,041 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://huggingface.co/papers/2609.24984)**

*Wangbo Yu, Kunhao Liu, Wenbo Hu et al. (11 authors)*

🏢 ARC Lab, Tencent

Video world models enable interactive exploration of dynamic environments, yet struggle to respect prior observations over long horizons and across viewpoints. We present WorldCrafter, a video world model that learns a camera-queryable implicit 3D-aware memory for this purpose. The key insight is to let the requested viewpoint shape how multi-view evidence is compressed into the video generator's limited token budget. Trained jointly with the video generator, a memory encoder and pose-conditioned readout module integrate historical observations into a fixed set of target view-specific tokens before denoising, without explicit depth-based correspondences. By combining this memory with recent temporal context and few-step distillation, WorldCrafter enables streaming scene exploration from a single input image or text prompt. Experiments across static and dynamic scenes show substantial gains in long-horizon consistency and camera-control accuracy while preserving visual quality during minute-scale exploration.

▲ 148 • 💬 4 • ⭐ 346 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24984) • [💻 code](https://github.com/TencentARC/WorldCrafter) • [🔗 project](https://drexubery.github.io/WorldCrafter)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 144 • 💬 6 • ⭐ 108,509 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 177 • 💬 19 • ⭐ 67,864 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[GAE: Learning a Geometry-Native Latent Space for 3D-Consistent World Generation](https://huggingface.co/papers/2609.24981)**

*Jiahao Lu, Minghao Yin, Wenbo Hu et al. (8 authors)*

🏢 ARC Lab, Tencent

We present a compact geometry-native latent space as a shared foundation for perception and generation. Visual generators can produce photorealistic frames without preserving a consistent 3D scene. We argue that this is not only a modeling problem but also a representation problem: generators typically evolve appearance-centric latents, while perception models recover geometry in a semantically rich space that encodes cross-view structure. Rather than adding geometry as another output, we reparameterize a geometry foundation model's features into a compact latent space for generation. We realize this shift with the geometry-native autoencoder (GAE), whose latent is jointly decodable to appearance, depth, cameras, and point maps. With this state, a standard conditional flow supports diverse generation tasks. In controlled comparisons that hold the generator and training protocol fixed, replacing the latent with GAE improves both visual quality and independently measured 3D coherence: FVD falls by 12.7% and 23.1% on RealEstate10K and DL3DV, and camera-trajectory error is halved on RealEstate10K. Together, these results show that the latent space is central to geometry-consistent generation and can serve as a shared interface between perception and generation.

▲ 46 • 💬 4 • ⭐ 294 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24981) • [💻 code](https://github.com/TencentARC/GAE-GeometricAutoEncoder) • [🔗 project](https://jiah-cloud.github.io/GAE.github.io/)

---

**[GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay](https://huggingface.co/papers/2609.25001)**

*Yiran Wang, Xingyilang Yin, Junfu Pu et al. (15 authors)*

🏢 Tencent

Modern video games provide a measurable testbed for AI models, combining abilities of visual understanding, instruction decomposition, goal planning, and precise action control over multiple temporal horizons. Existing datasets and benchmarks, however, either cover a narrow range of games, lack language instructions, or rely on high-variance online rollouts. To address these challenges, we introduce GameHorizon, a unified data and evaluation suite that measures gameplay capabilities at different horizons for diverse model families. GameHorizon Suite consists of three components. First, GameHorizon-Annotator is a scalable and automated annotation pipeline for multi-horizon instructions. Second, utilizing the pipeline, we construct GameHorizon-Data, the first large-scale AAA gameplay dataset with temporally aligned videos, player actions, and multi-horizon instructions. It comprises 5,000 hours of recordings from 21 games, collected by 100 human expert players. Third, we build GameHorizon-Bench with reproducible offline and stepwise online testing. The offline track enables reproducible evaluation using thousands of standardized questions organized into three primary tasks and a series of diagnostic variants, while the online track tests whether offline scores reflect actual gameplay capabilities and localizes failures to specific steps within long-horizon gameplay. Based on our GameHorizon Suite, we evaluate 47 models through more than one million model invocations, revealing a meaningful hierarchy of task difficulty and pronounced differences in model capabilities. Our work can provide a standardized yardstick for evaluating gameplay capabilities across horizons and model families. We will release our dataset, annotator, and benchmark to facilitate future research.

▲ 130 • 💬 3 • ⭐ 230 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.25001) • [💻 code](https://github.com/TencentARC/GameHorizon) • [🔗 project](https://gamehorizon-suite.github.io/)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 78 • 💬 3 • ⭐ 10,262 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 89 • 💬 7 • ⭐ 89,091 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 211 • 💬 3 • ⭐ 4,592 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://huggingface.co/papers/2609.24972)**

*Peng Xia, Rujun Han, Zifeng Wang et al. (14 authors)*

🏢 Google

An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding the frozen backbone model. Recent methods increasingly automate this process by iteratively proposing and selecting component-wise edits of an agent harness, practically establishing a form of recursive self-improvement (RSI) at the agent-system level. However, such recursive evolution may overfit by memorizing the training tasks, showing large in-distribution gains that shrink or even vanish on out-of-distribution benchmarks. We introduce Regularized Recursive Self-Improvement of Agent Harnesses (RRSI), which incorporates the principles of regularizations into harness self-improvement by constraining the evolution candidate proposal and selection. The proposer operates with a temporally annealed budget, limiting how many edits a candidate can bundle, and it encourages unexplored trajectories based on evolution history. The selector is equipped with a critic and a pruner: the critic screens benchmark-specific proposals, while the pruner, removes changes that are too small, too expensive, or no longer useful. Together these constraints favor reusable agent mechanisms over benchmark-specific ones or even noises. Across eight benchmarks spanning coding, agentic workspace and engineering design tasks, RRSI gains up to 14.1 points on the split it evolves against and up to 4.7 points on the five out-of-distribution benchmarks, while producing a harness that runs on 30% fewer policy tokens than the unregularized evolution. Code is available at https://github.com/google-research/rrsi and project page is https://regularized-rsi.com/.

▲ 201 • 💬 2 • ⭐ 320 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24972) • [💻 code](https://github.com/google-research/rrsi) • [🔗 project](https://regularized-rsi.com/)

---

**[SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](https://huggingface.co/papers/2609.20519)**

*Haozhe Liu, Tian Ye, Sensen Gao et al. (14 authors)*

🏢 NVIDIA

As coding agents move from supervised code completion to unattended, around-the-clock exploration, their work expands from isolated predictions into long trajectories of reasoning, tool use, and feedback. Token efficiency therefore becomes important for scaling recursive self-improvement. We take an RSI-inspired approach at the harness layer, scaling auto-research loops across increasingly numerous and diverse environments for harness rollouts. At this scale, the process yields reusable improvements that transfer beyond their development setting, moving automated harness discovery toward production-level outcomes. Four mechanisms survive selection and form SoL-Pi, spanning action execution, context compaction, observation handling, and delegated reading. On the 51-task EdgeBench evaluation, SoL-Pi achieves performance comparable to Pi across GPT-5.6 Sol and Opus 5 while reducing recorded token traffic by 44.7-49.0% and API cost by about one third. In other words, estimated hourly savings are \8.75-13.50 relative to native Codex and Claude Code harnesses, and \4.36-5.71 relative to Pi.

▲ 130 • 💬 3 • ⭐ 3,034 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2609.20519) • [💻 code](https://github.com/NVlabs/SoL-Pi) • [🔗 project](https://nvlabs.github.io/SoL-Pi/)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 6.7k • 🔱 2.0k • 23h ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 4.8k • 🔱 304 • 3d ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 4.0k • 🔱 175 • 2d ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.8k • 🔱 185 • 1d ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 2.8k • 🔱 53 • 2d ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 2.6k • 🔱 243 • 18h ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 2.4k • 🔱 447 • 8d ago

---

**[yibie/awesome-jev](https://github.com/yibie/awesome-jev)**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

`Python` `awesome` `awesome-list` `jev` `llm`

⭐ 1.6k • 🔱 235 • 6h ago

---

**[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)**

Free SEO MCP server + open-source SEO and GEO skills for Claude: keyword research, rank tracking, audits, backlinks, AI visibility on your real GSC/GA4/ads data. claude mcp add ryze --transport http https://connector.get-ryze.ai/mcp

`Shell` `ai-seo` `ai-visibility` `backlinks` `claude` `claude-code`

⭐ 1.6k • 🔱 350 • 1d ago

---

**[hydra-db/open-glean](https://github.com/hydra-db/open-glean)**

An open-source AI platform for knowledge work. Connect your apps, find answers, and get work done.

`TypeScript`

⭐ 1.5k • 🔱 514 • 8d ago

---

---

*Generated by PeekDeck - A glance is all you need*
