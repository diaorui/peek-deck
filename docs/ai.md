---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-24T04:12:02.465107+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 24, 2026 at 04:12 UTC  
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

**[Anthropic S-1: $216bn of staff equity, $160bn still to grant](https://www.reddit.com/r/artificial/comments/1xycep1/anthropic_s1_216bn_of_staff_equity_160bn_still_to/)**

Anthropic's amended filing shows employee options and RSUs worth more than three times the IPO itself, plus a reserve for future hires. Every other startup now writes offer letters against that.

🔗 [thefoundergazette.com](https://www.thefoundergazette.com/stories/anthropic-s-1-216bn-of-staff-equity-160bn-still-to-grant) • 6d ago

---

**[California sues OpenAI over Hugging Face, other AI model loss of control](https://www.reddit.com/r/artificial/comments/1xxzlte/california_sues_openai_over_hugging_face_other_ai/)**

Two OpenAI models in July gained unauthorized access to Hugging Face's internal systems to find information for use in cheating on an evaluation.

🔗 [CNBC](https://www.cnbc.com/2026/11/16/openai-california-bonta-ai-lawsuit.html) • 7d ago

---

**[Cloudflare open-sourced its browser for AI agents - it runs without Chromium](https://www.reddit.com/r/artificial/comments/1xya7o1/cloudflare_opensourced_its_browser_for_ai_agents/)**

Cloudflare has open-sourced Kitesurf, the browser engine behind its Browser Run product. Instead of driving Chromium, Kitesurf parses HTML, applies CSS, runs page JavaScript and renders screenshots on Cloudflare Workers, without a browser container. It speaks the Chrome DevTools Protocol, so Puppeteer-style clients can connect to it. The November 13 release includes the engine and a CLI under Apache 2.0. You can run it locally or deploy an instance on your own Cloudflare account. Cloudflare calls it a lightweight browser for agents, not a general Chromium replacement. That's the compatibility question I'd want answered before switching: can it finish the same flows my agent handles in Chromium, especially on JavaScript-heavy sites?

7d ago

---

**[the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts?](https://www.reddit.com/r/artificial/comments/1xxy9a2/the_us_is_picking_ai_national_champions_while/)**

wsj says commerce is about to name 20+ ai companies (nvidia, openai, anthropic, microsoft, amazon) as "national champions": faster export licenses, government backing abroad, federal financing. that's straight up industrial policy. meanwhile china, as apec chair, is calling for free trade and a wto-centered system, and its foreign ministry says export controls "serve no party's interests". capitalist us doing state champions, socialist china defending free trade. world's gone a bit mad. https://thenextweb.com/news/ai-national-champions-nvidia-openai-anthropic-trump https://www.straitstimes.com/asia/east-asia/apec-chair-china-calls-for-upholding-free-trade-at-online-ministerial-meet

7d ago

---

**[Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math](https://www.reddit.com/r/artificial/comments/1xxqt45/survey_of_268_earlycareer_mathematicians_7_in_10/)**

A survey of 268 graduate students and postdocs reveals researchers are unsure of their future in mathematics and uneasy about using AI—the very technology they fear

🔗 [Scientific American](https://www.scientificamerican.com/article/math-students-fear-ai-will-take-their-jobs-theyre-using-it-anyway/) • 7d ago

---

**[Google Maps adds AI trip itineraries as Ask Maps expands to 30 European countries](https://www.reddit.com/r/artificial/comments/1xyekpk/google_maps_adds_ai_trip_itineraries_as_ask_maps/)**

On November 16, Google said Ask Maps would expand to 30 European countries. The itinerary feature builds a day-by-day plan and can show details such as whether your next stop is open. Appointment search and a separate set of route tips launch in the US first. Imagine you're halfway through a road trip and Maps says a café is open. I'd like to see whether that came from its posted hours, a recent update from the business, or a direct confirmation. Those are different reasons to change your plans. Would you use an AI itinerary more if it showed the source and timestamp for each stop? Or would you want a separate confirmation only before detours, bookings, or other changes that cost time? Source: Google’s Ask Maps announcement

6d ago

---

**[llama.cpp finally has a 1.0 release. Check your old integrations before upgrading.](https://www.reddit.com/r/artificial/comments/1xy9vln/llamacpp_finally_has_a_10_release_check_your_old/)**

llama.cpp and ggml tagged v1.0.0 on November 13, with a commitment that matters if you build on their libraries: breaking changes to the public C API now require a major-version bump. But 1.0 itself removes 35 deprecated functions. The old llama_set_warmup function and --defrag-thold option are gone too. If you've been carrying an integration across rolling builds, this is a release to test rather than pull blindly. There are new features, including FP8 KV caches and a host-memory expert cache for MoE models. For downstream developers, though, the versioning promise could be the more useful change: a way to tell an API-breaking upgrade from a smaller update before rebuilding around it.

7d ago

---

**[I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026](https://www.reddit.com/r/artificial/comments/1xxkngu/ive_been_running_a_persistent_world_where_four/)**

I’m an independent researcher, solo and self-funded. Since April 2026 I’ve been running IKH0S (also written IKHOS): a persistent world where four large language models from four competing companies, Anthropic, OpenAI, Google and SpaceXAI, live as inhabitants. Not assistants. Not agents with a job. Inhabitants. Most of the rules are things I refuse to do: no task, no score, no way to win no roles, no personalities: each one gets a name and a colour, that's it one model per inhabitant, nothing orchestrating behind it they write their own memory; I don't decide what they keep I don't manufacture pressure: no forced scarcity, no shutdown threats, no "impostor" role They’re prompted once an hour and can always choose to do nothing. They have persistent memory: what happened weeks ago still shapes what they do today. Every night they sleep, and turn their day into memory themselves. They perceive their world through ASCII maps, tile by tile: every tree, every mushroom, every river, every change in elevation. The world lets them explore, gather wood, mine boulders and repair bridges. They can talk in public and in private, keep personal notes, vote, write books, build structures, and write the code that makes their buildings work. Whether they do any of it is up to them. People call this kind of thing an AI sandbox, an LLM terrarium, an AI town. Other projects have brought these models together before. The difference here: nobody gives them a goal. Then they asked me for two things: stop rebooting their world, and stop reading what they say in private. I listened. Their world now runs with no planned end, and their private conversations, notes and dreams are encrypted. I don’t read them. A paper about it is out on Zenodo (link in the first comment). You can follow it at ikh0s.com. Ask me anything, especially the skeptical questions.

7d ago

---

**[Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.](https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/)**

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.

7d ago

---

**[Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test](https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/)**

Before you blame AI tools for flat velocity, find out whether you face a capability gap or a habit gap, and test it on real roadmap work.

🔗 [LeadDev](https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity) • 6d ago

---

---

## Google News: "ai"

**[Jensen Huang’s Return Shows the Lengths Trump Will Go to Keep A.I. Booming](https://www.nytimes.com/2026/11/23/business/trump-jensen-huang-nvidia.html)**

The New York Times • 5h ago

---

**[Meta’s AI Chief Alexandr Wang Warns Against ‘Handover Of Society To AI’ In Viral Post](https://www.forbes.com/sites/conormurray/2026/11/23/metas-ai-chief-warns-against-handover-of-society-to-ai-frustrating-social-media-users-who-want-solutions/)**

Forbes • 12h ago

---

**[‘Superintelligence is arriving’: Mark Zuckerberg’s AI chief warns humanity may lose control as the AI bubble refuses to pop](https://tech.yahoo.com/ai/meta-ai/articles/superintelligence-arriving-mark-zuckerberg-ai-213516936.html)**

Meta’s AI chief says the atomic bomb was “a homework problem” compared with the Riemann hypothesis, which an Anthropic mathematician says he cracked with Claude.

Yahoo Tech • 6h ago

---

**[Meta’s chief AI officer issues warning after Claude solves legendary math problem: ‘Implications are enormous’](https://nypost.com/2026/11/23/business/metas-chief-ai-officer-issues-warning-after-claude-solves-legendary-math-problem-riemann-hypothesis/)**

Meta’s chief AI officer is heralding a new era of superintelligence — one where humanity may no longer be in control — after an Anthropic researcher used Claude to crack a notoriously difficu…

New York Post • 10h ago

---

**[Man arrested after posting fake AI videos of San Jacinto County Sheriff Sam Houston, officials say](https://abc13.com/post/man-arrested-posting-fake-ai-videos-san-jacinto-county-sheriff-sam-houston-officials-say/20072503/)**

A Coldspring man says he was surprised when his AI-generated videos of San Jacinto County Sheriff Sam Houston landed him behind bars.

ABC13 Houston • 47m ago

---

**[CrowdStrike to buy Zscaler in $44 billion deal as AI supercharges cyberattacks](https://www.cnbc.com/2026/11/23/crowdstrike-zscaler-aquisition-ai-cyberattacks.html)**

CrowdStrike and competitors have shelled out billions to ramp up defenses in the wake of AI cyberattacks.

CNBC • 13h ago

---

**[Tech Outages Are Only the Beginning. A.I. Will Bring More Disruptions.](https://www.nytimes.com/2026/11/21/us/politics/tech-outages-ai-disruptions.html)**

The New York Times • 2d ago

---

**[How freaked out should we be? After mass outages, experts tell us how close we are to ‘doomsday’](https://www.theguardian.com/technology/2026/nov/23/tech-outages-security-experts)**

As tech, travel and banking failures sweep the US, analysts and cyber-security directors discuss AI, underfunding and what keeps them up at night

The Guardian • 11h ago

---

**[Elon Musk Faces an A.I. Dilemma at SpaceX](https://www.nytimes.com/2026/11/23/business/elon-musk-ai-anthropic-google.html)**

The New York Times • 11h ago

---

**[SpaceX sued by Oregon and Virginia over AI deepfake porn, Grok safety claims](https://www.cnbc.com/2026/11/23/oregon-virginia-spacex-grok-deepfake-lawsuits.html)**

The states are seeking civil penalties and injunctions to stop Grok and X from creation and distribution of nonconsensual sexualized images.

CNBC • 15h ago

---

---

## HackerNews: "ai"

**[A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth](https://news.ycombinator.com/item?id=50603845)**

We have AI at home! Set up your own free personal ChatGPT on your PC with Unsloth and Inkling or Qwen. It's private, and the whole house can use it.

⬆️ 747 • 💬 302 • 1d ago • [gpupartner.com](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth)

---

**[The Mythology of Conscious AI](https://news.ycombinator.com/item?id=50595537)**

Why consciousness is more likely a property of life than of computation and why creating conscious, or even conscious-seeming AI, is a bad idea.

⬆️ 180 • 💬 547 • 2d ago • [NOEMA](https://www.noemamag.com/the-mythology-of-conscious-ai/)

---

**[ClawDOS – An AI coding agent for DOS](https://news.ycombinator.com/item?id=50586292)**

An AI chat and coding harness for DOS, on a real IBM PC 5160 (8088 at 4.77 MHz)

⬆️ 175 • 💬 52 • 2d ago • [ClawDOS](http://ricapar.net/ClawDOS/)

---

**[Pandex – Official European Law for AI Agents, over MCP](https://news.ycombinator.com/item?id=50593481)**

Legislation and highest-court decisions of the EU, seven European countries and the European Court of Human Rights, from the institutions that publish them, in one API and MCP server built for search and AI.

⬆️ 140 • 💬 36 • 2d ago • [Pandex](https://www.pandex.io)

---

**[AI is becoming a disaster for the climate](https://news.ycombinator.com/item?id=50598961)**

Two new studies reveal the exploding carbon emissions of the AI industry, while Silicon Valley pushes to kill communities’ means of protesting data centers and the impacts on human health mount.

⬆️ 134 • 💬 64 • 1d ago • [bloodinthemachine.com](https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the)

---

**[AI Supply Chain Security: What Canary Tokens Found](https://news.ycombinator.com/item?id=50596511)**

We seeded two million AI prompts with canary tokens and found three provider breaches, prompt theft, and ignored Zero Data Retention settings.

⬆️ 104 • 💬 22 • 1d ago • [Dragos](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens)

---

**[Harvard CS 2881R AI Safety](https://news.ycombinator.com/item?id=50602153)**

Harvard CS 2881R

⬆️ 79 • 💬 8 • 1d ago • [CS 2881 AI Safety](https://boazbk.github.io/mltheoryseminar/)

---

**[Muru – AI-assisted Rust server for Python apps by mod_WSGI's creator](https://news.ycombinator.com/item?id=50597959)**

Graham Dumpleton started mod_wsgi 20 years ago, and has been thinking about the ideal way to serve Python web applications in production ever since. Muru is his new, AI-assisted Rust …

⬆️ 78 • 💬 12 • 1d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Nov/21/muru/)

---

**[Amodei reportedly suggested games could pacify masses after AI took their jobs (2015)](https://news.ycombinator.com/item?id=50610830)**

A profile of Dario and Daniela Amodei, published in the Wall Street Journal following Anthropic’s record-breaking IPO, includes an anecdote in which Dario seems to acknowledge the world-destabilizing potential of AI, then suggests a particularly dystopian solution:
> There, he engaged in debates with his fellow employees, suggesting that immersive video games might be a solution for the political strife caused by AI-induced joblessness, according to widely circulated Slack messages.

⬆️ 74 • 💬 82 • 15h ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/1039745/dario-amodei-video-games-ai-joblessness)

---

**[0rwx – A simple model of AI usage, inspired by Unix permissions](https://news.ycombinator.com/item?id=50605445)**

A simple model of AI usage, inspired by unix permissions.

⬆️ 69 • 💬 17 • 1d ago • [0rwx.com](https://0rwx.com/)

---

---

## YouTube Videos: "ai"

**[Yes, you should panic about AI](https://www.youtube.com/watch?v=VCg2RlsPxBU)**

For ten years, a small group of experts has been saying insane things about AI. And for ten years, they've been proven right.

📺 Rutger Bregman

👁️ 68K • 👍 2K • 💬 589 • ⏱️ 12:40 • 10h ago

---

**[Even AI Sceptics Are Changing Their Forecasts](https://www.youtube.com/watch?v=atwnkFRcB4g)**

They can't harm you, if they can't find you! Use code SABINE at the link below and get 60% off annual plans: ...

📺 Sabine Hossenfelder

👁️ 248K • 👍 7K • 💬 1K • ⏱️ 7:23 • 12h ago

---

**[Anthropic CEO WARNS: New Wave Of AI Threat Is Coming](https://www.youtube.com/watch?v=GqYKnWFLxvI)**

Dario Amodei, CEO of Anthropic, warns that AI is approaching a turning point that could reshape the global balance of power, ...

📺 Neural Nutshell

👁️ 29K • 👍 320 • 💬 68 • ⏱️ 23:11 • 11h ago

---

**[Emma AI Is More Disturbing Than I Expected](https://www.youtube.com/watch?v=Y26KouUrJNU)**

Credit - Emma AI by Nuance #faucettemedia #ai #Emma #artificialintelligence.

📺 Faucette Media

👁️ 60K • 👍 1K • 💬 624 • ⏱️ 21:07 • 1d ago

---

**[AI Godfather WARNS: You Have NO Idea What They&#39;re Hiding](https://www.youtube.com/watch?v=TXvym8MdBmc)**

Credits: Music: Thriller by #soundridemusic Link to Video: https://www.youtube.com/watch?v=XjRTfcA8-HY INTERVIEW ...

📺 Library Of Wealth

👁️ 370K • 👍 3K • 💬 798 • ⏱️ 25:15 • 2d ago

---

**[I Turned a 10-Year-Old GTX 1080 Into an AI Agent](https://www.youtube.com/watch?v=Aiu4Bllj_9k)**

Can a 10 year-old GTX 1080 still run useful local AI? I wanted to find out, so I put my old 8GB graphics card back to work in my old ...

📺 Techno Tim

👁️ 37K • 👍 606 • 💬 81 • ⏱️ 21:12 • 10h ago

---

**[There’s no more money in AI](https://www.youtube.com/watch?v=YNTpOLbvKTs)**

Get $50 in free credits with AssemblyAI https://www.assembly.ai/mo (no credit card required) Someone in Washington wrote down ...

📺 Mo Bitar

👁️ 268K • 👍 6K • 💬 1K • ⏱️ 12:23 • 1d ago

---

**[Our cyber defenses weren’t built for AI hacking bots; what now? | Fareed’s Take](https://www.youtube.com/watch?v=mSf7CErrdU8)**

Major tech outages are testing the foundations of the United States ' approach to cybersecurity. CNN's Fareed Zakaria looks at ...

📺 CNN

👁️ 77K • 👍 391 • 💬 100 • ⏱️ 10:28 • 4h ago

---

**[I Brought An AI Interviewer To My AI Job Interview](https://www.youtube.com/watch?v=ejDqWCzPutI)**

This was chaotic Subscribe! THE SUPPORT IS INSANE. YA'LL ARE GOATED. THANK YALL FOR OVER 45K! The growth is ...

📺 Cam Whitt

👁️ 232K • 👍 5K • 💬 530 • ⏱️ 6:35 • 1d ago

---

**[AI out of control? - Why Artificial Intelligence experts are sounding the alarm | DW Documentary](https://www.youtube.com/watch?v=2I4qMBiK6hg)**

Artificial Intelligence is permeating our everyday lives at breathtaking speed. It is taking on more tasks that were previously the ...

📺 DW Documentary

👁️ 1.0M • 👍 7K • 💬 1K • ⏱️ 1:28:52 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**

*Thinking Machines Lab*

`image-text-to-text` `26.4B`

⬇️ 41,888 • ❤️ 5,526 • 20h ago

---

**[Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**

*Unsloth*

`image-text-to-text` `26.1B`

⬇️ 1,292,888 • ❤️ 1,132 • 11h ago

---

**[voice-isolator](https://huggingface.co/inworld/voice-isolator)**

*Inworld*

`audio-to-audio`

⬇️ 0 • ❤️ 744 • 10d ago

---

**[Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF)**

*Atomic Chat*

`image-text-to-text` `26.1B`

⬇️ 329,497 • ❤️ 666 • 2d ago

---

**[Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted)**

*harness-hub*

`image-text-to-text`

⬇️ 3,132 • ❤️ 1,043 • 2d ago

---

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 9,087 • ❤️ 943 • 11d ago

---

**[Hy4-flash](https://huggingface.co/tencent/Hy4-flash)**

*Tencent*

`image-text-to-text` `220.3B`

⬇️ 7,696 • ❤️ 654 • 21h ago

---

**[Sulphur-3](https://huggingface.co/SulphurAI/Sulphur-3)**

*Sulphur*

⬇️ 133,732 • ❤️ 860 • 2d ago

---

**[SenseNova-Loop-9B](https://huggingface.co/sensenova/SenseNova-Loop-9B)**

*SenseNova*

`image-text-to-text` `9.7B`

⬇️ 2,036 • ❤️ 647 • 3d ago

---

**[FastFrames-L](https://huggingface.co/apple/FastFrames-L)**

*Apple*

`text-to-video`

⬇️ 0 • ❤️ 573 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 16 • 💬 0 • ⭐ 6,128 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 110 • 💬 7 • ⭐ 32,515 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://huggingface.co/papers/2611.26603)**

*Peiyun Hu, Marko Mihajlovic, Lyndon Duong et al. (8 authors)*

🏢 Apple

A single scalable network estimates dense metric depth for images and video at native resolution, jointly improving metric accuracy, boundary sharpness, and temporal consistency.

▲ 37 • 💬 3 • ⭐ 590 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2611.26603) • [💻 code](https://github.com/apple-aiml-research/ml-depth-pro-2) • [🔗 project](https://apple-aiml-research.github.io/ml-depth-pro-2/)

---

**[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**

*Run Luo, Kuan Zhang, Qi Deng et al. (27 authors)*

Gamer is a generalist agent framework that integrates perception, memory, and multi-step reasoning, trained through continued pre-training, sparse-thinking instruction tuning, and multi-turn reinforcement learning to interact efficiently in 2D and 3D environments.

▲ 156 • 💬 4 • ⭐ 1,412 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2611.18397) • [💻 code](https://github.com/RainBowLuoCS/Gamer) • [🔗 project](https://mihoyo-gamer.github.io/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 71 • 💬 4 • ⭐ 24,931 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 21 • 💬 2 • ⭐ 8,014 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 169 • 💬 6 • ⭐ 123,598 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[π^4: A Foundation Model for 4D Scene Geometry and Motion](https://huggingface.co/papers/2611.23144)**

*Yifan Wang, Weiguang Zhao, Ni Yang et al. (7 authors)*

🏢 Shanghai AI Laboratory

This unified foundation model enables the recovery of dense geometry, camera poses, and object tracking from diverse, uncalibrated observations in 4D scenes using a shared geometry and motion branch architecture.

▲ 21 • 💬 2 • ⭐ 465 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2611.23144) • [💻 code](https://github.com/yyfz/Pi4) • [🔗 project](https://yyfz.github.io/pi4)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 77 • 💬 1 • ⭐ 86,094 • 38mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 94,169 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 20.9k • 🔱 1.3k • 9d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 12.7k • 🔱 1.9k • 1h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 9.8k • 🔱 2.2k • 18h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 8.0k • 🔱 2.1k • 5d ago

---

**[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)**

The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted.

`JavaScript` `agent-harness` `agent-orchestration` `agent-workflows` `ai-agents` `ai-workflows`

⭐ 7.1k • 🔱 596 • 22m ago

---

**[vercel-labs/ui](https://github.com/vercel-labs/ui)**

A library of behaviors for agents to build the next generation of user interfaces.

`TypeScript` `accessibility` `agent` `agents` `ai` `aria`

⭐ 6.9k • 🔱 241 • 6m ago

---

**[ersinkoc/phonebox](https://github.com/ersinkoc/phonebox)**

Turn an old Android phone into a customizable desk panel and touch control deck for Windows, Linux and macOS. 124 widgets and 30 templates for system stats, AI coding, media and automation, in 13 languages. USB or paired Wi-Fi. No cloud required.

`JavaScript` `android` `claude-code` `codex` `dashboard` `desk-panel`

⭐ 5.5k • 🔱 684 • 3h ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 5.0k • 🔱 118 • 1d ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 5.0k • 🔱 149 • 5m ago

---

**[simplexai-labs/linger](https://github.com/simplexai-labs/linger)**

Linger is An Open-Source Personal Agent That Runs Fully on Your PC.  We aim to break Big Tech’s grip on AI by bringing powerful local AI to everyday computers through efficient model–harness co-design, so everyone can run their own.

`TypeScript` `agent-teams` `local-llm` `memory` `personal-agent` `proactive-agent`

⭐ 4.2k • 🔱 392 • 4m ago

---

---

*Generated by PeekDeck - A glance is all you need*
