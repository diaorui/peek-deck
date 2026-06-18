---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-18T23:46:04.389708+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 18, 2026 at 23:46 UTC  
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

**[Bernie Sanders wants to give every American $1000 a year from AI profits and the reasoning actually makes sense](https://www.reddit.com/r/artificial/comments/1u9ifn2/bernie_sanders_wants_to_give_every_american_1000/)**

Saw this on Gizmodo today and it's been stuck in my head The argument is simple. AI learned from everyone's writing, art, code, conversations and companies are now worth trillions because of that. so why is none of it coming back to the people whose work built it The bill would create a $7 trillion fund, give the public a 50% stake in the biggest AI labs, $1000 a year per person to start, goes up as AI makes more Every time i use chatgpt i think about all the writers and coders and artists whose work it learned from who got nothing. This is at least someone trying to address that Is this actually doable or just a good idea that goes nowhere

2h ago

---

**[Started maintaining a small library at work and now I genuinely understand why maintainers go quiet](https://www.reddit.com/r/artificial/comments/1u9fwfx/started_maintaining_a_small_library_at_work_and/)**

Built a little internal utility about a year ago, open sourced it because why not, figured maybe 10 people would find it useful. It slowly picked up a few hundred stars and then the issues started coming in. Not a flood or anything but enough and what surprised me was how much of it wasn't really bugs it was people wanting features that made sense for their use case but would've made zero sense for the original scope of the thing. Or issues that were basically "your README didn't account for my specific setup." I like helping people, I thought I would enjoy this and I did at first but somewhere around month 4 I noticed I was dreading opening GitHub notifications. The AI-generated PRs made it worse honestly. Not because the code was always bad but because they'd come in with confident descriptions, look reasonable on the surface and then you'd spend 30 minutes tracing through edge cases only to realize whoever sent it hadn't actually tested it against anything real. At human contribution pace that was manageable. At "someone hit generate and submit" pace it's just a different problem. I have immense respect for maintainers of anything with serious adoption now. The people keeping libraries that half the internet depends on running are doing it mostly for free, mostly in their spare time,and mostly while dealing with issue reporters who write like they're filing a complaint with customer support. If you use open source software and it's saved you hours of work, go sponsor someone. Even a few dollars a month means something and most of these folks have a GitHub sponsors page just sitting there.

4h ago

---

**[Anthropic CEO Dario Amodei goes completely candid on why he left OpenAI: "When you feel that you can't trust someone when you see disturbing patterns of behavior, dishonesty, that makes it very hard to continue."](https://www.reddit.com/r/artificial/comments/1u8zigf/anthropic_ceo_dario_amodei_goes_completely_candid/)**

In a recent candid interview Anthropic CEO Dario Amodei did not hold back regarding his departure from OpenAI. He cited a fundamental breakdown of trust and "disturbing patterns of behavior" and "dishonesty" as the primary reasons it became impossible to stay. Considering the massive wave of high-profile safety researcher departures from OpenAI over the last year or two, Amodei’s comments add a lot of retroactive context to the cultural shift that happened right around the time ChatGPT was being spun up. What do you think? Does this align with everything we've seen play out with Sam Altman and the board over the past couple of years?

16h ago

---

**[Only 16 percent of Americans think AI will have a positive impact on society, a new study shows | TechCrunch](https://www.reddit.com/r/artificial/comments/1u93rnf/only_16_percent_of_americans_think_ai_will_have_a/)**

Who will foot the AI bills? Despite the fact that AI increasingly dominates our economy (it’s a hot IPO summer and we’re all just along for the ride), most Americans are not particularly optimistic about the technology’s long-term impact on the country, a new study from Pew Research reveals. In fact, although a whole lot of Americans increasingly use AI in their daily lives, most of them have neutral to negative views about it, the research reveals.

🔗 [TechCrunch](https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/) • 12h ago

---

**[RNNs vs Transformers vs SSMs: where should AI memory live for continual learning?](https://www.reddit.com/r/artificial/comments/1u9ba5s/rnns_vs_transformers_vs_ssms_where_should_ai/)**

the interesting comparison btwn the three is not recurrence vs attention vs state space but it is, whether memory lives in a tiny recurrent state, a growing KV cache or in something closer to the model network itself. RNNs keep memory in a recurrent hidden state which is elegant in itself cause the state carries forward step by step but it also creates a bottleneck i.e the model can have roughly O(N^2) parameters while carrying only roughly O(N) state across time. IMO, RNNs were doomed not because recurrence was a bad idea but because they had a bad ratio of memory to compute. Transformers is completely at the other side, instead of compressing the past into one hidden state, they store past activations as key-value entries and attend over them. These are the little post-it notes, every token leaves behind a key for finding it and a value for what should be remembered. That is extremely powerful but it has an awkward property i.e. the model is mostly managing context while it runs, not naturally turning that experience into durable model knowledge so you get a split between fixed weights on one side and fast changing KVcache memory on the other. SSMs are interesting because they bring explicit state back into the center of the architecture discussion. They are not just faster attention but they are another answer to the question of where sequence state should live. The part which I is exciting for me is whether state should live in a compressed working dimension or closer to the model’s internal neuron/connectivity structure. BDH is one promising example of the latter direction, one way to read it is as SSM-like in the GPU implementation, but graph-based in the more general interpretation. Compared with a standard SSM or a linear transformer, the model state lives in a much larger neuron space N rather than only a smaller working dimension D, with N>>D. The GPU version does not materialize the full graph. It keeps the graph as the interpretation but runs it through a compressed low-rank form, because GPUs like dense matrix math much more than sparse graphs. The state is also sparse and positive which makes the graph interpretation more natural. Instead of thinking of memory only as a growing bag of KV notes, you can reinterpret the update as a small change to a connectivity matrix i.e if the system was in one state and then moved to another, that before to after transition strengthens part of the graph. This is like a middle ground and I would call it not too little and not too much. RNNs compress too much into a small state, transformers keep adding to the KV cache as the sequence grows and a synaptic memory design tries to put working memory closer to the same structure that stores longer term function. Another way to say it is: memory should maybe be constant size and information-shaped, not just a time buffer of the last n tokens. I am not claiming at all that this kills transformers or solves continual learning entirely but I just think where should memory live is an important framing than the usual frontier AI horse race. Are network centric architectures an important direction in frontier AI or still contricted by having to compress history into state?

7h ago

---

**[Microsoft Makes Big AI Inroads in China by Selling OpenAI Models](https://www.reddit.com/r/artificial/comments/1u9a54p/microsoft_makes_big_ai_inroads_in_china_by/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-06-17/microsoft-s-china-ai-business-grows-on-openai-model-sales) • 7h ago

---

**[AI support vendor quoted 40% deflection, called 8% normal after 8 months](https://www.reddit.com/r/artificial/comments/1u9dfzr/ai_support_vendor_quoted_40_deflection_called_8/)**

went live with an AI support bot last january. connected it to our help center, trained it on our top 12 ticket types, gave it 6 weeks to learn. by month 3 we were at 6% deflection. month 8 we hit 8% and stalled. our account manager kept sending benchmark decks showing 7-12% was "typical for complex B2B" and for a while we just believed it. we even renewed because the deflection numbers looked fine relative to whatever PDFs he was sending over. what actually cracked it open was a founder i met at SaaStr in may. his team was hitting 47% deflection on about 900 tickets a month, billing and onboarding questions mostly, same general product category as us. i assumed he was measuring it wrong. he wasn't. he walked me through the setup and the difference was architecture, not training or prompting. his tool was built around resolution from day one. ours was a ticketing system with an LLM wrapper on top and they called it "AI customer service." we started re-evaluating and every single demo ended up being the same conversation: is the AI the actual core of this thing or just a layer sitting on top of a routing system. completely different product philosophies, and apparently a 39-point deflection gap between them in practice. still haven't switched yet so i don't have a clean before/after. but if 8% is what most teams are actually hitting then either we bought something broken or this whole category is one big benchmark hallucination.

5h ago

---

**[How to Tell a Good Speech Dataset for AI From a Bad One](https://www.reddit.com/r/artificial/comments/1u9283m/how_to_tell_a_good_speech_dataset_for_ai_from_a/)**

🔗 [thestreet.com](https://www.thestreet.com/crypto/newsroom/how-to-tell-a-good-speech-dataset-for-ai-from-a-bad-one) • 13h ago

---

**[Made a promo for my comic with Seedance 2.0. Thoughts?](https://www.reddit.com/r/artificial/comments/1u9kysb/made_a_promo_for_my_comic_with_seedance_20/)**

56m ago

---

**[A chessboard is a surprisingly good way to catch what VLMs still get wrong](https://www.reddit.com/r/artificial/comments/1u9e5kn/a_chessboard_is_a_surprisingly_good_way_to_catch/)**

Spent some time testing what vision language models actually understand versus what they can describe. A chessboard turned out to be a great probe because there is one correct answer for the layout (the FEN string). The models usually recognize the pieces, then write them onto the wrong squares. So the gap is not really perception, it is spatial reasoning and getting the structured output exactly right. This made me rethink how we benchmark these things. Accuracy on loose descriptions hides the part that breaks in production. We ran this at VideoDB Labs as part of a wider look at VLM evaluation. What is a task you have found that exposes the real limits of these models?

5h ago

---

---

## Google News: "ai"

**[Amazon investigating engineers who criticized AI data center expansion](https://www.cnbc.com/2026/06/18/amazon-engineers-ai-data-center-opposition.html)**

Five Amazon employees testified at Seattle City Council meetings where officials sought feedback on a year-long data center new construction pause.

CNBC • 4h ago

---

**[Exclusive: Conservatives plan nationwide protest against AI data centers](https://www.axios.com/2026/06/18/conservatives-protest-ai-data-centers)**

Axios • 7h ago

---

**[Regulators greenlight plan for quick AI data center grid connections](https://thehill.com/policy/energy-environment/5931287-ai-data-centers-grid-operators-ferc/)**

The Hill • 1h ago

---

**[Student Cheating Is Becoming Impossible to Detect in an A.I. Era](https://www.nytimes.com/2026/06/18/us/ai-apps-students-cheat.html)**

The New York Times • 11h ago

---

**[AI helped diagnose 18 children whose rare diseases had stumped doctors](https://www.nbcnews.com/video/ai-helped-diagnose-18-children-whose-rare-diseases-had-stumped-doctors-265343557823)**

New research from Boston Children's Hospital’s center for rare diseases and the AI company OpenAI reveals that off-the-shelf AI tools can help identify which errors in patients’ genomes might be causing the children’s diseases. NBC News' Jared Perlo discusses the findings of the research.

NBC News • 38m ago

---

**[Anthropic is battling Uncle Sam for control of superpowered AI](https://www.economist.com/briefing/2026/06/18/anthropic-is-battling-uncle-sam-for-control-of-superpowered-ai)**

The Economist • 11h ago

---

**[White House talks with Anthropic shift to setting AI security rules](https://www.politico.com/news/2026/06/18/white-house-talks-with-anthropic-shift-to-setting-ai-security-rules-00967758)**

Politico • 4h ago

---

**[The White House said Anthropic’s powerful AI was ‘jailbroken.’ Here’s what that means.](https://www.washingtonpost.com/technology/2026/06/18/surprisingly-simple-ways-ai-can-be-tricked-into-breaking-its-own-rules/)**

It’s surprisingly simple to trick chatbots into breaking their own rules and spilling forbidden knowledge. Even poems and bedtime stories can work.

The Washington Post • 7h ago

---

**[Accenture Takes a Hit on Worsening Outlook and Cloudy AI Future](https://www.wsj.com/business/accenture-takes-a-hit-on-worsening-outlook-and-cloudy-ai-future-73eb8bfb)**

WSJ • 5h ago

---

**[America Is Headed Toward the Infinite Workweek](https://www.theatlantic.com/technology/2026/06/ai-agents-jobs-exhaustion/687596/)**

The future of AI and jobs will be so much weirder than you think.

The Atlantic • 7h ago

---

---

## HackerNews: "ai"

**[Sixty percent of US consumers say 'AI' in brand messaging is a turnoff](https://news.ycombinator.com/item?id=48569278)**

Original research from 2,000 decision-makers and consumers on AI brand visibility, content trust, and what brands need to do as the web feels less human. 74% say the internet feels less human than it did 10 years ago.

⬆️ 1065 • 💬 573 • 1d ago • [The Leading Enterprise Content Platform | WordPress VIP](https://wpvip.com/future-of-the-web-2026/)

---

**[Has AI already killed self-help nonfiction books?](https://news.ycombinator.com/item?id=48558489)**

⬆️ 409 • 💬 479 • 2d ago • [tim.blog](https://tim.blog/2026/06/12/has-ai-already-killed-nonfiction/)

---

**[AI demands more engineering discipline. Not less](https://news.ycombinator.com/item?id=48570948)**

⬆️ 408 • 💬 205 • 1d ago • [charitydotwtf.substack.com](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline)

---

**[Only 16 Percent of Americans Think AI Will Have a Positive Impact on Society](https://news.ycombinator.com/item?id=48573332)**

Although Wall Street loves AI, every day Americans are significantly less optimistic about the industry, a new report from Pew Research shows.

⬆️ 393 • 💬 484 • 1d ago • [TechCrunch](https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/)

---

**[The founder's playbook: Building an AI-native startup](https://news.ycombinator.com/item?id=48566832)**

We share how AI-native founders are using Claude at every stage of the startup journey, with practical exercises, frameworks, and prompts.

⬆️ 238 • 💬 166 • 1d ago • [Claude](https://claude.com/blog/the-founders-playbook)

---

**[Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)**

CADAM is the open source text-to-CAD web application - Adam-CAD/CADAM

⬆️ 205 • 💬 97 • 1d ago • [GitHub](https://github.com/Adam-CAD/CADAM)

---

**[Microsoft turns to AWS as GitHub faces AI capacity crunch](https://news.ycombinator.com/item?id=48549918)**

Microsoft is adding AWS capacity for GitHub after AI-driven usage strained the developer platform, exposing Azure constraints and the infrastructure cost of agentic coding.

⬆️ 154 • 💬 76 • 2d ago • [RuntimeWire](https://runtimewire.com/article/microsoft-github-aws-ai-capacity-crunch)

---

**[The Competitive Moat That AI Can't Replicate](https://news.ycombinator.com/item?id=48573435)**

Portfolio and personal blog of Chris Hillman.

⬆️ 139 • 💬 122 • 1d ago • [ghostinthedata.info](https://ghostinthedata.info/posts/2026/2026-06-13-human-connection-moat/)

---

**[After AI takes everything](https://news.ycombinator.com/item?id=48556644)**

⬆️ 101 • 💬 113 • 2d ago • [ursb.me](https://ursb.me/en/posts/after-ai-takes-everything/)

---

**[The AI Hate Progression](https://news.ycombinator.com/item?id=48589485)**

I think I've spoken at length in other places about how I am a very staunch AI hater and everything I hate about how the tech is presented t...

⬆️ 99 • 💬 132 • 5h ago • [xodium.net](https://www.xodium.net/2026/06/the-ai-hate-progression.html)

---

---

## YouTube Videos: "ai"

**[The US Government Just Pulled The World&#39;s Most Powerful AI Offline](https://www.youtube.com/watch?v=7vz6T6TNIzo)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *The most powerful AI ever released to the ...

📺 Julia McCoy

👁️ 19K • 👍 1K • 💬 135 • ⏱️ 10:09 • 21h ago

---

**[AI Swarms Just Killed the One-Man Agency](https://www.youtube.com/watch?v=7cYtuRMro_U)**

Try Abacus AI* — https://chatllm.abacus.ai/fmj *One founder just replaced an entire AI team five real jobs run start to finish, ...

📺 Julia McCoy

👁️ 756 • 👍 84 • 💬 6 • ⏱️ 9:03 • 2h ago

---

**[Godfather Of AI WARNS: They&#39;re Building AI So Dangerous That They Can&#39;t Even Control It](https://www.youtube.com/watch?v=y_C00dr6i9U)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Geoffrey Hinton explains why he is ...

📺 Neural Nutshell

👁️ 3K • 👍 148 • 💬 48 • ⏱️ 11:35 • 7h ago

---

**[Jeff Bezos Makes Shocking AI Prediction and the Future of Jobs](https://www.youtube.com/watch?v=qI1tLQF-_9A)**

Speaking at the VivaTech conference in Paris on June 17, the Jeff Bezos pushed back on fears that artificial intelligence will ...

📺 New York Post

👁️ 10K • 👍 183 • 💬 60 • ⏱️ 5:28 • 1d ago

---

**[China’s New AI Is 6X More Efficient Than Claude](https://www.youtube.com/watch?v=gKBazze-8qU)**

China just dropped two new open-weight coding models, Kimi K2.7 Code and GLM-5.2, and the timing could not be more ...

📺 AI Revolution

👁️ 29K • 👍 892 • 💬 72 • ⏱️ 16:01 • 1d ago

---

**[AI Researchers Are Warning About What Comes After AGI](https://www.youtube.com/watch?v=ddgT5I2Xm8A)**

CHAPTERS ⤵ 00:00 - AGI to ASI: DeepMind's Roadmap to Superintelligence 07:43 - Count Anything: The AI Vision Model That ...

📺 Dylan Curious

👁️ 6K • 👍 390 • 💬 94 • ⏱️ 31:27 • 23h ago

---

**[Don&#39;t build more AI agents until you watch this](https://www.youtube.com/watch?v=BOXK2XFLA-E)**

Full post with Agent Maintenance Guide: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 47K • 👍 1K • 💬 158 • ⏱️ 18:25 • 1d ago

---

**[New #1 open-source AI model is here!](https://www.youtube.com/watch?v=6d__WOpZswY)**

GLM 5.2 review. New best open source AI model. #ai #aitools #llm #ainews #agi #singularity #gpt #deepseek Thanks to our ...

📺 AI Search

👁️ 295K • 👍 10K • 💬 1K • ⏱️ 29:57 • 1d ago

---

**[Humanoid Robot Factories Now Build One Per Hour — Here Are The Production Numbers](https://www.youtube.com/watch?v=Nkiyuo-z3Vc)**

Sources Figure AI Official Blog | Ramping Figure 03 Production | https://www.figure.ai/news/ramping-figure-03-production ...

📺 Jason Lowe on AI

👁️ 115K • 👍 6K • 💬 650 • ⏱️ 2:51 • 1d ago

---

**[Fable 5 Replacement Just Dropped: Fusion (Fable Level AI)](https://www.youtube.com/watch?v=wzay-VWjoRM)**

Fable 5 is gone, and now the big question is simple: what comes next? OpenRouter just introduced Fusion, a system that sends ...

📺 AI Revolution

👁️ 18K • 👍 684 • 💬 47 • ⏱️ 15:28 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 211,424 • ❤️ 1,697 • 13h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 4,307 • ❤️ 1,335 • 1d ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 56,162 • ❤️ 1,098 • 2d ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 229,156 • ❤️ 882 • 3d ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 527,080 • ❤️ 1,001 • 8d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 6,589 • ❤️ 403 • 1d ago

---

**[Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)**

*Prefeitura do Rio de Janeiro (City of Rio de Janeiro)*

Rio 3.5 Open 397B is a frontier-class, open-source image-text-to-text AI model post-trained from Qwen 3.5 397B. It excels in agentic coding, STEM, multilingual tasks, and multimodal reasoning, featuring a 1M context window and SwiReasoning for enhanced accuracy and efficiency.

`image-text-to-text` `403.4B`

⬇️ 190,501 • ❤️ 322 • 4d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 183,093 • ❤️ 2,161 • 6d ago

---

**[Qwopus3.6-27B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF)**

*Jackrong*

Qwopus-3.6-27B-Coder is a 27B parameter multimodal model fine-tuned for agentic coding and tool-use reasoning. It excels at repository-level code generation, debugging, and structured tool orchestration, leveraging trace inversion and native long-context support for complex developer workflows.

`image-text-to-text` `460.7M`

⬇️ 122,175 • ❤️ 250 • 3d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,420,052 • ❤️ 1,969 • 2mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 30 • 💬 1 • ⭐ 22,419 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 236 • 💬 4 • ⭐ 8,227 • 28d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 99 • 💬 4 • ⭐ 87,190 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 18 • 💬 1 • ⭐ 82,978 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[FastContext: Training Efficient Repository Explorer for Coding Agents](https://huggingface.co/papers/2606.14066)**

*Shaoqiu Zhang, Maoquan Wang, Yuling Shi et al. (8 authors)*

🏢 Microsoft

FastContext separates repository exploration from code solving in LLM agents using specialized exploration models that reduce token consumption and improve resolution rates.

▲ 83 • 💬 3 • ⭐ 576 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14066) • [💻 code](https://github.com/microsoft/fastcontext) • [🔗 project](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 166 • 💬 6 • ⭐ 4,084 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 42 • 💬 4 • ⭐ 30,684 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 80 • 💬 7 • ⭐ 77,661 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[JoyAI-VL-Interaction: Real-Time Vision-Language Interaction Intelligence](https://huggingface.co/papers/2606.14777)**

*Dingyu Yao, Junhao Zhou, Chenxu Yang et al. (15 authors)*

🏢 JD.com Open Source

A vision-language model operates continuously in real-time, making autonomous decisions about when to respond or delegate, enabling interactive systems that perceive and act upon environmental changes without user prompting.

▲ 187 • 💬 2 • ⭐ 293 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14777) • [💻 code](https://github.com/jd-opensource/JoyAI-VL-Interaction) • [🔗 project](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

---

**[VibeThinker-3B: Exploring the Frontier of Verifiable Reasoning in Small Language Models](https://huggingface.co/papers/2606.16140)**

*Sen Xu, Shixi Liu, Wei Wang et al. (9 authors)*

🏢 WeiboAI

VibeThinker-3B demonstrates that compact models can achieve state-of-the-art performance on verifiable reasoning tasks through specialized training techniques, challenging conventional scaling assumptions.

▲ 96 • 💬 1 • ⭐ 1,010 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.16140) • [💻 code](https://github.com/WeiboAI/VibeThinker) • [🔗 project](https://github.com/WeiboAI/VibeThinker)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 73.6k • 🔱 9.5k • 3h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 36.6k • 🔱 1.7k • 1m ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 9.8k • 🔱 893 • 8h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 4.5k • 🔱 393 • 8h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 3.8k • 🔱 421 • 2m ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.5k • 🔱 362 • 11h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.3k • 🔱 400 • 1d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.1k • 🔱 193 • 1d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.6k • 🔱 144 • 2d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.6k • 🔱 116 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
