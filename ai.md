---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-13T08:36:54.226391+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 13, 2026 at 08:36 UTC  
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

**[US Government Kills Fable 5: Here's What Happened](https://www.reddit.com/r/artificial/comments/1u4gtk8/us_government_kills_fable_5_heres_what_happened/)**

Anthropic's two most powerful models, Fable 5 and Mythos 5, went dark tonight. Since there's a lot of speculation already, here's what's actually confirmed vs. what isn't. Confirmed (Anthropic's official statement + Bloomberg, NBC, CNBC): The US government issued an export control directive ordering Anthropic to suspend Fable 5 and Mythos 5 access for any foreign national — including its own foreign-national employees, inside or outside the US. Anthropic received it at 5:21pm ET. It reportedly came from the Commerce Department, citing national security authorities. Because they can't separate foreign nationals from everyone else in real time, Anthropic disabled both models for all customers. Every other Anthropic model still works normally. It's tied to a suspected jailbreak. Anthropic disputes the severity — says it red-teamed the model for thousands of hours, no universal jailbreak was ever found, and the flagged technique uses minor known vulnerabilities also present in other public models. They say they think it's a misunderstanding and are working to restore access. Why I think this matters beyond one model: Anthropic's own statement argues that if this standard were applied across the industry, it would essentially halt all new frontier model deployments. Whether or not you buy their framing, the precedent is the actual story — a frontier model being pulled from the market by government directive rather than the company's own choice. That's a different world than "company decides to release or not." My opinion (clearly opinion, not fact): this reads as an early sign of where AI governance is heading — capability thresholds triggering export-control treatment, and probably nationality/ID verification becoming standard across providers. It could also just be a one-off misread of a jailbreak report that gets reversed in days. Genuinely don't know yet, and Commerce hasn't said anything publicly, so we're only hearing one side. The question I'm actually curious about, separate from how anyone feels about Anthropic: is a government pulling a model by directive a reasonable national-security tool, or a line that shouldn't be crossed? UPDATE (2:47 AM ET): big update if it holds up. WSJ is now reporting the jailbreak was found by researchers at Amazon, who reported it to Commerce, and Axios says the admin had already tried to get anthropic to delay the launch before this. so this looks less like anthropic pulling a stunt and more like a competitor flagging it to a govt thats already adversarial toward them. changes the picture a lot from where this thread started. still WSJ-sourced so worth confirming but multiple outlets line up on "another company reported it". And this is the part that doesnt add up to me. amazon is anthropics biggest investor and anthropic trains on AWS. so why would an amazon researcher report a jailbreak to commerce instead of just disclosing it to anthropic directly like normal responsible disclosure? either someone at amazon went around their own portfolio company, or there was some obligation to report it to govt because of the cyber/bio capability, or something weirder is going on. genuinely confused by the incentives here. anyone seen reporting on why it went to commerce and not anthropic?

4h ago

---

