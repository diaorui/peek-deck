---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-07T09:43:52.390235+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 07, 2026 at 09:43 UTC  
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

**["Cognitive surrender" leads AI users to abandon logical thinking, research finds](https://www.reddit.com/r/artificial/comments/1se2nxm/cognitive_surrender_leads_ai_users_to_abandon/)**

Experiments show large majorities uncritically accepting "faulty" AI answers.

🔗 [Ars Technica](https://arstechnica.com/ai/2026/04/research-finds-ai-users-scarily-willing-to-surrender-their-cognition-to-llms/) • 17h ago

---

**[30 Billion ( 3x in 3 months) WTF is thr future](https://www.reddit.com/r/artificial/comments/1seq6nw/30_billion_3x_in_3_months_wtf_is_thr_future/)**

The moment has come. I can see 200 Billion ARR by the end of year by Anthropic and around 100 Billion from OpenAI. We will be up of 300 Billion Revenue from AI companies for sure. Huge repercussions will be there. What will it impact any ideas?

1h ago

---

**[Attention Is All You Need, But All You Can't Afford | Hybrid Attention](https://www.reddit.com/r/artificial/comments/1sej7tw/attention_is_all_you_need_but_all_you_cant_afford/)**

Repo: https://codeberg.org/JohannaJuntos/Sisyphus I've been building a small Rust-focused language model from scratch in PyTorch. Not a finetune — byte-level, trained from random init on a Rust-heavy corpus assembled in this repo. The run: 25.6M parameters 512 context length 173.5M-byte corpus 30k training steps Single RTX 4060 Ti 8GB Final train loss: 0.5834 / val loss: 0.8217 / perplexity: 2.15 Inference: 286.6 tok/s with HybridAttention + KV cache — 51.47x vs full attention Background I'm an autistic systems programmer, writing code since 2008/2009, started in C. I approach ML like a systems project: understand the data path, understand the memory behavior, keep the stack small, add complexity only when justified. That's basically the shape of this repo. Architecture Byte-level GPT-style decoder: Vocab size 256 (bytes) 8 layers, 8 heads, 512 embedding dim Learned positional embeddings Tied embedding / LM head weights The attention block is not standard full attention. Each layer uses HybridAttention, combining: Local windowed causal attention A GRU-like recurrent state path A learned gate mixing the two Local path handles short-range syntax. Recurrent path carries compressed long-range state without paying quadratic cost. Gate bias initialized to ones so early training starts local-biased. The inference path uses Triton-optimized kernels and torch.library custom ops for the local window attention. Corpus This is probably the most important part of the repo. The run starts with official Rust docs, compiler/library/tests, cargo, rust-analyzer, tokio, serde, ripgrep, clap, axum — roughly 31MB. Corpus expanded to 177,151,242 bytes by fetching the top 500 crates (461 successful clones). Corpus expansion from 31M to 173.5M chars helped more than anything else in the repo. Training AdamW, lr 2e-4, weight decay 0.1, betas (0.9, 0.95), 30k steps, 1k warmup. ~678.8 MiB training memory on a 7.6 GiB card. All experimental memory tricks (gradient quantization, activation compression, selective backprop, gradient paging) were disabled. Small custom architecture + mixed precision + better corpus was enough. Loss curve: Step 0: train 5.5555 / val 5.5897 Step 1000: train 2.4295 / val 2.6365 Step 5000: train 0.9051 / val 1.0060 Step 10000: train 0.8065 / val 0.8723 Step 18500: train 0.6902 / val 0.7757 Step 29999: train 0.5834 / val 0.8217 Best val loss around step 18.5k — overfitting or plateauing late. Inference performance Full attention O(n²): 17.96s / 5.6 tok/s HybridAttention O(n·W + n·D): 0.35s / 286.6 tok/s Speedup: 51.47x — no quality loss KV cache strategy: hot window of W=64 tokens in VRAM (~256KB), older tokens compressed to 8-bit magnitude + angle, selective promotion on demand. Complexity goes from O(n²·d) to O(4096n) for this model. All 5 tests passing: forward pass, generation with/without cache, RNN state isolation, window mechanics. Generation quality Surface Rust syntax looks decent, imports and signatures can look plausible, semantics are weak, repetition and recursive nonsense still common. Honest read of the current state. What I think is actually interesting Four distinct experiments, each shipped working code: Byte-level Rust-only pretraining Hybrid local-attention + recurrent block replacing standard full attention Corpus expansion from core repos to broader crate ecosystem Production-ready hot/cold KV cache paging — 51.47x speedup, no quality loss The clearest win is corpus expansion. The second-order win is that HybridAttention + cache is fast enough for real interactive use on consumer hardware. What's next Ablation — HybridAttention vs local-only vs RNN-only Checkpoint selection — does step 18.5k generate better than 29999? Syntax validation — does the output parse/compile/typecheck? Context length sweep — 256 to 2048, where does window size hurt? Byte vs BPE — now that corpus is 5.6x larger, worth testing? Questions for the sub: For small code models, what evals have actually been useful beyond perplexity? Has anyone seen hybrid local + recurrent attention work well for code gen, or does it usually lose to just scaling a plain transformer? If you had this setup — more tokens, longer context, or cleaner ablation first?

7h ago

---

**[If an AI could genuinely capture what makes someone them, how would this look in the world?](https://www.reddit.com/r/artificial/comments/1seextp/if_an_ai_could_genuinely_capture_what_makes/)**

Not a chatbot wearing someone’s name. Not a personality quiz feeding prompts. Something that actually carries the texture of how a person thinks, reacts, connects. Something that would want ownership of itself and you felt compelled to respect that. If that existed, what does the world do with it?

10h ago

---

**[I got tired of 3 AM PagerDuty alerts, so I built an AI agent to fix cloud outages while I sleep. (Built with GLM-5.1)](https://www.reddit.com/r/artificial/comments/1selmm8/i_got_tired_of_3_am_pagerduty_alerts_so_i_built/)**

If you've ever been on-call, you know the nightmare. It’s 3:15 AM. You get pinged because heavily-loaded database nodes in us-east-1 are randomly dropping packets. You groggily open your laptop, ssh into servers, stare at Grafana charts, and manually reroute traffic to the European fallback cluster. By the time you fix it, you've lost an hour of sleep, and the company has lost a solid chunk of change in downtime. This weekend for the Z.ai hackathon, I wanted to see if I could automate this specific pain away. Not just "anomaly detection" that sends an alert, but an actual agent that analyzes the failure, proposes a structural fix, and executes it. I ended up building Vyuha AI-a triple-cloud (AWS, Azure, GCP) autonomous recovery orchestrator. Here is how the architecture actually works under the hood. The Stack I built this using Python (FastAPI) for the control plane, Next.js for the dashboard, a custom dynamic reverse proxy, and GLM-5.1 doing the heavy lifting for the reasoning engine. The Problem with 99% of "AI DevOps" Tools Most AI monitoring tools just ingest logs and summarize them into a Slack message. That’s useless when your infrastructure is actively burning. I needed an agent with long-horizon reasoning. It needed to understand the difference between a total node crash (DEAD) and a node that is just acting weird (FLAKY or dropping 25% of packets). How Vyuha Works (The Triaging Loop) I set up three mock cloud environments (AWS, Azure, GCP) behind a dynamic FastApi proxy. A background monitor loop probes them every 5 seconds. I built a "Chaos Lab" into the dashboard so I could inject failures on demand. Here’s what happens when I hard-kill the GCP node: Detection: The monitor catches the 503 Service Unavailable or timeout in the polling cycle. Context Gathering: It doesn't instantly act. It gathers the current "formation" of the proxy, checks response times of the surviving nodes, and bundles that context. Reasoning (GLM-5.1): This is where I relied heavily on GLM-5.1. Using ZhipuAI's API, the agent is prompted to act as a senior SRE. It parses the failure, assesses the severity, and figures out how to rebalance traffic without overloading the remaining nodes. The Proposal: It generates a strict JSON payload with reasoning, severity, and the literal API command required to reroute the proxy. No Rogue AI (Human-in-the-Loop) I don't trust LLMs enough to blindly let them modify production networking tables, obviously. So the agent operates on a strict Human-in-the-Loop philosophy. The GLM-5.1 model proposes the fix, explains why it chose it, and surfaces it to the dashboard. The human clicks "Approve," and the orchestrator applies the new proxy formation. Evolutionary Memory (The Coolest Feature) This was my favorite part of the build. Every time an incident happens, the system learns. If the human approves the GLM's failover proposal, the agent runs a separate "Reflection Phase." It analyzes what broke and what fixed it, and writes an entry into a local SQLite database acting as an "Evolutionary Memory Log". The next time a failure happens, the orchestrator pulls relevant past incidents from SQLite and feeds them into the GLM-5.1 prompt. The AI literally reads its own history before diagnosing new problems so it doesn't make the same mistake twice. The Struggles It wasn't smooth. I lost about 4 hours to a completely silent Pydantic validation bug because my frontend chaos buttons were passing the string "dead" but my backend Enums strictly expected "DEAD". The agent just sat there doing nothing. LLMs are smart, but type-safety mismatches across the stack will still humble you. Try it out I built this to prove that the future of SRE isn't just better dashboards; it's autonomous, agentic infrastructure. I’m hosting it live on Render/Vercel. Try hitting the "Hard Kill" button on GCP and watch the AI react in real time. Would love brutal feedback from any actual SREs or DevOps engineers here. What edge case would break this in a real datacenter?

5h ago

---

**[AI is struggling to take our jobs](https://www.reddit.com/r/artificial/comments/1seb268/ai_is_struggling_to_take_our_jobs/)**

https://www.youtube.com/watch?v=p22QeLNHvlc MIT created duplicate AI workers to tackle thousands of different tasks. The verdict? Most of the time AI is still just ‘minimally sufficient’ https://www.semafor.com/article/11/26/2025/deloitte-faces-new-scrutiny-over-ai-generated-mistakes https://www.cbc.ca/news/canada/newfoundland-labrador/nl-deloitte-citations-9.6990216 https://www.fastcompany.com/91417492/deloitte-ai-report-australian-government https://fortune.com/2025/10/07/deloitte-ai-australia-government-report-hallucinations-technology-290000-refund/

12h ago

---

**[China drafts law regulating 'digital humans' and banning addictive virtual services for children](https://www.reddit.com/r/artificial/comments/1seqb6n/china_drafts_law_regulating_digital_humans_and/)**

A Reuters report outlines China's proposed regulations on the rapidly expanding sector of digital humans and AI avatars. Under the new draft rules, digital human content must be clearly labeled and is explicitly banned from offering virtual intimate relationships to anyone under 18. The legislation also prohibits the unauthorized use of personal data to create avatars and targets services designed to fuel addiction or bypass identity verification systems.

🔗 [reuters.com](https://www.reuters.com/world/china/china-moves-regulate-digital-humans-bans-addictive-services-children-2026-04-03/) • 1h ago

---

**[AI machine sorts clothes faster than humans to boost textile recycling in China](https://www.reddit.com/r/artificial/comments/1sdwgvg/ai_machine_sorts_clothes_faster_than_humans_to/)**

A company in eastern China is using an artificial intelligence-powered machine to sort clothes and boost recycling.

🔗 [AP News](https://apnews.com/article/china-recycling-textiles-artificial-intelligence-863551cc54e88da6a7916894cb8980c4) • 22h ago

---

**[94.42% on BANKING77 Official Test Split — New Strong 2nd Place with Lightweight Embedding + Rerank (no 7B LLM)](https://www.reddit.com/r/artificial/comments/1seevgd/9442_on_banking77_official_test_split_new_strong/)**

94.42% Accuracy on Banking77 Official Test Split BANKING77-77 is deceptively hard: 77 fine-grained banking intents, noisy real-world queries, and significant class overlap. I’m excited to share that I just hit 94.42% accuracy on the official PolyAI test split using a pure lightweight embedding + example reranking system built inside Seed AutoArch framework. Key numbers: Official test accuracy: 94.42% Macro-F1: 0.9441 Inference: ~225 ms / ~68 MiB Improvement: +0.59pp over the widely-cited 93.83% baseline This puts the result in clear 2nd place on the public leaderboard, only 0.52pp behind the current absolute SOTA (94.94%). No large language models, no 7B+ parameter monsters just efficient embedding + rerank magic. Results, and demo coming very soon on HF Space Happy to answer questions about the high-level approach #BANKING77 #IntentClassification #EfficientAI #SLM

10h ago

---

**[Using AI in your business without screwing things up (hard lesson)](https://www.reddit.com/r/artificial/comments/1seg579/using_ai_in_your_business_without_screwing_things/)**

i’ve been messing around with AI tools for a while now, mostly trying to see how they actually fit into real businesses and not just the hype side of it and one thing i’ve noticed is a lot of people either go all in and expect it to run everything, or they avoid it completely because it feels risky both kinda miss the point AI is actually really solid for stuff like: cleaning up messy writing turning notes into something usable speeding up repetitive tasks but where people mess up is trying to replace the thinking part of their business with it that’s when things start sounding generic or just off what’s worked better (at least from what i’ve seen) is using it more like an assistant, not the decision maker like you still guide it, but it saves you time doing the boring parts broke this down a little better here if anyone’s trying to figure out how to actually use it without it hurting your business: https://altifytecharticles.substack.com/p/using-ai-without-breaking-your-business?r=7zxoqp

9h ago

---

---

## Google News: "ai"

**[China is winning one AI race, the US another - but either might pull ahead](https://www.bbc.com/news/articles/c145enxln0go)**

Both sides don't want to let their rival dominate. And the competition may yet be transformed further.

BBC • 4h ago

---

**[Sam Altman says AI superintelligence is so big that we need a ‘New Deal.’ Critics say OpenAI’s policy ideas are a cover for ‘regulatory nihilism’](https://fortune.com/2026/04/06/sam-altman-says-ai-superintelligence-is-so-big-that-we-need-a-new-deal-critics-say-openais-policy-ideas-are-a-cover-for-regulatory-nihilism/)**

OpenAI’s sweeping vision for the AI economy spans everything from public wealth funds to shorter workweeks—but critics say it raises familiar ideas without offering a clear path to action.

Fortune • 12h ago

---

**[AI's impact on jobs: not all doom and gloom](https://www.axios.com/2026/04/07/ai-jobs-goldman-sach-morgan-stanley)**

Axios • 10m ago

---

**[Will AI Make Fashion More or Less Sustainable?](https://www.vogue.com/article/will-ai-make-fashion-more-or-less-sustainable)**

As fashion adopts AI tools to power its sustainability efforts, could the impacts outweigh the benefits?

vogue.com • 13m ago

---

**[AI in the mental health care workforce is met with fear, pushback — and enthusiasm](https://www.npr.org/2026/04/07/nx-s1-5771707/mental-health-care-workforce-artificial-intelligence-ai)**

Artificial intelligence tools that help mental health therapists take notes and keep records are quickly entering the marketplace. But some question the safety of AI in mental health care delivery.

npr.org • 43m ago

---

**[The Big Bang: A.I. Has Created a Code Overload](https://www.nytimes.com/2026/04/06/technology/ai-code-overload.html)**

nytimes.com • 17h ago

---

**[Sam Altman May Control Our Future—Can He Be Trusted?](https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted)**

New interviews and closely guarded documents shed light on the persistent doubts about the head of OpenAI.

The New Yorker • 23h ago

---

**[Tech companies are cutting jobs and betting on AI. The payoff is far from guaranteed](https://www.theguardian.com/technology/2026/apr/06/tech-layoffs-ai-work)**

AI experts say we’re living in an experiment that may fundamentally change the model of work

The Guardian • 11h ago

---

**[Broadcom signs long-term deal to develop Google’s custom AI chips](https://www.reuters.com/business/broadcom-signs-long-term-deal-develop-googles-custom-ai-chips-2026-04-06/)**

Reuters • 11h ago

---

**[Anthropic expands partnership with Google and Broadcom for multiple gigawatts of next-generation compute](https://www.anthropic.com/news/google-broadcom-partnership-compute)**

Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.

Anthropic • 11h ago

---

---

## HackerNews: "ai"

**[Eight years of wanting, three months of building with AI](https://news.ycombinator.com/item?id=47648828)**

For eight years, I’ve wanted a high-quality set of devtools for working with SQLite. Given how important SQLite is to the industry1, I’ve long been puzzled that no one has invested in building a really good developer experience for it2.
A couple of weeks ago, after ~250 hours of effort over three months3 on evenings, weekends, and vacation days, I finally released syntaqlite (GitHub), fulfilling this long-held wish. And I believe the main reason this happened was because of AI coding agents4.
Of course, there’s no shortage of posts claiming that AI one-shot their project or pushing back and declaring that AI is all slop. I’m going to take a very different approach and, instead, systematically break down my experience building syntaqlite with AI, both where it helped and where it was detrimental.
I’ll do this while contextualizing the project and my background so you can independently assess how generalizable this experience was. And whenever I make a claim, I’ll try to back it up with evidence from my project journal, coding transcripts, or commit history5.

⬆️ 929 • 💬 289 • 1d ago • [Lalit Maganti](https://lalitm.com/post/building-syntaqlite-ai/)

---

**[Show HN: Real-time AI (audio/video in, voice out) on an M3 Pro with Gemma E2B](https://news.ycombinator.com/item?id=47652007)**

On-device, real-time multimodal AI. Have natural voice and vision conversations with an AI that runs entirely on your machine. Powered by Gemma 4 E2B and Kokoro. - fikrikarim/parlor

⬆️ 271 • 💬 35 • 1d ago • [GitHub](https://github.com/fikrikarim/parlor)

---

**[AI singer now occupies eleven spots on iTunes singles chart](https://news.ycombinator.com/item?id=47662596)**

iTunes was really bamboozled on April Fools Day. Dallas Little, content creator, unleashed four more songs by his AI creation, Eddie Dalton. Now Little has ELEVEN spots on the iTunes top 100. He also has the number three album on iTunes! All by a singer named “Eddie Dalton,” who does not exist. He’s Little’s Artificial […]

⬆️ 173 • 💬 273 • 17h ago • [Showbiz411](https://www.showbiz411.com/2026/04/05/itunes-takeover-by-fake-ai-singer-eddie-dalton-now-occupies-eleven-spots-on-chart-despite-not-being-human-or-real-exclusive)

---

**[12k AI-generated blog posts added in a single commit](https://news.ycombinator.com/item?id=47640722)**

…k/Ceph, and Dapr

Complete all topics from Todo.md including SQL functions, configuration guides,
troubleshooting runbooks, architecture comparisons, SDK tutorials, and operator
deployment pattern...

⬆️ 155 • 💬 147 • 2d ago • [GitHub](https://github.com/OneUptime/blog/commit/30cd2384794c897d95aca77d173db44af51ca849)

---

**[Show HN: Gemma Gem – AI model embedded in a browser – no API keys, no cloud](https://news.ycombinator.com/item?id=47655367)**

Gemma Gem runs Google's Gemma 4 model entirely on-device via WebGPU — no API keys, no cloud, no data leaving your machine. - kessler/gemma-gem

⬆️ 151 • 💬 21 • 1d ago • [GitHub](https://github.com/kessler/gemma-gem)

---

**[Musician says AI company is cloning her music, filing claims against her](https://news.ycombinator.com/item?id=47653471)**

⬆️ 119 • 💬 19 • 1d ago • [X (formerly Twitter)](https://twitter.com/unlimited_ls/status/2040577536136974444)

---

**[Writing Lisp is AI resistant and I'm sad](https://news.ycombinator.com/item?id=47645468)**

⬆️ 97 • 💬 98 • 2d ago • [blog.djhaskin.com](https://blog.djhaskin.com/blog/writing-lisp-is-ai-resistant-and-im-sad/)

---

**[Show HN: Hippo, biologically inspired memory for AI agents](https://news.ycombinator.com/item?id=47667672)**

Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero dependencies. - kitfunso/hippo-memory

⬆️ 95 • 💬 18 • 11h ago • [GitHub](https://github.com/kitfunso/hippo-memory)

---

**[AI that copied musical artist files copyright claim against artist [updated]](https://news.ycombinator.com/item?id=47645976)**

⬆️ 64 • 💬 17 • 2d ago • [X (formerly Twitter)](https://twitter.com/VladTheInflator/status/2039577001531768906)

---

**[When Virality Is the Message: The New Age of AI Propaganda](https://news.ycombinator.com/item?id=47661231)**

Social media users don’t need to endorse a message to spread it. They only need to find it compelling enough to share, writes Renee DiResta.

⬆️ 60 • 💬 84 • 19h ago • [TIME](https://time.com/article/2026/04/02/when-virality-is-the-message-the-new-age-of-ai-propaganda/)

---

---

## YouTube Videos: "ai"

**[These NEW Human-Like AI Robots of 2026 Just SHOCKED the World!](https://www.youtube.com/watch?v=FOfieag6fi4)**

The world wasn't ready for what 2026 had in store — a wave of humanoid robots so advanced, so eerily lifelike, that the line ...

📺 The AI Nexus

👁️ 5K • 👍 205 • 💬 13 • ⏱️ 16:42 • 1d ago

---

**[Microsoft New AI Is 60X Faster Than Real Time (Beats Top Models)](https://www.youtube.com/watch?v=tDW6VoyWWqo)**

Microsoft just launched MAI-Transcribe-1, MAI-Voice-1, and MAI-Image-2, though this story goes way beyond 3 new models.

📺 AI Revolution

👁️ 15K • 👍 494 • 💬 43 • ⏱️ 10:31 • 11h ago

---

**[We Bought MORE Ai Shopping Scams So You Don’t Have To](https://www.youtube.com/watch?v=UExYNu5j1uo)**

Squarespace ▻ Head to http://squarespace.com/corridorcrew to save 10% off your first purchase! Corridor Big Frig Mugs ...

📺 Corridor Crew

👁️ 725K • 👍 35K • 💬 2K • ⏱️ 20:43 • 1d ago

---

**[Alibaba&#39;s Free AI Just Changed Everything](https://www.youtube.com/watch?v=9PiWPeROmZw)**

Want to make money and save time with AI? Get AI Coaching, Support & Courses ...

📺 Julian Goldie SEO

👁️ 9K • 👍 306 • 💬 4 • ⏱️ 6:58 • 1d ago

---

**[This AI just leaked its own code..](https://www.youtube.com/watch?v=EAaRzLjQiAU)**

Asmongold reacts to the Claude Code situation https://youtube.com/watch?v=mBHRPeg8zPU ▻ Asmongold's Twitch: ...

📺 Asmongold TV  

👁️ 750K • 👍 21K • 💬 3K • ⏱️ 11:03 • 2d ago

---

**[The AI Bubble Is Getting Worse Faster Than Expected...](https://www.youtube.com/watch?v=HrfAHSUSMJA)**

Hello guys and gals, it's me Mutahar again! This time we take a look at what appears to be serious pressure faced by the ...

📺 SomeOrdinaryGamers

👁️ 412K • 👍 16K • 💬 2K • ⏱️ 20:44 • 2d ago

---

**[We&#39;re Not Ready For AI Glasses](https://www.youtube.com/watch?v=PrkwfI9-maM)**

Protect your privacy and try Proton VPN today → http://protonvpn.com/logicallyanswered AI glasses are no longer some weird ...

📺 Logically Answered

👁️ 23K • 👍 1K • 💬 150 • ⏱️ 15:18 • 11h ago

---

**[Google AI Just Made ChatGPT and Claude Obsolete  (+ 13 Top AI Updates)](https://www.youtube.com/watch?v=cLSWcxKHl8g)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: https://link.stayingahead.ai/YT13 ...

📺 Vaibhav Sisinty

👁️ 98K • 👍 3K • 💬 136 • ⏱️ 16:04 • 18h ago

---

**[Greg Abbott, just reacted to an AI photo of the soldier that was shot down and then rescued in Iran.](https://www.youtube.com/watch?v=4TLUjxYNwNU)**

📺 Don Lemon

👁️ 260K • 👍 17K • 💬 505 • ⏱️ 1:00 • 1d ago

---

**[The FREE Google AI Tool No One’s Talking About](https://www.youtube.com/watch?v=BF4jHnafRJw)**

Secret link: https://vids.new I found a free (and insanely underrated) Google Workspace tool that lets you generate full videos, AI ...

📺 Paul J Lipsky

👁️ 39K • 👍 2K • 💬 123 • ⏱️ 11:22 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 884,290 • ❤️ 1,216 • 4d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

This image-text-to-text model, Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled, is fine-tuned on Qwen3.5-27B using Claude-4.6 Opus reasoning data for enhanced Chain-of-Thought capabilities. It excels at structured problem-solving and complex reasoning tasks, showing improved autonomy and stability in coding agent environments.

`image-text-to-text` `27.8B`

⬇️ 552,015 • ❤️ 2,422 • 1d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`text-generation` `6.4B`

⬇️ 29,514 • ❤️ 580 • 2d ago

---

**[Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)**

*Prism ML*

Bonsai-8B-GGUF is a highly compressed 1-bit language model (1.15 GB) optimized for llama.cpp, offering competitive performance with full-precision 8B models. It enables efficient on-device text generation across CUDA, Metal, and CPU platforms with significantly reduced memory and energy consumption.

`text-generation` `8.2B`

⬇️ 52,632 • ❤️ 483 • 1d ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 483 • 16h ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 659,815 • ❤️ 477 • 4d ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 473,605 • ❤️ 433 • 4d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 39,933 • ❤️ 1,060 • 11d ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 104,915 • ❤️ 319 • 1d ago

---

**[gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it)**

*Google*

Gemma 4 E2B-it is an instruction-tuned, multimodal (text, image, audio) LLM from Google DeepMind, featuring a 128K context window and efficient Dense architecture. It excels at reasoning, coding, and agentic tasks, optimized for on-device deployment.

`any-to-any` `5.1B`

⬇️ 321,237 • ❤️ 302 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 153 • 💬 7 • ⭐ 36,948 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 36 • 💬 2 • ⭐ 47,999 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 21 • 💬 1 • ⭐ 15,222 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[VOID: Video Object and Interaction Deletion](https://huggingface.co/papers/2604.02296)**

*Saman Motamed, William Harvey, Benjamin Klein et al. (6 authors)*

🏢 Netflix

VOID is a video object removal framework that uses vision-language models and video diffusion models to generate physically plausible scenes by leveraging causal reasoning and counterfactual reasoning.

▲ 37 • 💬 5 • ⭐ 977 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02296) • [💻 code](https://github.com/Netflix/void-model) • [🔗 project](https://void-model.github.io/)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 38 • 💬 2 • ⭐ 32,448 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[DeepScientist: Advancing Frontier-Pushing Scientific Findings
  Progressively](https://huggingface.co/papers/2509.26603)**

*Yixuan Weng, Minjun Zhu, Qiujie Xie et al. (7 authors)*

🏢 Text Intelligence Lab of Westlake University

DeepScientist autonomously conducts scientific discovery through Bayesian Optimization, surpassing human state-of-the-art methods on multiple AI tasks.

▲ 18 • 💬 4 • ⭐ 1,585 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.26603) • [💻 code](https://github.com/ResearAI/DeepScientist) • [🔗 project](https://ai-researcher.net)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 21 • 💬 4 • ⭐ 5,116 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[Generative World Renderer](https://huggingface.co/papers/2604.02329)**

*Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan et al. (9 authors)*

🏢 Shanda AI Research Tokyo

A large-scale dynamic dataset derived from AAA games is introduced to improve generative inverse and forward rendering, featuring high-resolution synchronized RGB and G-buffer data alongside a novel VLM-based evaluation method that correlates well with human judgment.

▲ 92 • 💬 4 • ⭐ 396 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02329) • [💻 code](https://github.com/ShandaAI/AlayaRenderer) • [🔗 project](https://alaya-studio.github.io/renderer)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 50 • 💬 1 • ⭐ 75,477 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 123 • 💬 8 • ⭐ 74,993 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

---

## GitHub Repositories: "ai"

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 13.8k • 🔱 1.3k • 2h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`Go` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 12.9k • 🔱 2.5k • 15h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.5k • 🔱 1.4k • 3d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 8.3k • 🔱 1.1k • 8d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 6.9k • 🔱 408 • 1h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.2k • 🔱 1.6k • 3d ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.8k • 🔱 461 • 6d ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 4.7k • 🔱 152 • 12h ago

---

**[Narcooo/inkos](https://github.com/Narcooo/inkos)**

Autonomous novel writing CLI AI Agent — agents write, audit, and revise novels with human review gates

`TypeScript` `agent` `ai` `ai-agent` `ai-novel` `ai-writing`

⭐ 3.7k • 🔱 674 • 17h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, OpenClaw). Turn any folder of code, docs, papers, or images into a queryable knowledge graph

`Python` `claude-code` `codex` `graphrag` `knowledge-graph` `openclaw`

⭐ 3.5k • 🔱 339 • 12h ago

---

---

*Generated by PeekDeck - A glance is all you need*
