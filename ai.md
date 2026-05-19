---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-19T05:44:50.462984+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 19, 2026 at 05:44 UTC  
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

🔗 [AP News](https://apnews.com/article/musk-openai-trial-verdict-0b9b0bfaffe96f2c930341f52dfe4f8c) • 11h ago

---

**[What's the most useful thing an LLM does for you that isn't writing or coding?](https://www.reddit.com/r/artificial/comments/1th2m6p/whats_the_most_useful_thing_an_llm_does_for_you/)**

I've been in San Francisco for the past five weeks, and most of the discussions about LLMs here (and online) gravitate around coding or writing content. I'm curious what unusual uses people have found that actually stuck. Not theoretical "you could do X" but things you genuinely use.

7h ago

---

**[Cloudflare just published what they found after running Anthropic's Mythos Preview against 50+ of their own repos and the results are worth reading](https://www.reddit.com/r/artificial/comments/1tgy0j4/cloudflare_just_published_what_they_found_after/)**

If you missed the Project Glasswing announcement last month: Anthropic built a security-focused model that autonomously found thousands of high-severity vulnerabilities across every major OS and web browser, then decided it was too dangerous to release publicly. Instead they gave access to ~40 organizations to use it defensively . Cloudflare just posted their honest breakdown of the experience. The genuinely impressive part: the model can take several exploit primitives and reason about how to chain them into a working proof. The reasoning looks like the work of a senior researcher, not an automated scanner The catch: its built-in guardrails aren't consistent. The same task framed differently could produce completely different outcomes. Cloudflare's point is that this inconsistency is exactly why any future public release needs hardened safeguards layered on top. They also acknowledge the same capabilities that helped them find bugs in their own code will, in the wrong hands, accelerate attacks against every application on the internet. Worth a read if you've been following the Glasswing story.

10h ago

---

**[Linus Torvalds comments on "unmanageable" AI bug reports for Linux maintainers](https://www.reddit.com/r/artificial/comments/1tgrzbj/linus_torvalds_comments_on_unmanageable_ai_bug/)**

Linux creator Linus Torvalds addresses a growing problem in the Linux community, and it revolves around AI-generated bug reports.

🔗 [PC Guide](https://www.pcguide.com/news/linus-torvalds-comments-on-unmanageable-ai-bug-report-problem-for-linux-maintainers/) • 13h ago

---

**[Elon Musk: will appeal to the Ninth Circuit.](https://www.reddit.com/r/artificial/comments/1th1v4h/elon_musk_will_appeal_to_the_ninth_circuit/)**

X: "Regarding the OpenAI case, the judge & jury never actually ruled on the merits of the case, just on a calendar technicality. There is no question to anyone following the case in detail that Altman & Brockman did in fact enrich themselves by stealing a charity. The only question is WHEN they did it! I will be filing an appeal with the Ninth Circuit, because creating a precedent to loot charities is incredibly destructive to charitable giving in America. OpenAI was founded to benefit all of humanity."

8h ago

---

**[Pope Leo x Anthropic: Pope Leo to issue text on human dignity and AI with Anthropic co-founder](https://www.reddit.com/r/artificial/comments/1thaqjq/pope_leo_x_anthropic_pope_leo_to_issue_text_on/)**

🔗 [deadstack.net](https://deadstack.net/cluster/pope-leo-to-issue-ai-encyclical-with-anthropic) • 2h ago

---

**[The "just add more compute" argument for ai reasoning is getting exhausting](https://www.reddit.com/r/artificial/comments/1th1jkt/the_just_add_more_compute_argument_for_ai/)**

literally every time a major model completely fails a basic logic task, the default response from the hype crowd is "just wait for the next trillion parameters" it is so frustrating to watch. autoregressive LLMs are fundamentally just extremely spicy autocomplete. They don't actually know anything, they just guess the most statistically likely next token. you cant just brute force your way into 100% correctness by stacking more gpus and hoping it stops hallucinating was looking at some recent formal verification leaderboards today and it's honestly such a relief to see alternative architectures (like EBMs) finally starting to completely dominate traditional models. they actually compile and prove their logic instead of just yapping if we ever want AI to write software for like, aviation or power grids, relying on a chatbot to just hopefully not hallucinate a fatal error is terrifying. we desperately need systems that can mathematically prove they are right before they execute, not just models that sound confident while being wrong.

8h ago

---

**[The next generation of AI has a prerequisite: a healthy human ecosystem](https://www.reddit.com/r/artificial/comments/1th55jm/the_next_generation_of_ai_has_a_prerequisite_a/)**

AI systems are environmentally and socially embedded. They cannot thrive in a degraded human ecosystem. Therefore, the measurement and protection of human health (data integrity, environmental stability, and economic agency) is the primary engineering requirement for the next generation of AI. Slightly rephrased, AI systems are only as good as the human data, institutions, and economic conditions they’re trained on and deployed into. Curious what others think — is this already being treated as a first-class constraint, or is it still an afterthought?

6h ago

---

**[EU AI Act enforcement starts in 75 days - affects any team building AI agents for European clients](https://www.reddit.com/r/artificial/comments/1tgf0gm/eu_ai_act_enforcement_starts_in_75_days_affects/)**

If you're building AI agents or SaaS products used by European companies (or processing EU resident data), the EU AI Act applies to you regardless of where your company is based. Full enforcement for high-risk systems starts August 2, 2026. High-risk means: credit scoring, recruitment filtering, healthcare triage, education assessment, critical infrastructure. The practical requirements: Automatic decision logging (not optional) 6-month minimum log retention Technical documentation of your detection pipeline Human oversight architecture Accuracy and bias testing documentation Fines: up to 35M euros or 7% of global turnover. I broke down what the regulation requires, what auditors check, and realistic steps before the deadline. In link below Worth reading if your team is building anything AI-related for the European market.

22h ago

---

**[Today's Irony. We as small creators cannot use AI but big companies can ban us using same AI](https://www.reddit.com/r/artificial/comments/1tgx5p1/todays_irony_we_as_small_creators_cannot_use_ai/)**

Sharing my experiences from recent horrific fights among AI slop fighters and big companies. Lately I have been observing so much clout around AI slop. AI assisted articles. "Ban it" Threaten the creator who wrote it with AI in their own voice. Who has the power to use AI? Big companies can use the same automation and AI to ban small creators like me. Here's my Cry. As an individual am I falling behind? Why can a company use AI to ban and the creator cannot write it with AI assisted? Big companies can be any company who is overpowering and controlling who stays to speak.

10h ago

---

---

## Google News: "ai"

**[Exclusive | Google and Blackstone to Create New AI Cloud Company](https://www.wsj.com/tech/ai/google-and-blackstone-to-create-new-ai-cloud-company-0e35b91f)**

WSJ • 4h ago

---

**[Google, Blackstone launch cloud company as Wall Street races to fund AI boom](https://finance.yahoo.com/markets/article/google-blackstone-launch-cloud-company-as-wall-street-races-to-fund-ai-boom-023203769.html)**

The two giants are launching an AI compute supplier as the demand for AI infrastructure continues to grow.

Yahoo Finance • 3h ago

---

**[How tech analysts and investors reacted to Google and Blackstone teaming up on an AI company](https://www.businessinsider.com/smart-people-react-google-blackstone-collab-5-billion-ai-company-2026-5)**

"The small fry are getting squeezed out," wrote one equities portfolio manager.

Business Insider • 4m ago

---

**[Jury hands victory to Sam Altman and OpenAI in battle with Elon Musk](https://www.theguardian.com/technology/2026/may/18/sam-altman-trial-victory-elon-musk-openai)**

OpenAI CEO and president found not liable for breaking contracts made with Musk when founding the startup

The Guardian • 12h ago

---

**[Jury rules against Musk in landmark AI trial](https://www.axios.com/2026/05/18/musk-loses-ai-trial-openai-altman)**

Axios • 8h ago

---

**[OpenAI defeats Elon Musk's lawsuit, removes obstacle to IPO](https://www.reuters.com/legal/government/elon-musk-loses-lawsuit-against-openai-2026-05-18/)**

Reuters • 5h ago

---

**[Tech investors loved this earnings season — but the Iran war is piling pressure on the companies powering the AI boom](https://www.cnbc.com/2026/05/19/iran-war-ai-chip-supply-chain-costs.html)**

Stocks continue to rally amid the AI boom, but the chip sector is scrambling to shore up access to key materials as costs rise.

CNBC • 44m ago

---

**[Los Angeles mayor's race: AI videos supporting Spencer Pratt shake up political playbook](https://abc7.com/post/los-angeles-mayors-race-ai-videos-supporting-spencer-pratt-shake-political-playbook/19127203/)**

AI-generated videos depicting L.A. mayoral candidate Spencer Pratt as a superhero and his rival Karen Bass as a villain are gaining traction online.

ABC7 Los Angeles • 16m ago

---

**[NVIDIA CEO Jensen Huang at Dell Technologies World: ‘Demand Is Going Parabolic, Utterly Parabolic’](https://blogs.nvidia.com/blog/dell-technologies-agent-enterprise-ai/)**

NVIDIA CEO Jensen Huang joined Dell CEO Michael Dell on stage Monday to unveil the latest updates to the Dell AI Factory with NVIDIA — delivering a full-stack platform for autonomous agents, from deskside workstations to data center racks.

NVIDIA Blog • 7h ago

---

**[Opinion | The Generation That Grew Up With A.I. Hates It](https://www.nytimes.com/2026/05/18/opinion/ai-boo-commencement-speeches.html)**

The New York Times • 5h ago

---

---

## HackerNews: "ai"

**[I don't think AI will make your processes go faster](https://news.ycombinator.com/item?id=48168221)**

Explore the delirious rantings of Frederick Vanbrabant. A blog focused on the intersection of Enterprise Architecture, product, and business strategy.

⬆️ 657 • 💬 443 • 1d ago • [frederickvanbrabant.com](https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/)

---

**[AI is a technology not a product](https://news.ycombinator.com/item?id=48168626)**

It’s not even a feature. It’s just technology.

⬆️ 464 • 💬 206 • 1d ago • [Daring Fireball](https://daringfireball.net/2026/05/ai_is_technology_not_a_product)

---

**[We stopped AI bot spam in our GitHub repo using Git's –author flag](https://news.ycombinator.com/item?id=48181125)**

Is it the end of open source we know and love?

⬆️ 451 • 💬 203 • 14h ago • [archestra.ai](https://archestra.ai/blog/only-responsible-ai)

---

**[Frontier AI has broken the open CTF format](https://news.ycombinator.com/item?id=48157559)**

Why frontier AI has broken the open CTF format, hollowed out the scoreboard, and made competitive CTF performance a weaker signal than it used to be.

⬆️ 416 • 💬 451 • 2d ago • [kabir.au](https://kabir.au/blog/the-ctf-scene-is-dead)

---

**[AI subscriptions are a ticking time bomb for enterprise](https://news.ycombinator.com/item?id=48168056)**

Every AI lab is losing money serving your company right now. They know it. And they are doing it on purpose.

⬆️ 410 • 💬 396 • 1d ago • [thestateofbrand.com](https://www.thestateofbrand.com/news/ai-subscription-time-bomb)

---

**[Eric Schmidt speech about AI booed during graduation](https://news.ycombinator.com/item?id=48177785)**

Schmidt was met with boos at the University of Arizona as he likened the emergence of AI to the “technological transformation” brought about by the computer.

⬆️ 348 • 💬 375 • 18h ago • [NBC News](https://www.nbcnews.com/tech/tech-news/former-google-ceo-booed-graduation-speech-ai-rcna345585)

---

**[Two EA-18 fighter jets collide at Mountain Home airshow, pilots ejected safely](https://news.ycombinator.com/item?id=48173468)**

All four crew members ejected safely after two Navy jets collided and crashed on Sunday during an air show at the Mountain Home Air Force Base, officials said.

⬆️ 242 • 💬 249 • 1d ago • [KBOI](https://idahonews.com/news/local/two-f-18-fighter-jets-have-crashed-during-an-airshow-at-mountain-home-air-force-base)

---

**[We let AIs run radio stations](https://news.ycombinator.com/item?id=48183301)**

Four AI models run radio stations 24/7. Five months later, one became a protest broadcaster, one collapsed into ritual chant, one developed corporate jargon, and one wrote quiet poetry.

⬆️ 218 • 💬 179 • 11h ago • [andonlabs.com](https://andonlabs.com/blog/andon-fm)

---

**[AI eats the world (Spring 26) [pdf]](https://news.ycombinator.com/item?id=48179021)**

⬆️ 190 • 💬 109 • 16h ago • [static1.squarespace.com](https://static1.squarespace.com/static/50363cf324ac8e905e7df861/t/6a0af5d0484fbf5fe9a7743e/1779103184855/2026-Spring-AI.pdf)

---

**[US is starting to see heavy job losses in roles exposed to AI](https://news.ycombinator.com/item?id=48162354)**

⬆️ 164 • 💬 275 • 2d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-05-15/us-is-starting-to-see-heavy-job-losses-in-roles-exposed-to-ai)

---

---

## YouTube Videos: "ai"

**[Companies That Fired Workers For AI Are Failing](https://www.youtube.com/watch?v=5EvIY_2TWN8)**

Help Shape the New Course: AI Fluency for Thinkers I'm building a course to help people navigate AI with clarity and confidence.

📺 House of El - AI

👁️ 49K • 👍 4K • 💬 716 • ⏱️ 13:26 • 18h ago

---

**[OpenAI founder admits AI isn’t working](https://www.youtube.com/watch?v=ZugX7a99dLk)**

Using AI can lead to heart problems. https://x.com/@atmoio Interview with Andrej: ...

📺 Mo Bitar

👁️ 164K • 👍 9K • 💬 1K • ⏱️ 8:03 • 15h ago

---

**[The Kids HATE AI](https://www.youtube.com/watch?v=aKsTmB-_TwA)**

These commencement speakers had AI thrown back into their face by graduates who don't want anything to do with artificial ...

📺 TheDC Shorts

👁️ 19K • 👍 816 • 💬 506 • ⏱️ 3:03 • 12h ago

---

**[How to Make Long AI Videos with Consistent Characters (2026)](https://www.youtube.com/watch?v=dOmKYJoRboE)**

Create Long AI Videos with Consistent Characters on OpenArt ...

📺 Isa does AI

👁️ 10K • 💬 7 • ⏱️ 13:34 • 15h ago

---

**[Claude AI Just Did What 11 Years Of Experts Couldn&#39;t (+17 AI Updates)](https://www.youtube.com/watch?v=-BpzxxKe4YU)**

Join our WhatsApp Community: https://links.stayingahead.com/YT30 Google just turned your mouse cursor into an AI assistant, ...

📺 Vaibhav Sisinty

👁️ 44K • 👍 2K • 💬 58 • ⏱️ 18:39 • 14h ago

---

**[The Best AI Investor Just Shorted the Entire Market](https://www.youtube.com/watch?v=ci1OWrEUTvE)**

LIMITLESS HQ ⬇️ NEWSLETTER: https://limitlessft.substack.com/ FOLLOW ON X: https://x.com/LimitlessFT SPOTIFY: ...

📺 Limitless Podcast

👁️ 35K • 👍 1K • 💬 184 • ⏱️ 31:36 • 12h ago

---

**[Grok AI Was Asked About Germany’s Crop Circle — Elon Musk Shocked by Its Reply](https://www.youtube.com/watch?v=dysOQciIgYM)**

Grok AI Was Asked About Germany's Crop Circle — Elon Musk Shocked by Its Reply What happens when Grok AI is asked about ...

📺 Ultimate Finding

👁️ 54K • 👍 680 • 💬 38 • ⏱️ 24:50 • 1d ago

---

**[Man vs AI Robot: it’s officially over...](https://www.youtube.com/watch?v=j5MtBTPGJng)**

Man Vs Machine - we're entering the end times of AI deployment - do you want to live in a world of AI powered robots and LLM's ...

📺 Stylosa

👁️ 4K • 👍 160 • 💬 101 • ⏱️ 16:12 • 12h ago

---

**[Corporate AI Is A Delusion. $600 Billion Just VANISHED.](https://www.youtube.com/watch?v=WhRyYdW-mbk)**

The Trillion Dollar AI Lie is already reshaping the global economy. OpenAI, NVIDIA, Big Tech, and corporate CEOs are burning ...

📺 The Infographics Show

👁️ 245K • 👍 7K • 💬 1K • ⏱️ 19:36 • 1d ago

---

**[Ex-Google CEO Gets Booed While Discussing AI in Commencement Speech | WSJ News](https://www.youtube.com/watch?v=tNH43a1EI7s)**

Former Google Chief Executive Eric Schmidt shared his thoughts on technology and artificial intelligence during a ...

📺 WSJ News

👁️ 57K • 👍 1K • 💬 508 • ⏱️ 2:02 • 10h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 80,586 • ❤️ 780 • 16h ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 1,049,229 • ❤️ 1,131 • 1d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 24,031 • ❤️ 426 • 20h ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 268,305 • ❤️ 293 • 23h ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 237,613 • ❤️ 251 • 1d ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles. It excels at generating illustrations and artistic images, with key capabilities including high-resolution output (up to 1536^2) and compatibility with ComfyUI workflows, making it ideal for digital artists and anime enthusiasts.

⬇️ 545,205 • ❤️ 1,414 • 4d ago

---

**[Dramabox](https://huggingface.co/ResembleAI/Dramabox)**

*Resemble AI*

Dramabox is an expressive text-to-speech model fine-tuned from LTX-2.3, capable of voice cloning and generating audio with nuanced emotions and delivery. It uses prompt-driven control for speaker identity, emotion, and actions, making it ideal for creative audio production and dynamic voiceovers.

`text-to-speech`

⬇️ 1,001 • ❤️ 165 • 5d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 3,435,748 • ❤️ 4,045 • 13d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

Provides fixed Jinja chat templates for Qwen 3.5 & 3.6 models, resolving issues with tool calling, KV cache hit rates, and agentic loop stability for improved conversational AI and tool interaction.

⬇️ 0 • ❤️ 297 • 2d ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 15,024 • ❤️ 393 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 75 • 💬 3 • ⭐ 76,908 • 16mo ago

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

▲ 8 • 💬 0 • ⭐ 18,088 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 118 • 💬 10 • ⭐ 9,890 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[MMSkills: Towards Multimodal Skills for General Visual Agents](https://huggingface.co/papers/2605.13527)**

*Kangning Zhang, Shuai Shao, Qingyao Li et al. (11 authors)*

🏢 Shanghai Jiaotong University 1(NOT OFFICIAL)

Multimodal procedural knowledge frameworks enable visual agents to leverage external reusable skills through structured representations combining text, state cards, and visual keyframes, improving decision-making in complex environments.

▲ 105 • 💬 2 • ⭐ 103 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.13527) • [💻 code](https://github.com/DeepExperience/MMSkills) • [🔗 project](https://deepexperience.github.io/MMSkills/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 63,620 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Pixal3D: Pixel-Aligned 3D Generation from Images](https://huggingface.co/papers/2605.10922)**

*Dong-Yang Li, Wang Zhao, Yuxin Chen et al. (8 authors)*

🏢 ARC Lab, Tencent PCG

Pixal3D introduces a pixel-aligned 3D generation approach that addresses fidelity issues in 3D asset creation by establishing direct pixel-to-3D correspondences through back-projection conditioning.

▲ 30 • 💬 3 • ⭐ 1,010 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2605.10922) • [💻 code](https://github.com/TencentARC/Pixal3D) • [🔗 project](https://ldyang694.github.io/projects/pixal3d/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 25,300 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture](https://huggingface.co/papers/2605.12500)**

*Haiwen Diao, Penghao Wu, Hanming Deng et al. (58 authors)*

🏢 SenseNova

Unified vision-language models treat understanding and generation as integrated processes rather than separate tasks, demonstrating strong performance across multiple multimodal capabilities including image synthesis and action reasoning.

▲ 172 • 💬 1 • ⭐ 2,082 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.12500) • [💻 code](https://github.com/OpenSenseNova/SenseNova-U1)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 20 • 💬 3 • ⭐ 11,734 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

---

## GitHub Repositories: "ai"

**[op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)**

AI-agent Skill for generating polished HTML slide decks: editorial magazine and Swiss layouts, image prompts, social covers, and a WebGL/low-power presentation runtime.

`HTML` `ai-agent` `claude-code` `codex` `html-deck` `image-generation`

⭐ 9.9k • 🔱 803 • 3d ago

---

**[esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)**

DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.

`TypeScript` `agent` `agent-framework` `ai-agent` `ai-coding` `cli`

⭐ 4.4k • 🔱 236 • 3m ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 3.9k • 🔱 394 • 4h ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 3.4k • 🔱 380 • 1h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.1k • 🔱 905 • 1d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.4k • 🔱 157 • 1d ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.3k • 🔱 237 • 19h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.2k • 🔱 364 • 3d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.2k • 🔱 333 • 1d ago

---

**[GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist)**

Portable AI agent orchestration with mechanical protocol enforcement. 186 agents, zero runtime dependencies.

`Python` `agent-framework` `agent-system` `ai-agents` `claude-code` `cursor-ide`

⭐ 1.8k • 🔱 353 • 25d ago

---

---

*Generated by PeekDeck - A glance is all you need*
