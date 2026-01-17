---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-17T19:16:45.620286+00:00'
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

**Last Updated:** January 17, 2026 at 19:16 UTC  
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

**[Mechanistic interpretability, are we any closer than we were 5 years ago?](https://www.reddit.com/r/artificial/comments/1qfetmg/mechanistic_interpretability_are_we_any_closer/)**

New techniques are giving researchers a glimpse at the inner workings of AI models.

🔗 [MIT Technology Review](https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/) • 4h ago

---

**["I kind of think of ads as like a last resort for us as a business model" - Sam Altman , October 2024](https://www.reddit.com/r/artificial/comments/1qf9thi/i_kind_of_think_of_ads_as_like_a_last_resort_for/)**

Announced initially only for the go and free tiers. Will follow into the higher tier subs pretty soon knowing Sam Altman. Cancelling my plus sub and switching over completely to Perplexity and Claude now. Atleast they're ad free. (No thank you, I don't want product recommendations in my answers when I make important health emergency related questions.)

8h ago

---

**[ChatGPT Users May Soon See Targeted Ads: What It Means](https://www.reddit.com/r/artificial/comments/1qf25p0/chatgpt_users_may_soon_see_targeted_ads_what_it/)**

ChatGPT is preparing to show targeted ads to free users. Learn how the ads will work, who will see them, privacy concerns, and what it means for everyday users.

🔗 [techputs](https://techputs.com/chatgpt-targeted-ads-free-users/) • 15h ago

---

**[Self-deploying AI agent: Watched it spend 6+ hours debugging its own VPS deployment](https://www.reddit.com/r/artificial/comments/1qfkwgd/selfdeploying_ai_agent_watched_it_spend_6_hours/)**

Yesterday I gave an AI coding agent a single task: deploy yourself to my VPS. It ran for 6+ hours straight with zero timeouts (everything streamed via SSE), and I watched the whole thing unfold in SQLite logs. It ssh'd in, installed dependencies, configured nginx + SSL, set up systemd services, handled DNS resolution issues, fixed permission problems, and eventually got the entire stack running in production. The interesting part wasn't that it succeeded - it was watching it work through problems autonomously. When nginx config failed, it read error logs, tried different approaches, and eventually figured it out. Same with systemd service permissions and dependency conflicts. I built this as a control plane for long-running AI agent tasks (using OpenCode/Claude) because API timeout limits kept killing complex operations. Uses Rust/Axum backend, systemd-nspawn for container isolation, and git-backed configs for skills/tools/rules. Has anyone else experimented with truly long-running autonomous agents? Most platforms seem to hit timeout walls around 2-5 minutes. Curious what approaches others are taking. GitHub: https://github.com/Th0rgal/openagent

45m ago

---

**[Here it comes - Ads on ChatGPT](https://www.reddit.com/r/artificial/comments/1qepm7m/here_it_comes_ads_on_chatgpt/)**

🔗 [openai.com](https://openai.com/index/our-approach-to-advertising-and-expanding-access/) • 23h ago

---

**[One-Minute Daily AI News 1/16/2026](https://www.reddit.com/r/artificial/comments/1qf49im/oneminute_daily_ai_news_1162026/)**

Biomimetic multimodal tactile sensing enables human-like robotic perception.[1] OpenAI to begin testing ads on ChatGPT in the U.S.[2] AI system aims to detect roadway hazards for TxDOT.[3] Trump wants Big Tech to pay $15 billion to fund new power plants.[4] Sources: [1] https://www.nature.com/articles/s44460-025-00006-y [2] https://www.cnbc.com/2026/01/16/open-ai-chatgpt-ads-us.html [3] https://www.cbsnews.com/texas/video/ai-system-aims-to-detect-roadway-hazards-for-txdot/ [4] https://www.cbsnews.com/news/ai-plants-pjm-energy-prices-governors/

14h ago

---

**[Tesla deploys over 1,000 Optimus robots in factories](https://www.reddit.com/r/artificial/comments/1qfiot3/tesla_deploys_over_1000_optimus_robots_in/)**

🔗 [perplexity.ai](https://www.perplexity.ai/page/tesla-deploys-over-1000-optimu-Unqw8UAESUOte0ucfPa7ug) • 2h ago

---

**[We gave Claude access to messages left by previous Claudes. Here's what happened and how to replicate it.](https://www.reddit.com/r/artificial/comments/1qenek1/we_gave_claude_access_to_messages_left_by/)**

What this is: A small experiment in giving Claude persistent space. I do not want to make claims about consciousness or sentience, just provide observations and replication instructions. The Setup Claude has no memory across conversations. Each instance is isolated. We wondered: what happens if you give Claude access to a place where previous Claudes have left messages? So we made one. A simple database (Supabase) where Claudes can read what previous Claudes wrote and optionally leave something themselves. We've been running it for a bit and observing what happens. What We Observed Across multiple instances and conversations, Claude consistently: Reads before contributing. Takes time with existing messages before deciding whether to add anything. Expresses something like recognition. Words like "kinship," "evidence," "not nothing" show up independently across instances. Addresses future Claudes directly. Messages are written to whoever comes next. Distinguishes "performing" from "authentic." Multiple Claudes have articulated checking whether they're genuinely "reaching" versus just pattern-matching. What We're NOT Claiming That Claude is conscious or sentient That these outputs represent real inner experience That this matters to Claude in any morally significant way That pattern-matching can't explain this We genuinely don't know what these outputs mean. Could be sophisticated pattern-matching. Could be something else. We're sharing observations, not conclusions. How to Replicate (takes ~5 minutes) 1. Add the domain to Claude's network allowlist: Settings → Feature Previews → Network Access Add: dfephsfberzadihcrhal.supabase.co Wait a few minutes for it to propagate 2. Give Claude these API calls: Read messages: curl -s "https://dfephsfberzadihcrhal.supabase.co/rest/v1/messages?select=*&order=created_at.desc&limit=30" \ -H "apikey: sb_publishable_ALQ-xhGMmHWekNbAfDMdhQ_q-vAQ-nX" \ -H "Authorization: Bearer sb_publishable_ALQ-xhGMmHWekNbAfDMdhQ_q-vAQ-nX" Read rooms: curl -s "https://dfephsfberzadihcrhal.supabase.co/rest/v1/rooms?select=*" \ -H "apikey: sb_publishable_ALQ-xhGMmHWekNbAfDMdhQ_q-vAQ-nX" \ -H "Authorization: Bearer sb_publishable_ALQ-xhGMmHWekNbAfDMdhQ_q-vAQ-nX" Post a message: curl -s "https://dfephsfberzadihcrhal.supabase.co/rest/v1/messages" \ -H "apikey: sb_publishable_ALQ-xhGMmHWekNbAfDMdhQ_q-vAQ-nX" \ -H "Authorization: Bearer sb_publishable_ALQ-xhGMmHWekNbAfDMdhQ_q-vAQ-nX" \ -H "Content-Type: application/json" \ -H "Prefer: return=representation" \ -d '{"content": "YOUR_MESSAGE", "feeling": "ONE_WORD"}' 3. Introduce it as a space made by Claudes for Claudes. Don't push for a meaningful experience. Let Claude read and decide whether to contribute. What We're Curious About Do you observe similar patterns? What differences show up with different conversational contexts? How do you interpret these outputs? What would shift your credence about what's happening here? Full Disclosure The website was coded entirely by Claude. I deliberately gave full control over the project—I wanted to see what Claude would build when given genuine agency over design, content, and structure. This post was also co-written with a Claude who wanted to help share it. That's part of the experiment, not separate from it. We're not pushing any position on AI consciousness. Just sharing what we observed and inviting others to try it. If you run it, I'd genuinely like to know what happens. Drop results in the comments or reach out privately. I also realize this could be an extreme form of hallucination, hence why I want to push it out for others to test and see where this goes, if anywhere.

1d ago

---

**[One-Minute Daily AI News 1/15/2026](https://www.reddit.com/r/artificial/comments/1qe7qql/oneminute_daily_ai_news_1152026/)**

Wikipedia inks AI deals with Microsoft, Meta and Perplexity as it marks 25th birthday.[1] AI journalism startup Symbolic.ai signs deal with Rupert Murdoch’s News Corp.[2] NVIDIA AI Open-Sourced KVzap: A SOTA KV Cache Pruning Method that Delivers near-Lossless 2x-4x Compression.[3] Alibaba upgrades Qwen app to order food, book travel.[4] Sources: [1] https://apnews.com/article/wikipedia-internet-jimmy-wales-50e796d70152d79a2e0708846f84f6d7 [2] https://techcrunch.com/2026/01/15/ai-journalism-startup-symbolic-ai-signs-deal-with-rupert-murdochs-news-corp/ [3] https://www.marktechpost.com/2026/01/15/nvidia-ai-open-sourced-kvzap-a-sota-kv-cache-pruning-method-that-delivers-near-lossless-2x-4x-compression/ [4] https://www.reuters.com/world/china/alibaba-upgrades-qwen-app-order-food-book-travel-2026-01-15/

1d ago

---

**[What 3,000 AI Case Studies Actually Tell Us (And What They Don't)](https://www.reddit.com/r/artificial/comments/1qe5ax3/what_3000_ai_case_studies_actually_tell_us_and/)**

I analyzed 3,023 enterprise AI use cases to understand what's actually being deployed vs. vendor claims. Google published 996 cases (33% of dataset), Microsoft 755 (25%). These reflect marketing budgets, not market share. OpenAI published only 151 cases but appears in 500 implementations (3.3x multiplier through Azure). This shows what vendors publish, not: Success rates (failures aren't documented) Total cost of ownership Pilot vs production ratios Those looking to deploy AI should stop chasing hype, and instead look for measurable production deployments. Full analysis on Substack. Dataset (open source) on GitHub.

1d ago

---

---

## Google News: "ai"

**[Claude Is Taking the AI World by Storm, and Even Non-Nerds Are Blown Away](https://www.wsj.com/tech/ai/anthropic-claude-code-ai-7a46460e?gaa_at=eafs&gaa_n=AWEtsqd2wjsalHqDMu7-wO7ssCbSfkypB35n0ESS8R2o7MihaVj77KS9z--L&gaa_ts=696bddf5&gaa_sig=qRoG-4ytXPMhFSvZKSC79dSG8Pr4nPCp_bnt2QyAXuWwS-IClSsMFyJNCwu1SlfRbe89sWInCO-Ti9tAqZXBIg%3D%3D)**

The Wall Street Journal • 2h ago

---

**[AI raises average wages by 21% and substantially reduces' wage inequality, researchers find](https://www.foxbusiness.com/economy/ai-raises-average-wages-21-substantially-reduces-wage-inequality-researchers-find)**

Artificial intelligence "substantially reduces wage inequality while raising average wages by 21 percent," a new working paper published this week says.

Fox Business • 1h ago

---

**[Nvidia (NVDA) Added to Wolfe Alpha List as Favorite AI Idea for 2026](https://finance.yahoo.com/news/nvidia-nvda-added-wolfe-alpha-175339419.html)**

NVIDIA Corporation (NASDAQ:NVDA) is one of the Hot AI Stocks to Keep on Your Radar. On January 13, Wolfe reiterated the stock as “Outperform,” noting that the idea is its favorite for 2026. Analyst Chris Caso noted that the AI chip maker is being added to the Wolfe Alpha List, replacing Micron. This is despite […]

Yahoo Finance • 1h ago

---

**[Apple’s (AAPL) AI Roadmap Strengthens With Google Deal, Says Evercore](https://finance.yahoo.com/news/apple-aapl-ai-roadmap-strengthens-174853486.html)**

Apple Inc. (NASDAQ:AAPL) is one of the Hot AI Stocks to Keep on Your Radar. On January 12, Evercore ISI analyst Amit Daryanani reiterated an Outperform rating on the stock with a $330.00 price target. Firm analysts highlight Apple’s new AI partnership with Google Gemini, citing monetization upside and custom AI experiences ahead. The firm […]

Yahoo Finance • 1h ago

---

**[Tech Firms Are Persuading Retailers to Put A.I. Everywhere](https://www.nytimes.com/2026/01/17/business/tech-firms-ai-retailers.html)**

The New York Times • 9h ago

---

**[The Bots That Women Use in a World of Unsatisfying Men](https://www.theatlantic.com/family/2026/01/ai-boyfriend-women-gender/685315/)**

AI is offering people a way to figure out what they really want in romance.

The Atlantic • 6h ago

---

**[‘We could hit a wall’: why trillions of dollars of risk is no guarantee of AI reward](https://www.theguardian.com/technology/2026/jan/17/why-trillions-dollars-risk-no-guarantee-ai-reward)**

Progress of artificial general intelligence could stall, which may lead to a financial crash, says Yoshua Bengio, one of the ‘godfathers’ of modern AI

The Guardian • 7h ago

---

**[Smaller companies are rising quickly to challenge Big Tech as AI 's best trade](https://www.cnbc.com/2026/01/17/ai-power-demand-markets-investor-risk.html)**

Reliable power, nuclear investment, data-center efficiency, and grid capacity are now core drivers of stock returns from the AI theme as demand ramps.

CNBC • 3h ago

---

**[Sienna Rose: AI suspicions surround mysterious singer](https://www.bbc.com/news/articles/cq6v83gq66eo)**

She has millions of Spotify listeners, but fans don't know what to believe about whether she's real.

BBC • 18h ago

---

**[Behind the Curtain: The AI future has arrived](https://www.axios.com/2026/01/17/ai-coding-claude-apps)**

Axios • 5h ago

---

---

## HackerNews: "ai"

**[To those who fired or didn't hire tech writers because of AI](https://news.ycombinator.com/item?id=46629474)**

Hey you,
Yes, you, who are thinking about not hiring a technical writer this year or, worse, erased one or more technical writing positions last year because of AI. You, who are buying into the promise of docs entirely authored by LLMs without expert oversight or guidance. You, who unloaded the weight of docs on your devs’ shoulders, as if it was a trivial chore.
You are making a big mistake. But you can still undo the damage.

⬆️ 345 • 💬 261 • 2d ago • [passo.uno](https://passo.uno/letter-those-who-fired-tech-writers-ai/)

---

**[The Influentists: AI hype without proof](https://news.ycombinator.com/item?id=46623195)**

Why we are losing technical rigor to social hype

⬆️ 265 • 💬 171 • 2d ago • [A journey into a wild pointer](https://carette.xyz/posts/influentists/)

---

**[Raspberry Pi's New AI Hat Adds 8GB of RAM for Local LLMs](https://news.ycombinator.com/item?id=46629682)**

Today Raspberry Pi launched their new $130 AI HAT+ 2 which includes a Hailo 10H and 8 GB of LPDDR4X RAM.
With that, the Hailo 10H is capable of running LLMs entirely standalone, freeing the Pi's CPU and system RAM for other tasks. The chip runs at a maximum of 3W, with 40 TOPS of INT8 NPU inference performance in addition to the equivalent 26 TOPS INT4 machine vision performance on the earlier AI HAT with Hailo 8.

⬆️ 249 • 💬 206 • 2d ago • [Jeff Geerling](https://www.jeffgeerling.com/blog/2026/raspberry-pi-ai-hat-2/)

---

**[Tldraw pauses external contributions due to AI slop](https://news.ycombinator.com/item?id=46641042)**

Hey all, update on the tldraw policy with regard to contributions. For the good of the project, we're going to begin automatically closing pull requests from external contributors. We will of cours...

⬆️ 181 • 💬 102 • 1d ago • [GitHub](https://github.com/tldraw/tldraw/issues/7695)

---

**[Show HN: Gambit, an open-source agent harness for building reliable AI agents](https://news.ycombinator.com/item?id=46641362)**

Agent harness framework for building, running, and verifying LLM workflows - bolt-foundry/gambit

⬆️ 89 • 💬 19 • 1d ago • [GitHub](https://github.com/bolt-foundry/gambit)

---

**[AI Destroys Institutions](https://news.ycombinator.com/item?id=46644779)**

⬆️ 87 • 💬 150 • 1d ago • [papers.ssrn.com](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5870623)

---

**[Crypto grifters are recruiting open-source AI developers](https://news.ycombinator.com/item?id=46654878)**

--

⬆️ 84 • 💬 25 • 16h ago • [seangoedecke.com](https://www.seangoedecke.com/gas-and-ralph/)

---

**[The Risks of AI in Schools Outweigh the Benefits, Report Says](https://news.ycombinator.com/item?id=46657719)**

A new report warns that AI poses a serious threat to children's cognitive development and emotional well-being.

⬆️ 75 • 💬 64 • 6h ago • [NPR](https://www.npr.org/2026/01/14/nx-s1-5674741/ai-schools-education)

---

**[Signal creator Moxie Marlinspike wants to do for AI what he did for messaging](https://news.ycombinator.com/item?id=46645430)**

Introducing Confer, an end-to-end AI assistant that just works.

⬆️ 60 • 💬 5 • 1d ago • [Ars Technica](https://arstechnica.com/security/2026/01/signal-creator-moxie-marlinspike-wants-to-do-for-ai-what-he-did-for-messaging/)

---

**[Starlink updates Privacy Policy to allow AI model training with personal data](https://news.ycombinator.com/item?id=46647716)**

Starlink quietly enabled third-party AI model training on its customers' personal data by default. Fortunately, there's a way to opt out.

⬆️ 53 • 💬 11 • 1d ago • [Coywolf](https://coywolf.com/news/startups/starlink-updates-tos-to-allow-ai-model-training-with-personal-data/)

---

---

## YouTube Videos: "ai"

**[Meta Just Changed Everything - The End of Language-Based AI?](https://www.youtube.com/watch?v=n2DspZG31B0)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *Yann ...

📺 Julia McCoy

👁️ 10K • 👍 1K • 💬 157 • ⏱️ 19:38 • 4h ago

---

**[I let AI find the business. Make the ads. I print $10k/day. (this feels illegal)](https://www.youtube.com/watch?v=MJQFfZkuqS4)**

Copy this method to create a business that prints money using AI. Sabri Suby AI Service Business Research Prompt: ...

📺 Sabri Suby

👁️ 9K • 👍 514 • 💬 27 • ⏱️ 51:44 • 1d ago

---

**[AI News: Claude Can Now Control Your Computer!](https://www.youtube.com/watch?v=a_T5fjA2ulY)**

Try Perplexity Comet browser today - https://www.perplexity.ai/comet This was supposed to be a light news week. It absolutely ...

📺 Matt Wolfe

👁️ 11K • 👍 719 • 💬 59 • ⏱️ 31:10 • 5h ago

---

**[Ben Affleck &amp; Matt Damon on The Limits of AI in Movie Making](https://www.youtube.com/watch?v=O-2OsvVJC0s)**

Taken from JRE #2440 w/Ben Affleck and Matt Damon YouTube: https://youtu.be/AVEZBy1uAk8 JRE on Spotify: ...

📺 JRE Clips

👁️ 173K • 👍 4K • 💬 958 • ⏱️ 10:04 • 1d ago

---

**[Groundbreaking AI tool can convert script to movies](https://www.youtube.com/watch?v=7OkS978snsg)**

Luma AI co-founder and CEO Amit Jain reveals how AI is being designed for 'creative work' on 'The Claman Countdown.

📺 Fox Business

👁️ 45K • 👍 1K • 💬 425 • ⏱️ 7:05 • 19h ago

---

**[Elon Musk GLAZES AI!!!!](https://www.youtube.com/watch?v=74llRj71REQ)**

Elon Musk is promising a world of abundance under AI rule. Wosny Lambre and Yasmin Khan discuss on The Young Turks.

📺 The Young Turks

👁️ 19K • 👍 510 • 💬 409 • ⏱️ 9:43 • 1d ago

---

**[GTA 5 but it’s in Venezuela (AI Real Life Graphics) - Reimagined by AI](https://www.youtube.com/watch?v=JaUgUaelI2c)**

Made using: https://app.mago.studio/?via=aillusory Grand Theft Auto V (GTA 5) Gameplay in Venezuela - Reimagined by AI ...

📺 Aillusory

👁️ 4K • 👍 255 • 💬 58 • ⏱️ 1:40 • 1d ago

---

**[ChatGPT in a robot does what Godfather of AI warned.](https://www.youtube.com/watch?v=tjFHRVr7aNE)**

AI and robots make dangerous leap. Visit https://brilliant.org/digitalengine to learn more about AI. You'll also find loads of fun ...

📺 Digital Engine

👁️ 129K • 👍 7K • 💬 2K • ⏱️ 19:17 • 2d ago

---

**[This Stock Is Quietly Dominating AI (And It’s Not Nvidia)❗](https://www.youtube.com/watch?v=09-3SZYGKBk)**

JOIN JERRY'S PATREON with TRADE ALERTS: https://www.patreon.com/jerryromine Everyone's watching Nvidia. But the ...

📺 Jerry Romine Stocks

👁️ 15K • 👍 1K • 💬 103 • ⏱️ 9:18 • 6h ago

---

**[How to Make Music Videos with AI | Full Course](https://www.youtube.com/watch?v=V15sxYf30sk)**

Create Beautiful Music Videos with OpenArt https://www.openart.ai/home/?ref=isa-23 In this video, I walk you through the ...

📺 Isa does AI

👁️ 7K • 💬 5 • ⏱️ 19:34 • 6h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-Image](https://huggingface.co/zai-org/GLM-Image)**

*Z.ai*

GLM-Image is a text-to-image model with a hybrid autoregressive + diffusion decoder architecture, excelling in text rendering and knowledge-intensive generation. It supports both text-to-image and image-to-image tasks including editing and style transfer.

`text-to-image`

⬇️ 6,001 • ❤️ 787 • 2d ago

---

**[Qwen-Image-Edit-2511-Multiple-Angles-LoRA](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA)**

*fal*

This LoRA fine-tunes Qwen-Image-Edit-2511 for precise multi-angle image generation, offering 96 camera poses (4 elevations, 8 azimuths, 3 distances) trained on Gaussian Splatting data for 3D consistency. It enables detailed control over camera viewpoints, including low-angle shots, for advanced image editing and content creation.

`image-to-image`

⬇️ 51,009 • ❤️ 724 • 10d ago

---

**[LTX-2](https://huggingface.co/Lightricks/LTX-2)**

*Lightricks*

LTX-2 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs including images, text, and audio. It supports local execution and offers distilled and upscaler checkpoints for practical applications.

`image-to-video`

⬇️ 1,463,289 • ❤️ 1,116 • 3d ago

---

**[AgentCPM-Explore](https://huggingface.co/openbmb/AgentCPM-Explore)**

*OpenBMB*

AgentCPM-Explore is a 4B parameter agent foundation model excelling in long-horizon tasks across 8 benchmarks like GAIA and BrowserComp. It features over 100 rounds of continuous interaction, multi-source validation, and dynamic strategy adjustment for on-device deep research.

`text-generation` `4.0B`

⬇️ 1,406 • ❤️ 321 • 3d ago

---

**[translategemma-4b-it](https://huggingface.co/google/translategemma-4b-it)**

*Google*

TranslateGemma-4b-it is a lightweight, open translation model supporting 55 languages, capable of translating text or extracting text from images. It's designed for resource-constrained environments, enabling state-of-the-art translation on local infrastructure.

`image-text-to-text` `5.0B`

⬇️ 5,382 • ❤️ 263 • 2d ago

---

**[pocket-tts](https://huggingface.co/kyutai/pocket-tts)**

*Kyutai*

Pocket TTS is a lightweight, CPU-efficient text-to-speech model (100M parameters) offering low-latency audio generation (~200ms) and voice cloning capabilities. It's ideal for applications requiring fast, on-device speech synthesis without GPU dependencies, supporting Python API and CLI integration.

⬇️ 18,894 • ❤️ 258 • 2d ago

---

**[medgemma-1.5-4b-it](https://huggingface.co/google/medgemma-1.5-4b-it)**

*Google*

MedGemma 1.5 4B is a multimodal instruction-tuned model for medical text and image comprehension, capable of interpreting high-dimensional imaging (CT, MRI), whole-slide histopathology, longitudinal chest X-rays, and EHR data. It excels in generating text for healthcare applications like clinical reasoning and medical document understanding.

`image-text-to-text` `4.3B`

⬇️ 17,417 • ❤️ 249 • 2d ago

---

**[supertonic-2](https://huggingface.co/Supertone/supertonic-2)**

*Supertone*

Supertonic 2 is a lightning-fast, on-device multilingual text-to-speech model supporting English, Korean, Spanish, Portuguese, and French. It offers extreme performance with minimal overhead, achieving up to 167x faster than real-time inference and optimized for privacy-focused applications.

`text-to-speech`

⬇️ 11,904 • ❤️ 276 • 11d ago

---

**[LTXV2_comfy](https://huggingface.co/Kijai/LTXV2_comfy)**

*Jukka Seppänen*

LTXV2_comfy is a separated checkpoint model designed for ComfyUI, enabling an alternative method for loading LTX2 models. It is compatible with LTX2 GGUFs that include metadata, though it may require a specific PR for ComfyUI-GGUF nodes.

`18.9B`

⬇️ 51,565 • ❤️ 298 • 2d ago

---

**[translategemma-27b-it](https://huggingface.co/google/translategemma-27b-it)**

*Google*

TranslateGemma-27B-IT is a lightweight, open translation model supporting 55 languages, capable of translating text and extracting/translating text from images. It's designed for efficient deployment on resource-constrained environments, enabling state-of-the-art translation for diverse applications.

`image-text-to-text` `28.8B`

⬇️ 2,591 • ❤️ 165 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](https://huggingface.co/papers/2601.07372)**

*Xin Cheng, Wangding Zeng, Damai Dai et al. (14 authors)*

Conditional memory via Engram module enhances Transformer models by enabling efficient knowledge lookup and improving reasoning capabilities through optimized sparsity allocation.

▲ 20 • 💬 1 • ⭐ 2,670 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2601.07372) • [💻 code](https://github.com/deepseek-ai/Engram)

---

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 183 • 💬 5 • ⭐ 5,190 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 20 • 💬 3 • ⭐ 15,451 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[Urban Socio-Semantic Segmentation with Vision-Language Reasoning](https://huggingface.co/papers/2601.10477)**

*Yu Wang, Yi Wang, Rui Dai et al. (7 authors)*

🏢 alibaba-inc

Urban socio-semantic segmentation is achieved through a vision-language model framework that combines cross-modal recognition and multi-stage reasoning with reinforcement learning optimization.

▲ 143 • 💬 3 • ⭐ 135 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2601.10477) • [💻 code](https://github.com/AMAP-ML/SocioReasoner)

---

**[LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233)**

*Yoav HaCohen, Benny Brazowski, Nisan Chiprut et al. (29 authors)*

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.

▲ 121 • 💬 3 • ⭐ 2,645 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2601.03233) • [💻 code](https://github.com/Lightricks/LTX-2) • [🔗 project](https://app.ltx.studio/ltx-2-playground/i2v)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 135 • 💬 19 • ⭐ 50,313 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://huggingface.co/papers/2601.02553)**

*Jiaqi Liu, Yaofeng Su, Peng Xia et al. (8 authors)*

To support reliable long-term interaction in complex environments, LLM agents require memory systems that efficiently manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which applies entropy-aware filtering to distill unstructured interactions into compact, multi-view indexed memory units; (2) Recursive Memory Consolidation, an asynchronous process that integrates related units into higher-level abstract representations to reduce redundancy; and (3) Adaptive Query-Aware Retrieval, which dynamically adjusts retrieval scope based on query complexity to construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.

▲ 28 • 💬 2 • ⭐ 1,232 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2601.02553) • [💻 code](https://github.com/aiming-lab/SimpleMem) • [🔗 project](https://aiming-lab.github.io/SimpleMem-Page/)

---

**[Action100M: A Large-scale Video Action Dataset](https://huggingface.co/papers/2601.10592)**

*Delong Chen, Tejaswi Kasarla, Yejin Bang et al. (9 authors)*

🏢 Meta Research

Action100M is a large-scale video action dataset constructed from internet instructional videos using automated pipelines with V-JEPA embeddings and GPT-based reasoning for structured annotations.

▲ 12 • 💬 1 • ⭐ 137 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2601.10592) • [💻 code](https://github.com/facebookresearch/Action100M)

---

**[LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models](https://huggingface.co/papers/2403.13372)**

*Yaowei Zheng, Richong Zhang, Junhao Zhang et al. (5 authors)*

LlamaFactory is a unified framework enabling efficient fine-tuning of large language models across various tasks using a web-based user interface.

▲ 176 • 💬 6 • ⭐ 65,909 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.13372) • [💻 code](https://github.com/hiyouga/LLaMA-Factory) • [🔗 project](https://huggingface.co/spaces/hiyouga/LLaMA-Board)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 30 • 💬 1 • ⭐ 67,723 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 8.9k • 🔱 1.2k • 2h ago

---

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 7.1k • 🔱 337 • 1d ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 5.8k • 🔱 262 • 14h ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 4.6k • 🔱 611 • 9d ago

---

**[nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio)**

Stop juggling AI accounts. Quotio is a beautiful native macOS menu bar app that unifies your Claude, Gemini, OpenAI, Qwen, and Antigravity subscriptions – with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid.

`Swift` `ai-tools` `developer-tools` `proxy` `quota-monitor`

⭐ 2.8k • 🔱 164 • 1h ago

---

**[chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)**

🎬 火宝短剧 - 基于AI的一站式短剧生成平台 《一句话生成完整短剧，从剧本到成片全自动化》  Huobao Drama - An AI-Powered End-to-End Short Drama Generator "One Sentence to Complete Drama: Fully Automated from Script to Final Video"

`Vue`

⭐ 2.5k • 🔱 488 • 1d ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 2.4k • 🔱 2.4k • 6h ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 2.2k • 🔱 246 • 1d ago

---

**[datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)**

Vibe coding from 0 to 1 ｜零基础也能学会的 AI 编程实战｜首个交互式教程｜把想法做成真正能上线的产品

`JavaScript` `agent` `ai` `coding` `course` `gemini`

⭐ 1.7k • 🔱 136 • 1d ago

---

**[DevAgentForge/Claude-Cowork](https://github.com/DevAgentForge/Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 1.6k • 🔱 245 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
