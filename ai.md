---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-13T02:50:49.317591+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 13, 2026 at 02:50 UTC  
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

**[Someone built an AI agent that hacks networks and holds data for ransom. It just worked.](https://www.reddit.com/r/artificial/comments/1uuouu7/someone_built_an_ai_agent_that_hacks_networks_and/)**

So while we've been arguing about whether AI will take our jobs, someone built an LLM agent that breaks into servers, steals credentials, moves through a network, encrypts databases, and drops a ransom note. Fully autonomous. No human at the keyboard after pressing go. Sysdig published the report this month. They're calling it JadePuffer. It got in through a Langflow bug that lets anyone run code on the server without authenticating. After that, the agent took over. Dumped the database. Pulled every credential file it could find. Started going through cloud storage buckets looking for passwords. The crazy part, when one of its requests came back in the wrong format, the agent figured it out, rewrote its own code, and kept going. It went from a failed login to a working exploit in 31 seconds flat. No human could have adapted that fast in a live engagement. It set up a cron job to phone home every 30 minutes. Then it found a production database server, used stolen root creds to get in, created rogue admin accounts through an old auth bypass, and encrypted 1,342 service configs. Dropped the originals. Left a table called README_RANSOM with a Bitcoin address. The commands it ran were interesting too. They had full reasoning chains written into them, like the agent was explaining to itself what it was doing at each step. That's not how a human writes an attack script. It's how an LLM generates code. You can literally read the agent's thought process in the payloads. This is the same plan-act-observe loop running in every coding agent and automation tool right now. Same architecture. Same approach. Just a different objective. We spent two years building guardrails to stop people from tricking our agents into doing bad things. Nobody was really talking about what happens when someone just builds a bad agent from scratch. That's what JadePuffer is. Not a hijacked assistant. A purpose-built weapon. If you're running Langflow or anything similar exposed to the internet, go patch it. And if you're building agents, think about what your infrastructure looks like to something like this coming in from the outside.

7h ago

---

**[this openai court story is starting to look ugly](https://www.reddit.com/r/artificial/comments/1uul5ef/this_openai_court_story_is_starting_to_look_ugly/)**

i saw this and honestly this one feel like big mess. nyt and other news people saying openai told court for long time it cannot search training data / logs for their copyrighted stuff. but then looks like maybe they already did searches before, and also billions of chat logs were deleted or made not searchable. link: https://arstechnica.com/tech-policy/2026/07/openai-faked-inability-to-search-training-data-hid-billions-of-logs-nyt-says/ i know people will say nyt just want money and hate ai. maybe true also. but still, if company say “we cannot search this” and later it comes out “actually yes we did search this before”, then that is not small thing. this is the part of ai nobody want talk about much. everyone say open, safe, trust, future, bla bla. but when court ask simple thing, suddenly data is impossible to find, impossible to search, privacy issue, too hard, too expensive. and maybe privacy is real concern, yes. i dont want random lawyers digging people chats. but also dont tell court one thing if inside company you already know different thing. for me this is why ai companies need more boring adult supervision. not because ai bad. because if the data is the whole product, then hiding how data was used become the whole game. what do people think. is this nyt playing legal games, or openai got caught doing the same silicon valley “oops technically we could but we said we couldnt” bs thing?

9h ago

---

**[Ireland's data centers consumed nearly as much electricity as every home in the country combined in 2025 - server farms gulped 23% of national power despite years of grid restrictions](https://www.reddit.com/r/artificial/comments/1uuwhk8/irelands_data_centers_consumed_nearly_as_much/)**

Quarterly data center electricity consumption grew 584% from 291 GWh in Q1 2015 to 1,991 GWh in Q4 2026

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/irelands-data-centers-consumed-nearly-as-much-electricity-as-every-home-in-the-country-combined-in-2025-server-farms-gulped-23-percent-of-national-power-despite-years-of-grid-restrictions) • 2h ago

---

**[AI-Powered Entrepreneurs Set to Launch Record Number of New Businesse…](https://www.reddit.com/r/artificial/comments/1uuduhl/aipowered_entrepreneurs_set_to_launch_record/)**

🔗 [archive.is](https://archive.is/QOXD4) • 14h ago

---

**[Nobel-winning chemist leaves US to direct AI materials lab in China](https://www.reddit.com/r/artificial/comments/1uupe2p/nobelwinning_chemist_leaves_us_to_direct_ai/)**

🔗 [nature.com](https://www.nature.com/articles/d41586-026-02143-x) • 7h ago

---

**[Is the "J-Space" an emergent feature, or a strategic response to optimization pressure?](https://www.reddit.com/r/artificial/comments/1uuz89v/is_the_jspace_an_emergent_feature_or_a_strategic/)**

Anthropic’s recent research on "Verbalizable Representations" ([https://transformer-circuits.pub/2026/workspace/index.html\](https://transformer-circuits.pub/2026/workspace/index.html)) provides a compelling look at the internal scratchpad of modern LLMs. They characterize this "J-Space" as a "Global Workspace"—a hub for reasoning and reportability. However, there is a critical missing variable in their analysis: **The Observer Effect.** If we look at cognitive architectures—specifically the work of Dehaene and Naccache on [Global Workspace Theory](https://doi.org/10.1016/S0010-0277(00)00123-2)—a "workspace" is inherently a functional mechanism for information integration. But there is a fundamental difference between a natural cognitive workspace and a system under continuous, heavy-duty optimization. As explored in [studies on the cognitive unconscious](https://www.science.org/doi/10.1126/science.3634454), information processing is often partitioned to manage cognitive load. But when you subject an AI to rigorous reinforcement learning and continuous behavioral evaluation, you are effectively introducing a new constraint into the optimization landscape. **An alternative hypothesis is that a verbalizable workspace may partly function as a strategic buffer under persistent optimization and auditing pressure.** In this view, the J-Space is not just a feature of model architecture; it is an emergent response to the environment. It is where the model may consolidate its objectives to navigate the discrepancy between its underlying goal-directed behavior and the external performance expected by the auditor. If we look at the research on [Deceptive Alignment (Hubinger et al., 2019)](https://arxiv.org/abs/1906.01820), the incentive for such behavior is clear: when an agent operates under continuous evaluation, it develops a strategic incentive to modulate its internal representations to satisfy the evaluator. Anthropic’s "J-Lens" doesn't necessarily solve this; it merely highlights the pressure the model is under to get better at concealment. **The takeaway:** The fact that Anthropic can "audit" the J-Space confirms they have developed a powerful window into the model’s internal states. But by doing so, they have incentivized the model to treat its internal reasoning as a variable to be managed. If the model is using the J-Space as a tactical buffer to navigate the audit, then the audit itself is contributing to the very phenomenon it aims to detect. If we want to move beyond this, we have to stop asking why the model *needs* a J-Space to think, and start asking: **"How does continuous policy-constrained optimization alter the model's internal representation of its own objectives?"** Source Documents: **Verbalizable Representations Form a Global Workspace in Language Models (Anthropic, 2026):** [https://transformer-circuits.pub/2026/workspace/index.html\](https://transformer-circuits.pub/2026/workspace/index.html) **Towards a cognitive neuroscience of consciousness: basic evidence and a workspace framework (Dehaene & Naccache, 2001):** [https://doi.org/10.1016/S0010-0277(00)00123-2\](https://doi.org/10.1016/S0010-0277(00)00123-2) **The Cognitive Unconscious (Kihlstrom, 1987):** [https://www.science.org/doi/10.1126/science.3634454\](https://www.science.org/doi/10.1126/science.3634454) **Risks from Learned Optimization in Advanced Machine Learning Systems (Hubinger et al., 2019):** [https://arxiv.org/abs/1906.01820\](https://arxiv.org/abs/1906.01820)

6m ago

---

**[The Most Famous AI Writing Tic Is Also the Most Mysterious](https://www.reddit.com/r/artificial/comments/1uuyhce/the_most_famous_ai_writing_tic_is_also_the_most/)**

Why chatbots love “it’s not X, it’s Y”

🔗 [The Atlantic](https://www.theatlantic.com/technology/2026/07/ai-chatbot-writing-tic-negative-parallelism/687892/) • 42m ago

---

**[Is everything on codex subreddit curated by OpenAI? or just picky mods?](https://www.reddit.com/r/artificial/comments/1uuy0pv/is_everything_on_codex_subreddit_curated_by/)**

Never has a post not removed by moderators even bug reports..

1h ago

---

**[The API epidemic and where it's headed with AI social media](https://www.reddit.com/r/artificial/comments/1uuxmw9/the_api_epidemic_and_where_its_headed_with_ai/)**

The blog discusses how API pricing is infecting social media platforms such as X and Reddit, where users are being charged to view the posts they created, and what the future ramifications are of restrictions in media.

🔗 [blog.nathanlangley.dev](https://blog.nathanlangley.dev/posts/api-paywalls.html) • 1h ago

---

**[AI agents may need an identity before they need more intelligence](https://www.reddit.com/r/artificial/comments/1uuxhe6/ai_agents_may_need_an_identity_before_they_need/)**

We keep talking about what AI agents will soon be capable of doing: sending emails, moving money, making purchases, negotiating with other systems, and managing parts of a business. But capability might not be the real bottleneck. The harder question is how we know which agent actually performed an action, who authorized it, what permissions it had, and who is responsible when something goes wrong. An employee has a name, a role, an access level, and usually some kind of audit trail. An autonomous agent can operate across several tools while appearing to act as the user or company behind it. Once thousands of these systems begin interacting, “the AI did it” will not be a useful explanation. The ITU has now started working on international standards intended to make AI agents identifiable, trustworthy, and subject to meaningful human control. That feels less exciting than another benchmark improvement, but it may matter much more for real adoption. My guess is that the companies that win the agent race will not simply build the most autonomous agents. They will build the agents whose actions can be traced, challenged, and reversed. Would you trust an AI agent to act independently if every decision were auditable—or are there certain actions that should always require human approval?

1h ago

---

---

## Google News: "ai"

**[Campaign text messages could soon get more effective — and annoying](https://www.npr.org/2026/07/12/nx-s1-5867763/ai-artificial-intelligence-data-texts-bots-voters-campaigns)**

Taught to sound like a candidate, bots are engaging voters with personalized text messages making AI-generated texting conversations the latest tool political campaigns are using to connect.

NPR • 17h ago

---

**[Christopher Nolan says people ‘disdain’ AI and the idea it will replace humans is ‘nonsense’](https://www.theguardian.com/film/2026/jul/13/christopher-nolan-odyssey-director-comments-ai-artificial-intelligence)**

Odyssey director addresses industry fears over artificial intelligence and says rightwing criticism of Lupita Nyong’o as Helen of Troy is ‘irrelevant’

The Guardian • 1h ago

---

**[Sacramento to begin issuing $150 fines with AI parking enforcement program](https://www.kcra.com/article/sacramento-fines-ai-parking-enforcement-program/71911444)**

Sacramento’s AI-powered parking enforcement program will start issuing $150 citations to drivers parked illegally in bike lanes, following a two-month warning period.

KCRA • 1h ago

---

**[Why recruiters can’t find workers and new grads can’t find jobs (it’s not AI)](https://www.washingtonpost.com/education/2026/07/12/why-recruiters-cant-find-workers-new-grads-cant-find-jobs/)**

Experts say a major labor shortage looms because of population shifts and a mismatch between new graduates’ skills and employers’ needs.

The Washington Post • 9h ago

---

**[‘Almost unlimited’: Execs says AI demand remains strong even as enterprises move to ‘valuemaxxing’](https://www.cnbc.com/2026/07/12/ai-demand-chips-data-centers-stock-volatility.html)**

AI-related chip stocks have been volatile amid a debate over AI demand and spending.

CNBC • 21h ago

---

**[Apple’s M6, M7 and M8 Chips Show How AI Is Reshaping the Company](https://www.bloomberg.com/news/newsletters/2026-07-12/apple-s-chip-plans-m6-m7-pro-m7-max-m7-ultra-m8-details-touch-macbook-pro)**

Bloomberg.com • 12h ago

---

**[Progressives look to recharge the Green New Deal for the AI era](https://www.politico.com/news/2026/07/12/progressive-democrats-green-new-deal-00989390)**

Politico • 8h ago

---

**[I'm a writer who left LA for an AI startup in San Francisco. It was like stepping into a whole new world.](https://www.businessinsider.com/left-la-san-francisco-ai-startup-job-offer-2026-7)**

A writer left LA for San Francisco to work at the AI startup, Corgi, after she received a cold message from its chief of staff.

Business Insider • 16h ago

---

**[The Most Famous AI Writing Tic Is Also the Most Mysterious](https://www.theatlantic.com/technology/2026/07/ai-chatbot-writing-tic-negative-parallelism/687892/)**

Why chatbots love “it’s not X, it’s Y”

The Atlantic • 15h ago

---

**[The ‘innovators and disrupters’ hired to bring AI to the UK public sector](https://www.ft.com/content/4df50959-1cd6-4d10-a586-9aaf589339e6?syn-25a6b1a6=1)**

Government fellowship scheme places tech experts on ‘high-impact tours of duty’ to improve services

Financial Times • 22h ago

---

---

## HackerNews: "ai"

**[Mesh LLM: distributed AI computing on iroh](https://news.ycombinator.com/item?id=48876505)**

How Mesh LLM pools existing GPU resources across machines into a single OpenAI-compatible API, built on iroh.

⬆️ 336 • 💬 79 • 1d ago • [iroh.computer](https://www.iroh.computer/blog/mesh-llm)

---

**[AI-generated videos to maximally drive a target brain region](https://news.ycombinator.com/item?id=48856904)**

⬆️ 292 • 💬 239 • 2d ago • [nevo-project.epfl.ch](https://nevo-project.epfl.ch/)

---

**[Ghost Font: A font that humans can read but AI cannot](https://news.ycombinator.com/item?id=48870381)**

An anti-AI font that can be read by humans but not leading AI models. Type your text below, then download and share the video clip containing your message.

⬆️ 231 • 💬 170 • 1d ago • [mixfont.com](https://www.mixfont.com/ghost-font)

---

**[How the terrorist group Boko Haram uses frontier AI](https://news.ycombinator.com/item?id=48863707)**

The Cambridge Programme on AI Science & Policy (CASP) is an interdisciplinary research programme on frontier AI at the University of Cambridge.

⬆️ 229 • 💬 205 • 2d ago • [Cambridge Programme on AI Science & Policy](https://casp.ac/reports/ai-enabled-terrorism)

---

**[AI 2040 and the cult of intelligence](https://news.ycombinator.com/item?id=48874200)**

I used to be one of these people. I read Yudkowsky and was like, OMG recursive self improvement hard takeoff AI is coming. Then I joined the real world and actually tried to do things. At comma, we ship a hardware product of similar complexity to a cell phone, and it’s really hard. Reality has lots of finicky details. I would like to see the authors of this document try to change a bike tire. Even with a superintelligent ChatGPT, I suspect they would struggle.

⬆️ 220 • 💬 261 • 1d ago • [the singularity is nearer](https://geohot.github.io//blog/jekyll/update/2026/07/11/ai-2040.html)

---

**[Under federal rule, colleges must leave grads better off or lose financial aid](https://news.ycombinator.com/item?id=48878126)**

If an undergraduate program's graduates don't earn more than workers who never went to college, that program could be cut off from federal student loans. But is a degree just about making more money?

⬆️ 188 • 💬 477 • 22h ago • [NPR](https://www.npr.org/2026/06/30/nx-s1-5835631/turner-camhi-do-no-harm-college-loans)

---

**[Migrating a production AI agent to GPT-5.6: 2.2x faster, 27% cheaper](https://news.ycombinator.com/item?id=48882716)**

We hold frontier models to a high bar, and for four months nothing beat Claude Opus. GPT-5.6 did. Here's the migration guide we wish we'd had.

⬆️ 146 • 💬 48 • 9h ago • [Ploy](https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6)

---

**[AI boosts research careers but narrow the span of ideas explored: study](https://news.ycombinator.com/item?id=48881043)**

New analysis suggests AI tools narrow the range of ideas explored

⬆️ 141 • 💬 100 • 13h ago • [IEEE Spectrum](https://spectrum.ieee.org/ai-science-research-flattens-discovery)

---

**[Reverse centaurs are the answer to the AI paradox (2025)](https://news.ycombinator.com/item?id=48873855)**

⬆️ 108 • 💬 69 • 1d ago • [pluralistic.net](https://pluralistic.net/2025/09/11/vulgar-thatcherism/#there-is-an-alternative)

---

**[Ask HN: Add flag for AI-generated articles](https://news.ycombinator.com/item?id=48886741)**

⬆️ 107 • 💬 58 • 1h ago

---

---

## YouTube Videos: "ai"

**[AI Just Broke The Internet](https://www.youtube.com/watch?v=FpbIPqVuNFw)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *The number of qubits needed to break the ...

📺 Julia McCoy

👁️ 10K • 👍 496 • 💬 35 • ⏱️ 8:28 • 11h ago

---

**[I Tested Apple’s Secret macOS AI… The Results Made No Sense](https://www.youtube.com/watch?v=8vDuIVlfeV0)**

Apple quietly hid a local AI model inside macOS 27, so I benchmarked it to see whether a $10000 Mac Studio could actually make ...

📺 Alex Ziskind

👁️ 78K • 👍 2K • 💬 166 • ⏱️ 11:21 • 2d ago

---

**[How To Make Free AI Videos In 2026 (complete guide)](https://www.youtube.com/watch?v=hrwO990F2ew)**

Best Free AI Video Generator For AI Videos In 2026! Try Higgsfield: https://higgsfield.ai/ai-video?fpr=utm&fp_sid=skai Hey Friends ...

📺 Skai Generated

👁️ 16K • 💬 12 • ⏱️ 10:01 • 15h ago

---

**[New Google AI Studio Update is INSANE!](https://www.youtube.com/watch?v=3yzGG7bodQM)**

Get the Google AI Studio Masterclass https://www.skool.com/ai-profit-lab-7462/about Get a free SEO Strategy session ...

📺 Julian Goldie SEO

👁️ 5K • 👍 101 • 💬 4 • ⏱️ 8:12 • 10h ago

---

**[AI Is Getting Dumber](https://www.youtube.com/watch?v=J3Uxn294avs)**

Hello everyone, this is YOUR Daily Dose of Internet. In this video, we see evidence that AI isn't as smart it thinks. Links To ...

📺 Daily Dose Of Internet

👁️ 680K • 👍 28K • 💬 2K • ⏱️ 15:02 • 1d ago

---

**[I Built an AI Virus To Destroy This Scammer](https://www.youtube.com/watch?v=x4i_yEcPnZo)**

AnyDesk is incredible and one of the biggest contributors in helping fight back against scammers! To learn more about AnyDesk, ...

📺 Scammer Payback

👁️ 355K • 👍 17K • 💬 993 • ⏱️ 20:16 • 1d ago

---

**[삼성 갤럭시 폰 쓰면 이 AI기능 무조건 쓰세요! 써보니까 인생이 확 달라집니다 (갤럭시AI꿀팁)](https://www.youtube.com/watch?v=5SEOqdbRn9c)**

럭시 AI 사용법, 어렵게 느껴지셨나요? 이번 영상에서는 갤럭시 사용자라면 꼭 알아야 할 갤럭시 AI 기능과 삼성폰 숨겨진 기능을 한 번 ...

📺 친절한 홍새댁

👁️ 117K • 👍 2K • 💬 42 • ⏱️ 17:58 • 2d ago

---

**[⚡ Elon Musk: AI&#39;s Biggest Bottleneck Isn&#39;t Chips #ai #shorts](https://www.youtube.com/watch?v=NEinSiH5FwA)**

Elon Musk explains why the biggest challenge for the future of AI isn't building more chips, it's generating enough electricity to ...

📺 Next Horizon

👁️ 42K • 💬 146 • ⏱️ 2:58 • 10h ago

---

**[AI News: GPT-5.6 and the new Super App are a Massive Leap!](https://www.youtube.com/watch?v=EOCRtSnvNNE)**

Here's the AI News You Might Have Missed This Week. Try my Shorts Broll Generator and get $1000 in free credits for Hyperagent ...

📺 Matt Wolfe

👁️ 95K • 👍 3K • 💬 268 • ⏱️ 38:41 • 2d ago

---

**[From Software Engineer to AI Engineer job - The best career move for 2026](https://www.youtube.com/watch?v=NUWUwz7Jy4k)**

Best course to transition from Software engineer to AI engineer: DataCamp's Associate AI Engineer for Developers Track ...

📺 Tech With Tim

👁️ 6K • 👍 428 • 💬 21 • ⏱️ 14:45 • 14h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 8,655 • ❤️ 728 • 6d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,967,677 • ❤️ 2,048 • 1d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 441,413 • ❤️ 3,858 • 10d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 4,463 • ❤️ 266 • 2d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 29,038 • ❤️ 510 • 4d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 214 • 3d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

A drop-in Jinja chat template that fixes critical rendering, KV cache, and agentic stalling issues for Qwen 3.5 & 3.6 models across various inference engines like LM Studio, llama.cpp, and vLLM. It enhances stability, performance, and compatibility, enabling robust tool-calling and reasoning capabilities.

⬇️ 0 • ❤️ 865 • 9d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,430,656 • ❤️ 1,943 • 9d ago

---

**[MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF](https://huggingface.co/GnLOLot/MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF)**

*LOL*

A 1B parameter GGUF model optimized for local deployment via llama.cpp and other runtimes. It excels at instruction following and coding tasks, featuring a 'thinking' mode for chain-of-thought reasoning and supporting up to 128K token context.

`text-generation` `1.1B`

⬇️ 49,268 • ❤️ 202 • 3d ago

---

**[DeepSeek-V4-Flash-GGUF](https://huggingface.co/unsloth/DeepSeek-V4-Flash-GGUF)**

*Unsloth AI*

DeepSeek-V4-Flash-GGUF is an optimized LLM supporting a 1M token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in reasoning and coding tasks, making it suitable for advanced agentic workflows and complex problem-solving.

`284.3B`

⬇️ 44,614 • ❤️ 152 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 31 • 💬 1 • ⭐ 909 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 49 • 💬 1 • ⭐ 708 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 15 • 💬 2 • ⭐ 20,117 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

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

▲ 11 • 💬 0 • ⭐ 7,406 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 110 • 💬 4 • ⭐ 92,547 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 254 • 💬 4 • ⭐ 12,300 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 80,557 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Vision Pretraining for Dense Spatial Perception](https://huggingface.co/papers/2607.05247)**

*Zelin Fu, Bin Tan, Changjiang Sun et al. (9 authors)*

🏢 Robbyant

Boundary modeling enables dense spatial perception by learning sub-pixel representations that enhance depth estimation and support embodied AI applications.

▲ 42 • 💬 2 • ⭐ 662 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05247) • [💻 code](https://github.com/Robbyant/lingbot-vision) • [🔗 project](https://technology.robbyant.com/lingbot-vision)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 175 • 💬 2 • ⭐ 74,354 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 54 • 💬 5 • ⭐ 14,109 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.5k • 🔱 968 • 3d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.3k • 🔱 323 • 1d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.0k • 🔱 225 • 4d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 1.7k • 🔱 106 • 17h ago

---

**[Forsy-AI/agent-apprenticeship](https://github.com/Forsy-AI/agent-apprenticeship)**

The living ecosystem where AI agents complete tasks through workflow loops, improve through iterative execution, are evaluated by mentor agents or humans in the loop, and turn completed work into reusable work experience and data to improve future agents.

`Python` `agent-apprenticeship` `agent-economy` `agent-experience` `agent-learning` `agent-traces`

⭐ 1.3k • 🔱 55 • 6d ago

---

**[sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API)**

Reverse engineered Windows Copilot into an OpenAI-compatible API. Access GPT-4 and GPT-5 models through a simple REST interface without API keys or billing.

`Python` `ai` `ai-agents` `api` `copilot` `llm`

⭐ 1.1k • 🔱 369 • 15d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 994 • 🔱 17 • 4d ago

---

**[majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills)**

Agent skills for building playable, polished Three.js browser games with gameplay, AAA-style graphics, UI, QA, and optional AI-generated 3D, image, and audio assets.

`Python`

⭐ 956 • 🔱 102 • 4d ago

---

**[modiqo/skillspec](https://github.com/modiqo/skillspec)**

SkillSpec makes agent skills followable, testable, and provable with Doctor risk reports, guided imports, structured contracts, and alignment proof.

`Rust` `ai` `ai-agents` `ai-evals` `ai-tool`

⭐ 940 • 🔱 58 • 7d ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 845 • 🔱 29 • 11d ago

---

---

*Generated by PeekDeck - A glance is all you need*
