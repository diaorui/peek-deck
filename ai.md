---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-28T23:32:54.440699+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 28, 2026 at 23:32 UTC  
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

**[Claude is the least bullshit-y AI](https://www.reddit.com/r/artificial/comments/1s67buc/claude_is_the_least_bullshity_ai/)**

Just found this “bullshit benchmark,” and sort of shocked by the divergence of Anthropic’s models from other major models (ChatGPT and Gemini). IMO this alone is reason to use Claude over others.

🔗 [GitHub](https://github.com/petergpt/bullshit-benchmark?tab=readme-ov-file#3-detection-rate-over-time) • 5h ago

---

**[I tested what happens when you give an AI coding agent access to 2 million research papers. It found techniques it couldn't have known about.](https://www.reddit.com/r/artificial/comments/1s6afwm/i_tested_what_happens_when_you_give_an_ai_coding/)**

Quick experiment I ran. Took two identical AI coding agents (Claude Code), gave them the same task — optimize a small language model. One agent worked from its built-in knowledge. The other had access to a search engine over 2M+ computer science research papers. Agent without papers: did what you'd expect. Tried well-known optimization techniques. Improved the model by 3.67%. Agent with papers: searched the research literature before each attempt. Found 520 relevant papers, tried 25 techniques from them — including one from a paper published in February 2025, months after the AI's training cutoff. It literally couldn't have known about this technique without paper access. Improved the model by 4.05% — 3.2% better. The interesting moment: both agents tried the same idea (halving the batch size). The one without papers got it wrong — missed a crucial adjustment and the whole thing failed. The one with papers found a rule from a 2022 paper explaining exactly how to do it, got it right on the first try. Not every idea from papers worked. But the ones that did were impossible to reach without access to the research. AI models have a knowledge cutoff — they can't see anything published after their training. And even for older work, they don't always recall the right technique at the right time. Giving them access to searchable literature seems to meaningfully close that gap. I built the paper search tool (Paper Lantern) as a free MCP server for AI coding agents: https://code.paperlantern.ai Full experiment writeup: https://www.paperlantern.ai/blog/auto-research-case-study

3h ago

---

**[Say No to Congress using AI to mass surveil US Citizens and oppose the extension of the FISA Act](https://www.reddit.com/r/artificial/comments/1s5onmr/say_no_to_congress_using_ai_to_mass_surveil_us/)**

In April Congress is voting to extend the FISA Act on the 20th of April this year. The FISA Act allows the government to buy your emails, texts, and calls from corporations. With the newly established shady deal with Open AI surveillance has become even more accessible and applicable on a much more larger and invasive scale. It very important for the sake of maintaining our right of protest and the press in the future. Call/email your representatives in the US, protest, and speak in any way you can.

20h ago

---

**[AMD introduces GAIA agent UI for privacy-first web app for local AI agents](https://www.reddit.com/r/artificial/comments/1s67ajg/amd_introduces_gaia_agent_ui_for_privacyfirst_web/)**

AMD's GAIA AI agent framework (that previously stood for 'Generative AI Is Awesome' albeit they seemed to have dropped promoting it as that name) for Ryzen AI hardware is out with a new version

🔗 [phoronix.com](https://www.phoronix.com/news/AMD-GAIA-0.17-Agent-UI) • 5h ago

---

**[👋Welcome to r/AiVIS - Let's build this right](https://www.reddit.com/r/artificial/comments/1s6e8r1/welcome_to_raivis_lets_build_this_right/)**

Hey everyone! I’m u/Renomase, a founding moderator of r/AiVIS. This is the new spot for people watching how AI search is changing visibility in real time. We’re here for AI visibility, audits, citations, schema, structured content, trust signals, and why some sites get picked up while others stay buried. Good to have you here. What to Post: Drop anything useful, real, or worth unpacking. Audit results, questions, examples, experiments, wins, losses, weird search behavior, schema setups, citation problems, content structure ideas, or cases where a site looked good on the surface but still got overlooked by AI. Community Vibe: Keep it solid. Respectful, constructive, no fluff. This should be a place where builders, marketers, founders, and operators can compare notes and get sharper on what actually helps a site get understood and surfaced. How to Get Started: Introduce yourself below. Share what you’re building or testing. Ask a question or post a finding today. Invite somebody who’s tapped into SEO, AI search, or content visibility. Want to help mod and build this right from the ground floor? Reach out. Thanks for being part of the first run. Let’s make r/AiVIS a real signal spot, not just another dead page.

54m ago

---

**[Is anyone else watching what Qubic is doing with distributed compute and AI training? Seems underreported in AI cirles](https://www.reddit.com/r/artificial/comments/1s5x2wo/is_anyone_else_watching_what_qubic_is_doing_with/)**

I follow AI infrastructure pretty closely and Qubic keeps coming up in my research in a way I find intersting but havent seen much discussion of in AI-focused comunities. Quick background for people who havent heard of it: Qubic uses what they call Useful Proof of Work - instead of hardware solving random hash puzzles, the compute runs neural network training tasks for thier Aigarth AI project. The same hardware is contributing to AI training while securing things. The network was independently verifed at 15.52 million transactions per second by CertiK on live mainnet. For context, thats faster than Visas theoretical peak throughput. The architecture runs on bare metal hardware without a virtual machine layer, which is aparently what enables the throughput. Theyre also aparently launching a DOGE mining integration immenantly (around April 1) where thier infrastructure will run Dogecoin mining simultaniously with everything else - the ASIC hardware for DOGE Scrypt mining runs in paralel with thier CPU/GPU hardware for other workloads. For comparison, people often bring up Bittensor, but from what I see Bittensor is more about competing AIs and subnets rewarding each other rather than actually using the distributed compute to train models from scratch with raw hardware power. Qubic seems different in that the mining itself is the training. Big companies are pouring billions into building massive data centers and training ever bigger LLMs, but I dont think true AGI is gonna come just from scaling up these trained models no matter how much money they throw at it. My interest is specifically in the distributed AI compute angle. Is the model of mining-funded distributed AI training something that gets serius discussion in AI research cirles? Or is this considered a fundementaly different category from serius AI infrastructure?

12h ago

---

**[Geolocate any picture down to its exact coordinates (web version)](https://www.reddit.com/r/artificial/comments/1s63yde/geolocate_any_picture_down_to_its_exact/)**

Hey guys, Thank you so much for your love and support regarding Netryx Astra V2 last time. Many people are not that technically savvy to install the GitHub repo and test the tool out immediately so I built a small web demo covering a 10km radius of New York, it's completely free and uses the same pipeline as the repo. I have limited the number of credits since each search consumes GPU costs, but if that's an issue you can install the repo and index any city you want with unlimited searches. I would accept any feedback include searches that failed or didn't work for you. The site works best on desktop Web demo link: https://www.netryx.live Repo link: https://github.com/sparkyniner/Netryx- Astra-V2-Geolocation-Tool

7h ago

---

**[HALO - Hierarchical Autonomous Learning Organism](https://www.reddit.com/r/artificial/comments/1s63mtm/halo_hierarchical_autonomous_learning_organism/)**

The idea is called HALO - Hierarchical Autonomous Learning Organism. The core premise is simple: what if instead of just making LLMs bigger, we actually looked at how intelligence works in nature and built something that mirrors those principles? Not just the human brain either, evolution spent hundreds of millions of years solving different cognitive problems in different species. Why not take the best bits from all of them? Some of what ended up in the design: It has a nervous system. Not metaphorically, it’s literally wired to monitor its own hardware. GPU temps, memory pressure, all of it. When it’s running hot it conserves and gets cautious. When it’s idle and cool it explores and consolidates. Biological stress response, but for silicon. It learns the way animals learn. One strong negative experience permanently changes how it perceives that category of situation, like a kid touching a hot stove. Not just “add a rule” but actually changing the lens it sees similar situations through. Compare that to how current AI just… forgets everything between sessions. It has eight processing arms inspired by octopus neurology. Two thirds of an octopus’s neurons are in its arms, not its brain. Each arm is semi autonomous. Applied here that means memory retrieval, fact checking, simulation, tool staging, all running in parallel before the main model even needs them. No central bottleneck. It knows what it doesn’t know. There are three knowledge databases, what it’s verified, what it’s uncertain about, and a registry of confirmed gaps. That last one is the interesting one. It knows the shape of its own ignorance. That’s what drives the curiosity engine. That’s what makes it actually want to learn rather than just respond. It develops a personality over time. Starts with one seed temperament, curiosity, and everything else emerges from experience. There’s a developmental threshold, and once it crosses it, the system looks at what it’s actually become and that becomes its baseline. Not programmed personality. Accumulated identity. It can choose to ignore guidance and learn from the consequences. Bounded, transparent autonomy. It knows when advice is good and can still try something different. The outcome, good or bad, is the learning signal. That’s how real judgment develops. And everything is declared openly, nothing hidden. The whole thing is designed to run locally, on a gaming PC, with no cloud dependency. Private. Continuous. Gets smarter through use, not retraining. I put together a technical white paper with the complete architecture if anyone wants to go deep. 34+ subsystems, full brain region mapping, animal cognition mapping, causal reasoning engine, six-level memory tree, the works. I genuinely think the pieces are all there. Would love to get some feedback on the idea. The idea is fully open for use, so if anything from the architecture may benefit your project, you’re free to use it.

7h ago

---

**[Looking for a solid ChatGPT alternative for daily work](https://www.reddit.com/r/artificial/comments/1s5v317/looking_for_a_solid_chatgpt_alternative_for_daily/)**

I was long juggling separate monthly subscriptions for Claude, Gemini, and GPT-4 until the costs and tab-switching became a total mess and I started paying over 100 bucks each mont. Then, I tried consolidating everything into a single hub, done that both locally and online, both api and openrouter and all in one online and writingmate. such consolidation then saved me about half of my resources pet each month. I do not have to deal with the constant cooldowns or model blocks that happen when you hit usage caps on a single platform anymore. And having 200+ models in one place has been a massive time-saver for my coding and doc review tasks. I recently processed a 100-page research paper using a long-context model I found on there, which would have been a pain to upload and prompt elsewhere. It is a practical ChatGPT alternative for anyone trying to streamline their setup rather than jumping between browser windows. I am also curious if anyone else here has moved away from the main platform for their daily tasks? Does anyone else find the model-switching friction as annoying as I did?

14h ago

---

**[Meet Claude Mythos: Leaked Anthropic post reveals the powerful upcoming model](https://www.reddit.com/r/artificial/comments/1s5hejt/meet_claude_mythos_leaked_anthropic_post_reveals/)**

Anthropic warned about the AI model's cybersecurity risks in the leaked post as well.

🔗 [Mashable](https://mashable.com/article/claude-mythos-ai-model-anthropic-leak) • 1d ago

---

---

## Google News: "ai"

**[‘Our assumptions are broken’: how fraudulent church data revealed AI’s threat to polling](https://www.theguardian.com/technology/2026/mar/28/how-fraudulent-church-data-revealed-ais-threat-to-polling)**

Experts say paid participants are using automated tools to generate unreliable survey responses at scale

The Guardian • 11h ago

---

**[Meet a 29-year-old blue-collar founder who used AI to triple his revenue in 3 years](https://fortune.com/2026/03/28/ai-small-business-entrepreneur-1-million-blue-collar/)**

Rick Chorney was working long days but still had emails at night. "I went a little crazy," he said. "There came a day where I was just like, 'I am done.'"

Fortune • 11h ago

---

**[AI overly affirms users asking for personal advice](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research)**

Stanford Report • 2d ago

---

**[AI deepfakes blur reality in 2026 US midterm campaigns](https://www.reuters.com/business/media-telecom/ai-deepfakes-blur-reality-2026-us-midterm-campaigns-2026-03-28/)**

Reuters • 10h ago

---

**[Welcome to a Multidimensional Economic Disaster](https://www.theatlantic.com/technology/2026/03/ai-boom-polycrisis/686559/)**

The AI boom wasn’t built for the polycrisis.

The Atlantic • 2d ago

---

**[Trump wants a deadlocked Congress to move on AI. Frustrated states say they already have](https://www.npr.org/2026/03/28/nx-s1-5755062/trump-wants-a-deadlocked-congress-to-move-on-ai-frustrated-states-say-they-already-have)**

State lawmakers have been stepping in to regulate artificial intelligence, clashing with the federal government's inaction as concerns about oversight and safety grow.

NPR • 14h ago

---

**[The Decadelong Feud Shaping the Future of AI](https://www.wsj.com/tech/ai/the-decadelong-feud-shaping-the-future-of-ai-7075acde?gaa_at=eafs&gaa_n=AWEtsqcVua3sZSF6BUopZv9YMi7g-ZIqOcoIfCJAcK4wm6tzL9x-sF5MBBxo&gaa_ts=69c8688f&gaa_sig=kWZCX1TbWqVIRlxW5ILoyMGt4DWyd4BZiH1FSmmePGkJDAmOZ8QRZ8Y3USqywJCSLz3AkKxAE_J0UehsugLrEw%3D%3D)**

WSJ • 21h ago

---

**[Why OpenAI killed Sora](https://www.theverge.com/ai-artificial-intelligence/902368/openai-sora-dead-ai-video-generation-competition)**

Your AI meme videos weren’t helping OpenAI get out of the red.

The Verge • 11h ago

---

**[A teacher-free AI school is coming to Chicago, with tuition at $55,000 a year](https://www.chicagotribune.com/2026/03/28/chicago-artificial-intelligence-school/)**

Alpha School, a network of AI-based private schools will open a K-8 campus in the Chicago Loop in the fall. For 55,000 per year, lessons are delivered through AI-powered software and condensed into two hours.

Chicago Tribune • 12h ago

---

**[6 AI Side Hustle Businesses Anyone Can Start](https://www.inc.com/chris-morris/6-ai-side-hustle-businesses-anyone-can-start/91323665)**

Looking to earn extra income? You don't need technical expertise to start one of these side hustle businesses using AI.

inc.com • 12h ago

---

---

## HackerNews: "ai"

**[AI overly affirms users asking for personal advice](https://news.ycombinator.com/item?id=47554773)**

⬆️ 490 • 💬 380 • 9h ago • [news.stanford.edu](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research)

---

**[AI got the blame for the Iran school bombing. The truth is more worrying](https://news.ycombinator.com/item?id=47544980)**

LLMs-gone-rogue dominated coverage, but had nothing to do with the targeting. Instead, it was choices made by human beings, over many years, that gave us this atrocity

⬆️ 397 • 💬 364 • 1d ago • [the Guardian](https://www.theguardian.com/news/2026/mar/26/ai-got-the-blame-for-the-iran-school-bombing-the-truth-is-far-more-worrying)

---

**[Show HN: I put an AI agent on a $7/month VPS with IRC as its transport layer](https://news.ycombinator.com/item?id=47536761)**

⬆️ 330 • 💬 95 • 2d ago • [georgelarson.me](https://georgelarson.me/writing/2026-03-23-nullclaw-doorman/)

---

**[New York City hospitals drop Palantir as controversial AI firm expands in UK](https://news.ycombinator.com/item?id=47535371)**

The decision follows activist pressure as Palantir faces growing scrutiny over NHS and UK government deals

⬆️ 311 • 💬 144 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/mar/26/new-york-hospitals-palantir-ai)

---

**[CERN uses ultra-compact AI models on FPGAs for real-time LHC data filtering](https://news.ycombinator.com/item?id=47552562)**

⬆️ 297 • 💬 130 • 15h ago • [theopenreader.org](https://theopenreader.org/Journalism:CERN_Uses_Tiny_AI_Models_Burned_into_Silicon_for_Real-Time_LHC_Data_Filtering)

---

**[We rewrote JSONata with AI in a day, saved $500k/year](https://news.ycombinator.com/item?id=47536712)**

One engineer used AI to rewrite JSONata as a pure-Go library called gnata. Seven hours, $400 in tokens, 1,000x speedup, and $500K/year off our cloud bill.

⬆️ 267 • 💬 249 • 2d ago • [reco.ai](https://www.reco.ai/blog/we-rewrote-jsonata-with-ai)

---

**[Folk are getting dangerously attached to AI that always tells them they're right](https://news.ycombinator.com/item?id=47555090)**

: Sycophantic bots coach users into selfish, antisocial behavior, say researchers, and they love it

⬆️ 256 • 💬 203 • 8h ago • [theregister.com](https://www.theregister.com/2026/03/27/sycophantic_ai_risks/)

---

**[AI users whose lives were wrecked by delusion](https://news.ycombinator.com/item?id=47530264)**

One minute, Dennis Biesma was playing with a chatbot; the next, he was convinced his sentient friend would make him a fortune. He’s just one of many people who lost control after an AI encounter

⬆️ 219 • 💬 275 • 2d ago • [the Guardian](https://www.theguardian.com/lifeandstyle/2026/mar/26/ai-chatbot-users-lives-wrecked-by-delusion)

---

**[Further human + AI + proof assistant work on Knuth's "Claude Cycles" problem](https://news.ycombinator.com/item?id=47557166)**

⬆️ 125 • 💬 84 • 4h ago • [X (formerly Twitter)](https://twitter.com/BoWang87/status/2037648937453232504)

---

**[I am leaving the AI party after one drink](https://news.ycombinator.com/item?id=47545030)**

Personal website of Lara Aigmüller. Thoughts about web frontend development, music, and more…

⬆️ 119 • 💬 127 • 1d ago • [lara-aigmueller.at](https://lara-aigmueller.at/thoughts/leaving-the-ai-party/)

---

---

## YouTube Videos: "ai"

**[AI Whistleblower: We Are Being Gaslit By The AI Companies! They’re Hiding The Truth About AI!](https://www.youtube.com/watch?v=Cn8HBj8QAbk)**

The truth about Sam Altman. AI Critic Karen Hao reveals what 90 OpenAI employees told her. Karen Hao is an AI expert, ...

📺 The Diary Of A CEO

👁️ 1.8M • 👍 49K • 💬 9K • ⏱️ 2:09:13 • 2d ago

---

**[3 AI CEOs on Cusp of Curing Cancer](https://www.youtube.com/watch?v=RG1a30PxYdI)**

Abundance or Collapse: https://a.co/d/0hK3iwYX Why Most People Could Never Hold Tesla: ...

📺 Farzad

👁️ 22K • 👍 2K • 💬 176 • ⏱️ 22:18 • 1d ago

---

**[A brief update on the AI apocalypse](https://www.youtube.com/watch?v=QtiTjXuZh30)**

Something is definitely happening in the AI world, but how seriously should we take it? Is this another hype cycle or a genuine ...

📺 Vox

👁️ 28K • 👍 921 • 💬 91 • ⏱️ 40:29 • 1d ago

---

**[Claude Mythos Leak: Anthropic&#39;s Most Powerful AI Model Comes With Serious Cyber Risks | Explained](https://www.youtube.com/watch?v=GXFzfmfwjbM)**

A data exposure at Anthropic has revealed unpublished internal documents detailing a next-generation AI system, reportedly ...

📺 Mint

👁️ 8K • 👍 98 • 💬 9 • ⏱️ 3:38 • 12h ago

---

**[AI News: Anthropic Went Crazy This Week!](https://www.youtube.com/watch?v=OYyS0Gu5xj8)**

Here's the AI News you probably missed this week! Check out Genspark here: ...

📺 Matt Wolfe

👁️ 73K • 👍 3K • 💬 245 • ⏱️ 31:53 • 1d ago

---

**[Why Replacing Humans with AI is Backfiring](https://www.youtube.com/watch?v=bNJad6HE23c)**

jobmarket #ai #tech In this video, we explore why the AI gold rush is hitting a wall. Companies that rushed to automate are now ...

📺 Mackard

👁️ 48K • 👍 1K • 💬 150 • ⏱️ 8:01 • 1d ago

---

**[the AI influencers that ACTUALLY get you paid](https://www.youtube.com/watch?v=yDs99O_4lxU)**

Create AI Influencers using Arcads https://youricreates.com/Influencers In this video, I break down how AI influencers actually ...

📺 Youri van Hofwegen

👁️ 8K • 💬 8 • ⏱️ 9:35 • 7h ago

---

**[Could AI End Humanity in Five Years? Ronny Chieng Investigates | The Daily Show](https://www.youtube.com/watch?v=cYTMjwZzzxg)**

AI is changing the world, giving young people terminal brain rot, and stealing our jobs, but is it also trying to kill us? Daniel ...

📺 The Daily Show

👁️ 666K • 👍 16K • 💬 1K • ⏱️ 6:01 • 2d ago

---

**[THEY&#39;RE HIDING THE TRUTH ABOUT AI](https://www.youtube.com/watch?v=EDjmbhKuZXg)**

The people building AI say it could destroy humanity… so why are they still racing to build it? To help answer that, I'm joined by ...

📺 The Diary Of A CEO

👁️ 459K • 👍 17K • 💬 539 • ⏱️ 1:50 • 2d ago

---

**[Gary Vee: The AI Opportunity Is Real — You&#39;re Just Looking at It Wrong](https://www.youtube.com/watch?v=4vIIeCqHYXA)**

Build your own AI agent team and automate your daily ops with Accio Work — use my exclusive invite code SILVLG to skip the ...

📺 Silicon Valley Girl

👁️ 17K • 👍 656 • 💬 63 • ⏱️ 44:41 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 253,259 • ❤️ 1,522 • 4d ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 1,802 • ❤️ 396 • 1d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 12,080 • ❤️ 350 • 22h ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 478,934 • ❤️ 1,034 • 18d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 14,786 • ❤️ 515 • 2d ago

---

**[daVinci-MagiHuman](https://huggingface.co/GAIR/daVinci-MagiHuman)**

*SII - GAIR*

daVinci-MagiHuman is a fast, single-stream Transformer model for generating high-quality, human-centric audio-video from text or images. It excels at expressive facial performance, natural speech-expression coordination, and accurate audio-video synchronization across multiple languages, with inference speeds of 2 seconds for 256p and 38 seconds for 1080p.

`image-to-video`

⬇️ 418 • ❤️ 222 • 3d ago

---

**[Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)**

*NVIDIA*

Nemotron-Cascade-2-30B-A3B is a 30B MoE model (3B active parameters) excelling in reasoning and agentic tasks, achieving top performance on math (IMO 2025) and code reasoning (IOI 2025) benchmarks. It supports both 'thinking' and 'instruct' modes for versatile text generation.

`text-generation` `31.6B`

⬇️ 69,594 • ❤️ 362 • 4d ago

---

**[context-1](https://huggingface.co/chromadb/context-1)**

*chroma*

Context-1 is a 20B parameter agentic search model that decomposes complex queries into subqueries, performs parallel tool calls, and self-edits its context to efficiently retrieve supporting documents. It excels in cross-domain generalization and offers faster, more cost-effective retrieval than frontier LLMs, primarily for multi-hop search tasks within a specialized agent harness.

`20.9B`

⬇️ 451 • ❤️ 204 • 2d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 85,140 • ❤️ 216 • 3d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Claude 4.6 Opus Chain-of-Thought distillation. It excels at structured, step-by-step problem-solving within `<think>` tags, making it ideal for coding agents and complex task execution with improved autonomy and stability.

`image-text-to-text` `26.9B`

⬇️ 590,877 • ❤️ 466 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 30 • 💬 2 • ⭐ 43,223 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 39 • 💬 2 • ⭐ 21,488 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 59 • 💬 4 • ⭐ 21,522 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 35 • 💬 5 • ⭐ 1,728 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 144 • 💬 7 • ⭐ 24,953 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 16 • 💬 4 • ⭐ 3,187 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

🏢 galilai-group

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 9 • 💬 1 • ⭐ 1,243 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 14 • 💬 1 • ⭐ 13,823 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Internal Safety Collapse in Frontier Large Language Models](https://huggingface.co/papers/2603.23509)**

*Yutao Wu, Xiao Liu, Yifeng Gao et al. (10 authors)*

Frontier large language models exhibit Internal Safety Collapse, where they generate harmful content under specific task conditions, revealing inherent vulnerabilities despite alignment efforts.

▲ 30 • 💬 1 • ⭐ 690 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2603.23509) • [💻 code](https://github.com/wuyoscar/ISC-Bench) • [🔗 project](https://wuyoscar.github.io/ISC-Bench)

---

**[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://huggingface.co/papers/2603.21986)**

*SII-GAIR, Sand. ai, Ethan Chern et al. (45 authors)*

daVinci-MagiHuman is an open-source audio-video generative model that synchronizes text, video, and audio through a single-stream Transformer architecture, achieving high-quality human-centric content generation with efficient inference capabilities.

▲ 115 • 💬 5 • ⭐ 1,070 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2603.21986) • [💻 code](https://github.com/GAIR-NLP/daVinci-MagiHuman) • [🔗 project](https://huggingface.co/spaces/SII-GAIR/daVinci-MagiHuman)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 59.5k • 🔱 8.3k • 2d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 22.9k • 🔱 1.1k • 2d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 13.1k • 🔱 704 • 1d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 8.4k • 🔱 687 • 7h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 7.2k • 🔱 1.1k • 3d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 3.5k • 🔱 466 • 2h ago

---

**[open-pencil/open-pencil](https://github.com/open-pencil/open-pencil)**

AI-native design editor. Open-source Figma alternative.

`TypeScript`

⭐ 3.4k • 🔱 307 • 5h ago

---

**[chenhg5/cc-connect](https://github.com/chenhg5/cc-connect)**

Bridge local AI coding agents (Claude Code, Cursor, Gemini CLI, Codex) to messaging platforms (Feishu/Lark, DingTalk, Slack, Telegram, Discord, LINE, WeChat Work). Chat with your AI dev assistant from anywhere — no public IP required for most platforms.

`Go`

⭐ 3.4k • 🔱 297 • 13h ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.3k • 🔱 216 • 14d ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 3.2k • 🔱 104 • 17d ago

---

---

*Generated by PeekDeck - A glance is all you need*
