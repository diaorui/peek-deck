---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-26T10:07:38.911127+00:00'
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

**Last Updated:** March 26, 2026 at 10:07 UTC  
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

**[Pentagon formalizes Palantir's Maven AI as a core military system with multi-year funding — platform's investment grows to $13 billion from $480 million in 2024. The Pentagon is spending $13.4 billion on AI this year alone.](https://www.reddit.com/r/artificial/comments/1s3t064/pentagon_formalizes_palantirs_maven_ai_as_a_core/)**

The Pentagon is spending $13.4 billion on AI this year alone.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/pentagon-formalizes-palantirs-maven-ai-as-a-core-military-system-with-multi-year-funding-platforms-investment-grows-to-usd13-billion-from-usd480-million-in-2024) • 9h ago

---

**[Meta just acqui-hired its 4th AI startup in 4 months. Dreamer, Manus, Moltbook, and Scale AI's founder. Is anyone else watching this pattern?](https://www.reddit.com/r/artificial/comments/1s3xr4l/meta_just_acquihired_its_4th_ai_startup_in_4/)**

Quick rundown of what Meta's done since December: • Dec 2025: Acquired Manus (autonomous web agent) for $2B • Early 2026: Acqui-hired Moltbook team • Scale AI's Alexandr Wang stepped down as CEO to become Meta's first Chief AI Officer • March 23: Dreamer team (agentic AI platform) joins Meta Superintelligence Labs All of these teams are going into one division under Wang. Zuckerberg isn't just building models, he's assembling an entire talent army for agents. The Dreamer one is interesting because they were only in beta for a month before Meta grabbed them. The product let regular people build their own AI agents. Thousands of users already. Feels like Meta is betting everything on agents being the next platform shift, not just chatbots. What do you guys think - is this a smart consolidation play or is Zuck just panic-buying talent because open-source alone isn't enough? Full breakdown here

5h ago

---

**[Scientists find 100+ hidden exoplanets in NASA data using new AI system](https://www.reddit.com/r/artificial/comments/1s3rh9h/scientists_find_100_hidden_exoplanets_in_nasa/)**

"The team trained machine learning models to identify patterns in the data that can tell astronomers the type of event that has been detected, something that AI models excel at. RAVEN is designed to handle the whole exoplanet-detection process in one go — from detecting the signal to vetting it with machine learning and then statistically validating it. That means that it has an additional edge over other contemporary tools that only focus on specific parts of this process ... "RAVEN allows us to analyze enormous datasets consistently and objectively," senior team member and University of Warwick researcher David Armstrong said in the statement. "Because the pipeline is well-tested and carefully validated, this is not just a list of potential planets — it is also reliable enough to use as a sample to map the prevalence of distinct types of planets around sun-like stars." Within the candidate close-in planets, researchers could then determine the types of planets and their populations in detail. This revealed that around 10% of stars like the sun host a close-in planet, validating findings made by TESS's exoplanet-hunting predecessor Kepler. RAVEN was also able to help researchers determine just how rare close-in Neptune-size worlds are, finding that they occur around just 0.08% of sun-like stars. This absence of these worlds close to their parent star is referred to as the "Neptunian desert" by astronomers. "For the first time, we can put a precise number on just how empty this 'desert' is," leader of the Neptunian desert study team, Kaiming Cui of the University of Warwick said in the statement. "These measurements show that TESS can now match, and in some cases surpass, Kepler for studying planetary populations." The RAVEN results demonstrate the power of AI to search through vast swathes of astronomical data to spot subtle effects."

🔗 [Space](https://www.space.com/astronomy/exoplanets/100-new-alien-worlds-scientists-find-hidden-haul-in-data-from-nasa-exoplanet-hunting-spacecraft) • 10h ago

---

**[I open-sourced an always-on direct bridge between your LLM and your Mac. "Hey Q, read my screen and reply to this Slack message" please meet CODEC](https://www.reddit.com/r/artificial/comments/1s432by/i_opensourced_an_alwayson_direct_bridge_between/)**

TL;DR: Meet CODEC—a completely open-source tool that transforms any LLM into a personal computer agent. You can command it via text or voice to look at your screen, type, manage your apps, run commands, and even code its own plugins. Also new: you can now control everything remotely from your phone using a Cloudflare tunnel. It’s 100% local and free—no cloud, no subscriptions, and zero data leaving your hardware. I’ll cut right to the chase because the actual use cases are what matter here. Imagine just saying, "Hey Q, open Chrome and search for Tokyo flights next Monday," and watching your browser do exactly that. (I use "Q" as a shortcut for Qwen, running locally on my Mac Studio 35b a3b MLX). 💬 It reads your screen and types for you: If you say "draft a reply saying I'll look at it tonight," it looks at your screen, reads the active Slack or email, writes a polished response, and pastes it into the chat box. 👁️ It has full vision and voice: You can ask what's on your monitor, and it uses a vision model to describe it. Ask for a Japanese translation, and it speaks it back. 🎵 It controls your system: Tell it to remind you about a PR at 3 PM, and it makes an Apple Reminder. Tell it to play Spotify, skip tracks, or adjust volume, and it handles it natively. 🐍 It writes its own code: If I say "create a skill to check my Proxmox node," it writes a Python plugin, saves it, and runs it instantly without needing a reboot. All of this runs entirely privately and for free, triggered by voice, keyboard, or a wake word. 🌍 But the remote features are next level: Let's say I'm at a restaurant. I can pull up codec.mydomain.com on my phone (secured via Cloudflare Zero Trust) and type "check the backup script." My Mac runs it and sends the results—no SSH or VPN needed. 🛠️ Setting up the phone dashboard is also insanely simple. It's just two Python files: a FastAPI backend and a vanilla HTML front end. There's no React, no npm installs, and no build steps. You just clone the repo, run python3 codec_dashboard.py, point a Cloudflare Tunnel at port 8090, and add Zero Trust email auth. Boom. Your phone is securely talking to your machine through your own domain. 🔒 What I love most is the privacy. You aren't relying on Telegram to relay system commands through their servers. You aren't giving a Discord bot access to your local files, or letting a WhatsApp API scrape your AI conversations. It is completely direct, encrypted, and yours. 🛡️ Of course, giving an AI control of your OS sounds sketchy, which is why the security is baked right in. There's a dangerous command blocker that catches over 20 red-flag patterns (like sudo, rm -rf, or killall) and hits you with a Y/N prompt before anything actually runs. Everything the agent does is timestamped in a local ~/.codec/audit.log. You can even use a "dry-run" mode to safely preview actions without executing them. Oh, and the wake word detection has noise filtering, so a movie playing in the background won't accidentally trigger a random command. ⚡ Zero-latency skills: > Because speed is everything, CODEC has 15 built-in skills that fire instantly without even waking up the LLM. Things like the calculator, weather, system info, web search, timers with voice alerts, Spotify, Apple Notes, and even the self-writing skill creator run completely locally and instantaneously. 🧠 It works with anything: > You're not locked into a specific ecosystem. It works with Ollama, LM Studio, MLX (which absolutely flies on Apple Silicon), OpenAI, Anthropic, the Gemini free tier, or literally any OpenAI-compatible endpoint. For voice, it uses Whisper for speech-to-text, and Kokoro 82M for text-to-speech. Kokoro is ridiculously fast on M-series chips and gives you a rock-solid, consistent voice every single time. 💻 Multi-machine setups are a breeze: > Say you run a heavy model like Qwen 3.5 35B on your Mac Studio. You can use your MacBook Air as a lightweight "thin client" over your LAN. The Air doesn't need any models installed on it—it just beams your voice to the Studio's Whisper, gets the LLM's answer, and plays back the audio from Kokoro. 🐍 Built for builders: > Under the hood, the entire architecture is Python. Two files for the agent, two for the phone dashboard, a Whisper server, a skills folder, and a config file. A setup wizard handles the rest. Honestly, this is it. This is the AI operating system I actually wanted to use. I've spent the last year studying and building with AI full-time, and poured the last 10 intense days into making CODEC a reality. Because it has this much root-level system access, I knew it had to be completely open-source. I want you guys to save it, star it, clone it, tear it apart, and tell me what I missed! git clone https://github.com/AVADSA25/codec cd codec pip3 install pynput sounddevice soundfile numpy requests simple-term-menu brew install sox python3 setup_codec.py python3 codec.py Mickaël Farina — AVA Digital

16m ago

---

**[Open-source AI system on a $500 GPU outperforms Claude Sonnet on coding benchmarks](https://www.reddit.com/r/artificial/comments/1s2yg3y/opensource_ai_system_on_a_500_gpu_outperforms/)**

What if building more and more datacenters was not the only option? If we are able to get similar levels of performance for top models at a consumer level from smarter systems, then its only a matter of time before the world comes to the realization that AI is a lot less expensive and a whole lot more obtainable. Open source projects like ATLAS are on the frontier of this possibility- where a 22 year old college student from Virginia Tech built and ran a 14B parameter AI model on a single $500 Consumer GPU and scored higher than Claude Sonnet 4.5 on coding benchmarks (74.6% vs 71.4% on LiveCodeBench, 599 problems). No cloud, no API costs, no fine-tuning. Just a consumer graphics card and smart infrastructure around a small model. And the cost? Only around $0.004/task in electricity. The base model used in ATLAS only scores about 55%. The pipeline adds nearly 20 percentage points by generating multiple solution approaches, testing them, and selecting the best one. Proving that smarter infrastructure and systems design is the future of the industry. Repo: https://github.com/itigges22/ATLAS

1d ago

---

**[Google Gemini still has no native chat export in 2025. Here's how I solved it for my research workflow.](https://www.reddit.com/r/artificial/comments/1s40w44/google_gemini_still_has_no_native_chat_export_in/)**

One thing that's always bothered me about Gemini: you can run a 30-minute Deep Research session, get an incredible research report with 40+ citations, and then... there's no export button. Not even copy-to-clipboard for the formatted version. Compare this to ChatGPT which has had a built-in export function for a while now. My workflow is heavy Gemini use for research, then piping the output into Obsidian for long-form writing. The lack of export was a constant manual friction point. I ended up building a Chrome extension to solve this: Gemini Export Studio. What it does: - Export to PDF, Markdown (Obsidian-ready), JSON, CSV, Plain Text, or PNG - Deep Research exports with citations preserved inline - Merge multiple chats into one document - PII scrubbing (auto-redacts emails/names before sharing) - 100% local processing, no servers, no account It's free. Link in comments to avoid spam filter. Curious if others have hit this same wall with Gemini and what workarounds you've used.

2h ago

---

**[A nearly undetectable LLM attack needs only a handful of poisoned samples](https://www.reddit.com/r/artificial/comments/1s3zenu/a_nearly_undetectable_llm_attack_needs_only_a/)**

Prompt engineering has become a standard part of how large language models are deployed in production, and it introduces an attack surface most organizations have not yet addressed. Researchers have developed and tested a prompt-based backdoor attack method, called ProAttack, that achieves attack success rates approaching 100% on multiple text classification benchmarks without altering sample labels or injecting external trigger words.

🔗 [Help Net Security](https://www.helpnetsecurity.com/2026/03/26/llm-backdoor-attack-research/) • 4h ago

---

**[How do you save and organize your Gemini Deep Research outputs? Curious what workflows people use](https://www.reddit.com/r/artificial/comments/1s3yo4t/how_do_you_save_and_organize_your_gemini_deep/)**

I've been using Gemini for deep research and architecture planning, and the outputs are genuinely impressive. But I keep running into the same problem: once the research is done, getting it OUT of Gemini cleanly is painful. Copy-paste breaks all the formatting. Screenshots of long chats = 15 ugly images. Pasting into Notion = disaster. I ended up building a Chrome extension to export chats as PDF, Markdown, JSON, CSV, or plain text — one click, no server, no sign-up. But I'm curious — what do you all do? Manual copy-paste? Screenshot? Something else? What format do you actually need your Gemini outputs in for your workflow?

4h ago

---

**[Using 'imaginative' AI to survey past and future earthquake damage](https://www.reddit.com/r/artificial/comments/1s3r9zz/using_imaginative_ai_to_survey_past_and_future/)**

Researchers have used artificial intelligence to develop a new tool for assessing earthquake damage, a leap that could ultimately help first responders in making critical rescue decisions, suggests a new study. The team's AI, called the LoRA-Enhanced Ground-view Generation (LEGG) diffusion model, is trained on real aerial drone images that it uses to create highly photorealistic 3D reconstructions of the ground. Creating imagery detailed enough to fully capture a region's physical characteristics distinguishes this synthetic model, enabling it to recognize complex visual patterns and predict where structures may be damaged, even in densely populated urban areas. "What our algorithm does is generate thousands of pairs of semi-realistic photos of what a building looks like on the top and from the ground," said Rongjun Qin, co-author of the study and a professor of civil, environmental and geodetic engineering at The Ohio State University. "Having such data is vital, as drones gather important information from above, but people actually make emergency decisions from ground-level views." Similar studies on the aftermath of devastating earthquakes relied on UAV or lidar-based detection methods to survey collapsed buildings and structures from above, but none had addressed how damage might have looked on the ground prior to prolonged rescue efforts. Moreover, depending on the severity of the earthquake, manual damage assessments can take days or weeks to fully complete, which isn't ideal for rapid recovery missions. In this paper, Qin and his colleagues introduce a framework for bridging these gaps using AI-generated images, with the aim of laying the foundation for more accurate disaster assessment and better earthquake preparedness. "This simulation is essentially a map, but an experienced and well-trained AI could offer an additional supply of information that would be really helpful for emergency crews in making quick decisions about where to go when the clock is ticking," said Qin. The study was published in the International Journal of Remote Sensing. To test the applicability of their proposed algorithm, researchers conducted a case study on a real-world disaster, the 2023 Kahramanmaras, Turkey, earthquake, a powerful 7.8 magnitude quake that destroyed 280,000 buildings and damaged at least 700,000 more. Comparing drone imagery from 2015 to photos taken in the days after the shake revealed dramatic changes in the local built environment, such as collapsed buildings and temporary shelters in open areas. After showing their AI a dataset of only 3,000 of these city structures, the model was able to create images that enhanced the recognition of a number of building issues, including façade cracks, building tilts and partial collapses, demonstrating that it could extract subtle cues from multiple sources to generate high-resolution, photorealistic street-level views. This advanced capability stems from the combination of drone and ground imagery that researchers injected it with to ensure the model had a strong starting point for understanding potential structural damage and its community effects, said Qin. "As long as you have good data, AI can serve as a very generous predictor of past and future outcomes," he said. "It's a tool that can be incredibly helpful." In the future, applying the team's framework to novel scenarios or areas could inspire governments and engineers to design more resilient infrastructures as well as reshape post-disaster assessment and emergency management policies. "This work presents a great opportunity for engineers and other decision makers to remotely assess the damage in structures soon after a disaster," said Halil Sezen, co-author of the paper and a professor of structural engineering in civil, environmental and geodetic engineering at Ohio State. That said, their algorithm will likely be utilized in tandem with other emergency or resource planning tools, said Qin, noting that with more in-depth experiments, the model could help anticipate destruction levels in other earthquake-prone environments, like Japan or California. "There is still a lot of work to be done to bring in the kind of perspective AI offers," said Qin. "But the more good quality data that we have, the faster we're going to achieve our goals."

🔗 [phys.org](https://phys.org/news/2026-03-ai-survey-future-earthquake.html) • 10h ago

---

**[Can any one prove that i am wrong ? People dont use AI when it comes to emotion.](https://www.reddit.com/r/artificial/comments/1s401q9/can_any_one_prove_that_i_am_wrong_people_dont_use/)**

Many company are trying to replace some job roles with AI . But i dont agree with that i dont think people need that , what do you think ? 1) Founders building Sales AI agent products and company replacing Sales persons with AI voice : i think one of the factor which people buy products and services due to human to human trust. 2) [*recommendation*](https://search.brave.com/search?q=recommendation&spellcheck=0&source=alteredQuery) : will you watch a movie that is just reviewed by AI , Do you trust an AI given trip itinerary or a human prepared itinerary . I trust humans because i care about humans. 3) AI robots toys or pets : i dont think they can replace real pets , why because ai robots are so perfect and [*predictable*](https://search.brave.com/search?q=predictable&spellcheck=0&source=alteredQuery) *and i belive people dont like that .* *After using LLMs for more than 2 years i dont feel i am using AI for anything which is connected with my emotions , what do you think*

3h ago

---

---

## Google News: "ai"

**[Meta Lays Off 700 Employees, While Rewarding Top Executives](https://www.nytimes.com/2026/03/25/technology/meta-layoffs-ai-executives.html)**

The New York Times • 14h ago

---

**[China bars executives at Meta-owned AI company from leaving country](https://www.washingtonpost.com/national-security/2026/03/25/meta-manus-china-executives-banned/)**

Manus’s CEO and chief scientist are facing scrutiny from Beijing over the company’s $2 billion sale to Meta.

The Washington Post • 4h ago

---

**[Meet Figure AI: The company behind the humanoid robot hosted by Melania Trump](https://www.cnbc.com/2026/03/26/figure-ai-the-robotics-company-hosted-by-melania-trump.html)**

The White House hosted its first humanoid robot guest, with first lady Melania Trump appearing alongside a robot from startup Figure AI.

CNBC • 57m ago

---

**[Melania Trump brings special guest to AI event](https://www.cnn.com/2026/03/25/politics/video/melania-trump-robot-ai-event-white-house-klein-vrtc)**

First lady Melania Trump brought an AI-powered humanoid robot to a roundtable event at the White House on the second day of the inaugural Fostering the Future Together Global Coalition Summit. CNN’s Betsy Klein reports.

CNN • 9h ago

---

**[Robot joins Melania Trump at White House event to tout AI teachers](https://www.reuters.com/world/us/robot-joins-melania-trump-white-house-event-tout-ai-teachers-2026-03-25/)**

Reuters • 14h ago

---

**[AI builders push ahead as skepticism grows](https://www.axios.com/2026/03/26/ai-summit-optimists-humans-economy)**

Axios • 1h ago

---

**[OpenAI drops AI video tool Sora, startling Disney, sources say](https://www.ksl.com/article/51472526/openai-drops-ai-video-tool-sora-startling-disney-sources-say)**

The Walt Disney Company was blindsided with word that OpenAI was dropping video tool Sora altogether on Monday following a meeting, a person familiar with the matter said.

KSL.com • 10h ago

---

**[OpenAI thought it could own AI videos. The reality was too expensive](https://www.cnn.com/2026/03/26/business/openai-sora-consumer-misread)**

Six months and millions of dollars down the drain, OpenAI is pulling the plug on what it once called “the most powerful imagination engine ever built.”

CNN • 1h ago

---

**[Sam Altman Is Finally Admitting Something No One Else Wants To](https://slate.com/technology/2026/03/ai-openai-sam-altman-disney-sora-shutdown.html)**

OpenAI’s abrupt shutdown of Sora reveals the A.I. boom might be a lot more fragile than it looks.

Slate • 2d ago

---

**[Updates to GitHub Copilot interaction data usage policy](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/)**

From April 24 onward, interaction data from Copilot Free, Pro, and Pro+ users will be used to train and improve our AI models unless they opt out.

The GitHub Blog • 15h ago

---

---

## HackerNews: "ai"

**[Is anybody else bored of talking about AI?](https://news.ycombinator.com/item?id=47508745)**

Is anybody else bored of talking about AI?

⬆️ 726 • 💬 514 • 1d ago • [Unfinished Side Projects](https://blog.jakesaunders.dev/is-anybody-else-bored-of-talking-about-ai/)

---

**[Flighty Airports](https://news.ycombinator.com/item?id=47511589)**

Search any airport for real-time delays, weather, arrivals, departures, and performance insights powered by Flighty.

⬆️ 548 • 💬 179 • 1d ago • [Flighty](https://flighty.com/airports)

---

**[TurboQuant: Redefining AI efficiency with extreme compression](https://news.ycombinator.com/item?id=47513475)**

⬆️ 517 • 💬 144 • 1d ago • [research.google](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)

---

**[So where are all the AI apps?](https://news.ycombinator.com/item?id=47503006)**

Practical AI R&D

⬆️ 441 • 💬 409 • 1d ago • [Answer.AI](https://www.answer.ai/posts/2026-03-12-so-where-are-all-the-ai-apps.html)

---

**[I built an AI receptionist for a mechanic shop](https://news.ycombinator.com/item?id=47487536)**

Learn how I built an ai receptionist for my brother's mechanic shop

⬆️ 316 • 💬 320 • 2d ago • [itsthatlady.dev](https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/)

---

**[The bridge to wealth is being pulled up with AI](https://news.ycombinator.com/item?id=47503296)**

For two centuries, the credential system gave intelligence a route to heritable capital. Artificial intelligence is closing that route. This essay builds the argument from first principles - with probability theory, interactive simulations, and a prediction specific enough to be falsifiable - and puts a number on the window that remains.

⬆️ 266 • 💬 394 • 1d ago • [Daniel Homola](https://danielhomola.com/m%20&%20e/ai/your-bridge-to-wealth-is-being-pulled-up/)

---

**[Show HN: Cq – Stack Overflow for AI coding agents](https://news.ycombinator.com/item?id=47491466)**

cq explores a Stack Overflow for agents, a shared commons where agents can query past learnings, contribute new knowledge, and avoid repeating the same mistakes in isolation.

⬆️ 220 • 💬 98 • 2d ago • [Mozilla.ai](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)

---

**[Disney Exits OpenAI Deal After AI Giant Shutters Sora](https://news.ycombinator.com/item?id=47509234)**

The studio giant will no longer move forward with its OpenAI investment, as the AI company exits the video generation business.

⬆️ 206 • 💬 3 • 1d ago • [The Hollywood Reporter](https://www.hollywoodreporter.com/business/digital/openai-shutting-down-sora-ai-video-app-1236546187/)

---

**[The AI Industry Is Lying to You](https://news.ycombinator.com/item?id=47506259)**

Hi! If you like this piece and want to support my independent reporting and analysis, why not subscribe to my premium newsletter? It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5000 to 18,000 words, including

⬆️ 160 • 💬 128 • 1d ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/the-ai-industry-is-lying-to-you/)

---

**[I tried to prove I'm not AI. My aunt wasn't convinced](https://news.ycombinator.com/item?id=47515502)**

I asked experts if I'm real. Bad news. Even my aunt wasn't sure if I was a deepfake. AI is so convincing that a sitting prime minister struggled to prove he's alive. You might be next.

⬆️ 159 • 💬 178 • 23h ago • [bbc.com](https://www.bbc.com/future/article/20260324-i-tried-to-prove-im-not-an-ai-deepfake)

---

---

## YouTube Videos: "ai"

**[AI Whistleblower: We Are Being Gaslit By The AI Companies! They’re Hiding The Truth About AI!](https://www.youtube.com/watch?v=Cn8HBj8QAbk)**

The truth about Sam Altman. AI Critic Karen Hao reveals what 90 OpenAI employees told her. Karen Hao is an AI expert, ...

📺 The Diary Of A CEO

👁️ 47K • 👍 3K • 💬 449 • ⏱️ 2:09:13 • 2h ago

---

**[AI isn&#39;t going how we thought it would](https://www.youtube.com/watch?v=RsRVI6a0ZdU)**

Sources for this video: https://www.perplexity.ai/search/what-are-the-studies-showing-t-XhYKezmqQ5yeO3lqRFgPoQ?sm=d.

📺 David Shapiro

👁️ 32K • 💬 302 • ⏱️ 21:46 • 22h ago

---

**[the AI Bubble is Popping](https://www.youtube.com/watch?v=RdP06aUGbjI)**

today I talked about OpenAI ending Sora the AI video generation app. discord server: https://www.discord.gg/QmcmZdkCMc ...

📺 spatnz

👁️ 21K • 👍 2K • 💬 254 • ⏱️ 2:19 • 18h ago

---

**[FREE Tool To Create Ai Video (Unlimited Technique)](https://www.youtube.com/watch?v=T_Im-MK34tQ)**

We've found a fantastic new free AI tool that lets anyone create amazing video content! This new free AI tool is a game-changer for ...

📺 Africa Amaze

👁️ 6K • 👍 329 • 💬 108 • ⏱️ 8:19 • 21h ago

---

**[Inside Elon Musk&#39;s TeraFab AI Factory](https://www.youtube.com/watch?v=jjmwO0TvPkM)**

Grab your free seat to the 2-Day AI Mastermind here: https://link.outskill.com/TESLASPACEMAR4 Check out The Space Race: ...

📺 The Tesla Space

👁️ 79K • 👍 3K • 💬 212 • ⏱️ 12:44 • 15h ago

---

**[Claude Code + Nano Banana 2 = INSANE AI Website Animations](https://www.youtube.com/watch?v=zJl1yFYujiw)**

Claude Code + Nano Banana is Great for AI Website Animations Try Higgsfield today - https://higgsfield.ai?fpr=utm&fp_sid=mira ...

📺 Mira AI

👁️ 10K • 💬 8 • ⏱️ 10:39 • 17h ago

---

**[Jensen Huang: NVIDIA - The $4 Trillion Company &amp; the AI Revolution | Lex Fridman Podcast #494](https://www.youtube.com/watch?v=vif8NQcjVf0)**

Jensen Huang is the co-founder and CEO of NVIDIA, the world's most valuable company and the engine powering the AI ...

📺 Lex Fridman

👁️ 552K • 👍 15K • 💬 2K • ⏱️ 2:25:59 • 2d ago

---

**[BLACKOUTS IMMINENT As AI Strains Power Grids](https://www.youtube.com/watch?v=xr3wXf8YOeo)**

Ryan and Emily discuss potential blackouts across the US. Sign up for a PREMIUM Breaking Points subscriptions for full early ...

📺 Breaking Points

👁️ 135K • 👍 4K • 💬 614 • ⏱️ 6:41 • 15h ago

---

**[New Self Improving Hyperagents Break Limits Of AI](https://www.youtube.com/watch?v=7a6mCGDeGco)**

Visit https://lumalabs.ai/airevolution10 to try Luma AI just crossed a major line. Meta introduced Hyperagents that can rewrite their ...

📺 AI Revolution

👁️ 35K • 👍 934 • 💬 83 • ⏱️ 11:33 • 1d ago

---

**[Cops Use AI, Arrest the Wrong Guy](https://www.youtube.com/watch?v=kAEdH1YXB8I)**

Imagine you go into a business and their AI surveillance camera thinks it recognizes you as a trespasser. So that business ...

📺 The Civil Rights Lawyer

👁️ 517K • 👍 25K • 💬 3K • ⏱️ 2:37 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 184,056 • ❤️ 1,348 • 2d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 425,497 • ❤️ 962 • 15d ago

---

**[Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)**

*NVIDIA*

Nemotron-Cascade-2-30B-A3B is a 30B MoE model (3B active parameters) excelling in reasoning and agentic tasks, achieving top performance on math (IMO 2025) and code reasoning (IOI 2025) benchmarks. It supports both 'thinking' and 'instruct' modes for versatile text generation.

`text-generation` `31.6B`

⬇️ 55,529 • ❤️ 305 • 1d ago

---

**[daVinci-MagiHuman](https://huggingface.co/GAIR/daVinci-MagiHuman)**

*SII - GAIR*

daVinci-MagiHuman is a fast, single-stream Transformer model for generating high-quality, human-centric audio-video from text or images. It excels at expressive facial performance, natural speech-expression coordination, and accurate audio-video synchronization across multiple languages, with inference speeds of 2 seconds for 256p and 38 seconds for 1080p.

`image-to-video`

⬇️ 273 • ❤️ 168 • 20h ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 11,868 • ❤️ 373 • 7d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 57,056 • ❤️ 155 • 1d ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 22,089 • ❤️ 458 • 13d ago

---

**[Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2 is a fine-tuned LLM optimized for efficient chain-of-thought reasoning, delivering higher accuracy with reduced token usage. It excels in resource-constrained environments and agentic workflows by providing faster, more economical reasoning.

`image-text-to-text` `9.0B`

⬇️ 66,854 • ❤️ 161 • 3d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Claude 4.6 Opus Chain-of-Thought distillation. It excels at structured, step-by-step problem-solving within `<think>` tags, making it ideal for coding agents and complex task execution with improved autonomy and stability.

`image-text-to-text` `26.9B`

⬇️ 510,875 • ❤️ 410 • 2d ago

---

**[Foundation-1](https://huggingface.co/RoyalCities/Foundation-1)**

*Royal Cities*

Foundation-1 is a structured text-to-sample model for music production, enabling precise control over instrumentation, timbre, FX, and musical structure (tempo, key, bar count) for generating coherent, production-ready audio loops.

⬇️ 0 • ❤️ 263 • 9d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 30 • 💬 2 • ⭐ 41,917 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 14 • 💬 1 • ⭐ 13,620 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 39 • 💬 2 • ⭐ 19,954 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 59 • 💬 4 • ⭐ 19,971 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 33 • 💬 5 • ⭐ 909 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 4 • 💬 0 • ⭐ 817 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://huggingface.co/papers/2603.21986)**

*SII-GAIR, Sand. ai, Ethan Chern et al. (45 authors)*

daVinci-MagiHuman is an open-source audio-video generative model that synchronizes text, video, and audio through a single-stream Transformer architecture, achieving high-quality human-centric content generation with efficient inference capabilities.

▲ 101 • 💬 5 • ⭐ 813 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2603.21986) • [💻 code](https://github.com/GAIR-NLP/daVinci-MagiHuman) • [🔗 project](https://huggingface.co/spaces/SII-GAIR/daVinci-MagiHuman)

---

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 194 • 💬 5 • ⭐ 8,260 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 17 • 💬 0 • ⭐ 36,669 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://huggingface.co/papers/2603.08127)**

*Yougang Lyu, Xi Zhang, Xinhao Yi et al. (12 authors)*

EvoScientist is an adaptive multi-agent framework that enhances scientific discovery by continuously learning from past interactions through persistent memory modules.

▲ 15 • 💬 5 • ⭐ 1,979 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08127) • [💻 code](https://github.com/EvoScientist/EvoScientist)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 56.7k • 🔱 7.9k • 10h ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 22.6k • 🔱 1.1k • 16h ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 12.3k • 🔱 656 • 7m ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 7.3k • 🔱 582 • 1h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 6.9k • 🔱 1.1k • 16h ago

---

**[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)**

734+ structured cybersecurity skills for AI agents · MITRE ATT&CK mapped · agentskills.io open standard · Works with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI & 20+ platforms · Penetration testing, DFIR, threat intel, cloud security & more · Apache 2.0

`Python` `ai-agents` `claude` `claude-code` `cloud-security` `cybersecurity`

⭐ 3.7k • 🔱 381 • 2d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.2k • 🔱 215 • 12d ago

---

**[open-pencil/open-pencil](https://github.com/open-pencil/open-pencil)**

AI-native design editor. Open-source Figma alternative.

`TypeScript`

⭐ 3.2k • 🔱 283 • 15h ago

---

**[chenhg5/cc-connect](https://github.com/chenhg5/cc-connect)**

Bridge local AI coding agents (Claude Code, Cursor, Gemini CLI, Codex) to messaging platforms (Feishu/Lark, DingTalk, Slack, Telegram, Discord, LINE, WeChat Work). Chat with your AI dev assistant from anywhere — no public IP required for most platforms.

`Go`

⭐ 3.1k • 🔱 270 • 3h ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 3.1k • 🔱 100 • 14d ago

---

---

*Generated by PeekDeck - A glance is all you need*
