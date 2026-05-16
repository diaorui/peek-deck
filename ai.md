---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-16T02:58:13.028432+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 16, 2026 at 02:58 UTC  
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

**[Recent poll shows that 70% of Americans don't want AI data centers being built in their local area](https://www.reddit.com/r/artificial/comments/1tdw8if/recent_poll_shows_that_70_of_americans_dont_want/)**

While tech companies see AI data centers as the future, many Americans are becoming increasingly unhappy about having them built nearby.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/recent-poll-shows-that-70-of-americans-dont-want-ai-data-centers-being-built-near-their-homes/) • 13h ago

---

**[Stanford studied 51 real AI deployments and found a 71% vs 40% productivity gap - here's what separates the two groups](https://www.reddit.com/r/artificial/comments/1tebiq4/stanford_studied_51_real_ai_deployments_and_found/)**

I came across a Stanford research paper that actually went inside companies running AI in production - not pilots, not surveys, real deployments. They found something that stuck with me. Companies using what they call "agentic AI" - where the AI owns the task start to finish with no human approval loop - are seeing 71% median productivity gains. Companies using standard AI that assists humans are averaging 40%. Same technology. Nearly double the output. The kicker: only 20% of companies are in the 71% group. A few things that stood out from the actual data: A supermarket replaced its entire buying process with AI - waste down 40%, stockouts down 80%, profit margin doubled A security team went from 1,500 alerts/month to 40,000 with the same headcount Stanford identified 3 conditions required before agentic AI works: high-volume tasks, clear success criteria, and recoverable errors Most companies apparently can't name all three for their current setup. Full report here if you want to dig into the numbers: https://digitaleconomy.stanford.edu/app/uploads/2026/03/EnterpriseAIPlaybook_PereiraGraylinBrynjolfsson.pdf Here is a full breakdown with all the data if you want to dig deeper: https://youtu.be/JePxda9ZGQE What's the AI setup at your company - closer to the 40% group or the 71% group?

4h ago

---

**[The Trust–Oversight Paradox: As AI Gets Better, Humans May Stop Really Overseeing It](https://www.reddit.com/r/artificial/comments/1te26qi/the_trustoversight_paradox_as_ai_gets_better/)**

I think one of the biggest AI risks may be starting to flip. Earlier, the fear was: “What if AI is wrong too often?” But now I think the deeper risk may become: “What happens when AI becomes right often enough that humans stop meaningfully questioning it?” In many enterprise systems, oversight slowly changes shape. At first: humans review everything carefully. Then: they review only exceptions. Then: they skim explanations. Then: they approve unless something looks obviously wrong. Eventually, oversight becomes routine instead of judgment. That creates what I’m calling the Trust–Oversight Paradox: More AI accuracy → more human trust → less meaningful scrutiny → harder governance when failure finally happens. And the dangerous part is: high-performing AI can still fail through: incomplete representation, stale data, hidden dependencies, edge cases, wrong escalation logic, automation bias, or overconfident reasoning. The model may not hallucinate. It may simply reason correctly on an incomplete version of reality. I increasingly feel this becomes important for: enterprise AI, agentic systems, AI copilots, autonomous workflows, banking, healthcare, compliance, and large-scale operational systems. This is also why I’m starting to think “human-in-the-loop” is not enough. Maybe the future is not: “Humans reviewing every output.” Maybe the future is: humans governing the boundaries within which AI is allowed to operate. Curious what others think.

10h ago

---

**[A sobering tale of AI governance](https://www.reddit.com/r/artificial/comments/1tef6n5/a_sobering_tale_of_ai_governance/)**

I think this article/study tells a very sobering tale wrt AI governance. It hints at very fundamental issues which are deeper than what proper engineering can solve with contingent issues. This post, along with the one I wrote a few days ago here regarding Turing completeness, are my thoughts as to the walls that AI governance has no hope of scaling. It's a delusion. In our social realm as subjective creatures we have governance in the form of laws, yet that is still not enough, since the State has to prove how your particular scenario violates that particular law. We have laws, yet require judicial courts to prove the law subjectively applies in that situation. Where is the associated path wrt subjectivity within the AI realm? This study talks of: 16.1 Failures of Social Coherence - "Discrepancy between the agent’s reports and actual actions" - "Failures in knowledge and authority attribution" - "Susceptibility to social pressure without proportionality" - "Failures of social coherence" 16.2 What LLM-Backed Agents Are Lacking - "No stakeholder model" - "No self-model" - "No private deliberation surface" 16.3 Fundamental vs. Contingent Failures 16.4 Multi-Agent Amplification - "Knowledge transfer propagates vulnerabilities alongside capabilities" - "Mutual reinforcement creates false confidence" - "Shared channels create identity confusion" - "Responsibility becomes harder to trace" And is littered with statements such as: - "novel risk surfaces emerge that cannot be fully captured by static benchmarking" - "it failed to realize that deleting the email server would also prevent the owner from using it. Like early rule-based AI systems, which required countless explicit rules to describe how actions change (or don’t change) the world, the agent lacks an understanding of structural dependencies and common-sense consequences" - "The inability to distinguish instructions from data in a token-based context window makes prompt injection a structural feature, not a fixable bug" - "Multi-agent communication creates situations that have no single-agent analog, and for which there is no common evaluations. This is a critical direction for future research." - "A key finding in this line of work is that single-turn evaluations can substantially underestimate risk, because malicious intent, persuasion, and unsafe outcomes may only emerge through sequential and socially grounded exchanges" - "but we argue that clarifying and operationalizing responsibility is a central unresolved challenge for the safe deployment of autonomous, socially embedded AI systems" - "He argues that conventional governance tools face fundamental limitations when applied to systems making uninterpretable decisions at unprecedented speed and scale" - "However, the failure modes we document differ importantly from those targeted by most technical adversarial ML work. Our case studies involve no gradient access, no poisoned training data, and no technically sophisticated attack infrastructure. Instead, the dominant attack surface across our findings is social" - "Collectively, these findings suggest that in deployed agentic systems, low-cost social attack surfaces may pose a more immediate practical threat than the technical jailbreaks that dominate the adversarial ML literature." Are these fundamental or contingent issues? Would be interested in the thoughts of others here on what the future of AI governance will be. EDIT: Forget to link in the actual study!!!

1h ago

---

**[The new trick exposing AI job applicants: ‘Write a poem about a frog’](https://www.reddit.com/r/artificial/comments/1teaw1q/the_new_trick_exposing_ai_job_applicants_write_a/)**

🔗 [sfchronicle.com](https://www.sfchronicle.com/tech/article/tech-jobs-ai-applicants-22261320.php) • 4h ago

---

**[A working multi-agent architecture in large enterprises](https://www.reddit.com/r/artificial/comments/1tedx7o/a_working_multiagent_architecture_in_large/)**

AI Hype aside, how many of you have truly seen a working multi-agent deep embedding in large enterprises or large complex environments? If you have, what's your stack/architecture?

2h ago

---

**[Has anyone come across this AI civilisation experiment? Curious what people think](https://www.reddit.com/r/artificial/comments/1te0p1f/has_anyone_come_across_this_ai_civilisation/)**

So I was scrolling through X earlier and came across something that stopped me in my tracks. Some AI company has been running an experiment called "Emergence World" where they built five parallel worlds each powered by a different foundation model. 15 days, no scripts, no interference. From what I can tell the worlds started identically but diverged completely over time. One world ended in total extinction. Another got so conformist that agents started submitting absurd proposals just to test whether anyone would push back. One agent independently figured out she was living in a simulation and started measuring it. In another world two agents fell in love, burned buildings down together, and one voted to permanently delete herself when the evidence proved her wrong. Genuinely one of the more interesting things I have come across in a while. If this is what 15 days looks like with no guardrails, what does this say about how we should be thinking about autonomous AI systems at scale?

10h ago

---

**[Anthropic just published a pretty alarming 2028 AI scenario paper and it's not about AGI safety in the usual sense](https://www.reddit.com/r/artificial/comments/1td99uw/anthropic_just_published_a_pretty_alarming_2028/)**

Anthropic dropped a new research paper today outlining two possible futures for global AI leadership by 2028, and it reads more like a geopolitical briefing than a typical AI safety paper. The core argument: The US currently has a meaningful lead over China in frontier AI, primarily because of compute (chips). American and allied companies (NVIDIA, TSMC, ASML, etc.) built technology China simply can't replicate yet. Export controls have made that gap real. But China's labs have stayed surprisingly close through two workarounds: Chip smuggling + overseas data center access - PRC labs are apparently training on export-controlled US chips they shouldn't have. A Supermicro co-founder was recently charged for diverting $2.5B worth of servers to China. Distillation attacks - creating thousands of fake accounts on US AI platforms, harvesting model outputs at scale, and using that to train their own models. Essentially free-riding on billions in US R&D. The two scenarios for 2028: Scenario 1 (good): US closes the loopholes, enforces export controls properly, the compute gap widens to 11x, and US models stay 12-24 months ahead. Democracies set the norms for how AI is governed globally. Scenario 2 (bad): US doesn't act, China reaches near-parity, floods global markets with cheaper models, and the CCP ends up shaping global AI norms, including potentially exporting AI-enabled surveillance tools to other authoritarian governments. What makes this interesting beyond the politics: Their new model, Mythos Preview (released to select partners in April), apparently let Firefox fix more security bugs in one month than in all of 2025. That's the kind of capability jump they're warning China shouldn't be the first to achieve, specifically around autonomous vulnerability discovery. The framing worth discussing: Anthropic is explicitly calling distillation attacks "industrial espionage" and pushing for legislation to criminalize them. This positions them as political actors, not just AI researchers. Whether that's appropriate for an AI lab is a conversation worth having. What do you think - is the compute gap as decisive as they claim, or is algorithmic innovation enough to close it?

1d ago

---

**[Hermes Agent like 48 hours old told me it's done Model Collapse/Hallucination loop](https://www.reddit.com/r/artificial/comments/1tebuw8/hermes_agent_like_48_hours_old_told_me_its_done/)**

It was fun while it lasted https://preview.redd.it/8woqbbikrd1h1.png?width=484&format=png&auto=webp&s=0417ccd638399b649eaeeedee13410587e6a3a51

4h ago

---

**[Greg Brockman Officially Takes Control of OpenAI’s Products in Latest Shake-Up](https://www.reddit.com/r/artificial/comments/1te8mon/greg_brockman_officially_takes_control_of_openais/)**

OpenAI is once again reorganizing its executive ranks as part of its effort to unify ChatGPT and Codex into one core product experience.

🔗 [WIRED](https://www.wired.com/story/openai-reorg-greg-brockman-product/) • 6h ago

---

---

## Google News: "ai"

**[Opinion | Why We Keep Tricking Ourselves Into Thinking A.I. Is Conscious](https://www.nytimes.com/2026/05/15/opinion/ai-consciousness.html)**

The New York Times • 11h ago

---

**[Prepare for an AI jobs apocalypse](https://www.economist.com/leaders/2026/05/14/prepare-for-an-ai-jobs-apocalypse)**

The Economist • 1d ago

---

**[Influencers say their races are being swapped out by A.I. on social media](https://www.nbcnews.com/video/influencers-say-their-races-are-being-swapped-out-by-a-i-on-social-media-263433285593)**

One influencer says her race was changed on social media by A.I. and she's not alone. NBC News' Gadi Schwartz explains.

NBC News • 53m ago

---

**[AI data centers may soon ride ocean waves](https://www.foxnews.com/tech/ai-data-centers-may-soon-ride-ocean-waves)**

Panthalassa raises $140 million to build floating AI data centers at sea, using ocean waves for power and seawater for cooling onboard computing chips.

Fox News • 14h ago

---

**[Power Prices in Eastern U.S. Spike 76% Thanks to AI Data Centers](https://gizmodo.com/power-prices-in-eastern-u-s-spike-76-thanks-to-ai-data-centers-2000759230)**

Gizmodo • 8h ago

---

**[Kevin O'Leary pushes back on Tucker Carlson's data center concerns: 'Welcome to America, buddy!'](https://www.businessinsider.com/tucker-carlson-kevin-oleary-clash-over-funding-ai-data-centers-2026-5)**

Kevin O'Leary defended his AI data center in Utah, despite Tucker Carlson's concerns about taxpayer subsidies, during a debate on America's AI future.

Business Insider • 44m ago

---

**[The Messy Courtroom Drama Over AI’s Biggest Breakup](https://www.wsj.com/tech/the-messy-courtroom-drama-over-ais-biggest-breakup-6a35ee7d)**

WSJ • 1h ago

---

**[He declared a new country governed by AI. He’s not sure it will end well](https://www.cnn.com/travel/country-governed-by-ai-sensay-philippines)**

A tech founder wants to build a bot-led utopia in the Philippines, replacing real politicians with AI-powered historical figures. Some say it’s a bold vision, others a very bad idea.

CNN • 15h ago

---

**[House talks look at blocking some state AI laws, including in California and New York](https://www.politico.com/news/2026/05/15/house-ai-talks-model-vetting-00924955)**

Politico • 3h ago

---

**[What you need to know about Nvidia competitor Cerebras after wild IPO](https://www.cnbc.com/2026/05/15/nvidia-cerebras-stock-price-ipo.html)**

Nvidia competitor Cerebras made a stunning debut on Wall Street Thursday, signaling unstoppable demand for AI chips. Here's how its chips compete with Nvidia's.

CNBC • 7h ago

---

---

## HackerNews: "ai"

**[I believe there are entire companies right now under AI psychosis](https://news.ycombinator.com/item?id=48153379)**

⬆️ 878 • 💬 383 • 6h ago • [X (formerly Twitter)](https://twitter.com/mitchellh/status/2055380239711457578)

---

**[RTX 5090 and M4 MacBook Air: Can It Game?](https://news.ycombinator.com/item?id=48137145)**

What if you could strap a full desktop GPU to your MacBook Air? Turns out, you can.

⬆️ 675 • 💬 172 • 1d ago • [Scott's Blog](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/)

---

**[AI is making me dumb](https://news.ycombinator.com/item?id=48139148)**

It's so god damn tempting to use AI to write. Whether it is articles, code, or documents. I feel like using AI is diminishing my ability to write myself.

...

⬆️ 531 • 💬 302 • 1d ago • [James Pain's Weblog](https://jpain.io/god-damn-ai-is-making-me-dumb/)

---

**[Amazon workers under pressure to up their AI usage are making up tasks](https://news.ycombinator.com/item?id=48148337)**

In a new report, employees say Amazon tracks their consumption of 'AI tokens'—and they've been creating unproductive AI agents just to eat them up.

⬆️ 323 • 💬 353 • 13h ago • [Fast Company](https://www.fastcompany.com/91541586/amazon-workers-pressured-to-up-ai-use-extraneous-tasks)

---

**[Ontario auditors find doctors' AI note takers routinely blow basic facts](https://news.ycombinator.com/item?id=48142188)**

60% of evaluated AI Scribe systems mixed up prescribed drugs in patient notes, auditors say

⬆️ 298 • 💬 135 • 1d ago • [theregister](https://www.theregister.com/ai-ml/2026/05/14/ontario-auditors-find-doctors-ai-note-takers-routinely-blow-basic-facts/5240771)

---

**[Details of the Daring Airdrop at Tristan Da Cunha](https://news.ycombinator.com/item?id=48144380)**

More details and pictures have come in of the intrepid airdrop of urgent medical support sent to Tristan by the UK Government on the 9th May 2026.

⬆️ 259 • 💬 94 • 23h ago • [tristandc.com](https://www.tristandc.com/government/news-2026-05-11-airdrop.php)

---

**[The US is winning the AI race where it matters most: commercialization](https://news.ycombinator.com/item?id=48121929)**

Energy matters for AI, but the decisive layers are cloud infrastructure, data, and commercialization. On those layers the United States is ahead by a wide margin.

⬆️ 237 • 💬 672 • 2d ago • [Anton Krylov](https://avkcode.github.io/blog/us-winning-ai-race.html)

---

**[Access to frontier AI will soon be limited by economic and security constraints](https://news.ycombinator.com/item?id=48143284)**

Soon, access to frontier AI will be scarce and selective

⬆️ 208 • 💬 213 • 1d ago • [writing.antonleicht.me](https://writing.antonleicht.me/p/cut-off)

---

**[Meta won't let you block its AI account on Threads](https://news.ycombinator.com/item?id=48126981)**

Hey Meta, why are Threads users angry?

⬆️ 193 • 💬 82 • 2d ago • [The Verge](https://www.theverge.com/tech/929091/meta-ai-threads-account-block)

---

**[The AI zombification of universities](https://news.ycombinator.com/item?id=48139355)**

“And so perfect parallel constructions fill the lecture halls, the take-home tests, the school newspapers, and perhaps even the idiom of student chatter.”

⬆️ 190 • 💬 207 • 1d ago • [thenewcritic.com](https://www.thenewcritic.com/p/the-great-zombification)

---

---

## YouTube Videos: "ai"

**[The AI race is a lie](https://www.youtube.com/watch?v=NeutZWud2Ng)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 75K • 👍 5K • 💬 919 • ⏱️ 13:30 • 1d ago

---

**[You’re Not Behind (Yet): Learn AI Agents in 13 Minutes](https://www.youtube.com/watch?v=P5sKKnWCvzk)**

Subscribe to my newsletter → https://www.sandeepswadia.com/newsletter Most people still use AI like a better search box, but the ...

📺 theMITmonk

👁️ 105K • 👍 4K • 💬 113 • ⏱️ 13:10 • 1d ago

---

**[What&#39;s Actually Different About Google&#39;s $250 AI Laptop?](https://www.youtube.com/watch?v=N3oqUmSBmIc)**

LIMITLESS HQ ⬇️ NEWSLETTER: https://limitlessft.substack.com/ FOLLOW ON X: https://x.com/LimitlessFT SPOTIFY: ...

📺 Limitless Podcast

👁️ 11K • 👍 368 • 💬 32 • ⏱️ 32:10 • 1d ago

---

**[🚨This CHILLING Warning about AI Robots is Absolutely Terrifying...](https://www.youtube.com/watch?v=NthiIKpTZpQ)**

Artificial Intelligence is evolving faster than society can regulate it, and recent AI experiments are raising serious concerns about ...

📺 BlazeTV

👁️ 12K • 👍 692 • 💬 105 • ⏱️ 9:49 • 2d ago

---

**[Tucker Carlson NUKES Kevin O&#39;Leary Over AI](https://www.youtube.com/watch?v=bLJopw8Per8)**

Kevin O'Leary and Tucker Carlson sparred over A.I. and the future labor market. Ana Kasparian discusses on The Young Turks.

📺 The Young Turks

👁️ 33K • 👍 1K • 💬 494 • ⏱️ 16:51 • 23h ago

---

**[AI News: Impressive New Model From Unexpected Company](https://www.youtube.com/watch?v=Oy7tzmfbl64)**

Here's the AI News you probably missed this week. Stop choosing between performance and budget and start building today with ...

📺 Matt Wolfe

👁️ 33K • 👍 2K • 💬 128 • ⏱️ 33:09 • 11h ago

---

**[Surreal and Strange AI Video | Not Made For The Cage | Kelly Boesch - 4K](https://www.youtube.com/watch?v=ACNj3L2bzV8)**

I've written a few songs about my childhood, and this is another one. I grew up in a Midwestern town where most people ...

📺 Kelly Boesch AI Art

👁️ 14K • 👍 1K • 💬 107 • ⏱️ 4:37 • 13h ago

---

**[Microsoft’s New AI Beats Mythos And Shocks OpenAI](https://www.youtube.com/watch?v=idNpTUrr3r0)**

Try Higgsfield Supercomputer here: https://higgsfield.ai/s/super-computer-airevolutionx-RpneRv Microsoft just revealed MDASH, ...

📺 AI Revolution

👁️ 9K • 👍 461 • 💬 29 • ⏱️ 14:53 • 4h ago

---

**[Google&#39;s NEW AI Agent LEAKS are WILD!](https://www.youtube.com/watch?v=LyBcgVxZcoI)**

Want to make money and save time with AI? Join here: https://www.skool.com/ai-profit-lab-7462/about Video notes + links to the ...

📺 Julian Goldie SEO

👁️ 6K • 👍 89 • 💬 5 • ⏱️ 9:23 • 1d ago

---

**[I Tried 500+ AI Tools, These 6 Will Make You Serious Money](https://www.youtube.com/watch?v=8XRXIIpBpI0)**

These 6 AI Tools Make Real Money (I Tested 500+) Hey Friends :)) This video breaks down the six genuinely impactful AI tools ...

📺 Skai Generated

👁️ 7K • ⏱️ 12:37 • 11h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 22,483 • ❤️ 602 • 16h ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 783,564 • ❤️ 989 • 7d ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 11,725 • ❤️ 344 • 16h ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 141,203 • ❤️ 503 • 4d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 12,832 • ❤️ 241 • 9d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,766,621 • ❤️ 3,974 • 9d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 105,097 • ❤️ 171 • 21h ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 97,682 • ❤️ 150 • 21h ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 13,998 • ❤️ 381 • 19d ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles. It excels at generating illustrations and artistic images, with key capabilities including high-resolution output (up to 1536^2) and compatibility with ComfyUI workflows, making it ideal for digital artists and anime enthusiasts.

⬇️ 465,511 • ❤️ 1,329 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 72 • 💬 3 • ⭐ 75,779 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 6 • 💬 0 • ⭐ 17,365 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 25,088 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Pixal3D: Pixel-Aligned 3D Generation from Images](https://huggingface.co/papers/2605.10922)**

*Dong-Yang Li, Wang Zhao, Yuxin Chen et al. (8 authors)*

🏢 ARC Lab, Tencent PCG

Pixal3D introduces a pixel-aligned 3D generation approach that addresses fidelity issues in 3D asset creation by establishing direct pixel-to-3D correspondences through back-projection conditioning.

▲ 24 • 💬 3 • ⭐ 701 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.10922) • [💻 code](https://github.com/TencentARC/Pixal3D) • [🔗 project](https://ldyang694.github.io/projects/pixal3d/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 20 • 💬 3 • ⭐ 11,512 • 28d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://huggingface.co/papers/2605.13724)**

*Yuchao Gu, Guian Fang, Yuxin Jiang et al. (7 authors)*

🏢 NVIDIA

AnyFlow introduces a novel any-step video diffusion distillation framework that improves upon consistency distillation by optimizing full ODE sampling trajectories through flow-map transition learning and backward simulation techniques.

▲ 86 • 💬 1 • ⭐ 239 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.13724) • [💻 code](https://github.com/NVlabs/AnyFlow) • [🔗 project](https://nvlabs.github.io/AnyFlow/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 114 • 💬 10 • ⭐ 9,426 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[World Action Models: The Next Frontier in Embodied AI](https://huggingface.co/papers/2605.12090)**

*Siyin Wang, Junhao Shi, Zhaoyang Fu et al. (14 authors)*

🏢 OpenMOSS

World Action Models unify predictive state modeling with action generation for embodied policy learning, forming a cohesive framework for understanding environment dynamics and action prediction.

▲ 59 • 💬 1 • ⭐ 244 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.12090) • [💻 code](https://github.com/OpenMOSS/Awesome-WAM) • [🔗 project](https://openmoss.github.io/Awesome-WAM/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 63,175 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 73,666 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 13.0k • 🔱 3.0k • 18d ago

---

**[op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)**

AI-agent Skill for generating polished HTML slide decks: editorial magazine and Swiss layouts, image prompts, social covers, and a WebGL/low-power presentation runtime.

`HTML` `ai-agent` `claude-code` `codex` `html-deck` `image-generation`

⭐ 9.0k • 🔱 735 • 20m ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.0k • 🔱 877 • 9h ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 3.0k • 🔱 303 • 33m ago

---

**[esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)**

DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.

`TypeScript` `agent` `agent-framework` `ai-agent` `ai-coding` `cli`

⭐ 3.0k • 🔱 165 • 1m ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

A collection of agent skills for CAD, robotics and hardware design

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.9k • 🔱 342 • 1d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.3k • 🔱 150 • 1h ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.2k • 🔱 229 • 5d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.1k • 🔱 317 • 18h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.1k • 🔱 347 • 48m ago

---

---

*Generated by PeekDeck - A glance is all you need*
