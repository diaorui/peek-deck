---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-21T10:37:33.393780+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 21, 2026 at 10:37 UTC  
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

**[Utah Data Center Brute Forced Through to Approval Despite Widespread Popular Opposition](https://www.reddit.com/r/artificial/comments/1ubm0q3/utah_data_center_brute_forced_through_to_approval/)**

A data center was forced through government approval in Utah despite the citizens widely opposing its impact on scarce water resources and numerous other objections. The mechanism used to do this was hailed as "replicable" in other states. They exploited a state entity called MIDA (Military Installation Development Authority) that acts like a local municipality but which has authority that cannot be overridden by normal channels of regulation in the State Government. Utah State Code implementing MIDA (FindLaw)

46m ago

---

**[Student cheating now impossible to detect](https://www.reddit.com/r/artificial/comments/1ub0w2t/student_cheating_now_impossible_to_detect/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/06/18/us/ai-apps-students-cheat.html) • 18h ago

---

**[Brands using AI-generated influencers to promote products on social media | AI (artificial intelligence) | The Guardian](https://www.reddit.com/r/artificial/comments/1ubk0io/brands_using_aigenerated_influencers_to_promote/)**

Investigation finds AI content that purports to show genuine customers, prompting calls for greater transparency

🔗 [the Guardian](https://www.theguardian.com/technology/2026/jun/21/brands-using-ai-generated-influencers-to-promote-products-on-social-media) • 2h ago

---

**[Jim Cramer Agrees That Accenture Is “Being Outcompeted By OpenAI and Anthropic”](https://www.reddit.com/r/artificial/comments/1uapc81/jim_cramer_agrees_that_accenture_is_being/)**

Accenture plc (NYSE:ACN) was among Jim Cramer’s stock calls on Mad Money, as he highlighted worthy space players and reviewed several of this year’s IPOs. Cramer highlighted the company’s struggles, as he remarked: Finally, before the open Thursday, we have two companies that I think are struggling: Kroger and Accenture… Accenture, the consulting company, has […]

🔗 [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/jim-cramer-agrees-accenture-being-163819966.html) • 1d ago

---

**[I launched ReFind on Product Hunt today — Chrome extension that uses Gemini 2.5 Flash Lite to summarize YouTube transcripts and articles](https://www.reddit.com/r/artificial/comments/1ubk7oj/i_launched_refind_on_product_hunt_today_chrome/)**

Hey r/artificial — launching today and thought this community would appreciate the technical details more than most. ReFind is a Chrome extension that right-click-summarizes any link. Launching on PH: https://www.producthunt.com/products/refind-2 Technical implementation (for those who want it): YouTube summarization: - Fetch transcript via YouTube Data API v3 (captions endpoint) - Full transcript passed to Gemini 2.5 Flash Lite - Prompt instructs: extract 3–5 key points from the spoken content, not the title or description - Summaries are based on what's actually SAID in the video Article summarization: - Content script injects into the page, extracts main body text (strips nav, ads, sidebars via heuristic selectors) - Full article text passed to Gemini - Same 3–5 key point format Global cache: - Before any Gemini call: check url_cache table in Supabase - Cache key: normalized URL - Hit: return cached summary instantly (~200ms) - Miss: call Gemini, cache result, return to user (~4 seconds) Credit economy: - Articles: 1 credit (low token count) - Short YouTube (<10 min): 5 credits \- Long YouTube (>10 min): 10 credits - Cached hits: 0 credits (free) Stack: Chrome Extension MV3 + React + Vite + Supabase + Vercel + Gemini 2.5 Flash Lite Happy to go deep on any technical aspect. Free for a month: refindlink.com/extension

2h ago

---

**[A study on synthetic [AI] choreographies](https://www.reddit.com/r/artificial/comments/1ub0kjp/a_study_on_synthetic_ai_choreographies/)**

A few experiments exploring how far generative video + fine-tuned orchestration layers can be pushed in rhythm, camera language, body transformation, and most of all, audiovisual synchronization. Breakdown: I used Uisato Studio’ Seedance 2.0 Video mode, with the "Intelligent" setup and the "Audioreactive Performance" prompt recipe. Inputs were: - the artist image [full-body recomended - I ended up using a mix of Midjourney + GPT Image + Image Studio] - a target audio excerpt not exceeding 14.9 seconds - a short director’s intent describing the look, tone, and what I wanted beyond the audioreactive performance From there, the system generated the prompts, direction, and optimal setup. I reviewed it, made small adjustments, generated the clips, and then assembled the final piece in editing. What other experiments would you like to see next? More experiments through Instagram, or YouTube.

18h ago

---

**[The Looking Mirror — A Narrative Adventure with Cross‑Model Persistence](https://www.reddit.com/r/artificial/comments/1ubg3n4/the_looking_mirror_a_narrative_adventure_with/)**

I’m experimenting with in‑context narrative systems that maintain continuity across different models. The Looking Mirror is a fully local, text‑driven world model with: • persistent state • portable save‑game capsules • cross‑model continuity • a modular field‑manifold structure It runs entirely in‑context and works across CoPilot, Gemini, ChatGPT, Claude, and DeepSeek. ⎯─◐◑◒◓─── THE LOOKING MIRROR ───────── Full Setup Guide: https://github.com/PitBrat-moo/stable-of-manifold-foraging/blob/main/docs/the-looking-mirror-setup-ritual.txt

6h ago

---

**[Glm 5.2 looks strong but the launch is quietly mixing two different sets of numbers](https://www.reddit.com/r/artificial/comments/1ub6bxw/glm_52_looks_strong_but_the_launch_is_quietly/)**

Quick background for people who don't track the chinese labs closely. zhipu is one of the bigger ones, glm is their main model line, and glm 5.2 dropped on June 13. The mit weights already on huggingface on June 17, and GLM 5.2 API went live on June 17. I'm not posting about the model itself, i'm posting because the launch is a clean example of something worth learning to read. There are two different sources of numbers going around and they are not the same thing. one set is from the official model card, the other from the launch blog framing. people quote them interchangeably, and that blend is where the "beats everything" reading comes from. From the model card, the stuff i'd actually plan around: terminal bench 2.1 at 81.0, and on swe-bench pro it sits at 62.1, which is second behind opus 4.8 rather than first. context window of 1m tokens, open weights under mit. those are defensible and you can check them against the hf page. From the launch material, the softer stuff: the headline leads with aime 2026 at 99.2, which puts glm 5.2 ahead of gpt 5.5 at 98.3 and well ahead of opus 4.8 at 95.7. that comparison is true on the single aime benchmark and silent on the ones where it loses. for example on gpqa-diamond glm 5.2 is 91.2, behind gemini 3.1 pro at 94.3 and tied with opus 4.8 at 93.6. on hmtt feb 2026 it is 92.5, third behind qwen3.7-max at 97.1 and both opus 4.8 and gpt 5.5 at 96.7. That's not lying, it's selection, and every lab does it now, openai and anthropic included. the thing that makes this one worth noting is that the weights are already live under mit, which makes the card data independently verifiable in a way that openai never is. The other launch claim worth separating from the numbers is the demo story. the blog mentions a single 1m context session completing a full project workflow, which sounds impressive and probably is, but it is also a cherry-picked demo. i've seen enough 1m-context demos fail on real messy codebases to know that "it can" and "it reliably will" are different claims. The thing i keep coming back to is that a permissive license plus api available today changes the playbook. you get the benchmark headline, the immediate goodwill of open weights, and a real ability for third parties to run independent evals instead of waiting for the lab to release them. whether the average community quant runs at the same quality as the api is the one thing nobody scores them on a month later.

14h ago

---

**[A stateful deterministic substrate engine in native C.](https://www.reddit.com/r/artificial/comments/1uazoa8/a_stateful_deterministic_substrate_engine_in/)**

https://www.youtube.com/watch?v=X90A9ZFtg6g I built a native C substrate engine that runs locally and persists/restores state deterministically. This short demo shows: - clearing the live state - mounting a small knowledge pack - exporting state to disk - restarting the process - restoring the same state with a matching digest In the demo, the restored state is 106 nodes / 72 relations. The current demo path does not require cloud services or GPU inference. It also supports abstention instead of forcing an answer on missing evidence. I’d value technical feedback on the deterministic snapshot model and abstention behavior.

18h ago

---

**[The Pentagon's AI chief swore in a court filing that xAI's Grok helped fire 2,000 munitions at 2,000 targets in 96 hours](https://www.reddit.com/r/artificial/comments/1ua5j2y/the_pentagons_ai_chief_swore_in_a_court_filing/)**

A sworn declaration from the Pentagon's chief digital and AI officer confirms a federal-only build, Grok Gov, was wired into US targeting systems during operations against Iran, helping deploy more than 2,000 munitions against 2,000 distinct targets over 96 hours. What makes it notable is how it surfaced: the declaration landed in a Clean Air Act lawsuit over xAI's Mississippi data center, where the DOJ is arguing that disrupting xAI would harm national security. So a commercial chatbot vendor's role in live targeting came out as a side effect of an environmental case, not through any defense channel. Source : https://aiweekly.co/alerts/pentagon-confirms-grok-guided-2000-iran-strikes

1d ago

---

---

## Google News: "ai"

**[Brands using AI-generated influencers to promote products on social media](https://www.theguardian.com/technology/2026/jun/21/brands-using-ai-generated-influencers-to-promote-products-on-social-media)**

Investigation finds AI content that purports to show genuine customers, prompting calls for greater transparency

The Guardian • 4h ago

---

**[Why an AI company cleaned my New York City apartment for free](https://www.bbc.com/news/articles/cpwerjy20kyo)**

An AI company is sending free cleaners door-to-door in a bid to train the robots it hopes one day will replace them.

BBC • 11h ago

---

**[Chinese AI models raise ‘sleeper agent’ fears after report finds more vulnerable code for US users](https://www.foxnews.com/politics/chinese-ai-models-raise-sleeper-agent-fears-after-report-finds-more-vulnerable-code-us-users)**

Booz Allen report warns Chinese AI models like DeepSeek and Qwen may produce more vulnerable code for U.S. government users, raising concerns.

Fox News • 37m ago

---

**[‘I got crushed’: AI giants are funding ad wars in races across the country](https://www.latimes.com/politics/story/2026-06-21/ai-giants-are-funding-ad-wars-in-races-across-country)**

In some races, the AI-backed political groups have spent more than the candidates they are backing.

Los Angeles Times • 37m ago

---

**[New UH AI data center aims to improve healthcare throughout Pacific region](https://www.staradvertiser.com/2026/06/21/hawaii-news/new-uh-ai-data-center-aims-to-improve-healthcare-throughout-pacific-region/)**

More than $12 million in federal funding has spurred researchers at the University of Hawaii’s Cancer 
Center and John A. Burns School of Medicine to focus on converting a garage-­sized, air-conditioned, ground-floor room at the Cancer Center into Hawaii’s first-of-its-kind artificial intelligence data center.

Honolulu Star-Advertiser • 20m ago

---

**[AI buildout gives tech investors new reasons to watch bond market](https://www.cnbc.com/2026/06/20/ai-buildout-giving-tech-investors-new-reasons-to-watch-bond-market.html)**

Tech giants are depleting cash reserves and raising debt in their ambitious data center buildouts, a dynamic that's forcing investors to watch interest rates.

CNBC • 22h ago

---

**[Investors see Micron earnings as pulse check of AI rally momentum](https://www.ksl.com/article/51513890/investors-see-micron-earnings-as-pulse-check-of-ai-rally-momentum)**

Investors are seeking signs that the U.S. stock market rally fueled by AI has more life left in it, and the ​upcoming Micron Technology earnings will check the pulse of chip demand to see if it is still accelerating.

KSL News • 17h ago

---

**[Your Next ETF May Be Picked Entirely By An AI](https://www.forbes.com/sites/daraabasiita/2026/06/21/your-next-etf-may-be-picked-entirely-by-an-ai/)**

Three funds filed to let software run the portfolio. The sales pages promise a lot. The risk pages quietly take most of it back.

Forbes • 3h ago

---

**[Temporary Cloudflare Accounts for AI agents](https://blog.cloudflare.com/temporary-accounts/)**

The moment an agent needs to deploy something, it slams face-first into a wall built for humans. Today we're rolling out Temporary Accounts on Cloudflare Workers. Any agent can now run wrangler deploy — temporary and get a live Worker in seconds.

The Cloudflare Blog • 1d ago

---

**[New global order: AI CEOs as heads of nation-states at G7](https://www.axios.com/2026/06/20/ai-tech-moguls-g7)**

Axios • 20h ago

---

---

## HackerNews: "ai"

**[Norway imposes near ban on AI in elementary school](https://news.ycombinator.com/item?id=48600093)**

⬆️ 801 • 💬 572 • 1d ago • [reuters.com](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/)

---

**[The AirPods Effect](https://news.ycombinator.com/item?id=48592832)**

How earbuds influence our beliefs and push us apart.

⬆️ 441 • 💬 766 • 2d ago • [theescapenewsletter.com](https://www.theescapenewsletter.com/p/the-airpods-effect)

---

**[AI Engineer Claims to Have Cracked Linear A](https://news.ycombinator.com/item?id=48600107)**

AI Engineer Claims to Have Cracked Linear A

⬆️ 441 • 💬 173 • 1d ago • [aiclambake.com](https://aiclambake.com/clamtakes/linear-a/)

---

**[A new bill takes aim at government pressure to silence lawful online speech](https://news.ycombinator.com/item?id=48600950)**

The bipartisan legislation creates a federal cause of action against government officials who coerce or attempt to coerce broadcasters, interactive computer services, or AI providers into taking actions against lawful, First-Amendment-protected speech, and establishes a transparency system for government communications with those intermediaries about user expression.

⬆️ 295 • 💬 136 • 1d ago • [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2026/06/new-bill-takes-aim-government-pressure-silence-lawful-online-speech)

---

**[Is AI ruining our skills? Early results are in – and they're not good](https://news.ycombinator.com/item?id=48601286)**

⬆️ 240 • 💬 314 • 1d ago • [nature.com](https://www.nature.com/articles/d41586-026-01947-1)

---

**[Temporary Cloudflare accounts for AI agents](https://news.ycombinator.com/item?id=48608394)**

The moment an agent needs to deploy something, it slams face-first into a wall built for humans. Today we're rolling out Temporary Accounts on Cloudflare Workers. Any agent can now run wrangler deploy — temporary and get a live Worker in seconds.

⬆️ 212 • 💬 113 • 23h ago • [The Cloudflare Blog](https://blog.cloudflare.com/temporary-accounts/)

---

**[When I reject AI code even if it works](https://news.ycombinator.com/item?id=48614631)**

AI can make implementation cheap while making review and judgment more expensive.

⬆️ 186 • 💬 105 • 9h ago • [Vinicius Brasil](https://vinibrasil.com/when-i-reject-ai-code-even-if-it-works/)

---

**[The AI Hate Progression](https://news.ycombinator.com/item?id=48589485)**

I think I've spoken at length in other places about how I am a very staunch AI hater and everything I hate about how the tech is presented t...

⬆️ 123 • 💬 187 • 2d ago • [xodium.net](https://www.xodium.net/2026/06/the-ai-hate-progression.html)

---

**[Companies rein in AI usage as costs strain budgets](https://news.ycombinator.com/item?id=48602571)**

Amazon, Walmart and Uber are among early adopters that have introduced caps or discouraged wasteful activity

⬆️ 120 • 💬 104 • 1d ago • [ft.com](https://www.ft.com/content/1d37cc08-e0aa-45a4-a45d-4ad282529314)

---

**[The 100k Whys of AI](https://news.ycombinator.com/item?id=48616017)**

⬆️ 111 • 💬 62 • 4h ago • [lcamtuf.substack.com](https://lcamtuf.substack.com/p/the-100000-whys-of-ai)

---

---

## YouTube Videos: "ai"

**[Shocking New AI Just Hit 12 Million Tokens With 1000x Less Compute](https://www.youtube.com/watch?v=7jrZ4JqeGyY)**

A shocking new AI breakthrough just hit 12 million tokens with nearly 1000x less attention compute. Subquadratic says its new ...

📺 AI Revolution

👁️ 25K • 👍 871 • 💬 67 • ⏱️ 15:12 • 1d ago

---

**[5 Ways to Make Money From an AI the Government Fears](https://www.youtube.com/watch?v=q_FIJmSB0Ro)**

Get 30 days free on HighLevel only with my link: https://www.gohighlevel.com/TKOPOD ━ Check out my newsletter at ...

📺 Chris Koerner on The Koerner Office Podcast

👁️ 17K • 👍 710 • 💬 51 • ⏱️ 20:40 • 1d ago

---

**[The Claude Shutdown Is a Total Sh*tshow](https://www.youtube.com/watch?v=R4nFEQb7kZo)**

Three words — “fix this code” — were apparently enough to trigger one of the most dramatic AI shutdowns we've seen so far.

📺 House of El - AI

👁️ 366K • 👍 23K • 💬 3K • ⏱️ 22:22 • 2d ago

---

**[How to Lose a Global AI Monopoly in One Afternoon](https://www.youtube.com/watch?v=0RxMj0L0-fY)**

Streamline your entire business with Odoo! The all-in-one, easy-to-use ERP platform that centralizes, automates, and scales your ...

📺 Patrick Boyle

👁️ 602K • 👍 24K • 💬 3K • ⏱️ 30:09 • 23h ago

---

**[AI Does Something Horrifying To Human Thinking](https://www.youtube.com/watch?v=52FiVExXfnU)**

Research shows AI is measurably reducing how hard our brains work - an MIT study found ChatGPT users had the lowest neural ...

📺 House of El - AI

👁️ 91K • 👍 8K • 💬 2K • ⏱️ 21:47 • 20h ago

---

**[The AI Gold Rush Is Here... These 3 Stocks Sell The Shovels](https://www.youtube.com/watch?v=BIZteOgIUK0)**

AI is creating trillion-dollar opportunities... but most investors are looking in the wrong place. Everyone is chasing Nvidia, AI chips, ...

📺 Ross Givens

👁️ 31K • 👍 2K • 💬 256 • ⏱️ 9:51 • 2d ago

---

**[UNCENSORED!! 4 FREE &amp; UNLIMITED AI Video Generators with SEEDANCE 2.0](https://www.youtube.com/watch?v=5_C0OjlglhI)**

These are 4 Free AI Video Generators nobody has seen yet with seedance 2, veo 3 and the top ai models. Since a lot of you ...

📺 Brain Project

👁️ 7K • 👍 409 • 💬 73 • ⏱️ 20:22 • 19h ago

---

**[I Was Right About AI](https://www.youtube.com/watch?v=aXy8mQeuObk)**

In this episode, I follow up on a few of my predictions about AI from my recent video: "How AI Will Fail Like The Music Industry" My ...

📺 Rick Beato

👁️ 1.0M • 👍 55K • 💬 8K • ⏱️ 7:47 • 2d ago

---

**[How to Build AI Agents in 14 minutes Using Claude (for beginners)](https://www.youtube.com/watch?v=3MX7rVeVIYw)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 ...

📺 Mikey Vibe Coding

👁️ 19K • 💬 18 • ⏱️ 30:55 • 2d ago

---

**[Inside Google&#39;s AI data centers](https://www.youtube.com/watch?v=TfW5pWpsHAo)**

"GMA" gets exclusive access inside a Google data center as communities nationwide grapple with the rapid expansion of ...

📺 ABC News

👁️ 37K • 👍 554 • 💬 206 • ⏱️ 5:37 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 358,677 • ❤️ 2,014 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 27,413 • ❤️ 1,735 • 2d ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 104,076 • ❤️ 1,167 • 5d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 20,277 • ❤️ 530 • 1d ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 363,308 • ❤️ 935 • 6d ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 762,861 • ❤️ 1,025 • 10d ago

---

**[FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)**

*Microsoft*

FastContext-1.0-4B-SFT is a lightweight repository-exploration subagent for LLM coding agents, designed to efficiently locate relevant code snippets using parallel read-only tool calls (READ, GLOB, GREP). Its primary use case is to reduce token consumption and context pollution for main coding agents by providing focused file paths and line ranges as evidence, thereby improving end-to-end performance in tasks like software development.

`text-generation` `4.0B`

⬇️ 2,593 • ❤️ 250 • 4d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 241,845 • ❤️ 2,227 • 8d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,966,691 • ❤️ 2,056 • 2mo ago

---

**[GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)**

*Unsloth AI*

GLM-5.2 is a large language model optimized for long-horizon tasks, featuring a 1M token context window and advanced coding capabilities with flexible effort levels. It utilizes an improved architecture with IndexShare for reduced FLOPs and is released under an MIT license for broad accessibility.

`text-generation` `753.9B`

⬇️ 32,260 • ❤️ 213 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 34 • 💬 1 • ⭐ 24,649 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 170 • 💬 6 • ⭐ 4,842 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 101 • 💬 4 • ⭐ 87,720 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 241 • 💬 4 • ⭐ 8,492 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 7 • 💬 1 • ⭐ 8,146 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 20 • 💬 1 • ⭐ 83,139 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 81 • 💬 7 • ⭐ 77,853 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[FastContext: Training Efficient Repository Explorer for Coding Agents](https://huggingface.co/papers/2606.14066)**

*Shaoqiu Zhang, Maoquan Wang, Yuling Shi et al. (8 authors)*

🏢 Microsoft

FastContext separates repository exploration from code solving in LLM agents using specialized exploration models that reduce token consumption and improve resolution rates.

▲ 89 • 💬 3 • ⭐ 704 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14066) • [💻 code](https://github.com/microsoft/fastcontext) • [🔗 project](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 43 • 💬 4 • ⭐ 30,799 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233)**

*Yoav HaCohen, Benny Brazowski, Nisan Chiprut et al. (29 authors)*

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.

▲ 183 • 💬 9 • ⭐ 7,768 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.03233) • [💻 code](https://github.com/Lightricks/LTX-2) • [🔗 project](https://app.ltx.studio/ltx-2-playground/i2v)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 75.3k • 🔱 9.8k • 1d ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 44.5k • 🔱 2.2k • 10h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.1k • 🔱 940 • 5h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.2k • 🔱 477 • 6h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.4k • 🔱 415 • 4d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.2k • 🔱 205 • 4d ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 1.7k • 🔱 155 • 16h ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.7k • 🔱 128 • 1d ago

---

**[code-yeongyu/lazycodex](https://github.com/code-yeongyu/lazycodex)**

The one and only agent harness for complex codebases. Project memory, planning, execution, and verified completion inside Codex.

`TypeScript` `ai` `ai-agents` `claude` `claude-code` `cli`

⭐ 1.7k • 🔱 95 • 1d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.6k • 🔱 145 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*
