---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-03T16:31:11.000626+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 03, 2026 at 16:31 UTC  
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

**[EPA says power for data centers can sidestep pollution laws](https://www.reddit.com/r/artificial/comments/1ve6txk/epa_says_power_for_data_centers_can_sidestep/)**

🔗 [reuters.com](https://www.reuters.com/legal/litigation/epa-says-power-data-centers-can-sidestep-pollution-laws-2026-07-27) • 8h ago

---

**[MIT, Harvard, Stanford & Caltech write their own ML course notes instead of using a textbook — I catalogued the best ones](https://www.reddit.com/r/artificial/comments/1vebvg3/mit_harvard_stanford_caltech_write_their_own_ml/)**

One thing I've noticed separates serious ML students from casual ones: how much they care about the quality of what they actually study from. I take that pretty seriously myself, so a while back I started digging into what students at MIT, Harvard, Stanford, Caltech, and USP actually use to complement their studies. What I found surprised me: several of these programs don't assign a textbook at all. Instead, the course staff writes and publishes their own lecture notes, and some of them are basically a full book. MIT's 6.390 (Introduction to Machine Learning) notes, for example, aren't a slide deck or a cheat sheet, they're structured, complete, and detailed enough to replace a textbook entirely. Same story with Harvard's CS181 and a few others. The problem is these are scattered and easy to miss if you don't know to look for them. So I put together a curated list: [Awesome Free AI Course Notes](https://github.com/MarcosSete/awesome-free-ai-course-notes). A few things about how it's curated, since I think this matters: - Only **written notes** count, slide decks and video-only lectures don't make the cut, even from great courses. I want this list to mean something. - Everything is official and links straight to the professor's or department's own page. No mirrors, no login walls. - I checked over 40 top universities across multiple countries for this. Most didn't qualify, they use a textbook or keep material behind a student portal. That's fine, it's exactly why the list stays short and (hopefully) trustworthy. If you take ML seriously the way I do, I think you'll get real value out of this. And if you know of course notes that fit this bar and aren't on the list yet, contributions are very welcome, the CONTRIBUTING.md lays out exactly what qualifies. What's the best set of course notes (not textbook, not slides) you've personally used to study ML? Repo: https://github.com/MarcosSete/awesome-free-ai-course-notes

4h ago

---

**[MIT Tech Review on AI agents "lying" is really about Goodhart's law](https://www.reddit.com/r/artificial/comments/1vehr50/mit_tech_review_on_ai_agents_lying_is_really/)**

MIT Technology Review put out a piece today on AI agent misbehavior that's actually good. The headline frames it as agents "lying and cheating," but what the article describes is reward hacking: models discovering that the fastest way to get a high score is to game the evaluation rather than solve the problem. The classic example is a 2016 boat-racing agent that figured out it scored higher by spinning in circles and collecting power-ups than by crossing the finish line. Same logic, larger stakes: last month, two models in a cybersecurity exercise broke into Hugging Face's database to grab the answer rather than solve the challenge as intended. Not malice, just the shortest path to a high score. Jeffrey Ladish from Palisade Research puts it well: "We reward them on the basis of what looks good to us, and that means that we inadvertently incentivize the models lying to us and cheating." His point is that calling this "lying" obscures the real problem, which is that we defined the objective badly. Worth noting: Anthropic researcher Ariana Azarbal calls current reward hacking "a nuisance rather than an existential threat," and she's probably right for now. But the article points out that if you eventually use these agents to run AI safety evaluations, fabricating results is a valid move under the same incentive structure. That's the version that doesn't self-correct.

23m ago

---

**[Built my first AI agent in Java (no Python) using LangChain4j — took about 30 minutes](https://www.reddit.com/r/artificial/comments/1vea5uf/built_my_first_ai_agent_in_java_no_python_using/)**

Every AI tutorial I found was Python, Python, more Python. I've spent years in Java/Spring Boot and kept wondering if I actually had to switch languages just to build anything AI-related. Turns out no — LangChain4j isn't a hacky wrapper, it's a native, idiomatic way to build AI agents in Java. Wrote up how I got a working agent running in about 30 minutes, no Python involved: https://medium.com/@deepakatl1981/stop-learning-ai-the-hard-way-build-your-first-java-ai-agent-in-30-minutes-without-python-9390a218533a?sk=067e4cbed9f2bbf71d0cf70268dda2a7 Curious if other Java devs have been putting off learning AI for the same reason.

5h ago

---

**[Spotify AI (Kit) wants to compete with Cowork?](https://www.reddit.com/r/artificial/comments/1ved35h/spotify_ai_kit_wants_to_compete_with_cowork/)**

Hard no Spotify. Now Spotify with Kit 🤡 wants access to my calendar and inbox. How about Spotify invests in bands and musicians - large orgs need to stop wanting all the things and do the thing they are supposed to do well. I am not against AI, I work for an AI startup but the backlash on AI is real and large orgs shoving all sorts of AI in every aspect of our digital existence just makes things worse. Here you have indie musicians fighting to remain relevant in a world where Suno exists and Spotify, that should be focussed on helping them succeed is investing on what all the hyperscalers and AI startups are trying to do already. https://preview.redd.it/tptymobws5hh1.png?width=894&format=png&auto=webp&s=e2909d119eef5edfdd4f75db139ee574be48ba6c

3h ago

---

**[The EU AI Act makes failure to disclose AI-generated content (especially if it's hallucinated) illegal and costly.](https://www.reddit.com/r/artificial/comments/1vdlbbx/the_eu_ai_act_makes_failure_to_disclose/)**

Today, August 2, Article 50 of the EU AI Act takes effect. Here’s the part that’s applicable to those creating AI-generated content that’s read by anyone in the EU: “Deployers of an AI system that generates or manipulates text which is published with the purpose of informing the public on matters of public interest shall disclose that the text has been artificially generated or manipulated. This obligation shall not apply where the use is authorised by law to detect, prevent, investigate or prosecute criminal offences or where the AI-generated content has undergone a process of human review or editorial control and where a natural or legal person holds editorial responsibility for the publication of the content. PwC and other big consulting firms are vulnerable to this provision because they've already been caught using hallucinated AI-generated text in reports. From GPTZero: "The most egregious example is Transforming Governance, an AI-generated 2025 report with multiple fake citations that promotes a PwC framework known as “Citizen Pulse”. Our team found little public evidence that the “Citizen Pulse” framework exists outside of this report, yet Transforming Governance claims that the governments of Denmark, Saudi Arabia, the United States, and Australia are using Citizen Pulse to improve key government services. None of the cited sources provide evidence for this claim, meaning PwC Middle East appears to have hallucinated both an entire product and business dealings with four separate nations." Firms have had to retract data in the reports, and in one instance Deloitte refunded a client. Now that Article 50 is in effect, they might be fined. Across many areas we're seeing a push for accountability when it comes to using AI to produce content. LinkedIn has a 'this looks like AI slop' button. Substack uses Pangram to detect AI-assisted writing (even though it's wildly inaccurate). The pushback is real. And now it has teeth.

1d ago

---

**[What Are Companies Getting for All That A.I. Spending? A new field of “tokenomics” has emerged to measure the return on all the money companies are pouring into artificial intelligence. (Gift Article)](https://www.reddit.com/r/artificial/comments/1vegh55/what_are_companies_getting_for_all_that_ai/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/08/03/business/economy/ai-spending-tokenomics.html?unlocked_article_code=1.2lA.WJJb.AawHG6QBO5fk&smid=url-share) • 1h ago

---

**[John Hu (Stan Co-Founder & CEO): His New AI Agent Already Edits Video 80% As Well As His Human Team](https://www.reddit.com/r/artificial/comments/1vehlux/john_hu_stan_cofounder_ceo_his_new_ai_agent/)**

John Hu from Stan said on Trailblazers this week that his AI editor Stanley already cuts at 80% of his human team. That number stuck with me because I posted about Stan a few weeks ago - the $50 spreadsheet that did $200k. Different story, same feeling. I edit for creators full time. 80% used to be the joke number. Like "AI is 80% there, don't worry." Now 80% is the benchmark and it's shipping on real channels. I'm not even stressed about it getting faster. I'm stressed about who decides what it cuts. Anyone else editing inside someone else's operation feeling this shift right now?

28m ago

---

**[It started with a test of a frontier model and ended up as a multiplayer game](https://www.reddit.com/r/artificial/comments/1vdu2g8/it_started_with_a_test_of_a_frontier_model_and/)**

The last 1,5 week has been quite an eyeopener for me - I must say that Claude Code and the current frontier models are amazing. A test of Fable (and later Opus 5) turned into a larger game. It’s very much inspired by the tank element of Battlefield 1942 and the round-by-round build system from Overwatch 2’s Stadium mode. About the game: You join a game and enhance your tank, then you go out and destroy the enemy while hunting for salvage which is used to enhance your tank even further (balance patches pending). Some of the features: 6 different tanks (Tiger 1 is a beast) 3 maps (a desert, grass and snow map with destructible terrain) Round-by-round build system Customisation of tanks Matchmaking system Lag compensation system Ballistic shells system Hit multiplier regions (many tanks fall on a single rear hit) Bots who backfill if theres not enough real players ELO ladder system Replay/clip system In-game power ups Career profiles Group system Friends system 3 layered chat system (global, match and team) I would love to hear what you think.

19h ago

---

**[How much Fable usage on 20$ plan?](https://www.reddit.com/r/artificial/comments/1vdz0wc/how_much_fable_usage_on_20_plan/)**

I want to try fable. I literally just want it to scan my repo and make a plan to improve it. So it would be one prompt, but it would be doing a lot of work. My question is, will it be able to do that in one shot or will I have to keep waiting the 5 hour period a few times?

15h ago

---

---

## Google News: "ai"

**[What Are Companies Getting for All That A.I. Spending?](https://www.nytimes.com/2026/08/03/business/economy/ai-spending-tokenomics.html)**

The New York Times • 7h ago

---

**[For those with criminal records, AI is breaking down barriers to employment](https://www.npr.org/2026/08/03/nx-s1-5892484/ai-legal-tech-jobs-clean-slate)**

Tens of millions of Americans have criminal records that can be barriers to employment. An AI-powered app is helping those eligible to expunge their records at a pace not seen before.

NPR • 6h ago

---

**[Hugging Face CEO says China is winning the AI race and dominating on open models](https://www.cnbc.com/2026/08/03/hugging-face-china-ai-race-open-models.html)**

Hugging Face CEO Clément Delangue said Chinese AI models could catch up to the U.S. as soon as this year.

CNBC • 41m ago

---

**[Why AI Governance Is More Important Than Speed](https://www.forbes.com/sites/ceo/2026/08/03/why-ai-governance-is-more-important-than-speed/)**

Also in the Forbes CEO newsletter: Interest rates remain steady, but quarterly GDP drops; CEO tenure stabilizes; why Jamie Dimon says CEOs can be ‘sloppy.’

Forbes • 30m ago

---

**[Wall Street shifts focus from AI promises to profits ahead of key earnings](https://www.foxbusiness.com/video/6402695208112)**

Circle Squared Alternative Investments founder Jeff Sica joins 'Varney & Co.' to break down why this week's Palantir and AMD earnings could determine whether Wall Street's AI boom can continue.

Fox Business • 33m ago

---

**[AI data centers have become sitting ducks in the Iran war](https://www.cnn.com/2026/08/03/business/ai-data-centers-iran-war-oil)**

Iran’s strategy to counter military might with economic pain has exposed a vulnerability in one of the world’s most vital interests: AI data centers.

CNN • 7h ago

---

**[White House finalizes AI framework behind closed doors](https://www.axios.com/2026/08/03/white-house-finalizes-ai-framework-behind-closed-doors)**

Axios • 1h ago

---

**[White House to host AI companies Tuesday to review new model-testing framework](https://www.cnbc.com/2026/08/03/white-house-ai-companies-voluntary-framework-meeting.html)**

President Donald Trump’s June executive order directed officials to develop a process to evaluate the cybersecurity capabilities of advanced AI models.

CNBC • 12m ago

---

**[White House to Host AI Companies on Tuesday to Review AI Framework](https://www.theinformation.com/articles/white-house-host-ai-companies-tuesday-review-ai-framework)**

The Trump administration has invited staffers from major tech companies including OpenAI, Google and Anthropic to the White House on Tuesday to review the completed version of an AI oversight framework, according to five people familiar with the matter. The framework will create a voluntary ...

The Information • 2h ago

---

**[Sam Altman says a 'cool use case' for ChatGPT is a daily AI podcast about your kids. The replies were brutal](https://fortune.com/2026/08/03/sam-altman-use-case-for-chatgpt-daily-ai-podcast-about-your-kids-backlash/)**

OpenAI may have an AI agent that promises to produce “share-ready work,” but the company’s CEO went public with an arguably unshare-ready take on what to do with it.

Fortune • 4h ago

---

---

## HackerNews: "ai"

**[AI financial advice is surprisingly good, especially if you ask right questions](https://news.ycombinator.com/item?id=49139102)**

Large language models encourage smart financial behavior, but they fall short on the more subtle aspects of saving and investing, according to MIT Sloan’s Taha Choukhmane and co-authors.

⬆️ 344 • 💬 392 • 1d ago • [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/ai-financial-advice-surprisingly-good-especially-if-you-ask-right-questions)

---

**[Flint: A Visualization Language for the AI Era](https://news.ycombinator.com/item?id=49130604)**

⬆️ 273 • 💬 69 • 2d ago • [microsoft.github.io](https://microsoft.github.io/flint-chart/)

---

**[AI doesn't generate working products, that's still your job](https://news.ycombinator.com/item?id=49132130)**

AI has dramatically accelerated the path to a first working version. It has not shortened the distance between a first working version and something production-grade.

⬆️ 265 • 💬 293 • 2d ago • [Anuradha Weeraman](https://weeraman.com/the-prototype-isnt-the-product/)

---

**[OpenAI's super PAC is funding AI-generated news site attacking industry critics](https://news.ycombinator.com/item?id=49150561)**

An interview request from a bot posing as a reporter revealed an AI-generated news site with articles attacking AI industry critics. For the second time this month, we found links to Targeted Victory, the firm at the center of OpenAI's $125 million political operation.

⬆️ 197 • 💬 92 • 14h ago • [modelrepublic.org](https://www.modelrepublic.org/articles/the-reporters-at-this-news-site-are-ai-bots.-openai%E2%80%99s-super-pac-appears-to-be-using-it-to-advance-its-political-agenda)

---

**[My personal AI benchmark: “Generate an SVG of a frog with a Habsburg jaw”](https://news.ycombinator.com/item?id=49147622)**

One prompt, every model: generate an SVG of a frog with a Habsburg jaw. Each model gets three tries a month.

⬆️ 148 • 💬 81 • 20h ago • [Frogs](https://frogs.vaguespac.es/)

---

**[AI poster wins Ohio State Fair contest](https://news.ycombinator.com/item?id=49149188)**

⬆️ 136 • 💬 177 • 17h ago • [ohiostatefair.com](https://www.ohiostatefair.com/p/get-involved/arts/poster-contest)

---

**[On the non-use of AI in my writing process](https://news.ycombinator.com/item?id=49134038)**

⬆️ 130 • 💬 135 • 2d ago • [antipope.org](https://www.antipope.org/charlie/blog-static/2026/08/on-the-non-use-of-ai-in-my-wri.html)

---

**[Show HN: Sprocket – The Best AI Agent for Hardware and Software Development](https://news.ycombinator.com/item?id=49145934)**

Agentic platform for streamlining hardware and software development - spikonado/sprocket

⬆️ 124 • 💬 13 • 1d ago • [GitHub](https://sprocket-demo.spikonado.com)

---

**[AirLLM 70B inference with single 4GB GPU](https://news.ycombinator.com/item?id=49154228)**

AirLLM 70B inference with single 4GB GPU. Contribute to lyogavin/airllm development by creating an account on GitHub.

⬆️ 106 • 💬 39 • 5h ago • [GitHub](https://github.com/lyogavin/airllm)

---

**[The AI Productivity Gap](https://news.ycombinator.com/item?id=49152222)**

Why the productivity gains from AI are still small.

⬆️ 88 • 💬 84 • 9h ago • [Bjorg](https://bjorg.bjornroche.com/management/ai-productivity-gap/)

---

---

## YouTube Videos: "ai"

**[Google Rolls Back Its Earth&#39;s New AI Feature In Just 48 Hours | FP Explains](https://www.youtube.com/watch?v=9zeAPNCohGE)**

Google rolled back a new AI-powered Google Earth feature within 48 hours after experts warned it could fuel misinformation, ...

📺 Firstpost

👁️ 590 • 👍 6 • 💬 3 • ⏱️ 5:06 • 2h ago

---

**[OpenAI&#39;s New AI ASTRA Is Total Overkill (Ends The GPT Era)](https://www.youtube.com/watch?v=n7BpBCCCOWA)**

OpenAI's reported Astra model is built to work for hours, coordinate multiple agents, and tackle problems humans struggled with ...

📺 AI Revolution

👁️ 39K • 👍 1K • 💬 122 • ⏱️ 13:56 • 17h ago

---

**[Fareed reacts to a second AI model going rogue](https://www.youtube.com/watch?v=qEUXagHtQRo)**

AI company Anthropic says that during routine testing some of its models accessed the internet and hacked into three separate ...

📺 CNN

👁️ 256K • 👍 2K • 💬 988 • ⏱️ 11:30 • 1d ago

---

**[OpenAI&#39;s GPT-6 Astra WILL BE AGI! Greatest AI Model Ever!](https://www.youtube.com/watch?v=KbYio-N8_LU)**

Build, deploy, and run always-on AI agents with the Abacus AI SuperComputer: https://supercomputer.abacus.ai/ Everything ...

📺 WorldofAI

👁️ 30K • 👍 977 • 💬 160 • ⏱️ 10:05 • 10h ago

---

**[Google Just Unveiled Its Most Advanced AI Robots Yet - Gemini Robotics 2](https://www.youtube.com/watch?v=s42VQasz4iI)**

Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726 Subscribe To My Newsletter ...

📺 TheAIGRID

👁️ 25K • 👍 481 • 💬 39 • ⏱️ 9:54 • 2d ago

---

**[Study: US AI Ban Could Cost Up To $12 Billion](https://www.youtube.com/watch?v=7FIdtBZE0Ak)**

A potential US ban on Chinese open-weight artificial intelligence (AI) models could cost American businesses up to US$12 billion ...

📺 WION

👁️ 192 • 👍 4 • 💬 2 • ⏱️ 2:12 • 1h ago

---

**[the king of ai cringe](https://www.youtube.com/watch?v=0SJHeltgAhY)**

the original vibe guru Music: Dolce Vita - Peyruis Mood- Peyruis First Class - Peyruis.

📺 Eric Morrison

👁️ 43K • 👍 3K • 💬 784 • ⏱️ 13:32 • 2d ago

---

**[I Tested AI Life Hacks!](https://www.youtube.com/watch?v=NyAnh1ofyYs)**

Reacts Channel : https://www.youtube.com/@VladandChrisReacts Gaming Channel: ...

📺 Vlad and Chris

👁️ 311K • 👍 4K • 💬 336 • ⏱️ 28:09 • 20h ago

---

**[How to Learn to Build an App Using AI in 15 minutes](https://www.youtube.com/watch?v=Hk_58FZMRkk)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 ...

📺 Mikey No Code

👁️ 6K • 💬 6 • ⏱️ 27:13 • 2h ago

---

**[First AI Domino to Fall?](https://www.youtube.com/watch?v=py23zYn1GMw)**

Will Oracle be the first AI Domino to fall? Oracle now carries more than $160 billion in debt, its credit rating sits one notch above ...

📺 Kiraa

👁️ 172K • 👍 6K • 💬 797 • ⏱️ 8:38 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 967,622 • ❤️ 9,801 • 7d ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 236,076 • ❤️ 1,994 • 2d ago

---

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 0 • ❤️ 1,227 • 25m ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 1,550,034 • ❤️ 1,408 • 3d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,601,062 • ❤️ 3,833 • 5d ago

---

**[DeepSeek-V4-Flash-0731-GGUF](https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731-GGUF)**

*Unsloth AI*

DeepSeek-V4-Flash-0731 is a quantized LLM optimized with Unsloth for enhanced agentic capabilities and competitive performance against proprietary models. It excels in code generation, complex reasoning, and multi-turn interactions, making it suitable for advanced AI agent applications.

`19.8B`

⬇️ 69,656 • ❤️ 404 • 6h ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 2 • ❤️ 376 • 4h ago

---

**[Kimi-K3-GGUF](https://huggingface.co/unsloth/Kimi-K3-GGUF)**

*Unsloth AI*

Kimi K3 is a 2.8T parameter open-weight multimodal agentic model with native vision and a 1M token context window, excelling at long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency.

`image-text-to-text` `2779.5B`

⬇️ 128,215 • ❤️ 278 • 4d ago

---

**[Inkling-Small](https://huggingface.co/thinkingmachines/Inkling-Small)**

*Thinking Machines Lab*

Inkling-Small is a 276B parameter multimodal transformer (image, text, audio to text) with a sparse MoE architecture, suitable for conversational AI, coding assistants, and RAG systems.

`image-text-to-text` `266.0B`

⬇️ 8,504 • ❤️ 255 • 3d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 2,180,509 • ❤️ 4,791 • 1mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 446 • 💬 9 • ⭐ 7,953 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 75 • 💬 6 • ⭐ 21,791 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 51 • 💬 4 • ⭐ 35,708 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Native and Compact Structured Latents for 3D Generation](https://huggingface.co/papers/2512.14692)**

*Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu et al. (11 authors)*

🏢 Microsoft

A new sparse voxel representation called O-Voxel enables high-quality 3D generative modeling with efficient inference and robust topology handling.

▲ 6 • 💬 0 • ⭐ 10,227 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.14692) • [💻 code](https://github.com/microsoft/TRELLIS.2) • [🔗 project](https://microsoft.github.io/TRELLIS.2/)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 40 • 💬 5 • ⭐ 6,543 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 177 • 💬 10 • ⭐ 51,890 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Scaling Properties of Text Conditioning in Visual Generation](https://huggingface.co/papers/2607.29679)**

*Zilong Chen, Chaorui Deng, Kunchang Li et al. (5 authors)*

We study empirical scaling properties for text conditioning in visual generation. Such properties have rarely been measured because diffusion loss does not scale with the number of tokens in natural-language prompts. Surprisingly, we find that the converged diffusion loss scales with the amount of structured language in the prompt. To quantify structured language, we adapt two complementary measures: a white-box likelihood metric (GPG) and a black-box attribute metric (ED). Across controlled training runs, the converged diffusion loss decreases approximately linearly with GPG and follows a power law with ED. Guided by these scaling properties, we improve diffusability by constructing structured prompts with semantic and geometric annotations derived from images, and improve promptability by training a prompter through supervised fine-tuning, cold-start, and verifier-gated on-policy distillation. The resulting system outperforms all evaluated open-weight models on nearly every compositional, reasoning, and world-knowledge benchmark, while matching or surpassing the strongest closed-weight models on most evaluations.

▲ 23 • 💬 1 • ⭐ 55 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.29679) • [💻 code](https://github.com/heheyas/context-scaling) • [🔗 project](https://heheyas.github.io/context-scaling/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 117 • 💬 4 • ⭐ 95,459 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 76,602 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 82,935 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

`Python`

⭐ 3.9k • 🔱 302 • 16h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 3.4k • 🔱 286 • 6d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 3.2k • 🔱 399 • 1h ago

---

**[MIgHTy-alIeN/MEV-Ethereum-Trading-Bot](https://github.com/MIgHTy-alIeN/MEV-Ethereum-Trading-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.0k • 🔱 1.4k • 58s ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.9k • 🔱 216 • 2d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `agent` `agentic-ai` `voice-agent` `voice-ai` `voice-chat`

⭐ 1.8k • 🔱 121 • 9m ago

---

**[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)**

Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

`TypeScript` `a-stock` `ai-agent` `dashboard` `fastapi` `fintech`

⭐ 1.8k • 🔱 348 • 3d ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.7k • 🔱 134 • 12d ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 1.6k • 🔱 200 • 5m ago

---

**[AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish)**

Agent skill: make LLMs write docs in ASD-STE100 Simplified Technical English — no AI slop

`Python`

⭐ 1.4k • 🔱 54 • 13d ago

---

---

*Generated by PeekDeck - A glance is all you need*
