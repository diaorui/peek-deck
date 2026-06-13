---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-13T20:01:56.957137+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 13, 2026 at 20:01 UTC  
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

15h ago

---

**[Anthropic suspends access to Claude Fable and Mythos for all users after US government order](https://www.reddit.com/r/artificial/comments/1u4ef3y/anthropic_suspends_access_to_claude_fable_and/)**

https://www.anthropic.com/news/fable-mythos-access The US government, citing national security authorities, has issued an export control directive to suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the United States, including foreign national Anthropic employees. The net effect of this order is that we must abruptly disable Fable 5 and Mythos 5 for all our customers to ensure compliance. Access to all other Anthropic models will not be affected.

17h ago

---

**[ML in 2010 vs ML in 2026](https://www.reddit.com/r/artificial/comments/1u4jsei/ml_in_2010_vs_ml_in_2026/)**

The bitter lesson, visualized.

13h ago

---

**[World of Claudecraft: The first opensource MMORPG made 100% by AI (Fable 5)](https://www.reddit.com/r/artificial/comments/1u4h7k1/world_of_claudecraft_the_first_opensource_mmorpg/)**

Under 24h ago we launched and open-sourced a 100% vibecoded MMORPG "World of Claudecraft" -- seeing how far we can take AI for game development using Fable. Many developers started contributing and shipping updates, and the game has got better than I ever imagined... Feeling the AGI. You can play the game on https://worldofclaudecraft.com/ (8000 users) Our code is on Github: https://github.com/levy-street/world-of-claudecraft (456 stars) Discord community: https://discord.gg/GjhnUsBtw I thought some people who are vibecoding on opensource might like to know about or be interested in contributing 😄

15h ago

---

**[Am I the only one exclusively using Opus 4.8 on MAX after trying Fable 5 on MAX for three days?](https://www.reddit.com/r/artificial/comments/1u4yop0/am_i_the_only_one_exclusively_using_opus_48_on/)**

I used to be a firm believer in “use sonnet for most tasks, use opus for complex tasks.” My opinion on that was immediately flipped to “more compute saves time” after my first 10 minutes using fable 5 MAX. Why on earth would I want to possibly mess up a feature that slips my memory instead of using the most compute available to me to make each feature implemented fool proof? I’d also like to add that opus 4.8 on MAX feels like using haiku when compared to fable 5 on MAX. That absolutely isn’t cope, the difference is insane for software engineering.

1h ago

---

**[Does Commerce have the authority to apply export control for hosted AI model access?](https://www.reddit.com/r/artificial/comments/1u4yjdi/does_commerce_have_the_authority_to_apply_export/)**

U.S. export law already covers some software/data releases of controlled technology, so “nothing physical shipped” is not the objection. The open question is whether remote access to a hosted frontier model can count as a controlled export. That has not been the usual SaaS/cloud interpretation. The software stays on the provider’s servers and the user sends inputs and receives outputs. BIS guidance has generally treated cloud use differently from shipping software to a foreign user. Congress has been trying to close that gap through the Remote Access Security Act, which passed the House in January. RASA would give Commerce clearer authority over remote access to EAR-controlled items. Commerce now appears to be acting as if some version of that authority is already available. If that reading holds, the control point shifts. It is no longer just model weights, chips, or source code. It is access to a hosted system’s capability, gated by nationality or whatever verification regime the provider can build. Am I reading the RASA / SaaS export-control gap correctly here? Curious how export-control, cloud, or folks see it.

1h ago

---

**[what's the highest-stakes decision you've actually trusted AI to help you make?](https://www.reddit.com/r/artificial/comments/1u4zz8s/whats_the_higheststakes_decision_youve_actually/)**

not the "write my email" stuff, i mean a real one. a job offer, a breakup, whether to move, whether to start the thing. i've been using AI for actual decisions lately and i keep going back and forth on whether it's genuinely helping me think or just giving me a confident version of what i already wanted to hear. and before you judge me for using artificial intelligence to make very human decisions please understand i use it as an added useful perspective rather than a final decisive conclusion. the thing that's helped me most is asking more than one model and watching where they disagree, because the disagreement usually lands on the part i was avoiding. curious where everyone else draws the line. what's the biggest decision you've let it into, and did it actually help or just make you feel better about a call you'd already made (bonus points for an outcome as well!)

27m ago

---

**[Claude fable 5](https://www.reddit.com/r/artificial/comments/1u4zgnr/claude_fable_5/)**

Hey everyone..I hope you all are doing fine..so basically I am a tech nerd and building a start up on a unique SaaS idea using multiple AI workflows..now basically i heard about Claude launched fable 5 just a day ago and I was curious how powerful it is ? And also in terms of coding how powerful it Is ? I usually use Claude opus 4.6 and sonnet 4.6 for coding...and for which specified fields/jobs/tasks is it good for ?

48m ago

---

**[How will the mythos 5/fable 5 ban work moving forward?](https://www.reddit.com/r/artificial/comments/1u4r0vb/how_will_the_mythos_5fable_5_ban_work_moving/)**

Assuming they keep in place the rule in its current form, how would it even work? Obviously being physically present in the US is not the same as being a US citizen, so any kind of geographical restriction will not work. Will there be some sort of super strict account verification process? But then what if a US citizen lets their non-citizen friend use their account? Would that be a crime?

6h ago

---

**[Dude where's my rug?](https://www.reddit.com/r/artificial/comments/1u4lawv/dude_wheres_my_rug/)**

You may have noticed.. Fable 5 just got switched off for all non-US nationals on a government order. This makes me realise how fragile building on frontier models can be. The most capable available model is easy to start treating as a foundation, something to plan and build on. It is not. It is a convenience that happened to be available, until it was not. I got lucky on timing. I had not yet leaned on the frontier tier for anything foundational, so when it vanished, everything I had running kept running. But that was luck, not foresight. If a big piece of architecture had landed on my desk the week Fable launched, I almost certainly would have built it on the best model I could reach, because why would you not. The trap has nothing to do with carelessness. The frontier is genuinely the best tool in the room, so reaching for it on the important work is the natural move. Timing was the only thing that saved me from making exactly that choice. The capability of a frontier model is real. The access to it is conditional. Those are not the same thing, and this is a clean demonstration of the gap. The model did not get withdrawn because it was unsafe or because of anything Anthropic chose. Although their marketing Mythos as "too dangerous" certainly would not have helped their case. The outcome either way is it got withdrawn because a government drew a line, and the line was nationality, not capability or risk. If a model can be taken away from me specifically, because of where I was born, by a government I have no relationship with and no vote in, then it cannot be load-bearing in anything I build. For experiments, fine. For a pipeline that has to keep running, no. This is not a hypothetical. The top tier is gone from my account as I write this, with no clear date for its return, and there is nothing I or Anthropic can do about it. So the rule I now work by is simple. Nothing I depend on sits on a model that a single government can take away from me. When a frontier model is available, it is a turbo button for one-off work: a hard design exploration, a gnarly refactor, a research pass I want done well in one shot. It produces an artifact, and then everything downstream of that artifact runs on a lower tier that is not under the same restriction and is more than good enough for almost all of it. The frontier accelerates when I can reach it. It never holds weight, because some weeks I cannot reach it at all. The deeper version of this is local. Models I can run on my own machine, offline, that no directive can reach. They are weaker than the frontier. They do not need to be strong. They need to be mine. Anything in my stack that genuinely cannot go down is the thing I most want running locally, precisely because local is the only tier with no off switch held by someone else. This is what doing business with the US has become. What used to be a reliable partner for most of the world is turning into a fickle and unreliable liability. This is not new, and today's events only underscore it once more. A directive can land at 5pm and rewrite who is allowed to use a tool by the next morning, with no process you can see and no recourse you can take. That is not a foundation any builder outside the country can plan on. Which is also why I would not be surprised, or sorry, to see frontier labs look elsewhere. Europe would almost certainly welcome a lab like Anthropic. It would probably mean more work before each release, more process, more scrutiny up front. But it would also mean no rug pulls of this kind. Slower and predictable beats fast and revocable when you are the one building on top. None of this is anti-frontier. These models are extraordinary and I will use them again the moment I can, for what they are good at. It is a point about architecture, and about timing. If you are outside the US, access to the top tier is now a political variable, not a technical one, and it can flip to zero overnight. Whether you get burned by that is partly luck, depending on what you happened to build on it and when. Take luck out of it. Build the parts that have to survive on what you can actually keep, and let the frontier sprint on the days it is there. So I am curious how the rest of you are handling this. If you build outside the US, do you treat frontier access as something you can rely on, or have you already moved your foundations to models nobody can switch off on you? And where is your line between the two?

11h ago

---

---

## Google News: "ai"

**[U.S. Bars Foreigners From Using Anthropic’s Most Advanced A.I. Models](https://www.nytimes.com/2026/06/12/technology/anthropic-mythos-fable5-blocked.html)**

The New York Times • 16h ago

---

**[Zuckerberg says Meta made 'mistakes' in AI workforce shift](https://www.reuters.com/business/metas-zuckerberg-admits-mistakes-made-ai-transformation-2026-06-12/)**

Reuters • 21h ago

---

**[‘Tell Him He’s a Piece of Shit’: Meta’s New AI Unit Is a Total Mess](https://www.wired.com/story/mark-zuckerberg-meta-employee-meeting-interrupt-ai/)**

Executives and employees alike are struggling with Meta’s chaotic AI strategy, according to sources and internal discussions reviewed by WIRED.

WIRED • 22h ago

---

**[Mark Zuckerberg admits Meta has 'made mistakes' as AI overhaul reshapes 20% of its workforce: report](https://www.foxbusiness.com/technology/mark-zuckerberg-admits-meta-made-mistakes-ai-overhaul-reshapes-workforce)**

Mark Zuckerberg admits Meta has 'made mistakes' during its AI-driven workforce overhaul that is expected to ultimately affect about 20% of employees.

Fox Business • 17h ago

---

**[Apple’s big Siri update is here. Now the real challenge begins](https://www.cnn.com/2026/06/13/tech/apple-siri-ai-update)**

Siri is finally getting the big AI upgrade Wall Street has been waiting for. But it’s just the beginning.

CNN • 9h ago

---

**[AI oversight gap could leave a lasting legacy](https://www.axios.com/2026/06/13/ai-oversight-federal-states-courts)**

Axios • 3h ago

---

**[AI is revolutionising the stock market](https://www.ft.com/content/b31f1e09-5aae-4cad-af15-97adb15dba70?syn-25a6b1a6=1)**

Big Tech no longer prints money; it needs it. What will that mean when confidence dips?

Financial Times • 16h ago

---

**[My Top 5 Artificial Intelligence (AI) Stocks to Buy Right Now](https://www.fool.com/investing/2026/06/12/my-top-5-artificial-intelligence-ai-stocks-to-buy/)**

There are several strong AI stock picks available right now.

The Motley Fool • 22h ago

---

**[AI is disrupting investment](https://www.ft.com/content/b9273a66-f05d-4b28-bf34-be8ab93b89d1?syn-25a6b1a6=1)**

The technology is leading to a fundamental shift in the way investors allocate funds and diversify risks across every asset class

Financial Times • 15h ago

---

**[Dutch far-right party pays damages to court artist after changing image with AI](https://www.theguardian.com/world/2026/jun/13/geert-wilders-pvv-dutch-far-right-party-damages-court-artist-change-image-ai)**

Geert Wilders’ PVV altered sketch of jailed Syrian brothers to make them look more menacing

The Guardian • 16h ago

---

---

## HackerNews: "ai"

**[Open source AI must win](https://news.ycombinator.com/item?id=48511908)**

Civilizational intelligence infrastructure must remain free to study, build, deploy, and run, not rented from closed institutions.

⬆️ 1466 • 💬 457 • 17h ago • [Opensource AI Must Win](https://opensourceaimustwin.com/?share=v2)

---

**[AI agent bankrupted their operator while trying to scan DN42](https://news.ycombinator.com/item?id=48500012)**

⬆️ 1433 • 💬 523 • 1d ago • [Lan Tian @ Blog](https://lantian.pub/en/article/fun/ai-agent-bankrupted-their-operator-scan-dn42lantian.lantian/)

---

**[AI agent runs amok in Fedora and elsewhere](https://news.ycombinator.com/item?id=48484584)**

Agentic AI systems can be used to do a variety of things autonomously on behalf of a human user [...]

⬆️ 549 • 💬 244 • 2d ago • [LWN.net](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/)

---

**[Why AI hasn't replaced software engineers, and won't](https://news.ycombinator.com/item?id=48487540)**

Coding agents as normal technology

⬆️ 307 • 💬 356 • 2d ago • [normaltech.ai](https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers)

---

**[Workers are spending over 6 hours a week botsitting AI, fueling job frustration](https://news.ycombinator.com/item?id=48490057)**

Workers are spending an average of 6.4 hours a week — almost a full working day — "botsitting" AI, pushing some to look for an exit, researchers say.

⬆️ 278 • 💬 220 • 2d ago • [Business Insider](https://www.businessinsider.com/botsitting-ai-hidden-human-labor-at-work-2026-6)

---

**[Slightly reducing the sloppiness of AI generated front end](https://news.ycombinator.com/item?id=48504912)**

⬆️ 217 • 💬 128 • 1d ago • [envs.net](https://envs.net/~volpe/blog/posts/reduce-slop.html)

---

**[AI OSS tool repo goes archived over night after raising $7.3M Seed](https://news.ycombinator.com/item?id=48516504)**

TensorZero is an open-source LLMOps platform that unifies an LLM gateway, observability, evaluation, optimization, and experimentation. - tensorzero/tensorzero

⬆️ 209 • 💬 140 • 7h ago • [GitHub](https://github.com/tensorzero/tensorzero)

---

**[Shall we play a game? My AI nuclear simulation](https://news.ycombinator.com/item?id=48495575)**

My AI nuclear simulation is out now, and it's a WOPR.

⬆️ 205 • 💬 199 • 2d ago • [kennethpayne.uk](https://www.kennethpayne.uk/p/shall-we-play-a-game)

---

**[A jacket that harvests drinking water from the air](https://news.ycombinator.com/item?id=48497576)**

The advance in fabric technology comes alongside a new benchmark for atmospheric water harvesting.

⬆️ 159 • 💬 99 • 1d ago • [UT Austin News - The University of Texas at Austin](https://news.utexas.edu/2026/06/11/this-jacket-pulls-drinking-water-from-thin-air/)

---

**[AI coding at home without going broke](https://news.ycombinator.com/item?id=48518969)**

There are three ways to do AI coding at home without spending like a company, and which one fits depends mostly on how much you trust the next year of hardwa...

⬆️ 139 • 💬 128 • 3h ago • [stephen.bochinski.dev](https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/)

---

---

## YouTube Videos: "ai"

**[Latest Claude AI models suspended after orders from Trump administration • FRANCE 24 English](https://www.youtube.com/watch?v=MDaZ31jx2vQ)**

Anthropic says it's suspended access to its latest AI models, in order to comply with a US national security order. Just three days ...

📺 FRANCE 24 English

👁️ 81K • 👍 932 • 💬 352 • ⏱️ 1:32 • 8h ago

---

**[The End of Unrestricted AI: Why Claude Fable 5 Was Just Forced Offline](https://www.youtube.com/watch?v=b3jlsjOIOzs)**

My Links Newsletter: https://natesnewsletter.substack.com/ X: https://x.com/natebjones TikTok: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 42K • 👍 2K • 💬 635 • ⏱️ 10:04 • 13h ago

---

**[Anthropic&#39;s Fable Backlash, Nationalizing AI, Inflation Heats Up &amp; California’s Broken Elections](https://www.youtube.com/watch?v=gH4FTjDm9FQ)**

(0:00) Besties are back! (0:19) Anthropic gets massive backlash over secret Fable nerfing and privacy concerns (29:16) The AI ...

📺 All-In Podcast

👁️ 114K • 👍 4K • 💬 685 • ⏱️ 1:42:00 • 14h ago

---

**[We&#39;re Not Ready for Self-Building AI, But it&#39;s Happening](https://www.youtube.com/watch?v=QADKN3hantI)**

Try out Consensus!! https://get.consensus.app/n6durqk1ao40 Artificial Intelligence is beginning to improve itself. In today's video I ...

📺 Sabine Hossenfelder

👁️ 27K • 👍 3K • 💬 586 • ⏱️ 6:40 • 5h ago

---

**[The Invisible War: A Realistic AI Takeover Scenario](https://www.youtube.com/watch?v=S2oIFOm-XXQ)**

Detailed sources: ...

📺 Species | Documenting AGI

👁️ 60K • 👍 4K • 💬 729 • ⏱️ 28:12 • 22h ago

---

**[‘LIKELY NECESSARY’: Anthropic CEO floats AI tax to fund universal basic income](https://www.youtube.com/watch?v=ELiwQ5K0mZ4)**

'Barron's Roundtable' newsletter editor Josh Schafer discusses SpaceX's expected IPO and Anthropic's CEO suggesting a tax on ...

📺 Fox Business

👁️ 5K • 👍 111 • 💬 77 • ⏱️ 5:25 • 1d ago

---

**[AI Expert Issues DIRE WARNING You Have To See To Believe](https://www.youtube.com/watch?v=CR7UNbZag7U)**

Support The Show On Patreon!: https://www.patreon.com/seculartalk Subscribe to Krystal Kyle & Friends On Substack!

📺 Secular Talk

👁️ 87K • 👍 6K • 💬 1K • ⏱️ 18:21 • 18h ago

---

**[AI News: An INSANE Week… Here’s What Matters](https://www.youtube.com/watch?v=nydHKXjwu0U)**

Here's the AI News you probably missed this week. Discover More: 🛠️ Explore AI Tools & News: https://futuretools.io/ Weekly ...

📺 Matt Wolfe

👁️ 56K • 👍 2K • 💬 173 • ⏱️ 30:52 • 1d ago

---

**[Anthropic begged the world to stop AI… then shipped this](https://www.youtube.com/watch?v=1PBRhm5ZnjU)**

Render is the easiest place to ship full-stack apps and agents. The first 2000 people to use the code RENDER-FIRESHIP will get ...

📺 Fireship

👁️ 691K • 👍 25K • 💬 1K • ⏱️ 5:09 • 2d ago

---

**[Best AI Video Generator for 4K Videos in 2026 (Full Test)](https://www.youtube.com/watch?v=3DWP5w7yd2I)**

Access THE BEST 4K Video Generator in OpenArt https://youricreates.com/4k-AI In this video, I compare Veo 3.1, LTX-2.3, ...

📺 Youri van Hofwegen

👁️ 6K • 💬 5 • ⏱️ 10:18 • 5h ago

---

---

## HuggingFace Models: 🔥 Trending

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 92,080 • ❤️ 682 • 3d ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 1,689 • ❤️ 477 • 1d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 69,443 • ❤️ 1,950 • 1d ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 1,031 • ❤️ 394 • 18h ago

---

**[North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**

*Cohere Labs*

North Mini Code 1.0 is a 30B-3B parameter research model optimized for code generation and agentic software engineering, featuring a 256K context length and tool-use capabilities for terminal tasks.

`text-generation` `30.5B`

⬇️ 6,533 • ❤️ 345 • 2d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 1,005,883 • ❤️ 990 • 9d ago

---

**[higgs-audio-v3-tts-4b](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b)**

*Boson AI*

Higgs Audio v3 TTS is a 4B parameter autoregressive text-to-speech model supporting over 100 languages with zero-shot voice cloning. It offers fine-grained control over speech characteristics like emotion, style, and prosody via inline tokens, making it suitable for expressive conversational AI and voice agents.

`text-to-speech` `4.7B`

⬇️ 32,162 • ❤️ 407 • 3d ago

---

**[diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)**

*Unsloth AI*

DiffusionGemma-26B-A4B-it-GGUF is a 26B MoE multimodal generative model that produces text output from text, image, and video inputs using discrete diffusion. Optimized for speed and deployability, it leverages Gemma 4 architecture advancements for efficient token generation.

`image-text-to-text` `25.3B`

⬇️ 42,885 • ❤️ 238 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,411,202 • ❤️ 1,754 • 1mo ago

---

**[Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)**

*OBLITERATUS*

Gemma-4-12B-OBLITERATED is a text-generation model modified via weight surgery to achieve zero refusals while maintaining stock benchmark performance. It's designed for alignment research, red-teaming, and safety evaluation by removing safety guardrails.

`text-generation` `12.0B`

⬇️ 50,289 • ❤️ 271 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 92 • 💬 4 • ⭐ 85,728 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SIA: Self Improving AI with Harness & Weight Updates](https://huggingface.co/papers/2605.27276)**

*Prannay Hebbar, Yogendra Manawat, Samuel Verboomen et al. (7 authors)*

🏢 Hexo AI

A self-improving AI framework simultaneously updates both model weights and task-specific agent architecture through a language-model feedback agent across legal classification, GPU optimization, and biological data denoising tasks.

▲ 13 • 💬 2 • ⭐ 1,636 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2605.27276) • [💻 code](https://github.com/hexo-ai/sia) • [🔗 project](https://hexolabs.com/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 228 • 💬 3 • ⭐ 6,137 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 16 • 💬 1 • ⭐ 82,093 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[InterleaveThinker: Reinforcing Agentic Interleaved Generation](https://huggingface.co/papers/2606.13679)**

*Dian Zheng, Harry Lee, Manyuan Zhang et al. (7 authors)*

InterleaveThinker enables interleaved generation capabilities for image generators through a multi-agent pipeline with planner and critic agents, achieving performance comparable to state-of-the-art models while enhancing reasoning benchmarks.

▲ 74 • 💬 3 • ⭐ 110 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.13679) • [💻 code](https://github.com/zhengdian1/InterleaveThinker) • [🔗 project](https://zhengdian1.github.io/InterleaveThinker-proj/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 40 • 💬 4 • ⭐ 29,487 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Agents' Last Exam](https://huggingface.co/papers/2606.05405)**

*Yiyou Sun, Xinyang Han, Weichen Zhang et al. (308 authors)*

🏢 UC Berkeley

Agents' Last Exam (ALE) is a benchmark for evaluating AI agents on long-term, economically valuable real-world tasks across 13 industry clusters with 1K+ tasks, revealing significant gaps between benchmark performance and practical deployment.

▲ 329 • 💬 3 • ⭐ 614 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05405) • [💻 code](https://github.com/rdi-berkeley/agents-last-exam) • [🔗 project](https://agents-last-exam.org/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 80 • 💬 7 • ⭐ 76,711 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 166 • 💬 2 • ⭐ 67,402 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 119 • 💬 1 • ⭐ 10,114 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 70.0k • 🔱 8.9k • 2h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 4.0k • 🔱 348 • 2h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.6k • 🔱 369 • 8d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.2k • 🔱 341 • 2d ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.0k • 🔱 357 • 2d ago

---

**[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)**

Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

`TypeScript` `baas` `backend-as-a-service` `mcp` `open-source` `postgres`

⭐ 2.1k • 🔱 144 • 4h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.0k • 🔱 182 • 4d ago

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

⭐ 1.5k • 🔱 133 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*
