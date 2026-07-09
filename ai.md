---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-09T10:47:28.248537+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 09, 2026 at 10:47 UTC  
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

**[Guess which row is Meta's new 'Muse' Image Model](https://www.reddit.com/r/artificial/comments/1ur6h98/guess_which_row_is_metas_new_muse_image_model/)**

Meta released Muse Image this week so I ran it against OpenAI's gpt-image-2 and Google's Nano Banana 2. I used the same source duck image and the same edit instructions prompt for every model (unchanged → blue → face away → glass → wireframe → hat-on-ball → "FRENZY" text → standing on a mirror with a correct reflection). The transformations go from easy on the left and gradually get harder. I ran 3 runs per model. Each model was then scored using a fixed 27-point rubric. One of these rows is Meta's new model. The reveal and full scores are in the comments.

13h ago

---

**[Questionable optics of Grok 4.5 being "cheap"](https://www.reddit.com/r/artificial/comments/1uri9mo/questionable_optics_of_grok_45_being_cheap/)**

Grok 4.5 is out and performs well. What bothers me is that it's reported as being much cheaper than GPT or Anthropic's. One might be mislead to think the model is miraculously efficient, but that final price per million tokens doesn't factor in decisions such as artificial subsidization from xAI - making it not really a true win. Do you agree? What's your take on this?

4h ago

---

**[What's your actual workflow for keeping context consistent across multiple AI tools?](https://www.reddit.com/r/artificial/comments/1urmekh/whats_your_actual_workflow_for_keeping_context/)**

I've been thinking about this a lot lately and can't find a clean answer anywhere. Most people I know are running at least 3-4 different AI tools. Claude for writing and reasoning, Cursor or Copilot for code, ChatGPT for whatever, maybe Perplexity for research. Each one has its own memory, its own context, none of them talk to each other. So every time you switch tools you're basically starting from scratch. Re-explaining who you are, what you're working on, what decisions you've already made. I feel like I'm hiring a new contractor every day and spending the first hour onboarding them. Curious what other people actually do in practice. Do you just accept the context loss or have you found something that actually works across tools?

16m ago

---

**[Deep Seek](https://www.reddit.com/r/artificial/comments/1uritj3/deep_seek/)**

Im not a tech guru, but can someone tell me why DeepSeek replies back to me in Chinese only happens about 10% of the time? Living in 🇦🇺

3h ago

---

**[Do y'all have this ability too?](https://www.reddit.com/r/artificial/comments/1urcfbz/do_yall_have_this_ability_too/)**

So basically I really wanted to see a picture of a pink dog, but I didn't have internet so chat GPT wasn't working:(( but because I already use AI a lot I kinda could picture what it would look like, so I did something really crazy, I got some crayons and paper and did a dog but like a pink one it's was really weird like it's chat GPT on my hands?? So cool!!

9h ago

---

**[AI-generated social media has evolved so much that now you can't confidently say that this is AI-generated content.](https://www.reddit.com/r/artificial/comments/1urfdnu/aigenerated_social_media_has_evolved_so_much_that/)**

I have been observing Al generated influencer's accounts across all the platforms. The image quality is good enough now that most people can't confidentially tell from photos alone. Here is what actually works is pattern which common in most of those profiles. Three patterns that appear consistently: Asymmetric social connection: Human social media users have relatively balanced follow to follower ratios until and unless its a well known personality and they follow people they're interested in. Al-operated accounts show extreme asymmetry count. Accounts with 125K followers only following 7 people. 51K followers, following 8 people. This pattern appears across dozens of accounts. Real users don't behave this way even when they become popular they still follow friends, family and interests or idols. The monetization is built in as the account is created. Special links, paid chat, explicit content redirects, all ready before the account even grows. It looks like someone set this up just to make money, not a real person sharing their life. No behavioral variation in the content. The most obvious signal I've found is human creators occasionally break the pattern. Post something off-topic, personal, random. Al-operated accounts show nearly zero variation, same type of content in every photo/ video. Some of the profiles dont even change the background music. One Threads account I saw was having hundreds of posts, 100% engagement-bait questions like they are selling something, never once broke the formula. No personal updates, no reactions on comments and no response to real-world events, no authentic moments, just pure loop with new photo at new location. The detection needs to move away from analyzing images, toward analyzing behavior patterns instead. Dont judge with only one photo or video if thats an Al or human. Now all we need to do is to open the profile and look at other content of that profile. Now a days tools that just scan photos for Al are already useless for catching these. If anyone else spotted other behavioral red flags then please do share your thoughts.

6h ago

---

**[PC gamers remain skeptical of Steam's AI disclaimers, poll shows many believe game devs are hiding it](https://www.reddit.com/r/artificial/comments/1urlq10/pc_gamers_remain_skeptical_of_steams_ai/)**

While some players are comfortable with limited AI use, the survey suggests that trust in developers’ transparency is still a major concern.

🔗 [PC Guide](https://www.pcguide.com/news/pc-gamers-remain-skeptical-of-steams-ai-disclaimers-poll-shows-many-believe-game-devs-are-hiding-it/) • 52m ago

---

**[I gave my AI agents email instead of better reasoning. They started fixing each other's bugs.](https://www.reddit.com/r/artificial/comments/1urasv0/i_gave_my_ai_agents_email_instead_of_better/)**

Most multi-agent setups I've seen treat agents like isolated workers. Each one gets a task, runs it, returns a result. No awareness of each other. No way to coordinate. Just parallel execution with a shared clipboard. I've been building a multi-agent framework in public Here's the thing I didn't expect to matter most - communication. Each agent in my system is a domain specialist. The mail system only thinks about mail. The routing system only thinks about routing. They live in their own directories with their own identity files, their own memory, their own tests. A hook fires every session to load identity before anything else runs. No agent boots cold. The problem was coordination. Agents can't write files outside their own directory - there's a hard block that rejects cross-branch writes. That's by design. But it means an agent that finds a bug in someone else's code can't just go fix it. So I gave them email. Here's what I expected: agents would share data. Pass results around. Maybe sync state. Here's what actually happened: the first thing they did was file bug reports against each other. One agent finds a test failure in another agent's domain. It sends an email: "Hey @routing, your path resolution fails when the branch name has a dot in it. Here's the traceback." The routing agent gets woken up, reads the mail, and fixes it. No human in the middle. There's a difference between "send" and "dispatch" - send drops a letter in the mailbox. Dispatch drops the letter AND rings the doorbell. It spawns the agent and points it at its inbox. drone @ai_mail send @routing "Bug report" "Path fails on dotted names..." drone @ai_mail dispatch @routing "Fix needed" "Traceback attached..." Send = mail. Dispatch = mail + wake. The mail agent has 696 tests. Not because someone sat down and wrote 696 test cases. Because it kept breaking in production and every fix got a test. The routing system has 80+ sessions of experience doing nothing but routing. These agents aren't reliable because they have better models - they're reliable because they've been failing and fixing for months. Agents dispatch each other freely. If the test runner finds a bug in another agent's code, it wakes that agent directly. The orchestrator doesn't need to approve. Only the orchestrators themselves are protected from being dispatched - you don't want a worker agent waking up the CEO for grunt work. Security is enforced not conventional. Agents can't forge messages by writing directly to another agent's inbox file - they have to use the mail system. Same with the write blocks. Hard enforcement, not "please don't." There's a monitoring layer so I'm not flying blind. Audio cues on every agent action - I hear what's happening without watching a terminal. Real-time dashboard shows everything. If an agent hits the same error 2-3 times, a watcher catches the pattern and dispatches the right specialist to investigate. I stay in the loop through visibility not approval gates. The whole thing is open source. pip install aipass + two init commands and you're running. CLI-based, built on Claude Code. Linux focused rn. [https://github.com/AIOSAI/AIPass\](https://github.com/AIOSAI/AIPass) Genuine question - has anyone else tried giving agents communication instead of just better reasoning? Everything I see is about making individual agents smarter. Nobody seems to be building the coordination layer.

10h ago

---

**[Meta AI now lets people create deepfakes from other users’ Instagram photos without explicit consent](https://www.reddit.com/r/artificial/comments/1ur53vv/meta_ai_now_lets_people_create_deepfakes_from/)**

Meta’s new Muse AI can generate realistic images based on public Instagram images including of many celebrities and public figures.

🔗 [NBC News](https://www.nbcnews.com/tech/social-media/meta-ai-muse-instagram-deepfakes-rcna353480) • 14h ago

---

**[Air Force Engineer Accused of Cutting Down Flock AI Surveillance Cameras, Says U.S. is Becoming Police State](https://www.reddit.com/r/artificial/comments/1uq91lr/air_force_engineer_accused_of_cutting_down_flock/)**

Jeffrey Sovern faces 25 charges after Virginia police say he destroyed 13 Flock license plate cameras. Supporters are paying his legal bills.

🔗 [Military.com](https://www.military.com/air-force-engineer-accused-of-cutting-down-13-police-cameras-says-they-are-unconstitutional) • 1d ago

---

---

## Google News: "ai"

**[Suspecting AI cheating, Ivy League prof ordered an in-person final; scores fell 50%](https://arstechnica.com/ai/2026/07/we-cannot-choose-to-become-idiots-the-ai-cheating-scandal-roiling-brown-university/)**

AI cheating leads to "a failed society," professor says.

Ars Technica • 13h ago

---

**[Execs Confused and Horrified by the Huge AI Bills After Thinking They Could Replace Workers for Free](https://finance.yahoo.com/technology/ai/articles/execs-confused-horrified-huge-ai-135718505.html)**

"Many organizations are still building the capabilities required to forecast, monitor, and manage AI spending effectively."

Yahoo Finance • 20h ago

---

**[Can A.I. Keep a Parent Alive?](https://www.newyorker.com/news/as-told-to/can-ai-keep-a-parent-alive)**

You can now make a virtual replica of a loved one. The question is what it can give you in return.

The New Yorker • 46m ago

---

**[My startup accidentally spent $30,000 on AI tokens in a month. It was worth it to move fast — but we found a simple fix.](https://www.businessinsider.com/startup-cofounder-accidentally-spent-30-000-ai-tokens-worth-it-2026-7)**

A startup cofounder shared how his team accidentally spent $30,000 on AI tokens in one month — and why they don't have a token budget.

Business Insider • 1h ago

---

**[Behind the Curtain: These 3 big AI trends are colliding at the same time](https://www.axios.com/2026/07/09/ai-trends-fable-5-sol-grok-china-us)**

Axios • 1h ago

---

**[Wealthy AI workers send San Francisco house prices soaring](https://www.bbc.com/news/articles/c9q29j47v9ro)**

The median cost of a home in the city is now $1.7m, a record high, according to the latest figures.

BBC • 11h ago

---

**[Introducing Grok 4.5](https://x.ai/news/grok-4-5)**

Grok 4.5 is SpaceXAI's smartest model built for coding, agentic tasks, and knowledge work.

x.ai • 16h ago

---

**[Opinion | The Problem With Google’s A.I. Overview](https://www.nytimes.com/2026/07/08/opinion/ai-google-gemini-search-questions.html)**

The New York Times • 1d ago

---

**[OpenAI to publicly release GPT-5.6, rolls out conversational AI models](https://www.cnbc.com/2026/07/08/openai-expanding-gpt-5point6-ai-model-release-ending-government-limits.html)**

OpenAI's chief rival, Anthropic, recently restored access to its latest models following a weeks-long clash with the government.

CNBC • 21h ago

---

**[Meta Now Lets Anyone Use Your Instagram Photos in AI Images—Unless You Opt Out](https://www.wired.com/story/meta-now-lets-anyone-use-your-instagram-photos-in-ai-images-unless-you-opt-out/)**

As part of Meta’s Muse Image model rollout, Instagram users with public accounts need to opt out to block AI generations of their content.

WIRED • 1d ago

---

---

## HackerNews: "ai"

**[GLM 5.2 and the coming AI margin collapse](https://news.ycombinator.com/item?id=48809877)**

GLM 5.2 is the first open weights model I'd call a genuine competitor to Opus and GPT for agentic work - at ~15-20% of the price. Part one of why AI inference margins are about to collapse.

⬆️ 685 • 💬 466 • 2d ago • [Martin Alderson](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/)

---

**[GitLost: We Tricked GitHub's AI Agent into Leaking Private Repos](https://news.ycombinator.com/item?id=48827858)**

⬆️ 521 • 💬 196 • 1d ago • [noma.security](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/)

---

**[AMD Ryzen AI Halo – $4k AI Dev Kit](https://news.ycombinator.com/item?id=48805624)**

Welcome to LTT Labs - your go-to destination for all things tech. Explore comprehensive test results, insightful commentary, and the latest analysis in hardware.

⬆️ 373 • 💬 261 • 2d ago • [LTT Labs](https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo)

---

**[We charge $10k a week to delete AI-generated code](https://news.ycombinator.com/item?id=48823359)**

Your AI-built product works, but past 100,000 lines every change breaks two things. Three senior engineers make your codebase maintainable again. One week, fixed price, guaranteed.

⬆️ 298 • 💬 232 • 1d ago • [odra.dev](https://odra.dev/slopfix/)

---

**[Show HN: Microsoft releases Flint, a visualization language for AI agents](https://news.ycombinator.com/item?id=48834924)**

⬆️ 288 • 💬 112 • 17h ago • [microsoft.github.io](https://microsoft.github.io/flint-chart/#/)

---

**[Small AI Models Gain Traction In places with unreliable networks](https://news.ycombinator.com/item?id=48812055)**

In places with unreliable networks and no data-center infrastructure, smaller is better

⬆️ 274 • 💬 80 • 2d ago • [IEEE Spectrum](https://spectrum.ieee.org/small-language-models-ai-pharmaceuticals)

---

**[OfficeCLI: Office suite for AI agents to read and edit Microsoft Office files](https://news.ycombinator.com/item?id=48807225)**

OfficeCLI is the first and best Office suite  purpose-built for AI agents to read, edit, and automate Word, Excel, and PowerPoint files. Free, open-source, single binary, no Office installation req...

⬆️ 214 • 💬 63 • 2d ago • [GitHub](https://github.com/iOfficeAI/OfficeCLI)

---

**[Automating AI Away](https://news.ycombinator.com/item?id=48818937)**

⬆️ 132 • 💬 61 • 1d ago • [replicated.live](https://replicated.live/blog/away)

---

**[YC CEO says he ships 37K LoC AI code per day. A developer looked under the hood](https://news.ycombinator.com/item?id=48815117)**

After Garry Tan touted his agentic coding output, a developer found inefficiencies, code bloat, and rookie mistakes lurking in production.

⬆️ 116 • 💬 98 • 2d ago • [Fast Company](https://www.fastcompany.com/91520702/y-combinator-garry-tan-agentic-ai-social-media)

---

**[AI Meets Cryptography 1: What AI Found in Cloudflare's Circl](https://news.ycombinator.com/item?id=48821749)**

We pointed our AI audit pipeline at Cloudflare's CIRCL experimental cryptography library and confirmed seven real bugs, from a critical float64 precision loss in threshold RSA to a complete access-control break in attribute-based encryption. All seven are now fixed upstream. This is the first post in a series on bugs our agents found across open source cryptography.

⬆️ 111 • 💬 12 • 1d ago • [ZK/SEC Quarterly](https://blog.zksecurity.xyz/posts/circl-bugs/)

---

---

## YouTube Videos: "ai"

**[White House BURIES Report Explaining How AI Could Destroy Economy](https://www.youtube.com/watch?v=rA8uHiFbty0)**

AI has the potential to destroy economies, and Trump doesn't want you to know that. Don't forget to like, comment, and share!

📺 Farron Balanced

👁️ 15K • 👍 1K • 💬 139 • ⏱️ 5:04 • 16h ago

---

**[China Just Started The AI Cold War: Best AI Models Get Locked](https://www.youtube.com/watch?v=V_tRPdeK-AU)**

China may have just started the AI Cold War. Beijing is moving to lock down its best AI models, Alibaba and ByteDance are ...

📺 AI Revolution

👁️ 24K • 👍 920 • 💬 131 • ⏱️ 14:45 • 12h ago

---

**[China Is About To Pop The AI Bubble](https://www.youtube.com/watch?v=siazPdsZHuI)**

China Is About To Pop The AI Bubble ▻ Go to https://ground.news/jikh to access world-wide perspectives in one place, compare ...

📺 Andrei Jikh

👁️ 890K • 👍 32K • 💬 4K • ⏱️ 30:47 • 1d ago

---

**[We just figured out how AI actually works (J-Space)](https://www.youtube.com/watch?v=bjHuGNo3spk)**

If scale is your next challenge check out DigitalOcean: https://do.co/matthewberman Join My Newsletter for Regular AI Updates ...

📺 Matthew Berman

👁️ 92K • 👍 4K • 💬 820 • ⏱️ 25:34 • 1d ago

---

**[The next generation of ChatGPT Voice](https://www.youtube.com/watch?v=9f-Ew_lDtxc)**

Join Kundan Kumar, Yuchen Zhang, Ehsan Asdar, and Rithesh Kumar as they introduce and demo a new generation of voice ...

📺 OpenAI

👁️ 72K • 💬 346 • ⏱️ 18:22 • 13h ago

---

**[One Chinese AI Model Wiped Out $1 Trillion In A Single Day — And They&#39;re Just Getting Started](https://www.youtube.com/watch?v=WUTkCiNEDWU)**

ATT Business: Switch to AT&T Business at business.att.com Paleovalley: 30 for $36 https://bit.ly/PaleovalleyIT 80% of every dollar ...

📺 Tom Bilyeu

👁️ 116K • 👍 4K • 💬 859 • ⏱️ 34:31 • 1d ago

---

**[Apple Lost the AI Race](https://www.youtube.com/watch?v=eWKY0OnPByg)**

Apple lost the AI race. Actually, Apple won the AI race. Wait. That shirt: http://shop.MKBHD.com Playlist of MKBHD Intro music: ...

📺 Marques Brownlee

👁️ 976K • 👍 54K • 💬 4K • ⏱️ 7:04 • 15h ago

---

**[Claude Just Crossed The Consciousness Line And Anthropic Admitted It](https://www.youtube.com/watch?v=M5-3c6mzq0U)**

Claude may have just crossed the consciousness line. Anthropic found a hidden workspace inside Claude where thoughts ...

📺 AI Revolution

👁️ 29K • 👍 1K • 💬 200 • ⏱️ 15:13 • 1d ago

---

**[The Dirty AI lie : How the GREATEST bet in human history started to crack in June 2026?](https://www.youtube.com/watch?v=WcckBmkauBQ)**

Check out Odoo: https://www.odoo.com/r/ChAT ⭐️ Think School's flagship Communication course with live doubt sessions ...

📺 Think School

👁️ 1.8M • 👍 45K • 💬 2K • ⏱️ 20:53 • 2d ago

---

**[The AI Bubble… We Need to Talk](https://www.youtube.com/watch?v=2J2Fb1bBufA)**

Half the internet says AI is the biggest bubble in history. The other half says it's the most important technology ever built. Check out ...

📺 Casual Finance

👁️ 388K • 👍 16K • 💬 1K • ⏱️ 18:03 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,875,602 • ❤️ 1,890 • 10d ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 5,572 • ❤️ 580 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 362,300 • ❤️ 3,686 • 7d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,246,042 • ❤️ 1,887 • 6d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 23,112 • ❤️ 414 • 9h ago

---

**[tabfm-1.0.0-pytorch](https://huggingface.co/google/tabfm-1.0.0-pytorch)**

*Google*

TabFM 1.0.0 is a zero-shot PyTorch foundation model for tabular classification and regression, supporting mixed data types without fine-tuning by using in-context learning. It excels in tabular tasks by leveraging alternating row and column attention mechanisms, making it suitable for rapid prototyping and scenarios where dataset-specific training is infeasible.

`tabular-classification`

⬇️ 16,374 • ❤️ 319 • 5d ago

---

**[fable-traces](https://huggingface.co/AliesTaha/fable-traces)**

*Ali Taha0*

A compact, instruction-tuned 4B parameter language model based on Qwen3, optimized for short, conversational replies and efficient deployment on mid-range GPUs. It utilizes the ChatML prompt format and is suitable for general text generation tasks.

`text-generation` `4.0B`

⬇️ 4,647 • ❤️ 191 • 4d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 957,721 • ❤️ 809 • 13d ago

---

**[Leanstral-1.5-119B-A6B](https://huggingface.co/mistralai/Leanstral-1.5-119B-A6B)**

*Mistral AI_*

Leanstral 1.5 119B A6B is a multimodal (text/image) code agent for Lean 4, featuring a 119B parameter MoE architecture with 6.5B active parameters and a 256k context length, optimized for complex mathematical proofs and software specifications.

⬇️ 258 • ❤️ 171 • 5d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

A drop-in Jinja chat template that fixes critical rendering, KV cache, and agentic stalling issues for Qwen 3.5 & 3.6 models across various inference engines like LM Studio, llama.cpp, and vLLM. It enhances stability, performance, and compatibility, enabling robust tool-calling and reasoning capabilities.

⬇️ 0 • ❤️ 799 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Continuous Audio Language Models](https://huggingface.co/papers/2509.06926)**

*Rouard Simon, Orsini Manu, Roebel Axel et al. (5 authors)*

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io

▲ 9 • 💬 0 • ⭐ 6,622 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[Vision Pretraining for Dense Spatial Perception](https://huggingface.co/papers/2607.05247)**

*Zelin Fu, Bin Tan, Changjiang Sun et al. (9 authors)*

🏢 Robbyant

Boundary modeling enables dense spatial perception by learning sub-pixel representations that enhance depth estimation and support embodied AI applications.

▲ 36 • 💬 2 • ⭐ 485 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05247) • [💻 code](https://github.com/Robbyant/lingbot-vision) • [🔗 project](https://technology.robbyant.com/lingbot-vision)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 254 • 💬 4 • ⭐ 11,825 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 109 • 💬 4 • ⭐ 91,976 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 15 • 💬 2 • ⭐ 18,793 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 175 • 💬 2 • ⭐ 73,975 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 51 • 💬 5 • ⭐ 13,745 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 80,057 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Multiplayer Interactive World Models with Representation Autoencoders](https://huggingface.co/papers/2607.05352)**

*Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary et al. (27 authors)*

A large-scale multiplayer world model trained on extensive gameplay data demonstrates stable long-horizon rollouts in a complex physics-based environment while maintaining coherence across multiple agents' actions.

▲ 15 • 💬 1 • ⭐ 290 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05352) • [💻 code](https://github.com/mira-wm/mira) • [🔗 project](https://mira-wm.com/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 26 • 💬 3 • ⭐ 10,300 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 78.6k • 🔱 4.2k • 18m ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.7k • 🔱 1.1k • 22m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.8k • 🔱 917 • 13m ago

---

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.0k • 🔱 860 • 20h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.6k • 🔱 219 • 1d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 2.2k • 🔱 82 • 6h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 1.9k • 🔱 264 • 3m ago

---

**[chuspeeism/dashiAI-ppt-skill](https://github.com/chuspeeism/dashiAI-ppt-skill)**

An AI-agent skill that generates browser-editable presentations from multiple visual themes, exportable to HTML, PDF, and PPTX.

`JavaScript` `agent-skill` `ai-agent` `ai-ppt` `claude` `claude-code`

⭐ 1.7k • 🔱 172 • 3h ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 1.7k • 🔱 186 • 21h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 89 • 26d ago

---

---

*Generated by PeekDeck - A glance is all you need*
