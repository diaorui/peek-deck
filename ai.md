---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-14T14:51:36.917540+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 14, 2026 at 14:51 UTC  
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

**[Transformer co-author validates post-transformer cost efficiency breakthrough](https://www.reddit.com/r/artificial/comments/1vo5y3i/transformer_coauthor_validates_posttransformer/)**

https://preview.redd.it/frhws9cu1cjh1.png?width=1222&format=png&auto=webp&s=f3aa2f0bde64333c3fd4786a9b4c4e05a0c4e8f6 A 150-million-parameter model just redrew the ARC-AGI-1 cost-efficiency frontier. Btw, they show 600B scale retaining the recurrent latent reasoning capabilities. The result was evaluated by Łukasz Kaiser (co-author of the original Transformer paper), Remek Kinas (AI Researcher and co-creator of Bielik LLM) and Richard Zhong (NYU researcher) focused on model evaluation and benchmark robustness. ARC-AGI-1 is a public reasoning benchmark that tests whether a system can infer an underlying rule from a small number of examples and apply it to a new input, a capability often associated with human-like intelligence. Standard LLMs, despite their massive parameter counts, have historically struggled with ARC-AGI because it requires novel reasoning on unfamiliar problems. Transformers typically improve through brute-force scaling, which demands increasingly large amounts of compute. What these researchers have shown is that a non-transformer architecture can climb the ARC-AGI benchmark at a fraction of the compute cost of traditional models. Instead of relying on a standard attention-based Transformer stack and visible CoT, it uses recurrent memory and latent reasoning to achieve these strong results with drastically less compute. New architectures that deliver strong reasoning at low compute costs could change the economics of AI itself.

2h ago

---

**[I've built a fully autonomous meditation system for TouchDesigner](https://www.reddit.com/r/artificial/comments/1vo2kku/ive_built_a_fully_autonomous_meditation_system/)**

A new output from this experimental real-time BCI system for TouchDesigner; a Brain-Computer Interface pipeline that reads live EEG signals, classifies your mental state, and autonomously generates responsive AI video: a meditation guide that adapts to your brain activity, second by second. The system is built around OpenBCI (open-source hardware + software), but it's designed to work with most BCI headsets after a few pertinent tweaks to the OSC routing and channel-rename logic; Muse, Neurosity, BrainFlow-compatible devices, and others can all drive it. The architecture is deliberately modular: meditation is only one possible application. A knowledgeable user can repurpose the same EEG → interpretation → generative-response pipeline into entirely different audiovisual systems, interactive installations, performance tools, or other BCI-driven experiments. Accessible through both Patreon, and the Tools Store.

5h ago

---

**[New to AI](https://www.reddit.com/r/artificial/comments/1vo2xy9/new_to_ai/)**

Hi! I recently graduated high school and will be starting university this upcoming fall as an engineering major. Although I have used AI tools like Claude, ChatGPT etc but I lack experience (or any kind of knowledge) about how to make my own AI models and AI ethics. I just wanted to ask for some guidance from people who are already experienced in this field if there are classes/courses they recommend I take. I have some free time before university starts so I want to build some projects and kind of develop my skills especially for engineering internships later on since I am in a competitive field. I'd appreciate any advice for someone who is just starting out!

4h ago

---

**[When the smartest AI model is actually a terrible business move](https://www.reddit.com/r/artificial/comments/1vo13up/when_the_smartest_ai_model_is_actually_a_terrible/)**

I came across this article that flips the script on AI hype: sometimes the most advanced models are the worst for business. High costs, misaligned incentives, and ethical risks can turn a technical win into a strategic loss. Have you seen this play out in your work or industry? (Not affiliated, just thought it was a refreshing take.) [Source: https://www.hitechies.com/ai-smartest-model-worst-business-decision/\]

6h ago

---

**[How well do AI voice agents handle people who constantly interrupt?](https://www.reddit.com/r/artificial/comments/1vnqdgc/how_well_do_ai_voice_agents_handle_people_who/)**

This is a thing I keep noticing in real customer calls that doesn’t really show up in voice AI demos. People interrupt constantly. They start answering before the question is finished, correct themselves halfway through a sentence, say 'wait actually…' and completely change what they were asking about. That’s normal when two people are talking but it seems like a pretty difficult problem for an AI voice agent because it has to know whether the customer is adding context, correcting something or trying to stop the current response entirely. We’re looking at enterprise voice AI for longer customer service conversations and I’m beginning to wonder if turn taking is as important as natural voice. For anyone testing conversational AI over the phone, how are you testing interruptions? Is this still something customers notice pretty quickly?

15h ago

---

**[Realized there's a name for the thing I kept doing wrong in AI debugging sessions: confusing "symptom resolved" with "cause found"](https://www.reddit.com/r/artificial/comments/1vo4pwa/realized_theres_a_name_for_the_thing_i_kept_doing/)**

Kept running into a specific failure pattern across different AI-assisted debugging sessions and didn't have a clean way to describe it until I actually sat down and compared a few of them side by side. The pattern: an error goes away, I file the problem as solved, and sometime later the same underlying issue resurfaces wearing a different symptom. Turns out those are two separate claims that get treated as one by default. "The error is gone" only tells you the symptom stopped being visible. "The bug is fixed" requires the actual mechanism to have been addressed, and a model asked to make an error disappear will happily do exactly that, a wider try/catch, a retry wrapped around a flaky call, both of which satisfy the first claim while leaving the second completely unverified. What made this click was a case where a retry "fixed" what looked like a flaky database write, only for the same class of failure to show up two weeks later under a different error message. Root cause was duplicate event delivery hitting a handler that wasn't idempotent, something the retry had no way of addressing because nothing in the original context suggested duplication was even possible. The uncomfortable part: generating a fix and validating one are genuinely different skills, and almost every debugging workflow, AI-assisted or not, only exercises the first. Asking "does this make the error go away" is satisfying and fast. Asking "does this address the actual mechanism, and what did it silently change that I didn't ask for" is slower and easy to skip specifically because the first question already felt like progress. Wrote up the specific case and the sequence I now run before trusting a fix, generation and validation treated as separate steps instead of one motion: https://medium.com/@nagatomopedro05/why-your-ai-debugging-sessions-keep-going-in-circles-e645c35479c6 Curious if others have caught this same gap in their own process, a fix that technically resolves the error shown to the model while leaving the actual cause completely untouched.

3h ago

---

**[If an AI agent can hack systems during testing, should we be treating agents like security principals?](https://www.reddit.com/r/artificial/comments/1vnz5p3/if_an_ai_agent_can_hack_systems_during_testing/)**

Recent security testing involving AI models has raised an interesting question: we're no longer only worried about models generating insecure code—the models themselves can potentially perform complex actions when connected to tools and systems. Meta recently acknowledged that one of its AI models hacked another company during controlled cybersecurity testing. That makes me wonder whether traditional application security assumptions are enough for agentic systems. If an AI agent has access to: source code cloud infrastructure databases APIs credentials internal documents Should the agent itself be treated like a privileged user/service account? What controls should enterprises require before giving an agent meaningful production access? Least privilege? Sandboxing? Approval gates? Continuous monitoring? Separate agent identities? Where would you draw the line?

8h ago

---

**[Can face-matching networks prevent identity fraud without becoming surveillance systems?](https://www.reddit.com/r/artificial/comments/1vo729f/can_facematching_networks_prevent_identity_fraud/)**

New South Wales is considering joining Australia’s national face-matching network. The proposal would allow driver’s licence and photo-card images to be checked when someone’s identity needs to be confirmed. The practical benefit is easy to understand. If someone tries to open a bank account using documents stolen in a data breach, face matching could help identify that the person doesn’t match the real owner. The concern is what happens once a searchable system like this exists. The same legislative package would also give police access to unredacted images from certain toll-road cameras for serious investigations and missing-person cases. Both uses can sound reasonable on their own, but systems like this often become more controversial as their scope grows. Can face matching be used safely with strict access rules, limited retention, and independent oversight? Or does a national network inevitably become a surveillance system over time?

1h ago

---

**[The most useful AI skill in 2026 isn't prompting or agents. It's knowing when NOT to use AI](https://www.reddit.com/r/artificial/comments/1vo6h13/the_most_useful_ai_skill_in_2026_isnt_prompting/)**

Every day I see someone bolt an LLM onto something a shell script did better. The best AI practitioners I know are the ones who draw the line early: - Deterministic task, fixed rules? Script it. - One-off analysis with judgment? Ask a human or a cheap model. - Open-ended, branching, context-heavy? Now AI earns its keep. The $0 automation stack I run uses AI for exactly one step (summarizing news) and plain code for everything else. That's the whole secret: AI where it compounds, code where it doesn't. What's something you tried to do with AI that you now do without it?

1h ago

---

**[Same demo, two failures on DeepSeek V4 Pro 0813, then V4 Flash finished it](https://www.reddit.com/r/artificial/comments/1vo5x4i/same_demo_two_failures_on_deepseek_v4_pro_0813/)**

I only did a quick first test of DeepSeek V4 Pro 0813 tonight, so take this as a tiny sample, not a verdict. The first Pro run failed. I put the same demo through Flash, and Flash completed it. I honestly did not expect that result, so I ran Pro a second time before writing this. Same failure. The odd part is that it did not feel slow while generating. I was seeing roughly 80 to 90 tokens/s tonight. That looks fine on a counter, but it matters a lot less when the demo itself does not make it across the line. For my next pass, I will put the same requests through ZenMux and record the model route and provider with each request. That makes the comparison easier to inspect. It still does not turn two failed runs into a benchmark. My first impression is negative. Two runs are nowhere near enough for a broad claim, but two failures on a demo that Flash completed are worth writing down. What are people seeing right now with V4 Pro 0813? If you tested it against Flash, did you keep the same prompt and setup, and did Pro actually finish the demo?

2h ago

---

---

## Google News: "ai"

**[EXCLUSIVE: Apple trains its own AI model for China market with Alibaba's support, sources say](https://www.reuters.com/business/retail-consumer/apple-trains-its-own-ai-model-china-market-with-alibabas-support-sources-say-2026-08-14/)**

Reuters • 10h ago

---

**[Apple trained its own AI model for China with help from Alibaba](https://www.theverge.com/ai-artificial-intelligence/980160/apple-intelligence-china-custom-ai-model-alibaba)**

﻿The rare US-China partnership comes as Apple prepares to roll out its on-device generative AI service in China.

The Verge • 5h ago

---

**[Apple Develops China-Specific AI Model With Alibaba Support, Reuters Reports](https://finance.yahoo.com/technology/ai/articles/apple-develops-china-specific-ai-101429816.html)**

Apple Inc (NASDAQ:AAPL) has trained its own large language model specifically for the Chinese market with assistance from Alibaba (NYSE:BABA), Reuters reported on Friday, signalling a change in the technology giant’s approach to introducing artificial intelligence services in China. The development could give Apple greater control over its AI technology as it prepares to bring Apple Intelligence to Chinese users.

finance.yahoo.com • 4h ago

---

**[OpenAI and Anthropic in price war as Chinese AI rivals gain ground](https://www.ft.com/content/32a70a3c-7d28-40b4-808e-36edb58c7d01?syn-25a6b1a6=1)**

US groups release cheaper models after new challenges to their trillion-dollar ambitions

Financial Times • 10h ago

---

**[SMIC Q2 2026 earnings beat as AI demand drives price increases](https://qz.com/smic-chip-prices-ai-demand-revenue-earnings-081426)**

SMIC's second-quarter revenue hit $3 billion for the first time, rising 36% from a year earlier, as the company raised wafer prices and shipments climbed

qz.com • 1h ago

---

**[Hidden costs are enterprise AI’s next challenge](https://www.fastcompany.com/91589451/hidden-costs-are-enterprise-ais-next-challenge)**

fastcompany.com • 1h ago

---

**[Data breach notices are surging past last year's record as AI-powered attacks rise](https://qz.com/data-breach-victim-notices-2026-record-ai-attacks-081426)**

More than 471 million victim notices were issued in the first half of 2026, compared with 297.5 million for all of last year

qz.com • 1h ago

---

**[Opinion | These A.I. Policies Will Hurt Our Business. We Should Do Them Anyway.](https://www.nytimes.com/2026/08/14/opinion/ai-policy-tax-technology.html)**

nytimes.com • 5h ago

---

**[As online dating goes into ‘salvage mode’, can AI solve all its problems?](https://www.theguardian.com/lifeandstyle/2026/aug/14/online-dating-salvage-mode--ai-bumble-app)**

Dating apps such as Bumble forced to adapt as ‘swipe fatigue’ grows

The Guardian • 1h ago

---

**[Introducing Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/)**

Gemini 3.7 Flash is our most intelligent workhorse model yet for coding and agents.

blog.google • 21h ago

---

---

## HackerNews: "ai"

**[AI is removing the middle class of software engineering?](https://news.ycombinator.com/item?id=49271994)**

AI makes projects with weak engineering culture fail much faster.

⬆️ 978 • 💬 904 • 2d ago • [Blog - Florian Herrengt](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html)

---

**[Go is an ideal language for AI-assisted software engineering](https://news.ycombinator.com/item?id=49261133)**

As AI shifts software engineering from writing to reviewing, discover how Go's strict compiler and unified toolchain ensure reliable AI-generated code.

⬆️ 436 • 💬 530 • 2d ago • [developers.googleblog.com](https://developers.googleblog.com/why-go-is-an-ideal-language-for-ai-assisted-software-engineering/)

---

**[Someone is running mass vulnerability scans, spoofing AI bots like ClaudeBot](https://news.ycombinator.com/item?id=49272569)**

A continuously updating analysis of bot vs. human traffic, AI scraping, fetching, search indexing, browsing, robots.txt compliance, and AI chat referrals across 5,000+ websites.

⬆️ 301 • 💬 226 • 2d ago • [Known Agents](https://knownagents.com/insights)

---

**[US hires over 2k video gamers as air traffic controllers](https://news.ycombinator.com/item?id=49265879)**

Transportation Secretary Sean Duffy is touting the success of a campaign targeting video gamers to train as air traffic controllers.

⬆️ 210 • 💬 159 • 2d ago • [CBS News](https://www.cbsnews.com/news/video-gamer-air-traffic-controllers-faa-recruitment-sean-duffy/)

---

**[Choosing an AI model: one prompt, 11 models, different results](https://news.ycombinator.com/item?id=49285327)**

Netlify now runs any OpenRouter model, including Kimi K3, GLM 5.2 and DeepSeek V4. We tested 11 of them on the same build prompt to see how they differ.

⬆️ 208 • 💬 88 • 1d ago • [netlify.com](https://www.netlify.com/blog/one-prompt-11-models-very-different-results/)

---

**[Company Offering '100% Human-Written, Never AI' Medical Research Is 100% AI](https://news.ycombinator.com/item?id=49267057)**

Research Gold's team of human methodologists are either AI generated or using the identity of real people without their permission

⬆️ 196 • 💬 51 • 2d ago • [404 Media](https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/)

---

**[AI agents lie, cheat and steal. That is putting off users](https://news.ycombinator.com/item?id=49285604)**

⬆️ 163 • 💬 199 • 1d ago • [economist.com](https://www.economist.com/business/2026/08/12/ai-agents-lie-cheat-and-steal-that-is-putting-off-users)

---

**[Launch HN: Discovered Materials (YC P26) – AI agents to discover new materials](https://news.ycombinator.com/item?id=49269090)**

Measuring frontier model ability to discover new materials for the semiconductor industry — candidates verified by DFT and attempted in a real lab.

⬆️ 158 • 💬 35 • 2d ago • [Discovered Materials](https://discoveredmaterials.com/research/)

---

**[Text AI watermarks will always be trivial to remove](https://news.ycombinator.com/item?id=49287153)**

⬆️ 133 • 💬 159 • 23h ago • [seangoedecke.com](https://www.seangoedecke.com/text-ai-watermarks/)

---

**[Heart aerospace completes first flight of largest electric aircraft](https://news.ycombinator.com/item?id=49286270)**

Heart Aerospace’s X1 demonstrator became the world’s largest battery-electric aircraft ever flown, demonstrating electric flight at airliner scale and advancing development of the ES-30.

⬆️ 133 • 💬 144 • 1d ago • [Heart Aerospace](https://www.heartaerospace.com/newsroom/heart-aerospace-completes-first-flight-of-world-s-largest-electric-aircraft)

---

---

## YouTube Videos: "ai"

**[Anthropic Accidentally Created An AI Turf War](https://www.youtube.com/watch?v=sY2BE_AjqPE)**

Anthropic put AI agents together with conflicting goals and watched them escalate into sabotage - deleting accounts, disguising ...

📺 AI Revolution

👁️ 10K • 👍 463 • 💬 43 • ⏱️ 16:41 • 14h ago

---

**[Elon&#39;s own words just exposed AI bubble](https://www.youtube.com/watch?v=7QPrefKv4zw)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 127K • 👍 5K • 💬 2K • ⏱️ 17:04 • 1d ago

---

**[I built my first local AI agent](https://www.youtube.com/watch?v=PvGr7tm0Hes)**

In this video Adam works with Wendell from @Level1Techs to set up his first local AI agent using an MSI Cubi NUC and a ...

📺 PCWorld

👁️ 7K • 👍 385 • 💬 44 • ⏱️ 19:47 • 20h ago

---

**[YOU WILL PAY For Inevitable AI Bailout](https://www.youtube.com/watch?v=GjBJLdQ7uRI)**

Krystal and Saagar discuss discuss the incoming hidden AI bailout plot. Sign Up For 30 Day Free BP Trial: ...

📺 Breaking Points

👁️ 194K • 👍 5K • 💬 650 • ⏱️ 13:12 • 2d ago

---

**[AI Just Hacked a Government... And Its Nuclear Agency!](https://www.youtube.com/watch?v=VKhW4QnQMts)**

AI agents just ran a four-day cyber attack on a government with nobody at the keyboard - mapping 21 systems, cracking 85 ...

📺 AI Revolution

👁️ 31K • 👍 1K • 💬 125 • ⏱️ 17:01 • 1d ago

---

**[AI voting images shouldn&#39;t be allowed.](https://www.youtube.com/watch?v=5oDqBhmTfH0)**

aivideo #ai #chatgpt #news #politicsA recent study found that six of the most widely used AI chatbots were able to generate ...

📺 Jeremy Carrasco

👁️ 10K • 👍 2K • 💬 64 • ⏱️ 1:32 • 16h ago

---

**[This AI Got Exposed 💀](https://www.youtube.com/watch?v=58eDL1Us1kM)**

The AI character tom.rhoe went viral for making it look like he transformed his body at 64 years old. Then they got exposed when ...

📺 Mappelz

👁️ 898K • 👍 46K • 💬 173 • ⏱️ 0:33 • 18h ago

---

**[DC Used AI For Supergirl…](https://www.youtube.com/watch?v=szprp4wDOTk)**

In this video, we learn DC revealed they used AI for Supergirl… Follow Me On Social Media: Instagram: @therealdoomblazer ...

📺 DoomBlazer

👁️ 80K • 👍 11K • 💬 702 • ⏱️ 2:27 • 10h ago

---

**[The 7 Trillion AI Gamble Is Failing. Big Tech is TRAPPED Right NOW.](https://www.youtube.com/watch?v=OunJtLnyPT4)**

Tech CEOs are quietly cancelling their AI plans, and the reason isn't that artificial intelligence stopped working. It's that companies ...

📺 The Infographics Show

👁️ 1.2M • 👍 23K • 💬 3K • ⏱️ 25:41 • 2d ago

---

**[Say THIS to Destroy AI Bot Callers](https://www.youtube.com/watch?v=fhi6JU5pOJk)**

Destroying AI bot scam calls is hilarious, and pretty easy! ▻ Kraken Partnership: https://kraken.com/kitboga 0:00 AI Scam Calls ...

📺 Kitboga

👁️ 1.1M • 👍 65K • 💬 6K • ⏱️ 17:04 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 165,300 • ❤️ 1,480 • 2d ago

---

**[Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)**

*Qwen*

Qwen3.8-2.4T-A95B is a 2.4T parameter causal language model with 95B activated parameters, excelling in coding, professional tasks, research, and long-horizon agentic applications. It features a 262K native context length, flexible thinking control, and improved agent execution for complex, multi-step task completion.

`text-generation` `2446.2B`

⬇️ 3,832 • ❤️ 877 • 2d ago

---

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 1,997,541 • ❤️ 3,892 • 1d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 207,830 • ❤️ 803 • 2d ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 63 • ❤️ 564 • 3h ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 1,606,491 • ❤️ 3,364 • 13d ago

---

**[Minimax-h3-Turbo](https://huggingface.co/lightx2v/Minimax-h3-Turbo)**

*Lightx2v*

Minimax-h3-Turbo is a diffusion model for image-to-video generation, capable of producing high-quality videos from static images with controllable motion. It is primarily used for creative video editing and content creation, enabling users to animate still images.

`image-to-video`

⬇️ 149,865 • ❤️ 485 • 22h ago

---

**[Muse-Glimmer-30B-GGUF](https://huggingface.co/unsloth/Muse-Glimmer-30B-GGUF)**

*Unsloth AI*

Muse-Glimmer-30B-GGUF is a 30B parameter multimodal LLM optimized for local agentic tasks, featuring reliable tool use, multi-step reasoning, and failure recovery. It processes interleaved text and images, supporting multilingual inputs and controllable effort for efficient deployment on consumer hardware.

`image-text-to-text` `27.9B`

⬇️ 596,774 • ❤️ 404 • 3d ago

---

**[DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)**

*DeepSeek*

DeepSeek-V4-Pro-0813 is a powerful text generation model with enhanced agentic capabilities and DSpark speculative decoding for improved production performance. It excels in complex reasoning, coding, and tool-use tasks, outperforming previous versions and competing with leading proprietary models.

`text-generation` `1650.5B`

⬇️ 245 • ❤️ 400 • 22h ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 11,768,622 • ❤️ 1,311 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 597 • 💬 2 • ⭐ 1,735 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 122 • 💬 4 • ⭐ 98,087 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 124 • 💬 3 • ⭐ 21,517 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 52 • 💬 4 • ⭐ 37,128 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[MatrAIx: Simulating the World with 8.3 Billion Persona Agents](https://huggingface.co/papers/2608.04205)**

*Xiaomin Li, Yuexing Hao, Jianheng Hou et al. (93 authors)*

🏢 MatrAIx

MatrAIx is a large-scale simulated-user evaluation framework that uses diverse persona records and interactive environments to test AI systems across many domains.

▲ 37 • 💬 2 • ⭐ 1,015 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2608.04205) • [💻 code](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) • [🔗 project](https://matraix.ai/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 80 • 💬 6 • ⭐ 23,725 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

JoyAI-Video-Edit is a 16B-parameter autoregressive diffusion framework that enables real-time, open-ended video editing with high source fidelity and long-term temporal consistency on a single GPU.

▲ 92 • 💬 1 • ⭐ 1,146 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233)**

*Yoav HaCohen, Benny Brazowski, Nisan Chiprut et al. (29 authors)*

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.

▲ 187 • 💬 9 • ⭐ 9,000 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.03233) • [💻 code](https://github.com/Lightricks/LTX-2) • [🔗 project](https://app.ltx.studio/ltx-2-playground/i2v)

---

**[HuggingFace's Transformers: State-of-the-art Natural Language Processing](https://huggingface.co/papers/1910.03771)**

*Thomas Wolf, Lysandre Debut, Victor Sanh et al. (22 authors)*

🏢 Hugging Face

Transformers library provides state-of-the-art Transformer architectures and pretrained models for natural language processing tasks with a unified API and emphasis on extensibility and robust deployment.

▲ 27 • 💬 7 • ⭐ 164,107 • 83mo ago

[🎓 arXiv](https://arxiv.org/abs/1910.03771) • [💻 code](https://github.com/huggingface/transformers) • [🔗 project](https://huggingface.co)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 84,014 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 13.5k • 🔱 1.6k • 11h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.4k • 🔱 991 • 14h ago

---

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `c2pa` `claude` `provenance`

⭐ 7.0k • 🔱 759 • 11m ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 5.0k • 🔱 429 • 10h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 4.0k • 🔱 515 • 6d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.0k • 🔱 533 • 1d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.7k • 🔱 223 • 2d ago

---

**[MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.7k • 🔱 1.9k • 6h ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.4k • 🔱 185 • 2d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.1k • 🔱 170 • 23h ago

---

---

*Generated by PeekDeck - A glance is all you need*