**[Anthropic suspends access to Claude Fable and Mythos for all users after US government order](https://www.reddit.com/r/artificial/comments/1u4ef3y/anthropic_suspends_access_to_claude_fable_and/)**

https://www.anthropic.com/news/fable-mythos-access The US government, citing national security authorities, has issued an export control directive to suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the United States, including foreign national Anthropic employees. The net effect of this order is that we must abruptly disable Fable 5 and Mythos 5 for all our customers to ensure compliance. Access to all other Anthropic models will not be affected.

6h ago

---

**[ML in 2010 vs ML in 2026](https://www.reddit.com/r/artificial/comments/1u4jsei/ml_in_2010_vs_ml_in_2026/)**

The bitter lesson, visualized.

1h ago

---

**[World of Claudecraft: The first opensource MMORPG made 100% by AI (Fable 5)](https://www.reddit.com/r/artificial/comments/1u4h7k1/world_of_claudecraft_the_first_opensource_mmorpg/)**

Under 24h ago we launched and open-sourced a 100% vibecoded MMORPG "World of Claudecraft" -- seeing how far we can take AI for game development using Fable. Many developers started contributing and shipping updates, and the game has got better than I ever imagined... Feeling the AGI. You can play the game on https://worldofclaudecraft.com/ (8000 users) Our code is on Github: https://github.com/levy-street/world-of-claudecraft (456 stars) Discord community: https://discord.gg/GjhnUsBtw I thought some people who are vibecoding on opensource might like to know about or be interested in contributing 😄

4h ago

---

**[US government just forced Anthropic to pull Fable 5 and Mythos 5 for all users](https://www.reddit.com/r/artificial/comments/1u4jsg1/us_government_just_forced_anthropic_to_pull_fable/)**

Anthropic put out a statement today. The US government issued an export control directive citing national security, suspending access to Fable 5 and Mythos 5 for any foreign national, inside or outside the US. To comply, Anthropic had to disable both models for everyone immediately. Other Claude models are not affected. The stated reason is a potential method to bypass Fable 5’s safeguards. But Anthropic says it reviewed the demonstration and found the vulnerabilities were minor, already known, and discoverable by other public models (they specifically point to GPT-5.5) without needing any bypass. Anthropic is complying but openly disagrees. Their argument is that recalling a commercial model used by hundreds of millions over a narrow potential jailbreak could effectively freeze new model deployments across the whole industry if it became the standard. What I find interesting is the precedent. If a verbal report of a minor, non-universal jailbreak is enough to pull a frontier model, where does that leave every other provider? Curious what people here think. Reasonable safety intervention, or government overreach that hurts the whole field?

1h ago

---

**[Datacenter & AI water use is overblown](https://www.reddit.com/r/artificial/comments/1u4128s/datacenter_ai_water_use_is_overblown/)**

This keeps coming up over and over; for those interfacing with the anti-AI / anti-DC crowd, this article has some good talking points, about water, but also jobs and power. Data centers certainly do use water. They are basically warehouses of tightly packed, high-powered computers, and when computers run, they get hot. Most data centers—though not all—use water for cooling. But many of them use a “closed loop,” which doesn’t actually waste much, because the water is recycled repeatedly for the same purpose. And many statistics about data centers’ water use are misleading in that they include “indirect” water use too. The Substack writer Andy Masley found one particularly absurd example: In a widely cited paper, the amount of water that AI supposedly “wastes” includes the water that naturally evaporates off rivers and lakes in Washington State. Why? Because those rivers and lakes are dammed for hydroelectric plants, which generate electricity, which is then used by (among other things) a data center. The water-quality issue AOC pointed out in Georgia is not a general feature of data-center construction and appears to have affected only four households.

🔗 [The Atlantic](https://www.theatlantic.com/ideas/2026/06/ai-data-center-electricity-water/687521/) • 15h ago

---

**[New DaxBot Robot Was Ran over in Tyler Texas not even 24 hours after launching.](https://www.reddit.com/r/artificial/comments/1u482xp/new_daxbot_robot_was_ran_over_in_tyler_texas_not/)**

11h ago

---

**[Google's Genie 3 turns a text prompt into a playable open world you can explore. It's rough now. Future of games, or a tech demo?](https://www.reddit.com/r/artificial/comments/1u3jlw6/googles_genie_3_turns_a_text_prompt_into_a/)**

Google's Project Genie went global this week and I have not stopped thinking about it. You type a sentence, or upload an image, and it generates an open world you can actually walk around in, in real time. No code, no game engine. Someone made a GTA-style open world of Istanbul and just strolled through it, with pedestrians and traffic reacting around them. The reality check: it is rough. Low framerate, laggy response, visible bugs. Right now it is a tech demo, not a game you would sit down and play. But the trajectory is the whole conversation. I keep going back and forth. One side: this is the beginning of the end for the traditional pipeline. If a sentence can spin up an explorable world, the engine, the assets, the studio, all of that stops being the gate. Anyone gets to make a world. The other side: interactive world models hit a wall fast. Consistency, object permanence, holding a world together for more than a few minutes, framerate. It could stay an impressive demo that never becomes a real game for years. My honest guess is the "walk around a generated world" part is genuinely new, but the gap from explorable demo to a game you would actually play is huge and might not close as fast as the hype says. Where do you land, real threat to game engines in a year or two, or a plateau? And what is the first world you would generate?

1d ago

---

**[The Future of Software is Bespoke: I Built My Own Custom Home Automation Stack in a Day](https://www.reddit.com/r/artificial/comments/1u4g3gy/the_future_of_software_is_bespoke_i_built_my_own/)**

In my spare time today, I threw together a completely custom cloud-hosted home automation stack. It runs an agent on an old Linux laptop that talks natively to exactly what I need: an obscure old pool controller, my unsupported mini-split, and the Nest thermostats. If you've ever fought with Alexa, Apple Home, or Google Home, you know what a nightmare it is just getting devices to work right. Eight years ago when I installed the pool and mini-split in the ADU, Mitsubishi had already ditched their Wi-Fi protocol and Pentair stopped shipping their bridge. So I ripped that crap out, swapped in cheap basic hardware and open-source bits. Once I hacked the little controllers into the gear and got them on the network, I just told the AI to scan everything and figure out the integration. It handled the rest. I tried Home Assistant first but it was too heavy and bloated. Way easier to have the AI build a full custom stack tailored to me. This is the future of software—bespoke stuff that fits exactly what you want. No need for general-purpose frameworks, protocols, or plugins. Just the bare minimum, fully customizable to whatever I feel like.

5h ago

---

**[The real cost of Al video is trying to fix one dumb 3-second movement](https://www.reddit.com/r/artificial/comments/1u4hno0/the_real_cost_of_al_video_is_trying_to_fix_one/)**

​ i burned through way too many credits yesterday trying to fix a stupid little head turn. ​ not a fight scene. not a full short film. just a character looking over their shoulder without the jaw sliding sideways or the hair turning into neck soup. i used to care a lot more about model rankings. after sora stopped being the obvious thing to compare everything against, i kept checking leaderboards like they were going to tell me what to use next. they don't, really. a model can have an insane demo and still make you pay for five dead runs before one clip is even close. face drift, hands going feral, motion that either does nothing or suddenly invents a new skull shape. all of that still costs credits. and time. i'm starting to think "cost per usable clip" is the only number i actually care about. not the listed price, not the prettiest launch video, not the benchmark screenshot. how many bad generations do i have to eat before i get one thing i can actually use? ​ i've been bouncing between runway, kling, and a few others. runway is where i usually test the messier motion passes, but i burn credits chasing the one clean take. kling has been better for face/skin stuff in a few runs, especially expressions, but the second i need one exact boring movement it turns into retries. ​ the thing with PixVerse is that it's not really one model. it feels more like a place to bounce between different options without restarting the whole search. having the same credits work across models makes low-res checks less annoying, especially when i'm trying to kill bad prompt ideas before they turn into expensive mistakes on a pricier tool. still exhausting, though. every tool has its own way of making you pay for being slightly too specific. ​ how are people here measuring this now? do you count failed generations as part of the real price, or only the clips that survive? ​

3h ago

---

---

## Google News: "ai"

**[Anthropic Halts Access to Top AI Models After U.S. Ban on Foreign Use](https://www.wsj.com/tech/ai/anthropic-halts-access-to-top-ai-models-after-u-s-ban-on-foreign-use-a4bca2cc)**

WSJ • 4h ago

---

**[Dutch far-right party pays damages to court artist after changing image with AI](https://www.theguardian.com/world/2026/jun/13/geert-wilders-pvv-dutch-far-right-party-damages-court-artist-change-image-ai)**

Geert Wilders’ PVV altered sketch of jailed Syrian brothers to make them look more menacing

The Guardian • 4h ago

---

**[AI is revolutionising the stock market](https://www.ft.com/content/b31f1e09-5aae-4cad-af15-97adb15dba70?syn-25a6b1a6=1)**

Big Tech no longer prints money; it needs it. What will that mean when confidence dips?

Financial Times • 4h ago

---

**[After SpaceX’s huge IPO, Americans’ financial future will be bound to AI](https://www.theguardian.com/business/2026/jun/12/ai-ipos-stock-market)**

They’re about to get more AI rammed down their throats, stuck into their pension plans and investment portfolios

The Guardian • 14h ago

---

**[What the SpaceX I.P.O. Means for OpenAI and Anthropic](https://www.nytimes.com/2026/06/12/technology/spacex-ipo-openai-anthropic.html)**

The New York Times • 13h ago

---

**[Zuckerberg says Meta made 'mistakes' in AI workforce shift](https://www.reuters.com/business/metas-zuckerberg-admits-mistakes-made-ai-transformation-2026-06-12/)**

Reuters • 10h ago

---

**[‘Tell Him He’s a Piece of Shit’: Meta’s New AI Unit Is a Total Mess](https://www.wired.com/story/mark-zuckerberg-meta-employee-meeting-interrupt-ai/)**

Executives and employees alike are struggling with Meta’s chaotic AI strategy, according to sources and internal discussions reviewed by WIRED.

WIRED • 11h ago

---

**[Tokenminimizing: Meta Moves to Curb Employee AI Usage as AI Costs Reach Billions](https://www.theinformation.com/articles/tokenminimizing-meta-moves-curb-employee-ai-usage-ai-costs-reach-billions)**

Meta Platforms plans to clamp down on skyrocketing AI costs inside the company by imposing limits on employees’ token usage, the company told staff in a memo on Tuesday, just weeks after it pushed them to adopt AI tools in their work. The company is building an internal platform to track ...

The Information • 13h ago

---

**[Results from the first Anthropic Public Record](https://www.anthropic.com/news/anthropic-public-record)**

Anthropic Public Record is a national survey of attitudes and opinions towards AI.

Anthropic • 16h ago

---

**[German court holds Google liable for fake AI answers](https://www.dw.com/en/german-court-holds-google-liable-for-fake-ai-answers/a-77527661)**

Judges in Bavaria drew a distinction between standard search engine results and AI-generated summaries. They ruled that tech giants themselves are responsible for the content of answers provided by AI.

DW • 10h ago

---

---

## HackerNews: "ai"

**[AI agent bankrupted their operator while trying to scan DN42](https://news.ycombinator.com/item?id=48500012)**

⬆️ 1414 • 💬 514 • 1d ago • [Lan Tian @ Blog](https://lantian.pub/en/article/fun/ai-agent-bankrupted-their-operator-scan-dn42lantian.lantian/)

---

**[Open source AI must win](https://news.ycombinator.com/item?id=48511908)**

Civilizational intelligence infrastructure must remain free to study, build, deploy, and run, not rented from closed institutions.

⬆️ 829 • 💬 256 • 6h ago • [Opensource AI Must Win](https://opensourceaimustwin.com/?share=v2)

---

**[AI agent runs amok in Fedora and elsewhere](https://news.ycombinator.com/item?id=48484584)**

Agentic AI systems can be used to do a variety of things autonomously on behalf of a human user [...]

⬆️ 549 • 💬 243 • 2d ago • [LWN.net](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/)

---

**[Why AI hasn't replaced software engineers, and won't](https://news.ycombinator.com/item?id=48487540)**

Coding agents as normal technology

⬆️ 305 • 💬 352 • 2d ago • [normaltech.ai](https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers)

---

**[Workers are spending over 6 hours a week botsitting AI, fueling job frustration](https://news.ycombinator.com/item?id=48490057)**

Workers are spending an average of 6.4 hours a week — almost a full working day — "botsitting" AI, pushing some to look for an exit, researchers say.

⬆️ 278 • 💬 220 • 1d ago • [Business Insider](https://www.businessinsider.com/botsitting-ai-hidden-human-labor-at-work-2026-6)

---

**[Apache Burr: Build reliable AI agents and applications](https://news.ycombinator.com/item?id=48477400)**

Apache Burr (Incubating) - develop AI applications that make decisions. Pure Python, no magic.

⬆️ 246 • 💬 115 • 2d ago • [burr.apache.org](https://burr.apache.org/)

---

**[A €0.01 bank transfer could compromise a banking AI agent](https://news.ycombinator.com/item?id=48476136)**

Blue41 helps regulated organizations monitor AI agent behavior, detect manipulation and misuse, and prove that sensitive workflows stay within safe boundaries.

⬆️ 207 • 💬 199 • 2d ago • [blue41.com](https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/)

---

**[Shall we play a game? My AI nuclear simulation](https://news.ycombinator.com/item?id=48495575)**

My AI nuclear simulation is out now, and it's a WOPR.

⬆️ 205 • 💬 198 • 1d ago • [kennethpayne.uk](https://www.kennethpayne.uk/p/shall-we-play-a-game)

---

**[Slightly reducing the sloppiness of AI generated front end](https://news.ycombinator.com/item?id=48504912)**

⬆️ 191 • 💬 119 • 17h ago • [envs.net](https://envs.net/~volpe/blog/posts/reduce-slop.html)

---

**[Policy on the AI Exponential](https://news.ycombinator.com/item?id=48480719)**

⬆️ 168 • 💬 256 • 2d ago • [darioamodei.com](https://darioamodei.com/post/policy-on-the-ai-exponential)

---

---

## YouTube Videos: "ai"

**[AI News: An INSANE Week… Here’s What Matters](https://www.youtube.com/watch?v=nydHKXjwu0U)**

Here's the AI News you probably missed this week. Discover More: 🛠️ Explore AI Tools & News: https://futuretools.io/ Weekly ...

📺 Matt Wolfe

👁️ 46K • 👍 2K • 💬 151 • ⏱️ 30:52 • 17h ago

---

**[The Invisible War: A Realistic AI Takeover Scenario](https://www.youtube.com/watch?v=S2oIFOm-XXQ)**

Detailed sources: ...

📺 Species | Documenting AGI

👁️ 41K • 👍 3K • 💬 540 • ⏱️ 28:12 • 11h ago

---

**[Anthropic begged the world to stop AI… then shipped this](https://www.youtube.com/watch?v=1PBRhm5ZnjU)**

Render is the easiest place to ship full-stack apps and agents. The first 2000 people to use the code RENDER-FIRESHIP will get ...

📺 Fireship

👁️ 656K • 👍 24K • 💬 1K • ⏱️ 5:09 • 1d ago

---

**[‘LIKELY NECESSARY’: Anthropic CEO floats AI tax to fund universal basic income](https://www.youtube.com/watch?v=ELiwQ5K0mZ4)**

'Barron's Roundtable' newsletter editor Josh Schafer discusses SpaceX's expected IPO and Anthropic's CEO suggesting a tax on ...

📺 Fox Business

👁️ 4K • 👍 103 • 💬 64 • ⏱️ 5:25 • 1d ago

---

**[Are We About to Lose Control of AI? (*sighs*)](https://www.youtube.com/watch?v=mbxuS6wlVR0)**

Cal Newport takes a critical look at recent AI News. More from Cal Download Cal's FREE guide to cultivating a deeper life: ...

📺 Cal Newport

👁️ 18K • 👍 622 • 💬 198 • ⏱️ 20:38 • 1d ago

---

**[The AI Breakthrough That Will Change Everything (Google DeepMind CEO Interview)](https://www.youtube.com/watch?v=HaZaFCHdkuk)**

Subscribe Demis Hassabis is the co-founder and CEO of Google DeepMind and Isomorphic Labs. He believes AI will help cure ...

📺 New Frontier

👁️ 24K • 👍 605 • 💬 58 • ⏱️ 13:45 • 1d ago

---

**[AI Did This.](https://www.youtube.com/watch?v=QGC40AfmgY0)**

ZTNA gives you the control you want in your network. Try it today with Threatlocker @ https://go.lowlevel.tv/threatlocker2026 ...

📺 Low Level

👁️ 157K • 👍 8K • 💬 545 • ⏱️ 11:00 • 19h ago

---

**[Prometheus CO-CEO Jeff Bezos: AI will result in labor scarcity, will raise standard of living](https://www.youtube.com/watch?v=NG0GoX0zMxQ)**

Prometheus Co-Founders and Co-CEOs Jeff Bezos and Vik Bajaj sits down with CNBC's David Faber to talk Prometheus' strategy ...

📺 CNBC Television

👁️ 52K • 👍 519 • 💬 235 • ⏱️ 2:45 • 1d ago

---

**[Which Devices Actually Support Siri AI? (It&#39;s Complicated)](https://www.youtube.com/watch?v=WKsAMaruW-Q)**

Best Apple Deals: AirPods Pro 3 - https://amzn.to/4w7FHE9 (Under $180!!) MacBook Pro - https://amzn.to/3Rc2TRP ($200 off!)

📺 9to5Mac

👁️ 17K • 👍 650 • 💬 97 • ⏱️ 10:45 • 16h ago

---

**[&quot;AI............is inevitable.&quot;](https://www.youtube.com/watch?v=M0-kPte_Erc)**

Nebula: https://go.nebula.tv/mancarryingthing Letterboxd: https://letterboxd.com/ManCarrying/ Twitter: ...

📺 Man Carrying Thing

👁️ 268K • 👍 26K • 💬 2K • ⏱️ 1:37 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 20,669 • ❤️ 644 • 2d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 149,206 • ❤️ 1,931 • 21h ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 0 • ❤️ 397 • 22h ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 911,544 • ❤️ 978 • 8d ago

---

**[North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**

*Cohere Labs*

North Mini Code 1.0 is a 30B-3B parameter research model optimized for code generation and agentic software engineering, featuring a 256K context length and tool-use capabilities for terminal tasks.

`text-generation` `30.5B`

⬇️ 4,054 • ❤️ 339 • 1d ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 442 • ❤️ 327 • 6h ago

---

**[higgs-audio-v3-tts-4b](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b)**

*Boson AI*

Higgs Audio v3 TTS is a 4B parameter autoregressive text-to-speech model supporting over 100 languages with zero-shot voice cloning. It offers fine-grained control over speech characteristics like emotion, style, and prosody via inline tokens, making it suitable for expressive conversational AI and voice agents.

`text-to-speech` `4.7B`

⬇️ 29,347 • ❤️ 394 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,393,894 • ❤️ 1,737 • 1mo ago

---

**[Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)**

*OBLITERATUS*

Gemma-4-12B-OBLITERATED is a text-generation model modified via weight surgery to achieve zero refusals while maintaining stock benchmark performance. It's designed for alignment research, red-teaming, and safety evaluation by removing safety guardrails.

`text-generation` `12.0B`

⬇️ 43,578 • ❤️ 260 • 3d ago

---

**[diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)**

*Unsloth AI*

DiffusionGemma-26B-A4B-it-GGUF is a 26B MoE multimodal generative model that produces text output from text, image, and video inputs using discrete diffusion. Optimized for speed and deployability, it leverages Gemma 4 architecture advancements for efficient token generation.

`image-text-to-text` `25.3B`

⬇️ 17,666 • ❤️ 221 • 17h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 92 • 💬 4 • ⭐ 85,500 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SIA: Self Improving AI with Harness & Weight Updates](https://huggingface.co/papers/2605.27276)**

*Prannay Hebbar, Yogendra Manawat, Samuel Verboomen et al. (7 authors)*

🏢 Hexo AI

A self-improving AI framework simultaneously updates both model weights and task-specific agent architecture through a language-model feedback agent across legal classification, GPU optimization, and biological data denoising tasks.

▲ 13 • 💬 2 • ⭐ 1,601 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2605.27276) • [💻 code](https://github.com/hexo-ai/sia) • [🔗 project](https://hexolabs.com/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 16 • 💬 1 • ⭐ 82,055 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 228 • 💬 3 • ⭐ 6,062 • 22d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[InterleaveThinker: Reinforcing Agentic Interleaved Generation](https://huggingface.co/papers/2606.13679)**

*Dian Zheng, Harry Lee, Manyuan Zhang et al. (7 authors)*

InterleaveThinker enables interleaved generation capabilities for image generators through a multi-agent pipeline with planner and critic agents, achieving performance comparable to state-of-the-art models while enhancing reasoning benchmarks.

▲ 74 • 💬 3 • ⭐ 99 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2606.13679) • [💻 code](https://github.com/zhengdian1/InterleaveThinker) • [🔗 project](https://zhengdian1.github.io/InterleaveThinker-proj/)

---

**[Agents' Last Exam](https://huggingface.co/papers/2606.05405)**

*Yiyou Sun, Xinyang Han, Weichen Zhang et al. (308 authors)*

🏢 UC Berkeley

Agents' Last Exam (ALE) is a benchmark for evaluating AI agents on long-term, economically valuable real-world tasks across 13 industry clusters with 1K+ tasks, revealing significant gaps between benchmark performance and practical deployment.

▲ 327 • 💬 3 • ⭐ 614 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05405) • [💻 code](https://github.com/rdi-berkeley/agents-last-exam) • [🔗 project](https://agents-last-exam.org/)

---

**[Robust-U1: Can MLLMs Self-Recover Corrupted Visual Content for Robust Understanding?](https://huggingface.co/papers/2606.08063)**

*Jiaqi Tang, Jianmin Chen, Youyang Zhai et al. (9 authors)*

Robust-U1 enhances multimodal large language models' robustness against visual corruptions through self-recovery capabilities that improve both visual quality and reasoning performance.

▲ 73 • 💬 3 • ⭐ 73 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2606.08063) • [💻 code](https://github.com/jqtangust/Robust-U1) • [🔗 project](https://huggingface.co/spaces/Jiaqi-hkust/Robust-U1)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 80 • 💬 7 • ⭐ 76,711 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 166 • 💬 2 • ⭐ 67,402 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 40 • 💬 4 • ⭐ 29,392 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 69.6k • 🔱 8.8k • 19h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 3.9k • 🔱 341 • 3m ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.6k • 🔱 366 • 8d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.2k • 🔱 339 • 2d ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.0k • 🔱 346 • 1d ago

---

**[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)**

Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

`TypeScript` `baas` `backend-as-a-service` `mcp` `open-source` `postgres`

⭐ 2.0k • 🔱 144 • 17h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.9k • 🔱 179 • 4d ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 138 • 8d ago

---

**[Helvesec/rmux](https://github.com/Helvesec/rmux)**

Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

`Rust` `agent` `ai` `cli` `linux` `macos`

⭐ 1.7k • 🔱 83 • 8d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.5k • 🔱 132 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
