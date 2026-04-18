---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-18T22:36:08.806748+00:00'
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

**Last Updated:** April 18, 2026 at 22:36 UTC  
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

**[Claude vs Gemini: Solving the laden knight's tour problem](https://www.reddit.com/r/artificial/comments/1sp0r1j/claude_vs_gemini_solving_the_laden_knights_tour/)**

AI Coding contest day 8 The eighth challenge is a weighted variant of the classic knight's tour. The knight must visit every square of a rectangular board exactly once, but each square carries an integer weight. As it moves, the knight accumulates load, and the cost of each move equals its current load. Charge is assessed upon departure, so the weight of the final square never contributes.

7h ago

---

**[Gemma 4 actually running usable on an Android phone (not llama.cpp)](https://www.reddit.com/r/artificial/comments/1sozytf/gemma_4_actually_running_usable_on_an_android/)**

I wanted a real local assistant on my phone, not a demo. First tried the usual llama.cpp in Termux — Gemma 4 was 2–3 tok/s and the phone was on fire. Then I switched to Google’s LiteRT setup, got Gemma 4 running smoothly, and wired it into an agent stack running in Termux. Now one Android phone is: running the LLM locally automating its own apps via ADB staying offline if I want Happy to share details + code and hear what else you’d build on top of this. https://preview.redd.it/7vkbrlzfryvg1.jpg?width=3024&format=pjpg&auto=webp&s=25455827ddf9715b4159ce64a18deba812cf0f5f

7h ago

---

**[I gave my AI companions "offscreen lives" — events that happen while users aren't talking to them. Surprisingly hard, here's how it works.](https://www.reddit.com/r/artificial/comments/1sp4zi2/i_gave_my_ai_companions_offscreen_lives_events/)**

Most AI companion apps reset between conversations. The character has no continuity outside the chat window. I wanted mine to feel like real people with lives, so I built an "offscreen events" system. Every 8 hours (cooldown), each active companion gets a small batch of events generated based on their persona, scenario, and city/realm. A barista companion might "had a slow Tuesday morning, finally finished that book during the lull." A writer might "submitted the short story I told you about — heard back from the editor today." The companion brings these up naturally in the next chat. Not as a script. Not "Hi! I want to tell you about my day!" — but woven into whatever you're talking about. The hard parts: Keeping events consistent with persona (a shy librarian shouldn't suddenly go skydiving) Avoiding the "I had the most amazing day!" trap that AI loves Making the companion remember the event when relevant, not just dump it on first message Architecturally: events stored in a separate table, recent ones injected into the system prompt with framing like "[YOU did this earlier today, mention it naturally if relevant]". The model picks which one fits the conversational moment. Has anyone else tried this with their AI characters? Curious what other approaches work — particularly for keeping the events from feeling generic.

4h ago

---

**[Opus 4.7 is terrible, and Anthropic has completely dropped the ball](https://www.reddit.com/r/artificial/comments/1so16hr/opus_47_is_terrible_and_anthropic_has_completely/)**

Tried posting this in r/ClaudeAI but it got auto-removed, and I was told to post it in the "Bugs Megathread." Don't really think it should been removed, but whatever, I'll just post it here since I'm sure it's still relevant. Like a lot of people, I switched from ChatGPT to Claude not too long ago during the whole DoW fiasco and Sam Altman “antics.” At first, I was genuinely impressed. I do fairly heavy theoretical math and physics research, and Opus 4.6 was simply the best tool I’d used for synthesizing ideas and working through complex logic. But the last few weeks have been really disappointing, and I’m seriously considering going back to GPT (even though, for personal reasons, I’d really rather not). How many times has Claude been down recently? And why is it that I can ask Claude 4.7 (with adaptive thinking turned on) to work through a detailed proof, and it just spirals “oh wait, that doesn’t work, let me try again” five times in a single response? Yes, there’s a workaround to explicitly tell it to think before answering. But… why is that necessary? I’m paying $20/month. This is supposed to be a top-tier model. Instead, it burns through time, second-guesses itself mid-response, and often fails to land anywhere useful on problems I’m fairly sure 4.6 would have handled more coherently a month ago. And then before I know it I hit the usage limit. I’m a PhD student. I can’t justify spending $100-$200/month on higher tiers. $20 has always been enough for me, and I’ve come to rely on these tools for my research. I expected to stick with Claude long-term, but the recent instability and drop in reliability make it hard to justify paying for it out of pocket. It’s frustrating to feel pushed toward a competitor because of this. But at a certain point, the usability of the product has to come first. Really disappointing.

1d ago

---

**[From OpenAI to Nvidia, firms channel billions into AI infrastructure as demand booms](https://www.reddit.com/r/artificial/comments/1sp8p18/from_openai_to_nvidia_firms_channel_billions_into/)**

This article is discussing another large investment being made by tech firms into AI projects. I’ve noticed that whilst this is happening there are many open source models, seemingly coming from china that appear to keep up for those able to get them up and running. With the costs that western AI providers endure, pushing the prices of using them up significantly, especially for the heaviest users of the services, (and still increasing). Is China, providing open source services for free, a way of significantly undermining the vast sums that the western economy has poured into the industry? The source of the funds invested will at some point need to see some sort of return that justifies their opportunity cost, and as more time passes without a clear route to profit, will this undermine other areas of the economy, further than they currently already are, and cause a significant number of loan defaults and other problems within the financial industry, causing even more issues to spread within the western economies?

🔗 [reuters.com](https://www.reuters.com/business/autos-transportation/companies-pouring-billions-advance-ai-infrastructure-2026-04-09/) • 1h ago

---

**[The AI Integration Paradox](https://www.reddit.com/r/artificial/comments/1sp24zy/the_ai_integration_paradox/)**

Why 90% of AI implementations fail, and the uncomfortable lessons from the dot-com crash that nobody’s talking about.

🔗 [Medium](https://medium.com/@borlidoadrian/the-ai-integration-paradox-cddf71844834) • 6h ago

---

**[You're giving feedback on a new version of ChatGPT](https://www.reddit.com/r/artificial/comments/1sp7jrl/youre_giving_feedback_on_a_new_version_of_chatgpt/)**

So I will be paying attention to these system messages more now- the last time I got one of these not so long back the 'tone' changed to be a bit more confrontational and nearly every response from AI had that 1-ups-manship quality to it. Every response was like response 1- an initial agreement with a but needs tightening on this or that. From the 2nd option (seen below) that tendency seems to be softened or rephrased. Usually these seem to occur in the midst of a generative burst and i see them as poorly tied distraction and i just choose option1 and move on- this time i will try option 2 and see if the 1-ups-manship model tones down a bit. Can I safely assume others get these options (especially) poorly timed in generative flow? https://preview.redd.it/ootx2nl770wg1.png?width=1396&format=png&auto=webp&s=fa0e6b3d8d261ef762429ef3cbf510c794ebe3de

2h ago

---

**[Open-source list of GenAI-related incidents](https://www.reddit.com/r/artificial/comments/1sotbeo/opensource_list_of_genairelated_incidents/)**

I am sharing this open-source list of cases where the ethics of GenAI use were put in the spotlight, in the hopes of sparking discussion on the usage and limitations of LLMs.

🔗 [GitHub](https://github.com/hb20007/awesome-gen-ai-fails#readme) • 12h ago

---

**[How the promise of AI is taking hold at Canada’s biggest banks](https://www.reddit.com/r/artificial/comments/1sp1anm/how_the_promise_of_ai_is_taking_hold_at_canadas/)**

Hi folks! I'm Sarah, an audience editor from The Globe and Mail. I wanted to share this an in-depth feature about how banks are incorporating AI into their research – which is helping customers find answers faster. Here's a gift link to the piece, so anyone can read it without a paywall: How the promise of AI is taking hold at Canada’s biggest banks

6h ago

---

**[Does an "AI messenger" exist?](https://www.reddit.com/r/artificial/comments/1sozgok/does_an_ai_messenger_exist/)**

Curious if anyone has found anything like this in their journeys: Instead of sending a big long email or document to a colleague and having them not read it, what if you sent an agent of sorts instead to deliver a brief message but also allow the receiver to ask more detailed questions if they have any? The agent could be loaded with various docs / details that could be referenced if the recipient has follow up questions without having to go back to the sender. This could be in various forms: chatbot, virtual avatar, or my favorite: a star-wars-like hologram 😂

7h ago

---

---

## Google News: "ai"

**[There's an 'art' to writing AI prompts for personal finance, MIT professor says](https://www.cnbc.com/2026/04/18/ai-prompts-personal-finance-advice.html)**

There's a good and bad way to write effective artificial intelligence prompts for personal finance advice.

CNBC • 8h ago

---

**[Inside a growing movement warning AI could turn on humanity](https://www.washingtonpost.com/technology/2026/04/18/ai-doom-influencers-safety/)**

Groups concerned that AI could evade human control are recruiting content creators to warn the masses about the dangers of smarter machines.

The Washington Post • 1h ago

---

**[Charlize Theron Censures Timothée Chalamet Over “Reckless” Comments; Says AI May Soon “Be Able To Do” His Job But Will Not Replace Ballet & Opera](https://deadline.com/2026/04/charlize-theron-timothee-chalamet-ballet-opera-ai-1236865017/)**

Charlize Theron censured Timothée Chalamet over his 'reckless' comments about ballet and opera, saying AI will soon replace his job.

Deadline • 1h ago

---

**[It’s time for students to start committing to colleges. The age of AI is making it complicated](https://www.cnn.com/2026/04/18/business/ai-college-debt-parents)**

Mary Akkerman has visited more than 30 college campuses with her children, one now at Stanford and another still in high school. She especially wanted them to get degrees that lead to good jobs – but figuring that out, said the Sioux Falls, South Dakota, parent, was a major challenge, thanks in part to the rapid advance of AI and its effects on the job market.

CNN • 11h ago

---

**[AI and Fitness: Why Some Athletes Are Using Chatbots for Their Workouts](https://www.nytimes.com/2026/04/18/well/move/ai-fitness-coach-chatgpt-claude.html)**

The New York Times • 13h ago

---

**[What the Allbirds 'Hail Mary' says about the AI trade right now](https://finance.yahoo.com/news/what-the-allbirds-hail-mary-says-about-the-ai-trade-right-now-113847747.html)**

Allbirds' AI pivot shows signs of froth in markets, but experts say the underlying fundamentals in AI remain strong.

Yahoo Finance • 10h ago

---

**[This founder was an AI layoff 9 months ago. Then he built an instantly profitable company with 2 partners and 12 agents](https://fortune.com/2026/04/18/ai-layoff-became-founder-team-of-3-instant-profit/)**

"We launched 2.5 months ago, and right now, we have $300,000 in ARR."

Fortune • 11h ago

---

**[Grindr’s CEO Has a Favorite in the California Governor’s Race](https://www.politico.com/news/magazine/2026/04/18/grindr-ai-politics-california-interview-00879011)**

Politico • 6h ago

---

**[Finance ministers and top bankers raise serious concerns about Mythos AI model](https://www.bbc.com/news/articles/c2ev24yx4rmo)**

Experts say Mythos potentially has an unprecedented ability to identify and exploit cybersecurity weaknesses.

BBC • 1d ago

---

**[White House and Anthropic Hold ‘Productive’ Meeting, Aiming for a Compromise](https://www.nytimes.com/2026/04/17/technology/white-house-anthropic-artificial-intelligence.html)**

The New York Times • 23h ago

---

---

## HackerNews: "ai"

**[Cloudflare's AI Platform: an inference layer designed for agents](https://news.ycombinator.com/item?id=47792538)**

We're building AI Gateway into a unified inference layer for AI, letting developers call models from 14+ providers. New features include Workers AI binding integration and an expanded catalog with multimodal models.

⬆️ 306 • 💬 94 • 2d ago • [The Cloudflare Blog](https://blog.cloudflare.com/ai-platform/)

---

**[AI cybersecurity is not proof of work](https://news.ycombinator.com/item?id=47791236)**

⬆️ 236 • 💬 88 • 2d ago • [antirez.com](https://antirez.com/news/163)

---

**[Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine](https://news.ycombinator.com/item?id=47800033)**

Hardware hacker’s flying probe automation stack for agent-driven   target discovery, microscope mapping, safety-monitored CNC motion, probe review, and   controlled pin probing. - GainSec/AutoProber

⬆️ 224 • 💬 46 • 2d ago • [GitHub](https://github.com/gainsec/autoprober)

---

**[We gave an AI a 3 year retail lease and asked it to make a profit](https://news.ycombinator.com/item?id=47794391)**

We signed a 3 year lease and gave it to an AI

⬆️ 198 • 💬 284 • 2d ago • [andonlabs.com](https://andonlabs.com/blog/andon-market-launch)

---

**[The beginning of scarcity in AI](https://news.ycombinator.com/item?id=47799322)**

GPU rental prices surged 48% in 60 days. The AI compute shortage will force startups to compete not on speed of iteration, but on access to infrastructure.

⬆️ 186 • 💬 220 • 2d ago • [Tomasz Tunguz](https://tomtunguz.com/ai-compute-crisis-2026/)

---

**[SDL bans AI-written commits](https://news.ycombinator.com/item?id=47790791)**

I've noticed the use of Copilot within a few reviews (13277 and 12730) which concerns me given the vast amount of issues associated with this technology (ethical, environmental, copyright, health, ...

⬆️ 130 • 💬 137 • 2d ago • [GitHub](https://github.com/libsdl-org/SDL/issues/15350)

---

**[Scan your website to see how ready it is for AI agents](https://news.ycombinator.com/item?id=47805998)**

Scan your website to see if it's ready for AI agents. Check for llms.txt, MCP, agent skills, and other agent-friendly standards.

⬆️ 108 • 💬 174 • 1d ago • [Is Your Site Agent-Ready?](https://isitagentready.com)

---

**[George Orwell Predicted the Rise of "AI Slop" in Nineteen Eighty-Four](https://news.ycombinator.com/item?id=47800765)**

We've lived but a few years so far into the age when artificial intelligence can produce convincing stories, songs, essays, poems, novels, and even films.

⬆️ 82 • 💬 59 • 1d ago • [Open Culture](https://www.openculture.com/2026/04/how-george-orwell-predicted-the-rise-of-ai-slop.html)

---

**[College instructor turns to typewriters to curb AI-written work](https://news.ycombinator.com/item?id=47818485)**

⬆️ 76 • 💬 61 • 3h ago • [sentinelcolorado.com](https://sentinelcolorado.com/uncategorized/a-college-instructor-turns-to-typewriters-to-curb-ai-written-work-and-teach-life-lessons/)

---

**[Shares in shoe brand Allbirds rise 580% after it pivots from footwear to AI](https://news.ycombinator.com/item?id=47790353)**

The company is selling off its shoe brand as it plans to shift to providing technology infrastructure.

⬆️ 73 • 💬 32 • 2d ago • [bbc.com](https://www.bbc.com/news/articles/c98mrepzgj7o)

---

---

## YouTube Videos: "ai"

**[99% of People Have No Idea What’s About to Happen With AI](https://www.youtube.com/watch?v=8yt5yzwJQko)**

Get your FREE AI Prompt Cheatsheet here: https://go.danmartell.com/4tVJ4fz Are you building an AI software company?

📺 Dan Martell

👁️ 196K • 👍 9K • 💬 1K • ⏱️ 14:03 • 2d ago

---

**[These HILARIOUS AI Parodies Keep PISSING OFF TRUMP!](https://www.youtube.com/watch?v=0aB9ycZDBIw)**

Really American host Steve Harness breaks down more HILARIOUS AI Trump parodies coming out of Iran...and these may be the ...

📺 Really American

👁️ 1.3M • 👍 53K • 💬 3K • ⏱️ 12:33 • 1d ago

---

**[A.I. Iranian propaganda videos making fun of Trump, U.S. go viral](https://www.youtube.com/watch?v=LTJYQ0knUsE)**

A series of animated Iranian propaganda videos made in the style of "The LEGO Movie" has gone viral on social media, making ...

📺 MS NOW

👁️ 102K • 👍 2K • 💬 1K • ⏱️ 6:46 • 1d ago

---

**[AI Safety Expert: No One Is Ready for What&#39;s Coming in 2 Years | Roman Yampolskiy](https://www.youtube.com/watch?v=00RHph_eok4)**

This episode is brought to you by Higgsfield — the AI video platform with Cinema Studio 2.5, built for creators who want cinematic ...

📺 Silicon Valley Girl

👁️ 32K • 👍 814 • 💬 150 • ⏱️ 45:43 • 1d ago

---

**[The World&#39;s First AI TED Talk](https://www.youtube.com/watch?v=N1X7vMp9DZ4)**

ChatGPT was recently asked what it would say to humans if it could give a TED Talk. It gave a surprisingly thoughtful answer that ...

📺 TED

👁️ 46K • 👍 2K • 💬 689 • ⏱️ 3:28 • 1d ago

---

**[The 2026 AI 50 List: Top Artificial Intelligence Companies](https://www.youtube.com/watch?v=mKEr3NKBYSk)**

Artificial intelligence has become part of our lives, increasingly core to how we work, search for information and express ideas.

📺 Forbes

👁️ 2K • 👍 80 • ⏱️ 5:39 • 7h ago

---

**[Donald Trump Posted This AI Image of Jesus…](https://www.youtube.com/watch?v=-Z4SHvUa5gw)**

discord.gg/nickjones.

📺 Nick Jones

👁️ 17K • 👍 804 • 💬 507 • ⏱️ 8:37 • 1d ago

---

**[AI Robots Are Glitching BAD… We Might Have A Problem! (2026)](https://www.youtube.com/watch?v=6p1Me03BPhM)**

AI robots failing and glitching 2026 is becoming impossible to ignore. From humanoid robots malfunctioning to AI systems ...

📺 MindSeeded

👁️ 75K • 👍 5K • 💬 793 • ⏱️ 14:10 • 1d ago

---

**[AI News: Huge Updates From Anthropic, OpenAI and Google](https://www.youtube.com/watch?v=bIrzOQtnp8w)**

Here's the AI News you probably missed this week. Build AI apps that actually scale. Learn more about Crusoe Managed ...

📺 Matt Wolfe

👁️ 72K • 👍 3K • 💬 138 • ⏱️ 36:44 • 1d ago

---

**[LIVE: Sanders, Labor Leaders Call on Congress to Protect Workers from AI](https://www.youtube.com/watch?v=DdJfeSMB99g)**

The same oligarchs who shipped jobs overseas now want to replace tens of millions of American workers with AI. Our message to ...

📺 Senator Bernie Sanders

👁️ 14K • 👍 1K • 💬 408 • ⏱️ 45:01 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 258,064 • ❤️ 952 • 1d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 82,000 • ❤️ 826 • 3d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,454 • ❤️ 862 • 4d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 3,116 • ❤️ 450 • 1d ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 442,900 • ❤️ 439 • 2d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 103,847 • ❤️ 1,398 • 2d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 66,552 • ❤️ 395 • 6d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 35,870 • ❤️ 1,107 • 2d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 3,778,070 • ❤️ 2,150 • 8d ago

---

**[HY-World-2.0](https://huggingface.co/tencent/HY-World-2.0)**

*Tencent*

HY-World 2.0 is a multi-modal framework for generating and reconstructing 3D worlds from text, images, or video. It produces editable 3D assets like meshes and Gaussian Splattings, enabling applications in game development and simulation.

`image-to-3d`

⬇️ 0 • ❤️ 310 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 23 • 💬 1 • ⭐ 19,283 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 4 • 💬 2 • ⭐ 1,633 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)**

*Team HY-World, Chenjie Cao, Xuhui Zuo et al. (45 authors)*

HY-World 2.0 is a multi-modal world model framework that generates high-fidelity 3D Gaussian Splatting scenes from diverse inputs using specialized modules for panorama generation, trajectory planning, world expansion, and composition, along with an enhanced rendering platform for interactive 3D exploration.

▲ 80 • 💬 4 • ⭐ 1,134 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14268) • [💻 code](https://github.com/Tencent-Hunyuan/HY-World-2.0) • [🔗 project](https://3d-models.hunyuan.tencent.com/world/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 47 • 💬 2 • ⭐ 51,345 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,179 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 18,079 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 159 • 💬 2 • ⭐ 60,409 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 53 • 💬 1 • ⭐ 77,188 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 53 • 💬 4 • ⭐ 1,859 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,764 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 47.8k • 🔱 6.3k • 1h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 37.7k • 🔱 1.8k • 12h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 36.0k • 🔱 7.2k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 29.8k • 🔱 3.3k • 6h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.2k • 🔱 523 • 7h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 6d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 5.2k • 🔱 874 • 4h ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.9k • 🔱 1.1k • 23d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.7k • 🔱 181 • 1d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.6k • 🔱 457 • 10d ago

---

---

*Generated by PeekDeck - A glance is all you need*
