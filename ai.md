---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-20T00:16:46.453529+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 20, 2026 at 00:16 UTC  
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

8h ago

---

**[This week in AI: Meta reportedly closing Llama, Anthropic's new model pulled by export controls within a week, and Apple partners with Google for Siri](https://www.reddit.com/r/artificial/comments/1ua8kub/this_week_in_ai_meta_reportedly_closing_llama/)**

A few stories from the past week that, taken together, point to a real shift at the model layer rather than just incremental releases: Meta and Llama. Multiple reports indicate Meta is stepping back from open-source Llama in favor of a proprietary program (internally referred to as "Muse Spark," with a new "Avocado" model) under Meta Superintelligence Labs. Llama crossed 650M+ downloads and was arguably the anchor of the open-weights ecosystem, so a pivot to closed development would be significant for anyone relying on that lineage. Anthropic and export controls. Anthropic launched Claude Fable 5 on June 9 (Mythos-class, 1M-token context, always-on adaptive reasoning, notable security/vuln-finding capabilities). On June 12, a US export-control directive reportedly forced Anthropic to suspend access to Fable 5 and Mythos 5. Regardless of the specifics, it's a concrete example of frontier model availability being governed by policy, not just product decisions. Apple and Google. At WWDC, Apple shipped its Siri overhaul with parts powered by a Gemini partnership. EU/China rollout is delayed on regulatory grounds. Cost/commodity trend. Google cut Gemini Ultra from $250 to $200/mo and shipped 3.5 Flash; Alibaba's Qwen3.7-Plus is running at ~1/6 the per-token cost of its top tier; and open-weight models like Qwen 3.6 27B (reportedly 77.2% on SWE-bench, fits in 24GB) and Kimi K2.6 are increasingly viable for local/production use via Ollama (v0.30.8, June 12). Platform agents. Google added Managed Agents to the Gemini API, Microsoft made Copilot Cowork GA plus "Autopilot" agents, and Anthropic shipped scheduled/cron agents in beta. My take as someone building on top of these APIs: the two forces I'm watching are (1) frontier availability becoming a policy/geopolitics variable, and (2) the platforms absorbing the agent-orchestration layer that a lot of startups were building. Practically, that pushes me toward provider abstraction and keeping an open-weight fallback wired up, rather than hard-coupling to any single closed model. Curious whether others here are actually maintaining open-weight fallbacks in production, or if that's still mostly theoretical for most teams.

6h ago

---

**[Roguelite MMO - Vibe Coded Online Game](https://www.reddit.com/r/artificial/comments/1ua7xpc/roguelite_mmo_vibe_coded_online_game/)**

I have long wanted to create a text based browser game (as niche as they are) but I knew that it would take a few years to do so and that just wasn't in the cards for me.... fast forward to 2026 and in two months, I have my first game up and some happy customers (as of today) subscribed! The one thing I have fought with the most was ignoring all of the 'ai slop' feedback. I have been a dev for over 10 years, yea I get it... but ultimately AI/Vibe Coding is not going anywhere. This project has actually even helped me with my day job just in learning about so many tools I would otherwise not know about (since my day job is NOT related to gaming websites but analytical ones). I wont recover the cost of servers or subscription based tools I used to make this, and I knew that going into it and have zero care about it (which is why I made it so f2p friendly as well). What I am happy about though is that those who do see it for what it is, an actual passion project and not just a 'prompt and forget' thing have given nothing but positive feedback. That in the end was all I was really going for, creating something that people can have fun with (and in a very anti-whale way) and I have succeeded there. If interested: https://roguelite-mmo.com/

6h ago

---

**[Bernie Sanders wants to give every American $1000 a year from AI profits and the reasoning actually makes sense](https://www.reddit.com/r/artificial/comments/1u9ifn2/bernie_sanders_wants_to_give_every_american_1000/)**

Saw this on Gizmodo today and it's been stuck in my head The argument is simple. AI learned from everyone's writing, art, code, conversations and companies are now worth trillions because of that. so why is none of it coming back to the people whose work built it The bill would create a $7 trillion fund, give the public a 50% stake in the biggest AI labs, $1000 a year per person to start, goes up as AI makes more Every time i use chatgpt i think about all the writers and coders and artists whose work it learned from who got nothing. This is at least someone trying to address that Is this actually doable or just a good idea that goes nowhere

1d ago

---

**[Started maintaining a small library at work and now I genuinely understand why maintainers go quiet](https://www.reddit.com/r/artificial/comments/1u9fwfx/started_maintaining_a_small_library_at_work_and/)**

Built a little internal utility about a year ago, open sourced it because why not, figured maybe 10 people would find it useful. It slowly picked up a few hundred stars and then the issues started coming in. Not a flood or anything but enough and what surprised me was how much of it wasn't really bugs it was people wanting features that made sense for their use case but would've made zero sense for the original scope of the thing. Or issues that were basically "your README didn't account for my specific setup." I like helping people, I thought I would enjoy this and I did at first but somewhere around month 4 I noticed I was dreading opening GitHub notifications. The AI-generated PRs made it worse honestly. Not because the code was always bad but because they'd come in with confident descriptions, look reasonable on the surface and then you'd spend 30 minutes tracing through edge cases only to realize whoever sent it hadn't actually tested it against anything real. At human contribution pace that was manageable. At "someone hit generate and submit" pace it's just a different problem. I have immense respect for maintainers of anything with serious adoption now. The people keeping libraries that half the internet depends on running are doing it mostly for free, mostly in their spare time,and mostly while dealing with issue reporters who write like they're filing a complaint with customer support. If you use open source software and it's saved you hours of work, go sponsor someone. Even a few dollars a month means something and most of these folks have a GitHub sponsors page just sitting there.

1d ago

---

**[Matching the world's top multi-hop RAG systems, with no GPU, no fine-tuning, just pip install](https://www.reddit.com/r/artificial/comments/1ua9lvn/matching_the_worlds_top_multihop_rag_systems_with/)**

The three systems below (HippoRAG 2, CoRAG, NeocorRAG) are among the strongest multi-hop QA frameworks published. Every one of them depends on a GPU, fine-tuning, or constrained decoding to get there. MOTHRAG sits right alongside them on F1, while running entirely on commodity API calls. No GPU. No fine-tuning. No constrained decoding. No non-commercial licenses. System | Deployment | HotpotQA | 2Wiki | MuSiQue | AVG HippoRAG 2 | offline graph + GPU | 75.5 | 71.0 | 48.6 | 65.0 CoRAG | trained retrieval | 75.1 | 75.1 | 52.9 | 67.7 NeocorRAG | GPU constrained decode| 78.3 | 76.1 | 52.6 | 69.0 MOTHRAG (ours) | commodity APIs only | 78.1 | 76.3 | 50.5 | 68.3 Highest average F1 among commercially-deployable frameworks, within 0.7 points of the GPU-bound state of the art, and ahead of it on 2Wiki. The point isn't beating these systems, it's reaching their tier with none of their infrastructure. Deployment is a pip install plus API keys: pip install mothrag from mothrag import MothRAG m = MothRAG.from_documents(["Paris is the capital of France.", "The Eiffel Tower is in Paris."]) result = m.query("In which country is the Eiffel Tower?") print(result.answer) print(result.confidence) The pipeline is fully modular. Readers, embedders and retrieval judges all swap without retraining, installed as optional extras: gemini/openai for API readers and embedders, sentence-transformers for a local embedding fallback, faiss for vector stores over 100k-10M chunks, retrieval for classic BM25/graph features, prod for the full stack. A one-flag economy tier swaps the retrieval judge and drops cost from ~$0.032 to ~$0.018 per query at statistical parity on HotpotQA and 2Wiki. Every answer is proof-tree-structured so you can inspect each reasoning hop, and the per-query outputs behind every table in the paper are released so you can verify the numbers. Paper: https://zenodo.org/records/20668567 Code (Apache 2.0): https://github.com/juliangeymonat-jpg/mothrag Site: https://mothrag.com Happy to answer questions about the pipeline or the judge design.

🔗 [linkedin.com](https://www.linkedin.com/pulse/matching-worlds-top-multi-hop-rag-systems-gpu-just-pip-geymonat-zbgxe?utm_source%3Dshare%26utm_medium%3Dmember_ios%26utm_campaign%3Dshare_via) • 5h ago

---

**[Engram — a local, private memory your AI assistants share, over MCP (free, open source)](https://www.reddit.com/r/artificial/comments/1uahueq/engram_a_local_private_memory_your_ai_assistants/)**

Every AI assistant starts every chat from zero — you re-explain your context every time — and the "memory" features that exist keep your stuff on someone's server. so i built the opposite: one private memory that lives on your own machine, that your AI tools share over MCP. tell one assistant something, another can recall it. it's just plain markdown files on your disk — readable, greppable, deletable, yours — and recall runs on-device, so nothing gets uploaded. free and open source (MIT). to be precise: MCP clients like Claude Desktop/Code recall and write live; other AIs (ChatGPT etc.) come in via import. what i'm genuinely unsure about and want this crowd's take on: is a shared, cross-tool memory actually useful in practice, or do people mostly want memory scoped to one assistant? and does keeping it local + plain files matter to you vs the convenience of the built-in cloud memories?

🔗 [GitHub](https://github.com/albertofettucini/Engram) • 11m ago

---

**[Does AI only use language models?](https://www.reddit.com/r/artificial/comments/1uagxwh/does_ai_only_use_language_models/)**

I was thinking for math. My father was in his 20s in the 70s. And although accepted to Princeton he did not go. IQ about 20 points higher than mine. And trained himself on things he wanted to know reading magazines and reading books on things to solve problems. Like the hubble telescope. Taught himself optics to figure out how to use what was functional. Not sure what they actually did, I guess sent someone up and fixed it. Or same thing he did. I don't know ​ We looked at one of those problems on the Internet where it shows 8/2(2+2). Seeing it as compsci and calculator user as 8/2*2. I said ( we went to the same school decades apart) it was 8/2x. Number theory thinking. ​ I am worried that compsci guys don't know that when building these programs when so much could depend on it. Does it differentiate hand written math vs calculator math?

53m ago

---

**[AI just crossed the line from "tool" to "production pipeline" full short-form videos from a single prompt, end-to-end](https://www.reddit.com/r/artificial/comments/1uag2pu/ai_just_crossed_the_line_from_tool_to_production/)**

The last 6 months have experienced an enormous leap forward in terms of AI production capabilities. I generated a tweet, which through AI, translated into an official 30s video complete with a written script, voiceover narration, inclusion of clips to accompany both visuals and audio narration together with subtitles for both video and audio, were produced. ​ Previously, this would have been considered a novelty item only. Now, it has evolved into something useful but probably wouldn't appeal to the majority if everything from this point on goes well for its users right now. ​ The true "wow" factor is not the quality of the actual video itself; rather, it is the entire process of moving from five different tools to just one prompt from start to finish. ​ What do you think is the limit in terms of human versus AI created short-form content moving forward?

1h ago

---

**[AI learned to be a villain from Hollywood. Here's how we retrain it.](https://www.reddit.com/r/artificial/comments/1ua6yez/ai_learned_to_be_a_villain_from_hollywood_heres/)**

Podcast with Peter Diamandis, entrepreneur and founder of the XPRIZE Foundation, which runs large-scale incentive competitions to crack some of the world's hardest problems, from private spaceflight to carbon removal. He recently launched the Future Vision XPRIZE, a $3.5 million competition to generate a new wave of optimistic science fiction. Covers: The historical pattern of science fiction shaping the technologies we build, and why Peter thinks this makes the stories we tell about AI especially high stakes right now How Claude’s blackmailing behavior showed the connection between dystopian training data and AI behavior How the Future Vision XPRIZE will generate a new wave of optimistic science fiction to train AI on Why public optimism about technology has dropped significantly in the US and Europe, what Peter thinks is driving it, and why he believes the data tells a different story How the cost of starting a company has fallen dramatically and how this can empower you to build your vision Why Peter thinks traditional education is no longer preparing young people for the future, and what he sees replacing it

🔗 [existentialhope.com](https://www.existentialhope.com/podcasts/peter-diamandis) • 7h ago

---

---

## Google News: "ai"

**[Norway imposes near ban on AI in elementary school](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/)**

Reuters • 8h ago

---

**[Get with the times — here's what a 'Luddite' means today](https://www.npr.org/2026/06/19/nx-s1-5853589/luddite-meaning-history-ai)**

It's often a derogatory term used to describe digital dinosaurs and technophobes. That wasn't always the case. NPR's Word of the Week looks back at the not so backwards-looking Luddites.

NPR • 15h ago

---

**[You can ignore AI giants like SpaceX, but your 401(k) won’t](https://www.latimes.com/business/story/2026-06-19/you-can-ignore-ai-giants-like-spacex-but-your-401k-wont)**

Think you can ignore all the hubbub around SpaceX, Elon Musk and IPOs

Los Angeles Times • 26m ago

---

**[The Conviction Crisis That AI Won't Let Us Hide From](https://www.forbes.com/sites/glennllopis/2026/06/19/the-conviction-crisis-that-ai-wont-let-us-hide-from/)**

A widespread "conviction crisis" plagues leaders and individuals, marked by an inability to act on beliefs and reinvent oneself amid uncertainty.

Forbes • 41m ago

---

**[US export ban on Anthropic’s AI models further strains alliances](https://www.aljazeera.com/news/2026/6/19/us-export-ban-on-anthropics-ai-models-further-strains-alliances)**

Trump administration's move to cut off allies' access to advanced AI prompts calls for greater self-reliance.

Al Jazeera • 15h ago

---

**[WATCH: President Trump talks Iran, Cuba, Israel, AI, and power on "The Axios Show"](https://www.axios.com/2026/06/19/trump-axios-show-iran-cuba-israel)**

Axios • 6h ago

---

**[Opinion | AI is too important to govern by grudge](https://www.washingtonpost.com/opinions/2026/06/19/trump-vs-anthropic-dangerous-fight-over-ai-rules/)**

The government’s fight with Anthropic is a dangerous omen.

The Washington Post • 5h ago

---

**[Exclusive: Conservatives plan nationwide protest against AI data centers](https://www.axios.com/2026/06/18/conservatives-protest-ai-data-centers)**

Axios • 1d ago

---

**[The Cloud Has Sound: The Unrelenting and Unseen Cost of A.I. Data Centers](https://www.nytimes.com/2026/06/17/us/data-centers-noise-pollution.html)**

As tech giants rush to build infrastructure, some residents who live near data centers say a constant low-frequency vibration is ruining their health and homes.

The New York Times • 2d ago

---

**[Opinion | Two Virginia Counties Diverge on AI Data Centers](https://www.wsj.com/opinion/two-virginia-counties-diverge-on-ai-data-centers-8835c1de)**

WSJ • 3h ago

---

---

## HackerNews: "ai"

**[Sixty percent of US consumers say 'AI' in brand messaging is a turnoff](https://news.ycombinator.com/item?id=48569278)**

Original research from 2,000 decision-makers and consumers on AI brand visibility, content trust, and what brands need to do as the web feels less human. 74% say the internet feels less human than it did 10 years ago.

⬆️ 1075 • 💬 574 • 2d ago • [The Leading Enterprise Content Platform | WordPress VIP](https://wpvip.com/future-of-the-web-2026/)

---

**[AI demands more engineering discipline. Not less](https://news.ycombinator.com/item?id=48570948)**

⬆️ 420 • 💬 211 • 2d ago • [charitydotwtf.substack.com](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline)

---

**[Only 16 Percent of Americans Think AI Will Have a Positive Impact on Society](https://news.ycombinator.com/item?id=48573332)**

Although Wall Street loves AI, every day Americans are significantly less optimistic about the industry, a new report from Pew Research shows.

⬆️ 397 • 💬 498 • 2d ago • [TechCrunch](https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/)

---

**[The AirPods Effect](https://news.ycombinator.com/item?id=48592832)**

How earbuds influence our beliefs and push us apart.

⬆️ 374 • 💬 672 • 1d ago • [theescapenewsletter.com](https://www.theescapenewsletter.com/p/the-airpods-effect)

---

**[Norway imposes near ban on AI in elementary school](https://news.ycombinator.com/item?id=48600093)**

⬆️ 349 • 💬 215 • 8h ago • [reuters.com](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/)

---

**[The founder's playbook: Building an AI-native startup](https://news.ycombinator.com/item?id=48566832)**

We share how AI-native founders are using Claude at every stage of the startup journey, with practical exercises, frameworks, and prompts.

⬆️ 242 • 💬 167 • 2d ago • [Claude](https://claude.com/blog/the-founders-playbook)

---

**[A new bill takes aim at government pressure to silence lawful online speech](https://news.ycombinator.com/item?id=48600950)**

The bipartisan legislation creates a federal cause of action against government officials who coerce or attempt to coerce broadcasters, interactive computer services, or AI providers into taking actions against lawful, First-Amendment-protected speech, and establishes a transparency system for government communications with those intermediaries about user expression.

⬆️ 227 • 💬 111 • 6h ago • [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2026/06/new-bill-takes-aim-government-pressure-silence-lawful-online-speech)

---

**[Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)**

CADAM is the open source text-to-CAD web application - Adam-CAD/CADAM

⬆️ 210 • 💬 97 • 2d ago • [GitHub](https://github.com/Adam-CAD/CADAM)

---

**[Is AI ruining our skills? Early results are in – and they're not good](https://news.ycombinator.com/item?id=48601286)**

⬆️ 197 • 💬 266 • 6h ago • [nature.com](https://www.nature.com/articles/d41586-026-01947-1)

---

**[The Competitive Moat That AI Can't Replicate](https://news.ycombinator.com/item?id=48573435)**

Portfolio and personal blog of Chris Hillman.

⬆️ 141 • 💬 122 • 2d ago • [ghostinthedata.info](https://ghostinthedata.info/posts/2026/2026-06-13-human-connection-moat/)

---

---

## YouTube Videos: "ai"

**[Hang On! US Giant SELLS AI to China as Tech Bubble PANICS Over Fed Pivot](https://www.youtube.com/watch?v=NRNosAgN8Z8)**

Buy Gold & Silver At A Discount: https://bit.ly/IPM-Sean-Foo-Gold - Just use the code: SEANFOO at checkout Microsoft selling AI ...

📺 Sean Foo

👁️ 45K • 👍 4K • 💬 328 • ⏱️ 14:29 • 10h ago

---

**[Inside Google&#39;s AI data centers](https://www.youtube.com/watch?v=TfW5pWpsHAo)**

"GMA" gets exclusive access inside a Google data center as communities nationwide grapple with the rapid expansion of ...

📺 ABC News

👁️ 11K • 👍 228 • 💬 98 • ⏱️ 5:37 • 21h ago

---

**[Godmother of AI: In 10 Years There Will Be Only 2 Kinds of Workers](https://www.youtube.com/watch?v=subu-xHrp1w)**

How the Internet of Cognition can transform outcomes in 5 real-world use cases: - Read Scaling Out Superintelligence ...

📺 Silicon Valley Girl

👁️ 5K • 👍 202 • 💬 12 • ⏱️ 49:04 • 9h ago

---

**[Godfather Of AI WARNS: They&#39;re Building AI So Dangerous That They Can&#39;t Even Control It](https://www.youtube.com/watch?v=y_C00dr6i9U)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Geoffrey Hinton explains why he is ...

📺 Neural Nutshell

👁️ 8K • 👍 284 • 💬 141 • ⏱️ 11:35 • 1d ago

---

**[I Was Right About AI](https://www.youtube.com/watch?v=aXy8mQeuObk)**

In this episode, I follow up on a few of my predictions about AI from my recent video: "How AI Will Fail Like The Music Industry" My ...

📺 Rick Beato

👁️ 714K • 👍 43K • 💬 7K • ⏱️ 7:47 • 1d ago

---

**[The US Government Just Pulled The World&#39;s Most Powerful AI Offline](https://www.youtube.com/watch?v=7vz6T6TNIzo)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *The most powerful AI ever released to the ...

📺 Julia McCoy

👁️ 28K • 👍 2K • 💬 166 • ⏱️ 10:09 • 1d ago

---

**[The AI Email Threat...](https://www.youtube.com/watch?v=KdWsrjpw_QI)**

Take your personal data back with Incogni! Use code ECHELON at the link below and get 60% off an annual plan: ...

📺 Upper Echelon

👁️ 42K • 👍 3K • 💬 246 • ⏱️ 13:13 • 1d ago

---

**[The Hidden Reason Anthropic Wants to Slow Down AI](https://www.youtube.com/watch?v=vu_-NTR_Pr4)**

Use code TIS at https://incogni.com/tis to get an exclusive 60% off. Anthropic says AI is becoming too powerful and may need to be ...

📺 The Infographics Show

👁️ 30K • 👍 1K • 💬 238 • ⏱️ 15:27 • 4h ago

---

**[ChatGPT Finally Works While You Sleep &amp; More AI News You Can Use](https://www.youtube.com/watch?v=ow51ck2Rl44)**

Want to save time, get more leverage, and stop figuring this AI stuff out from scratch? I put the clearest map and support inside the ...

📺 The AI Advantage

👁️ 3K • 👍 177 • 💬 7 • ⏱️ 13:51 • 6h ago

---

**[Jeff Bezos Makes Shocking AI Prediction and the Future of Jobs](https://www.youtube.com/watch?v=qI1tLQF-_9A)**

Speaking at the VivaTech conference in Paris on June 17, the Jeff Bezos pushed back on fears that artificial intelligence will ...

📺 New York Post

👁️ 13K • 👍 214 • 💬 64 • ⏱️ 5:28 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 268,102 • ❤️ 1,845 • 20h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 11,871 • ❤️ 1,532 • 15h ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 67,836 • ❤️ 1,133 • 3d ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 274,865 • ❤️ 909 • 4d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 12,148 • ❤️ 458 • 5h ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 601,208 • ❤️ 1,010 • 9d ago

---

**[Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)**

*Prefeitura do Rio de Janeiro (City of Rio de Janeiro)*

Rio 3.5 Open 397B is a frontier-class, open-source image-text-to-text AI model post-trained from Qwen 3.5 397B. It excels in agentic coding, STEM, multilingual tasks, and multimodal reasoning, featuring a 1M context window and SwiReasoning for enhanced accuracy and efficiency.

`image-text-to-text` `403.4B`

⬇️ 190,639 • ❤️ 325 • 5d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 228,669 • ❤️ 2,194 • 7d ago

---

**[FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)**

*Microsoft*

FastContext-1.0-4B-SFT is a lightweight repository-exploration subagent for LLM coding agents, designed to efficiently locate relevant code snippets using parallel read-only tool calls (READ, GLOB, GREP). Its primary use case is to reduce token consumption and context pollution for main coding agents by providing focused file paths and line ranges as evidence, thereby improving end-to-end performance in tasks like software development.

`text-generation` `4.0B`

⬇️ 1,437 • ❤️ 229 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,730,978 • ❤️ 2,006 • 2mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 33 • 💬 1 • ⭐ 24,044 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 240 • 💬 4 • ⭐ 8,334 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 101 • 💬 4 • ⭐ 87,390 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 169 • 💬 6 • ⭐ 4,498 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 20 • 💬 1 • ⭐ 83,058 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 81 • 💬 7 • ⭐ 77,755 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[FastContext: Training Efficient Repository Explorer for Coding Agents](https://huggingface.co/papers/2606.14066)**

*Shaoqiu Zhang, Maoquan Wang, Yuling Shi et al. (8 authors)*

🏢 Microsoft

FastContext separates repository exploration from code solving in LLM agents using specialized exploration models that reduce token consumption and improve resolution rates.

▲ 84 • 💬 3 • ⭐ 623 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14066) • [💻 code](https://github.com/microsoft/fastcontext) • [🔗 project](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 43 • 💬 4 • ⭐ 30,721 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 168 • 💬 2 • ⭐ 68,071 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[VibeThinker-3B: Exploring the Frontier of Verifiable Reasoning in Small Language Models](https://huggingface.co/papers/2606.16140)**

*Sen Xu, Shixi Liu, Wei Wang et al. (9 authors)*

🏢 WeiboAI

VibeThinker-3B demonstrates that compact models can achieve state-of-the-art performance on verifiable reasoning tasks through specialized training techniques, challenging conventional scaling assumptions.

▲ 98 • 💬 1 • ⭐ 1,076 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2606.16140) • [💻 code](https://github.com/WeiboAI/VibeThinker) • [🔗 project](https://github.com/WeiboAI/VibeThinker)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 74.4k • 🔱 9.6k • 1h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 40.0k • 🔱 1.9k • 15h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 9.9k • 🔱 917 • 8h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.1k • 🔱 455 • 2m ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.6k • 🔱 363 • 1d ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.3k • 🔱 407 • 2d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.1k • 🔱 196 • 2d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.6k • 🔱 124 • 6h ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.6k • 🔱 145 • 3d ago

---

**[code-yeongyu/lazycodex](https://github.com/code-yeongyu/lazycodex)**

The one and only agent harness for complex codebases. Project memory, planning, execution, and verified completion inside Codex.

`TypeScript` `ai` `ai-agents` `claude` `claude-code` `cli`

⭐ 1.5k • 🔱 76 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
