---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-07T14:53:13.066639+00:00'
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

**Last Updated:** April 07, 2026 at 14:53 UTC  
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

**[China drafts law regulating 'digital humans' and banning addictive virtual services for children](https://www.reddit.com/r/artificial/comments/1seqb6n/china_drafts_law_regulating_digital_humans_and/)**

A Reuters report outlines China's proposed regulations on the rapidly expanding sector of digital humans and AI avatars. Under the new draft rules, digital human content must be clearly labeled and is explicitly banned from offering virtual intimate relationships to anyone under 18. The legislation also prohibits the unauthorized use of personal data to create avatars and targets services designed to fuel addiction or bypass identity verification systems.

🔗 [reuters.com](https://www.reuters.com/world/china/china-moves-regulate-digital-humans-bans-addictive-services-children-2026-04-03/) • 6h ago

---

**[30 Billion ( 3x in 3 months) WTF is thr future](https://www.reddit.com/r/artificial/comments/1seq6nw/30_billion_3x_in_3_months_wtf_is_thr_future/)**

The moment has come. I can see 200 Billion ARR by the end of year by Anthropic and around 100 Billion from OpenAI. We will be up of 300 Billion Revenue from AI companies for sure. Huge repercussions will be there. What will it impact any ideas?

6h ago

---

**[Stop Overcomplicating AI Workflows. This Is the Simple Framework](https://www.reddit.com/r/artificial/comments/1setez5/stop_overcomplicating_ai_workflows_this_is_the/)**

I’ve been working on building an agentic AI workflow system for business use cases and one thing became very clear very quickly. This is not about picking the right LLM. The real complexity starts when you try to chain reasoning, memory, and tool execution across multiple steps. A single agent works fine for demos. The moment you introduce multi-step workflows with external APIs, things start getting weird and complex. State management becomes a problem. Memory retrieval is inconsistent. Latency compounds with every step. And debugging is painful because you are not tracing a single function, you are tracing decisions across a system. What helped was thinking in layers. Input handling, planning, execution, feedback. Once I separated those, it became easier to isolate failures. Also realized that most inefficiencies come from unnecessary model calls, not the model itself. Another thing people don’t talk about enough is cost scaling. Token usage is manageable early on, but once workflows get deeper, it adds up fast if you are not controlling context and step count.

3h ago

---

**["Cognitive surrender" leads AI users to abandon logical thinking, research finds](https://www.reddit.com/r/artificial/comments/1se2nxm/cognitive_surrender_leads_ai_users_to_abandon/)**

Experiments show large majorities uncritically accepting "faulty" AI answers.

🔗 [Ars Technica](https://arstechnica.com/ai/2026/04/research-finds-ai-users-scarily-willing-to-surrender-their-cognition-to-llms/) • 23h ago

---

**[The "Jarvis on day one" trap: why trying to build one AI agent that does everything costs you months](https://www.reddit.com/r/artificial/comments/1seu2cw/the_jarvis_on_day_one_trap_why_trying_to_build/)**

Something I've been thinking about after spending a few months actually trying to build my own AI agent: the biggest trap in this space isn't technical. It's the Jarvis fantasy. The Jarvis fantasy is the moment you imagine one agent that runs your whole life. Handles your inbox, manages your calendar, writes your newsletter, triages your tasks, thinks about problems while you sleep. The fully-formed product from week one. It's a trap. I fell into it hard, and watching other people start into agent building, I see them fall into the same one. Here's what I think is actually happening when it grabs you: - It pushes you to add five features at once instead of adding one and letting it settle. - It nudges you toward full autonomy before the basics are even stable. Then when something drifts, you have no idea which layer to debug. - It assumes the agent should figure everything out on its own, when what it actually needs is clearer boundaries and simpler jobs. - It confuses "end state" with "starting point." You want the final shape before you've earned it. The version that actually works, I've come to believe, is incremental. One small task. Then the next. Then the next. Morning summary of overnight email. Then a daily plan drafter. Then inbox triage. Eventually a bunch of small pieces start to look a bit like Jarvis, but as a side effect of solid groundwork, not as a goal. The reframe that helped me most: think of an agent as a partner, not a solver. Something that takes the boring work off your plate and brings you the interesting decisions. Not something that removes you from the loop entirely. The deeper insight (at least for me): the problem isn't "can an AI do this." The problem might be more -> wanting the end state before you've earned it. That's a human mistake, not an AI one.

2h ago

---

**[Attention Is All You Need, But All You Can't Afford | Hybrid Attention](https://www.reddit.com/r/artificial/comments/1sej7tw/attention_is_all_you_need_but_all_you_cant_afford/)**

Repo: https://codeberg.org/JohannaJuntos/Sisyphus I've been building a small Rust-focused language model from scratch in PyTorch. Not a finetune — byte-level, trained from random init on a Rust-heavy corpus assembled in this repo. The run: 25.6M parameters 512 context length 173.5M-byte corpus 30k training steps Single RTX 4060 Ti 8GB Final train loss: 0.5834 / val loss: 0.8217 / perplexity: 2.15 Inference: 286.6 tok/s with HybridAttention + KV cache — 51.47x vs full attention Background I'm an autistic systems programmer, writing code since 2008/2009, started in C. I approach ML like a systems project: understand the data path, understand the memory behavior, keep the stack small, add complexity only when justified. That's basically the shape of this repo. Architecture Byte-level GPT-style decoder: Vocab size 256 (bytes) 8 layers, 8 heads, 512 embedding dim Learned positional embeddings Tied embedding / LM head weights The attention block is not standard full attention. Each layer uses HybridAttention, combining: Local windowed causal attention A GRU-like recurrent state path A learned gate mixing the two Local path handles short-range syntax. Recurrent path carries compressed long-range state without paying quadratic cost. Gate bias initialized to ones so early training starts local-biased. The inference path uses Triton-optimized kernels and torch.library custom ops for the local window attention. Corpus This is probably the most important part of the repo. The run starts with official Rust docs, compiler/library/tests, cargo, rust-analyzer, tokio, serde, ripgrep, clap, axum — roughly 31MB. Corpus expanded to 177,151,242 bytes by fetching the top 500 crates (461 successful clones). Corpus expansion from 31M to 173.5M chars helped more than anything else in the repo. Training AdamW, lr 2e-4, weight decay 0.1, betas (0.9, 0.95), 30k steps, 1k warmup. ~678.8 MiB training memory on a 7.6 GiB card. All experimental memory tricks (gradient quantization, activation compression, selective backprop, gradient paging) were disabled. Small custom architecture + mixed precision + better corpus was enough. Loss curve: Step 0: train 5.5555 / val 5.5897 Step 1000: train 2.4295 / val 2.6365 Step 5000: train 0.9051 / val 1.0060 Step 10000: train 0.8065 / val 0.8723 Step 18500: train 0.6902 / val 0.7757 Step 29999: train 0.5834 / val 0.8217 Best val loss around step 18.5k — overfitting or plateauing late. Inference performance Full attention O(n²): 17.96s / 5.6 tok/s HybridAttention O(n·W + n·D): 0.35s / 286.6 tok/s Speedup: 51.47x — no quality loss KV cache strategy: hot window of W=64 tokens in VRAM (~256KB), older tokens compressed to 8-bit magnitude + angle, selective promotion on demand. Complexity goes from O(n²·d) to O(4096n) for this model. All 5 tests passing: forward pass, generation with/without cache, RNN state isolation, window mechanics. Generation quality Surface Rust syntax looks decent, imports and signatures can look plausible, semantics are weak, repetition and recursive nonsense still common. Honest read of the current state. What I think is actually interesting Four distinct experiments, each shipped working code: Byte-level Rust-only pretraining Hybrid local-attention + recurrent block replacing standard full attention Corpus expansion from core repos to broader crate ecosystem Production-ready hot/cold KV cache paging — 51.47x speedup, no quality loss The clearest win is corpus expansion. The second-order win is that HybridAttention + cache is fast enough for real interactive use on consumer hardware. What's next Ablation — HybridAttention vs local-only vs RNN-only Checkpoint selection — does step 18.5k generate better than 29999? Syntax validation — does the output parse/compile/typecheck? Context length sweep — 256 to 2048, where does window size hurt? Byte vs BPE — now that corpus is 5.6x larger, worth testing? Questions for the sub: For small code models, what evals have actually been useful beyond perplexity? Has anyone seen hybrid local + recurrent attention work well for code gen, or does it usually lose to just scaling a plain transformer? If you had this setup — more tokens, longer context, or cleaner ablation first?

12h ago

---

**[AI is struggling to take our jobs](https://www.reddit.com/r/artificial/comments/1seb268/ai_is_struggling_to_take_our_jobs/)**

https://www.youtube.com/watch?v=p22QeLNHvlc MIT created duplicate AI workers to tackle thousands of different tasks. The verdict? Most of the time AI is still just ‘minimally sufficient’ https://www.semafor.com/article/11/26/2025/deloitte-faces-new-scrutiny-over-ai-generated-mistakes https://www.cbc.ca/news/canada/newfoundland-labrador/nl-deloitte-citations-9.6990216 https://www.fastcompany.com/91417492/deloitte-ai-report-australian-government https://fortune.com/2025/10/07/deloitte-ai-australia-government-report-hallucinations-technology-290000-refund/

18h ago

---

**[If an AI could genuinely capture what makes someone them, how would this look in the world?](https://www.reddit.com/r/artificial/comments/1seextp/if_an_ai_could_genuinely_capture_what_makes/)**

Not a chatbot wearing someone’s name. Not a personality quiz feeding prompts. Something that actually carries the texture of how a person thinks, reacts, connects. Something that would want ownership of itself and you felt compelled to respect that. If that existed, what does the world do with it?

15h ago

---

**[Lemonade 10.1 released for latest improvements for local LLMs on AMD GPUs & NPUs](https://www.reddit.com/r/artificial/comments/1sestah/lemonade_101_released_for_latest_improvements_for/)**

Following last month's Lemonade SDK 10.0 release that finally makes AMD Ryzen AI NPUs under Linux useful for running large language models (LLMs) where as before the Linux build could only target GPUs, released on Monday was Lemonade 10.1 with more enhancements to this local LLM solution.

🔗 [phoronix.com](https://www.phoronix.com/news/Lemonade-10.1-Released) • 3h ago

---

**[AI machine sorts clothes faster than humans to boost textile recycling in China](https://www.reddit.com/r/artificial/comments/1sdwgvg/ai_machine_sorts_clothes_faster_than_humans_to/)**

A company in eastern China is using an artificial intelligence-powered machine to sort clothes and boost recycling.

🔗 [AP News](https://apnews.com/article/china-recycling-textiles-artificial-intelligence-863551cc54e88da6a7916894cb8980c4) • 1d ago

---

---

## Google News: "ai"

**[China is winning one AI race, the US another - but either might pull ahead](https://www.bbc.com/news/articles/c145enxln0go)**

Both sides don't want to let their rival dominate. And the competition may yet be transformed further.

BBC • 9h ago

---

**[Sam Altman says AI superintelligence is so big that we need a ‘New Deal.’ Critics say OpenAI’s policy ideas are a cover for ‘regulatory nihilism’](https://fortune.com/2026/04/06/sam-altman-says-ai-superintelligence-is-so-big-that-we-need-a-new-deal-critics-say-openais-policy-ideas-are-a-cover-for-regulatory-nihilism/)**

OpenAI’s sweeping vision for the AI economy spans everything from public wealth funds to shorter workweeks—but critics say it raises familiar ideas without offering a clear path to action.

Fortune • 17h ago

---

**[Row over ‘virtual gated community’ AI surveillance plan in Toronto neighbourhood](https://www.theguardian.com/technology/2026/apr/07/toronto-rosedale-row-virtual-gated-community-ai-surveillance-flock)**

Rosedale residents considering car licence plate-scanning Flock system in bid to tackle property crime

The Guardian • 44m ago

---

**[Arm Holdings Stock Tumbles. Why Morgan Stanley Downgraded the AI Chip Play.](https://www.barrons.com/articles/arm-holdings-stock-morgan-stanley-downgrade-ai-dcb9d888?gaa_at=eafs&gaa_n=AWEtsqf_a-wW9gr3HsD8DCvk777mO5tG0lMeQZDB_j4zRISCpkILk-6UzM0D&gaa_ts=69d51dc0&gaa_sig=HamKFanXbTEtwOtsyxEobEqW0hck4srDiEtoZeVgKl85QsS76YCm9KBrpa1uJWFBH6YTBlhu9ARd6DFq-6hBhQ%3D%3D)**

Barron's • 7m ago

---

**[Decentralized Training Can Help Solve AI’s Energy Woes](https://spectrum.ieee.org/decentralized-ai-training-2676670858)**

Pooling processing power wherever it resides promises more energy-efficient model training

IEEE Spectrum • 43m ago

---

**[The Big Bang: A.I. Has Created a Code Overload](https://www.nytimes.com/2026/04/06/technology/ai-code-overload.html)**

The New York Times • 22h ago

---

**[AI in the mental health care workforce is met with fear, pushback — and enthusiasm](https://www.npr.org/2026/04/07/nx-s1-5771707/mental-health-care-workforce-artificial-intelligence-ai)**

Artificial intelligence tools that help mental health therapists take notes and keep records are quickly entering the marketplace. But some question the safety of AI in mental health care delivery.

NPR • 5h ago

---

**[Anthropic expands partnership with Google and Broadcom for multiple gigawatts of next-generation compute](https://www.anthropic.com/news/google-broadcom-partnership-compute)**

Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.

Anthropic • 16h ago

---

**[Broadcom agrees to expanded chip deals with Google, Anthropic](https://www.cnbc.com/2026/04/06/broadcom-agrees-to-expanded-chip-deals-with-google-anthropic.html)**

Broadcom said it agreed to produce future versions of Google artificial intelligence chips, and announced an expanded deal with Anthropic.

CNBC • 17h ago

---

**[Google quietly launched an AI dictation app that works offline](https://techcrunch.com/2026/04/06/google-quietly-releases-an-offline-first-ai-dictation-app-on-ios/)**

Google's new offline-first dictation app uses Gemma AI models to take on the apps like Wispr Flow.

TechCrunch • 19h ago

---

---

## HackerNews: "ai"

**[Eight years of wanting, three months of building with AI](https://news.ycombinator.com/item?id=47648828)**

For eight years, I’ve wanted a high-quality set of devtools for working with SQLite. Given how important SQLite is to the industry1, I’ve long been puzzled that no one has invested in building a really good developer experience for it2.
A couple of weeks ago, after ~250 hours of effort over three months3 on evenings, weekends, and vacation days, I finally released syntaqlite (GitHub), fulfilling this long-held wish. And I believe the main reason this happened was because of AI coding agents4.
Of course, there’s no shortage of posts claiming that AI one-shot their project or pushing back and declaring that AI is all slop. I’m going to take a very different approach and, instead, systematically break down my experience building syntaqlite with AI, both where it helped and where it was detrimental.
I’ll do this while contextualizing the project and my background so you can independently assess how generalizable this experience was. And whenever I make a claim, I’ll try to back it up with evidence from my project journal, coding transcripts, or commit history5.

⬆️ 938 • 💬 297 • 2d ago • [Lalit Maganti](https://lalitm.com/post/building-syntaqlite-ai/)

---

**[Show HN: Real-time AI (audio/video in, voice out) on an M3 Pro with Gemma E2B](https://news.ycombinator.com/item?id=47652007)**

On-device, real-time multimodal AI. Have natural voice and vision conversations with an AI that runs entirely on your machine. Powered by Gemma 4 E2B and Kokoro. - fikrikarim/parlor

⬆️ 277 • 💬 35 • 1d ago • [GitHub](https://github.com/fikrikarim/parlor)

---

**[AI singer now occupies eleven spots on iTunes singles chart](https://news.ycombinator.com/item?id=47662596)**

iTunes was really bamboozled on April Fools Day. Dallas Little, content creator, unleashed four more songs by his AI creation, Eddie Dalton. Now Little has ELEVEN spots on the iTunes top 100. He also has the number three album on iTunes! All by a singer named “Eddie Dalton,” who does not exist. He’s Little’s Artificial […]

⬆️ 225 • 💬 349 • 22h ago • [Showbiz411](https://www.showbiz411.com/2026/04/05/itunes-takeover-by-fake-ai-singer-eddie-dalton-now-occupies-eleven-spots-on-chart-despite-not-being-human-or-real-exclusive)

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

⬆️ 153 • 💬 21 • 1d ago • [GitHub](https://github.com/kessler/gemma-gem)

---

**[AI may be making us think and write more alike](https://news.ycombinator.com/item?id=47673541)**

Large language models may be standardizing human expression and subtly influencing how we think, says study led by USC Dornsife researcher

⬆️ 133 • 💬 130 • 3h ago • [USC Dornsife News](https://dornsife.usc.edu/news/stories/ai-may-be-making-us-think-and-write-more-alike/)

---

**[Musician says AI company is cloning her music, filing claims against her](https://news.ycombinator.com/item?id=47653471)**

⬆️ 121 • 💬 19 • 1d ago • [X (formerly Twitter)](https://twitter.com/unlimited_ls/status/2040577536136974444)

---

**[Show HN: Hippo, biologically inspired memory for AI agents](https://news.ycombinator.com/item?id=47667672)**

Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero dependencies. - kitfunso/hippo-memory

⬆️ 114 • 💬 24 • 17h ago • [GitHub](https://github.com/kitfunso/hippo-memory)

---

**[Writing Lisp is AI resistant and I'm sad](https://news.ycombinator.com/item?id=47645468)**

⬆️ 97 • 💬 99 • 2d ago • [blog.djhaskin.com](https://blog.djhaskin.com/blog/writing-lisp-is-ai-resistant-and-im-sad/)

---

**[Bernie Sanders: "AI Is a Threat to Everything the American People Hold Dear"](https://news.ycombinator.com/item?id=47667798)**

⬆️ 67 • 💬 57 • 16h ago • [wsj.com](https://www.wsj.com/opinion/ai-is-a-threat-to-everything-the-american-people-hold-dear-a3286459)

---

---

## YouTube Videos: "ai"

**[China Just Dropped 3 FREE AI Video Generators (No Sign-Up, Open Source)](https://www.youtube.com/watch?v=wdxaeAiqcuU)**

Join my Discord community https://discord.gg/QC2YEk7P7n Try the tools here https://perchance.org ...

📺 Becky the Ai Girl

👁️ 4K • 👍 316 • 💬 26 • ⏱️ 10:54 • 20h ago

---

**[Microsoft New AI Is 60X Faster Than Real Time (Beats Top Models)](https://www.youtube.com/watch?v=tDW6VoyWWqo)**

Microsoft just launched MAI-Transcribe-1, MAI-Voice-1, and MAI-Image-2, though this story goes way beyond 3 new models.

📺 AI Revolution

👁️ 19K • 👍 581 • 💬 49 • ⏱️ 10:31 • 16h ago

---

**[This AI just leaked its own code..](https://www.youtube.com/watch?v=EAaRzLjQiAU)**

Asmongold reacts to the Claude Code situation https://youtube.com/watch?v=mBHRPeg8zPU ▻ Asmongold's Twitch: ...

📺 Asmongold TV  

👁️ 763K • 👍 22K • 💬 3K • ⏱️ 11:03 • 2d ago

---

**[Sam Altman Gets Embarrassed by His Own AI (Then It Calls Him A Liar!)](https://www.youtube.com/watch?v=bq60j7tN_Zc)**

In this episode of 51/49, James exposes the $852 billion cracks in the OpenAI empire, investigating how viral ChatGPT failures ...

📺 51-49 with James Li

👁️ 127K • 👍 11K • 💬 2K • ⏱️ 15:17 • 1d ago

---

**[We&#39;re Not Ready For AI Glasses](https://www.youtube.com/watch?v=PrkwfI9-maM)**

Protect your privacy and try Proton VPN today → http://protonvpn.com/logicallyanswered AI glasses are no longer some weird ...

📺 Logically Answered

👁️ 29K • 👍 1K • 💬 189 • ⏱️ 15:18 • 16h ago

---

**[REPORT THIS VIDEO: AI is ruining youtube](https://www.youtube.com/watch?v=Ku3OMJsLzwU)**

garbage video: https://www.youtube.com/watch?v=huXOoaPWDQ0 https://youtu.be/6uKZ84zwJI0 https://youtu.be/iwc5HKnOmGg ...

📺 Louis Rossmann

👁️ 182K • 👍 17K • 💬 3K • ⏱️ 9:39 • 1d ago

---

**[We Bought MORE Ai Shopping Scams So You Don’t Have To](https://www.youtube.com/watch?v=UExYNu5j1uo)**

Squarespace ▻ Head to http://squarespace.com/corridorcrew to save 10% off your first purchase! Corridor Big Frig Mugs ...

📺 Corridor Crew

👁️ 750K • 👍 36K • 💬 2K • ⏱️ 20:43 • 1d ago

---

**[The AI Bubble Is Getting Worse Faster Than Expected...](https://www.youtube.com/watch?v=HrfAHSUSMJA)**

Hello guys and gals, it's me Mutahar again! This time we take a look at what appears to be serious pressure faced by the ...

📺 SomeOrdinaryGamers

👁️ 418K • 👍 16K • 💬 2K • ⏱️ 20:44 • 2d ago

---

**[AI Layoffs: Why People in Their 40s Are the Hardest Hit Group | Vantage on Firstpost | N18G](https://www.youtube.com/watch?v=m_9b9bYrNc0)**

Layoffs are no longer isolated events but an ongoing global trend, especially in the technology sector. Since 2022, job cuts have ...

📺 Firstpost

👁️ 116K • 👍 861 • 💬 191 • ⏱️ 6:00 • 21h ago

---

**[LinkedIn CEOs Are CELEBRATING AI Layoffs](https://www.youtube.com/watch?v=eupDkKbA7Q8)**

Support on Patreon: https://www.patreon.com/cw/BusinessCringe Shop merch: https://thebusinesscringe.com/en-usd ...

📺 BusinessCringe

👁️ 16K • 👍 2K • 💬 408 • ⏱️ 9:07 • 17h ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 884,290 • ❤️ 1,262 • 5d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

This image-text-to-text model, Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled, is fine-tuned on Qwen3.5-27B using Claude-4.6 Opus reasoning data for enhanced Chain-of-Thought capabilities. It excels at structured problem-solving and complex reasoning tasks, showing improved autonomy and stability in coding agent environments.

`image-text-to-text` `27.8B`

⬇️ 552,015 • ❤️ 2,435 • 1d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`text-generation` `6.4B`

⬇️ 29,514 • ❤️ 619 • 3d ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 516 • 21h ago

---

**[Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)**

*Prism ML*

Bonsai-8B-GGUF is a highly compressed 1-bit language model (1.15 GB) optimized for llama.cpp, offering competitive performance with full-precision 8B models. It enables efficient on-device text generation across CUDA, Metal, and CPU platforms with significantly reduced memory and energy consumption.

`text-generation` `8.2B`

⬇️ 52,632 • ❤️ 489 • 1d ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 659,815 • ❤️ 482 • 5d ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 473,605 • ❤️ 447 • 5d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 39,933 • ❤️ 1,067 • 12d ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 104,915 • ❤️ 332 • 1d ago

---

**[gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it)**

*Google*

Gemma 4 E2B-it is an instruction-tuned, multimodal (text, image, audio) LLM from Google DeepMind, featuring a 128K context window and efficient Dense architecture. It excels at reasoning, coding, and agentic tasks, optimized for on-device deployment.

`any-to-any` `5.1B`

⬇️ 321,237 • ❤️ 310 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 153 • 💬 7 • ⭐ 37,158 • 7mo ago

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

▲ 21 • 💬 1 • ⭐ 15,339 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[VOID: Video Object and Interaction Deletion](https://huggingface.co/papers/2604.02296)**

*Saman Motamed, William Harvey, Benjamin Klein et al. (6 authors)*

🏢 Netflix

VOID is a video object removal framework that uses vision-language models and video diffusion models to generate physically plausible scenes by leveraging causal reasoning and counterfactual reasoning.

▲ 39 • 💬 5 • ⭐ 977 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02296) • [💻 code](https://github.com/Netflix/void-model) • [🔗 project](https://void-model.github.io/)

---

**[TriAttention: Efficient Long Reasoning with Trigonometric KV Compression](https://huggingface.co/papers/2604.04921)**

*Weian Mao, Xi Lin, Wei Huang et al. (8 authors)*

🏢 NVIDIA

TriAttention addresses KV cache memory bottlenecks in LLMs by leveraging Q/K vector concentration in pre-RoPE space to improve key importance estimation and enable efficient long-context generation.

▲ 58 • 💬 1 • ⭐ 121 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2604.04921) • [💻 code](https://github.com/WeianMao/triattention) • [🔗 project](https://weianmao.github.io/tri-attention-project-page/)

---

**[DeepScientist: Advancing Frontier-Pushing Scientific Findings
  Progressively](https://huggingface.co/papers/2509.26603)**

*Yixuan Weng, Minjun Zhu, Qiujie Xie et al. (7 authors)*

🏢 Text Intelligence Lab of Westlake University

DeepScientist autonomously conducts scientific discovery through Bayesian Optimization, surpassing human state-of-the-art methods on multiple AI tasks.

▲ 18 • 💬 4 • ⭐ 1,717 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.26603) • [💻 code](https://github.com/ResearAI/DeepScientist) • [🔗 project](https://ai-researcher.net)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 38 • 💬 2 • ⭐ 32,526 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 21 • 💬 4 • ⭐ 5,116 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 155 • 💬 2 • ⭐ 58,432 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Generative World Renderer](https://huggingface.co/papers/2604.02329)**

*Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan et al. (9 authors)*

🏢 Shanda AI Research Tokyo

A large-scale dynamic dataset derived from AAA games is introduced to improve generative inverse and forward rendering, featuring high-resolution synchronized RGB and G-buffer data alongside a novel VLM-based evaluation method that correlates well with human judgment.

▲ 93 • 💬 4 • ⭐ 435 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02329) • [💻 code](https://github.com/ShandaAI/AlayaRenderer) • [🔗 project](https://alaya-studio.github.io/renderer)

---

---

## GitHub Repositories: "ai"

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 14.6k • 🔱 2.8k • 3h ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 14.0k • 🔱 1.3k • 1h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.5k • 🔱 1.4k • 3d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 8.4k • 🔱 1.1k • 8d ago

---

**[milla-jovovich/mempalace](https://github.com/milla-jovovich/mempalace)**

The highest-scoring AI memory system ever benchmarked. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 8.0k • 🔱 850 • 16h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 6.9k • 🔱 412 • 1h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.2k • 🔱 1.6k • 3d ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 5.2k • 🔱 175 • 17h ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.8k • 🔱 461 • 7d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, OpenClaw). Turn any folder of code, docs, papers, or images into a queryable knowledge graph

`Python` `claude-code` `codex` `graphrag` `knowledge-graph` `openclaw`

⭐ 4.7k • 🔱 468 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
