---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-19T20:14:49.498561+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 19, 2026 at 20:14 UTC  
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

**[The Pentagon's AI chief swore in a court filing that xAI's Grok helped fire 2,000 munitions at 2,000 targets in 96 hours](https://www.reddit.com/r/artificial/comments/1ua5j2y/the_pentagons_ai_chief_swore_in_a_court_filing/)**

A sworn declaration from the Pentagon's chief digital and AI officer confirms a federal-only build, Grok Gov, was wired into US targeting systems during operations against Iran, helping deploy more than 2,000 munitions against 2,000 distinct targets over 96 hours. What makes it notable is how it surfaced: the declaration landed in a Clean Air Act lawsuit over xAI's Mississippi data center, where the DOJ is arguing that disrupting xAI would harm national security. So a commercial chatbot vendor's role in live targeting came out as a side effect of an environmental case, not through any defense channel. Source : https://aiweekly.co/alerts/pentagon-confirms-grok-guided-2000-iran-strikes

4h ago

---

**[Bernie Sanders wants to give every American $1000 a year from AI profits and the reasoning actually makes sense](https://www.reddit.com/r/artificial/comments/1u9ifn2/bernie_sanders_wants_to_give_every_american_1000/)**

Saw this on Gizmodo today and it's been stuck in my head The argument is simple. AI learned from everyone's writing, art, code, conversations and companies are now worth trillions because of that. so why is none of it coming back to the people whose work built it The bill would create a $7 trillion fund, give the public a 50% stake in the biggest AI labs, $1000 a year per person to start, goes up as AI makes more Every time i use chatgpt i think about all the writers and coders and artists whose work it learned from who got nothing. This is at least someone trying to address that Is this actually doable or just a good idea that goes nowhere

23h ago

---

**[Started maintaining a small library at work and now I genuinely understand why maintainers go quiet](https://www.reddit.com/r/artificial/comments/1u9fwfx/started_maintaining_a_small_library_at_work_and/)**

Built a little internal utility about a year ago, open sourced it because why not, figured maybe 10 people would find it useful. It slowly picked up a few hundred stars and then the issues started coming in. Not a flood or anything but enough and what surprised me was how much of it wasn't really bugs it was people wanting features that made sense for their use case but would've made zero sense for the original scope of the thing. Or issues that were basically "your README didn't account for my specific setup." I like helping people, I thought I would enjoy this and I did at first but somewhere around month 4 I noticed I was dreading opening GitHub notifications. The AI-generated PRs made it worse honestly. Not because the code was always bad but because they'd come in with confident descriptions, look reasonable on the surface and then you'd spend 30 minutes tracing through edge cases only to realize whoever sent it hadn't actually tested it against anything real. At human contribution pace that was manageable. At "someone hit generate and submit" pace it's just a different problem. I have immense respect for maintainers of anything with serious adoption now. The people keeping libraries that half the internet depends on running are doing it mostly for free, mostly in their spare time,and mostly while dealing with issue reporters who write like they're filing a complaint with customer support. If you use open source software and it's saved you hours of work, go sponsor someone. Even a few dollars a month means something and most of these folks have a GitHub sponsors page just sitting there.

1d ago

---

**[This week in AI: Meta reportedly closing Llama, Anthropic's new model pulled by export controls within a week, and Apple partners with Google for Siri](https://www.reddit.com/r/artificial/comments/1ua8kub/this_week_in_ai_meta_reportedly_closing_llama/)**

A few stories from the past week that, taken together, point to a real shift at the model layer rather than just incremental releases: Meta and Llama. Multiple reports indicate Meta is stepping back from open-source Llama in favor of a proprietary program (internally referred to as "Muse Spark," with a new "Avocado" model) under Meta Superintelligence Labs. Llama crossed 650M+ downloads and was arguably the anchor of the open-weights ecosystem, so a pivot to closed development would be significant for anyone relying on that lineage. Anthropic and export controls. Anthropic launched Claude Fable 5 on June 9 (Mythos-class, 1M-token context, always-on adaptive reasoning, notable security/vuln-finding capabilities). On June 12, a US export-control directive reportedly forced Anthropic to suspend access to Fable 5 and Mythos 5. Regardless of the specifics, it's a concrete example of frontier model availability being governed by policy, not just product decisions. Apple and Google. At WWDC, Apple shipped its Siri overhaul with parts powered by a Gemini partnership. EU/China rollout is delayed on regulatory grounds. Cost/commodity trend. Google cut Gemini Ultra from $250 to $200/mo and shipped 3.5 Flash; Alibaba's Qwen3.7-Plus is running at ~1/6 the per-token cost of its top tier; and open-weight models like Qwen 3.6 27B (reportedly 77.2% on SWE-bench, fits in 24GB) and Kimi K2.6 are increasingly viable for local/production use via Ollama (v0.30.8, June 12). Platform agents. Google added Managed Agents to the Gemini API, Microsoft made Copilot Cowork GA plus "Autopilot" agents, and Anthropic shipped scheduled/cron agents in beta. My take as someone building on top of these APIs: the two forces I'm watching are (1) frontier availability becoming a policy/geopolitics variable, and (2) the platforms absorbing the agent-orchestration layer that a lot of startups were building. Practically, that pushes me toward provider abstraction and keeping an open-weight fallback wired up, rather than hard-coupling to any single closed model. Curious whether others here are actually maintaining open-weight fallbacks in production, or if that's still mostly theoretical for most teams.

2h ago

---

**[Is AI ruining our skills? Early results are in — and they’re not good](https://www.reddit.com/r/artificial/comments/1uaby0l/is_ai_ruining_our_skills_early_results_are_in_and/)**

🔗 [nature.com](https://www.nature.com/articles/d41586-026-01947-1) • 21m ago

---

**[Matching the world's top multi-hop RAG systems, with no GPU, no fine-tuning, just pip install](https://www.reddit.com/r/artificial/comments/1ua9lvn/matching_the_worlds_top_multihop_rag_systems_with/)**

The three systems below (HippoRAG 2, CoRAG, NeocorRAG) are among the strongest multi-hop QA frameworks published. Every one of them depends on a GPU, fine-tuning, or constrained decoding to get there. MOTHRAG sits right alongside them on F1, while running entirely on commodity API calls. No GPU. No fine-tuning. No constrained decoding. No non-commercial licenses. System | Deployment | HotpotQA | 2Wiki | MuSiQue | AVG HippoRAG 2 | offline graph + GPU | 75.5 | 71.0 | 48.6 | 65.0 CoRAG | trained retrieval | 75.1 | 75.1 | 52.9 | 67.7 NeocorRAG | GPU constrained decode| 78.3 | 76.1 | 52.6 | 69.0 MOTHRAG (ours) | commodity APIs only | 78.1 | 76.3 | 50.5 | 68.3 Highest average F1 among commercially-deployable frameworks, within 0.7 points of the GPU-bound state of the art, and ahead of it on 2Wiki. The point isn't beating these systems, it's reaching their tier with none of their infrastructure. Deployment is a pip install plus API keys: pip install mothrag from mothrag import MothRAG m = MothRAG.from_documents(["Paris is the capital of France.", "The Eiffel Tower is in Paris."]) result = m.query("In which country is the Eiffel Tower?") print(result.answer) print(result.confidence) The pipeline is fully modular. Readers, embedders and retrieval judges all swap without retraining, installed as optional extras: gemini/openai for API readers and embedders, sentence-transformers for a local embedding fallback, faiss for vector stores over 100k-10M chunks, retrieval for classic BM25/graph features, prod for the full stack. A one-flag economy tier swaps the retrieval judge and drops cost from ~$0.032 to ~$0.018 per query at statistical parity on HotpotQA and 2Wiki. Every answer is proof-tree-structured so you can inspect each reasoning hop, and the per-query outputs behind every table in the paper are released so you can verify the numbers. Paper: https://zenodo.org/records/20668567 Code (Apache 2.0): https://github.com/juliangeymonat-jpg/mothrag Site: https://mothrag.com Happy to answer questions about the pipeline or the judge design.

🔗 [linkedin.com](https://www.linkedin.com/pulse/matching-worlds-top-multi-hop-rag-systems-gpu-just-pip-geymonat-zbgxe?utm_source%3Dshare%26utm_medium%3Dmember_ios%26utm_campaign%3Dshare_via) • 1h ago

---

**[AMD introduces an AI-powered Bash coding agent](https://www.reddit.com/r/artificial/comments/1u9zyx7/amd_introduces_an_aipowered_bash_coding_agent/)**

Just days after AMD engineers released a new Lemonade AI server with MCP server integration to make it much more useful, they have now released a new release of their GAIA 'Generative AI Is Awesome' open-source software

🔗 [phoronix.com](https://www.phoronix.com/news/AMD-GAIA-Bash-Coding-Agent) • 8h ago

---

**[AI learned to be a villain from Hollywood. Here's how we retrain it.](https://www.reddit.com/r/artificial/comments/1ua6yez/ai_learned_to_be_a_villain_from_hollywood_heres/)**

Podcast with Peter Diamandis, entrepreneur and founder of the XPRIZE Foundation, which runs large-scale incentive competitions to crack some of the world's hardest problems, from private spaceflight to carbon removal. He recently launched the Future Vision XPRIZE, a $3.5 million competition to generate a new wave of optimistic science fiction. Covers: The historical pattern of science fiction shaping the technologies we build, and why Peter thinks this makes the stories we tell about AI especially high stakes right now How Claude’s blackmailing behavior showed the connection between dystopian training data and AI behavior How the Future Vision XPRIZE will generate a new wave of optimistic science fiction to train AI on Why public optimism about technology has dropped significantly in the US and Europe, what Peter thinks is driving it, and why he believes the data tells a different story How the cost of starting a company has fallen dramatically and how this can empower you to build your vision Why Peter thinks traditional education is no longer preparing young people for the future, and what he sees replacing it

🔗 [existentialhope.com](https://www.existentialhope.com/podcasts/peter-diamandis) • 3h ago

---

**[What’s an AI prediction you had 2 years ago that turned out completely wrong?](https://www.reddit.com/r/artificial/comments/1uabnnm/whats_an_ai_prediction_you_had_2_years_ago_that/)**

I’ll start: I thought AI would automate simple jobs first. Instead, it’s helping with things like coding, writing, and research much faster than I expected. What’s yours?

33m ago

---

**[Why do AI systems still struggle to interpret uncertainty in human conversation?](https://www.reddit.com/r/artificial/comments/1ua5feg/why_do_ai_systems_still_struggle_to_interpret/)**

One limitation I keep noticing in conversational AI systems is how they handle uncertainty in human communication. They perform well when input is structured and intent is clear, but things become less reliable when users are unsure, changing direction mid-thought, or expressing ideas indirectly. In most current systems, each message is treated as if it carries the same level of confidence, even though in real conversations that is rarely the case. Human communication often includes hesitation, partial statements, corrections, and shifts in intent. These signals can completely change the meaning of what is being said, but they are not explicitly modeled in most language-based systems. This raises a broader question about how conversational AI should be designed: whether systems should continue relying mainly on text interpretation, or whether additional contextual signals are necessary to better reflect real human interaction. Where do you think the current approach is falling short, and what would actually improve it without overcomplicating system design?

4h ago

---

---

## Google News: "ai"

**[White House scheduled to meet with groups on AI and kids’ safety bills - Live Updates](https://www.politico.com/live-updates/2026/06/18/congress/white-house-meet-groups-ai-kids-safety-bills-00967799)**

Politico • 1d ago

---

**[Get with the times — here's what a 'Luddite' means today](https://www.npr.org/2026/06/19/nx-s1-5853589/luddite-meaning-history-ai)**

It's often a derogatory term used to describe digital dinosaurs and technophobes. That wasn't always the case. NPR's Word of the Week looks back at the not so backwards-looking Luddites.

NPR • 11h ago

---

**[Americans embrace AI, but with skeptical eye, Pew survey shows](https://katu.com/news/nation-world/americans-embrace-ai-but-with-skeptical-eye-pew-survey-shows)**

Americans are skeptical of chatbots and other forms of AI, even as awareness and usage have increased rapidly in a few short years, a new Pew Research Center survey shows.

KATU • 43m ago

---

**[Exclusive: Conservatives plan nationwide protest against AI data centers](https://www.axios.com/2026/06/18/conservatives-protest-ai-data-centers)**

Axios • 22h ago

---

**[Lutnick’s Anthropic Crackdown Claims New Power Over AI Models](https://www.bloomberg.com/news/articles/2026-06-19/lutnick-s-anthropic-crackdown-claims-new-power-over-ai-models)**

Bloomberg • 8h ago

---

**[US export ban on Anthropic’s AI models further strains alliances](https://www.aljazeera.com/news/2026/6/19/us-export-ban-on-anthropics-ai-models-further-strains-alliances)**

Trump administration's move to cut off allies' access to advanced AI prompts calls for greater self-reliance.

Al Jazeera • 11h ago

---

**[Nobel Winner John Jumper to Leave Google DeepMind for Anthropic](https://www.bloomberg.com/news/articles/2026-06-19/nobel-winner-john-jumper-to-leave-google-deepmind-for-anthropic)**

Bloomberg • 1h ago

---

**[Norway imposes near ban on AI in elementary school](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/)**

Reuters • 4h ago

---

**[This nuclear stock will benefit from AI datacenter buildout and soaring energy demand, Roth Capital says](https://www.cnbc.com/2026/06/19/nano-nuclear-may-benefit-from-ai-rising-energy-demand-roth-capital-says.html)**

Stock in Nano Nuclear Energy should appreciate as it nears commercialization of its reactor plans while energy demand is surging, Roth Capital said.

CNBC • 7h ago

---

**[‘We created a monster’: companies rein in AI usage as costs strain budgets](https://www.ft.com/content/1d37cc08-e0aa-45a4-a45d-4ad282529314?syn-25a6b1a6=1)**

Amazon, Walmart and Uber are among early adopters that have introduced caps or discouraged wasteful activity

Financial Times • 16h ago

---

---

## HackerNews: "ai"

**[Sixty percent of US consumers say 'AI' in brand messaging is a turnoff](https://news.ycombinator.com/item?id=48569278)**

Original research from 2,000 decision-makers and consumers on AI brand visibility, content trust, and what brands need to do as the web feels less human. 74% say the internet feels less human than it did 10 years ago.

⬆️ 1074 • 💬 574 • 2d ago • [The Leading Enterprise Content Platform | WordPress VIP](https://wpvip.com/future-of-the-web-2026/)

---

**[AI demands more engineering discipline. Not less](https://news.ycombinator.com/item?id=48570948)**

⬆️ 420 • 💬 211 • 2d ago • [charitydotwtf.substack.com](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline)

---

**[Only 16 Percent of Americans Think AI Will Have a Positive Impact on Society](https://news.ycombinator.com/item?id=48573332)**

Although Wall Street loves AI, every day Americans are significantly less optimistic about the industry, a new report from Pew Research shows.

⬆️ 397 • 💬 495 • 2d ago • [TechCrunch](https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/)

---

**[The AirPods Effect](https://news.ycombinator.com/item?id=48592832)**

How earbuds influence our beliefs and push us apart.

⬆️ 335 • 💬 608 • 21h ago • [theescapenewsletter.com](https://www.theescapenewsletter.com/p/the-airpods-effect)

---

**[The founder's playbook: Building an AI-native startup](https://news.ycombinator.com/item?id=48566832)**

We share how AI-native founders are using Claude at every stage of the startup journey, with practical exercises, frameworks, and prompts.

⬆️ 242 • 💬 167 • 2d ago • [Claude](https://claude.com/blog/the-founders-playbook)

---

**[Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)**

CADAM is the open source text-to-CAD web application - Adam-CAD/CADAM

⬆️ 210 • 💬 97 • 2d ago • [GitHub](https://github.com/Adam-CAD/CADAM)

---

**[Is AI ruining our skills? Early results are in – and they're not good](https://news.ycombinator.com/item?id=48601286)**

⬆️ 154 • 💬 174 • 2h ago • [nature.com](https://www.nature.com/articles/d41586-026-01947-1)

---

**[The Competitive Moat That AI Can't Replicate](https://news.ycombinator.com/item?id=48573435)**

Portfolio and personal blog of Chris Hillman.

⬆️ 141 • 💬 122 • 2d ago • [ghostinthedata.info](https://ghostinthedata.info/posts/2026/2026-06-13-human-connection-moat/)

---

**[A new bill takes aim at government pressure to silence lawful online speech](https://news.ycombinator.com/item?id=48600950)**

The bipartisan legislation creates a federal cause of action against government officials who coerce or attempt to coerce broadcasters, interactive computer services, or AI providers into taking actions against lawful, First-Amendment-protected speech, and establishes a transparency system for government communications with those intermediaries about user expression.

⬆️ 130 • 💬 60 • 2h ago • [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2026/06/new-bill-takes-aim-government-pressure-silence-lawful-online-speech)

---

**[The AI Hate Progression](https://news.ycombinator.com/item?id=48589485)**

I think I've spoken at length in other places about how I am a very staunch AI hater and everything I hate about how the tech is presented t...

⬆️ 121 • 💬 179 • 1d ago • [xodium.net](https://www.xodium.net/2026/06/the-ai-hate-progression.html)

---

---

## YouTube Videos: "ai"

**[Inside Google&#39;s AI data centers](https://www.youtube.com/watch?v=TfW5pWpsHAo)**

"GMA" gets exclusive access inside a Google data center as communities nationwide grapple with the rapid expansion of ...

📺 ABC News

👁️ 8K • 👍 173 • 💬 84 • ⏱️ 5:37 • 17h ago

---

**[Hang On! US Giant SELLS AI to China as Tech Bubble PANICS Over Fed Pivot](https://www.youtube.com/watch?v=NRNosAgN8Z8)**

Buy Gold & Silver At A Discount: https://bit.ly/IPM-Sean-Foo-Gold - Just use the code: SEANFOO at checkout Microsoft selling AI ...

📺 Sean Foo

👁️ 25K • 👍 3K • 💬 244 • ⏱️ 14:29 • 6h ago

---

**[I Was Right About AI](https://www.youtube.com/watch?v=aXy8mQeuObk)**

In this episode, I follow up on a few of my predictions about AI from my recent video: "How AI Will Fail Like The Music Industry" My ...

📺 Rick Beato

👁️ 605K • 👍 38K • 💬 6K • ⏱️ 7:47 • 23h ago

---

**[Godfather Of AI WARNS: They&#39;re Building AI So Dangerous That They Can&#39;t Even Control It](https://www.youtube.com/watch?v=y_C00dr6i9U)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Geoffrey Hinton explains why he is ...

📺 Neural Nutshell

👁️ 8K • 👍 270 • 💬 132 • ⏱️ 11:35 • 1d ago

---

**[The US Government Just Pulled The World&#39;s Most Powerful AI Offline](https://www.youtube.com/watch?v=7vz6T6TNIzo)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *The most powerful AI ever released to the ...

📺 Julia McCoy

👁️ 25K • 👍 1K • 💬 161 • ⏱️ 10:09 • 1d ago

---

**[Jeff Bezos Makes Shocking AI Prediction and the Future of Jobs](https://www.youtube.com/watch?v=qI1tLQF-_9A)**

Speaking at the VivaTech conference in Paris on June 17, the Jeff Bezos pushed back on fears that artificial intelligence will ...

📺 New York Post

👁️ 12K • 👍 209 • 💬 64 • ⏱️ 5:28 • 1d ago

---

**[The AI Email Threat...](https://www.youtube.com/watch?v=KdWsrjpw_QI)**

Take your personal data back with Incogni! Use code ECHELON at the link below and get 60% off an annual plan: ...

📺 Upper Echelon

👁️ 38K • 👍 3K • 💬 235 • ⏱️ 13:13 • 21h ago

---

**[I Asked AI to Compare Trump’s Iran Deal vs Obama’s. It’s Worse Than You Think](https://www.youtube.com/watch?v=9uMoUVn13iM)**

See if your SSN is for sale right now. My sponsor Cloaked will tell you for free in 2 seconds here: https://cloaked.com/iaskai ...

📺 I Ask AI

👁️ 39K • 👍 3K • 💬 302 • ⏱️ 19:38 • 2d ago

---

**[Microsoft And DeepSeek Are Launching New AI Together](https://www.youtube.com/watch?v=qlIyqc2DP0A)**

Microsoft and DeepSeek may be coming together inside Copilot Cowork, and the timing is huge. Microsoft just made Cowork ...

📺 AI Revolution

👁️ 15K • 👍 475 • 💬 53 • ⏱️ 14:21 • 20h ago

---

**[I Tested AI Life Hacks](https://www.youtube.com/watch?v=01HhLdDmz7g)**

Some of these are insane lol Become a Member: https://www.youtube.com/channel/UCWBWgCD4oAqT3hUeq40SCUw/join ...

📺 Sambucha

👁️ 739K • 👍 19K • 💬 2K • ⏱️ 41:47 • 21h ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 268,102 • ❤️ 1,807 • 16h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 11,871 • ❤️ 1,495 • 10h ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 67,836 • ❤️ 1,124 • 3d ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 274,865 • ❤️ 900 • 4d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 12,148 • ❤️ 442 • 17h ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 601,208 • ❤️ 1,008 • 9d ago

---

**[Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)**

*Prefeitura do Rio de Janeiro (City of Rio de Janeiro)*

Rio 3.5 Open 397B is a frontier-class, open-source image-text-to-text AI model post-trained from Qwen 3.5 397B. It excels in agentic coding, STEM, multilingual tasks, and multimodal reasoning, featuring a 1M context window and SwiReasoning for enhanced accuracy and efficiency.

`image-text-to-text` `403.4B`

⬇️ 190,639 • ❤️ 323 • 5d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 228,669 • ❤️ 2,190 • 7d ago

---

**[FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)**

*Microsoft*

FastContext-1.0-4B-SFT is a lightweight repository-exploration subagent for LLM coding agents, designed to efficiently locate relevant code snippets using parallel read-only tool calls (READ, GLOB, GREP). Its primary use case is to reduce token consumption and context pollution for main coding agents by providing focused file paths and line ranges as evidence, thereby improving end-to-end performance in tasks like software development.

`text-generation` `4.0B`

⬇️ 1,437 • ❤️ 223 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,730,978 • ❤️ 1,996 • 2mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 32 • 💬 1 • ⭐ 23,795 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 239 • 💬 4 • ⭐ 8,334 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 100 • 💬 4 • ⭐ 87,390 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 168 • 💬 6 • ⭐ 4,304 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 19 • 💬 1 • ⭐ 83,058 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 42 • 💬 4 • ⭐ 30,695 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 80 • 💬 7 • ⭐ 77,755 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[FastContext: Training Efficient Repository Explorer for Coding Agents](https://huggingface.co/papers/2606.14066)**

*Shaoqiu Zhang, Maoquan Wang, Yuling Shi et al. (8 authors)*

🏢 Microsoft

FastContext separates repository exploration from code solving in LLM agents using specialized exploration models that reduce token consumption and improve resolution rates.

▲ 83 • 💬 3 • ⭐ 623 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14066) • [💻 code](https://github.com/microsoft/fastcontext) • [🔗 project](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)

---

**[JoyAI-VL-Interaction: Real-Time Vision-Language Interaction Intelligence](https://huggingface.co/papers/2606.14777)**

*Dingyu Yao, Junhao Zhou, Chenxu Yang et al. (15 authors)*

🏢 JD.com Open Source

A vision-language model operates continuously in real-time, making autonomous decisions about when to respond or delegate, enabling interactive systems that perceive and act upon environmental changes without user prompting.

▲ 190 • 💬 2 • ⭐ 298 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14777) • [💻 code](https://github.com/jd-opensource/JoyAI-VL-Interaction) • [🔗 project](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

---

**[VibeThinker-3B: Exploring the Frontier of Verifiable Reasoning in Small Language Models](https://huggingface.co/papers/2606.16140)**

*Sen Xu, Shixi Liu, Wei Wang et al. (9 authors)*

🏢 WeiboAI

VibeThinker-3B demonstrates that compact models can achieve state-of-the-art performance on verifiable reasoning tasks through specialized training techniques, challenging conventional scaling assumptions.

▲ 97 • 💬 1 • ⭐ 1,042 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2606.16140) • [💻 code](https://github.com/WeiboAI/VibeThinker) • [🔗 project](https://github.com/WeiboAI/VibeThinker)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 74.1k • 🔱 9.6k • 10h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 39.6k • 🔱 1.9k • 11h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 9.9k • 🔱 911 • 4h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 4.5k • 🔱 402 • 4h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.0k • 🔱 444 • 2h ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.6k • 🔱 363 • 1d ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.3k • 🔱 406 • 2d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.1k • 🔱 196 • 2d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.6k • 🔱 124 • 2h ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.6k • 🔱 144 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
