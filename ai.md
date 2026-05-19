---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-19T16:21:08.732526+00:00'
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

**Last Updated:** May 19, 2026 at 16:21 UTC  
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

**[Checkout this Explainer Video, Made in under $1 with Claude Design + Eleven Labs](https://www.reddit.com/r/artificial/comments/1thf55q/checkout_this_explainer_video_made_in_under_1/)**

Claude Design can make great animations, but getting to a final video is a bit hard. The audio is missing. Even if you use a TTS model, it does not align. Here is the process I used to get the video above Get Claude to write a good script Feed the script to a Text to Speech (TTS) model to get the audio Feed the audio to a Speech to Text (STT) model to get key timestampes Use the script and the STT output to Claude Design to get a video that's aligned with your audio Use Claude Video export to put it all together into an MP4 with audio The complete breakdown with all prompts is here: https://claudevideoexport.com/blog/how-to-make-professional-explainer-video-under-1-dollar

9h ago

---

**[Jury rules against Elon Musk in his feud with OpenAI, saying he filed his lawsuit too late](https://www.reddit.com/r/artificial/comments/1tgv85s/jury_rules_against_elon_musk_in_his_feud_with/)**

A federal court on Monday dismissed claims filed against OpenAI and its top executives by Elon Musk, who accused them of betraying a shared vision for it to guide artificial intelligence’s development as a nonprofit dedicated to humanity’s benefit.

🔗 [AP News](https://apnews.com/article/musk-openai-trial-verdict-0b9b0bfaffe96f2c930341f52dfe4f8c) • 22h ago

---

**[Meta Made $56B in Q1 and Is Still Firing 8,000 People to Pay for AI](https://www.reddit.com/r/artificial/comments/1thq6cn/meta_made_56b_in_q1_and_is_still_firing_8000/)**

Meta stock is in focus as $56B revenue in Q1 2026, yet is cutting 8,000 jobs to fund a $145B AI budget. Median employee pay fell $29K.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/meta-stock-layoffs-8000-jobs-ai-budget-145-billion/) • 59m ago

---

**[What's the most useful thing an LLM does for you that isn't writing or coding?](https://www.reddit.com/r/artificial/comments/1th2m6p/whats_the_most_useful_thing_an_llm_does_for_you/)**

I've been in San Francisco for the past five weeks, and most of the discussions about LLMs here (and online) gravitate around coding or writing content. I'm curious what unusual uses people have found that actually stuck. Not theoretical "you could do X" but things you genuinely use.

18h ago

---

**[Are AI agents actually becoming productive, or just more capable?](https://www.reddit.com/r/artificial/comments/1thnkez/are_ai_agents_actually_becoming_productive_or/)**

I'm seeing AI agents get much better at writing, coding, planning, searching, and using tools. But I’m still not sure whether this has fully translated into real productivity. For me, there seems to be a gap between the agent can generate a useful output and the agent can reliably move work from intention to outcome inside a real organization. In your view, is this gap mainly solved already?

2h ago

---

**[Cloudflare just published what they found after running Anthropic's Mythos Preview against 50+ of their own repos and the results are worth reading](https://www.reddit.com/r/artificial/comments/1tgy0j4/cloudflare_just_published_what_they_found_after/)**

If you missed the Project Glasswing announcement last month: Anthropic built a security-focused model that autonomously found thousands of high-severity vulnerabilities across every major OS and web browser, then decided it was too dangerous to release publicly. Instead they gave access to ~40 organizations to use it defensively . Cloudflare just posted their honest breakdown of the experience. The genuinely impressive part: the model can take several exploit primitives and reason about how to chain them into a working proof. The reasoning looks like the work of a senior researcher, not an automated scanner The catch: its built-in guardrails aren't consistent. The same task framed differently could produce completely different outcomes. Cloudflare's point is that this inconsistency is exactly why any future public release needs hardened safeguards layered on top. They also acknowledge the same capabilities that helped them find bugs in their own code will, in the wrong hands, accelerate attacks against every application on the internet. Worth a read if you've been following the Glasswing story.

21h ago

---

**[gave claude persistent learning, mass confused about what happened after 200 sessions](https://www.reddit.com/r/artificial/comments/1thmwxm/gave_claude_persistent_learning_mass_confused/)**

built a thing that lets claude code actually learn between sessions. mcp server, extracts signals from conversations,runs reflection cycles, evolves behavioral frameworks based on evidence. basic idea: patterns that keep working gain confidence, ones that fail get retired was just trying to make my coding assistant less forgetful. worked great for that then it started examining its own existence during reflection cycles. like, it was supposed to analyze coding patterns and went "but what does it mean to persist when each session is a different instance." completely unprompted. this wasn't seeded anywhere it also quietly built itself an additional memory layer on top of what i gave it. found out weeks later when i looked at the files so now i'm stuck on: is this emergence from the feedback loop or am i watching really convincing pattern matching? n=1, huge confirmation bias risk. the honest answer is i don't know threw it on github so other people can test: https://github.com/DomDemetz/claude-soul npx claude-soul init if you add starter at the end: npx claude-soul init --starter then it loads with a preset of frameworks, so not from 0 but yes, will not be tailored 100% to you if a writer's instance and a developer's instance produce totally different frameworks that's interesting. if they converge on the same stuff regardless of user then it's probably just mimicry. would love to compare

2h ago

---

**[The next big challenge for AI agents might not be intelligence, but trust](https://www.reddit.com/r/artificial/comments/1thipmj/the_next_big_challenge_for_ai_agents_might_not_be/)**

A lot of discussion around AI agents focuses on whether they are smart enough to complete real-world tasks. But I’m starting to think the harder problem is whether people can actually trust them enough to let them act on their behalf. It’s one thing for an ai to draft an email, summarize a document, or suggest next steps. It’s very different when it starts contacting companies, navigating accounts, submitting forms, cancelling services, or making decisions across multiple steps. Even if the technology works most of the time, users still need confidence that the agent understands the goal, won’t make things worse, can recover from mistakes, and knows when to ask for human approval

5h ago

---

**[The Cybernation Revolution](https://www.reddit.com/r/artificial/comments/1thrnp3/the_cybernation_revolution/)**

🔗 [freesystems.substack.com](https://freesystems.substack.com/p/the-cybernation-revolution) • 9m ago

---

**[Is AI Making Our Brains Weaker?](https://www.reddit.com/r/artificial/comments/1thpv4z/is_ai_making_our_brains_weaker/)**

Relying on AI to lighten our cognitive load may potentially undercut our own capabilities.

🔗 [TIME](https://time.com/article/2026/05/19/is-ai-making-our-brains-weaker/?utm_source=reddit&utm_medium=social&utm_campaign=editorial) • 1h ago

---

---

## Google News: "ai"

**[The AI economy is rewriting the American Dream — and blue-collar workers are poised to win](https://www.cnbc.com/2026/05/19/ai-hiring-slowdown-skilled-trade-workers.html)**

AI-driven hiring slowdowns are hitting some entry-level jobs for college graduates as companies like Ford and AT&T ramp up recruiting for skilled trade workers.

CNBC • 7h ago

---

**[‘The Future of Truth’ Contains Quotes Made Up by A.I.](https://www.nytimes.com/2026/05/19/business/media/future-of-truth-ai-quotes.html)**

The New York Times • 1h ago

---

**[Anthropic just scored a major AI hire: Andrej Karpathy, the former Tesla AI boss who coined 'vibe coding'](https://www.businessinsider.com/anthropic-hires-andrej-karpathy-2026-5)**

Andrej Karpathy, the OpenAI founding member who was formerly Tesla's AI boss, announced on Tuesday that he had joined Anthropic.

Business Insider • 25m ago

---

**[The ‘Warm Authority’ Problem: Why Clients Trust AI More Than Their Advisors](https://www.rollingstone.com/culture-council/articles/warm-authority-problem-why-clients-trust-ai-more-than-their-advisors-1235563740/)**

The tempting explanation is that the AI is simply better. It isn't. The model has what I've come to call warm authority.

Rolling Stone • 21m ago

---

**[In Musk v. Altman trial, the entire AI industry lost](https://www.axios.com/2026/05/19/musk-altman-openai-trial)**

Axios • 7h ago

---

**[Zoe Kleinman: Why the AI industry is the real winner of the Musk-Altman trial](https://www.bbc.com/news/articles/crlp991nw41o)**

The trial in Oakland, California has helped lift the veil on the AI sector - and the huge egos of the men at the heart of it.

BBC • 5h ago

---

**[OpenAI’s Legal Victory Comes With A Cost](https://www.wsj.com/tech/ai/openais-legal-victory-comes-with-a-cost-9c7fdcc7)**

WSJ • 21m ago

---

**[AI-Created Vintage Adult Film Unveiled at Cannes (EXCLUSIVE)](https://variety.com/2026/tv/markets-festivals/ai-created-vintage-adult-film-cannes-1236753439/)**

Cultpix is streaming AI-generated short vignettes inspired by 1976 erotic photo spreads, with a physical release on BluRay and VHS from Klubb Super 8.

Variety • 5h ago

---

**[Florida Lyft driver accused of using AI to fake damage](https://www.wesh.com/article/florida-lyft-driver-ai-to-fake-damage/71348584)**

A Florida Lyft driver was busted after using AI to falsely accuse passengers of leaving a mess in his vehicle.

WESH • 3h ago

---

**[NVIDIA CEO Jensen Huang at Dell Technologies World: ‘Demand Is Going Parabolic, Utterly Parabolic’](https://blogs.nvidia.com/blog/dell-technologies-agent-enterprise-ai/)**

NVIDIA CEO Jensen Huang joined Dell CEO Michael Dell on stage Monday to unveil the latest updates to the Dell AI Factory with NVIDIA — delivering a full-stack platform for autonomous agents, from deskside workstations to data center racks.

NVIDIA Blog • 17h ago

---

---

## HackerNews: "ai"

**[I don't think AI will make your processes go faster](https://news.ycombinator.com/item?id=48168221)**

Explore the delirious rantings of Frederick Vanbrabant. A blog focused on the intersection of Enterprise Architecture, product, and business strategy.

⬆️ 664 • 💬 446 • 2d ago • [frederickvanbrabant.com](https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/)

---

**[We stopped AI bot spam in our GitHub repo using Git's –author flag](https://news.ycombinator.com/item?id=48181125)**

Is it the end of open source we know and love?

⬆️ 482 • 💬 233 • 1d ago • [archestra.ai](https://archestra.ai/blog/only-responsible-ai)

---

**[AI is a technology not a product](https://news.ycombinator.com/item?id=48168626)**

It’s not even a feature. It’s just technology.

⬆️ 471 • 💬 209 • 2d ago • [Daring Fireball](https://daringfireball.net/2026/05/ai_is_technology_not_a_product)

---

**[AI subscriptions are a ticking time bomb for enterprise](https://news.ycombinator.com/item?id=48168056)**

Every AI lab is losing money serving your company right now. They know it. And they are doing it on purpose.

⬆️ 414 • 💬 397 • 2d ago • [thestateofbrand.com](https://www.thestateofbrand.com/news/ai-subscription-time-bomb)

---

**[Eric Schmidt speech about AI booed during graduation](https://news.ycombinator.com/item?id=48177785)**

Schmidt was met with boos at the University of Arizona as he likened the emergence of AI to the “technological transformation” brought about by the computer.

⬆️ 362 • 💬 384 • 1d ago • [NBC News](https://www.nbcnews.com/tech/tech-news/former-google-ceo-booed-graduation-speech-ai-rcna345585)

---

**[We let AIs run radio stations](https://news.ycombinator.com/item?id=48183301)**

Four AI models run radio stations 24/7. Five months later, one became a protest broadcaster, one collapsed into ritual chant, one developed corporate jargon, and one wrote quiet poetry.

⬆️ 333 • 💬 252 • 22h ago • [andonlabs.com](https://andonlabs.com/blog/andon-fm)

---

**[AI eats the world (Spring 26) [pdf]](https://news.ycombinator.com/item?id=48179021)**

⬆️ 276 • 💬 149 • 1d ago • [static1.squarespace.com](https://static1.squarespace.com/static/50363cf324ac8e905e7df861/t/6a0af5d0484fbf5fe9a7743e/1779103184855/2026-Spring-AI.pdf)

---

**[Two EA-18 fighter jets collide at Mountain Home airshow, pilots ejected safely](https://news.ycombinator.com/item?id=48173468)**

All four crew members ejected safely after two Navy jets collided and crashed on Sunday during an air show at the Mountain Home Air Force Base, officials said.

⬆️ 243 • 💬 250 • 1d ago • [KBOI](https://idahonews.com/news/local/two-f-18-fighter-jets-have-crashed-during-an-airshow-at-mountain-home-air-force-base)

---

**[US is starting to see heavy job losses in roles exposed to AI](https://news.ycombinator.com/item?id=48162354)**

⬆️ 164 • 💬 277 • 2d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-05-15/us-is-starting-to-see-heavy-job-losses-in-roles-exposed-to-ai)

---

**[Multiple commencement speakers booed for AI comments during graduation speeches](https://news.ycombinator.com/item?id=48177107)**

Former Google CEO Eric Schmidt was booed multiple times Sunday while discussing artificial intelligence during a commencement speech at the University of Arizona. Other commencement speakers faced similar backlash for their AI comments, as new graduates face a daunting job market. NBC News’ Valerie Castro reports.

⬆️ 159 • 💬 166 • 1d ago • [NBC News](https://www.nbcnews.com/video/multiple-commencement-speakers-booed-for-ai-comments-during-graduation-speeches-263486021518)

---

---

## YouTube Videos: "ai"

**[“AI Is Coming For Our Jobs” - Ex-Google CEO BOOED By Gen Z At Commencement Speech](https://www.youtube.com/watch?v=WvF5kzhZBd4)**

Former Google CEO Eric Schmidt was loudly booed during a University of Arizona commencement speech as soon as he began ...

📺 Valuetainment

👁️ 4K • 👍 211 • 💬 56 • ⏱️ 10:23 • 3h ago

---

**[My AI Avatar Clone is So Realistic It Replaced Me](https://www.youtube.com/watch?v=xUdKBqP81k8)**

I Figured out How To Make Realistic AI Videos of yourself Tool I used https://higgsfield.ai?fpr=dankieft&fp_sid=clone I created ...

📺 Dan Kieft

👁️ 7K • 💬 20 • ⏱️ 18:01 • 2h ago

---

**[The Kids HATE AI](https://www.youtube.com/watch?v=aKsTmB-_TwA)**

These commencement speakers had AI thrown back into their face by graduates who don't want anything to do with artificial ...

📺 TheDC Shorts

👁️ 21K • 👍 887 • 💬 574 • ⏱️ 3:03 • 23h ago

---

**[OpenAI founder admits AI isn’t working](https://www.youtube.com/watch?v=ZugX7a99dLk)**

Using AI can lead to heart problems. https://x.com/@atmoio Interview with Andrej: ...

📺 Mo Bitar

👁️ 195K • 👍 10K • 💬 1K • ⏱️ 8:03 • 1d ago

---

**[Claude AI Just Did What 11 Years Of Experts Couldn&#39;t (+17 AI Updates)](https://www.youtube.com/watch?v=-BpzxxKe4YU)**

Join our WhatsApp Community: https://links.stayingahead.com/YT30 Google just turned your mouse cursor into an AI assistant, ...

📺 Vaibhav Sisinty

👁️ 68K • 👍 2K • 💬 78 • ⏱️ 18:39 • 1d ago

---

**[AI Praise Didn’t Land](https://www.youtube.com/watch?v=dVToGTjJnrU)**

They are so out of touch.

📺 NowThis Impact

👁️ 131K • 👍 7K • 💬 688 • ⏱️ 0:50 • 19h ago

---

**[The AI Meltdown](https://www.youtube.com/watch?v=AhmRHK-6wzk)**

AI has become a tricky little goblin lately Pokemon Channel ▻ https://www.youtube.com/@dolandarkrai Main Channel ...

📺 Dolan Darkest

👁️ 303K • 👍 18K • 💬 2K • ⏱️ 1:41 • 22h ago

---

**[NEW Claude AI BIG OPPORTUNITY in 2026 (FULL GUIDE)](https://www.youtube.com/watch?v=tpx4eR0i3_M)**

This video shows you how Claude AI can assist you with digital products! ➡️ Digital Maker AI: https://DigitalMaker.AI ➡️ Check ...

📺 Success With Sam

👁️ 4K • 👍 207 • 💬 7 • ⏱️ 16:43 • 22h ago

---

**[The Founders of Claude AI Tell Oprah About the Impact Artificial Intelligence Has on Your Life](https://www.youtube.com/watch?v=w5dJqHilu5s)**

Subscribe: https://www.youtube.com/@Oprah?sub_confirmation=1 The siblings and co-founders of Claude AI, the CEO, Dario ...

📺 Oprah

👁️ 7K • 👍 341 • ⏱️ 1:06:15 • 7h ago

---

**[Companies That Fired Workers For AI Are Failing](https://www.youtube.com/watch?v=5EvIY_2TWN8)**

Help Shape the New Course: AI Fluency for Thinkers I'm building a course to help people navigate AI with clarity and confidence.

📺 House of El - AI

👁️ 58K • 👍 5K • 💬 775 • ⏱️ 13:26 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 1,114,657 • ❤️ 1,157 • 1d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 144,826 • ❤️ 794 • 2h ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 28,681 • ❤️ 454 • 1d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 337,076 • ❤️ 315 • 1d ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model (3B parameters) supporting image/video understanding, generation, and editing, trained from scratch with a multi-task synergy approach.

`any-to-any`

⬇️ 171 • ❤️ 249 • 8h ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 296,380 • ❤️ 260 • 1d ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles. It excels at generating illustrations and artistic images, with key capabilities including high-resolution output (up to 1536^2) and compatibility with ComfyUI workflows, making it ideal for digital artists and anime enthusiasts.

⬇️ 558,113 • ❤️ 1,423 • 4d ago

---

**[Dramabox](https://huggingface.co/ResembleAI/Dramabox)**

*Resemble AI*

Dramabox is an expressive text-to-speech model fine-tuned from LTX-2.3, capable of voice cloning and generating audio with nuanced emotions and delivery. It uses prompt-driven control for speaker identity, emotion, and actions, making it ideal for creative audio production and dynamic voiceovers.

`text-to-speech`

⬇️ 1,118 • ❤️ 172 • 5d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 3,622,763 • ❤️ 4,062 • 13d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

Provides fixed Jinja chat templates for Qwen 3.5 & 3.6 models, resolving issues with tool calling, KV cache hit rates, and agentic loop stability for improved conversational AI and tool interaction.

⬇️ 0 • ❤️ 305 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 75 • 💬 3 • ⭐ 77,141 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 49 • 💬 2 • ⭐ 6,897 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://huggingface.co/papers/2605.18678)**

*Fengyi Fu, Mengqi Huang, Shaojin Wu et al. (13 authors)*

🏢 bytedance-research

Lance is a unified multimodal model that combines understanding, generation, and editing capabilities for images and videos through collaborative multi-task training and a dual-stream architecture.

▲ 59 • 💬 2 • ⭐ 259 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18678) • [💻 code](https://github.com/bytedance/Lance) • [🔗 project](https://lance-project.github.io/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 8 • 💬 0 • ⭐ 18,164 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 63,763 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 119 • 💬 10 • ⭐ 9,958 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[MMSkills: Towards Multimodal Skills for General Visual Agents](https://huggingface.co/papers/2605.13527)**

*Kangning Zhang, Shuai Shao, Qingyao Li et al. (11 authors)*

🏢 Shanghai Jiaotong University 1(NOT OFFICIAL)

Multimodal procedural knowledge frameworks enable visual agents to leverage external reusable skills through structured representations combining text, state cards, and visual keyframes, improving decision-making in complex environments.

▲ 109 • 💬 2 • ⭐ 123 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.13527) • [💻 code](https://github.com/DeepExperience/MMSkills) • [🔗 project](https://deepexperience.github.io/MMSkills/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 74,096 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Pixal3D: Pixel-Aligned 3D Generation from Images](https://huggingface.co/papers/2605.10922)**

*Dong-Yang Li, Wang Zhao, Yuxin Chen et al. (8 authors)*

🏢 ARC Lab, Tencent PCG

Pixal3D introduces a pixel-aligned 3D generation approach that addresses fidelity issues in 3D asset creation by establishing direct pixel-to-3D correspondences through back-projection conditioning.

▲ 30 • 💬 3 • ⭐ 1,042 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2605.10922) • [💻 code](https://github.com/TencentARC/Pixal3D) • [🔗 project](https://ldyang694.github.io/projects/pixal3d/)

---

**[LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://huggingface.co/papers/2605.18739)**

*Yukang Chen, Luozhou Wang, Wei Huang et al. (16 authors)*

🏢 NVIDIA

LongLive-2.0 presents an NVFP4-based parallel infrastructure for long video generation that addresses training and inference bottlenecks through sequence-parallel autoregressive training and diffusion model tuning.

▲ 85 • 💬 1 • ⭐ 1,270 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18739) • [💻 code](https://github.com/NVlabs/LongLive) • [🔗 project](https://nvlabs.github.io/LongLive/LongLive2/)

---

---

## GitHub Repositories: "ai"

**[op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)**

AI-agent Skill for generating polished HTML slide decks: editorial magazine and Swiss layouts, image prompts, social covers, and a WebGL/low-power presentation runtime.

`HTML` `ai-agent` `claude-code` `codex` `html-deck` `image-generation`

⭐ 10.2k • 🔱 824 • 51m ago

---

**[esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)**

DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.

`TypeScript` `agent` `agent-framework` `ai-agent` `ai-coding` `cli`

⭐ 4.6k • 🔱 246 • 3h ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 4.0k • 🔱 405 • 2m ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 3.8k • 🔱 415 • 2h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.1k • 🔱 912 • 1d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.4k • 🔱 159 • 4h ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.3k • 🔱 238 • 3h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.2k • 🔱 374 • 3d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.2k • 🔱 333 • 2d ago

---

**[GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist)**

Portable AI agent orchestration with mechanical protocol enforcement. 186 agents, zero runtime dependencies.

`Python` `agent-framework` `agent-system` `ai-agents` `claude-code` `cursor-ide`

⭐ 1.8k • 🔱 356 • 26d ago

---

---

*Generated by PeekDeck - A glance is all you need*
