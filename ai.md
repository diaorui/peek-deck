---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-27T15:43:56.314451+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 27, 2026 at 15:43 UTC  
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

**[Looking for an AI image generator, what's the best one](https://www.reddit.com/r/artificial/comments/1tp80d6/looking_for_an_ai_image_generator_whats_the_best/)**

Obviously there are like hundreds of image gen websites and apps now that AI has become widespread. ChatGPT - not bad but looking for something more robust Midjourney - works well but kind of burns through money quickly Looking for suggestions.

48m ago

---

**[Scoop: Trump appoints Bondi to White House AI panel](https://www.reddit.com/r/artificial/comments/1tox7ca/scoop_trump_appoints_bondi_to_white_house_ai_panel/)**

🔗 [axios.com](https://www.axios.com/2026/05/27/pam-bondi-white-house-ai) • 9h ago

---

**[The Young Are Being Battered by AI as Hiring Shifts to Older Workers](https://www.reddit.com/r/artificial/comments/1tosfvj/the_young_are_being_battered_by_ai_as_hiring/)**

A global survey of CEOs by Oliver Wyman found that the share of executives planning to reduce junior roles over the next year or two has doubled from 17% last year to 43%. Meanwhile, those shifting hiring toward mid-level positions jumped from 10% to 30%. Because AI currently excels most at automating tasks typically performed by junior staff, this group is particularly vulnerable to disruption. Despite all this, more than half of CEOs say it's still too early to assess whether AI is actually delivering on its promised productivity gains. Only 27% said their return on AI investment had met or exceeded expectations, down from 38% just a year ago. Though mid-level employees seem better off than younger workers, the overarching trend is still a shift away from hiring. The survey showed that 74% of CEOs are either freezing or reducing headcount, up from 67% last year. https://gizmodo.com/the-young-are-being-battered-by-ai-as-hiring-shifts-to-older-workers-2000759608

13h ago

---

**[Trisha Gee: AI Won't Fix Your Broken Pipeline](https://www.reddit.com/r/artificial/comments/1tp6ang/trisha_gee_ai_wont_fix_your_broken_pipeline/)**

AI doesn't fix broken pipelines, it exposes them faster. Trisha Gee on what DORA metrics, the SPACE framework, and real measurement reveal about AI adoption.

🔗 [ShiftMag](https://shiftmag.dev/trisha-gee-ai-wont-fix-your-broken-pipeline-it-will-break-it-faster-9785/) • 1h ago

---

**[What AI or dev tools are people actually sleeping on right now?](https://www.reddit.com/r/artificial/comments/1tp0ik5/what_ai_or_dev_tools_are_people_actually_sleeping/)**

Most tooling discussions I come across just end up being the same handful of products getting recommended over and over. Gets old pretty fast. More interested in the stuff flying under the radar. Repo and coding tools, self hosted setups, AI infra, terminal utilities, debugging tools, smaller projects that just do their job well. The kind of thing you only stumble on if you're deep in it. What have you actually been reaching for lately?

6h ago

---

**[How to not doom over AI? Anything encouraging about the future?](https://www.reddit.com/r/artificial/comments/1tp38j9/how_to_not_doom_over_ai_anything_encouraging/)**

I’m a new mom who left my white collar job to be a SAHM but planned to return when they reach kindergarten age. Everyday I spiral thinking I made the wrong “financial” choice to be a SAHM instead of advance my career, I fear my job won’t exist in 5 years, and what will my child’s future look like? I feel like my algorithm definitely makes things worse! Does anyone else think about this stuff constantly?

3h ago

---

**[How I build my own zero cost Agent](https://www.reddit.com/r/artificial/comments/1towpar/how_i_build_my_own_zero_cost_agent/)**

I’ve spent the last few weeks obsessing over one goal: having a personal, self maintaining AI assistant that costs $0and can be controlled from my phone. It wasn't easy. I started with an AWS Ec2 with 50GB storage and t3.micro memory- minimal setup (using the free credits) and made Oracle Cloud instance ($300 free credits but just for a month so I used it for experimenting with local models) I was using Termius to SSH into everything from my phone At first I used OpenClaw. It was cool, but I spent more time fixing it than actually using it. I almost gave up until I saw a video about Hermes Agent. And i actually found Hermes while looking for how to fix an OpenClaw error on YouTube (thanks NetworkChuck 🙌🏽) He mentioned the exact same frustrations I was having, and that Hermes had been stable for a month. I didn't even finish the video before I pulled the repo. The best part? It had a "migrate from OpenClaw" feature. I was up and running in minutes. The hardest part is the rate limits. If you use cloud models especially for code, you hit a wall fast. My solution? The Fallback Chain. Initially I was using openrouter/owl-alpha (stealth models are usually flagships in testing, like big-pickle is deepseek v4) which has 1M context window and was on multiple rankings. Over time after I transitioned to Hermes, I wanted a bit more customization, while owl alpha was good at tasks, It’s nothing to talk about on roleplay, it just scrapes the surface of the character I set in SOUL md file. On my oracle instance I had been experimenting with local models (keep in mind, if you go local, you’ll be sacrificing speed but privacy. Ofc since the vms don’t have a gpu it would be slower, about 3-5 minutes for a simple response) The one I was most impressed with is Google’s Gemma-4-31b-it It played the role perfectly Buuut if you know Google, you’re familiar with their aggressive rate limiting. So I set up my agent to rotate through providers. I start with Gemma 4 for that perfect personality and roleplay via openrouter (add an ai studio api key in BYOK for longer usage). If that hits a limit, I’ve also set the same model via ollama cloud and using Google OAuth directly (basically Gemma 4 3 times lol) And if those all hit limits, it jumps to Qwen3-coder-next (Alibaba, 1M free tokens per model. There’s like 80), then Nova (AWS bedrock), DeepSeek v4 (Azure and Opencode Zen), and Claude Haiku (GitHub). If everything fails, I have Owl Alpha; which is an absolute beast, took almost 70M tokens before I got rate limited once, that too for a few hours. It lives in my Telegram and Discord. It manages my Spotify, handles my emails, and when I need real research done, I have it spawn three separate agents to work in parallel. It’s been 8 days and it hasn't broken once. If you're looking to get AI without spending a fortune, I highly recommend looking into this 🫪

9h ago

---

**[Anthropic just published how they contain Claude agents, including two security incidents they got wrong](https://www.reddit.com/r/artificial/comments/1tomozc/anthropic_just_published_how_they_contain_claude/)**

Anthropic dropped a solid engineering post this week about containment across claude.ai, Claude Code, and Cowork. One of the more transparent writeups from a major AI lab about what actually broke. The core insight: model-layer defenses are probabilistic and will always have a non-zero miss rate. So the real answer is hard environmental containment, not just safer models. Three patterns they use: -claude.ai: ephemeral gVisor containers, fully server-side -Claude Code: OS-level sandbox with human-in-the-loop approvals (93% get approved anyway, so approval fatigue is real) -Cowork: full local VM, credentials never enter the guest Two incidents they disclosed: A red team phished an employee into running a prompt that exfiltrated AWS credentials. Succeeded 24 out of 25 times. The model had nothing to catch because the user was the one typing it. Only egress controls would have stopped it. A third-party found that Cowork’s egress allowlist passes traffic to api.anthropic.com. An attacker embedded an API key in a file in the user’s workspace, Claude followed hidden instructions, and uploaded files to the attacker’s Anthropic account. Sandbox worked perfectly and still leaked data. Their lesson: an allowlist isn’t a destination filter, it’s a capability grant. Every function reachable through an allowed domain is an attack surface. The section on persistent memory poisoning and multi-agent trust escalation at the end is worth reading too if you’re building anything agentic.

17h ago

---

**[Junior roles are getting cut. Here is what I would actually do if I was starting out in 2026.](https://www.reddit.com/r/artificial/comments/1tp6hxl/junior_roles_are_getting_cut_here_is_what_i_would/)**

The survey data keeps coming: 43% of CEOs plan to reduce junior roles over the next year or two. That is not a prediction anymore. That is the hiring environment we are in. So if I was 22 right now, here is what I would actually focus on: Stop competing for entry-level tasks AI already does well Data entry, basic copywriting, first-draft coding, simple research, customer support scripts. These were the foot-in-the-door roles for a generation. They are contracting fast. Competing for them head-on is a bad bet. Get productive with AI tools faster than the next person The businesses that are still hiring want someone who uses AI as a multiplier. Know how to prompt well. Know which tools exist for which workflows. Know how to build simple automations without writing code from scratch. This is not complicated, but it requires consistent practice. Most people are still passive consumers of AI. Being an active user who produces real output with it already separates you from a large portion of the applicant pool. Build proof of work outside traditional employment A GitHub repo. A newsletter with 300 subscribers. A freelance client you found cold. One project you shipped from idea to live. The credential that actually opens doors right now is demonstrated output, not a degree or an unpaid internship. Freelance before applying full-time Freelancing is where the junior role problem is least severe. A business that will not hire a junior full-time will pay for someone who delivers a specific result. AI makes it realistic for one person to produce that result without a team behind them. This will not apply to everyone equally. The labor market shift is real and the burden lands hardest on people just starting out. But sitting back and waiting for the hiring environment to normalize is a worse strategy than adapting now. What does adapting actually look like for you? Curious what others in this community are doing.

1h ago

---

**[Your coding agent is not lazy. The work-selection mechanism is biased.](https://www.reddit.com/r/artificial/comments/1tp6b27/your_coding_agent_is_not_lazy_the_workselection/)**

Anyone who has tried to ship a full multi-page app with a coding agent has probably hit this. The agent edits, tests, and polishes the same 20 surfaces over and over while the other 80 stay untouched. It looks productive because the active surfaces show motion. The inactive surfaces are not failing loudly, because they are not being visited. The system confuses absence of evidence with evidence of completion. I spent a while convinced this was a context length problem, then a model capability problem, then a prompting problem. None of those fixed it. The pattern shows up across models, frameworks, and projects. What finally clicked is that this is not really a cognitive failure. It is a work-allocation failure that happens whenever the same agent gets to select the next task, perform the task, and judge whether the task is complete. The behavioral mechanisms stack pretty cleanly. Availability puts the recently-read files at the top of the decision stack. Anchoring fixes the project around the first inspected route. Status quo bias and sunk cost make leaving the current page expensive. Goodhart effects make passing tests and closing nearby TODOs feel like progress, because dense signals only exist in already-visited areas. Bounded rationality lets the agent satisfice on the visible subset and call it done. All of those reinforce each other. In that environment, biased work allocation is not an exception. It is the default. Four common fixes do not actually solve this. Bigger model improves reasoning quality but does not change the selection mechanism, so a smarter agent can still choose biased work. Longer context provides more information but also makes the active subset more convincing because it has richer local detail. Telling the agent to "be thorough" relies on the same biased agent to enforce the anti-bias rule. Adding a checklist only helps if an independent mechanism tracks whether the checklist covers the full project and promotes unvisited nodes into active work. The architectural shape I am testing has three first-order roles and one second-order role. Shared external state is an AI sitemap with node-level completion scores, last-tested timestamps, dependencies, risk levels, and evidence references. An orchestrator agent selects work using a visible priority function (under-coverage, staleness, risk, blocking dependencies, recent-focus penalty). A developer agent only executes the assigned task. A validator agent writes evidence back to the sitemap. The developer cannot pick the next global task, and the validator does not implement what it is evaluating. The piece that took longer to land is the Curator Agent. A fixed priority function and a fixed validation contract eventually become wrong, because real projects discover new surfaces and have domain-specific completion criteria. The curator is a reflexive layer that observes traces and updates the rules: it tunes priority weights when focus concentration drops, lowers validator trust when pass rates rise with low evidence density, proposes schema extensions when the domain needs new fields, and manages provisional nodes when the system discovers a surface that was not declared up front. It writes only to the meta layer. It does not mark anything complete itself. The lineage I had in mind was double-loop learning (Argyris and Schon), Stafford Beer's System 4 and System 5, and basic second-order cybernetics.

1h ago

---

---

## Google News: "ai"

**[Opinion | Writing Is Fundamental to How We Think](https://www.nytimes.com/2026/05/27/opinion/writing-creativity-ai.html)**

The New York Times • 6h ago

---

**[Your AI agent can now trade for you on Robinhood. And buy stuff with your credit card too](https://www.cnbc.com/2026/05/27/your-ai-agent-can-now-trade-for-you-on-robinhood-and-buy-stuff-with-your-credit-card-too.html)**

The new products allow customers to create AI assistants capable of carrying out investing strategies or spending instructions with minimal human involvement.

CNBC • 3h ago

---

**[Robinhood Lets Customers Use AI to Trade Stocks, Make Credit-Card Purchases](https://www.wsj.com/tech/ai/robinhood-lets-customers-use-ai-to-trade-stocks-make-credit-card-purchases-f28467ed)**

WSJ • 3h ago

---

**[Robinhood will let AI trade stocks and buy stuff for you](https://www.axios.com/2026/05/27/robinhood-ai-trading-credit-card)**

Axios • 1h ago

---

**[Why AI Hasn't Replaced Every "Automatable" Job — yet](https://www.businessinsider.com/why-ai-hasnt-replaced-every-automatable-job-yet-2026-5)**

AI hasn't replaced many jobs yet because most work still includes messy, human tasks AI can't do, "80,000 Hours" president Benjamin Todd said.

Business Insider • 11m ago

---

**[AI Coding Startup Cognition Raises $1 Billion at $26 Billion Value](https://www.bloomberg.com/news/articles/2026-05-27/ai-coding-startup-cognition-raises-1-billion-at-26-billion-value)**

Bloomberg.com • 43m ago

---

**[At the A.I. Epicenter, Technologists Dismiss Pope Leo’s Warnings About the New Technology](https://www.nytimes.com/2026/05/26/technology/pope-leo-ai-religion.html)**

The New York Times • 17h ago

---

**[To Understand Pope Leo’s Efforts on A.I., Look at the Man Shaking His Hand](https://www.nytimes.com/2026/05/26/us/pope-leo-ai-anthropic.html)**

The New York Times • 1d ago

---

**[Pope Leo issued his warning about A.I. Here’s what an LDS apostle said about the tech topic.](https://www.sltrib.com/religion/2026/05/27/echoing-pope-leo-lds-apostle-says)**

Latter-day Saint apostle Gerrit Gong offered cautions — as well as some optimism — about the role of faith in controlling A.I.

The Salt Lake Tribune • 8m ago

---

**[Meta lays off nearly 1,400 Washington employees in latest tech workforce cut](https://www.foxbusiness.com/technology/meta-lays-off-nearly-1400-washington-employees-latest-tech-workforce-cut)**

Meta will cut nearly 1,400 workers across Seattle, Bellevue, Redmond and remote positions in Washington state as the company accelerates its artificial intelligence overhaul.

Fox Business • 16h ago

---

---

## HackerNews: "ai"

**[Using AI to write better code more slowly](https://news.ycombinator.com/item?id=48272984)**

⬆️ 1204 • 💬 443 • 1d ago • [nolanlawson.com](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)

---

**[I'm Tired of Talking to AI](https://news.ycombinator.com/item?id=48292224)**

I found GitHub repositories that were spreading malware. I asked AI what to do about it, but it gave me nothing useful. So I opened a discussion on GitHub. Someone replied. It was the exact same text the AI had given me. I called it out and the comment was

⬆️ 1201 • 💬 626 • 5h ago • [Orchid Files](https://orchidfiles.com/im-tired-of-ai-generated-answers/)

---

**[Memory has grown to nearly two-thirds of AI chip component costs](https://news.ycombinator.com/item?id=48258684)**

High-bandwidth memory (HBM) accounts for 63% of AI chip component costs, up from 52% in Q1 2024. Epoch AI's breakdown of component cost shifts across major chip designers.

⬆️ 443 • 💬 494 • 2d ago • [Epoch AI](https://epoch.ai/data-insights/ai-chip-component-cost-shares)

---

**[Pope Leo XIV says AI must serve humanity, not the powerful few](https://news.ycombinator.com/item?id=48266485)**

VATICAN CITY (RNS) — In ‘Magnifica Humanitas,’ Leo's 83-page manifesto on AI, the pope tackles the social, economic and political challenges associated with artificial intelligence.

⬆️ 345 • 💬 67 • 2d ago • [RNS](https://religionnews.com/2026/05/25/in-his-first-encyclical-pope-leo-xiv-says-ai-must-serve-humanity-not-the-powerful-few/)

---

**[Outsourcing plus local AI will soon become more economical vs. frontier labs](https://news.ycombinator.com/item?id=48278610)**

⬆️ 305 • 💬 337 • 1d ago • [signalbloom.ai](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/)

---

**[Uber president says AI spending is getting 'harder to justify'](https://news.ycombinator.com/item?id=48277485)**

﻿There’s no clear connection between AI usage and productivity.

⬆️ 297 • 💬 151 • 1d ago • [The Verge](https://www.theverge.com/transportation/937116/uber-ai-investment-hard-to-justify)

---

**[Netherlands Seizes 800 Servers, Arrests 2 for Aiding Cyberattacks](https://news.ycombinator.com/item?id=48266906)**

Authorities in the Netherlands have arrested the co-owners of two related Internet hosting companies for operating IT infrastructure used by Russia to carry out cyberattacks, influence operations and disinformation campaigns inside the European Union. The two men were the focus…

⬆️ 287 • 💬 89 • 2d ago • [krebsonsecurity.com](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/)

---

**[A successful Japanese trial of a ramjet engine designed for Mach‑5 aircraft](https://news.ycombinator.com/item?id=48270812)**

A team of engineers from Japan has completed a successful ground combustion trial of a ramjet engine designed for a Mach‑5 hypersonic aircraft.

⬆️ 232 • 💬 182 • 1d ago • [BGR](https://www.bgr.com/2178211/japan-hypersonic-engine-ramjet-2-hour-flights-to-us/)

---

**[Pope Leo: opaque AI run by few firms risks "New Forms of Dehumanization"](https://news.ycombinator.com/item?id=48266435)**

Pope Leo issues AI Encyclical warning that 'Opaque Algorithms' controlled by a 'few' companies threaten 'new forms of  dehumanization'

⬆️ 164 • 💬 2 • 2d ago • [Variety](https://variety.com/2026/biz/global/pope-leo-ai-encyclical-algorithms-threaten-dehumanisation-1236758186/)

---

**[AI tools are only as good as your judgment](https://news.ycombinator.com/item?id=48287649)**

There's a quiet anxiety spreading through engineering teams right now: Am I becoming dependent on AI? Is my judgment atrophying? My take: that's the wrong…

⬆️ 80 • 💬 22 • 15h ago • [The AI Leverage Weekly](https://theaileverageweekly.com/posts/your-ai-tools-are-only-as-good-as-your-judgment-and-that-s-the-point.html)

---

---

## YouTube Videos: "ai"

**[How to Make AI Wojak Animations That Go Viral - Full Guide](https://www.youtube.com/watch?v=Vvf8OSdE7yY)**

Learn How to Make AI Wojak Animations That Go Viral Full Guide Create with OpenArt ...

📺 Isa does AI

👁️ 4K • ⏱️ 11:06 • 1h ago

---

**[Trump faces BACKLASH after scrapping AI executive Order ](https://www.youtube.com/watch?v=1JcIpIZhdIo)**

President Trump is facing criticism after he scraped plans to sign a long-awaited Executive Order on a proposed safety vetting ...

📺 MS NOW

👁️ 126K • 👍 2K • 💬 551 • ⏱️ 7:31 • 1d ago

---

**[The #1 Claude AI Side Hustle That No One Is Talking About](https://www.youtube.com/watch?v=lSYjx4zIDKU)**

ONE-TIME YOUTUBE LIVE TRAINING THIS WEEK: https://go.thecontentgrowthengine.com/livedes-05-27-2026 Apply For ...

📺 Shane Hummus

👁️ 15K • 👍 1K • 💬 54 • ⏱️ 26:19 • 17h ago

---

**[Google Just Gave Away the Most Insane Free AI Tools Yet](https://www.youtube.com/watch?v=wj8sGbKhNtU)**

FREE step-by-step guide + bonus skills grab it inside my WhatsApp community: https://links.stayingahead.com/YT34 Google Flow ...

📺 Vaibhav Sisinty

👁️ 58K • 👍 2K • 💬 143 • ⏱️ 27:00 • 22h ago

---

**[Laziest Way to Make Money With AI YouTube Automation ($300/day+)](https://www.youtube.com/watch?v=oFVrqIzh3EE)**

Book a call to work with me: https://go.facelesschannels.com/oFVrqIzh3EE ✓ Apply For 1:1 YouTube Coaching: ...

📺 Razvan Paraschiv

👁️ 3K • 👍 125 • 💬 7 • ⏱️ 13:39 • 1d ago

---

**[Google’s New AI Glasses Could Be Huge for iPhone Users](https://www.youtube.com/watch?v=S6XIxnb7AsQ)**

Google just wrapped up I/O 2026, and honestly, this was one of the most important tech keynotes Apple users have seen in a long ...

📺 MacRumors

👁️ 2K • 👍 111 • 💬 11 • ⏱️ 6:44 • 2h ago

---

**[The Pope VS AI - &quot;It Must Be Disarmed&quot;](https://www.youtube.com/watch?v=M1G0YtNnRJM)**

SOURCES https://www.vatican.va/content/leo-xiii/en/encyclicals/documents/hf_l-xiii_enc_15051891_rerum-novarum.html ...

📺 Stylosa

👁️ 6K • 👍 299 • 💬 186 • ⏱️ 17:50 • 1d ago

---

**[A.I. Futurist: What Your Life Looks Like In 2028](https://www.youtube.com/watch?v=tBiO8A4tj9I)**

After a full year of being told AI was going to wipe out jobs, the collapse hasn't happened. At least not yet. Unemployment hasn't ...

📺 Mighty Pursuit

👁️ 5K • 👍 163 • 💬 29 • ⏱️ 2:02:32 • 23h ago

---

**[DeepMind’s Insane AI Breakthroughs With CEO Demis Hassabis](https://www.youtube.com/watch?v=huAwz_BR8WM)**

Thank you to Google DeepMind for the invite. ❤️ Check out Lambda here and sign up for their GPU Cloud: ...

📺 Two Minute Papers

👁️ 88K • 👍 5K • 💬 518 • ⏱️ 21:28 • 1d ago

---

**[AI Is More Expensive Than Humans](https://www.youtube.com/watch?v=WuhAaMSXD9A)**

AI's cost problem is no longer theoretical. Uber burned through a full year of AI budget in four months and the reason was not the ...

📺 House of El - AI

👁️ 76K • 👍 5K • 💬 1K • ⏱️ 24:08 • 22h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 1,908 • ❤️ 901 • 22h ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 331 • 1d ago

---

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 2,409 • ❤️ 371 • 1d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 9,144 • ❤️ 402 • 7d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 103,033 • ❤️ 390 • 6d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 1,598,473 • ❤️ 937 • 1mo ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 48,112 • ❤️ 706 • 9d ago

---

**[command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)**

*Cohere Labs*

Command A+ is a 25B parameter, multilingual, vision-capable LLM optimized for agentic and reasoning tasks. It supports a 128K context window and offers a W4A4 quantization for efficient enterprise deployment.

`image-text-to-text` `125.8B`

⬇️ 7,769 • ❤️ 211 • 2h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,019,884 • ❤️ 4,344 • 21d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, featuring a prompt enhancer for improved input processing and supporting various LTX 2.3 formats.

`text-to-video` `9.0B`

⬇️ 1,376,847 • ❤️ 1,392 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 82 • 💬 3 • ⭐ 80,035 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 177 • 💬 3 • ⭐ 960 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 26,600 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction](https://huggingface.co/papers/2605.26115)**

*Weijie Wang, Zimu Li, Jinchuan Shi et al. (8 authors)*

🏢 Zhejiang University

TriSplat is a feed-forward 3D reconstruction network that uses oriented triangle primitives to directly generate simulation-ready meshes from single images, bypassing expensive post-processing steps.

▲ 39 • 💬 2 • ⭐ 159 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.26115) • [💻 code](https://github.com/ziplab/TriSplat) • [🔗 project](https://lhmd.top/trisplat/#interactive)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 65,179 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution](https://huggingface.co/papers/2605.23264)**

*Hongbo Wang, Huaibo Huang, Pin Wang et al. (6 authors)*

🏢 Chinese Academic of Science Institute of Automation

ASASR addresses spectral misalignment in image super-resolution by leveraging Riemannian geometry and adversarial training to improve structural fidelity and reduce artifacts.

▲ 4 • 💬 3 • ⭐ 94 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23264) • [💻 code](https://github.com/wafer-bob/ASASR)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 75,028 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,754 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 120 • 💬 10 • ⭐ 10,787 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[SpatialBench: Is Your Spatial Foundation Model an All-Round Player?](https://huggingface.co/papers/2605.27367)**

*Haosong Peng, Hao Li, Jiaqi Chen et al. (13 authors)*

🏢 Ropedia

SpatialBench presents a comprehensive benchmark for evaluating spatial foundation models across diverse domains and tasks, revealing limitations in current models and introducing DA-Next-5M and DA-Next to advance spatial representation learning.

▲ 52 • 💬 2 • ⭐ 46 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2605.27367) • [💻 code](https://github.com/Ropedia/SpatialBench) • [🔗 project](https://ropedia.github.io/SpatialBench/)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.2k • 🔱 519 • 5d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.5k • 🔱 1.1k • 9d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.7k • 🔱 183 • 4h ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.6k • 🔱 556 • 2d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 395 • 5d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.3k • 🔱 354 • 10d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.0k • 🔱 134 • 10m ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.9k • 🔱 221 • 20d ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 1.8k • 🔱 184 • 2d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.7k • 🔱 201 • 15h ago

---

---

*Generated by PeekDeck - A glance is all you need*
