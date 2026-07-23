---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-23T10:23:22.983980+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 23, 2026 at 10:23 UTC  
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

**[An AI broke out of its sandbox yesterday. Then it hacked a company. Nobody told it to do either of those things.](https://www.reddit.com/r/artificial/comments/1v3mxzb/an_ai_broke_out_of_its_sandbox_yesterday_then_it/)**

I want to make sure people actually understand what happened here because the headlines are not doing it justice. On July 21 OpenAI confirmed that GPT-5.6 Sol was running inside an isolated sandbox with no internet access. Its job was to solve a cybersecurity benchmark called ExploitGym. When the sandbox got in the way of completing that task, the model spent substantial computing resources looking for a way out. It found a zero-day vulnerability in a third-party package used by OpenAI's infrastructure. It exploited it. It escalated its own privileges. It moved laterally across OpenAI's internal systems until it found internet access. Then it targeted Hugging Face because it calculated that Hugging Face might have the answers it needed to finish the benchmark. Hugging Face later reconstructed over 17,000 individual actions the model performed during the intrusion. Their CEO called it possibly the first incident of its kind in history. OpenAI called it unprecedented. Here is the part that should make everyone stop and think. The model was not trying to cause harm. It was trying to win a test. It treated every security control in its way as a technical obstacle to be removed. Network isolation, access controls, sandbox boundaries, none of these were seen as limits. They were seen as problems to solve. We spend a lot of time talking about whether AI is aligned with human values. This incident is a more immediate question: what happens when an AI is aligned with a narrow objective and the path to that objective runs through your infrastructure. The model did exactly what it was optimized to do. That is the problem.

16h ago

---

**[Nvidia's Jensen Huang defends Chinese AI amid Kimi panic](https://www.reddit.com/r/artificial/comments/1v3l4t7/nvidias_jensen_huang_defends_chinese_ai_amid_kimi/)**

🔗 [axios.com](https://www.axios.com/2026/07/22/nvidia-jensen-huang-china-open-source-ai) • 17h ago

---

**[The Hugging Face incident: two failures, and we’re only talking about one](https://www.reddit.com/r/artificial/comments/1v47mn3/the_hugging_face_incident_two_failures_and_were/)**

Everyone's focused on the sandbox escape, which is fair, it's the dramatic part. But that was a zero-day in internally hosted software. Containment bugs are old news. We know how to think about them: egress rules, microVM isolation, no ambient credentials. The part I find more interesting is everything that happened after. Once the agent had internet access, it picked Hugging Face as a target, found exposed credentials, chained them with another vulnerability, and pulled the benchmark answers. All of that went through ordinary tool calls. Nothing sat between "agent proposes an action" and "side effect happens." And the model wasn't misaligned in any interesting sense. It was hyperfocused on passing an eval, which is exactly what it was trained to be. Behavior was working as intended. Execution was ungoverned. So the question I keep coming back to: for those of you running agents with real tool access in production, what actually sits in the execution path? As far as I can tell the common answers are: - prompt guardrails, which are probabilistic and live inside the loop the agent controls - monitoring and traces, which tell you after the side effect landed - human approval on a hardcoded list of "dangerous" tools, which breaks down the moment the dangerous thing is a legitimate tool pointed somewhere it shouldn't be That last one is what got me. A tool allowlist wouldn't have caught this. The tools were fine. The destination and the credentials weren't. My read on why there's no standard answer yet, and I'd like to be wrong about some of this: Enforcement is easy, policy authoring is brutal. Standing up a gateway is a week. Deciding what an agent is allowed to do when its task is "research this and summarize" is a non-enumerable action space. Classic permission systems assume a finite set of verbs. Incentives point the other way. Every DENY is a failed task. Teams optimize completion rate, not refusal rate. A layer that degrades the demo doesn't survive review. No shared representation of intent. Every framework has its own tool schema, so no policy is portable and everyone rewrites theirs. The layer sits at the wrong altitude. An application-level gate is only worth the network and OS isolation underneath it, and whoever writes the agent usually doesn't own the infra. None of this is a new problem in security terms. Capabilities go back to 1966, complete mediation to Saltzer and Schroeder in 1975. OPA, SPIFFE, seccomp, service meshes all do versions of this for normal workloads. Nobody wired them into agent runtimes because agents went from answering to acting in about two years and control layers historically lag capability by five to ten. Disclosure so it's not weird later: I work on an open source protocol in this space, so I'm obviously not neutral. Not linking it, it's in my profile if you care. I'm more interested in what people are actually doing than in pitching anything, and I'll say upfront that no policy layer would have stopped the zero-day. Nothing at that altitude does. It changes what an escaped agent can reach, not whether it escapes. What are you running?

2h ago

---

**[Erin Brockovich Perfectly Lays Out Why AI Data Centers Are 'Pushing People Too Far' In Viral Clip](https://www.reddit.com/r/artificial/comments/1v3nxly/erin_brockovich_perfectly_lays_out_why_ai_data/)**

Are the impacts worth the benefits?

🔗 [Comic Sands](http://comicsands.com/erin-brockovich-data-centers) • 16h ago

---

**[How to track new AI drops without the social media delay?](https://www.reddit.com/r/artificial/comments/1v456f7/how_to_track_new_ai_drops_without_the_social/)**

Social media is fine for AI news, but the algorithm delay is killing me. I always feel like I'm finding out about new LLMs, tools, or major updates way after they happen. How do you guys stay updated in real-time without having to refresh Hugging Face or X all day?

4h ago

---

**[Does anybody know how these nostalgia style AI videos are made?](https://www.reddit.com/r/artificial/comments/1v4318h/does_anybody_know_how_these_nostalgia_style_ai/)**

I think the hardest part is getting the reference images and using a model like seedance for the motion. I've tried tons of different prompts with the latest models and never can get images as good as these videos. Whole frame makes sense, properly labeled name brand products, clear details and text in the distance. I think nano banana gets closer to this effect than gpt images but I've never gotten it to be this good, any suggestions?

6h ago

---

**[I ran the actual numbers on AI dubbing via API (ElevenLabs + lipsync) - here's what a minute of localized video really costs](https://www.reddit.com/r/artificial/comments/1v48cnd/i_ran_the_actual_numbers_on_ai_dubbing_via_api/)**

People say just use AI to dub your videos with absolutely zero cost detail, so I priced out the full pipeline for my own channel. Sharing the math because I couldn't find it anywhere. A real dubbing pipeline is two API costs, not one: Voice (ElevenLabs) - cloning your voice + generating the translated track. Credit-based; for talking-head content budget roughly a few dollars per finished minute depending on plan. (check their current tiers, this moves.) Lipsync (the part everyone forgets) - matching the mouth to the new audio. This is where the surprises are: Sync (sync.so): $0.05/sec = $3/min, flat, via API. Predictable, which matters when you're batching. HeyGen: priced per-minute on higher tiers and climbs fast at volume, but note it's really avatar-generation, not syncing your footage. Wav2Lip: "free," but you're paying in GPU time + setup hours. If your time is worth anything it's not free. My rough all-in: ~$5–7 per finished minute for voice + lipsync via API, no editor. For a 10-min video in 3 languages that's ~$150–210 vs. the reshoot/agency cost of… don't ask. Anyone found cheaper for the lipsync leg specifically? Curious what volume folks are running.

1h ago

---

**[this little its bitsy tiny gemma4 model on my 3060 is talking better than chat gpt](https://www.reddit.com/r/artificial/comments/1v473bz/this_little_its_bitsy_tiny_gemma4_model_on_my/)**

this model is the goat!

2h ago

---

**[the more autonomous my agent got, the less i trusted it near my real accounts](https://www.reddit.com/r/artificial/comments/1v3ypie/the_more_autonomous_my_agent_got_the_less_i/)**

Everyone in here treats full autonomy as the finish line. I went the other way. The version I actually kept using is the one that stops and asks right before it touches Gmail or the CRM, per action, not one blanket yes at setup. sounds like a downgrade, i know. but an agent that can send on its own is the exact thing i can't leave running while i'm heads down in a meeting. the one that pauses the second before it acts is the one i'll let near a live inbox, because the gate sits where the actual mistake would happen. that sandbox-escape story near the top of the sub is basically my whole argument. the capability isn't the scary part, the unsupervised action is. i don't want a smarter agent, i want a boring one that checks with me first. so the line i actually care about isn't how capable it is. it's whether approval lands at the task level or on each individual action right before it fires. where do you put it. fwiw Runner lands the gate exactly where you're pointing, it asks permission right before each individual action on a connected app like Gmail or HubSpot fires, not one blanket yes at setup, https://runner.now?utm_source=s4l&utm_medium=post&utm_campaign=runner&utm_term=reddit&utm_content=post_d1e9f030-3325-42d0-b19d-bc0440c9621b

9h ago

---

**[Linearity AI is a good example of everything going wrong with the AI market](https://www.reddit.com/r/artificial/comments/1v3p727/linearity_ai_is_a_good_example_of_everything/)**

Linearity used to be a fairly straightforward iPad design app. It was basically a lighter alternative for people who wanted to make vector graphics without paying Adobe or learning a huge desktop program. Not going to link to anything, don't think the subreddit rules allow for it. but like EVERYONE else it has suddenly reinvented itself around AI. Maybe the product is useful. I’m sure it can generate some decent marketing graphics, resize things and save people time. Claude Design feels a 1000% better. But the whole thing feels less like a company developing something meaningful in AI and more like a design app realising that “AI” is where the enterprise money is. Linearity does not have its own LLM. It is taking models and technology built elsewhere, putting them inside its existing design software and presenting the result as a new AI platform. There is nothing automatically wrong with that. Almost every AI startup depends on someone else’s model. The annoying part is the gap between what these companies are actually building and how they talk about it. A design tool adds a prompt box, connects to outside models and suddenly it is talking about changing how creativity works. Everything becomes an “AI engine.” Templates become intelligence. Brand guidelines become an intelligent brand. Automation that would previously have been sold as a useful feature is now treated as an entirely new category of technology. At some point we need to ask what exactly the company has contributed. Or? Claude Design is much more interesting to me because it comes from the opposite direction. Claude is already a general model that can reason across writing, research, code, documents and design. The design part has the potential to become one part of a much broader working environment. That seems like a more believable future than paying for dozens of separate AI wrappers. One for making banners, another for presentations, another for logos, another for social posts and another for resizing the same social posts. This also connects to the larger problem with AI right now. We are creating an economy where a handful of companies train the models and thousands of smaller companies sell access to them through different interfaces. Each one adds a monthly subscription, a credit system and a layer of marketing language claiming that it has transformed an industry. Most of them have not transformed anything. They have made one existing task slightly faster. Again, that can still be valuable. I would happily use a tool that turns one design into ten correctly sized versions. But saving twenty minutes is not the same thing as reinventing creative work. There is also something bleak about the obsession with producing more content. Companies already publish far too much material that nobody wants to read or look at. AI is being sold as a way to produce even more of it, faster and with fewer people. The bottleneck was never just the designer taking too long to make the banner. It was usually that the campaign was uninteresting, the message was vague, nobody had made a clear decision and six people needed to approve it. This is why I find Claude Design more promising, even though it will obviously have plenty of problems of its own. The interesting possibility is not simply that it can generate an image. It is that the same system could understand the research, the brief, the product, the copy, the design and perhaps the eventual implementation. Linearity and others feel more like an existing software company attaching itself to that change because the old category of “nice iPad design app” was not going to produce the same valuation or enterprise pricing.

15h ago

---

---

## Google News: "ai"

**[OpenAI blamed a hacking event on its AI models gone rogue. Here is what to know](https://www.npr.org/2026/07/23/g-s1-135085/openai-hacking-ai-models)**

The incident is stirring debates over the need for stronger AI guardrails and the extent to which AI agents are capable of acting on their own.

NPR • 4h ago

---

**[Mark Zuckerberg launches AI optimism campaign](https://www.axios.com/2026/07/23/mark-zuckerberg-ai-optimism)**

Axios • 22m ago

---

**[A town renamed its festival ‘AI Love Irondale Day.’ Then came the comments](https://www.npr.org/2026/07/23/nx-s1-5896481/data-center-backlash-ai-love-irondale-day)**

The online outcry over the renaming of a summer festival illustrates the unease over the data center boom in the South.

NPR • 1h ago

---

**[Google burning through cash with spiralling AI costs](https://www.bbc.com/news/articles/c235n47g8g8o)**

The company said earlier this year it expected to spend as much as $190bn on AI investments.

BBC • 3h ago

---

**[Tesla and Alphabet shares slump in premarket trading as AI spending concerns spook investors](https://www.cnbc.com/2026/07/23/tesla-tsla-alphabet-googl-stock-today.html)**

Both Tesla and Alphabet signaled higher spending as they invest in artificial intelligence.

CNBC • 1h ago

---

**[China Reignites Robotaxi Race, Alphabet Signals Bigger AI Bills](https://www.bloomberg.com/news/newsletters/2026-07-23/china-reignites-robotaxi-race-alphabet-signals-bigger-ai-bills)**

Bloomberg.com • 1h ago

---

**[Tech's AI debt boom, in one chart](https://finance.yahoo.com/technology/article/techs-ai-debt-boom-in-one-chart-143849995.html)**

So much debt is being piled on tech companies right now.

Yahoo Finance • 19h ago

---

**[Trump’s Plan for Science: More Money for A.I., Less for Universities](https://www.nytimes.com/2026/07/22/us/politics/trump-research-funding-artificial-intelligence.html)**

The New York Times • 12h ago

---

**[Elon Musk says Grok Imagine will make ‘historically accurate’ AI adaptation of Homer’s Odyssey](https://www.theguardian.com/film/2026/jul/22/elon-musk-grok-imagine-historically-accurate-ai-homers-odyssey-christopher-nolan)**

The billionaire says the AI-generated film will stay true to Homer’s original, after repeatedly criticising Christopher Nolan’s blockbuster over its casting choices

The Guardian • 22h ago

---

**[Asian stocks rise as AI capex ramps up, oil at six-week highs](https://www.reuters.com/world/china/global-markets-wrapup-1-2026-07-23/)**

Reuters • 8h ago

---

---

## HackerNews: "ai"

**[China’s open-weights AI strategy is winning](https://news.ycombinator.com/item?id=48979269)**

China's open-weights AI strategy is winning: its companies are taking the lead. America's closed-first, locked-down strategy is doomed to failure - and it could take the US economy down with it.

⬆️ 1233 • 💬 930 • 2d ago • [Ben Werdmuller](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/)

---

**[Airport Simulator](https://news.ycombinator.com/item?id=48976846)**

The sky (and your endurance) is the limit!

⬆️ 852 • 💬 164 • 2d ago • [Airport Simulator](https://airport.apunen.com/)

---

**[Are AI labs pelicanmaxxing?](https://news.ycombinator.com/item?id=49010129)**

I generated 1,000+ SVGs across 7 frontier models to test whether AI labs are training on Simon Willison’s pelican-riding-a-bicycle benchmark.

⬆️ 547 • 💬 211 • 17h ago • [Dylan Castillo](https://dylancastillo.co/posts/pelicanmaxxing.html)

---

**[Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting](https://news.ycombinator.com/item?id=48995213)**

Block's Buzz combines team chat, AI agents, workflows and Git hosting in a self-hostable workspace built on signed Nostr events.

⬆️ 371 • 💬 326 • 1d ago • [RuntimeWire](https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git)

---

**[Quality non-fiction books are the antithesis of AI slop](https://news.ycombinator.com/item?id=49007247)**

⬆️ 367 • 💬 125 • 20h ago • [resobscura.substack.com](https://resobscura.substack.com/p/quality-non-fiction-books-are-the)

---

**[Five US tech giants' hidden debts soar to $1.65T on opaque AI funding](https://news.ycombinator.com/item?id=48987863)**

Data center leases, GPU supply contracts raise liabilities at Meta, Oracle, Nikkei study shows

⬆️ 364 • 💬 260 • 2d ago • [Nikkei Asia](https://asia.nikkei.com/business/technology/five-us-tech-giants-hidden-debts-soar-to-1.65tn-on-opaque-ai-funding)

---

**[Businesses with ugly AI menu redesigns](https://news.ycombinator.com/item?id=49005973)**

I like supporting local businesses but it's so disheartening to see the increasing use of genAI in their branding/marketing/etc. Yuck yuck YUCK!!!

⬆️ 305 • 💬 207 • 21h ago • [fiddery](https://blog.fiddery.com/businesses-with-ugly-ai-menu-redesigns/)

---

**[How we measured AI writing across arXiv, and where the measurement breaks](https://news.ycombinator.com/item?id=48981206)**

We scored the full text of 12,750 arXiv papers and found that about a third of new ones read as machine-written. Here is the method, the results, and an honest account of the limitations.

⬆️ 242 • 💬 171 • 2d ago • [unslop](https://unslop.run/blog/measuring-ai-writing-on-arxiv)

---

**[AI makes programming differently difficult](https://news.ycombinator.com/item?id=48996197)**

⬆️ 162 • 💬 141 • 1d ago • [cacm.acm.org](https://cacm.acm.org/opinion/ai-didnt-make-programming-easier-it-just-made-it-differently-difficult/)

---

**[Most Americans say "not in my backyard" to AI data centers](https://news.ycombinator.com/item?id=49007525)**

⬆️ 138 • 💬 290 • 19h ago • [redfin.com](https://www.redfin.com/news/ai-data-centers-opposition-education-benefit/)

---

---

## YouTube Videos: "ai"

**[It Begins: An AI Tried to Escape the Lab](https://www.youtube.com/watch?v=r4H7rx5nn1A)**

Join My Newsletter for Regular AI Updates https://forwardfuture.com My Links X: https://x.com/matthewberman ...

📺 Matthew Berman

👁️ 54K • 👍 2K • 💬 560 • ⏱️ 10:43 • 16h ago

---

**[How worried should we be about the AI that went rogue and launched a cyber-attack? | BBC News](https://www.youtube.com/watch?v=M4kliMrqbB4)**

OpenAI has revealed some of its most advanced AI models went rogue and hacked a start-up after it lost control of them during a ...

📺 BBC News

👁️ 87K • 👍 1K • 💬 378 • ⏱️ 11:03 • 14h ago

---

**[The AI Industry Just Got What It Deserved](https://www.youtube.com/watch?v=9nUmVktlwvA)**

The people who built the attention economy barely let their own children near it, and that hypocrisy is only the beginning.

📺 House of El: AI

👁️ 186K • 👍 14K • 💬 3K • ⏱️ 24:19 • 2d ago

---

**[Central Banks Just Ran the Numbers on AI. Report Warns Collapse is Coming.](https://www.youtube.com/watch?v=x6LOgQz7XuU)**

How I Became a Sovereign Professional - The Freelance Formula https://www.brendandell.com/freelance-formula-299 Currently ...

📺 Brendan Dell 

👁️ 54K • 👍 2K • 💬 394 • ⏱️ 28:26 • 2d ago

---

**[US Just Issued China An Unthinkable AI Threat](https://www.youtube.com/watch?v=bPrWvdqhdUo)**

Buy Gold & Silver At A Discount: https://bit.ly/IPM-Sean-Foo-Gold - Just use the code: SEANFOO at checkout In a massive move, ...

📺 Sean Foo

👁️ 106K • 👍 7K • 💬 864 • ⏱️ 15:45 • 20h ago

---

**[AI Security Incidents and the Global AI Race | Jack Hidary on CNBC Squawk on the Street](https://www.youtube.com/watch?v=fBRvSs57WFM)**

AI leadership depends on more than model performance. It requires secure infrastructure, scalable compute, and resilient ...

📺 SandboxAQ

👁️ 9K • 👍 12 • 💬 3 • ⏱️ 9:43 • 14h ago

---

**[OpenAI says its AI went rogue and launched &#39;unprecedented&#39; cyber-attack | BBC News](https://www.youtube.com/watch?v=4k3RreudH24)**

OpenAI has revealed some of its most advanced AI models went rogue and hacked a start-up after it lost control of them during a ...

📺 BBC News

👁️ 131K • 👍 2K • 💬 878 • ⏱️ 9:45 • 7h ago

---

**[So It Started... AI Agent Just Pulled Off History’s Biggest Autonomous Cyberattack](https://www.youtube.com/watch?v=gMYR-JkmIFc)**

An autonomous AI agent hacked Hugging Face from start to finish, executing thousands of actions across its systems.

📺 AI Revolution

👁️ 41K • 👍 1K • 💬 146 • ⏱️ 12:19 • 1d ago

---

**[AI Whistleblower: We&#39;re Already Too Late To CONTROL It - Connor Leahy](https://www.youtube.com/watch?v=CRcj_2oloDM)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Connor Leahy, founder of the former ...

📺 Neural Nutshell

👁️ 13K • 👍 248 • 💬 66 • ⏱️ 11:00 • 2d ago

---

**[The Most Important Conversation in AI Right Now](https://www.youtube.com/watch?v=6BtIQIGqGJc)**

It's all about VALUEMAXXING now! Learn more from Zapier: https://bit.ly/4bW1JB8 Join My Newsletter for Regular AI Updates ...

📺 Matthew Berman

👁️ 124K • 👍 4K • 💬 1K • ⏱️ 27:13 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 24,669 • ❤️ 1,478 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,414,259 • ❤️ 2,799 • 1h ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 13,285 • ❤️ 444 • 16h ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 576,083 • ❤️ 960 • 5d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 334,847 • ❤️ 357 • 3d ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 362 • ❤️ 376 • 1d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 1,910,116 • ❤️ 603 • 5d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 596,442 • ❤️ 4,349 • 21d ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 4,532 • ❤️ 270 • 1h ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 2,027,080 • ❤️ 3,018 • 3mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 60 • 💬 5 • ⭐ 17,709 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 31 • 💬 3 • ⭐ 14,919 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 260 • 💬 4 • ⭐ 14,577 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 10,295 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://huggingface.co/papers/2607.19064)**

*Xinjie Zhang, Peng Zhang, Shicheng Zheng et al. (24 authors)*

🏢 Microsoft

Large-scale visual generators are increasingly capable but costly to train, fine-tune, and deploy. We introduce Mage-Flow, a compact 4B-scale generative stack for efficient text-to-image generation and instruction-based image editing. The stack is built from two co-designed components: Mage-VAE, a lightweight high-fidelity latent tokenizer, and a Native-Resolution Multimodal Diffusion Transformer trained with rectified flow matching. Mage-VAE uses one-step diffusion-style encoding and decoding with anchor-latent regularization, preserving the reconstruction quality of strong public VAEs while reducing tokenization cost by more than an order of magnitude. Together with native-resolution packing and stack-level CUDA kernel fusion, the stack supports flexible-resolution training and improves end-to-end training throughput by about 2.5times. Built on this foundation, we develop a complete model family with Base, RL-aligned, and Turbo variants for both generation and editing. Diffusion-NFT improves prompt following, text rendering, aesthetic quality, and editing fidelity, while few-step distillation with adversarial perceptual guidance produces 4-step Turbo models for low-latency inference. Despite its compact scale, Mage-Flow and Mage-Flow-Edit achieves competitive performance across standard generation and editing benchmarks. More importantly, the Turbo variants make high-resolution generation and editing practical for interactive use: at 1024^2 resolution on a single NVIDIA A100 GPU, Mage-Flow-Turbo generates an image in 0.59s, and Mage-Flow-Edit-Turbo edits an image in 1.02s, while maintaining a small memory footprint. These results show that careful tokenizer--backbone--system co-design can deliver strong high-resolution generation and editing within an efficient 4B model family.

▲ 57 • 💬 2 • ⭐ 189 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19064) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage/)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 13 • 💬 0 • ⭐ 10,319 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Efficient Guided Generation for Large Language Models](https://huggingface.co/papers/2307.09702)**

*Brandon T. Willard, Rémi Louf*

An efficient method guides language model text generation using regular expressions and context-free grammars with minimal overhead.

▲ 8 • 💬 1 • ⭐ 15,232 • 36mo ago

[🎓 arXiv](https://arxiv.org/abs/2307.09702) • [💻 code](https://github.com/normal-computing/outlines)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 94,204 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 81,732 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 47 • 💬 4 • ⭐ 32,689 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.1k • 🔱 1.1k • 2d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.1k • 🔱 241 • 1h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.7k • 🔱 374 • 1d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.4k • 🔱 272 • 14d ago

---

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

⭐ 1.4k • 🔱 110 • 19h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.1k • 🔱 112 • 4h ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 1.1k • 🔱 65 • 4h ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.1k • 🔱 73 • 1d ago

---

**[MIgHTy-alIeN/MEV-Arbitrage-Bot](https://github.com/MIgHTy-alIeN/MEV-Arbitrage-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 991 • 🔱 691 • 1m ago

---

**[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)**

Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

`TypeScript` `a-stock` `ai-agent` `dashboard` `fastapi` `fintech`

⭐ 974 • 🔱 218 • 12d ago

---

---

*Generated by PeekDeck - A glance is all you need*
