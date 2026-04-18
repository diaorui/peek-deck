---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-18T09:01:42.763618+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 18, 2026 at 09:01 UTC  
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

**[Opus 4.7 is terrible, and Anthropic has completely dropped the ball](https://www.reddit.com/r/artificial/comments/1so16hr/opus_47_is_terrible_and_anthropic_has_completely/)**

Tried posting this in r/ClaudeAI but it got auto-removed, and I was told to post it in the "Bugs Megathread." Don't really think it should been removed, but whatever, I'll just post it here since I'm sure it's still relevant. Like a lot of people, I switched from ChatGPT to Claude not too long ago during the whole DoW fiasco and Sam Altman “antics.” At first, I was genuinely impressed. I do fairly heavy theoretical math and physics research, and Opus 4.6 was simply the best tool I’d used for synthesizing ideas and working through complex logic. But the last few weeks have been really disappointing, and I’m seriously considering going back to GPT (even though, for personal reasons, I’d really rather not). How many times has Claude been down recently? And why is it that I can ask Claude 4.7 (with adaptive thinking turned on) to work through a detailed proof, and it just spirals “oh wait, that doesn’t work, let me try again” five times in a single response? Yes, there’s a workaround to explicitly tell it to think before answering. But… why is that necessary? I’m paying $20/month. This is supposed to be a top-tier model. Instead, it burns through time, second-guesses itself mid-response, and often fails to land anywhere useful on problems I’m fairly sure 4.6 would have handled more coherently a month ago. And then before I know it I hit the usage limit. I’m a PhD student. I can’t justify spending $100-$200/month on higher tiers. $20 has always been enough for me, and I’ve come to rely on these tools for my research. I expected to stick with Claude long-term, but the recent instability and drop in reliability make it hard to justify paying for it out of pocket. It’s frustrating to feel pushed toward a competitor because of this. But at a certain point, the usability of the product has to come first. Really disappointing.

19h ago

---

**[Google patents AI tech that will personalize websites and make them look different for everyone](https://www.reddit.com/r/artificial/comments/1so3vto/google_patents_ai_tech_that_will_personalize/)**

The patent describes a system that uses artificial intelligence to create personalized web pages for each user.

🔗 [PC Guide](https://www.pcguide.com/news/google-patents-ai-tech-that-will-personalize-websites-and-make-them-look-different-for-everyone/) • 17h ago

---

**[Reese Witherspoon Doubles Down on Telling Women to Learn AI: Jobs We Hold Are "Three Times More Likely to Be Automated By AI"](https://www.reddit.com/r/artificial/comments/1snqqjo/reese_witherspoon_doubles_down_on_telling_women/)**

Reese Witherspoon is again advising her followers that there's no time like the present to start learning about and using artificial intelligence.

🔗 [Variety](https://variety.com/2026/tv/news/reese-witherspoon-ai-jobs-women-1236723992/) • 1d ago

---

**[We added cryptographic approval to our AI agent… and it was still unsafe](https://www.reddit.com/r/artificial/comments/1sorsxu/we_added_cryptographic_approval_to_our_ai_agent/)**

We’ve been working on adding “authorization” to an AI agent system. At first, it felt solved: - every action gets evaluated - we get a signed ALLOW / DENY - we verify the signature before execution Looks solid, right? It wasn’t. We hit a few problems almost immediately: The approval wasn’t bound to the actual execution Same “ALLOW” could be reused for a slightly different action. No state binding Approval was issued when state = X Execution happened when state = Y Still passed verification. No audience binding An approval for service A could be replayed against service B. Replay wasn’t actually enforced at the boundary Even with nonces, enforcement wasn’t happening where execution happens. So what we had was: a signed decision What we needed was: a verifiable execution contract The difference is subtle but critical: - “Was this approved?” -> audit question - “Can this execute?” -> enforcement question Most systems answer the first one. Very few actually enforce the second one. Curious how others are thinking about this. Are you binding approvals to: - exact intent? - execution state? - execution target? Or are you just verifying signatures and hoping it lines up?

43m ago

---

**[The AI Wearable Ecosystem: Closer than you think. Socially acceptable?](https://www.reddit.com/r/artificial/comments/1sors65/the_ai_wearable_ecosystem_closer_than_you_think/)**

I've been researching how personal AI tech devices are likely to develop ... technical capabilities, form factors, privacy and governance issues etc. I think it looks likely that there won't be one 'must have' device, and that there'll be more of a wearable ecosystem, with devices for different environments ... Glasses: outward and inward cameras, picking up facial expressions, gestures etc. Bone conduction audio. Augmented VR, infrared overlay etc. Cuff/Wristband: beyond a smart watch .. sensors picking up finger movements/gestures as input. Haptic actuators giving silent notifications. Pen/Stylus: currently underused as could also pick up gestures and have a microphone. Table top Node: palm sized unit. 360 degree vision and audio. Scout/Mini Drone: hovers above you for all round awareness, or can be sent ahead to scout an area, or find you children etc. All integrating with your smart phone, which may become more of a portable battery bank for charging other devices. Here's a blog post I have written that goes into more detail, including the privacy and legal issue etc (no ads/sign up etc) ... The AI Wearable Ecosystem What other devices might be developed? Should these devices be banned from recording other people?

44m ago

---

**[I made a self healing PRD system for Claude code](https://www.reddit.com/r/artificial/comments/1sokj0w/i_made_a_self_healing_prd_system_for_claude_code/)**

I went out to create something that would would build prds for me for projects I'm working on. The core idea it is that it asks for all of the information that's needed for a PRD and it could also review the existing code to answer these questions. Then it breaks up the parts of the plan into separate files and only starts the next part after the first part is complete. Added to that is that it's reaching out to codex every end of part and does an independent review of the code. What I found that was really cool is that when I did that with my existing project to enhance it, the system continued to find more issues through the feedback loop with codex and opened new prds for those issues. So essentially it's running through my code finding issues as it's working on extending it

7h ago

---

**[What AI image generator works the best?](https://www.reddit.com/r/artificial/comments/1so4m79/what_ai_image_generator_works_the_best/)**

There seems to be about 1000 different options. I'm just looking for one that takes a prompt and spits out something usable. I'm good with paying for it if I need to but it needs to be able.to handle a lot of work.

17h ago

---

**[Update on my February posts about replacing RAG retrieval with NL querying — some things I've learned from actually building it](https://www.reddit.com/r/artificial/comments/1soibgb/update_on_my_february_posts_about_replacing_rag/)**

A couple of months ago I posted here (r/LLMDevs, r/artificial) proposing that an LLM could save its context window into a citation-grounded document store and query it in plain language, replacing embedding similarity as the retrieval mechanism for reasoning recovery. Karpathy's LLM Knowledge Bases post and a recent TDS context engineering piece have since touched on similar territory, so it felt like a good time to resurface with what I've actually found building it. The hybrid question got answered in practice Several commenters in the original threads predicted you'd inevitably end up hybrid — cheap vector filter first, LLM reasoning over the shortlist. That's roughly right, but the failure mode that drove it was different from what I expected. Pure semantic search didn't degrade because of scale per se; it started missing retrievals because the query and the target content used different vocabulary for the same concept. The fix was an index-first strategy — a lightweight topic-tagged index that narrows candidates before the NL query runs. So the hybrid layer is structural metadata, not a vector pre-filter. The LLM resists using its own memory This one surprised me. Claude has a persistent tendency to prefer internal reasoning over querying the memory store, even when a query would return more accurate results. Left unchecked, it reconstructs rather than retrieves — which is exactly the failure mode the system was designed to prevent. Fixing it required encoding the query requirement in the system prompt, a startup gate checklist, and explicit framing of what it costs to skip retrieval. It's behavioral, not architectural, but it's a real problem that neither article addresses. The memory layer should decouple from the interface model One thing I haven't tested but follows logically from the architecture: if the persistent state lives in the document store rather than in the model, the interface LLM becomes interchangeable. You should be able to swap Claude for ChatGPT or Gemini with minimal fidelity loss, and potentially run multiple models concurrently against the same memory as a coordination layer. There's also an interesting quality asymmetry that wouldn't exist in vector RAG: because retrieval here uses the interface model's reasoning rather than a separate embedding step, a more capable model should directly improve retrieval quality — not just generation quality. I haven't verified either of these in practice, but the architecture seems to imply them. Curious whether anyone has tested something similar. Memory hygiene is a real maintenance problem Karpathy's post talks about "linting" the wiki for inconsistencies. I ran into a version of this from a different angle: an append-only notes system accumulates stale entries with no way to distinguish resolved from active items. You end up needing something like a note lifecycle (e.g., resolve, revise, retract, etc.) with versioned identifiers so the system can tell what's current. The maintenance overhead of keeping memory coherent is underappreciated in both the Karpathy and TDS pieces. Still in the research and build phase. For anyone curious about the ad hoc system I've been using to test this while working through the supporting literature, the repo is here: https://github.com/pjmattingly/Claude-persistent-memory — pre-alpha quality, but it's the working substrate behind the observations above. Happy to go deeper on any of this.

8h ago

---

**[Claude Design, a new Anthropic Labs product, lets you collaborate with Claude to create polished visual work like designs, prototypes, slides, one-pagers, and more](https://www.reddit.com/r/artificial/comments/1so44z2/claude_design_a_new_anthropic_labs_product_lets/)**

Claude Design is powered by Claude Opus 4.7 and is available in research preview for Claude Pro, Max, Team, and Enterprise subscribers.

🔗 [anthropic.com](https://www.anthropic.com/news/claude-design-anthropic-labs) • 17h ago

---

**[DeepSeek Targets $10B Valuation in Funding Push Amid Global AI Race](https://www.reddit.com/r/artificial/comments/1so7tep/deepseek_targets_10b_valuation_in_funding_push/)**

Chinese AI startup DeepSeek is in talks to raise fresh capital at a $10 billion valuation, signaling a major shift for a company that has largely avoided external funding despite rapidly rising global influence in artificial intelligence.

🔗 [Financership](https://www.financership.com/deepseek-10b-valuation-funding-ai-race/) • 15h ago

---

---

## Google News: "ai"

**[Hundreds of Fake Pro-Trump Avatars Emerge on Social Media](https://www.nytimes.com/2026/04/17/business/media/artificial-intelligence-trump-social-media.html)**

The New York Times • 4h ago

---

**[AI chipmaker Cerebras files to go public after scrapping IPO plans last year](https://www.cnbc.com/2026/04/17/cerebras-new-ipo-ai-chips.html)**

Cerebras said that it can expand its business with OpenAI over the coming years and that it gave OpenAI a warrant to purchase stock.

CNBC • 15h ago

---

**[AI startups are moving into smaller neighborhoods and shifting San Francisco's economic center](https://www.businessinsider.com/ai-startup-moving-into-smaller-neighborhoods-changing-office-culture-sf-2026-3)**

AI startups and their collaborative and fast-moving culture are leading them to choose office spaces away from downtown SF in smaller neighborhoods.

Business Insider • 50m ago

---

**[Volvo Built A Software Defined Vehicle AI Future For EX60 Era](https://www.forbes.com/sites/jamesmorris/2026/04/18/volvo-builds-software-defined-vehicle-ai-future-for-ex60-era/)**

Forbes • 31m ago

---

**[CEO of blacklisted Anthropic and White House hold ‘productive’ discussions on AI](https://www.cnn.com/2026/04/17/business/anthropic-white-house-meeting-dario-amodei)**

Anthropic CEO Dario Amodei visited the White House on Friday for a high-stakes meeting with the president’s top adviser, while his AI company battles the Trump administration in court for blacklisting its Claude AI model.

CNN • 20h ago

---

**[Finance ministers and top bankers raise serious concerns about Mythos AI model](https://www.bbc.com/news/articles/c2ev24yx4rmo)**

Experts say Mythos potentially has an unprecedented ability to identify and exploit cybersecurity weaknesses.

BBC • 22h ago

---

**[Perspective: AI demand is inflated, and only Anthropic is being realistic](https://www.cnbc.com/2026/04/17/ai-tokens-anthropic-openai-nvidia.html)**

The main usage metric for artificial intelligence, called tokens, looks explosive on paper, but it may be significantly overstated.

CNBC • 13h ago

---

**[The attack on Sam Altman exposed a dark underbelly of the anti-AI movement](https://www.cnn.com/2026/04/17/tech/anti-ai-attack-sam-altman)**

Mainstream artificial intelligence safety groups moved quickly to distance themselves after a 20-year-old allegedly attacked the home of OpenAI CEO Sam Altman last week in what law enforcement officers said appeared to be part of a plot to harm AI executives. But people in some corners of the internet cheered the attack.

CNN • 1d ago

---

**[Build a More Secure, Always-On Local AI Agent with OpenClaw and NVIDIA NemoClaw](https://developer.nvidia.com/blog/build-a-secure-always-on-local-ai-agent-with-nvidia-nemoclaw-and-openclaw/)**

Agents are evolving from question-and-answer systems into long-running autonomous assistants that read files, call APIs, and drive multi-step workflows. However, deploying an agent to execute code and…

NVIDIA Developer • 13h ago

---

**[FAA quietly developing AI-enabled predictive air traffic management system](https://theaircurrent.com/air-traffic-control/faa-smart-ai-predictive-air-traffic-management-system-palantir-thales/)**

Palantir, Thales and ASI competing on secretive initiative that could redefine how the U.S. ATC system operates

The Air Current • 16h ago

---

---

## HackerNews: "ai"

**[Cloudflare's AI Platform: an inference layer designed for agents](https://news.ycombinator.com/item?id=47792538)**

We're building AI Gateway into a unified inference layer for AI, letting developers call models from 14+ providers. New features include Workers AI binding integration and an expanded catalog with multimodal models.

⬆️ 306 • 💬 94 • 1d ago • [The Cloudflare Blog](https://blog.cloudflare.com/ai-platform/)

---

**[Elevated errors on Claude.ai, API, Claude Code](https://news.ycombinator.com/item?id=47779730)**

Check if Claude AI is down right now. Real-time status monitoring, uptime history, latency metrics, and incident tracking for claude.ai, Claude API, and Claude Code. Community-powered outage reports and alerts.

⬆️ 243 • 💬 222 • 2d ago • [Claude Status](https://claudestatus.com/)

---

**[AI cybersecurity is not proof of work](https://news.ycombinator.com/item?id=47791236)**

⬆️ 236 • 💬 88 • 1d ago • [antirez.com](https://antirez.com/news/163)

---

**[AI-assisted cognition endangers human development?](https://news.ycombinator.com/item?id=47783024)**

Does AI-assisted cognition threaten human development? Explore the risks of AI-assisted thinking and learn strategies to use AI tools without freezing your critical thinking.

⬆️ 230 • 💬 187 • 2d ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/ai-assisted-cognition-endangers-human-development/)

---

**[Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine](https://news.ycombinator.com/item?id=47800033)**

Hardware hacker’s flying probe automation stack for agent-driven   target discovery, microscope mapping, safety-monitored CNC motion, probe review, and   controlled pin probing. - GainSec/AutoProber

⬆️ 222 • 💬 46 • 1d ago • [GitHub](https://github.com/gainsec/autoprober)

---

**[We gave an AI a 3 year retail lease and asked it to make a profit](https://news.ycombinator.com/item?id=47794391)**

We signed a 3 year lease and gave it to an AI

⬆️ 197 • 💬 281 • 1d ago • [andonlabs.com](https://andonlabs.com/blog/andon-market-launch)

---

**[Are the costs of AI agents also rising exponentially? (2025)](https://news.ycombinator.com/item?id=47778922)**

There is an extremely important question about the near-future of AI that almost no-one is asking.   We’ve all seen the graphs from METR showing that the length of tasks AI agents can perform has been growing exponentially over the last 7 years. While GPT-2 could only do software engineering tasks t

⬆️ 196 • 💬 50 • 2d ago • [Toby Ord](https://www.tobyord.com/writing/hourly-costs-for-ai-agents)

---

**[US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]](https://news.ycombinator.com/item?id=47778920)**

⬆️ 190 • 💬 137 • 2d ago • [fingfx.thomsonreuters.com](https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf)

---

**[The beginning of scarcity in AI](https://news.ycombinator.com/item?id=47799322)**

GPU rental prices surged 48% in 60 days. The AI compute shortage will force startups to compete not on speed of iteration, but on access to infrastructure.

⬆️ 182 • 💬 212 • 1d ago • [Tomasz Tunguz](https://tomtunguz.com/ai-compute-crisis-2026/)

---

**[AI ruling prompts warnings from US lawyers: Your chats could be used against you](https://news.ycombinator.com/item?id=47778308)**

⬆️ 154 • 💬 100 • 2d ago • [reuters.com](https://www.reuters.com/legal/government/ai-ruling-prompts-warnings-us-lawyers-your-chats-could-be-used-against-you-2026-04-15/)

---

---

## YouTube Videos: "ai"

**[The World&#39;s First AI TED Talk](https://www.youtube.com/watch?v=N1X7vMp9DZ4)**

ChatGPT was recently asked what it would say to humans if it could give a TED Talk. It gave a surprisingly thoughtful answer that ...

📺 TED

👁️ 27K • 👍 1K • 💬 508 • ⏱️ 3:28 • 11h ago

---

**[99% of People Have No Idea What’s About to Happen With AI](https://www.youtube.com/watch?v=8yt5yzwJQko)**

Get your FREE AI Prompt Cheatsheet here: https://go.danmartell.com/4tVJ4fz Are you building an AI software company?

📺 Dan Martell

👁️ 177K • 👍 8K • 💬 1K • ⏱️ 14:03 • 1d ago

---

**[A.I. Iranian propaganda videos making fun of Trump, U.S. go viral](https://www.youtube.com/watch?v=LTJYQ0knUsE)**

A series of animated Iranian propaganda videos made in the style of "The LEGO Movie" has gone viral on social media, making ...

📺 MS NOW

👁️ 76K • 👍 2K • 💬 871 • ⏱️ 6:46 • 13h ago

---

**[AI Safety Expert: No One Is Ready for What&#39;s Coming in 2 Years | Roman Yampolskiy](https://www.youtube.com/watch?v=00RHph_eok4)**

This episode is brought to you by Higgsfield — the AI video platform with Cinema Studio 2.5, built for creators who want cinematic ...

📺 Silicon Valley Girl

👁️ 24K • 👍 583 • 💬 111 • ⏱️ 45:43 • 20h ago

---

**[These HILARIOUS AI Parodies Keep PISSING OFF TRUMP!](https://www.youtube.com/watch?v=0aB9ycZDBIw)**

Really American host Steve Harness breaks down more HILARIOUS AI Trump parodies coming out of Iran...and these may be the ...

📺 Really American

👁️ 991K • 👍 47K • 💬 3K • ⏱️ 12:33 • 1d ago

---

**[The AI Expert Who Thinks We&#39;ve Already Lost — Dr Roman Yampolskiy](https://www.youtube.com/watch?v=3I60uZEqXr0)**

Triggernometry is proudly independent. Thanks to the sponsors below for making that possible: - Trade on what happens next ...

📺 Triggernometry

👁️ 212K • 👍 6K • 💬 2K • ⏱️ 1:11:10 • 2d ago

---

**[China Just Built an Autonomous AI Robot Army: Killer Robots With Guns and Rockets](https://www.youtube.com/watch?v=_Vw_6QrqS8c)**

China just revealed an autonomous robot war pack built from dog bots, drones, laser weapons, and unmanned boats, Europe is ...

📺 AI Revolution

👁️ 50K • 👍 1K • 💬 108 • ⏱️ 16:14 • 1d ago

---

**[LIVE: Sanders, Labor Leaders Call on Congress to Protect Workers from AI](https://www.youtube.com/watch?v=DdJfeSMB99g)**

The same oligarchs who shipped jobs overseas now want to replace tens of millions of American workers with AI. Our message to ...

📺 Senator Bernie Sanders

👁️ 13K • 👍 1K • 💬 364 • ⏱️ 45:01 • 1d ago

---

**[Donald Trump Posted This AI Image of Jesus…](https://www.youtube.com/watch?v=-Z4SHvUa5gw)**

discord.gg/nickjones.

📺 Nick Jones

👁️ 16K • 👍 782 • 💬 491 • ⏱️ 8:37 • 1d ago

---

**[AI News: Huge Updates From Anthropic, OpenAI and Google](https://www.youtube.com/watch?v=bIrzOQtnp8w)**

Here's the AI News you probably missed this week. Build AI apps that actually scale. Learn more about Crusoe Managed ...

📺 Matt Wolfe

👁️ 51K • 👍 2K • 💬 120 • ⏱️ 36:44 • 18h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 258,064 • ❤️ 932 • 23h ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 82,000 • ❤️ 769 • 3d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,454 • ❤️ 854 • 3d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 3,116 • ❤️ 430 • 1d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 103,847 • ❤️ 1,388 • 2d ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 442,900 • ❤️ 388 • 1d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 66,552 • ❤️ 384 • 5d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 3,778,070 • ❤️ 2,130 • 7d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 35,870 • ❤️ 1,105 • 2d ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 4,119 • ❤️ 294 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 23 • 💬 1 • ⭐ 19,047 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 4 • 💬 2 • ⭐ 1,073 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)**

*Team HY-World, Chenjie Cao, Xuhui Zuo et al. (45 authors)*

HY-World 2.0 is a multi-modal world model framework that generates high-fidelity 3D Gaussian Splatting scenes from diverse inputs using specialized modules for panorama generation, trajectory planning, world expansion, and composition, along with an enhanced rendering platform for interactive 3D exploration.

▲ 74 • 💬 4 • ⭐ 1,022 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14268) • [💻 code](https://github.com/Tencent-Hunyuan/HY-World-2.0) • [🔗 project](https://3d-models.hunyuan.tencent.com/world/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 47 • 💬 2 • ⭐ 51,246 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 18,026 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,070 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 51 • 💬 4 • ⭐ 1,802 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 52 • 💬 1 • ⭐ 77,128 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 159 • 💬 2 • ⭐ 60,340 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,648 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 47.6k • 🔱 6.2k • 2h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 37.1k • 🔱 1.8k • 2d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 35.7k • 🔱 7.2k • 14h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 29.3k • 🔱 3.2k • 13h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.2k • 🔱 521 • 1h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 5d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 5.1k • 🔱 862 • 4d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.9k • 🔱 1.1k • 23d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.7k • 🔱 181 • 1d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.6k • 🔱 454 • 9d ago

---

---

*Generated by PeekDeck - A glance is all you need*
