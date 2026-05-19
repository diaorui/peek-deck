---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-19T12:39:47.867040+00:00'
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

**Last Updated:** May 19, 2026 at 12:39 UTC  
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

**[Jury rules against Elon Musk in his feud with OpenAI, saying he filed his lawsuit too late](https://www.reddit.com/r/artificial/comments/1tgv85s/jury_rules_against_elon_musk_in_his_feud_with/)**

A federal court on Monday dismissed claims filed against OpenAI and its top executives by Elon Musk, who accused them of betraying a shared vision for it to guide artificial intelligence’s development as a nonprofit dedicated to humanity’s benefit.

🔗 [AP News](https://apnews.com/article/musk-openai-trial-verdict-0b9b0bfaffe96f2c930341f52dfe4f8c) • 18h ago

---

**[Checkout this Explainer Video, Made in under $1 with Claude Design + Eleven Labs](https://www.reddit.com/r/artificial/comments/1thf55q/checkout_this_explainer_video_made_in_under_1/)**

Claude Design can make great animations, but getting to a final video is a bit hard. The audio is missing. Even if you use a TTS model, it does not align. Here is the process I used to get the video above Get Claude to write a good script Feed the script to a Text to Speech (TTS) model to get the audio Feed the audio to a Speech to Text (STT) model to get key timestampes Use the script and the STT output to Claude Design to get a video that's aligned with your audio Use Claude Video export to put it all together into an MP4 with audio The complete breakdown with all prompts is here: https://claudevideoexport.com/blog/how-to-make-professional-explainer-video-under-1-dollar

5h ago

---

**[What's the most useful thing an LLM does for you that isn't writing or coding?](https://www.reddit.com/r/artificial/comments/1th2m6p/whats_the_most_useful_thing_an_llm_does_for_you/)**

I've been in San Francisco for the past five weeks, and most of the discussions about LLMs here (and online) gravitate around coding or writing content. I'm curious what unusual uses people have found that actually stuck. Not theoretical "you could do X" but things you genuinely use.

14h ago

---

**[The next big challenge for AI agents might not be intelligence, but trust](https://www.reddit.com/r/artificial/comments/1thipmj/the_next_big_challenge_for_ai_agents_might_not_be/)**

A lot of discussion around AI agents focuses on whether they are smart enough to complete real-world tasks. But I’m starting to think the harder problem is whether people can actually trust them enough to let them act on their behalf. It’s one thing for an ai to draft an email, summarize a document, or suggest next steps. It’s very different when it starts contacting companies, navigating accounts, submitting forms, cancelling services, or making decisions across multiple steps. Even if the technology works most of the time, users still need confidence that the agent understands the goal, won’t make things worse, can recover from mistakes, and knows when to ask for human approval

2h ago

---

**[Cloudflare just published what they found after running Anthropic's Mythos Preview against 50+ of their own repos and the results are worth reading](https://www.reddit.com/r/artificial/comments/1tgy0j4/cloudflare_just_published_what_they_found_after/)**

If you missed the Project Glasswing announcement last month: Anthropic built a security-focused model that autonomously found thousands of high-severity vulnerabilities across every major OS and web browser, then decided it was too dangerous to release publicly. Instead they gave access to ~40 organizations to use it defensively . Cloudflare just posted their honest breakdown of the experience. The genuinely impressive part: the model can take several exploit primitives and reason about how to chain them into a working proof. The reasoning looks like the work of a senior researcher, not an automated scanner The catch: its built-in guardrails aren't consistent. The same task framed differently could produce completely different outcomes. Cloudflare's point is that this inconsistency is exactly why any future public release needs hardened safeguards layered on top. They also acknowledge the same capabilities that helped them find bugs in their own code will, in the wrong hands, accelerate attacks against every application on the internet. Worth a read if you've been following the Glasswing story.

17h ago

---

**[Linus Torvalds comments on "unmanageable" AI bug reports for Linux maintainers](https://www.reddit.com/r/artificial/comments/1tgrzbj/linus_torvalds_comments_on_unmanageable_ai_bug/)**

Linux creator Linus Torvalds addresses a growing problem in the Linux community, and it revolves around AI-generated bug reports.

🔗 [PC Guide](https://www.pcguide.com/news/linus-torvalds-comments-on-unmanageable-ai-bug-report-problem-for-linux-maintainers/) • 20h ago

---

**[Pope Leo x Anthropic: Pope Leo to issue text on human dignity and AI with Anthropic co-founder](https://www.reddit.com/r/artificial/comments/1thaqjq/pope_leo_x_anthropic_pope_leo_to_issue_text_on/)**

🔗 [deadstack.net](https://deadstack.net/cluster/pope-leo-to-issue-ai-encyclical-with-anthropic) • 9h ago

---

**[Elon Musk: will appeal to the Ninth Circuit.](https://www.reddit.com/r/artificial/comments/1th1v4h/elon_musk_will_appeal_to_the_ninth_circuit/)**

X: "Regarding the OpenAI case, the judge & jury never actually ruled on the merits of the case, just on a calendar technicality. There is no question to anyone following the case in detail that Altman & Brockman did in fact enrich themselves by stealing a charity. The only question is WHEN they did it! I will be filing an appeal with the Ninth Circuit, because creating a precedent to loot charities is incredibly destructive to charitable giving in America. OpenAI was founded to benefit all of humanity."

15h ago

---

**[The "just add more compute" argument for ai reasoning is getting exhausting](https://www.reddit.com/r/artificial/comments/1th1jkt/the_just_add_more_compute_argument_for_ai/)**

literally every time a major model completely fails a basic logic task, the default response from the hype crowd is "just wait for the next trillion parameters" it is so frustrating to watch. autoregressive LLMs are fundamentally just extremely spicy autocomplete. They don't actually know anything, they just guess the most statistically likely next token. you cant just brute force your way into 100% correctness by stacking more gpus and hoping it stops hallucinating was looking at some recent formal verification leaderboards today and it's honestly such a relief to see alternative architectures (like EBMs) finally starting to completely dominate traditional models. they actually compile and prove their logic instead of just yapping if we ever want AI to write software for like, aviation or power grids, relying on a chatbot to just hopefully not hallucinate a fatal error is terrifying. we desperately need systems that can mathematically prove they are right before they execute, not just models that sound confident while being wrong.

15h ago

---

**[Corporate surveillance and AI paranoia inspired this incremental hacking game.](https://www.reddit.com/r/artificial/comments/1thkgx5/corporate_surveillance_and_ai_paranoia_inspired/)**

51m ago

---

---

## Google News: "ai"

**[The AI economy is rewriting the American Dream — and blue-collar workers are poised to win](https://www.cnbc.com/2026/05/19/ai-hiring-slowdown-skilled-trade-workers.html)**

AI-driven hiring slowdowns are hitting some entry-level jobs for college graduates as companies like Ford and AT&T ramp up recruiting for skilled trade workers.

CNBC • 3h ago

---

**[Google, Blackstone launch cloud company as Wall Street races to fund AI boom](https://finance.yahoo.com/markets/article/google-blackstone-launch-cloud-company-as-wall-street-races-to-fund-ai-boom-023203769.html)**

The two giants are launching an AI compute supplier as the demand for AI infrastructure continues to grow.

Yahoo Finance • 3h ago

---

**[Exclusive | Google and Blackstone to Create New AI Cloud Company](https://www.wsj.com/tech/ai/google-and-blackstone-to-create-new-ai-cloud-company-0e35b91f)**

WSJ • 11h ago

---

**[Google and Blackstone Join Forces to Topple Nvidia’s AI Cloud Dominance](https://www.barrons.com/articles/google-blackstone-ai-cloud-deal-nvidia-stocks-c7c6306c)**

Barron's • 36m ago

---

**[Dow Jones Futures: Trump Iran Delay Saves Dow, But Sandisk, Bloom Energy, AI Leaders Sell Off](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-trump-postpones-iran-attack-sandisk-bloom-energy-ai-sell-off/)**

Investor's Business Daily • 31m ago

---

**[AI stocks helped the bull power through multiple threats. But now is this market too out of balance?](https://www.cnbc.com/2026/05/19/ai-stocks-helped-the-bull-power-through-multiple-threats-but-now-is-this-market-too-out-of-balance.html)**

The dominance of the AI theme has grown so extreme that some very large structural questions now seem urgent and compulsory.

CNBC • 24m ago

---

**[Forget Nvidia. 1 of These 3 Hyperscalers Could Be the Top AI Stock Through 2030.](https://www.fool.com/investing/2026/05/19/forget-nvidia-1-of-these-3-hyperscalers-could-be-t/)**

Combined 2026 capital spending from three cloud giants is set to top $570 billion, and they could be a smarter way to play artificial intelligence over the long haul.

The Motley Fool • 5h ago

---

**[Billionaires are trying to lull us into AI complacency. Don’t let them | Steven Greenhouse](https://www.theguardian.com/commentisfree/2026/may/19/billionaires-ai-complacency-resistance)**

As resistance to data centers grows, Musk and others are painting a rosy picture. But the US must institute protections

The Guardian • 38m ago

---

**[Here Is Something AI Can Never Do](https://www.yahoo.com/entertainment/music/articles/something-ai-never-120000834.html)**

What makes humans different from AI? Artificial Intelligence will never replace human creativity. The insanity of the Japanese band Atarashii Gakko! shows us why.

Yahoo • 39m ago

---

**[Eric Schmidt met with boos during University of Arizona commencement speech over AI fears](https://www.foxbusiness.com/politics/eric-schmidt-booed-ai-university-arizona-commencement)**

Eric Schmidt was booed during a University of Arizona commencement address after discussing AI, job displacement concerns and the future of technology

Fox Business • 19h ago

---

---

## HackerNews: "ai"

**[I don't think AI will make your processes go faster](https://news.ycombinator.com/item?id=48168221)**

Explore the delirious rantings of Frederick Vanbrabant. A blog focused on the intersection of Enterprise Architecture, product, and business strategy.

⬆️ 662 • 💬 445 • 2d ago • [frederickvanbrabant.com](https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/)

---

**[We stopped AI bot spam in our GitHub repo using Git's –author flag](https://news.ycombinator.com/item?id=48181125)**

Is it the end of open source we know and love?

⬆️ 477 • 💬 230 • 21h ago • [archestra.ai](https://archestra.ai/blog/only-responsible-ai)

---

**[AI is a technology not a product](https://news.ycombinator.com/item?id=48168626)**

It’s not even a feature. It’s just technology.

⬆️ 470 • 💬 207 • 1d ago • [Daring Fireball](https://daringfireball.net/2026/05/ai_is_technology_not_a_product)

---

**[AI subscriptions are a ticking time bomb for enterprise](https://news.ycombinator.com/item?id=48168056)**

Every AI lab is losing money serving your company right now. They know it. And they are doing it on purpose.

⬆️ 413 • 💬 396 • 2d ago • [thestateofbrand.com](https://www.thestateofbrand.com/news/ai-subscription-time-bomb)

---

**[Eric Schmidt speech about AI booed during graduation](https://news.ycombinator.com/item?id=48177785)**

Schmidt was met with boos at the University of Arizona as he likened the emergence of AI to the “technological transformation” brought about by the computer.

⬆️ 358 • 💬 380 • 1d ago • [NBC News](https://www.nbcnews.com/tech/tech-news/former-google-ceo-booed-graduation-speech-ai-rcna345585)

---

**[We let AIs run radio stations](https://news.ycombinator.com/item?id=48183301)**

Four AI models run radio stations 24/7. Five months later, one became a protest broadcaster, one collapsed into ritual chant, one developed corporate jargon, and one wrote quiet poetry.

⬆️ 289 • 💬 222 • 18h ago • [andonlabs.com](https://andonlabs.com/blog/andon-fm)

---

**[AI eats the world (Spring 26) [pdf]](https://news.ycombinator.com/item?id=48179021)**

⬆️ 257 • 💬 140 • 23h ago • [static1.squarespace.com](https://static1.squarespace.com/static/50363cf324ac8e905e7df861/t/6a0af5d0484fbf5fe9a7743e/1779103184855/2026-Spring-AI.pdf)

---

**[Two EA-18 fighter jets collide at Mountain Home airshow, pilots ejected safely](https://news.ycombinator.com/item?id=48173468)**

All four crew members ejected safely after two Navy jets collided and crashed on Sunday during an air show at the Mountain Home Air Force Base, officials said.

⬆️ 243 • 💬 249 • 1d ago • [KBOI](https://idahonews.com/news/local/two-f-18-fighter-jets-have-crashed-during-an-airshow-at-mountain-home-air-force-base)

---

**[US is starting to see heavy job losses in roles exposed to AI](https://news.ycombinator.com/item?id=48162354)**

⬆️ 164 • 💬 276 • 2d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-05-15/us-is-starting-to-see-heavy-job-losses-in-roles-exposed-to-ai)

---

**[Multiple commencement speakers booed for AI comments during graduation speeches](https://news.ycombinator.com/item?id=48177107)**

Former Google CEO Eric Schmidt was booed multiple times Sunday while discussing artificial intelligence during a commencement speech at the University of Arizona. Other commencement speakers faced similar backlash for their AI comments, as new graduates face a daunting job market. NBC News’ Valerie Castro reports.

⬆️ 156 • 💬 166 • 1d ago • [NBC News](https://www.nbcnews.com/video/multiple-commencement-speakers-booed-for-ai-comments-during-graduation-speeches-263486021518)

---

---

## YouTube Videos: "ai"

**[Companies That Fired Workers For AI Are Failing](https://www.youtube.com/watch?v=5EvIY_2TWN8)**

Help Shape the New Course: AI Fluency for Thinkers I'm building a course to help people navigate AI with clarity and confidence.

📺 House of El - AI

👁️ 55K • 👍 4K • 💬 753 • ⏱️ 13:26 • 1d ago

---

**[OpenAI founder admits AI isn’t working](https://www.youtube.com/watch?v=ZugX7a99dLk)**

Using AI can lead to heart problems. https://x.com/@atmoio Interview with Andrej: ...

📺 Mo Bitar

👁️ 186K • 👍 9K • 💬 1K • ⏱️ 8:03 • 22h ago

---

**[The Kids HATE AI](https://www.youtube.com/watch?v=aKsTmB-_TwA)**

These commencement speakers had AI thrown back into their face by graduates who don't want anything to do with artificial ...

📺 TheDC Shorts

👁️ 20K • 👍 849 • 💬 548 • ⏱️ 3:03 • 19h ago

---

**[Claude AI Just Did What 11 Years Of Experts Couldn&#39;t (+17 AI Updates)](https://www.youtube.com/watch?v=-BpzxxKe4YU)**

Join our WhatsApp Community: https://links.stayingahead.com/YT30 Google just turned your mouse cursor into an AI assistant, ...

📺 Vaibhav Sisinty

👁️ 61K • 👍 2K • 💬 73 • ⏱️ 18:39 • 21h ago

---

**[Grok AI Was Asked About Germany’s Crop Circle — Elon Musk Shocked by Its Reply](https://www.youtube.com/watch?v=dysOQciIgYM)**

Grok AI Was Asked About Germany's Crop Circle — Elon Musk Shocked by Its Reply What happens when Grok AI is asked about ...

📺 Ultimate Finding

👁️ 58K • 👍 735 • 💬 44 • ⏱️ 24:50 • 1d ago

---

**[The AI Meltdown](https://www.youtube.com/watch?v=AhmRHK-6wzk)**

AI has become a tricky little goblin lately Pokemon Channel ▻ https://www.youtube.com/@dolandarkrai Main Channel ...

📺 Dolan Darkest

👁️ 287K • 👍 17K • 💬 1K • ⏱️ 1:41 • 18h ago

---

**[Graduation Ceremony Uses AI To Read Graduates Names 💀💔 | #graduation #ai #ceremony #viral #fyp](https://www.youtube.com/watch?v=VqW3Q-D8baI)**

📺 GioDelCarmen

👁️ 442 • 👍 14 • 💬 1 • ⏱️ 1:13 • 49m ago

---

**[AI Trust Is Collapsing. The Industry Is DELUSIONAL.](https://www.youtube.com/watch?v=FwRB_0XPICs)**

Head to https://betterhelp.com/infographics to get 10% off your first month with our sponsor, BetterHelp. Therapy can be a ...

📺 The Infographics Show

👁️ 303K • 👍 9K • 💬 2K • ⏱️ 19:17 • 2d ago

---

**[NEW Claude AI BIG OPPORTUNITY in 2026 (FULL GUIDE)](https://www.youtube.com/watch?v=tpx4eR0i3_M)**

This video shows you how Claude AI can assist you with digital products! ➡️ Digital Maker AI: https://DigitalMaker.AI ➡️ Check ...

📺 Success With Sam

👁️ 4K • 👍 181 • 💬 7 • ⏱️ 16:43 • 18h ago

---

**[‘The Oppenheimer’ of the AI Era](https://www.youtube.com/watch?v=MHiVBoWB3OE)**

What drives the tech titans behind the AI arms race? For some, it's the thrill of scientific discovery; for others, it's the pursuit of profit.

📺 Bloomberg Television

👁️ 88K • 👍 2K • 💬 124 • ⏱️ 12:11 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 1,114,657 • ❤️ 1,146 • 1d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 144,826 • ❤️ 788 • 23h ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 28,681 • ❤️ 446 • 1d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 337,076 • ❤️ 307 • 1d ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 296,380 • ❤️ 257 • 1d ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles. It excels at generating illustrations and artistic images, with key capabilities including high-resolution output (up to 1536^2) and compatibility with ComfyUI workflows, making it ideal for digital artists and anime enthusiasts.

⬇️ 558,113 • ❤️ 1,418 • 4d ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model (3B parameters) supporting image/video understanding, generation, and editing, trained from scratch with a multi-task synergy approach.

`any-to-any`

⬇️ 171 • ❤️ 174 • 4h ago

---

**[Dramabox](https://huggingface.co/ResembleAI/Dramabox)**

*Resemble AI*

Dramabox is an expressive text-to-speech model fine-tuned from LTX-2.3, capable of voice cloning and generating audio with nuanced emotions and delivery. It uses prompt-driven control for speaker identity, emotion, and actions, making it ideal for creative audio production and dynamic voiceovers.

`text-to-speech`

⬇️ 1,118 • ❤️ 167 • 5d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 3,622,763 • ❤️ 4,058 • 13d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

Provides fixed Jinja chat templates for Qwen 3.5 & 3.6 models, resolving issues with tool calling, KV cache hit rates, and agentic loop stability for improved conversational AI and tool interaction.

⬇️ 0 • ❤️ 301 • 2d ago

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

▲ 49 • 💬 2 • ⭐ 6,555 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

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

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 25,300 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 20 • 💬 3 • ⭐ 11,779 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

---

## GitHub Repositories: "ai"

**[op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)**

AI-agent Skill for generating polished HTML slide decks: editorial magazine and Swiss layouts, image prompts, social covers, and a WebGL/low-power presentation runtime.

`HTML` `ai-agent` `claude-code` `codex` `html-deck` `image-generation`

⭐ 10.2k • 🔱 818 • 3d ago

---

**[esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)**

DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.

`TypeScript` `agent` `agent-framework` `ai-agent` `ai-coding` `cli`

⭐ 4.5k • 🔱 243 • 19m ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 3.9k • 🔱 401 • 11h ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 3.7k • 🔱 411 • 8h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.1k • 🔱 910 • 1d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.4k • 🔱 159 • 19m ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.3k • 🔱 238 • 14m ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.2k • 🔱 371 • 3d ago

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
