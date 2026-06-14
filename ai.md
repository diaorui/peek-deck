---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-14T06:41:58.486743+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 14, 2026 at 06:41 UTC  
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

**[Microsoft president says AI backlash at graduation events should be wake-up call for the tech industry](https://www.reddit.com/r/artificial/comments/1u50mve/microsoft_president_says_ai_backlash_at/)**

Microsoft president and vice chairman Brad Smith recently shared his – definitely informed – opinion about the growing backlash against AI. Smith thinks that other leaders in...

🔗 [TechSpot](https://www.techspot.com/news/112751-microsoft-president-ai-backlash-graduation-events-wake-up.html) • 10h ago

---

**[US Government Kills Fable 5: Here's What Happened](https://www.reddit.com/r/artificial/comments/1u4gtk8/us_government_kills_fable_5_heres_what_happened/)**

Anthropic's two most powerful models, Fable 5 and Mythos 5, went dark tonight. Since there's a lot of speculation already, here's what's actually confirmed vs. what isn't. Confirmed (Anthropic's official statement + Bloomberg, NBC, CNBC): The US government issued an export control directive ordering Anthropic to suspend Fable 5 and Mythos 5 access for any foreign national — including its own foreign-national employees, inside or outside the US. Anthropic received it at 5:21pm ET. It reportedly came from the Commerce Department, citing national security authorities. Because they can't separate foreign nationals from everyone else in real time, Anthropic disabled both models for all customers. Every other Anthropic model still works normally. It's tied to a suspected jailbreak. Anthropic disputes the severity — says it red-teamed the model for thousands of hours, no universal jailbreak was ever found, and the flagged technique uses minor known vulnerabilities also present in other public models. They say they think it's a misunderstanding and are working to restore access. Why I think this matters beyond one model: Anthropic's own statement argues that if this standard were applied across the industry, it would essentially halt all new frontier model deployments. Whether or not you buy their framing, the precedent is the actual story — a frontier model being pulled from the market by government directive rather than the company's own choice. That's a different world than "company decides to release or not." My opinion (clearly opinion, not fact): this reads as an early sign of where AI governance is heading — capability thresholds triggering export-control treatment, and probably nationality/ID verification becoming standard across providers. It could also just be a one-off misread of a jailbreak report that gets reversed in days. Genuinely don't know yet, and Commerce hasn't said anything publicly, so we're only hearing one side. The question I'm actually curious about, separate from how anyone feels about Anthropic: is a government pulling a model by directive a reasonable national-security tool, or a line that shouldn't be crossed? UPDATE (2:47 AM ET): big update if it holds up. WSJ is now reporting the jailbreak was found by researchers at Amazon, who reported it to Commerce, and Axios says the admin had already tried to get anthropic to delay the launch before this. so this looks less like anthropic pulling a stunt and more like a competitor flagging it to a govt thats already adversarial toward them. changes the picture a lot from where this thread started. still WSJ-sourced so worth confirming but multiple outlets line up on "another company reported it". And this is the part that doesnt add up to me. amazon is anthropics biggest investor and anthropic trains on AWS. so why would an amazon researcher report a jailbreak to commerce instead of just disclosing it to anthropic directly like normal responsible disclosure? either someone at amazon went around their own portfolio company, or there was some obligation to report it to govt because of the cyber/bio capability, or something weirder is going on. genuinely confused by the incentives here. anyone seen reporting on why it went to commerce and not anthropic? UPDATE (June 13 7:15 PM ET): still suspended, no resolution. roughly 24+ hours in now. a few confirmed additions: - Commerce STILL hasn't made any public statement. NBC says they "did not immediately reply to a request for comment." so a full day later the govt's actual rationale is still not on the record, we're entirely on anthropic + reporting. - one detail that firms up the directive: NBC reports the letter came from Commerce Sec Lutnick to Dario Amodei and was "written with the help of officials from" other agencies, so this wasn't one guy acting alone, it was coordinated. - anthropic promised more technical detail "within 24 hours of the order" but as of now hasn't published an appeal process, a mitigation checklist, or a timeline. that silence is the actual story right now, it suggests this isn't a quick fix on their end, it's a negotiation with Commerce over what counts as acceptable safeguards. - IPO angle for the watchers: this landed ~11 days after anthropic confidentially filed. reporting says pre-IPO shares dipped and regulatory risk is now part of the listing story. bottom line: treat fable/mythos as down indefinitely, no date. most likely path per the reporting is a quiet return in days-to-weeks gated behind extra safeguards or a vetting layer. will update if commerce finally says something or access comes back.

1d ago

---

**[Can an AI agent complete a task and still fail?](https://www.reddit.com/r/artificial/comments/1u58qwi/can_an_ai_agent_complete_a_task_and_still_fail/)**

A lot of AI-agent discussions focus on whether the agent completed the task. But I think there is a missing category: the agent may complete the task, but do it in an unsafe or policy-violating way. For example, an agent could finish the job but use the wrong tool, skip an approval step, expose private information, or take an action that should have been blocked. In our ACM CAIS 2026 paper, we call this the Verifier Tax. The idea is to separate: safe success unsafe success failure We studied this in tool-using LLM agent scenarios using τ-bench and proposed a two-tier verification architecture: deterministic checks first, then an LLM-based verifier for more contextual cases. The main takeaway: verification can make agents safer by reducing unsafe success, but it may also reduce task completion as tasks get longer. Paper: https://dl.acm.org/doi/full/10.1145/3786335.3813160 Curious what people think: if an AI agent completes a task but violates a safety rule, should that count as success or failure?

4h ago

---

**[Anthropic suspends access to Claude Fable and Mythos for all users after US government order](https://www.reddit.com/r/artificial/comments/1u4ef3y/anthropic_suspends_access_to_claude_fable_and/)**

https://www.anthropic.com/news/fable-mythos-access The US government, citing national security authorities, has issued an export control directive to suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the United States, including foreign national Anthropic employees. The net effect of this order is that we must abruptly disable Fable 5 and Mythos 5 for all our customers to ensure compliance. Access to all other Anthropic models will not be affected.

1d ago

---

**[What would actually make you trust an AI? Not "it sounds right," but trust it the way you trust a person or an institution?](https://www.reddit.com/r/artificial/comments/1u5cxn6/what_would_actually_make_you_trust_an_ai_not_it/)**

We're starting to lean on AI for real decisions, but two things are odd about it: it can be completely confident and completely wrong, and most assistants forget everything between conversations so there's no track record, no "self" that's accountable for what it told you last week. So I'm genuinely curious how people here think about this: what would have to be true about an AI system before you'd trust it the way you trust a doctor, a newspaper, or a bank? Is it transparency (you can check its sources)? A verifiable track record? Some kind of persistent identity and accountability? Or is "trust" just the wrong frame for a tool? Not looking for "never trust AI". I'm interested in the specific conditions that would move the needle for you.

50m ago

---

**[ML in 2010 vs ML in 2026](https://www.reddit.com/r/artificial/comments/1u4jsei/ml_in_2010_vs_ml_in_2026/)**

The bitter lesson, visualized.

23h ago

---

**[World of Claudecraft: The first opensource MMORPG made 100% by AI (Fable 5)](https://www.reddit.com/r/artificial/comments/1u4h7k1/world_of_claudecraft_the_first_opensource_mmorpg/)**

Under 24h ago we launched and open-sourced a 100% vibecoded MMORPG "World of Claudecraft" -- seeing how far we can take AI for game development using Fable. Many developers started contributing and shipping updates, and the game has got better than I ever imagined... Feeling the AGI. You can play the game on https://worldofclaudecraft.com/ (8000 users) Our code is on Github: https://github.com/levy-street/world-of-claudecraft (456 stars) Discord community: https://discord.gg/GjhnUsBtw I thought some people who are vibecoding on opensource might like to know about or be interested in contributing 😄

1d ago

---

**[Found this interesting resource on Data Centers in the US. Shows tax incentives on the map too. Fairly neutral on positioning. Does anyone know what Beaumont and Sheridan is?](https://www.reddit.com/r/artificial/comments/1u51wqm/found_this_interesting_resource_on_data_centers/)**

I came across this website when I was trying to figure out how real the complaints to data center opposition are. Has anyone seen this site before? I can't figure out what it is. Looks kind of like a legal site, but I don't think it is. https://beaumontandsheridan.com/resources/data-centers-the-internets-body/

9h ago

---

**[I just got an error as I was about to send a message to the ChatGPT client that says "You can send up to -4 files. Remove 4 to continue". What should I do? (repost from r/ChatGPT)](https://www.reddit.com/r/artificial/comments/1u54507/i_just_got_an_error_as_i_was_about_to_send_a/)**

Is this also a sign that I should stop using ChatGPT?

8h ago

---

**[We are all inside different machines.](https://www.reddit.com/r/artificial/comments/1u510q3/we_are_all_inside_different_machines/)**

We talk about AI as if it is a single thing. One system, one trajectory, one set of values to interrogate or reform. It is not, and it is becoming less so.

🔗 [jackmaguire.org](https://jackmaguire.org/blog/we-are-all-inside-different-machines/) • 10h ago

---

---

## Google News: "ai"

**[Anthropic to disable its most advanced AI models after US order limiting foreign access](https://www.theguardian.com/technology/2026/jun/13/anthropic-disable-advanced-ai-models-us-government-order)**

Company said US government believes safeguards can be bypassed and product used to identify software vulnerabilities

The Guardian • 18h ago

---

**[The Job That AI Was Supposed to Kill Needs More Humans Than Ever](https://www.wsj.com/tech/ai/the-job-that-ai-was-supposed-to-kill-needs-more-humans-than-ever-0771e4cf)**

WSJ • 18h ago

---

**[Opinion | How to Kick SpaceX Out of Your 401(k)](https://www.nytimes.com/2026/06/13/opinion/spacex-stock-ipo-ai.html)**

The New York Times • 19h ago

---

**[Russian families use AI to 'resurrect' loved ones killed in Ukraine](https://www.bbc.com/news/articles/cwy24v72n19o)**

The highly controversial trend lies at the intersection of Russia's war on Ukraine, new AI technologies and grief.

BBC • 7h ago

---

**[Inside the whirlwind 24 hours that led the White House to slap export controls on Anthropic](https://www.politico.com/news/2026/06/13/inside-the-whirlwind-24-hours-that-led-the-white-house-to-slap-export-controls-on-anthropic-00961519)**

Politico • 7h ago

---

**[Apple’s big Siri update is here. Now the real challenge begins](https://www.cnn.com/2026/06/13/tech/apple-siri-ai-update)**

Siri is finally getting the big AI upgrade Wall Street has been waiting for. But it’s just the beginning.

CNN • 20h ago

---

**[Introducing Omnigent: A Meta-Harness to Combine, Control and Share Your Agents](https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents)**

Omnigent is a new open source meta-harness that sits above coding tools like Claude Code, Codex, and custom agents, so you can compose, govern, and share AI agents from one place.

Databricks • 15h ago

---

**[New OpenAI Academy courses for the next era of work](https://openai.com/index/academy-courses-applying-ai-at-work/)**

OpenAI introduces three Academy courses that help people build practical AI skills, create repeatable workflows, and apply agents in everyday work.

OpenAI • 1d ago

---

**[Global Capitalism Bets It All on AI Future That Alarms Voters](https://www.bloomberg.com/news/articles/2026-06-13/global-capitalism-bets-it-all-on-ai-future-that-alarms-voters)**

Bloomberg.com • 13h ago

---

**[Bentonville photographer accused of using AI to create CSAM released from jail Friday](https://www.nwahomepage.com/knwa/bentonville-photographer-accused-of-using-ai-to-create-csam-released-from-jail-friday/)**

The Bentonville photographer accused of generating child sexual abuse materials (CSAM) using artificial intelligence appeared before a judge Friday morning and was released on a $350,000 bond.

KNWA FOX24 • 8h ago

---

---

## HackerNews: "ai"

**[Open source AI must win](https://news.ycombinator.com/item?id=48511908)**

Civilizational intelligence infrastructure must remain free to study, build, deploy, and run, not rented from closed institutions.

⬆️ 1532 • 💬 466 • 1d ago • [Opensource AI Must Win](https://opensourceaimustwin.com/?share=v2)

---

**[AI agent bankrupted their operator while trying to scan DN42](https://news.ycombinator.com/item?id=48500012)**

⬆️ 1446 • 💬 525 • 2d ago • [Lan Tian @ Blog](https://lantian.pub/en/article/fun/ai-agent-bankrupted-their-operator-scan-dn42lantian.lantian/)

---

**[Why AI hasn't replaced software engineers, and won't](https://news.ycombinator.com/item?id=48487540)**

Coding agents as normal technology

⬆️ 309 • 💬 356 • 2d ago • [normaltech.ai](https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers)

---

**[Police officer investigated for using AI to 'create evidence' in multiple cases](https://news.ycombinator.com/item?id=48520807)**

⬆️ 298 • 💬 140 • 10h ago • [news.sky.com](https://news.sky.com/story/derbyshire-police-officer-investigated-for-using-ai-to-create-evidence-in-multiple-cases-13553661)

---

**[Workers are spending over 6 hours a week botsitting AI, fueling job frustration](https://news.ycombinator.com/item?id=48490057)**

Workers are spending an average of 6.4 hours a week — almost a full working day — "botsitting" AI, pushing some to look for an exit, researchers say.

⬆️ 278 • 💬 220 • 2d ago • [Business Insider](https://www.businessinsider.com/botsitting-ai-hidden-human-labor-at-work-2026-6)

---

**[AI coding at home without going broke](https://news.ycombinator.com/item?id=48518969)**

There are three ways to do AI coding at home without spending like a company, and which one fits depends mostly on how much you trust the next year of hardwa...

⬆️ 275 • 💬 233 • 13h ago • [stephen.bochinski.dev](https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/)

---

**[AI OSS tool repo goes archived over night after raising $7.3M Seed](https://news.ycombinator.com/item?id=48516504)**

TensorZero is an open-source LLMOps platform that unifies an LLM gateway, observability, evaluation, optimization, and experimentation. - tensorzero/tensorzero

⬆️ 254 • 💬 163 • 18h ago • [GitHub](https://github.com/tensorzero/tensorzero)

---

**[Slightly reducing the sloppiness of AI generated front end](https://news.ycombinator.com/item?id=48504912)**

⬆️ 218 • 💬 130 • 1d ago • [envs.net](https://envs.net/~volpe/blog/posts/reduce-slop.html)

---

**[Shall we play a game? My AI nuclear simulation](https://news.ycombinator.com/item?id=48495575)**

My AI nuclear simulation is out now, and it's a WOPR.

⬆️ 205 • 💬 201 • 2d ago • [kennethpayne.uk](https://www.kennethpayne.uk/p/shall-we-play-a-game)

---

**[A jacket that harvests drinking water from the air](https://news.ycombinator.com/item?id=48497576)**

The advance in fabric technology comes alongside a new benchmark for atmospheric water harvesting.

⬆️ 159 • 💬 99 • 2d ago • [UT Austin News - The University of Texas at Austin](https://news.utexas.edu/2026/06/11/this-jacket-pulls-drinking-water-from-thin-air/)

---

---

## YouTube Videos: "ai"

**[The Big Short Guy Just Bet Everything Against AI](https://www.youtube.com/watch?v=2B7EhGIk0L4)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *Michael Burry the investor who called the ...

📺 Julia McCoy

👁️ 19K • 👍 994 • 💬 180 • ⏱️ 9:43 • 15h ago

---

**[AI Expert Issues DIRE WARNING You Have To See To Believe](https://www.youtube.com/watch?v=CR7UNbZag7U)**

Support The Show On Patreon!: https://www.patreon.com/seculartalk Subscribe to Krystal Kyle & Friends On Substack!

📺 Secular Talk

👁️ 115K • 👍 7K • 💬 1K • ⏱️ 18:21 • 1d ago

---

**[Anthropic&#39;s Fable Backlash, Nationalizing AI, Inflation Heats Up &amp; California’s Broken Elections](https://www.youtube.com/watch?v=gH4FTjDm9FQ)**

(0:00) Besties are back! (0:19) Anthropic gets massive backlash over secret Fable nerfing and privacy concerns (29:16) The AI ...

📺 All-In Podcast

👁️ 221K • 👍 6K • 💬 965 • ⏱️ 1:42:00 • 1d ago

---

**[The Invisible War: A Realistic AI Takeover Scenario](https://www.youtube.com/watch?v=S2oIFOm-XXQ)**

Detailed sources: ...

📺 Species | Documenting AGI

👁️ 83K • 👍 5K • 💬 901 • ⏱️ 28:12 • 1d ago

---

**[Google’s New AI Just Broke The AI Speed Limit: DiffusionGemma](https://www.youtube.com/watch?v=YiIrnYalHS4)**

Google just revealed DiffusionGemma, a new open AI model that generates text in a totally different way and can run up to four ...

📺 AI Revolution

👁️ 18K • 👍 617 • 💬 54 • ⏱️ 14:57 • 1d ago

---

**[Latest Claude AI models suspended after orders from Trump administration • FRANCE 24 English](https://www.youtube.com/watch?v=MDaZ31jx2vQ)**

Anthropic says it's suspended access to its latest AI models, in order to comply with a US national security order. Just three days ...

📺 FRANCE 24 English

👁️ 127K • 👍 1K • 💬 411 • ⏱️ 1:32 • 19h ago

---

**[Anthropic begged the world to stop AI… then shipped this](https://www.youtube.com/watch?v=1PBRhm5ZnjU)**

Render is the easiest place to ship full-stack apps and agents. The first 2000 people to use the code RENDER-FIRESHIP will get ...

📺 Fireship

👁️ 716K • 👍 25K • 💬 1K • ⏱️ 5:09 • 2d ago

---

**[AI News: An INSANE Week… Here’s What Matters](https://www.youtube.com/watch?v=nydHKXjwu0U)**

Here's the AI News you probably missed this week. Discover More: 🛠️ Explore AI Tools & News: https://futuretools.io/ Weekly ...

📺 Matt Wolfe

👁️ 66K • 👍 2K • 💬 185 • ⏱️ 30:52 • 1d ago

---

**[This Is Bad... They Just Shut Down FABLE 5](https://www.youtube.com/watch?v=1e4D6ukN0QY)**

Anthropic's Fable 5 was live for only three days before everything changed. The US government stepped in, access to Fable 5 and ...

📺 AI Revolution

👁️ 10K • 👍 466 • 💬 123 • ⏱️ 12:49 • 7h ago

---

**[&quot;AI............is inevitable.&quot;](https://www.youtube.com/watch?v=M0-kPte_Erc)**

Nebula: https://go.nebula.tv/mancarryingthing Letterboxd: https://letterboxd.com/ManCarrying/ Twitter: ...

📺 Man Carrying Thing

👁️ 295K • 👍 28K • 💬 2K • ⏱️ 1:37 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 92,080 • ❤️ 728 • 3d ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 1,689 • ❤️ 540 • 1d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 69,443 • ❤️ 1,969 • 1d ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 1,031 • ❤️ 431 • 1d ago

---

**[North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**

*Cohere Labs*

North Mini Code 1.0 is a 30B-3B parameter research model optimized for code generation and agentic software engineering, featuring a 256K context length and tool-use capabilities for terminal tasks.

`text-generation` `30.5B`

⬇️ 6,533 • ❤️ 359 • 2d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 1,005,883 • ❤️ 996 • 9d ago

---

**[diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)**

*Unsloth AI*

DiffusionGemma-26B-A4B-it-GGUF is a 26B MoE multimodal generative model that produces text output from text, image, and video inputs using discrete diffusion. Optimized for speed and deployability, it leverages Gemma 4 architecture advancements for efficient token generation.

`image-text-to-text` `25.3B`

⬇️ 42,885 • ❤️ 250 • 1d ago

---

**[higgs-audio-v3-tts-4b](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b)**

*Boson AI*

Higgs Audio v3 TTS is a 4B parameter autoregressive text-to-speech model supporting over 100 languages with zero-shot voice cloning. It offers fine-grained control over speech characteristics like emotion, style, and prosody via inline tokens, making it suitable for expressive conversational AI and voice agents.

`text-to-speech` `4.7B`

⬇️ 32,162 • ❤️ 416 • 5h ago

---

**[Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)**

*OBLITERATUS*

Gemma-4-12B-OBLITERATED is a text-generation model modified via weight surgery to achieve zero refusals while maintaining stock benchmark performance. It's designed for alignment research, red-teaming, and safety evaluation by removing safety guardrails.

`text-generation` `12.0B`

⬇️ 50,289 • ❤️ 282 • 4d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,411,202 • ❤️ 1,768 • 1mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 94 • 💬 4 • ⭐ 85,865 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 80 • 💬 7 • ⭐ 76,932 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 228 • 💬 3 • ⭐ 6,166 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[SIA: Self Improving AI with Harness & Weight Updates](https://huggingface.co/papers/2605.27276)**

*Prannay Hebbar, Yogendra Manawat, Samuel Verboomen et al. (7 authors)*

🏢 Hexo AI

A self-improving AI framework simultaneously updates both model weights and task-specific agent architecture through a language-model feedback agent across legal classification, GPU optimization, and biological data denoising tasks.

▲ 14 • 💬 2 • ⭐ 1,663 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2605.27276) • [💻 code](https://github.com/hexo-ai/sia) • [🔗 project](https://hexolabs.com/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 40 • 💬 4 • ⭐ 29,610 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 16 • 💬 1 • ⭐ 82,123 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference](https://huggingface.co/papers/2510.09665)**

*Yuhan Liu, Yihua Cheng, Jiayi Yao et al. (11 authors)*

LMCACHE enables efficient KV cache management for large language models by storing caches outside GPU memory, supporting cache reuse across queries and inference engines while achieving significant throughput improvements.

▲ 5 • 💬 0 • ⭐ 8,960 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.09665) • [💻 code](https://github.com/LMCache/LMCache)

---

**[InterleaveThinker: Reinforcing Agentic Interleaved Generation](https://huggingface.co/papers/2606.13679)**

*Dian Zheng, Harry Lee, Manyuan Zhang et al. (7 authors)*

InterleaveThinker enables interleaved generation capabilities for image generators through a multi-agent pipeline with planner and critic agents, achieving performance comparable to state-of-the-art models while enhancing reasoning benchmarks.

▲ 75 • 💬 3 • ⭐ 117 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.13679) • [💻 code](https://github.com/zhengdian1/InterleaveThinker) • [🔗 project](https://zhengdian1.github.io/InterleaveThinker-proj/)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 119 • 💬 1 • ⭐ 10,155 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 166 • 💬 2 • ⭐ 67,461 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 70.3k • 🔱 8.9k • 13h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 4.1k • 🔱 355 • 13h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.6k • 🔱 370 • 8d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.3k • 🔱 344 • 3d ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.0k • 🔱 363 • 2d ago

---

**[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)**

Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

`TypeScript` `baas` `backend-as-a-service` `mcp` `open-source` `postgres`

⭐ 2.1k • 🔱 145 • 7h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.0k • 🔱 182 • 5d ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 138 • 9d ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 1.8k • 🔱 81 • 18h ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.5k • 🔱 135 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*
