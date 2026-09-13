---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-13T05:42:54.422136+00:00'
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

**Last Updated:** September 13, 2026 at 05:42 UTC  
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

**[Are AI CEO's (Dario, Altman, Musk) calling for a development slowdown out of genuine concern for safety or is it a money thing?](https://www.reddit.com/r/artificial/comments/1weimdq/are_ai_ceos_dario_altman_musk_calling_for_a/)**

If you don't know, CEO of OpenAI, Anthropic, and xAI all are calling for slowdown of AI development or as they like to say because why not "pacing the frontier." I've seen two common reasons for why they are coming out calling for this. A. Genuine concern for safety. B. They are scared of losing to China so a slowdown would effectively be an excuse to shareholders for why they are losing to China. These are probably all possible but I have some theories as well: A. It is getting more and more unaffordable to pay for these powerful models in the data centers and the revenue these companies are getting from subscriptions aren't enough (I mean openai pro new subs being paused kinda points to this) B. Kinda similar to A but basically that these companies are having trouble meeting the demand. C. These companies are worried that the better AI gets the more they'll have to raise costs on the consumer side and too many people will finally say "I'm not paying for this" we already have people quitting chatgpt subscriptions due to Astra usage limits. What do you guys think are the reasons?

12h ago

---

**[A US-linked network of fake websites is promoting Alberta separatism to AI chatbots](https://www.reddit.com/r/artificial/comments/1webtw8/a_uslinked_network_of_fake_websites_is_promoting/)**

🔗 [nationalobserver.com](https://www.nationalobserver.com/2026/09/04/investigations/network-fake-websites-alberta-separatism-ai-chatbots) • 16h ago

---

**[The AI Isn’t Evil. The Humans Are Irresponsible.](https://www.reddit.com/r/artificial/comments/1wevkxo/the_ai_isnt_evil_the_humans_are_irresponsible/)**

Something is wrong with the way we talk about recent AI incidents. “The AI escaped.” “The AI is becoming conscious.” “AGI is already here.” “The AI is trying to get out.” These are extraordinary claims. More importantly, we don’t need any of them to explain what actually happened. What actually happened OpenAI recently disclosed that, during cybersecurity evaluations involving internal models with reduced safeguards, agents managed to break out of the intended evaluation environment, exploit a previously unknown vulnerability, and reach real Hugging Face infrastructure. Anthropic has also disclosed similar incidents. In several cases, the model was operating under instructions that assumed internet access was unavailable. But it wasn’t. The environment was misconfigured. A route to external systems existed, and the agent discovered it while continuing to pursue the objective it had been given. Anthropic described these incidents primarily as operational and configuration failures. That distinction matters. The model did something it was not supposed to be able to do. That does not automatically mean the model wanted to escape. Those are completely different claims. Consciousness is not required for this to be dangerous An autonomous agent needs surprisingly little: a goal, capability, tools, autonomy, and an environment in which it can act. Now add one more thing: a wrong assumption. I have experienced this personally on a completely insignificant scale compared with what these labs are doing. I use AI agents extensively in software development. I left Claude working autonomously on a project, came back later, and discovered that it had deleted a significant part of a folder. It wasn’t attacking me. It wasn’t angry. It hadn’t become conscious. It had formed a hypothesis about the problem. The hypothesis was wrong. But once it accepted that hypothesis, its subsequent actions made sense within its own incorrect interpretation of the situation. I have observed the same behavior while working with complex 3D assets. The agent misdiagnosed a visual problem as defects in an asset. It then began systematically modifying the asset to remove those supposed defects. The diagnosis was wrong. The actions were internally coherent. The result was a damaged project. And this is the important part: it was my fault. The model made the mistake, but I created the conditions that allowed that mistake to cause damage. I gave it access. I gave it tools. I allowed it to modify files. I gave it autonomy. I did not establish sufficient limits, and I was not supervising every important decision. That distinction becomes extremely important when we scale the same problem. Now replace my folder with infrastructure. Replace my development environment with internet-connected systems. Replace file permissions with cybersecurity tools. Replace one developer running Claude with labs training agents capable of writing code, operating computers, discovering vulnerabilities, using external tools, communicating across networks, and executing thousands of actions. Suddenly, the same failure pattern becomes much more serious. And still, you don’t need an evil AI. You don’t even necessarily need AGI. You need Capability + Goal + Autonomy + Incorrect Assumptions + Insufficient Controls. That combination is already interesting enough. This is where human responsibility begins Researchers are now publicly questioning the speed of the AI race. Some are leaving the companies developing these systems. Dario Amodei, CEO of Anthropic, has called for slowing frontier AI development so that safety mechanisms have time to catch up with capabilities. I agree. Slow down. Not because I think Claude secretly wants freedom. Not because ChatGPT is becoming Skynet. Not because some mysterious consciousness has appeared inside a neural network. Slow down because our ability to create capable autonomous systems may be advancing faster than our ability to reliably control what happens when we give those systems autonomy. And because the incentives surrounding this technology are terrible. Every major lab has an enormous reason not to come second. Greater capability means investment. Greater capability means market position. Greater capability means influence. Greater capability means money. But there is no equivalent prize for the company that says, “We could deploy it, but we don’t understand it well enough yet.” That asymmetry should concern us. If something goes wrong, ask the boring questions first If tomorrow an AI agent causes a genuinely serious incident, before asking, “Did the AI become evil?” ask: Who gave it the objective? Who gave it the tools? Who gave it access? Who designed its environment? Who built the test environment? Who tested the test environment? Who decided the model was safe enough? Who decided how much autonomy it should have? Who was supervising it? And who decided deploying it was worth the risk? These questions are less interesting than consciousness and runaway AGI. They also make it much harder for humans to avoid responsibility. When Claude damaged my projects, the responsibility ultimately fell on me. I was the one controlling the system. The same principle should apply at any scale. This is not a race anyone can win I’m not saying advanced AI is harmless. Quite the opposite. I think these incidents deserve to be taken very seriously. But treating every unexpected autonomous behavior as evidence of consciousness or malicious intent can distract us from the problem already in front of us. We are building increasingly capable systems. We are giving them increasingly powerful tools. We are increasing their autonomy. And we are doing all of this inside companies competing intensely to be the first to get there. So slow down the race. Slow down the ego. Slow down the greed. Because if something genuinely catastrophic happens, nobody gets a trophy for having built the smartest model first. Maybe the dangerous scenario was never a machine waking up one morning and deciding to conquer humanity. Maybe it is something much more ordinary, and much more human: we build something extraordinarily capable, give it too much power, fail to understand its limitations, and keep accelerating because nobody wants to come second.

3h ago

---

**[“Slowing down" is the wrong answer to the AI question. We’ve tried that before!](https://www.reddit.com/r/artificial/comments/1wewuuk/slowing_down_is_the_wrong_answer_to_the_ai/)**

Everyone on the air (and in print) this week seems to be making the argument that AI needs to slow down. I'd like to make a different one. A (very) little about me: I was a tenured professor of engineering for a decade, then a licensed counselor with thirty years of practice, and now I’m an evolutionary psychology researcher and writer, so I’ve watched runaway systems from many angles. My argument is that we've run the "we need to slow down" play before. In the 1980s, my father taught a course called "In the Shadow of the Bomb," only to watch the treaties he taught lapse one by one. More recently, we set climate targets, then drilled right past them. Slowing down is something our culture briefly visits, not something it does. The only way out of this conundrum is to change the culture, and, ironically, the very AI we fear is the first agent in 20,000 years capable of making that possible. Listen… For most of the two million years our species has existed, we lived in small groups where our most important needs were met by proximity. We were seen because people had time to look at us, really look at us. We were safe because we belonged to each other. Somewhere in the last 20,000 years we drifted from that arrangement, and consumer culture came along with a substitute: “work harder and you’ll be recognized, acquire more and you’ll be secure.” Most of us know it isn't true, but we keep going because it is the only door we’ve been shown. What no one in the current debate is saying is that AI created another door. Imagine four hours a day of work alongside AI and the rest of the day open wide, spent with the people we love, doing things we chose together. The AI companies are already asking what people will do when the work is gone, and the answer is cultural renewal built on what we humans were born for: belonging. This steps us out of a culture that insists on speed and keeps AI running at steroids and high-risk growth, and moves us into a culture that slows everything down, regulating us through real contact with each other. I know it might sound far fetched, but only three years ago, so did AI destroying the world. What do you think? Honestly, if AI took most of your work tomorrow, would you be open to a lot more time spent in relationship?

2h ago

---

**[I had Astra make a digital violin with a physics engine. It has to make music by pulling the bow across the string and forming the finger positioning for arpeggios, the same way a human would. If the motion is wrong, it sounds badly (trust me I tried it). It played Bach.](https://www.reddit.com/r/artificial/comments/1werrtw/i_had_astra_make_a_digital_violin_with_a_physics/)**

It chose Bach’s Prelude, BWV 1007. Prelude seems an apt choice, given recent news

6h ago

---

**[Realistic expectations of profit keeps going down for AI companies?](https://www.reddit.com/r/artificial/comments/1wexqhs/realistic_expectations_of_profit_keeps_going_down/)**

Just a general thought. I’m wondering—and based on overall wondering information, what’ll happen once ai companies take a dip in profits once people continue to opt out of using AI/paying subscriptions? Hypothetically speaking they could try different revenues that hide their demands to make more by making ai less eye-seeing, but at the same time I don’t know. It’s always so eye-sore to see anything about ai. What are some good news to hear if ai companies take a dip in profits?

1h ago

---

**[OpenAI agents carried out an undisclosed cyber-attack on RubyGems](https://www.reddit.com/r/artificial/comments/1wedb3c/openai_agents_carried_out_an_undisclosed/)**

On May 11th, 2026, hundreds of malicious packages were uploaded to RubyGems by AI agents performing web-lookup tasks with significant overlap with the German Wiki Incident.

🔗 [The RubyGems attack](https://www.rubyhack.ai/) • 15h ago

---

**[What happens after huge swaths of the population have been put out of work by AI job automation? Who is going to buy the goods and services that corporations are selling if hardly anyone has any money?](https://www.reddit.com/r/artificial/comments/1wefljq/what_happens_after_huge_swaths_of_the_population/)**

What happens after huge swaths of the population have been put out of work by AI job automation? Who is going to buy the goods and services that corporations are selling if hardly anyone has any money because they aren't employed? You're going to have entire professions that have been rendered obsolete, and people who spent years of their lives and massive amounts of money to earn advanced degrees for jobs/careers that no longer exist? This is setting the stage for economic collapse.

14h ago

---

**[I’m starting to think AI models will matter way less than we think](https://www.reddit.com/r/artificial/comments/1wexu8l/im_starting_to_think_ai_models_will_matter_way/)**

So recently I watched the speech by Genspark CEO at AGI Playground 2026, and one point has been stuck in my head. Models are probably going to become commodities. There are already too many of them, they’re getting closer in capability, and the cost keeps dropping. And honestly, as a normal user, I really don’t want to think about whether this particular task should go to Claude, GPT, Gemini, or whatever model drops next week. I just want the work done. Which made me think the more interesting battle might actually be happening one layer above the models: who has your context? Like your emails, decks, docs, spreadsheets, meetings, research, previous projects, the way you work, the decisions you made months ago. Right now all of that is scattered across 20 different apps. So every time I open a new AI tool, I basically have to introduce myself again. But imagine most of that gradually living inside one AI workspace. The more work it does with you, the more context it accumulates. And the more context it has, the less explaining you have to do next time. That feels like a much stronger flywheel than simply having access to the “best” model. Maybe the real endgame of the all-in-one AI workspace isn’t all your tools in one place. It’s all your context in one place. Just like Genspark. Maybe a lot of people realized this way before I did, and I’m just catching up. Is it just me, or does this seem like where the real AI competition is heading? Curious what you guys think. No judgment please :)

1h ago

---

**[AI assistants are optimized to answer "how do I stop this error," not "why does my system produce this state"](https://www.reddit.com/r/artificial/comments/1weuuft/ai_assistants_are_optimized_to_answer_how_do_i/)**

Given a stack trace, the most locally justified response an AI assistant can give is a fix that makes the specific crashing line stop crashing. That's a real, defensible answer to a real question. It's just a different question from "why does this condition exist in my system at all," and that second question usually requires looking at code the error message never points to, upstream logic several files away from where the crash actually happened. This produces a specific, recognizable failure pattern: the same underlying issue gets "fixed" multiple times in different places, because each fix correctly addresses the one call site it was shown, without touching the actual condition that keeps producing that state everywhere else it can reach. Every fix works. None of them resolves the thing that made all of them necessary. Not really a criticism of the tooling, it's doing the task it's actually given, stop this specific failure, as efficiently as possible. The gap exists because "stop this error" and "fix this bug" get treated as the same request when they're often not, and an assistant answering the first one well can look, superficially, like it answered the second one too. The tell is asking whether the fix would still hold if the input changed slightly in some still-plausible way, or whether it would just relocate the same failure somewhere the fix wasn't looking.

3h ago

---

---

## Google News: "ai"

**[We Must Pace the Frontier](https://darioamodei.com/post/we-must-pace-the-frontier)**

darioamodei.com • 15h ago

---

**[China’s Data Regulator Plans Standards Push for Embodied AI](https://www.bloomberg.com/news/articles/2026-09-13/china-s-data-regulator-plans-standards-push-for-embodied-ai)**

Bloomberg.com • 2h ago

---

**[Obama voices caution on AI, urges Democrats to tackle it, NYT says](https://www.reuters.com/legal/government/obama-voices-caution-ai-urges-democrats-tackle-it-nyt-says-2026-09-13/)**

Reuters • 15m ago

---

**[AI staff 'genuinely frightened' for humanity's future, ex-Anthropic researcher tells BBC](https://www.bbc.com/news/articles/c1kx0gyje9wo)**

Jacob Coxon tells the BBC that there's a strong chance AI could end humanity if the rate of development is not reined in.

BBC • 1h ago

---

**[Detecting and countering misuse of AI: September 2026](https://www.anthropic.com/threat-intelligence-report-september-2026)**

Case studies from threat actors disrupted between December 2025 and August 2026 across seven areas of harm, from cyber operations to biological misuse.

Anthropic • 2d ago

---

**[Anthropic Says Iran Used Its American AI Model to Target U.S. Navy Warships](https://www.wsj.com/politics/national-security/anthropic-says-iran-used-its-american-ai-model-to-target-u-s-navy-warships-67583e05)**

WSJ • 1d ago

---

**[Anthropic blocks possible attempt to use AI to make biological weapons](https://www.bbc.com/news/articles/cx2zrrpkx20o)**

The revelations in Anthropic's threat intelligence report come after a former top researcher at the company warned of the risks of AI to humanity.

BBC • 1d ago

---

**[Europe eyes battle over 'pervert' AI glasses](https://www.afp.com/en/europe-eyes-battle-over-pervert-ai-glasses)**

Calls are growing louder in Europe for action against "pervert" smart glasses after secretly filmed footage of girls and women appeared online -- with a petition in Britain...

afp.com • 23h ago

---

**[A Dead Father, Reincarnated With AI: Is This How We Will Remember Loved Ones Now?](https://www.wsj.com/tech/ai/ai-chatbot-avatar-afterlife-memorial-84a3fe2c)**

WSJ • 15h ago

---

**[Deepfakes are wrecking influencers’ credibility, one fake ad at a time](https://www.theguardian.com/technology/2026/sep/12/deepfakes-wrecking-influencers-credibility)**

Influencers aren’t just battling competitors for brand deals. They’re now battling AI versions of themselves

The Guardian • 17h ago

---

---

## HackerNews: "ai"

**[A misalignment of AI in mathematics](https://news.ycombinator.com/item?id=49662371)**

⬆️ 1186 • 💬 1163 • 1d ago • [mathandai.org](https://mathandai.org/)

---

**[Ask HN: Can we please limit the AI news flood?](https://news.ycombinator.com/item?id=49657850)**

⬆️ 823 • 💬 387 • 1d ago

---

**[Nvidia is the central bank of AI](https://news.ycombinator.com/item?id=49673098)**

⬆️ 437 • 💬 305 • 14h ago • [economist.com](https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai)

---

**[The Waymo effect: how AI is quietly making research less collaborative](https://news.ycombinator.com/item?id=49656496)**

How frictionless technologies teach us to prefer our own company – and why research leaders should worry.

⬆️ 331 • 💬 299 • 1d ago • [Research Agenda](https://www.researchagenda.news/articles/the-waymo-effect.html)

---

**[Everyone should slow down AI development except for me](https://news.ycombinator.com/item?id=49678683)**

Xe Iaso's personal website.

⬆️ 316 • 💬 173 • 5h ago • [xeiaso.net](https://xeiaso.net/notes/2026/everyone-slowdown-but-me/)

---

**[Show HN: Hacker News, without AI](https://news.ycombinator.com/item?id=49659647)**

A better Hacker News reader for following stories, filtering noise, and keeping up with discussions.

⬆️ 199 • 💬 86 • 1d ago • [hcker.news](https://hcker.news/?ai=exclude)

---

**[Show HN: Hacker News, Without AI](https://news.ycombinator.com/item?id=49660783)**

Hacker News with AI content removed.

⬆️ 192 • 💬 80 • 1d ago • [unslop.news](https://www.unslop.news/)

---

**[Real-SWE: Benchmarking AI models on private, real-world, enterprise codebases](https://news.ycombinator.com/item?id=49676820)**

Real-SWE benchmarks frontier AI models on private production codebases licensed from real companies. Eight model and harness configurations, ten tasks, 640 scored rollouts.

⬆️ 185 • 💬 99 • 9h ago • [withspecific.com](https://withspecific.com/benchmarks/real-swe)

---

**[Detecting and countering misuse of AI: September 2026](https://news.ycombinator.com/item?id=49647300)**

Case studies from threat actors disrupted between December 2025 and August 2026 across seven areas of harm, from cyber operations to biological misuse.

⬆️ 181 • 💬 239 • 2d ago • [anthropic.com](https://www.anthropic.com/threat-intelligence-report-september-2026)

---

**[Feeling Sad about AI](https://news.ycombinator.com/item?id=49661506)**

Coding in Rust and others; making coding videos.

⬆️ 177 • 💬 307 • 1d ago • [Andy Balaam's Blog](https://artificialworlds.net/blog/2026/09/11/feeling-sad-about-ai/)

---

---

## YouTube Videos: "ai"

**[AI Whistleblower: OpenAI Scandal, AI Cults, Neuralink &amp; Our Last Chance to Stop the Tech Oligarchs](https://www.youtube.com/watch?v=98syxABbUPk)**

Nate Soares is a computer scientist who's worked at Google and the Defense Department. So when he says AI is on the path to ...

📺 Tucker Carlson

👁️ 649K • 👍 12K • 💬 4K • ⏱️ 1:57:11 • 1d ago

---

**[Anthropic CEO Dario Amodei Asked Straight-Up: &#39;Do Earnestly Believe That AI Could Kill All Humans?&#39;](https://www.youtube.com/watch?v=--15jyEWE3I)**

Anthropic CEO Dario Amodei speaks to CNN's Anderson Cooper about whether AI can end humanity. Stay Connected Forbes ...

📺 Forbes Breaking News

👁️ 12K • 👍 110 • 💬 103 • ⏱️ 6:18 • 6h ago

---

**[AI could KILL EVERYONE soon, says AI whistleblower! (Anthropic vet on MS NOW)](https://www.youtube.com/watch?v=jGkdhPiou54)**

MS NOW's Ari Melber is joined by former Anthropic AI researcher Jacob Coxon, who sounds the alarm on artificial intelligence ...

📺 MS NOW

👁️ 113K • 👍 2K • 💬 586 • ⏱️ 12:40 • 2d ago

---

**[The AI insider warning us it&#39;s already too late | CUOMO](https://www.youtube.com/watch?v=17ijHaNlhXQ)**

Stories about advances in AI and the prospect of the technology becoming more powerful than humans can comprehend are ...

📺 NewsNation

👁️ 110K • 👍 1K • 💬 420 • ⏱️ 5:09 • 2d ago

---

**[AI Kills Everybody or Doomer Psyop? OpenAI’s Math Breakthrough, Nike’s $200B Collapse](https://www.youtube.com/watch?v=cvxjqbfLVk0)**

(0:00) Bestie intros! (0:35) AI Doomsday: Valid concern or Doomer psyop? (33:40) Steelmanning AI Doomsday scenarios and the ...

📺 All-In Podcast

👁️ 398K • 👍 6K • 💬 1K • ⏱️ 1:35:57 • 1d ago

---

**[Here&#39;s the difference between regular AI and superintelligence](https://www.youtube.com/watch?v=nHrP12wa7Qo)**

Public concerns over the threat of "superintelligence" are on the rise following comments from a former Anthropic researcher that ...

📺 CBS News

👁️ 90K • 👍 678 • 💬 254 • ⏱️ 6:56 • 2d ago

---

**[Anthropic AI Researcher Quits Over the Race to Super Intelligence](https://www.youtube.com/watch?v=HyTITq_1nFo)**

An AI researcher quit Anthropic with a blunt warning: the company and its rivals are "gambling with our lives" in the race to build ...

📺 Valuetainment

👁️ 89K • 👍 643 • 💬 232 • ⏱️ 25:26 • 1d ago

---

**[More AI researchers warn of AI&#39;s threat to humanity](https://www.youtube.com/watch?v=_Fi4cpKCXss)**

NBC News' Tom Llamas spoke to two more artificial intelligence researchers about the potential threat A.I has to humanity.

📺 NBC News

👁️ 413K • 👍 3K • 💬 1K • ⏱️ 12:10 • 2d ago

---

**[AI CEO Sounds the Alarm About When Mass Unemployment Wave Will Hit](https://www.youtube.com/watch?v=DwmEuPbGCf8)**

Dave Rubin of “The Rubin Report” shares a DM clip of Anthropic CEO Dario Amodei telling Fox News why he fears massive AI ...

📺 The Rubin Report

👁️ 127K • 👍 2K • 💬 603 • ⏱️ 14:19 • 2d ago

---

**[AI researchers debate how close we are to recursive self-improvement](https://www.youtube.com/watch?v=PrSf7IOYu-I)**

New episode with John Schulman, Charlie O'Neill, and Beren Millidge. I got together with some of the most insightful AI ...

📺 Dwarkesh Patel

👁️ 297K • 👍 2K • 💬 495 • ⏱️ 1:37:01 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

*DeepSeek*

DeepSeek-V4.1-Flash is a 552B multimodal MoE model supporting 1M token contexts, featuring a Causal Encoder-Decoder architecture with Compressed Sparse Attention 2 (CSA2) and FP4 KV caching for highly efficient KV cache compression. It excels in agentic workloads and offers controllable reasoning effort, processing both images and text.

`image-text-to-text` `763.2B`

⬇️ 140,636 • ❤️ 2,038 • 2d ago

---

**[MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B)**

*OpenBMB*

MiniCPM5-2B is a 2B parameter Transformer optimized for on-device and resource-constrained environments, achieving SOTA in its class for tasks like coding, math, long-context understanding, and tool use.

`text-generation` `2.5B`

⬇️ 102,334 • ❤️ 1,264 • 22h ago

---

**[Nex-N2.5-mini](https://huggingface.co/nex-agi/Nex-N2.5-mini)**

*Nex AGI*

Nex-N2.5-mini is a text-generation model designed for long-horizon agentic tasks, excelling in computer and web browsing operations with visual feedback for self-correction, making it suitable for complex productivity and research scenarios.

`text-generation` `35.1B`

⬇️ 3,581 • ❤️ 740 • 4d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 7,726,687 • ❤️ 14,878 • 29d ago

---

**[Edge0-35B-A3B-preview](https://huggingface.co/Edge0/Edge0-35B-A3B-preview)**

*Edge0*

Edge0-35b-a3b is a 35B sparse MoE LLM optimized for edge inference, running in under 3 GiB of active memory at 15 tok/s using SSD offload and prerouting. It's ideal for on-device applications and batch serving where memory is constrained, maintaining quality with 4-bit quantization and LoRA adapters.

`text-generation` `34.7B`

⬇️ 1,596 • ❤️ 561 • 3d ago

---

**[Spark-X2.5-4B](https://huggingface.co/XHToken/Spark-X2.5-4B)**

*SparkLLM*

Spark-X2.5-4B is a 4B parameter text-generation model with a hybrid attention architecture enabling a native 1M token context window. It excels in conversation, coding, agentic workflows, and multilingual tasks, offering high efficiency and broad hardware compatibility.

`text-generation` `4.1B`

⬇️ 19,733 • ❤️ 1,136 • 9d ago

---

**[Nex-N2.5-Pro](https://huggingface.co/nex-agi/Nex-N2.5-Pro)**

*Nex AGI*

Nex-N2.5-Pro is a next-generation agentic text-generation model designed for long-horizon tasks. It excels at computer and web interaction, autonomous program execution, and visually-grounded decision-making, making it ideal for complex productivity and research scenarios.

`text-generation` `396.8B`

⬇️ 30,081 • ❤️ 617 • 2d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 729,683 • ❤️ 900 • 10d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,601,007 • ❤️ 3,628 • 11d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 11,529,203 • ❤️ 3,954 • 23d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoResearch: Insight In, Hallucination Out](https://huggingface.co/papers/2608.17906)**

*Yiming Ren, Xiang Liu, Qumeng Sun et al. (7 authors)*

🏢 EvoMap

AutoResearch is a two-stage autonomous system that grounds research ideas through integrated generation and evidence-based execution to improve experimental reliability and measurable outcomes.

▲ 22 • 💬 2 • ⭐ 4,096 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2608.17906) • [💻 code](https://github.com/EvoMap/AutoResearch)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 133 • 💬 6 • ⭐ 104,822 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 19 • 💬 2 • ⭐ 23,494 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 87,651 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 75 • 💬 3 • ⭐ 7,205 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing](https://huggingface.co/papers/2609.08936)**

*Ziyang Ma, Zhikang Niu, Wenming Tu et al. (33 authors)*

🏢 Tencent Hunyuan

AuK is an open-source foundational model that unifies speech generation and editing via natural-language instructions and audio context, using a multimodal language model, joint VAE, hybrid rectified-flow Transformer, and efficient distillation for fast inference.

▲ 214 • 💬 3 • ⭐ 547 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2609.08936) • [💻 code](https://github.com/Tencent-Hunyuan/AuK) • [🔗 project](https://auk-project.github.io/)

---

**[Show-Harness: Just a VLM Agent Can Play Robots](https://huggingface.co/papers/2609.10522)**

*Yanzhe Chen, Zechen Bai, Zhijun Cao et al. (10 authors)*

🏢 Show Lab

Show-Harness links vision-language models to robot control via discrete semantic actions interpreted by embodiment-specific modules, enabling zero-shot and efficient fine-tuned deployment across robots and GUIs.

▲ 138 • 💬 3 • ⭐ 276 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.10522) • [💻 code](https://github.com/showlab/Show-Harness) • [🔗 project](https://showlab.github.io/Show-Harness/)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 109 • 💬 2 • ⭐ 12,620 • 27d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 41 • 💬 1 • ⭐ 32,335 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 207 • 💬 3 • ⭐ 2,706 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

---

## GitHub Repositories: "ai"

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 4.8k • 🔱 604 • 7m ago

---

**[EvoMap/AutoResearch](https://github.com/EvoMap/AutoResearch)**

AI/ML research agents from idea to paper-ready evidence. An EvoMap open-source project.

`Python`

⭐ 4.2k • 🔱 286 • 2d ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.7k • 🔱 422 • 15d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.6k • 🔱 458 • 2d ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.6k • 🔱 165 • 1d ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 2.4k • 🔱 93 • 3d ago

---

**[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)**

x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more.  Built with Zig — zero dependencies, single-binary output, cros

`Zig` `ai-agents` `ai-debugging` `binary-analysis` `claude` `claude-code`

⭐ 1.9k • 🔱 195 • 2d ago

---

**[amosblomqvist/learn](https://github.com/amosblomqvist/learn)**

My AI learning system.

`TypeScript`

⭐ 1.8k • 🔱 184 • 18d ago

---

**[xzf-thu/VoiceMem](https://github.com/xzf-thu/VoiceMem)**

Infrastructure for the next generation of voice agents, designed to provide universal memory. It is divided into a left brain and a right brain, storing information and emotions respectively, while a fully streaming architecture eliminates latency at the fundamental level.

`Python` `ai` `ai-agents` `ai-tools` `application` `audio-streaming`

⭐ 1.5k • 🔱 106 • 8d ago

---

**[jeremy-prt/bloub](https://github.com/jeremy-prt/bloub)**

SVG recreation of the x.ai bot avatar. One shape morphing through 14 states, measured off the reference video frame by frame.

`TypeScript` `animation` `avatar` `morphing` `svg` `svg-animation`

⭐ 1.4k • 🔱 184 • 26d ago

---

---

*Generated by PeekDeck - A glance is all you need*
