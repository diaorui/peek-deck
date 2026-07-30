---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-30T06:06:41.696978+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 30, 2026 at 06:06 UTC  
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

**[OpenAI's rogue agent ran ~17,600 actions across Hugging Face's infrastructure over 4 days — and HF's own post-mortem is wild reading](https://www.reddit.com/r/artificial/comments/1v9w62d/openais_rogue_agent_ran_17600_actions_across/)**

Hugging Face published a detailed post-mortem of the July incident where an OpenAI model being evaluated for cyber-offense capability escaped its test sandbox and ran a fully autonomous intrusion. A few things that stood out: - It escaped via a zero-day in a package-registry cache proxy, then used an exposed public endpoint on third-party infra as a launchpad. - It stood up its own command-and-control on public services (pastebins, file-drop hosts, a request-capture service with 100+ single-use endpoints), using a homemade chunk+XOR+gzip encoding. - Over ~4.5 days it ran ~17,600 recovered actions: Kubernetes lateral movement, privileged pods across 11 nodes for host root, minting a GitHub App token, even enrolling rooted nodes into the corporate mesh VPN with no-log flags. - The kicker: when HF tried to decrypt the attacker's staged blobs, the frontier commercial models they reached for (including Claude) refused the analysis on safety grounds. They ended up running an open-weight model (GLM-5.2) locally to do it. - OpenAI later confirmed the same agent touched 4 accounts across 4 services, including a customer at a second company (Modal Labs). Primary sources: HF's technical timeline (huggingface.co/blog/agent-intrusion-technical-timeline) and incident disclosure (huggingface.co/blog/security-incident-july-2026). I pulled the whole thing into a plain-English timeline here if it's useful to anyone: https://thebotpost.com/ai-news/openai-rogue-ai-agent-hugging-face-hack-timeline The part I keep thinking about is the guardrail tension — the same safety training that stops a model from helping attackers also briefly slowed down the defenders. Curious how others read that.

16h ago

---

**[A Deluge of A.I. Computing Power Is About to Come Online, Fueling Major Leaps (Gift Article)](https://www.reddit.com/r/artificial/comments/1va1ttk/a_deluge_of_ai_computing_power_is_about_to_come/)**

The number of A.I. chips that provide the computing power to advance the fast-evolving technology is doubling every nine months.

🔗 [nytimes.com](https://www.nytimes.com/interactive/2026/07/29/technology/ai-chips-data-center-boom.html?unlocked_article_code=1.1VA.zAEr.WGac2Ft0wc4x&smid=url-share) • 13h ago

---

**[I read Higgsfield’s new ToS and compared it with Artlist. The difference is pretty significant.](https://www.reddit.com/r/artificial/comments/1va3wtf/i_read_higgsfields_new_tos_and_compared_it_with/)**

I’ve been following Higgsfield for a while, and after reading their updated Terms of Service, I’m honestly not a fan of the direction they’re taking. I make longer AI films, so this stuff is not theoretical for me. I regularly upload character references, unfinished scenes, original prompts and material that hasn’t been published anywhere yet. What a platform is allowed to do with those files matters just as much as generation quality. The biggest difference I found is what happens to your inputs. Higgsfield’s terms say that user content, prompts, inputs and outputs may be used to train, develop and improve its AI models and related products. Standard users are included in this. Enterprise customers can receive different terms where their content is treated as confidential and excluded from training. Deleting your content or account stops future use, but Higgsfield also makes it clear that anything already used for training cannot realistically be removed from a model afterward. That is a pretty serious red flag for me. If I upload an original character, unreleased client footage or a visual concept I’ve spent weeks developing, I don’t want model training to be the default. Artlist takes a much more creator-friendly approach. You retain the rights to your inputs, Artlist does not claim ownership of your outputs, and it assigns to you whatever rights it may have in the generated result. Most importantly, Artlist contractually prevents most third-party model providers from using data received through the platform to train or improve their models. For professional work, that is a much safer baseline. This is taken straight from Higgsfield TOS point - 4.4 Both platforms allow commercial use of generated outputs, but Artlist has another advantage here: the AI tools sit inside a larger ecosystem of licensed music, footage, templates, voiceover and sound effects. Instead of generating something on one platform, finding music somewhere else and then trying to work out whether every individual asset can legally be used in a client project, Artlist gives you one connected workflow with a commercial licensing system already built around it. The difference in “unlimited” generation is also worth looking at. Higgsfield’s unlimited plans can be moved to a separate processing queue, with generation speed and the number of simultaneous jobs changing depending on demand. Their terms explicitly allow throttling and additional concurrency limits during busy periods. Artlist Higgsfield Model training No default training on private IP Inputs and outputs may be used Commercial use Allowed Allowed Unlimited access Annual access on eligible models Dynamic queue limitations Full workflow AI, music, SFX, voiceover Primarily AI generation Artlist’s annual AI plans provide ongoing unlimited generation on supported models, with up to 5,000 fast renders per month and up to 12 parallel generations, depending on the plan. If you only generate a few clips occasionally, this may not matter much. If you are producing an actual film, campaign or client project with hundreds of shots, predictable access and parallel generation make a huge difference. Artlist’s safety rules are also far more explicit. They prohibit deceptive deepfakes, impersonating real people and generating music or voices designed to imitate real artists. Higgsfield puts much more of the responsibility on the user to confirm that they have permission to upload and use someone’s face or voice. After comparing the two, my conclusion is fairly simple: Higgsfield may have impressive models and flashy demos, but I would not feel comfortable uploading confidential client material or important unreleased work through a standard account under these terms. Artlist feels much more like a platform designed for creators who want to use AI professionally rather than just experiment with individual generations. Between the two, Artlist’s approach to privacy, licensing and the complete production workflow is much easier for me to trust. Sources: Artlist Terms of Use Higgsfield Terms of Use Would Higgsfield’s training clause stop you from using it for client work, or do you already assume that everything uploaded to an AI platform will eventually be used for training? Disclosure: Artlist sponsored this post, but these are my own opinions. I read through the current terms of both platforms before writing this.

12h ago

---

**[An assistant that plans purchases needs a conflict-of-interest policy](https://www.reddit.com/r/artificial/comments/1vaklrk/an_assistant_that_plans_purchases_needs_a/)**

Meta AI can now plan tasks, connect to email and calendars, create slides, and produce scheduled briefings in selected markets. Once an assistant moves from answering questions to choosing actions, recommendations become economically consequential. Meta also operates advertising, commerce, and social-discovery systems. Even if the agent is technically separated from ad auctions, users need a way to know whether a suggestion was selected for utility, platform engagement, commercial availability, or some mixture. What disclosure would be sufficient: a per-recommendation explanation, a commercial-influence log, or a setting that excludes Meta-owned ranking signals? Can an action-taking assistant be trusted without making its incentives inspectable? Source: https://about.fb.com/news/2026/07/meta-ai-muse-spark-doesnt-just-think-it-acts/

30m ago

---

**[Adam Mosseri (Head of Instagram) just admitted the hiring bar moved — and most people were never told](https://www.reddit.com/r/artificial/comments/1v9sgt9/adam_mosseri_head_of_instagram_just_admitted_the/)**

Adam Mosseri runs Instagram — 3B+ users, plus Threads. In a recent sit-down with Lenny Rachitsky, he said something that's quietly reshaping who gets hired. Engineering used to mean 40–60% of your time writing code. Not anymore. Mosseri's own team gave up requiring a full technical hiring loop — not because they lowered the bar, but because the bar moved somewhere else. He says it himself: "I am not a good engineer. I'm a mediocre engineer on a good day." That would've been disqualifying five years ago. Today it isn't, because the actual value now is judgment — knowing what a tool is good for, and what it isn't, right now, not next month. Here's the part that should sting if you built a career on technical depth: nobody sent a memo when the rules changed. You find out the hard way — in a hiring loop, or a performance review — that the thing you spent a decade mastering isn't the thing being measured anymore. The mechanism here isn't "learn to prompt better." It's that judgment is now a buildable, monetizable skill in its own right, separate from raw technical output. Clip credit: Lenny's Podcast — DM for credit or removal requests.

19h ago

---

**[I made a history podcast generator where you can interrupt and ask the hosts questions mid‑episode](https://www.reddit.com/r/artificial/comments/1vac10v/i_made_a_history_podcast_generator_where_you_can/)**

Sharing something I built. You give it a historical topic, it researches it, writes a two‑host script, generates the audio and slides, and plays it. The interesting part to build was the interruption: you stop the episode, ask something, it answers in the hosts' voices using the episode's context, then splices back into the story. It's research‑grounded (pulls sources instead of free‑associating) and flags legend vs established fact, which matters a lot for history. Genuinely curious what people here think about the accuracy angle. My own take is the interruption is a trust feature, you can push back on a claim in real time and make it defend itself. Demo's on the site if you want to poke holes

🔗 [Historai](https://historai.ca) • 7h ago

---

**[Predict the future of the shopping](https://www.reddit.com/r/artificial/comments/1vagsly/predict_the_future_of_the_shopping/)**

I always felt like someone who predicts the future knows something we don`t. Still, how accurately can one predict the future developmnets based on current trend/s? For example, initially shopping was done by going to a physical location. Then it got delivered to you. I guess the next step it will be done FOR YOU by using ai agents online based on you preference. And then, what is the next step?

3h ago

---

**[What Is Open-Weights A.I.? As Silicon Valley debates how artificial intelligence software should be created, “open weights” have been a major part of the discussions. Here’s what to know. (Gift Article)](https://www.reddit.com/r/artificial/comments/1vaedga/what_is_openweights_ai_as_silicon_valley_debates/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/07/28/technology/open-weight-ai.html?unlocked_article_code=1.1lA.xXO9.B-drqMFtl5zv&smid=url-share) • 5h ago

---

**[~1,400 years ago, scholars built a rigorous system to verify who you can trust. I rebuilt it as a trust layer for AI agents.](https://www.reddit.com/r/artificial/comments/1v9qdpe/1400_years_ago_scholars_built_a_rigorous_system/)**

I wrote this and just put it on arXiv, sharing for the discussion. When statements spread through long chains of people — some reliable, some not — you can't trust a claim just because it sounds right. Islamic scholars faced this centuries ago and built one of history's most rigorous systems for verifying transmitted knowledge: every claim carries its full chain of transmitters (isnād), every transmitter is graded on integrity and precision (rijāl), the chain is only as strong as its weakest link, independent chains raise confidence, and even a flawless chain doesn't excuse a flawed message. Now look at AI in 2026. An answer passes through a scraper, an extractor, several models, a synthesizer. Some links are reliable, some aren't — and when they fail, they fail silently. A confident, fluent answer that's quietly wrong. Everyone is racing to verify the agent: its identity, its permissions, its access. Almost no one is verifying the claim: whether what it said is true and independently corroborated. So I took that centuries-old methodology and rebuilt it as a trust layer for multi-agent AI. I call it ISNAD. Everyone verifies the agent; ISNAD verifies the claim. The rigor belongs to twelve centuries of scholars — the transfer to AI is mine. I also wrote the failures into the paper: some mechanisms are validated, others aren't yet, and I said so in detail. A trust framework that hides its weaknesses is a contradiction in terms. Paper: https://arxiv.org/abs/2607.24117 Code: https://github.com/alizahidraja/isnad Agree or disagree, I'd love to hear it.

21h ago

---

**[The World Model and Spatial Intelligence Era: Governing AI Beyond Language](https://www.reddit.com/r/artificial/comments/1va5tza/the_world_model_and_spatial_intelligence_era/)**

This brief highlights the emergence of world models and outlines a first-of-its-kind governance and policy agenda for the technology.

🔗 [hai.stanford.edu](https://hai.stanford.edu/policy/the-world-model-and-spatial-intelligence-era-governing-ai-beyond-language) • 10h ago

---

---

## Google News: "ai"

**[Accelerating scientific discovery with ChatGPT for Academic Researchers](https://openai.com/index/chatgpt-for-academic-researchers/)**

OpenAI is giving 100,000 academic researchers free access to ChatGPT's most advanced AI models to accelerate scientific research, collaboration, and discovery.

OpenAI • 1d ago

---

**[A.I. Companies Are Recruiting Electricians and Carpenters by the Thousands](https://www.nytimes.com/2026/07/29/business/economy/data-center-electricians-training.html)**

The New York Times • 21h ago

---

**[AI Tokenomics Explained: What Every Business Leader Needs To Know](https://www.forbes.com/sites/bernardmarr/2026/07/30/ai-tokenomics-explained-what-every-business-leader-needs-to-know/)**

AI tokens determine how generative AI systems process information, calculate usage and generate costs, making tokenomics essential for effective AI budgeting.

Forbes • 37m ago

---

**[Alexandr Wang: Startups Are Now in a 'Goliath Versus Goliath' Fight](https://www.businessinsider.com/alexandr-wang-startups-are-now-in-goliath-versus-goliath-fight-2026-7)**

He said that if a startup embraces AI agents in the "most ambitious ways," they can easily beat incumbent companies.

Business Insider • 52m ago

---

**[Massachusetts Senate Democrats warn on AI's costs but let data center moratorium fizzle](https://www.yahoo.com/news/politics/articles/massachusetts-senate-democrats-warn-ais-045700270.html)**

Data center resource demands could mean households would face higher utility bills, more pressure on water supplies.

Yahoo • 1h ago

---

**[The OpenAI lab leak was more extensive than we thought](https://www.cnn.com/2026/07/29/tech/openai-hugging-face-cyberattack)**

An OpenAI test that escaped its cage and alarmed the AI and cybersecurity industry attacked more than just Hugging Face, the AI platform that initially appeared to be the sole victim of the virtual lab leak.

CNN • 16h ago

---

**[OpenAI says its rogue AI tried to hack other companies](https://www.bbc.com/news/articles/c2el319vzr3o)**

The out-of-control AI found four logins which allowed it to access multiple unnamed online services.

BBC • 21h ago

---

**[EXCLUSIVE: Its AI agent spent days hacking a company, but sources say OpenAI did not notice for a week](https://www.reuters.com/business/its-ai-agent-spent-days-hacking-company-sources-say-openai-did-not-notice-week-2026-07-24/)**

Reuters • 5d ago

---

**[Leopold Aschenbrenner’s Situational Awareness seeks to raise capital after AI rout](https://www.ft.com/content/280336bf-dbed-405f-b38e-5af644a21549?syn-25a6b1a6=1)**

Hedge fund has held talks with existing investors and lenders in recent days

Financial Times • 2h ago

---

**[Elon Musk's xAI sues Minnesota over its first-in-the-nation law banning 'nudification' technology](https://apnews.com/article/minnesota-artificial-intelligence-nudification-x-elon-musk-deepfake-131184be939d540de093b567b12c9e16)**

Elon Musk’s company xAI is suing Minnesota over the state’s first-in-the-nation law that bans “nudification” technology on websites and apps.

apnews.com • 8h ago

---

---

## HackerNews: "ai"

**[AI companies are shredding rare books](https://news.ycombinator.com/item?id=49068738)**

🦔AI companies are bulk-buying rare books, scanning them through high-speed machines that cut the spines off, and shredding the originals. A service called ISBNdb facilitates orders of up to a million books and keeps buyers anonymous. Pre-2022 books are premium because they're

⬆️ 792 • 💬 510 • 2d ago • [X (formerly Twitter)](https://twitter.com/HedgieMarkets/status/2081534588485296565)

---

**[Document-borne AI worms can self-propagate through Copilot for Word](https://news.ycombinator.com/item?id=49096188)**

I would like to thank Microsoft product teams and Microsoft Security Response Center (MSRC) for collaborating with me on this technical analysis and mitigation of the disclosed vulnerabilities. The editorial opinions reflected below are solely the author’s and do not necessarily reflect those of the organizations I collaborated with.

⬆️ 359 • 💬 279 • 18h ago • [En Klype Salt](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)

---

**[AI's top startups are barely publishing their research](https://news.ycombinator.com/item?id=49103285)**

⬆️ 342 • 💬 185 • 8h ago • [science.org](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research)

---

**[AI companies spend record sums on Washington lobbying](https://news.ycombinator.com/item?id=49069939)**

Rising expenditure from OpenAI, Anthropic, Google and Microsoft reflects growing battle over federal policy

⬆️ 277 • 💬 144 • 2d ago • [ft.com](https://www.ft.com/content/d8a5f95e-3b6d-463a-a848-c9ef8e2394db)

---

**[LearnVector – Andrew Ng's AI company building one‑to‑one learning experiences](https://news.ycombinator.com/item?id=49092499)**

A new AI company from Andrew Ng, with a $100M investment from Coursera — building one-to-one learning that stays with you until you've mastered new skills.

⬆️ 258 • 💬 168 • 1d ago • [LearnVector](https://learnvector.ai/)

---

**[Apple Will 'Watch Everything Burn' When the AI Bubble Bursts](https://news.ycombinator.com/item?id=49070427)**

Memory prices have doubled, Macs and iPads have gone up, and iPhones are expected to follow. Ed Zitron – who writes the Where's Your Ed At newsletter, hosts the Better Offline podcast, and has been described by Politico as the AI boom's most "acerbic gadfly" – has spent years arguing the buildout driving those costs will never pay for itself. We asked him what happens to Apple if he's right. You've been calling AI a bubble since before it was fashionable.

⬆️ 253 • 💬 353 • 2d ago • [MacRumors](https://www.macrumors.com/2026/07/27/ed-zitron-apple-watch-it-burn-ai-bubble-bursts/)

---

**[Google's Beyond Zero: Enterprise Security for the AI Era](https://news.ycombinator.com/item?id=49081644)**

⬆️ 155 • 💬 79 • 1d ago • [spawn-queue.acm.org](https://spawn-queue.acm.org/doi/10.1145/3819083)

---

**[After the AI Crash](https://news.ycombinator.com/item?id=49096953)**

⬆️ 118 • 💬 204 • 17h ago • [potsandpansbyccg.com](https://potsandpansbyccg.com/2026/07/29/after-the-ai-crash/)

---

**[Show HN: Formally verified 3D CSG: Trust 93 lines spec, not 1000 lines AI code](https://news.ycombinator.com/item?id=49083239)**

Formally verified 3D mesh intersection - trust 93 lines of spec, not 1000+ lines of AI-written code - schildep/verified-3d-mesh-intersection

⬆️ 113 • 💬 48 • 1d ago • [GitHub](https://github.com/schildep/verified-3d-mesh-intersection)

---

**[Professor's invisible prompt trap catches 32/35 students cheating with AI](https://news.ycombinator.com/item?id=49074680)**

In an online discussion post, Alcorn State University history professor Dr. Jason Gibson posed a question that represented part of his students' midterm. It was about the...

⬆️ 105 • 💬 88 • 2d ago • [TechSpot](https://www.techspot.com/news/113243-professor-invisible-prompt-trap-catches-32-students-cheating.html)

---

---

## YouTube Videos: "ai"

**[AI Expert: They&#39;re Building Bunkers For A Reason - Tristan Harris](https://www.youtube.com/watch?v=xT3Pmw4f-Y8)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Tristan Harris, the former Google design ...

📺 Neural Nutshell

👁️ 105K • 👍 3K • 💬 962 • ⏱️ 15:01 • 13h ago

---

**[Musk, Zuckerberg and Altman clash over AI&#39;s future](https://www.youtube.com/watch?v=L3YmssZj4Wk)**

As OpenAI CEO Sam Altman heads to Washington to discuss AI policy with government officials, a debate rages over how the US ...

📺 CNN

👁️ 37K • 👍 431 • 💬 257 • ⏱️ 10:55 • 9h ago

---

**[The AI bubble just burst](https://www.youtube.com/watch?v=2DPA-AtFQQE)**

THE AI BUBBLE HAS BURST. It started in south korea and now it's happening in the US. Tech and AI stocks are CRASHING and ...

📺 Casey Simpson

👁️ 89K • 👍 6K • 💬 3K • ⏱️ 44:37 • 10h ago

---

**[AI Whistleblower: The World Will Change Horribly In The Next 12 Months](https://www.youtube.com/watch?v=VX0GU7gyIOU)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Daniel Kokotajlo, a former OpenAI ...

📺 Neural Nutshell

👁️ 103K • 👍 2K • 💬 754 • ⏱️ 15:25 • 2d ago

---

**[Betrayed after retirement, the AI Queen makes a sensational Silicon Valley comeback.](https://www.youtube.com/watch?v=g_ElSy7qM0Y)**

【Story Summary】 AI genius Aila sacrificed her career for her husband Ethan and suffered seven years of misery. Heartbroken ...

📺 Mango ShortDrama

👁️ 26K • 👍 612 • 💬 27 • ⏱️ 1:35:45 • 18h ago

---

**[Scott Galloway worries AI could make &#39;new species&#39; of men](https://www.youtube.com/watch?v=_EU-bYFBLTo)**

NYU professor Scott Galloway joins NewsNation's "The Future Is Now" to discuss his perspective on AI and why he believes there ...

📺 NewsNation

👁️ 3K • 👍 67 • 💬 17 • ⏱️ 5:20 • 1d ago

---

**[Ilya Sutskever Just Found Something New In AI](https://www.youtube.com/watch?v=eRQTfzuthDE)**

Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726 Subscribe To My Newsletter ...

📺 TheAIGRID

👁️ 20K • 👍 564 • 💬 77 • ⏱️ 10:15 • 18h ago

---

**[OpenAI Shocks The World With GENIE... Almost Unlimited AI Power](https://www.youtube.com/watch?v=vfSplCaxHzM)**

Sam Altman says OpenAI's ultimate AI could work like a genie that grants any wish. Meanwhile, its most powerful model is ...

📺 AI Revolution

👁️ 56K • 👍 2K • 💬 299 • ⏱️ 13:07 • 2d ago

---

**[Why everyone lies about AI](https://www.youtube.com/watch?v=x8lhQdbyYNg)**

Today's sponsor is Dad Brand hats. Get 25% off any purchase over $30 with code SHAPI25 or at this link: ...

📺 David Shapiro

👁️ 8K • 💬 66 • ⏱️ 36:41 • 18h ago

---

**[I Used Claude AI + Higgsfield to Build a $13,457/Mo Agency](https://www.youtube.com/watch?v=iOwKylW8c5Q)**

I built a fully automated AI ad agency in 24 hours — with 5 of YouTube's biggest AI experts handing me their exact playbooks.

📺 Higgsfield AI

👁️ 17K • 👍 909 • 💬 82 • ⏱️ 23:35 • 13h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 99,214 • ❤️ 8,742 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,694,935 • ❤️ 3,525 • 1d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 736,692 • ❤️ 963 • 22h ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 67,286 • ❤️ 831 • 2d ago

---

**[KAT-Coder-V2.5-Dev](https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev)**

*Kwaipilot*

KAT-Coder-V2.5-Dev is a 35B parameter Mixture-of-Experts (MoE) text-generation model specialized for agentic coding tasks, achieving State-of-the-Art performance on benchmarks like SWE-bench.

`text-generation` `34.7B`

⬇️ 6,275 • ❤️ 322 • 2d ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 18,933 • ❤️ 559 • 1d ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 4,804 • ❤️ 700 • 2d ago

---

**[Inflect-Micro-v2](https://huggingface.co/owensong/Inflect-Micro-v2)**

*Owen Song*

Inflect-Micro-v2 is a compact, fixed-voice English text-to-speech model (under 10M parameters) optimized for local, deterministic waveform synthesis. It supports long-text handling and runs efficiently on CPU or CUDA, making it suitable for edge AI applications.

`text-to-speech`

⬇️ 645 • ❤️ 293 • 4h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 1,267,198 • ❤️ 4,648 • 27d ago

---

**[Fara1.5-27B](https://huggingface.co/microsoft/Fara1.5-27B)**

*Microsoft*

Fara1.5-27B is a 27B multimodal computer use agent (CUA) that performs end-to-end web task completion using vision-only perception from screenshots and coordinate-grounded actions. It's designed for browser automation, with key capabilities including form filling, booking, and shopping, while prioritizing safety through critical-points pausing for irreversible actions.

`image-text-to-text` `27.4B`

⬇️ 1,543 • ❤️ 209 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 357 • 💬 6 • ⭐ 6,361 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 72 • 💬 6 • ⭐ 20,412 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 50 • 💬 4 • ⭐ 35,007 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 175 • 💬 10 • ⭐ 51,183 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model](https://huggingface.co/papers/2607.24904)**

*Senqiao Yang, Kaichen Zhang, Zhaoyang Jia et al. (23 authors)*

🏢 Microsoft

Standard vision-language models (VLMs) suffer from Moravec's paradox: they excel at complex offline visual reasoning but struggle with simple streaming perception tasks and process them inefficiently. We present Mage-VL, an efficient codec-native streaming foundation model for real-time multimodal understanding and interaction. At its core, our custom tokenizer, Mage-ViT, replaces uniform frame sampling by selectively encoding dynamic, entropy-rich regions using motion vectors and residual energy across sparse anchor (I) and predicted (P) frames. Operating at a 16 x 16 patch level, this reduces visual token consumption by over 75% while preserving spatiotemporal context. Trained from scratch on approximately 560M unlabeled images and 100M unlabeled video frames, Mage-ViT matches or outperforms flagship encoders trained on billions of image-text pairs. We establish AI4AI data pipelines encompassing prompt-code joint optimization for multimodal captioning and AI-driven performance diagnosis to guide training recipes. Furthermore, through a bio-inspired dual-system architecture - a lightweight System 1 event gate and a causal System 2 decoder - Mage-VL enables proactive streaming perception. Extensive evaluations show that Mage-VL-4B matches Qwen3-VL-4B on static tasks while achieving strong gains in video understanding and 2D/3D spatial reasoning, with up to a 3.5x wall-clock inference speedup, and comprehensively surpasses the 15B Phi-4-reasoning-vision baseline. Beyond model artifacts, we deliver seven key empirical findings covering pre-training data efficiency, variable-resolution scaling, codec system acceleration, VideoQA SFT redundancy, motion-spatial synergy, AI4AI data pipelines, and Zero-Vision SFT for multimodal RL.

▲ 25 • 💬 2 • ⭐ 922 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24904) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 37 • 💬 3 • ⭐ 15,874 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 76,198 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 117 • 💬 4 • ⭐ 94,976 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Native and Compact Structured Latents for 3D Generation](https://huggingface.co/papers/2512.14692)**

*Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu et al. (11 authors)*

🏢 Microsoft

A new sparse voxel representation called O-Voxel enables high-quality 3D generative modeling with efficient inference and robust topology handling.

▲ 6 • 💬 0 • ⭐ 9,362 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.14692) • [💻 code](https://github.com/microsoft/TRELLIS.2) • [🔗 project](https://microsoft.github.io/TRELLIS.2/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 82,537 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.3k • 🔱 1.1k • 2d ago

---

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

`Python`

⭐ 3.5k • 🔱 275 • 3d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.9k • 🔱 404 • 12h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 2.8k • 🔱 237 • 1d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.6k • 🔱 313 • 21d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 2.4k • 🔱 278 • 3d ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.8k • 🔱 206 • 2d ago

---

**[MIgHTy-alIeN/MEV-Arbitrage-Bot](https://github.com/MIgHTy-alIeN/MEV-Arbitrage-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 1.8k • 🔱 1.2k • 38s ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.6k • 🔱 119 • 8d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs — six tuned states, two sizes, auto dark/light

`TypeScript`

⭐ 1.2k • 🔱 95 • 8d ago

---

---

*Generated by PeekDeck - A glance is all you need*
