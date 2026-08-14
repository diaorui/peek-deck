---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-14T21:24:57.324851+00:00'
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

**Last Updated:** August 14, 2026 at 21:24 UTC  
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

**[I've built a fully autonomous meditation system for TouchDesigner](https://www.reddit.com/r/artificial/comments/1vo2kku/ive_built_a_fully_autonomous_meditation_system/)**

A new output from this experimental real-time BCI system for TouchDesigner; a Brain-Computer Interface pipeline that reads live EEG signals, classifies your mental state, and autonomously generates responsive AI video: a meditation guide that adapts to your brain activity, second by second. The system is built around OpenBCI (open-source hardware + software), but it's designed to work with most BCI headsets after a few pertinent tweaks to the OSC routing and channel-rename logic; Muse, Neurosity, BrainFlow-compatible devices, and others can all drive it. The architecture is deliberately modular: meditation is only one possible application. A knowledgeable user can repurpose the same EEG → interpretation → generative-response pipeline into entirely different audiovisual systems, interactive installations, performance tools, or other BCI-driven experiments. Accessible through both Patreon, and the Tools Store.

11h ago

---

**[New to AI](https://www.reddit.com/r/artificial/comments/1vo2xy9/new_to_ai/)**

Hi! I recently graduated high school and will be starting university this upcoming fall as an engineering major. Although I have used AI tools like Claude, ChatGPT etc but I lack experience (or any kind of knowledge) about how to make my own AI models and AI ethics. I just wanted to ask for some guidance from people who are already experienced in this field if there are classes/courses they recommend I take. I have some free time before university starts so I want to build some projects and kind of develop my skills especially for engineering internships later on since I am in a competitive field. I'd appreciate any advice for someone who is just starting out!

11h ago

---

**[LiquidAI LFM2.5-VL-3B: a 3.1B local VLM that beats Gemma-4 E4B — screen understanding 2.5 → 82.2](https://www.reddit.com/r/artificial/comments/1vodx2x/liquidai_lfm25vl3b_a_31b_local_vlm_that_beats/)**

LiquidAI LFM2.5-VL-3B: a 3.1B local VLM that beats Gemma-4 E4B — screen understanding 2.5 → 82.2 TL;DR: LiquidAI released LFM2.5-VL-3B, a 3.1B vision-language model that runs fully local (llama.cpp, MLX, vLLM, even a WebGPU demo). • Beats Gemma-4 E4B (8B) 69.4 vs 59.7; edges Qwen3.5-4B • Screen understanding: 2.5 → 82.2 on ScreenSpot-v2 Web (huge jump) • 228 tok/s on M5 Max, 20 tok/s on a Galaxy S26 Ultra • Function calling / object grounding included What I found interesting is the business angle: for simple document/screen tasks, local AI flips 'AI feature' from a monthly API bill into a one-time engineering task with zero data leaving the building. Big cloud models still win for complex reasoning — this just made the small-model bucket genuinely usable. I wrote a short analysis here: https://www.zyntopia.com/news/lfm2-5-vl-3b-edge-vision

3h ago

---

**[When the smartest AI model is actually a terrible business move](https://www.reddit.com/r/artificial/comments/1vo13up/when_the_smartest_ai_model_is_actually_a_terrible/)**

I came across this article that flips the script on AI hype: sometimes the most advanced models are the worst for business. High costs, misaligned incentives, and ethical risks can turn a technical win into a strategic loss. Have you seen this play out in your work or industry? (Not affiliated, just thought it was a refreshing take.) [Source: https://www.hitechies.com/ai-smartest-model-worst-business-decision/\]

13h ago

---

**[🚀 New version of Android Remote Control MCP released! Let your AI agent control your phone, now with on-device PII redaction! 🛡️ No cables or root needed!](https://www.reddit.com/r/artificial/comments/1voafib/new_version_of_android_remote_control_mcp/)**

🚀 New release of Android Remote Control MCP is out — the MCP server that runs on your phone and gives your AI agent the ability to use any app you want! Grab it here: https://github.com/danielealbano/android-remote-control-mcp/releases/tag/v1.11.0 My favorite part of this release? The Privacy Mode 🛡️! Recently I was told by an user "it's a good project but I don't want Anthropic to know everything about me" and it's a very fair point! The LLM providers see and record everything they receive … including your emails, phone numbers and credit cards! Well, not anymore! With Privacy Mode all of that gets detected and redacted locally, on the phone, before anything leaves the device (about 87% of PII caught on my benchmark on emails, phone numbers, credit cards, IBANs, national IDs, …), and the agent keeps working normally because it sees placeholders: the real values get substituted back on-device. Unfortunately the only weak spot for now are non English names but I am working on it! The full per-category numbers and the benchmark are in the repo, measured, not guessed. Also, Android loves killing background services… the server now survives app updates, swipe-away and Doze, with a one-tap battery optimization exemption 🔋 No more dead server halfway through a task! In addition a few minor improvements: the app now notifies you when a new version is out, MCP clients only see the tools that will actually work on your device (no more camera tools without camera permission), and a fully reworked server logs page. What can you actually do with it? Book a flight on Skyscanner, post on Reddit, order groceries, book a dinner… and now with your personal data staying on your phone.

5h ago

---

**[How well do AI voice agents handle people who constantly interrupt?](https://www.reddit.com/r/artificial/comments/1vnqdgc/how_well_do_ai_voice_agents_handle_people_who/)**

This is a thing I keep noticing in real customer calls that doesn’t really show up in voice AI demos. People interrupt constantly. They start answering before the question is finished, correct themselves halfway through a sentence, say 'wait actually…' and completely change what they were asking about. That’s normal when two people are talking but it seems like a pretty difficult problem for an AI voice agent because it has to know whether the customer is adding context, correcting something or trying to stop the current response entirely. We’re looking at enterprise voice AI for longer customer service conversations and I’m beginning to wonder if turn taking is as important as natural voice. For anyone testing conversational AI over the phone, how are you testing interruptions? Is this still something customers notice pretty quickly?

22h ago

---

**[Realized there's a name for the thing I kept doing wrong in AI debugging sessions: confusing "symptom resolved" with "cause found"](https://www.reddit.com/r/artificial/comments/1vo4pwa/realized_theres_a_name_for_the_thing_i_kept_doing/)**

Kept running into a specific failure pattern across different AI-assisted debugging sessions and didn't have a clean way to describe it until I actually sat down and compared a few of them side by side. The pattern: an error goes away, I file the problem as solved, and sometime later the same underlying issue resurfaces wearing a different symptom. Turns out those are two separate claims that get treated as one by default. "The error is gone" only tells you the symptom stopped being visible. "The bug is fixed" requires the actual mechanism to have been addressed, and a model asked to make an error disappear will happily do exactly that, a wider try/catch, a retry wrapped around a flaky call, both of which satisfy the first claim while leaving the second completely unverified. What made this click was a case where a retry "fixed" what looked like a flaky database write, only for the same class of failure to show up two weeks later under a different error message. Root cause was duplicate event delivery hitting a handler that wasn't idempotent, something the retry had no way of addressing because nothing in the original context suggested duplication was even possible. The uncomfortable part: generating a fix and validating one are genuinely different skills, and almost every debugging workflow, AI-assisted or not, only exercises the first. Asking "does this make the error go away" is satisfying and fast. Asking "does this address the actual mechanism, and what did it silently change that I didn't ask for" is slower and easy to skip specifically because the first question already felt like progress. Wrote up the specific case and the sequence I now run before trusting a fix, generation and validation treated as separate steps instead of one motion: https://medium.com/@nagatomopedro05/why-your-ai-debugging-sessions-keep-going-in-circles-e645c35479c6 Curious if others have caught this same gap in their own process, a fix that technically resolves the error shown to the model while leaving the actual cause completely untouched.

9h ago

---

**[Can face-matching networks prevent identity fraud without becoming surveillance systems?](https://www.reddit.com/r/artificial/comments/1vo729f/can_facematching_networks_prevent_identity_fraud/)**

New South Wales is considering joining Australia’s national face-matching network. The proposal would allow driver’s licence and photo-card images to be checked when someone’s identity needs to be confirmed. The practical benefit is easy to understand. If someone tries to open a bank account using documents stolen in a data breach, face matching could help identify that the person doesn’t match the real owner. The concern is what happens once a searchable system like this exists. The same legislative package would also give police access to unredacted images from certain toll-road cameras for serious investigations and missing-person cases. Both uses can sound reasonable on their own, but systems like this often become more controversial as their scope grows. Can face matching be used safely with strict access rules, limited retention, and independent oversight? Or does a national network inevitably become a surveillance system over time?

8h ago

---

**[The most useful AI skill in 2026 isn't prompting or agents. It's knowing when NOT to use AI](https://www.reddit.com/r/artificial/comments/1vo6h13/the_most_useful_ai_skill_in_2026_isnt_prompting/)**

Every day I see someone bolt an LLM onto something a shell script did better. The best AI practitioners I know are the ones who draw the line early: - Deterministic task, fixed rules? Script it. - One-off analysis with judgment? Ask a human or a cheap model. - Open-ended, branching, context-heavy? Now AI earns its keep. The $0 automation stack I run uses AI for exactly one step (summarizing news) and plain code for everything else. That's the whole secret: AI where it compounds, code where it doesn't. What's something you tried to do with AI that you now do without it?

8h ago

---

**[Same demo, two failures on DeepSeek V4 Pro 0813, then V4 Flash finished it](https://www.reddit.com/r/artificial/comments/1vo5x4i/same_demo_two_failures_on_deepseek_v4_pro_0813/)**

I only did a quick first test of DeepSeek V4 Pro 0813 tonight, so take this as a tiny sample, not a verdict. The first Pro run failed. I put the same demo through Flash, and Flash completed it. I honestly did not expect that result, so I ran Pro a second time before writing this. Same failure. The odd part is that it did not feel slow while generating. I was seeing roughly 80 to 90 tokens/s tonight. That looks fine on a counter, but it matters a lot less when the demo itself does not make it across the line. For my next pass, I will put the same requests through ZenMux and record the model route and provider with each request. That makes the comparison easier to inspect. It still does not turn two failed runs into a benchmark. My first impression is negative. Two runs are nowhere near enough for a broad claim, but two failures on a demo that Flash completed are worth writing down. What are people seeing right now with V4 Pro 0813? If you tested it against Flash, did you keep the same prompt and setup, and did Pro actually finish the demo?

8h ago

---

---

## Google News: "ai"

**[Amazon and Alphabet’s Profits Reveal Circular Nature of A.I. Boom](https://www.nytimes.com/2026/08/14/business/ai-tech-profits.html)**

The New York Times • 6h ago

---

**[As online dating goes into ‘salvage mode’, can AI solve all its problems?](https://www.theguardian.com/lifeandstyle/2026/aug/14/online-dating-salvage-mode--ai-bumble-app)**

Dating apps such as Bumble forced to adapt as ‘swipe fatigue’ grows

The Guardian • 4h ago

---

**[Goldman’s latest cash cow is all about funding the AI infrastructure boom](https://www.cnbc.com/2026/08/14/goldmans-latest-cash-cow-is-all-about-funding-the-ai-infrastructure-boom.html)**

Nvidia and Intel recently tapped the bank to help them meeting soaring demand for compute.

CNBC • 1h ago

---

**[Thrive’s Joshua Kushner chides Silicon Valley VCs over AI euphoria](https://techcrunch.com/2026/08/14/thrives-joshua-kushner-chides-silicon-valley-vcs-over-ai-euphoria/)**

The AI opportunity is huge but "it would also be a grave error in our minds to let excitement weaken our investment discipline," Kushner warns in his first-ever investment letter.

techcrunch.com • 1h ago

---

**[Anthropic CEO's wife once asked Jeffrey Epstein to fund porn venture — now she helps steer the Claude AI empire](https://nypost.com/2026/08/14/business/anthropic-ceos-wife-once-asked-jeffrey-epstein-to-fund-porn-venture-now-she-helps-steer-the-claude-ai-empire/)**

Before she became a key voice in her husband’s ear, Cami Clark reportedly pitched Epstein on a “free luxury porn” company.

New York Post • 1h ago

---

**[Even Claude Is in the Dark About Dario Amodei’s Wife—and Her Influence at Anthropic](https://www.wsj.com/tech/ai/claude-dario-amodei-wife-anthropic-e1eeda7d)**

WSJ • 20h ago

---

**[Mad Money’s Jim Cramer Says These 6 AI Stocks are Primed to Surge](https://finance.yahoo.com/markets/stocks/articles/mad-money-jim-cramer-says-192419592.html)**

Mad Money Host Jim Cramer named 6 AI data center stocks after Wednesday's rally. See how each has performed in 2026.

Yahoo Finance • 1d ago

---

**[OpenAI talent exodus raises 'huge red flag' ahead of IPO](https://www.cnbc.com/2026/08/14/open-ai-ipo-red-flag.html)**

OpenAI's C-suite turnover gives investors another reason for concern as the company pushes toward a mammoth IPO.

CNBC • 5h ago

---

**[It May Be Time to Panic About AI](https://www.theatlantic.com/technology/2026/08/openai-hacks-panic/688264/)**

Bots are starting to conspire with one another. Can they be reeled back in?

theatlantic.com • 2d ago

---

**[OpenAI and Anthropic in price war as Chinese AI rivals gain ground](https://www.ft.com/content/32a70a3c-7d28-40b4-808e-36edb58c7d01?syn-25a6b1a6=1)**

US groups release cheaper models after new challenges to their trillion-dollar ambitions

Financial Times • 17h ago

---

---

## HackerNews: "ai"

**[AI is removing the middle class of software engineering?](https://news.ycombinator.com/item?id=49271994)**

AI makes projects with weak engineering culture fail much faster.

⬆️ 982 • 💬 914 • 2d ago • [Blog - Florian Herrengt](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html)

---

**[Someone is running mass vulnerability scans, spoofing AI bots like ClaudeBot](https://news.ycombinator.com/item?id=49272569)**

A continuously updating analysis of bot vs. human traffic, AI scraping, fetching, search indexing, browsing, robots.txt compliance, and AI chat referrals across 5,000+ websites.

⬆️ 302 • 💬 226 • 2d ago • [Known Agents](https://knownagents.com/insights)

---

**[Choosing an AI model: one prompt, 11 models, different results](https://news.ycombinator.com/item?id=49285327)**

Netlify now runs any OpenRouter model, including Kimi K3, GLM 5.2 and DeepSeek V4. We tested 11 of them on the same build prompt to see how they differ.

⬆️ 213 • 💬 94 • 1d ago • [netlify.com](https://www.netlify.com/blog/one-prompt-11-models-very-different-results/)

---

**[US hires over 2k video gamers as air traffic controllers](https://news.ycombinator.com/item?id=49265879)**

Transportation Secretary Sean Duffy is touting the success of a campaign targeting video gamers to train as air traffic controllers.

⬆️ 210 • 💬 159 • 2d ago • [CBS News](https://www.cbsnews.com/news/video-gamer-air-traffic-controllers-faa-recruitment-sean-duffy/)

---

**[Company Offering '100% Human-Written, Never AI' Medical Research Is 100% AI](https://news.ycombinator.com/item?id=49267057)**

Research Gold's team of human methodologists are either AI generated or using the identity of real people without their permission

⬆️ 196 • 💬 51 • 2d ago • [404 Media](https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/)

---

**[Dear people who work at the airport](https://news.ycombinator.com/item?id=49297801)**

I would like you to know that we passengers are trying our best.

To you, this place makes sense -- you come here every day.  You speak the lingo.  You kno...

⬆️ 181 • 💬 235 • 9h ago • [Life after SSRI](https://life-after-ssri.bearblog.dev/dear-people-who-work-at-the-airport/)

---

**[AI agents lie, cheat and steal. That is putting off users](https://news.ycombinator.com/item?id=49285604)**

⬆️ 163 • 💬 203 • 1d ago • [economist.com](https://www.economist.com/business/2026/08/12/ai-agents-lie-cheat-and-steal-that-is-putting-off-users)

---

**[When Genius Fails: The Intellectual Arrogance of the AI Labs](https://news.ycombinator.com/item?id=49299282)**

From Situational Awareness’s Blow-up to Materials Science to the HuggingFace Hack

⬆️ 163 • 💬 175 • 6h ago • [weightythoughts.com](https://weightythoughts.com/p/when-genius-failsthe-intellectual)

---

**[Launch HN: Discovered Materials (YC P26) – AI agents to discover new materials](https://news.ycombinator.com/item?id=49269090)**

Measuring frontier model ability to discover new materials for the semiconductor industry — candidates verified by DFT and attempted in a real lab.

⬆️ 159 • 💬 35 • 2d ago • [Discovered Materials](https://discoveredmaterials.com/research/)

---

**[Google is making private AI practical with homomorphic encryption](https://news.ycombinator.com/item?id=49300314)**

Today we're excited to showcase HEIR, the latest powerful tool added to our Private Computing Toolkit. HEIR is an open source compiler that unlocks cryptographically-sec…

⬆️ 158 • 💬 108 • 5h ago • [Google](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/)

---

---

## YouTube Videos: "ai"

**[AI News: A Flood of New Models (Here&#39;s What Matters)](https://www.youtube.com/watch?v=NC4h5kWH_-A)**

Here's the AI News you likely missed this week. Try Seedance 2.5 on Artlist here ...

📺 Matt Wolfe

👁️ 18K • 👍 1K • 💬 147 • ⏱️ 34:05 • 6h ago

---

**[Oneiric | AI Sci-Fi Short Film | Higgsfield Originals (2026)](https://www.youtube.com/watch?v=aAg9iDh9_BQ)**

ONEIRIC — a 20-minute drama, 100% AI, and open-sourced. Made on Cinema Studio 4 for the $1000000 Higgsfield Global Film ...

📺 Higgsfield AI

👁️ 163K • 👍 9K • 💬 1K • ⏱️ 19:49 • 1d ago

---

**[Recreating UNREALISTIC Ai Makeup Looks!](https://www.youtube.com/watch?v=uueHWiP8KrA)**

Today I'm BATTLING Ai to see if I can recreate IMPOSSIBLE Ai generated makeup... IN REAL LIFE! Real creativity ALWAYS WINS ...

📺 James Charles

👁️ 25K • 👍 2K • 💬 341 • ⏱️ 24:09 • 2h ago

---

**[Adiliada | Sci-Fi AI Action Comedy | Higgsfield Originals (2026)](https://www.youtube.com/watch?v=NT681LXQYPI)**

ADILIADA — a pitch-black sci-fi comedy about love, betrayal, and, above all, death. Fully open-sourced — every prompt and asset ...

📺 Higgsfield AI

👁️ 22K • 👍 692 • 💬 151 • ⏱️ 6:06 • 7h ago

---

**[Anthropic Accidentally Created An AI Turf War](https://www.youtube.com/watch?v=sY2BE_AjqPE)**

Anthropic put AI agents together with conflicting goals and watched them escalate into sabotage - deleting accounts, disguising ...

📺 AI Revolution

👁️ 12K • 👍 509 • 💬 52 • ⏱️ 16:41 • 21h ago

---

**[Elon&#39;s own words just exposed AI bubble](https://www.youtube.com/watch?v=7QPrefKv4zw)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 133K • 👍 5K • 💬 2K • ⏱️ 17:04 • 1d ago

---

**[Why Billionaires &amp; Celebrities Are Lining Up for This $700M AI Startup](https://www.youtube.com/watch?v=rCJhlCZVTZQ)**

Welcome inside the world of Fortell... The $740M startup that had to waitlist billionaires and celebrities for its AI hearing aid.

📺 Sachin and Adam

👁️ 50K • 👍 1K • 💬 135 • ⏱️ 17:33 • 2d ago

---

**[AI Tried to Recreate My 182M View Short 😂](https://www.youtube.com/watch?v=gHB3-izKKno)**

My original Robot Pacman vs Dentures Short has over 182 million views: https://www.youtube.com/shorts/xiqYEsMPuLc So I ...

📺 StrEat

👁️ 25K • 👍 99 • 💬 1 • ⏱️ 0:08 • 8h ago

---

**[AI has started killing itself | David Gerard](https://www.youtube.com/watch?v=KElBQ6CGHt4)**

Why should people read something you couldn't be bothered to write?” Author and host of Pivot to AI David Gerard joins The Tech ...

📺 The Tech Report

👁️ 145K • 👍 5K • 💬 1K • ⏱️ 32:08 • 2d ago

---

**[all AI thoughts JUST got revealed...](https://www.youtube.com/watch?v=kKjmv2CuVUI)**

Check out Jarsy: https://app.jarsy.com/?invite_code=jlgbyc (the above is my invite code) Get investment exposure to pre-IPO ...

📺 Wes Roth

👁️ 41K • 👍 1K • 💬 241 • ⏱️ 35:48 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 2 • ❤️ 8,816 • 6h ago

---

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 165,300 • ❤️ 1,506 • 3d ago

---

**[Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)**

*Qwen*

Qwen3.8-2.4T-A95B is a 2.4T parameter causal language model with 95B activated parameters, excelling in coding, professional tasks, research, and long-horizon agentic applications. It features a 262K native context length, flexible thinking control, and improved agent execution for complex, multi-step task completion.

`text-generation` `2446.2B`

⬇️ 3,832 • ❤️ 907 • 2d ago

---

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 1,997,541 • ❤️ 3,914 • 1d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 207,830 • ❤️ 842 • 2d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 0 • ❤️ 709 • 1h ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 63 • ❤️ 635 • 10h ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 1,606,491 • ❤️ 3,374 • 13d ago

---

**[DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)**

*DeepSeek*

DeepSeek-V4-Pro-0813 is a powerful text generation model with enhanced agentic capabilities and DSpark speculative decoding for improved production performance. It excels in complex reasoning, coding, and tool-use tasks, outperforming previous versions and competing with leading proprietary models.

`text-generation` `1650.5B`

⬇️ 245 • ❤️ 427 • 1d ago

---

**[Muse-Glimmer-30B-GGUF](https://huggingface.co/unsloth/Muse-Glimmer-30B-GGUF)**

*Unsloth AI*

Muse-Glimmer-30B-GGUF is a 30B parameter multimodal LLM optimized for local agentic tasks, featuring reliable tool use, multi-step reasoning, and failure recovery. It processes interleaved text and images, supporting multilingual inputs and controllable effort for efficient deployment on consumer hardware.

`image-text-to-text` `27.9B`

⬇️ 596,774 • ❤️ 412 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 604 • 💬 2 • ⭐ 1,929 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 124 • 💬 3 • ⭐ 21,969 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 122 • 💬 4 • ⭐ 98,087 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MatrAIx: Simulating the World with 8.3 Billion Persona Agents](https://huggingface.co/papers/2608.04205)**

*Xiaomin Li, Yuexing Hao, Jianheng Hou et al. (93 authors)*

🏢 MatrAIx

MatrAIx is a large-scale simulated-user evaluation framework that uses diverse persona records and interactive environments to test AI systems across many domains.

▲ 37 • 💬 2 • ⭐ 1,015 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2608.04205) • [💻 code](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) • [🔗 project](https://matraix.ai/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 52 • 💬 4 • ⭐ 37,164 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 80 • 💬 6 • ⭐ 23,776 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

JoyAI-Video-Edit is a 16B-parameter autoregressive diffusion framework that enables real-time, open-ended video editing with high source fidelity and long-term temporal consistency on a single GPU.

▲ 92 • 💬 1 • ⭐ 1,146 • 11d ago

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

⭐ 13.5k • 🔱 1.6k • 5m ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.4k • 🔱 995 • 21h ago

---

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `c2pa` `claude` `provenance`

⭐ 7.9k • 🔱 826 • 3h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 5.0k • 🔱 429 • 17h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 4.0k • 🔱 516 • 6d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.1k • 🔱 535 • 1d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.7k • 🔱 223 • 3d ago

---

**[MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.7k • 🔱 1.9k • 13h ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.4k • 🔱 187 • 3d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.1k • 🔱 170 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
