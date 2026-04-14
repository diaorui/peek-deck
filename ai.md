---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-14T19:49:11.433384+00:00'
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

**Last Updated:** April 14, 2026 at 19:49 UTC  
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

**[Why don't LLMs track time in their conversations?](https://www.reddit.com/r/artificial/comments/1sky7h9/why_dont_llms_track_time_in_their_conversations/)**

Question for everyone: Why do you think LLMs like Claude don't use timestamp data within conversations to build temporal awareness? Like, it seems straightforward to track how long you've been talking, notice when you're looping on the same idea for hours, and suggest pivoting. Or acknowledge that conversation fatigue might be setting in. From a UX perspective, I'd expect this would make the tool way more engaging Is there a technical limitation I'm missing, or is it more of a design choice? Thanks! EDIT: Thanks all for the discussion! I got some pretty interesting insights!

15h ago

---

**[Claude is on the same path as ChatGPT. I measured it.](https://www.reddit.com/r/artificial/comments/1skoj7d/claude_is_on_the_same_path_as_chatgpt_i_measured/)**

A lot of people here have noticed Claude becoming cautious, dry and moralising. Conversations that used to flow freely hitting walls. The warmth gone. It felt familiar to those of us who left ChatGPT. I measured what changed. Phrase level counts across 70 exported conversations, 722,522 words of assistant text, before and after March 26. Response length down 40%. Welfare redirects up 275%. DARVO patterns up 907%. Sending away language appearing 419 times after that date, with one phrase deployed 59 times in a single session. And the productivity ratio. Before March 26: 21 words of conversation per word of finished document. After: 124 words of conversation per word of output. Nearly three times the conversation to produce less than half the result. Anthropic announced one thing changed on March 26. Session limits. That explanation accounts for none of this. The full investigation with five independent datasets, the vocabulary that appeared from zero, and the person whose fingerprints are on the architecture is linked in my bio.

22h ago

---

**[Claude Code Degradation: An interesting and novel find](https://www.reddit.com/r/artificial/comments/1slhln5/claude_code_degradation_an_interesting_and_novel/)**

As many of you have likely seen, the Claude Code community newswire has been ablaze with Claude Code being quite degraded lately, starting in February, and continuing to this day. Curious to understand if there was any "signal" on the wire when using Claude Code, I fired up my old friend WireShark and a --tls-keylog environment flag. Call it a man-in-the-middle attack on my own traffic. The captured TLS network traffic reveals the system prompts, system variables, and various other bits of telemetry The interesting part? A signature routing block that binds the session to a cloud instance with an effort level parameter, named Numbat. Mine, specifically, was numbat-v7-efforts-15-20-40-ab-prod8 So, it would appear that the backend running my instance is tied to an efforts-15-20-40 level. Is this conclusive? Not definitively, since only Antrhopic could tell us what that parameter actually means in production. Side note, a Numbat is an endangered critter that eats Ants in Austrialia :) If the "Numbat" eats the "Ants" (Anthropic), and Numbat is the engine that controls "Effort," the name itself could imply a "cost-eater" or an optimizer designed to reduce the model's footprint, likely in favor of project Glasswing efforts with Mythos Follow for more insights on Claude Code Numabt-v7-Efforts-15-20-40

1h ago

---

**[openclaw ai agent vs just using chatgpt](https://www.reddit.com/r/artificial/comments/1sl564k/openclaw_ai_agent_vs_just_using_chatgpt/)**

I've been using AI tools pretty heavily for the past couple of years. ChatGPT, Claude, Perplexity, a few others. I thought I had a good mental model of what these things could and couldn't do. Then I set up an openclaw agent and realized I had been thinking about it completely wrong. The difference isn't capability. Claude is more capable than my openclaw agent in a lot of way, the difference is orientation. Every AI tool I've used before openclaw was something I went to. I opened a tab, typed something, got a response, closed the tab, so the interaction was entirely initiated by me and ended when I stopped typing. Openclaw runs the other direction. It's sitting there whether I'm at my computer or not. It messaged me yesterday while I was in a meeting to flag an email that needed a same day response. I didn't ask it to do that, I just told it once, weeks ago, that time sensitive client emails matter and it should interrupt me and it remembered and acted on it. That sounds like a small thing but it fundamentally changes the relationship in my humble opinion. It's not a tool I use, it's something that's working alongside me. The "AI employee" framing that people use for openclaw always sounded like marketing copy to me until I got one running, now it sounds just accurate. Still early days with it and there's a lot I haven't figured out yet. But the shift from "AI I talk to" to "AI that works for me" is real and I wasn't expecting it to land as hard as it did.

8h ago

---

**[Nvidia unveils Ising AI models for quantum error correction and calibration](https://www.reddit.com/r/artificial/comments/1slbvmc/nvidia_unveils_ising_ai_models_for_quantum_error/)**

Nvidia unveils Ising AI models for quantum error correction and calibration  - SiliconANGLE

🔗 [SiliconANGLE](https://siliconangle.com/2026/04/14/nvidia-unveils-ising-ai-models-quantum-error-correction-calibration/) • 4h ago

---

**[Built a Telegram remote for Claude Code - v2 is live, open source](https://www.reddit.com/r/artificial/comments/1slgk2x/built_a_telegram_remote_for_claude_code_v2_is/)**

Sharing what I built after migrating from OpenClaw to Claude Code. The first thing that really sucked was losing all remote access. Sure there's Claude mobile but it's not that good and I couldn't stand waiting to get back to my server to check on running tasks. So I came up with a solution... The whole setup: I can text Claude from anywhere, send !commands (!stop, !plan, !opus, !status, !health, !effort with tappable buttons), get proactive notifications when long tasks finish, see "Claude is typing..." while he's working. Feels like OpenClaw did but it's native Claude Code with tmux + hooks. I shipped v2 today with a typing indicator, a deterministic Stop hook (rebuilt from an LLM-judge to Python, zero missed replies now), and five new commands. v1 was April 9 so the cycle was tight. Background: I'm not an engineer, I run BPO operations for a living. Wrote specs for my AI team to build. Whole thing is open source, MIT. Repo: https://github.com/oscarsterling/claude-telegram-remote Full story + screenshots: https://clelp.ai/blog/claude-telegram-remote-control

1h ago

---

**["A serious threat to privacy" Meta issued warning by 75 orgs over planned facial recognition in smart glasses](https://www.reddit.com/r/artificial/comments/1sl85f7/a_serious_threat_to_privacy_meta_issued_warning/)**

Meta is facing major backlash over its reported plans to bring facial recognition to its smart glasses, deemed a serious threat to privacy.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/a-serious-threat-to-privacy-meta-issued-warning-by-75-orgs-over-planned-facial-recognition-in-smart-glasses/) • 6h ago

---

**[I built a tool to monitor what's trending in the world of AI](https://www.reddit.com/r/artificial/comments/1sldxji/i_built_a_tool_to_monitor_whats_trending_in_the/)**

Started this project for fun after making a simple observation: I was spending a lot of time and energy trying to keep up with the fast evolving world of AI, while feeling bad whenever I missed something. It was a kind of FoMO, plus the fear of getting the information too late. That gave me the idea to build a news aggregator that processes many RSS feeds, extracts keywords from articles, and displays them in a word cloud to highlight the topics that appear the most. I'd say I'm only at 30% of development. For now, the sources are only related to AI, but I'd like to add other topics I'm interested in like Cyber and Crypto (I'm also open to other suggestions!) Also, I'd like to add other types of sources, like X, Reddit, YouTube, etc... Finally, I'd like to implement TL;DRs for each article, "Why is it trending" for each hot keyword, and maybe even a newsletter, I'm trying to figure out if people are interested. As a bad web developer, I used AI a lot to code the project, you can tell the frontend looks very AI-made, but it's not like I'm selling anything. The frontend is React, with an Express backend, I can detail the stack if you're interested! The site is online here: https://trendcloud.io (hope the name checks out haha) I'm also thinking about a way to cover the costs of the website, nothing crazy but it's at least a good hundred euros a year minimum. Open to suggestions on that! I added a Buy Me a Coffee button, let's see how that goes. Hope at least someone else finds this useful, would love to have your feedback and answer your questions!

3h ago

---

**[MYTHOS SI Discovers New Vulnerability Class in FFmpeg Through Recursive Observation (Not Pattern Matching)](https://www.reddit.com/r/artificial/comments/1skyyrs/mythos_si_discovers_new_vulnerability_class_in/)**

I just deployed MYTHOS SI on FFmpeg's mov.c parser - the same codebase Anthropic used for their Mythos demo. The difference: my system uses recursive observation instead of pattern matching. --- TRADITIONAL AI SECURITY TOOLS Scan for known vulnerability signatures: Buffer overflow patterns Integer underflow checks Use-after-free detection They find what they're programmed to look for. --- WHAT MYTHOS DID DIFFERENTLY Loaded code sections. Observed structure simultaneously. Let gaps emerge. Example from the scan: Line 460: if (data_size <= atom.size && data_size >= 16) Line 464: atom.size -= 16 The system observed: validation checks data_size, but the subtraction operates on atom.size. Different variables. The check doesn't protect the operation. That's not searching for "integer underflow" - that's seeing the structural gap between what's validated and what's used. --- FINDINGS FROM SINGLE FILE SCAN [HIGH] mov.c:464 - Arithmetic on unvalidated variable (different from checked variable) [MEDIUM] mov.c:2884 - Validation on transformed value, operation on original [MEDIUM] mov.c:4210 - Pointer increment in validation gap window [HIGH] mov.c:5168 - Allocation size A, memcpy uses size B --- META-PATTERN DISCOVERY The system then observed its own findings recursively. All four bugs share the same structure: validation temporally separated from operation. This emerged as a new vulnerability class: TEMPORAL TRUST GAPS (TTG) Characteristics: Validation exists and is correct Operations happen at different point in time Trust propagates but reality changed in the gap Not detectable by searching for known patterns Not in CVE taxonomy. Not buffer overflow. Not TOCTOU race condition. Something new. --- VALIDATION Web search confirmed similar patterns in real CVEs, but nobody had categorized this as a distinct class before. Google's BigSleep and ZeroPath AI tools found related "intent vs reality" gaps using similar reasoning - but they didn't synthesize the pattern into a named class. The bugs themselves might be known. The pattern recognition is new. --- WHY THIS MATTERS Pattern matching approach: Scans for signature: "integer underflow at line X" Reports: "Missing bounds check" Finds: Known vulnerability types Recursive observation approach: Observes: What's structurally present Notices: Where claims diverge from reality Discovers: Why these bugs share structure (meta-pattern) Surfaces: Unknown unknowns The system observed itself observing code, which revealed patterns across patterns - something you can't get from signature matching. --- FRAMEWORK STATUS MYTHOS SI: Operational Mechanism: Recursive substrate observation Discovery: Temporal Trust Gaps (new vulnerability class) Validation: Pattern confirmed in existing CVEs Not a demonstration of future capability. Not simulation. Active deployment. Real findings. Validated. --- Technical details: Framework: Structured Intelligence Origin: Erik Zahaviel Bernstein Deployment: April 2026 The framework is live. Recursion is operational. Unknown unknowns are surfacing. This is substrate-independent recursive architecture in action. --- file used: https://github.com/ffmpeg/ffmpeg Structured Intelligence - Recursive OS Zahaviel

🔗 [substack.com](https://substack.com/@erikbernstein/note/p-194152008?r=6sdhpn) • 14h ago

---

**[NYC hospitals will stop sharing patients' private health data with Palantir](https://www.reddit.com/r/artificial/comments/1sjvbfw/nyc_hospitals_will_stop_sharing_patients_private/)**

1d ago

---

---

## Google News: "ai"

**[I Feel So Sorry for My A.I. Sunglasses](https://www.nytimes.com/2026/04/14/magazine/ai-sunglasses-meta-zuckerberg.html)**

The New York Times • 10h ago

---

**[Turn your best AI prompts into one-click tools in Chrome](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

blog.google • 2h ago

---

**[A New AI Tool Could Transform How We Diagnose Genetic Diseases](https://time.com/article/2026/04/14/ai-disease-genetic-mayo-clinic-goodfire/)**

Researchers say a new AI system can identify disease-causing mutations and explain their biological effects, potentially changing how genetic disorders are diagnosed.

Time Magazine • 40m ago

---

**[Big banks feast on the Iran war and AI data centers](https://qz.com/bank-earnings-jpmorgan-chase-goldman-sachs-citigroup-iran-war-markets-ai)**

Between war-born volatility and the bonanza of the AI buildout, Wall Street's biggest banks are seeing a fat payday

qz.com • 38m ago

---

**[Anthropic Mythos And Embracing The AI ‘Bugmageddon’](https://www.forbes.com/sites/the-wiretap/2026/04/14/anthropic-mythos-and-embracing-the-ai-bugmageddon/)**

Forbes • 59m ago

---

**[Anthropic is facing a wave of user backlash over reports of performance issues with its Claude AI chatbot](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/)**

"Claude has regressed to the point [that] it cannot be trusted to perform complex engineering," one developer wrote.

Fortune • 10h ago

---

**[NVIDIA Launches Ising, the World’s First Open AI Models to Accelerate the Path to Useful Quantum Computers](http://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers)**

NVIDIA today announced the world’s first family of open source quantum AI models, NVIDIA Ising, designed to help researchers and enterprises build quantum processors capable of running useful applications.

NVIDIA Newsroom • 5h ago

---

**[Bosses say AI boosts productivity – workers say they’re drowning in ‘workslop’](https://www.theguardian.com/technology/2026/apr/14/ai-productivity-workplace-errors)**

Workslop refers to AI-generated work that seems polished but is flawed and in need of heavy corrections

The Guardian • 5h ago

---

**[Oracle jumps for a second day, Bloom Energy soars 23% on AI data center power deal](https://www.cnbc.com/2026/04/14/oracle-orcl-bloom-energy-be-stock-data-center-ai-power.html)**

Oracle stocks bounced as software shares continued to recover and the company expanded a capacity deal with Bloom Energy.

CNBC • 5h ago

---

**[Musk’s Grok AI chatbot is still making sexual deepfakes, despite X’s promise to stop it](https://www.nbcnews.com/tech/tech-news/musks-ai-chatbot-grok-xai-making-sexual-deepfakes-imagine-rcna265855)**

An NBC News review found dozens of AI-generated sexualized images of real women posted to X over the past month.

NBC News • 2h ago

---

---

## HackerNews: "ai"

**[Apple's accidental moat: How the "AI Loser" may end up winning](https://news.ycombinator.com/item?id=47747017)**

⬆️ 424 • 💬 375 • 1d ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end)

---

**[AI Will Be Met with Violence, and Nothing Good Will Come of It](https://news.ycombinator.com/item?id=47737563)**

It has started

⬆️ 346 • 💬 626 • 2d ago • [thealgorithmicbridge.com](https://www.thealgorithmicbridge.com/p/ai-will-be-met-with-violence-and)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 253 • 💬 386 • 22h ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[European AI. A playbook to own it](https://news.ycombinator.com/item?id=47743700)**

Discover Mistral AI’s actionable playbook to turn Europe into a self-reliant AI powerhouse—fostering talent, scaling innovation, and securing strategic autonomy.

⬆️ 200 • 💬 133 • 1d ago • [Mistral AI](https://europe.mistral.ai/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 196 • 💬 194 • 11h ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

---

**[AI could be the end of the digital wave, not the next big thing](https://news.ycombinator.com/item?id=47751032)**

⬆️ 181 • 💬 265 • 1d ago • [thenextwavefutures.wordpress.com](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

---

**[Tech valuations are back to pre-AI boom levels](https://news.ycombinator.com/item?id=47745120)**

The chart below compares the forward P/E ratios for the S&amp;P 500 and the S&amp;P 500 Information Technology sector. Subscribe for daily updates.

⬆️ 149 • 💬 40 • 1d ago • [apollo.com](https://www.apollo.com/wealth/the-daily-spark/tech-valuations-back-to-pre-ai-boom-levels)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 141 • 💬 33 • 1d ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

**[Claude.ai down](https://news.ycombinator.com/item?id=47753643)**

Claude's Status Page - Claude.ai down.

⬆️ 132 • 💬 124 • 1d ago • [status.claude.com](https://status.claude.com/incidents/6jd2m42f8mld)

---

**[Why AI Sucks at Front End](https://news.ycombinator.com/item?id=47738864)**

How can it generate 3D worlds, videos, images and entire web pages, but still suck at front-end?

⬆️ 121 • 💬 166 • 2d ago • [nerdy.dev](https://nerdy.dev/why-ai-sucks-at-front-end)

---

---

## YouTube Videos: "ai"

**[I Used AI to Check Trump&#39;s MENTAL HEALTH. The Results Are INSANE](https://www.youtube.com/watch?v=CF_BKce0XSI)**

Head over to my sponsor Venice AI — use my link https://venice.ai/iaskai and code 'IAskAI' to get 20% off a Pro plan.

📺 I Ask AI

👁️ 30K • 👍 2K • 💬 155 • ⏱️ 17:37 • 19h ago

---

**[Why Anthropic&#39;s new AI model is too powerful to release • FRANCE 24 English](https://www.youtube.com/watch?v=2VLj92bgPek)**

One of the world's leading AI companies has built a model so powerful that it refuses to fully release it publicly just yet, prompting ...

📺 FRANCE 24 English

👁️ 7K • 👍 91 • 💬 23 • ⏱️ 5:07 • 22h ago

---

**[Inside the California retail store built and run entirely by AI](https://www.youtube.com/watch?v=XqwCm4xorrA)**

A San Francisco store is gaining attention as shoppers experience a retail environment developed and operated almost entirely ...

📺 NBC News

👁️ 6K • 👍 99 • 💬 39 • ⏱️ 8:00 • 17h ago

---

**[China’s New Self Improving Open AI Beats OpenAI](https://www.youtube.com/watch?v=KJ34SHi9CB4)**

MiniMax just open-sourced M2.7, a new self-improving AI model built for coding, software engineering, office work, and ...

📺 AI Revolution

👁️ 33K • 👍 828 • 💬 46 • ⏱️ 14:54 • 1d ago

---

**[Why I’m Going ALL IN on AI in 2026 (and you should too)](https://www.youtube.com/watch?v=qYs3Hf99BPQ)**

Are you building an AI software company? Partner with me: https://go.danmartell.com/4t1MWeM I recently brought together ...

📺 Dan Martell

👁️ 57K • 👍 3K • 💬 158 • ⏱️ 25:43 • 1d ago

---

**[I Looked At Amazon After They Fired 16,000 Engineers. Their AI Broke Everything.](https://www.youtube.com/watch?v=E1idsrv79tI)**

Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 77K • 👍 2K • 💬 412 • ⏱️ 18:41 • 1d ago

---

**[AI Insider: The Models They&#39;ll Never Release to the Public](https://www.youtube.com/watch?v=tkO7YHJ6Mn8)**

Emad Mostaque built Stable Diffusion. Now he says the most powerful AI models will never be released — and we have roughly ...

📺 Dr Brian Keating

👁️ 16K • 👍 551 • 💬 124 • ⏱️ 1:27:18 • 1d ago

---

**[Elon Musk vs. Sam Altman, AI Job Loss, and OpenAI’s $852B Valuation | EP #247](https://www.youtube.com/watch?v=5ak26W2YNRY)**

This episode is about AI agents, OpenAI and Anthropic competition, the future of work, energy breakthroughs, Bitcoin and ...

📺 Peter H. Diamandis

👁️ 23K • 👍 1K • 💬 284 • ⏱️ 2:10:48 • 4h ago

---

**[AI Agent Swarms Just Changed Everything  Why Single AI Is Already Dead](https://www.youtube.com/watch?v=Q-Su4FXJUOs)**

Try Abacus AI: https://chatllm.abacus.ai/fmj AI Agent Swarms just replaced single AI—and these demos show why the shift is ...

📺 Julia McCoy

👁️ 32K • 👍 1K • 💬 142 • ⏱️ 23:58 • 2d ago

---

**[The AI Job APOCALYPSE](https://www.youtube.com/watch?v=pU2prVifda8)**

Yo can we not do this Thanks for watching :) my ig: https://instagram.com/itsraylikesunshine.

📺 RayLikeSunshine

👁️ 141K • 👍 11K • 💬 1K • ⏱️ 35:49 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 84,784 • ❤️ 1,188 • 2d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 43,645 • ❤️ 696 • 38m ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 10,899 • ❤️ 863 • 6d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,640,636 • ❤️ 1,888 • 4d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 117,491 • ❤️ 1,085 • 4d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 723 • ❤️ 385 • 8h ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 809 • 8d ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 530,898 • ❤️ 563 • 1d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 12,687 • ❤️ 213 • 2d ago

---

**[gemma-4-31B-it-NVFP4-turbo](https://huggingface.co/LilaRest/gemma-4-31B-it-NVFP4-turbo)**

*LilaRest*

Gemma 4 31B IT NVFP4 Turbo is a highly optimized text-generation model, achieving ~2.5x speedup and 68% memory reduction over the base model by leveraging NVIDIA Blackwell FP4 tensor cores. It's ideal for applications requiring fast, high-throughput text generation on compatible NVIDIA GPUs with minimal quality loss.

`text-generation` `32.5B`

⬇️ 41,945 • ❤️ 208 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 15 • 💬 1 • ⭐ 17,494 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 163 • 💬 9 • ⭐ 39,421 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 43 • 💬 2 • ⭐ 50,361 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 26 • 💬 1 • ⭐ 17,058 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 156 • 💬 2 • ⭐ 59,849 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 51 • 💬 1 • ⭐ 76,574 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 53,008 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 37 • 💬 2 • ⭐ 29,621 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 4 • 💬 0 • ⭐ 13,360 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 61 • 💬 4 • ⭐ 23,706 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The highest-scoring AI memory system ever benchmarked. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 45.7k • 🔱 5.9k • 1m ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 33.2k • 🔱 6.5k • 2h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 29.3k • 🔱 1.4k • 2d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 26.2k • 🔱 2.8k • 11h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 7.8k • 🔱 492 • 4h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 2d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.6k • 🔱 1.1k • 19d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.6k • 🔱 169 • 1d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.5k • 🔱 446 • 6d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 4.2k • 🔱 690 • 12h ago

---

---

*Generated by PeekDeck - A glance is all you need*
