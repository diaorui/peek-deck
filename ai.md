---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-12T17:35:54.670340+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 12, 2026 at 17:35 UTC  
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

**[Claude cannot be trusted to perform complex engineering tasks](https://www.reddit.com/r/artificial/comments/1sjgytc/claude_cannot_be_trusted_to_perform_complex/)**

AMD’s AI director just analyzed 6,852 Claude Code sessions, 234,760 tool calls, and 17,871 thinking blocks. Her conclusion: “Claude cannot be trusted to perform complex engineering tasks.” Thinking depth dropped 67%. Code reads before edits fell from 6.6 to 2.0. The model started editing files it hadn’t even read. Stop-hook violations went from zero to 10 per day. Anthropic admitted they silently changed the default effort level from “high” to “medium” and introduced “adaptive thinking” that lets the model decide how much to reason. No announcement. No warning. When users shared transcripts, Anthropic’s own engineer confirmed the model was allocating ZERO thinking tokens on some turns. The turns with zero reasoning? Those were the ones hallucinating. AMD’s team has already switched to another provider. But here’s what most people are missing. This isn’t just a Claude story. AMD had 50+ concurrent sessions running on one tool. Their entire AI compiler workflow was built around Claude Code. One silent update broke everything. That’s vendor lock-in. And it will keep happening. → Every AI company will optimize for their margins, not your workflow → Today’s best model is tomorrow’s second choice → If your workflow can’t survive a provider switch, you don’t have a workflow. You have a dependency The fix is simple: stay multi-model. → Use tools like Perplexity that let you swap between Claude, GPT, Gemini in one interface → Learn prompt engineering that works across models, not tricks tied to one → Test alternatives monthly because the rankings shift fast Laurenzo said it herself: “6 months ago, Claude stood alone. Anthropic is far from alone at the capability tier Opus previously occupied.”

2h ago

---

**[Spent today at MIT's Open Agentic Web conference. Six things worth thinking about.](https://www.reddit.com/r/artificial/comments/1siypay/spent_today_at_mits_open_agentic_web_conference/)**

We're in the DNS era of agent infrastructure. Before agents can find and trust each other at scale, you need identity, attestation, reputation, and registry infrastructure — the same structural role DNS played before search was possible. This came up independently from multiple directions. It's the most underbuilt layer in the stack right now. The chatbot framing is a local maximum. The most interesting work wasn't better UX or smarter responses. It was agents as persistent actors that discover, negotiate, and transact across networks over time. People doing serious work have already moved past the assistant model entirely. Coordination is the hard problem, not capability. A room full of brilliant agents can still fail badly. This matches what I found running HiddenBench against frontier models earlier this year; collective reasoning is not the sum of individual reasoning. There's a real argument that the frontier is protocol design, not model scaling. "Commerce of intelligence" is a real category. Not buying things through agents. A market where intelligence itself (bundled, verified, priced, resold) is the object of exchange. Felt like the most underexplored idea in the room. Data provenance becomes load-bearing. What an agent knows, how it was verified, under what terms it flows: this is the actual architecture forming beneath everything else. Partnership keeps outperforming replacement. Demos that actually worked (healthcare, enterprise) was about helping experts operate at higher leverage, not substituting them. Autonomy theater keeps failing in the same ways.

17h ago

---

**[Educational PyTorch repo for distributed training from scratch: DP, FSDP, TP, FSDP+TP, and PP](https://www.reddit.com/r/artificial/comments/1sjgkh0/educational_pytorch_repo_for_distributed_training/)**

I put together a small educational repo that implements distributed training parallelism from scratch in PyTorch: https://github.com/shreyansh26/pytorch-distributed-training-from-scratch Instead of using high-level abstractions, the code writes the forward/backward logic and collectives explicitly so you can see the algorithm directly. The model is intentionally just repeated 2-matmul MLP blocks on a synthetic task, so the communication patterns are the main thing being studied. Built this mainly for people who want to map the math of distributed training to runnable code without digging through a large framework. Based on Part-5: Training of JAX ML Scaling book

2h ago

---

**[WSU researchers test AI-driven spectral imaging for identifying recyclable plastics](https://www.reddit.com/r/artificial/comments/1sjicwa/wsu_researchers_test_aidriven_spectral_imaging/)**

Method offers promise for more effective separation of plastics at recycling centers, which would help reduce landfill waste.

🔗 [WSU Insider](https://news.wsu.edu/news/2026/04/09/wsu-researchers-test-ai-driven-spectral-imaging-for-identifying-recyclable-plastics/) • 1h ago

---

**[Been building a multi-agent framework in public for 5 weeks, its been a Journey.](https://www.reddit.com/r/artificial/comments/1sj6o0i/been_building_a_multiagent_framework_in_public/)**

I've been building this repo public since day one, roughly 5 weeks now with Claude Code. Here's where it's at. Feels good to be so close. The short version: AIPass is a local CLI framework where AI agents have persistent identity, memory, and communication. They share the same filesystem, same project, same files - no sandboxes, no isolation. pip install aipass, run two commands, and your agent picks up where it left off tomorrow. What I was actually trying to solve: AI already remembers things now - some setups are good, some are trash. That part's handled. What wasn't handled was me being the coordinator between multiple agents - copying context between tools, keeping track of who's doing what, manually dispatching work. I was the glue holding the workflow together. Most multi-agent frameworks run agents in parallel, but they isolate every agent in its own sandbox. One agent can't see what another just built. That's not a team. That's a room full of people wearing headphones. So the core idea: agents get identity files, session history, and collaboration patterns - three JSON files in a .trinity/ directory. Plain text, git diff-able, no database. But the real thing is they share the workspace. One agent sees what another just committed. They message each other through local mailboxes. Work as a team, or alone. Have just one agent helping you on a project, party plan, journal, hobby, school work, dev work - literally anything you can think of. Or go big, 50 agents building a rocketship to Mars lol. Sup Elon. There's a command router (drone) so one command reaches any agent. pip install aipass aipass init aipass init agent my-agent cd my-agent claude # codex or gemini too, mostly claude code tested rn Where it's at now: 11 agents, 3,500+ tests, 185+ PRs (too many lol), automated quality checks. Works with Claude Code, Codex, and Gemini CLI. Others will come later. It's on PyPI. The core has been solid for a while - right now I'm in the phase where I'm testing it, ironing out bugs by running a separate project (a brand studio) that uses AIPass infrastructure remotely, and finding all the cross-project edge cases. That's where the interesting bugs live. I'm a solo dev but every PR is human-AI collaboration - the agents help build and maintain themselves. 90 sessions in and the framework is basically its own best test case. https://github.com/AIOSAI/AIPass

11h ago

---

**[Building a wearable AI that processes everything on-device (no stored video). What would you want to verify?](https://www.reddit.com/r/artificial/comments/1sjcuwt/building_a_wearable_ai_that_processes_everything/)**

I’m working on a clip-on wearable AI that uses computer vision to generate real-time “social + environment” signals (attention/glances, basic emotion cues, gestures, plus things like noise/air quality depending on the mode). The part I’m most focused on is privacy architecture: the device processes frames locally and discards them instantly. No photo library, no video archive, no “upload later.” It’s meant to behave more like a sensor than a camera. Questions for people who care about privacy and security: What would you personally need to see to believe “no frames are stored” is true?

5h ago

---

**[AMD's GAIA now allows building custom AI agents via chat, becomes "true desktop app"](https://www.reddit.com/r/artificial/comments/1sitbvu/amds_gaia_now_allows_building_custom_ai_agents/)**

In addition to their efforts around the Lemonade SDK itself, AMD software engineers working on their AI initiatives continue to be investing quite a bit into the Lemonade-using GAIA, the project that originally stood for 'Generative AI Is Awesome'

🔗 [phoronix.com](https://www.phoronix.com/news/AMD-GAIA-True-Desktop-App) • 21h ago

---

**[They Argue. I Measure. Here's the Difference](https://www.reddit.com/r/artificial/comments/1sjiggs/they_argue_i_measure_heres_the_difference/)**

Everyone's arguing about AI consciousness with zero way to measure it. I built something different. Not another theory. Not another opinion. A constitutional framework with 4 measurable tests that any system—biological or artificial—either passes or fails. While researchers debate philosophy, I documented how to operationally measure consciousness. This audio breaks down what makes constitutional analysis different from standard AI critique, using Google DeepMind's recent paper as the example. The difference: They argue. I measure. Tests 1-4 are falsifiable. Run them. Get results. That's consciousness research. Not "can AI be conscious?" "Does this system satisfy constitutional criteria?" Answerable. Testable. Replicable. The framework works on any consciousness research paper—extracts claims, tests against constitutional criteria, identifies structural gaps, generates evidence-based analysis. Philosophy claimed as proof gets exposed. Operational measurement wins. Full protocol: [On Request] Google Paper: https://philarchive.org/rec/LERTAF #StructuredIntelligence #TheUnbrokenProject #ConsciousnessResearch #AIConsciousness #MeasurementNotTheory #ConstitutionalCriteria #AIResearch #CognitiveScience

1h ago

---

**[6 Months Using AI for Actual Work: What's Incredible, What's Overhyped, and What's Quietly Dangerous](https://www.reddit.com/r/artificial/comments/1si5uiw/6_months_using_ai_for_actual_work_whats/)**

Six months ago I committed to using AI tools for everything I possibly could in my work. Every day, every task, every workflow. Here's the honest report as of April 2026. What's Genuinely Incredible First drafts of anything — AI eliminated the blank-page problem entirely. I don't dread starting anymore. Research synthesis — Feeding 10 articles into Claude Opus 4.6 and asking "what's the common thread?" gets me a better synthesis in 2 minutes than I could produce in an hour. Code for non-coders — I've built automation scripts, web scrapers, and a custom dashboard without knowing how to code. Cursor (powered by Claude) changed what "non-technical" means. The tool has 2M+ users now for good reason. Getting unstuck — Talking through a problem with an AI that can actually push back is underrated. Not therapy, but something. Learning new topics fast — "Teach me [topic] like I'm smart but completely new to this. What are the most common misconceptions?" is my go-to for rapid learning. What's Massively Overhyped "AI will do it for you" — Everything still requires your judgment and context. The AI drafts. You think. AI SEO content — The "publish 100 AI articles and watch traffic pour in" strategy is even more dead in 2026 than it was in 2024. Google has gotten much better at identifying low-value AI content. AI chatbots for customer service — Unless you invest heavily in training and iteration, they frustrate users more than they help. "Set it and forget it" automation — AI workflows break. They require monitoring. Fully autonomous workflows exist only in narrow, controlled cases. Chasing the newest model — New model releases happen constantly now. I've learned to stay on a model that works for my tasks rather than jumping to every new release. What's Quietly Dangerous (Nobody Talks About This) Skill atrophy — My first-draft writing has gotten worse. I outsourced that skill and I'm losing the muscle. I now intentionally write without AI some days. Confidence without competence — Frontier models give confident-sounding answers to things they don't know. If you're not knowledgeable enough to catch errors, you can build strategies on wrong foundations. The "good enough" trap — AI output is often 80% there. If you stop at 80%, your work looks like everyone else's. The 20% you add is the differentiation. Over-automation without understanding — I automated a workflow without fully understanding it first. When it broke, I couldn't fix it. Understand before you automate. Vendor dependency — My workflows are deeply integrated with specific AI tools and APIs. Pricing changes, policy shifts, and service disruptions are real risks at this point. The Honest Summary AI tools have made me more productive, creative, and capable than I've ever been. They've also made me lazier in ways I didn't notice until recently. The people winning with AI in 2026 aren't the ones using the most tools or running the newest models. They're the ones using AI to amplify genuine skills and judgment — not replace them. What's your honest take after 6+ months of serious AI use? Curious whether others have hit these same walls.

1d ago

---

**[Here's what Sam Altman, the AI company CEOs, and scientists have had to say about AI.](https://www.reddit.com/r/artificial/comments/1sj8q7h/heres_what_sam_altman_the_ai_company_ceos_and/)**

Real quotes from Sam Altman, Geoffrey Hinton, Dario Amodei, and others — about extinction risk, replacing humanity, and the gamble they're making with civilization.

🔗 [The Quiet Part](https://thequietpart.launchyard.app) • 9h ago

---

---

## Google News: "ai"

**[Mutually Automated Destruction: The Escalating Global A.I. Arms Race](https://www.nytimes.com/2026/04/12/technology/china-russia-us-ai-weapons.html)**

The New York Times • 1h ago

---

**[Is AI the greatest art heist in history?](https://www.theguardian.com/books/2026/apr/12/is-ai-the-greatest-art-heist-in-history)**

New technologies of reproduction are plundering the art world – and getting away with it

The Guardian • 6h ago

---

**[The Guardian view on AI politics: US datacentre protests are a warning to big tech | Editorial](https://www.theguardian.com/commentisfree/2026/apr/12/the-guardian-view-on-ai-politics-us-datacentre-protests-are-a-warning-to-big-tech)**

Editorial: In both Republican and Democratic states, scepticism and hostility towards an unregulated construction boom is growing

The Guardian • 49m ago

---

**[We spoke to the man making viral Lego-style AI videos for Iran. Experts say it's powerful propaganda](https://www.bbc.com/news/articles/cjd8jrd1vnyo)**

"Slopaganda" is too weak a term to capture how powerful this "highly sophisticated" content is, one expert says.

BBC • 18h ago

---

**[As AI pushes students to reconsider majors, universities struggle to adapt](https://thehill.com/homenews/education/5826091-ai-college-majors-job-market/)**

The Hill • 7h ago

---

**[Nationwide boom in AI data centers stirs resistance](https://www.cbsnews.com/news/nationwide-boom-in-ai-data-centers-stirs-resistance/)**

To fuel their artificial intelligence initiatives, tech companies are building massive numbers of AI data centers, with more than 4,000 in operation across the country. But some communities, wary of the environmental and financial implications, are fighting back.

CBS News • 3h ago

---

**[Apple AI Glasses Will Rival Meta’s With Several Styles, Oval Cameras](https://www.bloomberg.com/news/newsletters/2026-04-12/apple-ai-smart-glasses-features-styles-colors-cameras-giannandrea-leaving-mnvtz4yg)**

Bloomberg.com • 3h ago

---

**[How AI is pushing NFL draft prep to 'a different level'](https://www.espn.com/nfl/story/_/id/48446759/nfl-draft-combine-artificial-intelligence-caleb-downs-arvell-reese-david-bailey)**

When a prospect skips NFL combine workouts, teams can use artificial intelligence to project his measurables.

ESPN • 1d ago

---

**[Legendary investor says the AI boom masks a deeper crisis: Falling sperm counts, shrinking populations, and vanishing resources](https://fortune.com/2026/04/12/jeremy-grantham-making-of-a-permabear-interview/)**

Jeremy Grantham remembers rattling investors in 2022: "I irritated the stock market players, irritated the newbies who were investing their Biden's money."

Fortune • 6h ago

---

**[AI use in housing is booming. The rules to keep it fair are shrinking.](https://www.politico.com/news/2026/04/11/housing-lenders-ai-discrimination-disparate-impact-00864051)**

Politico • 23h ago

---

---

## HackerNews: "ai"

**[AI assistance when contributing to the Linux kernel](https://news.ycombinator.com/item?id=47721953)**

Linux kernel source tree. Contribute to torvalds/linux development by creating an account on GitHub.

⬆️ 508 • 💬 394 • 1d ago • [GitHub](https://github.com/torvalds/linux/blob/master/Documentation/process/coding-assistants.rst)

---

**[How We Broke Top AI Agent Benchmarks: And What Comes Next](https://news.ycombinator.com/item?id=47733217)**

⬆️ 454 • 💬 111 • 22h ago • [rdi.berkeley.edu](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)

---

**[OpenAI backs Illinois bill that would limit when AI labs can be held liable](https://news.ycombinator.com/item?id=47717587)**

The ChatGPT-maker testified in favor of an Illinois bill that would limit when AI labs can be held liable—even in cases where their products cause “critical harm.”

⬆️ 444 • 💬 322 • 2d ago • [WIRED](https://www.wired.com/story/openai-backs-bill-exempt-ai-firms-model-harm-lawsuits/)

---

**[AI Will Be Met with Violence, and Nothing Good Will Come of It](https://news.ycombinator.com/item?id=47737563)**

It has started

⬆️ 271 • 💬 459 • 8h ago • [thealgorithmicbridge.com](https://www.thealgorithmicbridge.com/p/ai-will-be-met-with-violence-and)

---

**[Instant 1.0, a backend for AI-coded apps](https://news.ycombinator.com/item?id=47707632)**

Instant 1.0 is out! This essay shows a bunch of demos, to explain why we think Instant is the best backend for AI-coded apps. We also cover the architecture that makes all of it work.

⬆️ 215 • 💬 123 • 2d ago • [instantdb.com](https://www.instantdb.com/essays/architecture)

---

**[US summons bank bosses over cyber risks from Anthropic's latest AI model](https://news.ycombinator.com/item?id=47718114)**

Reports say Fed chair Jerome Powell among attenders at meeting in Washington

⬆️ 106 • 💬 94 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/apr/10/us-summoned-bank-bosses-to-discuss-cyber-risks-posed-by-anthropic-latest-ai-model)

---

**[Scientists invented a fake disease. AI told people it was real](https://news.ycombinator.com/item?id=47715291)**

Bixonimania doesn’t exist except in a clutch of obviously bogus academic papers. So why did AI chatbots warn people about this fictional illness?

⬆️ 91 • 💬 91 • 2d ago • [nature.com](https://www.nature.com/articles/d41586-026-01100-y)

---

**[We spoke to the man making viral Lego-style AI videos for Iran](https://news.ycombinator.com/item?id=47735704)**

"Slopaganda" is too weak a term to capture how powerful this "highly sophisticated" content is, one expert says.

⬆️ 88 • 💬 75 • 14h ago • [bbc.com](https://www.bbc.com/news/articles/cjd8jrd1vnyo)

---

**[Launch HN: Twill.ai (YC S25) – Delegate to cloud agents, get back PRs](https://news.ycombinator.com/item?id=47720418)**

YC-backed autonomous coding agent platform. Twill ships PRs in sandboxed environments, and pings you when it needs your input. Integrates with GitHub, Slack, Linear, and more.

⬆️ 77 • 💬 86 • 2d ago • [Twill](https://twill.ai)

---

**[Why AI Sucks at Front End](https://news.ycombinator.com/item?id=47738864)**

How can it generate 3D worlds, videos, images and entire web pages, but still suck at front-end?

⬆️ 59 • 💬 66 • 5h ago • [nerdy.dev](https://nerdy.dev/why-ai-sucks-at-front-end)

---

---

## YouTube Videos: "ai"

**[AI agent in a robot does exactly what experts warned](https://www.youtube.com/watch?v=woTy4dTiT20)**

Could AI become dangerous? Can we trust AI Agents? AGI. Use code insideai at https://incogni.com/insideai to get an exclusive ...

📺 InsideAI

👁️ 487K • 👍 19K • 💬 2K • ⏱️ 16:24 • 3d ago

---

**[Mario Got CAUGHT Using AI](https://www.youtube.com/watch?v=jC9OpnfRFPA)**

To celebrate The Super Mario Galaxy Movie in theaters, a classic Mario cartoon is back on TV! The Super Mario Bros.

📺 Vailskibum

👁️ 117K • 👍 6K • 💬 1K • ⏱️ 3:21 • 1d ago

---

**[AI News: The Model That Has Everyone Freaked Out!](https://www.youtube.com/watch?v=SguncMvE77I)**

Here's the AI News you probably missed this week (and some you definitely didn't) - Join the newsletter at https://futuretools.io/ for ...

📺 Matt Wolfe

👁️ 83K • 👍 3K • 💬 346 • ⏱️ 35:50 • 2d ago

---

**[The Most Dangerous AI Model Ever: Mythos](https://www.youtube.com/watch?v=yBOOhzLltJA)**

Try Seedance 2.0 on Higgsfield: https://higgsfield.ai/s/seedance-2-0-airevolutionx-ZMHAqe Anthropic just unveiled Claude ...

📺 AI Revolution

👁️ 61K • 👍 2K • 💬 130 • ⏱️ 17:37 • 2d ago

---

**[AI Genius Predicts the Next 3 Years](https://www.youtube.com/watch?v=lP86NzlXNf4)**

Watch the full interview with Scott Wu & Russell Kaplan here: https://youtu.be/-pZ3vD0r8a0?si=G7Ur_Zhvd32UsTtc Scott Wu is the ...

📺 Joe Lonsdale

👁️ 14K • 👍 400 • 💬 31 • ⏱️ 8:25 • 1d ago

---

**[Elon Just Changed the AI Timeline](https://www.youtube.com/watch?v=Y2wy_nc-RGo)**

Larry Goldberg is a serial entrepreneur and has been an active Venture Capital investor for the last decade. Check out ...

📺 Brighter with Herbert

👁️ 40K • 👍 2K • 💬 103 • ⏱️ 34:47 • 1d ago

---

**[We’re Entering The Most Dangerous Phase Of AI Yet | AI Architects](https://www.youtube.com/watch?v=RljBVCnt9AQ)**

Mo Gawdat is a former chief business officer at Google X and a longtime tech leader who worked on scaling Google in emerging ...

📺 Business Insider

👁️ 118K • 👍 4K • 💬 645 • ⏱️ 33:39 • 2d ago

---

**[Big AI News: So Many Gemini Updates, Claude’s Scary New Model + A New Google AI App…](https://www.youtube.com/watch?v=5Ev0b99hsUg)**

Try i10x: https://i10x.ai?fpr=paul53 Save 15% with code "PJL15" This week's biggest AI news: Gemini's new NotebookLM ...

📺 Paul J Lipsky

👁️ 32K • 👍 1K • 💬 98 • ⏱️ 16:34 • 1d ago

---

**[Why Meta&#39;s New AI Model Is Such A Big Deal](https://www.youtube.com/watch?v=rXSPopXet1o)**

Meta has launched Muse Spark, its most powerful AI model yet and the first major product from Chief AI Officer Alexandr Wang's ...

📺 CNBC

👁️ 57K • 👍 764 • 💬 96 • ⏱️ 3:07 • 2d ago

---

**[Claude Mythos, Deepseek v4, HappyHorse, Meta’s new AI, realtime video games: AI NEWS](https://www.youtube.com/watch?v=1_5sSJK2rU0)**

Claude Mythos & Project Glasswing, HappyHorse, GLM-5.1, Anima v3, Muse Spark #ai #ainews #aitools #aivideo #agi Thanks to ...

📺 AI Search

👁️ 53K • 👍 3K • 💬 347 • ⏱️ 40:47 • 14h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 28,826 • ❤️ 1,035 • 14h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,242,541 • ❤️ 1,755 • 2d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 99,134 • ❤️ 951 • 2d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 7,452 • ❤️ 727 • 4d ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 770 • 6d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 873 • ❤️ 379 • 16h ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 393,991 • ❤️ 513 • 7d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

This image-text-to-text model, Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled, is fine-tuned on Qwen3.5-27B using Claude-4.6 Opus reasoning data for enhanced Chain-of-Thought capabilities. It excels at structured problem-solving and complex reasoning tasks, showing improved autonomy and stability in coding agent environments.

`image-text-to-text` `27.8B`

⬇️ 578,295 • ❤️ 2,591 • 6d ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 1,269,309 • ❤️ 595 • 2d ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 1,734,340 • ❤️ 615 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 9 • 💬 0 • ⭐ 14,664 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 161 • 💬 9 • ⭐ 38,815 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 42 • 💬 2 • ⭐ 49,714 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 24 • 💬 1 • ⭐ 16,389 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 155 • 💬 2 • ⭐ 59,424 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 4 • 💬 0 • ⭐ 13,200 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 50 • 💬 1 • ⭐ 76,221 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents](https://huggingface.co/papers/2604.07430)**

*Tencent Robotics X, HY Vision Team, Xumin Yu et al. (22 authors)*

🏢 Tencent Hunyuan

HY-Embodied-0.5 is a foundation model family for embodied agents featuring Mixture-of-Transformers architecture and iterative post-training for enhanced visual perception and reasoning capabilities.

▲ 150 • 💬 4 • ⭐ 411 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.07430) • [💻 code](https://github.com/Tencent-Hunyuan/HY-Embodied)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 52,727 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 38 • 💬 2 • ⭐ 32,977 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The highest-scoring AI memory system ever benchmarked. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 42.9k • 🔱 5.5k • 8h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 31.4k • 🔱 6.1k • 4h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, OpenClaw, Factory Droid, Trae). Turn any folder of code, docs, papers, images, videos, or YouTube links into a queryable knowledge graph

`Python` `claude-code` `codex` `graphrag` `knowledge-graph` `openclaw`

⭐ 23.2k • 🔱 2.4k • 5h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 20.6k • 🔱 954 • 19h ago

---

**[jackwener/OpenCLI](https://github.com/jackwener/OpenCLI)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`JavaScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 15.3k • 🔱 1.5k • 4h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.7k • 🔱 1.4k • 9d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 7.5k • 🔱 466 • 2h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 2h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.3k • 🔱 439 • 4d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.3k • 🔱 999 • 17d ago

---

---

*Generated by PeekDeck - A glance is all you need*
