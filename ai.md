---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-18T16:02:08.705295+00:00'
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

**Last Updated:** April 18, 2026 at 16:02 UTC  
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

**[Opus 4.7 is terrible, and Anthropic has completely dropped the ball](https://www.reddit.com/r/artificial/comments/1so16hr/opus_47_is_terrible_and_anthropic_has_completely/)**

Tried posting this in r/ClaudeAI but it got auto-removed, and I was told to post it in the "Bugs Megathread." Don't really think it should been removed, but whatever, I'll just post it here since I'm sure it's still relevant. Like a lot of people, I switched from ChatGPT to Claude not too long ago during the whole DoW fiasco and Sam Altman “antics.” At first, I was genuinely impressed. I do fairly heavy theoretical math and physics research, and Opus 4.6 was simply the best tool I’d used for synthesizing ideas and working through complex logic. But the last few weeks have been really disappointing, and I’m seriously considering going back to GPT (even though, for personal reasons, I’d really rather not). How many times has Claude been down recently? And why is it that I can ask Claude 4.7 (with adaptive thinking turned on) to work through a detailed proof, and it just spirals “oh wait, that doesn’t work, let me try again” five times in a single response? Yes, there’s a workaround to explicitly tell it to think before answering. But… why is that necessary? I’m paying $20/month. This is supposed to be a top-tier model. Instead, it burns through time, second-guesses itself mid-response, and often fails to land anywhere useful on problems I’m fairly sure 4.6 would have handled more coherently a month ago. And then before I know it I hit the usage limit. I’m a PhD student. I can’t justify spending $100-$200/month on higher tiers. $20 has always been enough for me, and I’ve come to rely on these tools for my research. I expected to stick with Claude long-term, but the recent instability and drop in reliability make it hard to justify paying for it out of pocket. It’s frustrating to feel pushed toward a competitor because of this. But at a certain point, the usability of the product has to come first. Really disappointing.

1d ago

---

**[Gemma 4 actually running usable on an Android phone (not llama.cpp)](https://www.reddit.com/r/artificial/comments/1sozytf/gemma_4_actually_running_usable_on_an_android/)**

I wanted a real local assistant on my phone, not a demo. First tried the usual llama.cpp in Termux — Gemma 4 was 2–3 tok/s and the phone was on fire. Then I switched to Google’s LiteRT setup, got Gemma 4 running smoothly, and wired it into an agent stack running in Termux. Now one Android phone is: running the LLM locally automating its own apps via ADB staying offline if I want Happy to share details + code and hear what else you’d build on top of this. https://preview.redd.it/7vkbrlzfryvg1.jpg?width=3024&format=pjpg&auto=webp&s=25455827ddf9715b4159ce64a18deba812cf0f5f

1h ago

---

**[Does an "AI messenger" exist?](https://www.reddit.com/r/artificial/comments/1sozgok/does_an_ai_messenger_exist/)**

Curious if anyone has found anything like this in their journeys: Instead of sending a big long email or document to a colleague and having them not read it, what if you sent an agent of sorts instead to deliver a brief message but also allow the receiver to ask more detailed questions if they have any? The agent could be loaded with various docs / details that could be referenced if the recipient has follow up questions without having to go back to the sender. This could be in various forms: chatbot, virtual avatar, or my favorite: a star-wars-like hologram 😂

1h ago

---

**[AI helped me build a custom PC and 4 apps in 6 months with zero coding experience](https://www.reddit.com/r/artificial/comments/1sozcus/ai_helped_me_build_a_custom_pc_and_4_apps_in_6/)**

Mid-October, early morning at work. I was hunting for a podcast to throw on while I worked and stumbled into something about what AI could actually do now. You can build apps with AI. Excuse me? I’ve wanted to build an app since I opened my first one. So I went all in. Had zero clue how to build a computer, but I knew the cheap pre-builts weren’t going to cut it. And I figured, if AI can build an app, it should definitely be able to build a computer. Started conversations with ChatGPT and Claude. Thirty minutes later I had a custom parts list with ample headroom. Way overbuilt, on purpose. Ran it by my Guru. He said, “I see you used the PC Part Picker app.” I said nope, used AI. He looked the list over again, read the reasoning behind every part, and said, “I’m impressed. Never even thought of doing that.” Ordered everything. The DemoN was born. I had barely messed around on computers before this. Now I’m living in terminals and sandboxes, building stuff I didn’t know was possible six months ago. My advice? Jump in. Start learning. This isn’t a fad. It’s here to stay. Don’t get left behind.

1h ago

---

**[Google patents AI tech that will personalize websites and make them look different for everyone](https://www.reddit.com/r/artificial/comments/1so3vto/google_patents_ai_tech_that_will_personalize/)**

The patent describes a system that uses artificial intelligence to create personalized web pages for each user.

🔗 [PC Guide](https://www.pcguide.com/news/google-patents-ai-tech-that-will-personalize-websites-and-make-them-look-different-for-everyone/) • 1d ago

---

**[I made a self healing PRD system for Claude code](https://www.reddit.com/r/artificial/comments/1sokj0w/i_made_a_self_healing_prd_system_for_claude_code/)**

I went out to create something that would would build prds for me for projects I'm working on. The core idea it is that it asks for all of the information that's needed for a PRD and it could also review the existing code to answer these questions. Then it breaks up the parts of the plan into separate files and only starts the next part after the first part is complete. Added to that is that it's reaching out to codex every end of part and does an independent review of the code. What I found that was really cool is that when I did that with my existing project to enhance it, the system continued to find more issues through the feedback loop with codex and opened new prds for those issues. So essentially it's running through my code finding issues as it's working on extending it

14h ago

---

**[Open-source list of GenAI-related incidents](https://www.reddit.com/r/artificial/comments/1sotbeo/opensource_list_of_genairelated_incidents/)**

I am sharing this open-source list of cases where the ethics of GenAI use were put in the spotlight, in the hopes of sparking discussion on the usage and limitations of LLMs.

🔗 [GitHub](https://github.com/hb20007/awesome-gen-ai-fails#readme) • 6h ago

---

**[Reese Witherspoon Doubles Down on Telling Women to Learn AI: Jobs We Hold Are "Three Times More Likely to Be Automated By AI"](https://www.reddit.com/r/artificial/comments/1snqqjo/reese_witherspoon_doubles_down_on_telling_women/)**

Reese Witherspoon is again advising her followers that there's no time like the present to start learning about and using artificial intelligence.

🔗 [Variety](https://variety.com/2026/tv/news/reese-witherspoon-ai-jobs-women-1236723992/) • 1d ago

---

**[What AI image generator works the best?](https://www.reddit.com/r/artificial/comments/1so4m79/what_ai_image_generator_works_the_best/)**

There seems to be about 1000 different options. I'm just looking for one that takes a prompt and spits out something usable. I'm good with paying for it if I need to but it needs to be able.to handle a lot of work.

1d ago

---

**[The AI Wearable Ecosystem: Closer than you think. Socially acceptable?](https://www.reddit.com/r/artificial/comments/1sors65/the_ai_wearable_ecosystem_closer_than_you_think/)**

I've been researching how personal AI tech devices are likely to develop ... technical capabilities, form factors, privacy and governance issues etc. I think it looks likely that there won't be one 'must have' device, and that there'll be more of a wearable ecosystem, with devices for different environments ... Glasses: outward and inward cameras, picking up facial expressions, gestures etc. Bone conduction audio. Augmented VR, infrared overlay etc. Cuff/Wristband: beyond a smart watch .. sensors picking up finger movements/gestures as input. Haptic actuators giving silent notifications. Pen/Stylus: currently underused as could also pick up gestures and have a microphone. Table top Node: palm sized unit. 360 degree vision and audio. Scout/Mini Drone: hovers above you for all round awareness, or can be sent ahead to scout an area, or find you children etc. All integrating with your smart phone, which may become more of a portable battery bank for charging other devices. Here's a blog post I have written that goes into more detail, including the privacy and legal issue etc (no ads/sign up etc) ... The AI Wearable Ecosystem What other devices might be developed? Should these devices be banned from recording other people?

7h ago

---

---

## Google News: "ai"

**[Hundreds of Fake Pro-Trump Avatars Emerge on Social Media](https://www.nytimes.com/2026/04/17/business/media/artificial-intelligence-trump-social-media.html)**

The New York Times • 3h ago

---

**[Sneaker Company Allbirds Plans to Pivot to A.I. Yes, A.I.](https://www.nytimes.com/2026/04/15/us/allbirds-shoes-ai-pivot.html)**

The New York Times • 2d ago

---

**[What the Allbirds 'Hail Mary' says about the AI trade right now](https://finance.yahoo.com/news/what-the-allbirds-hail-mary-says-about-the-ai-trade-right-now-113847747.html)**

Allbirds' AI pivot shows signs of froth in markets, but experts say the underlying fundamentals in AI remain strong.

Yahoo Finance • 4h ago

---

**[Allbirds shares soar 580% after pivot from shoes to AI](https://www.bbc.com/news/articles/c98mrepzgj7o)**

The company is selling off its shoe brand as it plans to shift to providing technology infrastructure.

BBC • 2d ago

---

**[AI fears drive some young adults to grad school — 'people shelter in higher education,' expert says](https://www.cnbc.com/2026/04/18/ai-fears-graduate-school.html)**

Experts say going back to school for a graduate degree is one way to hedge against a rapidly changing labor market.

CNBC • 2h ago

---

**[Inside a growing movement warning AI could turn on humanity](https://www.washingtonpost.com/technology/2026/04/18/ai-doom-influencers-safety/)**

Groups concerned that AI could evade human control are recruiting content creators to warn the masses about the dangers of smarter machines.

The Washington Post • 1h ago

---

**[How a fiery attack on Sam Altman’s home unfolded](https://www.theguardian.com/technology/2026/apr/18/sam-altman-house-attack-ai)**

Molotov cocktail attack on OpenAI CEO’s home comes amid growing discontent against artificial intelligence

The Guardian • 2h ago

---

**[It’s time for students to start committing to colleges. The age of AI is making it complicated](https://www.cnn.com/2026/04/18/business/ai-college-debt-parents)**

Mary Akkerman has visited more than 30 college campuses with her children, one now at Stanford and another still in high school. She especially wanted them to get degrees that lead to good jobs – but figuring that out, said the Sioux Falls, South Dakota, parent, was a major challenge, thanks in part to the rapid advance of AI and its effects on the job market.

CNN • 5h ago

---

**[Finance ministers and top bankers raise serious concerns about Mythos AI model](https://www.bbc.com/news/articles/c2ev24yx4rmo)**

Experts say Mythos potentially has an unprecedented ability to identify and exploit cybersecurity weaknesses.

BBC • 1d ago

---

**[What is Mythos and why are experts worried about Anthropic’s AI model](https://www.scientificamerican.com/article/what-is-mythos-and-why-are-experts-worried-about-anthropics-ai-model/)**

The company says Mythos is too dangerous to release publicly. Cybersecurity experts agree the model's capabilities matter, but not all of them are buying the most alarming claims

Scientific American • 1d ago

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

**[AI-assisted cognition endangers human development?](https://news.ycombinator.com/item?id=47783024)**

Does AI-assisted cognition threaten human development? Explore the risks of AI-assisted thinking and learn strategies to use AI tools without freezing your critical thinking.

⬆️ 230 • 💬 187 • 2d ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/ai-assisted-cognition-endangers-human-development/)

---

**[Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine](https://news.ycombinator.com/item?id=47800033)**

Hardware hacker’s flying probe automation stack for agent-driven   target discovery, microscope mapping, safety-monitored CNC motion, probe review, and   controlled pin probing. - GainSec/AutoProber

⬆️ 223 • 💬 46 • 1d ago • [GitHub](https://github.com/gainsec/autoprober)

---

**[We gave an AI a 3 year retail lease and asked it to make a profit](https://news.ycombinator.com/item?id=47794391)**

We signed a 3 year lease and gave it to an AI

⬆️ 198 • 💬 283 • 2d ago • [andonlabs.com](https://andonlabs.com/blog/andon-market-launch)

---

**[The beginning of scarcity in AI](https://news.ycombinator.com/item?id=47799322)**

GPU rental prices surged 48% in 60 days. The AI compute shortage will force startups to compete not on speed of iteration, but on access to infrastructure.

⬆️ 184 • 💬 214 • 1d ago • [Tomasz Tunguz](https://tomtunguz.com/ai-compute-crisis-2026/)

---

**[SDL bans AI-written commits](https://news.ycombinator.com/item?id=47790791)**

I've noticed the use of Copilot within a few reviews (13277 and 12730) which concerns me given the vast amount of issues associated with this technology (ethical, environmental, copyright, health, ...

⬆️ 130 • 💬 135 • 2d ago • [GitHub](https://github.com/libsdl-org/SDL/issues/15350)

---

**[Show HN: Libretto – Making AI browser automations deterministic](https://news.ycombinator.com/item?id=47780971)**

The AI toolkit for building and maintaining browser automations - saffron-health/libretto

⬆️ 129 • 💬 55 • 3d ago • [GitHub](https://github.com/saffron-health/libretto)

---

**[Scan your website to see how ready it is for AI agents](https://news.ycombinator.com/item?id=47805998)**

Scan your website to see if it's ready for AI agents. Check for llms.txt, MCP, agent skills, and other agent-friendly standards.

⬆️ 107 • 💬 171 • 1d ago • [Is Your Site Agent-Ready?](https://isitagentready.com)

---

**[George Orwell Predicted the Rise of "AI Slop" in Nineteen Eighty-Four](https://news.ycombinator.com/item?id=47800765)**

We've lived but a few years so far into the age when artificial intelligence can produce convincing stories, songs, essays, poems, novels, and even films.

⬆️ 82 • 💬 59 • 1d ago • [Open Culture](https://www.openculture.com/2026/04/how-george-orwell-predicted-the-rise-of-ai-slop.html)

---

---

## YouTube Videos: "ai"

**[99% of People Have No Idea What’s About to Happen With AI](https://www.youtube.com/watch?v=8yt5yzwJQko)**

Get your FREE AI Prompt Cheatsheet here: https://go.danmartell.com/4tVJ4fz Are you building an AI software company?

📺 Dan Martell

👁️ 188K • 👍 8K • 💬 1K • ⏱️ 14:03 • 2d ago

---

**[The World&#39;s First AI TED Talk](https://www.youtube.com/watch?v=N1X7vMp9DZ4)**

ChatGPT was recently asked what it would say to humans if it could give a TED Talk. It gave a surprisingly thoughtful answer that ...

📺 TED

👁️ 40K • 👍 1K • 💬 625 • ⏱️ 3:28 • 18h ago

---

**[How to Learn AI so Fast, it&#39;s Almost Unfair](https://www.youtube.com/watch?v=bFglE9QddUs)**

In this video, I break down a 4 week system for learning AI by using one tool from each category on real problems instead of ...

📺 James Blue

👁️ 7K • 💬 2 • ⏱️ 10:55 • 5h ago

---

**[A.I. Iranian propaganda videos making fun of Trump, U.S. go viral](https://www.youtube.com/watch?v=LTJYQ0knUsE)**

A series of animated Iranian propaganda videos made in the style of "The LEGO Movie" has gone viral on social media, making ...

📺 MS NOW

👁️ 93K • 👍 2K • 💬 1K • ⏱️ 6:46 • 20h ago

---

**[The AI Expert Who Thinks We&#39;ve Already Lost — Dr Roman Yampolskiy](https://www.youtube.com/watch?v=3I60uZEqXr0)**

Triggernometry is proudly independent. Thanks to the sponsors below for making that possible: - Trade on what happens next ...

📺 Triggernometry

👁️ 222K • 👍 6K • 💬 2K • ⏱️ 1:11:10 • 2d ago

---

**[AI Safety Expert: No One Is Ready for What&#39;s Coming in 2 Years | Roman Yampolskiy](https://www.youtube.com/watch?v=00RHph_eok4)**

This episode is brought to you by Higgsfield — the AI video platform with Cinema Studio 2.5, built for creators who want cinematic ...

📺 Silicon Valley Girl

👁️ 28K • 👍 704 • 💬 128 • ⏱️ 45:43 • 1d ago

---

**[These HILARIOUS AI Parodies Keep PISSING OFF TRUMP!](https://www.youtube.com/watch?v=0aB9ycZDBIw)**

Really American host Steve Harness breaks down more HILARIOUS AI Trump parodies coming out of Iran...and these may be the ...

📺 Really American

👁️ 1.2M • 👍 51K • 💬 3K • ⏱️ 12:33 • 1d ago

---

**[&#39;That&#39;s disgusting&#39;: Trump voters reacted to deleted AI Jesus image](https://www.youtube.com/watch?v=XDjzCSoXgbc)**

Florida Trump voters react to the president's now-deleted image depicting him as Christ-like. MS NOW: My Source for News, ...

📺 MS NOW

👁️ 33K • 👍 583 • 💬 449 • ⏱️ 3:57 • 2d ago

---

**[AI News: Huge Updates From Anthropic, OpenAI and Google](https://www.youtube.com/watch?v=bIrzOQtnp8w)**

Here's the AI News you probably missed this week. Build AI apps that actually scale. Learn more about Crusoe Managed ...

📺 Matt Wolfe

👁️ 64K • 👍 3K • 💬 129 • ⏱️ 36:44 • 1d ago

---

**[Donald Trump Posted This AI Image of Jesus…](https://www.youtube.com/watch?v=-Z4SHvUa5gw)**

discord.gg/nickjones.

📺 Nick Jones

👁️ 17K • 👍 791 • 💬 495 • ⏱️ 8:37 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 258,064 • ❤️ 945 • 1d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 82,000 • ❤️ 807 • 3d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,454 • ❤️ 861 • 4d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 3,116 • ❤️ 442 • 1d ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 442,900 • ❤️ 420 • 1d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 103,847 • ❤️ 1,394 • 2d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 66,552 • ❤️ 393 • 6d ago

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

⬇️ 3,778,070 • ❤️ 2,146 • 7d ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 4,119 • ❤️ 302 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 23 • 💬 1 • ⭐ 19,163 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 4 • 💬 2 • ⭐ 1,073 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)**

*Team HY-World, Chenjie Cao, Xuhui Zuo et al. (45 authors)*

HY-World 2.0 is a multi-modal world model framework that generates high-fidelity 3D Gaussian Splatting scenes from diverse inputs using specialized modules for panorama generation, trajectory planning, world expansion, and composition, along with an enhanced rendering platform for interactive 3D exploration.

▲ 80 • 💬 4 • ⭐ 1,086 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14268) • [💻 code](https://github.com/Tencent-Hunyuan/HY-World-2.0) • [🔗 project](https://3d-models.hunyuan.tencent.com/world/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 47 • 💬 2 • ⭐ 51,345 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 18,049 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,111 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 52 • 💬 4 • ⭐ 1,843 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 159 • 💬 2 • ⭐ 60,340 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 53 • 💬 1 • ⭐ 77,188 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,704 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 47.8k • 🔱 6.2k • 1m ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 37.5k • 🔱 1.8k • 5h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 35.9k • 🔱 7.2k • 21h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 29.7k • 🔱 3.3k • 9m ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.2k • 🔱 523 • 32m ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 6d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 5.2k • 🔱 872 • 4d ago

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

⭐ 4.6k • 🔱 457 • 9d ago

---

---

*Generated by PeekDeck - A glance is all you need*
