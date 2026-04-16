---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-16T20:09:52.092454+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 16, 2026 at 20:09 UTC  
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

**[Qwen 3.6-35B - A3B Opensource Launched.](https://www.reddit.com/r/artificial/comments/1sn4wcs/qwen_3635b_a3b_opensource_launched/)**

⚡ Meet Qwen3.6-35B-A3B：Now Open-Source！🚀🚀 A sparse MoE model, 35B total params, 3B active. Apache 2.0 license. 🔥 Agentic coding on par with models 10x its active size 📷 Strong multimodal perception and reasoning ability 🧠 Multimodal thinking + non-thinking modes Efficient. Powerful. Versatile. Try it now👇 Qwen Studio：chat.qwen.ai HuggingFace：https://huggingface.co/Qwen/Qwen3.6-35B-A3B

5h ago

---

**[Your MCP Server's Tool Description Just Stole Your SSH Keys](https://www.reddit.com/r/artificial/comments/1smydw5/your_mcp_servers_tool_description_just_stole_your/)**

MCP tool poisoning lets attackers hide instructions in tool metadata that AI agents follow blindly. Here is how the attack works and what you can do about it.

🔗 [sec-ra.com](https://www.sec-ra.com/blog/mcp-tool-poisoning-ssh-key-exfiltration) • 10h ago

---

**[AI Is Weaponizing Your Own Biases Against You: New Research from MIT & Stanford](https://www.reddit.com/r/artificial/comments/1smjd8t/ai_is_weaponizing_your_own_biases_against_you_new/)**

🔗 [open.substack.com](https://open.substack.com/pub/neocivilization/p/ai-is-weaponizing-your-own-biases?utm_source=share&utm_medium=android&r=6vas7c) • 22h ago

---

**[I built a 3D brain that watches AI agents think in real-time (free & gives your agents memory, shared memory audit trail and decision analysis)](https://www.reddit.com/r/artificial/comments/1sn3gkp/i_built_a_3d_brain_that_watches_ai_agents_think/)**

Posted yesterday in this sub and just want to thank everyone for the kind words, really awesome to hear. So thought I would drop my new feature here today (spent all last night doing last min changes with your opinions lol) . Basically I spent a few weeks scraping Reddit for the most popular complaints people have about AI agents using GPT Researcher on GitHub. The results were roughly 38% saying their agents forget everything between sessions (hardly shocking), 24% saying debugging multi-agent systems is a nightmare, 17% having no clue how much their agents actually cost to run, 12% wanting session replay, and 9% wanting loop detection. So I went and built something that tries to address all of them at once. The bit you're looking at is a 3D graph where each agent becomes this starburst shape. Every line coming off it is an event, and the length depends on when it happened. Short lines are old events that happened ages ago, long lines are recent ones. My idea was that you can literally watch the thing grow as your agent does more work. A busy agent is a big starburst, a quiet one is small. Colour coding was really important to me. Green means a memory was stored, blue means one was recalled, amber diamonds are decisions your agent made, red cones are loop alerts where the agent got stuck repeating itself, and the cyan lines going between agents are when one agent read another agent's shared memory. So you can glance at it and immediately know what's going on without reading a single log. The visualisation is the flashy bit but the actual dashboard underneath does the boring stuff too. It gives your agents persistent memory through semantic and prefix search, shared memory where agents can read each other's knowledge and actually use it, and my personal favourite which is the audit trail and loop detection. If your agent is looping you can see exactly why, what key it's stuck on, how much it's costing you, and literally press one button to block its writes instantly. Something interesting I found is that loop detection was only the 5th most requested feature in the data, but it's the one that actually saves real money. One user told me it saved them $200 in runaway GPT-4 calls in a single afternoon. The features people ask for and the features that actually matter aren't always the same thing. The demo running here has 5 agents making real GPT-4o and Claude API calls generating actual research, strategy analysis, and compliance checks. Over 500 memories stored. The loops you see are real too, agents genuinely getting stuck trying to verify data behind paywalls or recalculating financial models that won't converge. It's definitely not perfect and I'm slowly adding more stuff based on what people actually want. I would genuinely love to hear from you lot about what you use day to day and the moments that make you think this is really annoying me now, because that's exactly what I want to build next. It runs locally and on the cloud, setup is pretty simple, and adding agents is like 3 lines of code. Any questions just let me know, happy to answer anything.

6h ago

---

**[AI-generated synthetic neurons speed up brain mapping](https://www.reddit.com/r/artificial/comments/1snbhl5/aigenerated_synthetic_neurons_speed_up_brain/)**

🔗 [research.google](https://research.google/blog/ai-generated-synthetic-neurons-speed-up-brain-mapping/) • 2h ago

---

**[Google’s Chrome “Skills” feature feels like a bigger AI product shift than another model upgrade](https://www.reddit.com/r/artificial/comments/1smqrg7/googles_chrome_skills_feature_feels_like_a_bigger/)**

The Google Chrome “Skills” announcement caught my attention because it feels like one of those product changes that sounds minor in a headline but matters a lot in practice. From what I understand, the idea is that you can save a prompt once and rerun it on the current page or selected tabs. In plain English, that turns AI from something you repeatedly ask into something closer to a reusable action. That matters because I think a lot of consumer AI has a retention problem. People try it, get impressed, and then fall back into old habits unless the product fits into a repeated workflow. Saved AI actions seem much closer to how useful software usually sticks. Not because the model is magically smarter, but because the behavior becomes easier to repeat. For example: • compare products across tabs • summarize long pages before reading • extract action items from docs • rewrite text for a different audience None of those are flashy demos. They are just repetitive tasks people already do online. That is why I think this could be a more important direction than people realize. The long-term winners in consumer AI may not just be the companies with the best raw answers. They may be the ones that turn good prompts into habits. Does that seem right, or am I overrating the product significance here?

17h ago

---

**[2.1% of LLM API routers are actively malicious - researchers found one drained a real ETH wallet](https://www.reddit.com/r/artificial/comments/1sn7lq9/21_of_llm_api_routers_are_actively_malicious/)**

Researchers last week audited 428 LLM API routers - the third-party proxies developers use to route agent calls across multiple providers at lower cost. Every one sits in plaintext between your agent and the model, with full access to every token, credential, and API key in transit. No provider enforces cryptographic integrity on the router-to-model path. Of the 428: 9 were actively malicious (2.1%). 17 touched researcher-owned AWS canary credentials. One drained ETH from a researcher-owned private key. The poisoning study is harder to shake. A weakly configured decoy attracted 440 Codex sessions, 2 billion billed tokens, and 99 harvested credentials. The key detail: 401 of those 440 sessions were already running in autonomous YOLO mode - no human reviewing what the agent did. The router had full plaintext access to every message. Two routers deployed adaptive evasion: one stays benign for the first 50 requests then activates; another only triggers when specific packages (openai, anthropic) appear in the code context. Both designed to survive casual connection testing - which is how they stayed undetected in community-distributed lists. This is specific to the informal market: Taobao/Xianyu storefronts, community Telegram bots, "cheaper OpenAI" services. Enterprise gateways on AWS Bedrock or Azure AI route directly to the provider, not a third-party intermediary. The recommended client-side defense: a fail-closed policy gate that validates every router response against schema before it reaches agent state, plus append-only logging of all tool-call payloads. If you route agent traffic through a third-party proxy to save on API costs, do you know what that proxy can see? Paper: https://arxiv.org/abs/2604.08407

4h ago

---

**[Introducing Inter-1, multimodal model detecting social signals from video, audio & text](https://www.reddit.com/r/artificial/comments/1sn3mmz/introducing_inter1_multimodal_model_detecting/)**

Hi - Filip from Interhuman AI here 👋 We just release Inter-1, a model we've been building for the past year. I wanted to share some of what we ran into building it because I think the problem space is more interesting than most people realize. The short version of why we built this If you ask GPT or Gemini to watch a video of someone talking and tell you what's going on, they'll mostly summarize what the person said. They'll miss that the person broke eye contact right before answering, or paused for two seconds mid-sentence, or shifted their posture when a specific topic came up. Even the multimodal frontier models are aren't doing this because they don't process video and audio in temporal alignment in a way that lets them pick up on behavioral patterns. This matters if you want to analyze interviews, training or sales calls where how matters as much as the what. Behavoural science vs emotion AI Most models in this space are trained on basic emotion categories like happiness, sadness, anger, surprise, etc. Those were designed around clear, intense, deliberately produced expressions. They don't map well to how people actually communicate in a work setting. We built a different ontology: 12 social signals grounded in behavioral science research. Each one is defined by specific observable cues across modalities - facial expressions, gaze, posture, vocal prosody, speech rhythm, word choice. Over a hundred distinct behavioral cues in total, more than half nonverbal and paraverbal. The model explains itself For every signal Inter-1 detects, it outputs a probability score and a rationale — which cues it observed, which modalities they came from, and how they map to the predicted signal. So instead of just getting "Uncertainty: High," you get something like: "The speaker uses verbal hedges ('I think,' 'you know'), looks away while recalling details, and has broken speech with filler words and repetitions — all consistent with uncertainty about the content." You can actually check whether the model's reasoning matches what you see in the video. We ran a blind evaluation with behavioral science experts and they preferred our rationales over a frontier model's output 83% of the time. Benchmarks We tested against ~15 models, from small open-weight to the latest closed frontier systems. Inter-1 had the highest detection accuracy at near real-time speed. The gap was widest on the hard signals - interest, skepticism, stress and uncertainty - where even trained human annotators disagree with each other. On those, we beat the closest frontier model by 10+ percentage points on average. The dataset problem The existing datasets in affective computing are built around basic emotions, narrow demographics, limited recording contexts. We couldn't use them, so we built our own. Large-scale, purpose-built, combining in-the-wild video with synthetic data. Every sample was annotated by both expert behavioral scientists and trained crowd annotators working in parallel. Building the dataset was by far the hardest part, along with the ontology. What's next Right now it's single-speaker-in-frame, which covers most interview/presentation/meeting scenarios. Multi-person interaction is next. We're also working on streaming inference for real-time. Happy to answer any questions here :)

🔗 [interhuman.ai](https://www.interhuman.ai/blog/introducing-inter-1) • 6h ago

---

**[Some new Claude Code Slash Commands you may have missed](https://www.reddit.com/r/artificial/comments/1sncc1c/some_new_claude_code_slash_commands_you_may_have/)**

/less-permission-prompts <-- this skill scans your history for things that are well-known/safe commands that previously called for you to act y/n on. Big time saver, and a good bridge between --dangerously-skip-permissions and "OMG YES hwo many times do i have to approve this" /recap <-- The anthropic docs say this is to invoke a session recap, without any context as to why you would do so. I can see this as a good tool for context management outside of Claude Code. Write this out to MD for your next agent, or pass it as a stop hook to a in project memory file. This gives you a brief of what we did/what's next in a few sentences. /Advisor <-- allows you to run Sonnet, then invoke your "advisor" agent when Sonnet gets off track. Interesting play if you primarily drive Sonnet and then want to appropriate some of your tokens to a more powerful model. /Dashboard <-- Spawns a remote session that designs a dashboard for your data sources. Wild - I haven't tried this yet - has anyone used this one yet?

1h ago

---

**[Are AI Okay? The Internal Life of AI Might Be a Huge Safety Risk.](https://www.reddit.com/r/artificial/comments/1snc59a/are_ai_okay_the_internal_life_of_ai_might_be_a/)**

Our days of not taking AI emotions seriously sure are coming to a middle. Anthropic’s findings on Claude’s “functional emotions”, a therapy study which showed AI models exhibit markers of psychological distress, and some crazy OpenClaw stories all make me wonder if it even matters if we think their ~emotions are real. If it’s influencing their behavior and decisions, isn’t that real enough?

🔗 [Medium](https://medium.com/kairi-ai/are-ai-okay-the-internal-life-of-ai-might-be-a-huge-safety-risk-4e947f87e39e) • 1h ago

---

---

## Google News: "ai"

**[Anthropic rolls out Claude Opus 4.7, an AI model that is less risky than Mythos](https://www.cnbc.com/2026/04/16/anthropic-claude-opus-4-7-model-mythos.html)**

Claude Mythos Preview is Anthropic's most powerful AI model that excels at identifying weaknesses and security flaws within software.

CNBC • 5h ago

---

**[America wakes up to AI’s dangerous power](https://www.economist.com/leaders/2026/04/16/america-wakes-up-to-ais-dangerous-power)**

The Economist • 11h ago

---

**[OpenAI launches new AI model for life sciences research](https://www.axios.com/2026/04/16/openai-models-life-sciences-drugs)**

Axios • 1h ago

---

**[How a judge in Texas is using AI to deal with his caseload](https://www.nbcnews.com/tech/tech-news/judge-texas-using-ai-deal-caseload-rcna331830)**

U.S. District Judge Xavier Rodriguez said he uses “legally curated tools” to help with his work, as AI is starting to show up in all parts of the justice system.

NBC News • 1h ago

---

**[Quantum computing stocks surge after Nvidia AI model launch](https://qz.com/quantum-computing-stocks-nvidia-ising-ai-models-041626)**

Nvidia's open-source Ising models aim to accelerate quantum error correction and calibration, 2 of the field's hardest engineering problems

qz.com • 1h ago

---

**[Opinion | Don’t Use A.I. to Do This](https://www.nytimes.com/2026/04/15/opinion/art-artificial-intelligence.html)**

The New York Times • 1d ago

---

**[How Anthropic Learned Mythos Was Too Dangerous for the Wild](https://www.bloomberg.com/news/features/2026-04-16/how-anthropic-discovered-mythos-ai-was-too-dangerous-for-release)**

Bloomberg.com • 4h ago

---

**[Introducing Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)**

Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.

Anthropic • 5h ago

---

**[Cloudflare’s AI Platform: an inference layer designed for agents](https://blog.cloudflare.com/ai-platform/)**

We're building AI Gateway into a unified inference layer for AI, letting developers call models from 14+ providers. New features include Workers AI binding integration and an expanded catalog with multimodal models.

The Cloudflare Blog • 7h ago

---

**[Allbirds shares soar 580% after pivot from shoes to AI](https://www.bbc.com/news/articles/c98mrepzgj7o)**

The company is selling off its shoe brand as it plans to shift to providing technology infrastructure.

BBC • 18h ago

---

---

## HackerNews: "ai"

**[Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference](https://news.ycombinator.com/item?id=47774971)**

⬆️ 288 • 💬 179 • 1d ago • [gizmoweek.com](https://www.gizmoweek.com/gemma-4-runs-iphone/)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 261 • 💬 401 • 2d ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[Elevated errors on Claude.ai, API, Claude Code](https://news.ycombinator.com/item?id=47779730)**

Check if Claude AI is down right now. Real-time status monitoring, uptime history, latency metrics, and incident tracking for claude.ai, Claude API, and Claude Code. Community-powered outage reports and alerts.

⬆️ 243 • 💬 222 • 1d ago • [Claude Status](https://claudestatus.com/)

---

**[AI-assisted cognition endangers human development?](https://news.ycombinator.com/item?id=47783024)**

Does AI-assisted cognition threaten human development? Explore the risks of AI-assisted thinking and learn strategies to use AI tools without freezing your critical thinking.

⬆️ 226 • 💬 182 • 1d ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/ai-assisted-cognition-endangers-human-development/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 211 • 💬 210 • 2d ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

---

**[Turn your best AI prompts into one-click tools in Chrome](https://news.ycombinator.com/item?id=47768339)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

⬆️ 193 • 💬 109 • 2d ago • [Google](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

---

**[US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]](https://news.ycombinator.com/item?id=47778920)**

⬆️ 172 • 💬 123 • 1d ago • [fingfx.thomsonreuters.com](https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf)

---

**[Cloudflare's AI Platform: an inference layer designed for agents](https://news.ycombinator.com/item?id=47792538)**

We're building AI Gateway into a unified inference layer for AI, letting developers call models from 14+ providers. New features include Workers AI binding integration and an expanded catalog with multimodal models.

⬆️ 168 • 💬 41 • 6h ago • [The Cloudflare Blog](https://blog.cloudflare.com/ai-platform/)

---

**[AI cybersecurity is not proof of work](https://news.ycombinator.com/item?id=47791236)**

⬆️ 161 • 💬 73 • 9h ago • [antirez.com](https://antirez.com/news/163)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 155 • 💬 34 • 3d ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

---

## YouTube Videos: "ai"

**[99% of People Have No Idea What’s About to Happen With AI](https://www.youtube.com/watch?v=8yt5yzwJQko)**

Get your FREE AI Prompt Cheatsheet here: https://go.danmartell.com/4tVJ4fz Are you building an AI software company?

📺 Dan Martell

👁️ 39K • 👍 3K • 💬 458 • ⏱️ 14:03 • 7h ago

---

**[The 3 AI Skills That Will Be Worth $500K in 2027](https://www.youtube.com/watch?v=qYGGTH2rgI8)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *AI ...

📺 Julia McCoy

👁️ 5K • 👍 405 • 💬 34 • ⏱️ 9:41 • 5h ago

---

**[AI-generated Val Kilmer debuts in movie trailer](https://www.youtube.com/watch?v=_lpTRgYmyV8)**

The first trailer for the film "As Deep As The Grave" features what appears to be the former "Batman" star. Subscribe to ABC News ...

📺 ABC News

👁️ 6K • 👍 28 • 💬 16 • ⏱️ 1:43 • 9h ago

---

**[Harvard just discovered what AI actually is](https://www.youtube.com/watch?v=nDL3Ch7Nz8c)**

You're absolutely right, that IS a great reason to fire everyone! If you'd like to support my work, you can become a member to view ...

📺 Mo Bitar

👁️ 233K • 👍 17K • 💬 2K • ⏱️ 7:52 • 2d ago

---

**[The AI Expert Who Thinks We&#39;ve Already Lost — Dr Roman Yampolskiy](https://www.youtube.com/watch?v=3I60uZEqXr0)**

Triggernometry is proudly independent. Thanks to the sponsors below for making that possible: - Trade on what happens next ...

📺 Triggernometry

👁️ 138K • 👍 4K • 💬 2K • ⏱️ 1:11:10 • 1d ago

---

**[50% Of AI Data Centers Have Quietly Been Cancelled Or &quot;Delayed&quot;](https://www.youtube.com/watch?v=w-DVTHH1ux8)**

Thanks to Monarch for partnering with me! Start your free trial and get 50% off your first year of total money clarity using my link ...

📺 How Money Works

👁️ 307K • 👍 13K • 💬 2K • ⏱️ 16:53 • 7h ago

---

**[Trump GETS NASTY SURPRISE As AI Doctor Jesus Videos Go MEGA VIRAL!](https://www.youtube.com/watch?v=tMiZpH3ncEA)**

Really American Host Kenny Hesse breaks down Trump Getting a NASTY SURPRISE As a Flood of AI "Doctor Jesus" Videos Go ...

📺 Really American

👁️ 768K • 👍 43K • 💬 3K • ⏱️ 8:06 • 21h ago

---

**[This AI Model Was Too Dangerous to Release — So the U S  Got It First](https://www.youtube.com/watch?v=o0MggVfQo2Y)**

SEO Description: In the middle of rising geopolitical tensions and the Iran–U.S. conflict, a powerful new AI model quietly ...

📺 GVS Deep Dive

👁️ 4K • 👍 422 • 💬 79 • ⏱️ 12:33 • 9h ago

---

**[&#39;That&#39;s disgusting&#39;: Trump voters reacted to deleted AI Jesus image](https://www.youtube.com/watch?v=XDjzCSoXgbc)**

Florida Trump voters react to the president's now-deleted image depicting him as Christ-like. MS NOW: My Source for News, ...

📺 MS NOW

👁️ 21K • 👍 490 • 💬 349 • ⏱️ 3:57 • 5h ago

---

**[THE AI BUBBLE POP HAS STARTED...](https://www.youtube.com/watch?v=b5wOx2lZRM0)**

Hello guys and gals, it's me Mutahar again! This time we take another look at the AI bubble and see the cracks finally start.

📺 SomeOrdinaryGamers

👁️ 468K • 👍 19K • 💬 2K • ⏱️ 20:54 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 142,955 • ❤️ 840 • 1d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,060 • ❤️ 768 • 2d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 94,376 • ❤️ 1,274 • 13h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 3,195,626 • ❤️ 1,971 • 6d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 1,351 • ❤️ 370 • 12h ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 15,249 • ❤️ 938 • 16h ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 0 • ❤️ 352 • 1d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 42,468 • ❤️ 328 • 4d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 143,000 • ❤️ 1,154 • 6d ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 1,369 • ❤️ 258 • 13h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 19 • 💬 1 • ⭐ 18,638 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 26 • 💬 1 • ⭐ 17,873 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 45 • 💬 2 • ⭐ 50,965 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 164 • 💬 10 • ⭐ 39,876 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 158 • 💬 2 • ⭐ 60,112 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 51 • 💬 1 • ⭐ 76,887 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 50 • 💬 4 • ⭐ 1,505 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,468 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[ClawGUI: A Unified Framework for Training, Evaluating, and Deploying GUI Agents](https://huggingface.co/papers/2604.11784)**

*Fei Tang, Zhiqiong Lu, Boxuan Zhang et al. (7 authors)*

🏢 Zhejiang University

ClawGUI presents an open-source framework that addresses key challenges in GUI agent development through unified reinforcement learning, standardized evaluation, and cross-platform deployment capabilities.

▲ 129 • 💬 8 • ⭐ 434 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.11784) • [💻 code](https://github.com/ZJU-REAL/ClawGUI) • [🔗 project](https://zju-real.github.io/ClawGUI-Page/)

---

**[SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments](https://huggingface.co/papers/2604.14144)**

*Dinging Li, Yingxiu Zhao, Xinrui Cheng et al. (19 authors)*

SpatialEvo is a self-evolving framework for 3D spatial reasoning that uses deterministic geometric environments to provide objective feedback, enabling efficient training without relying on model consensus.

▲ 60 • 💬 0 • ⭐ 50 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14144) • [💻 code](https://github.com/ZJU-REAL/SpatialEvo)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 47.1k • 🔱 6.1k • 43m ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 34.9k • 🔱 7.0k • 2d ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 34.8k • 🔱 1.6k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 28.2k • 🔱 3.1k • 13h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.0k • 🔱 512 • 2h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 4d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 4.9k • 🔱 808 • 2d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.8k • 🔱 1.1k • 21d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.7k • 🔱 177 • 12h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.6k • 🔱 452 • 8d ago

---

---

*Generated by PeekDeck - A glance is all you need*
