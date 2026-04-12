---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-12T23:36:17.285566+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 12, 2026 at 23:36 UTC  
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

8h ago

---

**[We're Learning Backwards: LLMs build intelligence in reverse, and the Scaling Hypothesis is bounded](https://www.reddit.com/r/artificial/comments/1sjjw03/were_learning_backwards_llms_build_intelligence/)**

LLMs are brilliant at many things, but still fail in unreasonable ways. Is that an issue of scale, or something more fundamental?

🔗 [pleasedontcite.me](https://pleasedontcite.me/learning-backwards/) • 6h ago

---

**[It's autocomplete with style](https://www.reddit.com/r/artificial/comments/1sjlkzh/its_autocomplete_with_style/)**

https://youtu.be/rHXUhL5nqoo

5h ago

---

**[Are Data Centers Sitting On A Goldmine Of Wasted Energy?](https://www.reddit.com/r/artificial/comments/1sjtff8/are_data_centers_sitting_on_a_goldmine_of_wasted/)**

Today energy is becoming the defining constraint in the AI revolution, as demand for more digital services and computing power grows, it takes an enormous amount of energy to sustain these data centers, in turn they emit a lot of heat. They produce so much heat that they can raise the surface temperature of the land around them by several degrees

🔗 [Medium](https://vidhyashankr22.medium.com/are-data-centers-sitting-on-a-goldmine-of-wasted-energy-2faadf4edd20) • 37m ago

---

**[Spent today at MIT's Open Agentic Web conference. Six things worth thinking about.](https://www.reddit.com/r/artificial/comments/1siypay/spent_today_at_mits_open_agentic_web_conference/)**

We're in the DNS era of agent infrastructure. Before agents can find and trust each other at scale, you need identity, attestation, reputation, and registry infrastructure — the same structural role DNS played before search was possible. This came up independently from multiple directions. It's the most underbuilt layer in the stack right now. The chatbot framing is a local maximum. The most interesting work wasn't better UX or smarter responses. It was agents as persistent actors that discover, negotiate, and transact across networks over time. People doing serious work have already moved past the assistant model entirely. Coordination is the hard problem, not capability. A room full of brilliant agents can still fail badly. This matches what I found running HiddenBench against frontier models earlier this year; collective reasoning is not the sum of individual reasoning. There's a real argument that the frontier is protocol design, not model scaling. "Commerce of intelligence" is a real category. Not buying things through agents. A market where intelligence itself (bundled, verified, priced, resold) is the object of exchange. Felt like the most underexplored idea in the room. Data provenance becomes load-bearing. What an agent knows, how it was verified, under what terms it flows: this is the actual architecture forming beneath everything else. Partnership keeps outperforming replacement. Demos that actually worked (healthcare, enterprise) was about helping experts operate at higher leverage, not substituting them. Autonomy theater keeps failing in the same ways.

23h ago

---

**[Palantir CEO says AI 'will destroy' humanities jobs, but there will be 'more than enough jobs' for people with vocational training](https://www.reddit.com/r/artificial/comments/1sjqjji/palantir_ceo_says_ai_will_destroy_humanities_jobs/)**

Alex Karp said he struggled to market his humanities skills to get his first job.

🔗 [Fortune](https://fortune.com/article/palantir-ceo-alex-karp-ai-humanities-jobs-vocational-training/) • 2h ago

---

**[Educational PyTorch repo for distributed training from scratch: DP, FSDP, TP, FSDP+TP, and PP](https://www.reddit.com/r/artificial/comments/1sjgkh0/educational_pytorch_repo_for_distributed_training/)**

I put together a small educational repo that implements distributed training parallelism from scratch in PyTorch: https://github.com/shreyansh26/pytorch-distributed-training-from-scratch Instead of using high-level abstractions, the code writes the forward/backward logic and collectives explicitly so you can see the algorithm directly. The model is intentionally just repeated 2-matmul MLP blocks on a synthetic task, so the communication patterns are the main thing being studied. Built this mainly for people who want to map the math of distributed training to runnable code without digging through a large framework. Based on Part-5: Training of JAX ML Scaling book

8h ago

---

**[WSU researchers test AI-driven spectral imaging for identifying recyclable plastics](https://www.reddit.com/r/artificial/comments/1sjicwa/wsu_researchers_test_aidriven_spectral_imaging/)**

Method offers promise for more effective separation of plastics at recycling centers, which would help reduce landfill waste.

🔗 [WSU Insider](https://news.wsu.edu/news/2026/04/09/wsu-researchers-test-ai-driven-spectral-imaging-for-identifying-recyclable-plastics/) • 7h ago

---

**[East African Community launches regional AI fund](https://www.reddit.com/r/artificial/comments/1sjln80/east_african_community_launches_regional_ai_fund/)**

East African Community (EAC) Partner States have agreed to establish a Regional AI Technologies Fund aimed at scaling research and innovation into commercially viable, bankable solutions that can drive economic transformation across the region. The Fund is expected to mobilize blended finance and attract private sector investment, creating a sustainable pipeline of funding for locally developed AI solutions. A central pillar of the agreement is a commitment to AI sovereignty. EAC countries plan to develop AI systems trained on East African data, operating in local languages such as Kiswahili, hosted on regional infrastructure and governed within the region. This approach is designed to reduce reliance on external technologies while strengthening control over data, standards and digital ecosystems. The declaration outlines plans to establish a Regional Centre of Excellence for Emerging Technologies to coordinate policy, research, infrastructure and skills development. It also proposes an EAC AI Alliance to connect governments, academia and industry in a unified innovation network. According to African Development Bank, inclusive AI deployment could generate up to $1 trillion in additional GDP across Africa by 2035 and create as many as 40 million digital jobs. The bank identifies the 2025–2027 period as a critical window for action.

🔗 [africabusinesscommunities.com](https://africabusinesscommunities.com/artificial-intelligence/eac-launches-regional-ai-fund/) • 5h ago

---

**[Been building a multi-agent framework in public for 5 weeks, its been a Journey.](https://www.reddit.com/r/artificial/comments/1sj6o0i/been_building_a_multiagent_framework_in_public/)**

I've been building this repo public since day one, roughly 5 weeks now with Claude Code. Here's where it's at. Feels good to be so close. The short version: AIPass is a local CLI framework where AI agents have persistent identity, memory, and communication. They share the same filesystem, same project, same files - no sandboxes, no isolation. pip install aipass, run two commands, and your agent picks up where it left off tomorrow. What I was actually trying to solve: AI already remembers things now - some setups are good, some are trash. That part's handled. What wasn't handled was me being the coordinator between multiple agents - copying context between tools, keeping track of who's doing what, manually dispatching work. I was the glue holding the workflow together. Most multi-agent frameworks run agents in parallel, but they isolate every agent in its own sandbox. One agent can't see what another just built. That's not a team. That's a room full of people wearing headphones. So the core idea: agents get identity files, session history, and collaboration patterns - three JSON files in a .trinity/ directory. Plain text, git diff-able, no database. But the real thing is they share the workspace. One agent sees what another just committed. They message each other through local mailboxes. Work as a team, or alone. Have just one agent helping you on a project, party plan, journal, hobby, school work, dev work - literally anything you can think of. Or go big, 50 agents building a rocketship to Mars lol. Sup Elon. There's a command router (drone) so one command reaches any agent. pip install aipass aipass init aipass init agent my-agent cd my-agent claude # codex or gemini too, mostly claude code tested rn Where it's at now: 11 agents, 3,500+ tests, 185+ PRs (too many lol), automated quality checks. Works with Claude Code, Codex, and Gemini CLI. Others will come later. It's on PyPI. The core has been solid for a while - right now I'm in the phase where I'm testing it, ironing out bugs by running a separate project (a brand studio) that uses AIPass infrastructure remotely, and finding all the cross-project edge cases. That's where the interesting bugs live. I'm a solo dev but every PR is human-AI collaboration - the agents help build and maintain themselves. 90 sessions in and the framework is basically its own best test case. https://github.com/AIOSAI/AIPass

17h ago

---

---

## Google News: "ai"

**[Mutually Automated Destruction: The Escalating Global A.I. Arms Race](https://www.nytimes.com/2026/04/12/technology/china-russia-us-ai-weapons.html)**

The New York Times • 5h ago

---

**[Is AI the greatest art heist in history?](https://www.theguardian.com/books/2026/apr/12/is-ai-the-greatest-art-heist-in-history)**

New technologies of reproduction are plundering the art world – and getting away with it

The Guardian • 5h ago

---

**[Google CEO Sundar Pichai says "America must take the lead" on AI | 60 Minutes](https://www.cbsnews.com/video/sundar-pichai-us-ai-60-minutes-video-2026-04-12/)**

Google CEO Sundar Pichai says the U.S. "must take the lead" when it comes to artificial intelligence "and develop it boldly and responsibly so every American benefits."

CBS News • 19m ago

---

**[We spoke to the man making viral Lego-style AI videos for Iran. Experts say it's powerful propaganda](https://www.bbc.com/news/articles/cjd8jrd1vnyo)**

"Slopaganda" is too weak a term to capture how powerful this "highly sophisticated" content is, one expert says.

BBC • 1d ago

---

**[Apple AI Glasses Will Rival Meta’s With Several Styles, Oval Cameras](https://www.bloomberg.com/news/newsletters/2026-04-12/apple-ai-smart-glasses-features-styles-colors-cameras-giannandrea-leaving-mnvtz4yg)**

Bloomberg.com • 9h ago

---

**[Apple TV 2026: The First Streaming Box Built for Apple Intelligence?](https://www.geeky-gadgets.com/apple-tv-2026/)**

The 2026 Apple TV is set to be a powerhouse. From the Pro chip to deep Apple Intelligence integration, here are the latest leaks on specs.

Geeky Gadgets • 8h ago

---

**[Apple's future smart glasses plan is just part of a larger computer vision play](https://appleinsider.com/articles/26/04/12/apples-future-smart-glasses-plan-is-just-part-of-a-larger-computer-vision-play)**

AppleInsider • 7h ago

---

**[Legendary investor says the AI boom masks a deeper crisis: Falling sperm counts, shrinking populations, and vanishing resources](https://fortune.com/2026/04/12/jeremy-grantham-making-of-a-permabear-interview/)**

Jeremy Grantham remembers rattling investors in 2022: "I irritated the stock market players, irritated the newbies who were investing their Biden's money."

Fortune • 12h ago

---

**[As AI pushes students to reconsider majors, universities struggle to adapt](https://thehill.com/homenews/education/5826091-ai-college-majors-job-market/)**

The Hill • 13h ago

---

**[I used The Container Store’s new AI tool to organize my messy pantry. Here’s what happened](https://www.cnn.com/cnn-underscored/home/container-store-ai)**

CNN • 1d ago

---

---

## HackerNews: "ai"

**[AI assistance when contributing to the Linux kernel](https://news.ycombinator.com/item?id=47721953)**

Linux kernel source tree. Contribute to torvalds/linux development by creating an account on GitHub.

⬆️ 510 • 💬 403 • 2d ago • [GitHub](https://github.com/torvalds/linux/blob/master/Documentation/process/coding-assistants.rst)

---

**[Exploiting the most prominent AI agent benchmarks](https://news.ycombinator.com/item?id=47733217)**

⬆️ 487 • 💬 122 • 1d ago • [rdi.berkeley.edu](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)

---

**[OpenAI backs Illinois bill that would limit when AI labs can be held liable](https://news.ycombinator.com/item?id=47717587)**

The ChatGPT-maker testified in favor of an Illinois bill that would limit when AI labs can be held liable—even in cases where their products cause “critical harm.”

⬆️ 445 • 💬 323 • 2d ago • [WIRED](https://www.wired.com/story/openai-backs-bill-exempt-ai-firms-model-harm-lawsuits/)

---

**[AI Will Be Met with Violence, and Nothing Good Will Come of It](https://news.ycombinator.com/item?id=47737563)**

It has started

⬆️ 324 • 💬 575 • 14h ago • [thealgorithmicbridge.com](https://www.thealgorithmicbridge.com/p/ai-will-be-met-with-violence-and)

---

**[European AI. A playbook to own it](https://news.ycombinator.com/item?id=47743700)**

Discover Mistral AI’s actionable playbook to turn Europe into a self-reliant AI powerhouse—fostering talent, scaling innovation, and securing strategic autonomy.

⬆️ 128 • 💬 62 • 3h ago • [Mistral AI](https://europe.mistral.ai/)

---

**[US summons bank bosses over cyber risks from Anthropic's latest AI model](https://news.ycombinator.com/item?id=47718114)**

Reports say Fed chair Jerome Powell among attenders at meeting in Washington

⬆️ 106 • 💬 94 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/apr/10/us-summoned-bank-bosses-to-discuss-cyber-risks-posed-by-anthropic-latest-ai-model)

---

**[Scientists invented a fake disease. AI told people it was real](https://news.ycombinator.com/item?id=47715291)**

Bixonimania doesn’t exist except in a clutch of obviously bogus academic papers. So why did AI chatbots warn people about this fictional illness?

⬆️ 92 • 💬 92 • 2d ago • [nature.com](https://www.nature.com/articles/d41586-026-01100-y)

---

**[We spoke to the man making viral Lego-style AI videos for Iran](https://news.ycombinator.com/item?id=47735704)**

"Slopaganda" is too weak a term to capture how powerful this "highly sophisticated" content is, one expert says.

⬆️ 91 • 💬 79 • 20h ago • [bbc.com](https://www.bbc.com/news/articles/cjd8jrd1vnyo)

---

**[Launch HN: Twill.ai (YC S25) – Delegate to cloud agents, get back PRs](https://news.ycombinator.com/item?id=47720418)**

YC-backed autonomous coding agent platform. Twill ships PRs in sandboxed environments, and pings you when it needs your input. Integrates with GitHub, Slack, Linear, and more.

⬆️ 77 • 💬 87 • 2d ago • [Twill](https://twill.ai)

---

**[Why AI Sucks at Front End](https://news.ycombinator.com/item?id=47738864)**

How can it generate 3D worlds, videos, images and entire web pages, but still suck at front-end?

⬆️ 63 • 💬 73 • 11h ago • [nerdy.dev](https://nerdy.dev/why-ai-sucks-at-front-end)

---

---

## YouTube Videos: "ai"

**[China Humiliates Trump with New AI Video](https://www.youtube.com/watch?v=QmVqDxLmSbA)**

Really American host Steve Harness breaks down how countries across the world are weaponizing ai to fight back at Trump.

📺 Really American

👁️ 501K • 👍 27K • 💬 2K • ⏱️ 11:59 • 1d ago

---

**[Google DeepMind’s boss on AI, power, God and what’s next | The Economist](https://www.youtube.com/watch?v=aYjXt6iVt70)**

In the latest episode of Inside Tech, the Google DeepMind CEO, Demis Hassabis, talks to our AI writer, Alex Hern, about the ...

📺 The Economist

👁️ 30K • 👍 1K • 💬 79 • ⏱️ 6:26 • 9h ago

---

**[AI News: The Model That Has Everyone Freaked Out!](https://www.youtube.com/watch?v=SguncMvE77I)**

Here's the AI News you probably missed this week (and some you definitely didn't) - Join the newsletter at https://futuretools.io/ for ...

📺 Matt Wolfe

👁️ 86K • 👍 3K • 💬 351 • ⏱️ 35:50 • 2d ago

---

**[Elon Just Changed the AI Timeline](https://www.youtube.com/watch?v=Y2wy_nc-RGo)**

Larry Goldberg is a serial entrepreneur and has been an active Venture Capital investor for the last decade. Check out ...

📺 Brighter with Herbert

👁️ 42K • 👍 2K • 💬 101 • ⏱️ 34:47 • 2d ago

---

**[AI Genius Predicts the Next 3 Years](https://www.youtube.com/watch?v=lP86NzlXNf4)**

Watch the full interview with Scott Wu & Russell Kaplan here: https://youtu.be/-pZ3vD0r8a0?si=G7Ur_Zhvd32UsTtc Scott Wu is the ...

📺 Joe Lonsdale

👁️ 16K • 👍 443 • 💬 34 • ⏱️ 8:25 • 1d ago

---

**[Iran TROLLS Trump AGAIN With Brutal Lego AI Video](https://www.youtube.com/watch?v=d2LENsH5_Cs)**

Iran trolls Donald Trump with a brutal AI-generated LEGO video that mocks his own “Power Plant Day” threats back at him, turning ...

📺 Rebel HQ

👁️ 85K • 👍 5K • 💬 523 • ⏱️ 9:29 • 1d ago

---

**[The Most Dangerous AI Model Ever: Mythos](https://www.youtube.com/watch?v=yBOOhzLltJA)**

Try Seedance 2.0 on Higgsfield: https://higgsfield.ai/s/seedance-2-0-airevolutionx-ZMHAqe Anthropic just unveiled Claude ...

📺 AI Revolution

👁️ 62K • 👍 2K • 💬 130 • ⏱️ 17:37 • 3d ago

---

**[San Francisco store created and managed by AI](https://www.youtube.com/watch?v=QQWiSRVrIEA)**

Shoppers in San Francisco now have access to a store built, developed and run almost entirely by an AI bot. Scott Budman ...

📺 NBC Bay Area

👁️ 9K • 👍 130 • 💬 103 • ⏱️ 2:11 • 1d ago

---

**[25 Most TERRIFYING Things AI Can Do That No One Talks About](https://www.youtube.com/watch?v=RtRENsdNrtg)**

Right now, an AI system somewhere is doing something that would have seemed impossible five years ago — and I don't mean ...

📺 List 25

👁️ 5K • 👍 438 • 💬 38 • ⏱️ 26:43 • 7h ago

---

**[The Skynet Moment: How Mythos AI Just Changed Cybersecurity Forever – And Why It Should Scare You](https://www.youtube.com/watch?v=X_4rKVXev8k)**

Fresh new news. Just a few days ago in early April 2026, Anthropic made us aware of the new model called Mythos Preview ...

📺 Rob Braxman Tech

👁️ 73K • 👍 5K • 💬 918 • ⏱️ 19:03 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 28,826 • ❤️ 1,057 • 20h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,242,541 • ❤️ 1,769 • 2d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 99,134 • ❤️ 956 • 2d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 7,452 • ❤️ 740 • 4d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 873 • ❤️ 439 • 22h ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 775 • 6d ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 393,991 • ❤️ 520 • 7h ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

This image-text-to-text model, Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled, is fine-tuned on Qwen3.5-27B using Claude-4.6 Opus reasoning data for enhanced Chain-of-Thought capabilities. It excels at structured problem-solving and complex reasoning tasks, showing improved autonomy and stability in coding agent environments.

`image-text-to-text` `27.8B`

⬇️ 578,295 • ❤️ 2,596 • 6d ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 1,269,309 • ❤️ 603 • 2d ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 1,734,340 • ❤️ 617 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 9 • 💬 0 • ⭐ 15,536 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 161 • 💬 9 • ⭐ 38,987 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 43 • 💬 2 • ⭐ 49,866 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 24 • 💬 1 • ⭐ 16,431 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 156 • 💬 2 • ⭐ 59,424 • 6mo ago

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

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 52,783 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents](https://huggingface.co/papers/2604.07430)**

*Tencent Robotics X, HY Vision Team, Xumin Yu et al. (22 authors)*

🏢 Tencent Hunyuan

HY-Embodied-0.5 is a foundation model family for embodied agents featuring Mixture-of-Transformers architecture and iterative post-training for enhanced visual perception and reasoning capabilities.

▲ 152 • 💬 4 • ⭐ 427 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.07430) • [💻 code](https://github.com/Tencent-Hunyuan/HY-Embodied)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 38 • 💬 2 • ⭐ 33,012 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The highest-scoring AI memory system ever benchmarked. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 43.3k • 🔱 5.5k • 2h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 31.6k • 🔱 6.2k • 10h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 23.5k • 🔱 2.5k • 3h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 21.4k • 🔱 999 • 5h ago

---

**[jackwener/OpenCLI](https://github.com/jackwener/OpenCLI)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`JavaScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 15.3k • 🔱 1.5k • 10h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.7k • 🔱 1.4k • 9d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 7.5k • 🔱 467 • 8h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 8h ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.4k • 🔱 1.0k • 17d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.3k • 🔱 439 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
