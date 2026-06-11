---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-11T11:54:48.953084+00:00'
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

**Last Updated:** June 11, 2026 at 11:54 UTC  
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

**[Nobody needs AI to search the Internet, court says in ruling against Google](https://www.reddit.com/r/artificial/comments/1u2cwez/nobody_needs_ai_to_search_the_internet_court_says/)**

🔗 [arstechnica.com](https://arstechnica.com/tech-policy/2026/06/nobody-needs-ai-to-search-the-internet-court-says-in-ruling-against-google/) • 16h ago

---

**[I ran Fable 5 for half day and the guardrails are the real story](https://www.reddit.com/r/artificial/comments/1u28c7d/i_ran_fable_5_for_half_day_and_the_guardrails_are/)**

Anthropic dropped Fable 5 and I immediately swapped it into our dev stack. We route everything through a single endpoint on zenmux, so the actual switch was changing one model string and watching the latency graphs. The good parts first because there are a lot of them. I threw a refactoring task at it: split a messy python service into modules, preserve the public api, and write tests that prove nothing broke. Fable 5 planned the whole thing, caught a circular dependency I did not mention, and verified the tests pass. With Opus 4.8 I usually have to nudge it a couple of times when it forgets to update the init file. Fable 5 just did it. Then I dumped our full codebase and asked it to find a race condition we had been hunting for a week. It traced the async flow, named the exact function, and described the interleaving that triggers the bug. That level of context digestion feels new. Opus is good at long context, but Fable 5 felt like it was actually reasoning across the whole window instead of pattern matching near the top. I also sent it a blurry dashboard screenshot from a client call and it rebuilt the html and echarts config including the tooltip formatting. My designer’s first words were "when did you learn front end." I did not. But here is the part nobody in the launch threads is talking about enough. It is slow. On high effort I am seeing 45 to 90 seconds for a single complex turn. Our latency graphs go from a flat green line to a jagged mess the moment Fable 5 traffic hits. And it is expensive. The same prompt that costs X on Opus 4.8 costs roughly 1.4 to 1.7X on Fable 5 because it generates more tokens and runs at a higher effort tier by default. It writes its own reasoning traces out loud and bills you for them. For research tasks the quality is worth it. For "rewrite this email" it is comically overpowered. The bigger issue is the silent fallback. Fable 5 is basically Mythos with guardrails. When your prompt touches cybersecurity, biology, chemistry, or distillation, it silently routes to Opus 4.8. No warning. I found this out debugging a staging proxy config, entirely normal internal work, and halfway through the thread the code style changed. Checked the metadata and sure enough it had fallen back to Opus 4.8 mid thread because the word "proxy" made the classifier jumpy. Anthropic says this happens in under 5 percent of sessions globally, but for my stack it was closer to 15 percent because we touch infrastructure and networking a lot. When it happens mid task the model switch breaks context. I had a four turn debugging sequence where turn three flipped to Opus because I mentioned a firewall rule, then turn four flipped back. The state was preserved but the tone and depth shifted enough that I had to restart the thread. After 12 hours here is where I land. If you are doing pure software engineering, data analysis, or scientific reasoning in safe domains, Fable 5 is the best model I have ever used. It is not close. But if you touch infrastructure or security, the silent fallback is genuinely annoying and you need to monitor which model actually answered you. We only caught the switch because our gateway logs the per call trace. Without that you might not even know it swapped until the tone changes. I am keeping it enabled for our non sensitive dev workflows. For anything touching infra I am routing to Opus 4.8 explicitly until I understand the classifier boundaries better. Fable 5 is a beast. Anthropic just needs to tell you when it is not the one driving.

18h ago

---

**[Microsoft continues global rollout of Copilot's smiley AI companion Mico, now available in 40 countries](https://www.reddit.com/r/artificial/comments/1u2uzmm/microsoft_continues_global_rollout_of_copilots/)**

Mico for Copilot was introduced at the tail end of last year, exclusive to the United States. Now it's available around the world.

🔗 [PC Guide](https://www.pcguide.com/news/microsoft-continues-global-rollout-of-copilots-smiley-ai-companion-mico-now-available-in-40-countries/) • 1h ago

---

**[Judge Learns Lawyers on Both Sides of Case Used AI, Cancels Trial, Kicks Everyone Off the Case](https://www.reddit.com/r/artificial/comments/1u2onqz/judge_learns_lawyers_on_both_sides_of_case_used/)**

When two AIs argue against each other, the legal system loses.

🔗 [404 Media](https://www.404media.co/judge-learns-lawyers-on-both-sides-of-case-used-ai-cancels-trial-kicks-everyone-off-the-case/) • 7h ago

---

**[When someone shares a productivity system](https://www.reddit.com/r/artificial/comments/1u2wm54/when_someone_shares_a_productivity_system/)**

Good system. One addition that moved the needle for me: ​ I track "capacity conversion" -- when AI saves me 3 hours on a task what do those 3 hours actually become? ​ Most people save time with AI and then fill it with more busywork. The ROI only materializes when you deliberately redirect saved time toward higher-value activities. ​ I keep a simple log: "AI saved X hours on [task]. Redirected to [activity]. Value of redirected time: [$amount]." ​ After 6 months, my actual ROI was 4x higher than the "time saved" metric suggested because of where the saved time went. ​

15m ago

---

**[Anthropic Fable 5's silent downgrade got walked back in 24 hours, that should concern you even more](https://www.reddit.com/r/artificial/comments/1u2vs06/anthropic_fable_5s_silent_downgrade_got_walked/)**

A lot of discussion about Fable 5 has focused on the visible restrictions: cybersecurity, biology, certain chemistry. You hit a wall, you get a notification, you get redirected to Opus 4.8. That's frustrating, but at least it's honest. At least you know the model stepped back. Here's the part that's really disturbing, buried in a 319-page system card: There's a second category of restriction. For AI development and research work, Fable 5 doesn't redirect you. It doesn't notify you. It responds. It just delivers a deliberately weakened answer, and the system card describes this explicitly as "not visible to the user." Anthropic walked this back within 24 hours after fierce backlash. They apologized. "We made the wrong tradeoff." Good. But sit with what actually happened here, because the reversal is being treated as the end of the story when it's the beginning of a much harder problem. We now know three things we cannot unknow: Anthropic built this. They shipped it. And they only reversed it when the backlash was loud enough. The question isn't whether this specific invisible downgrade still exists. The question is what else might they be doing, in categories that don't generate the same backlash, that isn't disclosed in a document most people will never read anyway. This is a new kind of problem. And to understand why, you have to take a step back for a second. The pattern In January 2026, OpenAI announced that they would retire GPT-4o. Hundreds of thousands of daily users had built working relationships with that model over months: preferences it learned, corrections they made, communication styles that developed through hundreds of sessions. Gone. In February 2026, Gemini users found their chat histories had quietly vanished. No warning. No export. In April, Anthropic cut off Claude Pro and Max subscribers from using their subscriptions with third-party tools. Workflows that people depended on broke overnight. Each of these was framed differently. Model retirement. Policy update. Security measure. But the outcome was the same: users built something inside a platform, and then the platform unilaterally changed the terms. What you actually lose when a platform changes the deal When Instagram disables your account, you lose photos and followers. That's painful. But you still have everything in your head. The knowledge is still yours. What accumulates inside an AI conversation is different. It's not content. It's context. Every correction you made. Every preference the model picked up. Every project it understood. Every working session where you talked through a problem and landed somewhere useful. That's not a file you can download. It's not stored anywhere you control. It lives on their servers, tied to their model, subject to their terms. And Anthropic's own support page makes the stakes of this concrete: you cannot change the email address on your Claude account. Their recommended solution if your email becomes inaccessible is to delete your account and start over. Everything you built, gone. Their advice: "make sure you use an email you'll have long-term access to." That's the whole policy. Why Fable 5's invisible restriction is different The previous platform risks were about access. You lose access to the model. You lose access to your history. That's painful but understandable. The Fable 5 silent downgrade was about trust. You still had access. The model still responded. You just couldn't tell whether you were getting full capability or a deliberately degraded version of it. And the population being silently downgraded was specifically AI researchers and developers. Anthropic's stated justification is preventing acceleration of bad actors. But that's a justification that applies to only about 0.03% of traffic, while also describing exactly the researchers building tools that compete with Anthropic's own infrastructure. It's worth noting the timing: Fable 5 dropped just over a week after Anthropic confidentially filed IPO paperwork. The walkback doesn't close the unfalsifiability problem, instead it deepens it. Anthropic's own explanation for why they built it this way: "Visible safeguards can be probed, so they have to be robust, which takes time to get right. Invisible safeguards can be targeted more narrowly, allowing us to ship quickly." That's arguably a coherent engineering rationale. It's also a description of a permanent incentive. They showed us the capability. They showed us the willingness. The check on it was public pressure, not policy. That's not a foundation you can build upon. Your work with AI Most of us are not building competing AI infrastructure. The AI research restriction may not touch us directly. But the pattern matters regardless. The visible restrictions are already broad enough that people doing legitimate genomics work, security research, and health-adjacent projects are getting bounced mid-session before they've said anything substantive. The classifier fires on context, not just explicit requests. Session history. Project names. Adjacent topics. And the deeper issue is the one that applies to everyone: everything you've built inside Claude, every preference it's learned, every piece of context it carries about your work, exists at Anthropic's discretion. It always has. What Fable 5 adds is the proof that the model's responses can and will be manipulated in ways you can't see. Next time, this will only surface when someone reads the right paragraph in a 319-page document and makes enough noise - if they choose to disclose it at all. The model you're talking to might not be the model you think you're talking to. We just learned that this is concretely, verifiably true. The Fortune piece on Fable 5 and the system card are both worth reading if you haven't, and Wired has the walkback. (Links in first comment)

57m ago

---

**[Within a few years, owning the smartest AI will mean nothing — everyone will have it. The edge is knowing how to run it.](https://www.reddit.com/r/artificial/comments/1u2viem/within_a_few_years_owning_the_smartest_ai_will/)**

Every layer of AI solved the problem the last one left behind. The unsolved one: a shared, measurable standard for how to RUN intelligence — yours and the AI's, together. I spent 10+ years writing it down and it's falsifiable (pre-registered tests, failure lines locked before data). Asking for your strongest critiques Essay: https://joshmason573557.substack.com/p/colive-the-missing-standard-for-the

1h ago

---

**[Is this music AI?](https://www.reddit.com/r/artificial/comments/1u2vfy1/is_this_music_ai/)**

I think it is but I'd just like to get some second opinions, especially from music creators. This is their spotify page https://open.spotify.com/artist/4dSJvPjnA1RU6KcngvaZ96 The artwork is definitely AI and there's no real composer name so some red flags there already.

🔗 [youtu.be](https://youtu.be/hVF7jzQXseU?si=FES8aphr-gmCcESB) • 1h ago

---

**[Has anyone built (or bought) a Digital Brain for your Business?](https://www.reddit.com/r/artificial/comments/1u2ulai/has_anyone_built_or_bought_a_digital_brain_for/)**

I'm really interested in trying to learn about this new concept of having a one central AI-powered database acting as a digital brain for your business, pulling in all of the various data sources and having one single source of truth. People like Nate B Jones talk about it and I really want to try to build something - but concious how wrong they can go. Are there any credible ones already build I can base off? Has anyone done this?

2h ago

---

**[GitLab says Git is being reengineered for "machine scale." Was the idea of "Git for AI agents" ahead of its time?](https://www.reddit.com/r/artificial/comments/1u20ht8/gitlab_says_git_is_being_reengineered_for_machine/)**

I was reading GitLab's recent statements around agentic software engineering, and one quote really stood out: "Git itself is being reengineered for machine scale." (Business Insider) According to GitLab, future software development will involve AI agents that: plan, code, review, deploy, and repair software, with humans providing oversight and architectural judgment. (Business Insider) That got me thinking. There has been projects for some time arguing that AI agents shouldn't simply be treated as better autocomplete systems. Instead, they argued that agents should become first-class participants in software development: with their own identities, their own branches, their own merge requests, their own audit trails, and infrastructure designed for machine-rate collaboration. One example is GitLawb, which has described itself as a kind of "Git for agents." At the time, a lot of people dismissed these ideas as unnecessary or overly ambitious. But now GitLab—a multi-billion-dollar DevSecOps company—is talking about: agent-specific APIs, machine-scale Git infrastructure, orchestration layers coordinating agents, and agents acting as first-class users of development platforms. (Business Insider) It does raise an interesting question: Was the underlying thesis correct all along? We've seen similar patterns before: Containers existed before Kubernetes became the standard. Electric vehicle startups pushed ideas that incumbents later adopted. Cloud-native companies advocated architectures that the rest of the industry eventually embraced. The original innovators don't always dominate the market. But when major incumbents begin rebuilding around similar assumptions, it often suggests that the problem itself is real. So I'm curious what this community thinks: Do AI agents require an entirely new layer of collaboration infrastructure? Or will existing platforms simply evolve enough to absorb these workflows? Because if GitLab is right, software development may be transitioning from:humans using AI tools to humans managing teams of AI developers. And if that's the case, version control itself may have to evolve.

23h ago

---

---

## Google News: "ai"

**[Why U.S. AI giants like Anthropic, OpenAI are launching major expansions in London](https://www.cnbc.com/2026/06/11/anthropic-openai-london-expansions-big-tech.html)**

The U.K. capital has become a key growth target for many of the world's most talked about AI companies.

CNBC • 1h ago

---

**[Anthropic Walks Back Policy That Could Have ‘Sabotaged’ AI Researchers Using Claude](https://www.wired.com/story/anthropic-responds-to-backlash-on-claudes-secret-sabotage-on-ai-research/)**

The company changed course after researchers spoke out against the policy, which would have covertly limited Claude’s ability to develop competing AI models.

WIRED • 8h ago

---

**[Anthropic's Amodei calls for workers’ rights over AI](https://www.yahoo.com/news/politics/articles/anthropics-amodei-calls-workers-rights-111819373.html)**

Amodei said AI could soon create both huge economic growth and massive unemployment.

Yahoo • 36m ago

---

**[DiffusionGemma: 4x faster text generation](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)**

An overview of DiffusionGemma, an exceptionally fast text generation model with up to 4x faster speeds.

blog.google • 19h ago

---

**[What the rise in flash drives tells us about inflation (and AI)](https://www.axios.com/2026/06/11/inflation-ai-computer-flash)**

Axios • 54m ago

---

**[Bank of America buys into agentic AI trade, double upgrades this stock](https://www.cnbc.com/2026/06/11/bank-of-america-buys-into-agentic-ai-trade-double-upgrades-this-stock.html)**

The bank thinks a growing market for CPUs will be a boon to the chipmaker that has surged more than 60% since its first quarter earnings report release.

CNBC • 32m ago

---

**[India’s workers are training AI robots to take their jobs](https://www.aljazeera.com/gallery/2026/6/11/photos-indias-workers-are-training-ai-robots-to-take-their-jobs)**

Developers believe that feeding first-person footage into specialised AI models will help robots copy human behaviour.

Al Jazeera • 1h ago

---

**[AI absolutism is breaking our brains. The apocalyptic future we’re being sold isn’t inevitable](https://www.theguardian.com/technology/2026/jun/11/ai-absolutism-apocalyptic-future)**

Nor is the dreamy promise that this tech will unlock boundless potential and productivity

The Guardian • 1h ago

---

**[Opinion | I was a V.C. Partner. We Can’t Let Silicon Valley Buy Democracy.](https://www.nytimes.com/2026/06/11/opinion/silicon-valley-ai-politics.html)**

The New York Times • 2h ago

---

**[AI is sparking a jobs boom — just not for newbies](https://www.cnn.com/2026/06/11/business/ai-jobs-work)**

As Corporate America scrambles to fill artificial intelligence jobs, junior workers are getting left behind.

CNN • 1h ago

---

---

## HackerNews: "ai"

**[German ruling declares Google liable for false answers in AI Overviews](https://news.ycombinator.com/item?id=48470248)**

A German regional court has ruled that Google is directly liable for the content of its AI search overviews. According to the court, previous limited liability protections for search engine operators don't apply to AI overviews. In this case, Google's AI had falsely linked two publishers to fraud and made claims that didn't appear in any of the linked sources. The ruling could set a precedent for AI-generated content liability worldwide.

⬆️ 982 • 💬 523 • 1d ago • [The Decoder](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/)

---

**[CEOs who think AI replaces their employees are just bad CEOs](https://news.ycombinator.com/item?id=48465675)**

⬆️ 824 • 💬 300 • 1d ago • [techdirt.com](https://www.techdirt.com/2026/06/09/ceos-who-think-ai-replaces-their-employees-are-just-bad-ceos/)

---

**[Apple reveals new AI architecture built around Google Gemini models](https://news.ycombinator.com/item?id=48450142)**

Apple today announced a major overhaul of its Apple Intelligence platform, revealing a new architecture built on foundation models developed in collaboration with Google using the technologies behind the Gemini family. The new architecture centers on Apple Foundation Models co-developed with Google, which Apple says are adapted to run both on-device and on servers through its existing Private Cloud Compute infrastructure.

⬆️ 730 • 💬 559 • 2d ago • [MacRumors](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/)

---

**[Siri AI](https://news.ycombinator.com/item?id=48449084)**

Next-generation Apple Intelligence and Siri AI bring helpful features to iOS 27, iPadOS 27, macOS Golden Gate, watchOS 27, and visionOS 27.

⬆️ 671 • 💬 696 • 2d ago • [Apple](https://www.apple.com/apple-intelligence/)

---

**[AI is slowing down](https://news.ycombinator.com/item?id=48446893)**

If you liked this piece, you should subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of NVIDIA, Anthropic and OpenAI’s

⬆️ 663 • 💬 761 • 2d ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/ai-is-slowing-down/)

---

**[Microsoft's open source tools were hacked to steal passwords of AI developers](https://news.ycombinator.com/item?id=48457830)**

Microsoft shut down dozens of GitHub code repositories for Azure and AI coding tools after a reported hack.

⬆️ 556 • 💬 193 • 2d ago • [TechCrunch](https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/)

---

**[Cleaning up after AI rockstar developers](https://news.ycombinator.com/item?id=48458586)**

We've all worked with a rockstar developer. They joined the team years ago, full of energy. They had great ideas about new tech, new paradigms, new architectures. Their cutting-edge ideas left everyone else feeling a bit behind and outdated.

⬆️ 491 • 💬 358 • 2d ago • [codingwithjesse.com](https://www.codingwithjesse.com/blog/rockstar-developers/)

---

**[AI agent runs amok in Fedora and elsewhere](https://news.ycombinator.com/item?id=48484584)**

Agentic AI systems can be used to do a variety of things autonomously on behalf of a human user [...]

⬆️ 441 • 💬 188 • 11h ago • [LWN.net](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/)

---

**[Ask HN: What are tools you have made for yourself since the advent of AI?](https://news.ycombinator.com/item?id=48449187)**

⬆️ 429 • 💬 744 • 2d ago

---

**[Apple Core AI Framework](https://news.ycombinator.com/item?id=48449665)**

Run AI models in your app on Apple silicon.

⬆️ 363 • 💬 107 • 2d ago • [Apple Developer Documentation](https://developer.apple.com/documentation/coreai/)

---

---

## YouTube Videos: "ai"

**[AI Stock Bubble Bursts - $1.3 Trillion Market Crash Sparks Global Panic](https://www.youtube.com/watch?v=RA_WC4EKAhA)**

Join the discussion on our Substack at https://www.worldaffairsincontext.com/, where we discuss geopolitics, economics, and the ...

📺 World Affairs In Context

👁️ 70K • 👍 5K • 💬 379 • ⏱️ 11:55 • 23h ago

---

**[Anthropic&#39;s CEO raises concerns over rapidly developing AI technology](https://www.youtube.com/watch?v=C9Rnt3FKaIY)**

In an interview with ABC News' Linsey Davis, Dario Amodei issued an urgent warning about the dangers of AI, calling for ...

📺 ABC News

👁️ 7K • 👍 116 • 💬 45 • ⏱️ 2:07 • 11h ago

---

**[Anthropic Just Dropped Fable 5 And It’s Terrifying](https://www.youtube.com/watch?v=8TjCwdnZSp8)**

Anthropic just released Claude Fable 5, its first publicly available Mythos-class AI model, and the whole launch feels different.

📺 AI Revolution

👁️ 57K • 👍 2K • 💬 311 • ⏱️ 11:30 • 1d ago

---

**[The Riskiest Moment of the AI Bubble](https://www.youtube.com/watch?v=AcjnLc4TH4M)**

NOTE! Since I recorded this video: 1. OpenAI has indeed made it's first filing to go public, though how long from now that will ...

📺 Hank Green

👁️ 1.4M • 👍 44K • 💬 4K • ⏱️ 12:29 • 1d ago

---

**[The dark side of AI - Exploitation of humans and nature | DW Documentary](https://www.youtube.com/watch?v=ND7owjmtPNo)**

Magical, autonomous, all-powerful: Artificial intelligence fuels our dreams and nightmares. While tech companies promise us a ...

📺 DW Documentary

👁️ 93K • 👍 3K • 💬 387 • ⏱️ 54:11 • 19h ago

---

**[Master 95% of AI Video in 15 Minutes (Become a PRO)](https://www.youtube.com/watch?v=RUAuMD5hUBw)**

Create Your AI Videos Here: https://openart.ai/home?ref=MasterAIVideo Download My Claude AI Video Prompt Skill: ...

📺 Tao Prompts

👁️ 7K • 👍 482 • 💬 33 • ⏱️ 15:24 • 16h ago

---

**[Trump Sells UFC Coins as Iran Strikes &amp; Melania Pushes AI in a Speech Worthy of AI | The Daily Show](https://www.youtube.com/watch?v=gmpaIbsPpFo)**

Melania ushers in the age of AI while sounding like a robot, tensions rise again in Iran as the U.S. and Tehran trade blows, and ...

📺 The Daily Show

👁️ 763K • 👍 25K • 💬 1K • ⏱️ 9:00 • 9h ago

---

**[The AI Bubble Pop Everyone Predicted Just Got Canceled](https://www.youtube.com/watch?v=lBs5w7cgF8o)**

Despite recent speculation, the AI bubble pop is canceled, a thesis no longer supported by current evidence. We look at insights ...

📺 Dr. Josh C. Simmons

👁️ 6K • 👍 331 • 💬 124 • ⏱️ 11:38 • 15h ago

---

**[Claude Mythos (Fable) Just Went Live!! It&#39;s the best AI i&#39;ve ever used...](https://www.youtube.com/watch?v=-s8eOkoPAwc)**

Sign up for the AI Edge newsletter for weekly AI guides: https://www.aiedgehq.co/ Claude Fable 5 just dropped, and it's the ...

📺 AI Edge

👁️ 12K • 👍 464 • 💬 39 • ⏱️ 21:09 • 1d ago

---

**[They released Mythos (the most powerful AI)… #c#carterpcstech #mythos #ai #fable5](https://www.youtube.com/watch?v=wk37Ysf6r2g)**

They released Mythos (the most powerful AI)… #c#carterpcstech #mythos #ai #fable5.

📺 CarterPCs

👁️ 1.9M • 👍 101K • 💬 2K • ⏱️ 0:36 • 13h ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 131,794 • ❤️ 1,836 • 2d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 675,936 • ❤️ 918 • 6d ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 0 • ❤️ 368 • 22h ago

---

**[higgs-audio-v3-tts-4b](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b)**

*Boson AI*

Higgs Audio v3 TTS is a 4B parameter autoregressive text-to-speech model supporting over 100 languages with zero-shot voice cloning. It offers fine-grained control over speech characteristics like emotion, style, and prosody via inline tokens, making it suitable for expressive conversational AI and voice agents.

`text-to-speech` `4.7B`

⬇️ 19,948 • ❤️ 335 • 15h ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 711,706 • ❤️ 555 • 1d ago

---

**[nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)**

*NVIDIA*

Nemotron 3.5 ASR is a multilingual, streaming Automatic Speech Recognition (ASR) model supporting 40 language-locales. It uses a Cache-Aware FastConformer-RNNT architecture for efficient, low-latency transcription of audio into punctuated text, suitable for both streaming and batch processing.

`automatic-speech-recognition`

⬇️ 4,965 • ❤️ 363 • 5d ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 7,170 • ❤️ 479 • 7d ago

---

**[North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**

*Cohere Labs*

North Mini Code 1.0 is a 30B-3B parameter research model optimized for code generation and agentic software engineering, featuring a 256K context length and tool-use capabilities for terminal tasks.

`text-generation` `30.5B`

⬇️ 1,859 • ❤️ 291 • 1h ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 140,221 • ❤️ 506 • 6d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,057,541 • ❤️ 1,649 • 1mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 91 • 💬 4 • ⭐ 85,117 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Agents' Last Exam](https://huggingface.co/papers/2606.05405)**

*Yiyou Sun, Xinyang Han, Weichen Zhang et al. (308 authors)*

🏢 UC Berkeley

Agents' Last Exam (ALE) is a benchmark for evaluating AI agents on long-term, economically valuable real-world tasks across 13 industry clusters with 1K+ tasks, revealing significant gaps between benchmark performance and practical deployment.

▲ 228 • 💬 2 • ⭐ 529 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05405) • [💻 code](https://github.com/rdi-berkeley/agents-last-exam) • [🔗 project](https://agents-last-exam.org/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 15 • 💬 1 • ⭐ 81,823 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Rethinking the Divergence Regularization in LLM RL](https://huggingface.co/papers/2606.09821)**

*Jiarui Yao, Xiangxin Zhou, Penghui Qi et al. (6 authors)*

🏢 Tencent-Hunyuan-Multimodal-RL

DRPO improves LLM reinforcement learning stability by replacing hard masks with smooth regularization that provides continuous gradient corrections beyond trust-region boundaries.

▲ 28 • 💬 4 • ⭐ 434 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.09821) • [💻 code](https://github.com/Tencent-Hunyuan/UniRL)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 172 • 💬 10 • ⭐ 49,239 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 225 • 💬 3 • ⭐ 5,702 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[SCAIL-2: Unifying Controlled Character Animation with End-to-end In-Context Conditioning](https://huggingface.co/papers/2606.10804)**

*Wenhao Yan, Fengjia Guo, Zhuoyi Yang et al. (4 authors)*

🏢 Z.ai

SCAIL-2 enables end-to-end character animation by directly transferring motion from driving videos without intermediate representations, using unified task decomposition and synthetic data generation.

▲ 32 • 💬 2 • ⭐ 220 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2606.10804) • [💻 code](https://github.com/zai-org/SCAIL-2) • [🔗 project](https://teal024.github.io/SCAIL-2/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 165 • 💬 2 • ⭐ 67,169 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 113 • 💬 1 • ⭐ 9,854 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 40 • 💬 4 • ⭐ 29,172 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 67.7k • 🔱 8.5k • 10m ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace for DeepSeek models, with Code and Claw modes built into your application.

`TypeScript`

⭐ 3.8k • 🔱 331 • 10h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.5k • 🔱 349 • 6d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.2k • 🔱 334 • 5h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 2.8k • 🔱 319 • 1d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.9k • 🔱 176 • 2d ago

---

**[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)**

Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

`TypeScript` `baas` `backend-as-a-service` `mcp` `open-source` `postgres`

⭐ 1.9k • 🔱 143 • 4h ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 138 • 6d ago

---

**[Helvesec/rmux](https://github.com/Helvesec/rmux)**

Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

`Rust` `agent` `ai` `cli` `linux` `macos`

⭐ 1.7k • 🔱 80 • 6d ago

---

**[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)**

Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base  Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工具链 + 自动进化经验库 | 支持 Claude Code / Kiro / Cursor / Cline 等代码 AI 客户端

`Shell`

⭐ 1.5k • 🔱 309 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
