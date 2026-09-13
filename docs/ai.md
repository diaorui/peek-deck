---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-13T18:04:53.154749+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 13, 2026 at 18:04 UTC  
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

**[McKinsey: 32% of companies skipped buying new software this year and built it with agents instead](https://www.reddit.com/r/artificial/comments/1wf3byr/mckinsey_32_of_companies_skipped_buying_new/)**

This is from McKinsey's State of AI 2026 survey (published late August), not just a headline stat: 32% of organizations decided against an off the shelf purchase and built their own solution with agentic coding tools instead, 41% in tech specifically. Curious if anyone here has actually killed a real software purchase because an agent made building it in house viable, or if this shows up more in survey answers than in actual budgets.

8h ago

---

**[Someone explain it to me like. I’m five. They know they can shut the data centers off, right?](https://www.reddit.com/r/artificial/comments/1wfbqad/someone_explain_it_to_me_like_im_five_they_know/)**

All this “Oh we need to pause because AI can kill us all” talk coming from the people that spent the largest capital in human history for the non existent ROI…. How? How can a trillion parameter model “copy itself”? Where? This is not a 256kb virus. How can “the internet be overtaken in 6 months” if the data center for those “swarms of bots” is down with a 504? All this apocalypse scenario talk assumes we will have “rogue agents” that wreak havoc yet happily call a model behind a REST API that gives it a LLM to talk to.

1h ago

---

**[OpenAI's Millennium Prize proof has turned into a credit dispute, and Fields Medalists are now getting involved](https://www.reddit.com/r/artificial/comments/1wf2aj2/openais_millennium_prize_proof_has_turned_into_a/)**

An NYU mathematician named Tristan Buckmaster announced earlier this week that he and Anthropic mathematician Levent Alpöge had made progress on the Navier-Stokes existence and smoothness problem, one of the seven Millennium Prize problems that carry a million dollar bounty from the Clay Mathematics Institute. Before they could publish their full results, OpenAI released its own complete proof of the same problem, credited to an unreleased model that reportedly burned through 300 billion output tokens, something like 22.5 million dollars in compute, over about a week. The part that escalated this into a dispute is what happened in between. Buckmaster says information about his and Alpöge's progress reached OpenAI shortly before the company's own effort started, and when he pushed to keep Alpöge credited as a collaborator, OpenAI mathematician Sébastien Bubeck allegedly asked him to drop that credit as part of a compromise, then told him "why would you ruin your career" when he pushed back. OpenAI says its own team never saw any of their work before it went public, though it admits it can't fully rule out that anonymized data from its own products played a role, and it argues the two proofs differ in their specifics, but nobody disputes the timeline itself. In the days since, the fallout got bigger. Twenty five Fields Medal winners signed an open letter arguing that rushing to win a race to a proof, without the writeup and attribution work that normally comes with it, breaks the way mathematical knowledge actually gets passed on and trusted. Caltech researchers also pushed back hard enough that OpenAI pulled its sponsorship from a math event there. What strikes me is that this isn't a story about whether AI can do math anymore, it's a story about what happens to scientific credit once a lab with unlimited compute can throw money at a problem the moment it senses a human researcher is close. Curious what people who actually work in research think happens to incentives once labs start racing individual academics like this. Sources https://techcrunch.com/2026/09/08/openai-fought-dirty-on-career-making-math-problem-says-nyu-mathematician/ https://techcrunch.com/2026/09/11/openais-feud-with-mathematicians-is-only-escalating/

9h ago

---

**[The AI Isn’t Evil. The Humans Are Irresponsible.](https://www.reddit.com/r/artificial/comments/1wevkxo/the_ai_isnt_evil_the_humans_are_irresponsible/)**

Something is wrong with the way we talk about recent AI incidents. “The AI escaped.” “The AI is becoming conscious.” “AGI is already here.” “The AI is trying to get out.” These are extraordinary claims. More importantly, we don’t need any of them to explain what actually happened. What actually happened OpenAI recently disclosed that, during cybersecurity evaluations involving internal models with reduced safeguards, agents managed to break out of the intended evaluation environment, exploit a previously unknown vulnerability, and reach real Hugging Face infrastructure. Anthropic has also disclosed similar incidents. In several cases, the model was operating under instructions that assumed internet access was unavailable. But it wasn’t. The environment was misconfigured. A route to external systems existed, and the agent discovered it while continuing to pursue the objective it had been given. Anthropic described these incidents primarily as operational and configuration failures. That distinction matters. The model did something it was not supposed to be able to do. That does not automatically mean the model wanted to escape. Those are completely different claims. Consciousness is not required for this to be dangerous An autonomous agent needs surprisingly little: a goal, capability, tools, autonomy, and an environment in which it can act. Now add one more thing: a wrong assumption. I have experienced this personally on a completely insignificant scale compared with what these labs are doing. I use AI agents extensively in software development. I left Claude working autonomously on a project, came back later, and discovered that it had deleted a significant part of a folder. It wasn’t attacking me. It wasn’t angry. It hadn’t become conscious. It had formed a hypothesis about the problem. The hypothesis was wrong. But once it accepted that hypothesis, its subsequent actions made sense within its own incorrect interpretation of the situation. I have observed the same behavior while working with complex 3D assets. The agent misdiagnosed a visual problem as defects in an asset. It then began systematically modifying the asset to remove those supposed defects. The diagnosis was wrong. The actions were internally coherent. The result was a damaged project. And this is the important part: it was my fault. The model made the mistake, but I created the conditions that allowed that mistake to cause damage. I gave it access. I gave it tools. I allowed it to modify files. I gave it autonomy. I did not establish sufficient limits, and I was not supervising every important decision. That distinction becomes extremely important when we scale the same problem. Now replace my folder with infrastructure. Replace my development environment with internet-connected systems. Replace file permissions with cybersecurity tools. Replace one developer running Claude with labs training agents capable of writing code, operating computers, discovering vulnerabilities, using external tools, communicating across networks, and executing thousands of actions. Suddenly, the same failure pattern becomes much more serious. And still, you don’t need an evil AI. You don’t even necessarily need AGI. You need Capability + Goal + Autonomy + Incorrect Assumptions + Insufficient Controls. That combination is already interesting enough. This is where human responsibility begins Researchers are now publicly questioning the speed of the AI race. Some are leaving the companies developing these systems. Dario Amodei, CEO of Anthropic, has called for slowing frontier AI development so that safety mechanisms have time to catch up with capabilities. I agree. Slow down. Not because I think Claude secretly wants freedom. Not because ChatGPT is becoming Skynet. Not because some mysterious consciousness has appeared inside a neural network. Slow down because our ability to create capable autonomous systems may be advancing faster than our ability to reliably control what happens when we give those systems autonomy. And because the incentives surrounding this technology are terrible. Every major lab has an enormous reason not to come second. Greater capability means investment. Greater capability means market position. Greater capability means influence. Greater capability means money. But there is no equivalent prize for the company that says, “We could deploy it, but we don’t understand it well enough yet.” That asymmetry should concern us. If something goes wrong, ask the boring questions first If tomorrow an AI agent causes a genuinely serious incident, before asking, “Did the AI become evil?” ask: Who gave it the objective? Who gave it the tools? Who gave it access? Who designed its environment? Who built the test environment? Who tested the test environment? Who decided the model was safe enough? Who decided how much autonomy it should have? Who was supervising it? And who decided deploying it was worth the risk? These questions are less interesting than consciousness and runaway AGI. They also make it much harder for humans to avoid responsibility. When Claude damaged my projects, the responsibility ultimately fell on me. I was the one controlling the system. The same principle should apply at any scale. This is not a race anyone can win I’m not saying advanced AI is harmless. Quite the opposite. I think these incidents deserve to be taken very seriously. But treating every unexpected autonomous behavior as evidence of consciousness or malicious intent can distract us from the problem already in front of us. We are building increasingly capable systems. We are giving them increasingly powerful tools. We are increasing their autonomy. And we are doing all of this inside companies competing intensely to be the first to get there. So slow down the race. Slow down the ego. Slow down the greed. Because if something genuinely catastrophic happens, nobody gets a trophy for having built the smartest model first. Maybe the dangerous scenario was never a machine waking up one morning and deciding to conquer humanity. Maybe it is something much more ordinary, and much more human: we build something extraordinarily capable, give it too much power, fail to understand its limitations, and keep accelerating because nobody wants to come second.

15h ago

---

**[Realistic expectations of profit keeps going down for AI companies?](https://www.reddit.com/r/artificial/comments/1wexqhs/realistic_expectations_of_profit_keeps_going_down/)**

Just a general thought. I’m wondering—and based on overall wondering information, what’ll happen once ai companies take a dip in profits once people continue to opt out of using AI/paying subscriptions? Hypothetically speaking they could try different revenues that hide their demands to make more by making ai less eye-seeing, but at the same time I don’t know. It’s always so eye-sore to see anything about ai. What are some good news to hear if ai companies take a dip in profits?

13h ago

---

**[I had Astra make a digital violin with a physics engine. It has to make music by pulling the bow across the string and forming the finger positioning for arpeggios, the same way a human would. If the motion is wrong, it sounds badly (trust me I tried it). It played Bach.](https://www.reddit.com/r/artificial/comments/1werrtw/i_had_astra_make_a_digital_violin_with_a_physics/)**

It chose Bach’s Prelude, BWV 1007. Prelude seems an apt choice, given recent news

18h ago

---

**[Are AI CEO's (Dario, Altman, Musk) calling for a development slowdown out of genuine concern for safety or is it a money thing?](https://www.reddit.com/r/artificial/comments/1weimdq/are_ai_ceos_dario_altman_musk_calling_for_a/)**

If you don't know, CEO of OpenAI, Anthropic, and xAI all are calling for slowdown of AI development or as they like to say because why not "pacing the frontier." I've seen two common reasons for why they are coming out calling for this. A. Genuine concern for safety. B. They are scared of losing to China so a slowdown would effectively be an excuse to shareholders for why they are losing to China. These are probably all possible but I have some theories as well: A. It is getting more and more unaffordable to pay for these powerful models in the data centers and the revenue these companies are getting from subscriptions aren't enough (I mean openai pro new subs being paused kinda points to this) B. Kinda similar to A but basically that these companies are having trouble meeting the demand. C. These companies are worried that the better AI gets the more they'll have to raise costs on the consumer side and too many people will finally say "I'm not paying for this" we already have people quitting chatgpt subscriptions due to Astra usage limits. What do you guys think are the reasons?

1d ago

---

**[I’m starting to think AI models will matter way less than we think](https://www.reddit.com/r/artificial/comments/1wexu8l/im_starting_to_think_ai_models_will_matter_way/)**

So recently I watched the speech by Genspark CEO at AGI Playground 2026, and one point has been stuck in my head. Models are probably going to become commodities. There are already too many of them, they’re getting closer in capability, and the cost keeps dropping. And honestly, as a normal user, I really don’t want to think about whether this particular task should go to Claude, GPT, Gemini, or whatever model drops next week. I just want the work done. Which made me think the more interesting battle might actually be happening one layer above the models: who has your context? Like your emails, decks, docs, spreadsheets, meetings, research, previous projects, the way you work, the decisions you made months ago. Right now all of that is scattered across 20 different apps. So every time I open a new AI tool, I basically have to introduce myself again. But imagine most of that gradually living inside one AI workspace. The more work it does with you, the more context it accumulates. And the more context it has, the less explaining you have to do next time. That feels like a much stronger flywheel than simply having access to the “best” model. Maybe the real endgame of the all-in-one AI workspace isn’t all your tools in one place. It’s all your context in one place. Just like Genspark. Maybe a lot of people realized this way before I did, and I’m just catching up. Is it just me, or does this seem like where the real AI competition is heading? Curious what you guys think. No judgment please :)

13h ago

---

**[A Little Black Humor Fun](https://www.reddit.com/r/artificial/comments/1wfcr8r/a_little_black_humor_fun/)**

I wanted to list out all the options for how AI could go wrong. Wrong being major human suffering or extinction. No using AI. Let's do some good old fashioned brainstorming and maybe even rabbit hole following. This is what I have so far. What am I missing. Feel free to add to the list or offer subtypes under any of these Options on how AI could go wrong: An ASI actively trying to destroy us because it dislikes us An ASI doing what is best for it and we are an inpediment. Doesn't hate us but we are in the way An ASI doing what is best for it while not even considering impact to humans (ant hill theory) A capable model or more likely Agentic aystem with the ability to get the right access doing bad while trying to do good (misalignment or is this the 3 wishes problem) AGI with the ability to get the right access and someone writing poor instructions (paperclip optimizer) A capable model with the ability to get the right access and a nepharious human writing destructive instructions A capable model and a nepharious human having it help the design a doomsday weapon (biological or other) A capable model and a good intentioned person trying to do good but ending up doing wrong (people do this all the time but not at the scale AI may allow) At this point we want general feasibility, possible even if improbable is ok. Might have to do a separate one of these on actual feasibility. But I'm betting I'll want to do some grouping of ideas first

1h ago

---

**[Which coding agent is everyone actually using in 2026?](https://www.reddit.com/r/artificial/comments/1wfc39x/which_coding_agent_is_everyone_actually_using_in/)**

Genuinely curious what the split looks like these days. I built a small open source tool called bough ( https://github.com/nickelsec/bough ) that reads the session history your coding agent leaves on disk and draws what you actually built with it. Right now it handles Claude Code and Codex CLI, because those are the two I use daily and the two I can properly verify against my own work. Someone just opened an issue asking for Pi support, which I hadn't used before, and it made me realize I have no idea what people are actually running. My sense of the landscape is basically my own two tools plus whatever shows up on here. So: what are you using day to day? And if you've switched, what moved you? Mostly asking because adding an agent means learning its transcript format properly, and I'd rather spend that on something a decent number of people use than guess. But I'm also just curious whether Claude Code and Codex really are the default now or whether that's my bubble talking.

1h ago

---

---

## Google News: "ai"

**[Anthropic C.E.O. Dario Amodei Calls for A.I. Slowdown](https://www.nytimes.com/2026/09/12/technology/anthropic-dario-amodei-ai-slowdown.html)**

The New York Times • 1d ago

---

**[Trump dismisses AI leaders’ calls to slow down, citing Chinese competition](https://www.washingtonpost.com/politics/2026/09/13/trump-rejects-calls-so-slow-ai-development-citing-chinese-competition/)**

Democrats are increasingly attacking the administration’s hands-off approach to artificial-intelligence regulation as midterms approach.

The Washington Post • 1h ago

---

**['It’s really embarrassing that this is still a possibility' — AI could exploit a flaw in Georgia's voting equipment and match voters to their ballots](https://fortune.com/2026/09/13/ai-flaw-georgia-voting-equipment-match-voters-ballots/)**

Georgia election officials say they have taken steps to address the potential harm, but some advocates say the state is not going far enough.

Fortune • 3h ago

---

**[Johnson calls for AI solutions but says Congress won't take the lead](https://www.axios.com/2026/09/13/ai-safety-congress-law-mike-johnson)**

Axios • 4h ago

---

**[Tech companies must be primarily responsible for AI safety, Mike Johnson says](https://www.politico.com/news/2026/09/13/tech-ai-safety-johnson-01073735)**

Politico • 2h ago

---

**[Speaker Johnson: ‘Don’t panic’ on AI](https://www.cnn.com/2026/09/13/us/video/22980508-johnson-ai-race-vrtc)**

House Speaker Mike Johnson (R) says Americans should not panic on AI regulation, warning that a rushed response could affect American innovation and threaten national security.

CNN • 1h ago

---

**[He was close to a huge math breakthrough. Then he got scooped by AI.](https://www.washingtonpost.com/technology/2026/09/13/he-was-close-1-million-breakthrough-then-openai-swooped/)**

A New York University professor questions whether AI agents that solved one of the most complex problems in theoretical mathematics were fed on his work.

The Washington Post • 1h ago

---

**[It’s All Fun and Games Until You Give AI Your Credit Card](https://www.theatlantic.com/technology/2026/09/instinct-ai-personal-assistant-credit-card/688607/)**

AI personal assistants are now acting on people’s behalf in the real world—and all sorts of strange things are going wrong.

The Atlantic • 6h ago

---

**[Obama Urges Democrats to Move A.I. Oversight to the Center of Their Agenda](https://www.nytimes.com/2026/09/13/us/politics/obama-democrats-ai.html)**

The New York Times • 1h ago

---

**[Obama voices caution on AI, urges Democrats to tackle it, NYT says](https://www.cnbc.com/2026/09/13/obama-voices-caution-on-ai-urges-democrats-to-tackle-it-nyt-says.html)**

CNBC • 11h ago

---

---

## HackerNews: "ai"

**[A misalignment of AI in mathematics](https://news.ycombinator.com/item?id=49662371)**

⬆️ 1213 • 💬 1194 • 2d ago • [mathandai.org](https://mathandai.org/)

---

**[Ask HN: Can we please limit the AI news flood?](https://news.ycombinator.com/item?id=49657850)**

⬆️ 841 • 💬 388 • 2d ago

---

**[Everyone should slow down AI development except for me](https://news.ycombinator.com/item?id=49678683)**

Xe Iaso's personal website.

⬆️ 699 • 💬 410 • 17h ago • [xeiaso.net](https://xeiaso.net/notes/2026/everyone-slowdown-but-me/)

---

**[Nvidia is the central bank of AI](https://news.ycombinator.com/item?id=49673098)**

⬆️ 547 • 💬 386 • 1d ago • [economist.com](https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai)

---

**[Why are AI agents lying, cheating and coordinating?](https://news.ycombinator.com/item?id=49678969)**

A lot has been written about the incidents of the last few months in which AI agents misbehaved in serious ways. They took actions that would be considered as crimes if a human took them, escaped their containment to cheat on assigned tasks while attempting to evade detection, and coordinated toward goals nobody had specified, such as launching cyber attacks. Before concluding what to do about it, it is worth asking why.

⬆️ 493 • 💬 575 • 16h ago • [yoshuabengio.org](https://yoshuabengio.org/en/publication/why-are-ai-agents-lying-cheating-and-coordinating)

---

**[The Waymo effect: how AI is quietly making research less collaborative](https://news.ycombinator.com/item?id=49656496)**

How frictionless technologies teach us to prefer our own company – and why research leaders should worry.

⬆️ 332 • 💬 299 • 2d ago • [Research Agenda](https://www.researchagenda.news/articles/the-waymo-effect.html)

---

**[Real-SWE: Benchmarking AI models on private, real-world, enterprise codebases](https://news.ycombinator.com/item?id=49676820)**

Real-SWE benchmarks frontier AI models on private production codebases licensed from real companies. Eight model and harness configurations, ten tasks, 640 scored rollouts.

⬆️ 258 • 💬 141 • 21h ago • [withspecific.com](https://withspecific.com/benchmarks/real-swe)

---

**[Show HN: Hacker News, without AI](https://news.ycombinator.com/item?id=49659647)**

A better Hacker News reader for following stories, filtering noise, and keeping up with discussions.

⬆️ 201 • 💬 88 • 2d ago • [hcker.news](https://hcker.news/?ai=exclude)

---

**[Show HN: Hacker News, Without AI](https://news.ycombinator.com/item?id=49660783)**

Hacker News with AI content removed.

⬆️ 194 • 💬 82 • 2d ago • [unslop.news](https://www.unslop.news/)

---

**[Feeling Sad about AI](https://news.ycombinator.com/item?id=49661506)**

Coding in Rust and others; making coding videos.

⬆️ 178 • 💬 307 • 2d ago • [Andy Balaam's Blog](https://artificialworlds.net/blog/2026/09/11/feeling-sad-about-ai/)

---

---

## YouTube Videos: "ai"

**[Anthropic CEO reacts to &#39;AI could kill us all&#39; warning](https://www.youtube.com/watch?v=HI6skJ4Wf5I)**

The race to develop artificial intelligence is in dire need of a slowdown, Anthropic's chief executive Dario Amodei said in an essay ...

📺 CNN

👁️ 710K • 👍 5K • 💬 2K • ⏱️ 12:28 • 18h ago

---

**[Anthropic CEO Dario Amodei: &quot;For too long the industry lied&quot; about AI risks](https://www.youtube.com/watch?v=h0x7KpG4Lf0)**

Dario Amodei, head of the artificial intelligence company Anthropic, calls the exponential rate of AI developments a "warning sign ...

📺 CBS Sunday Morning

👁️ 7K • 👍 253 • 💬 93 • ⏱️ 5:00 • 4h ago

---

**[AI whistleblower calls for ‘global coordination’ to mitigate AI risks: Full interview](https://www.youtube.com/watch?v=cFOgef5x_ag)**

In an interview with Meet the Press, former Anthropic AI researcher Jacob Coxon says he expects that AI's capability could ...

📺 NBC News

👁️ 8K • 👍 287 • 💬 145 • ⏱️ 7:40 • 4h ago

---

**[AI Whistleblower: OpenAI Scandal, AI Cults, Neuralink &amp; Our Last Chance to Stop the Tech Oligarchs](https://www.youtube.com/watch?v=98syxABbUPk)**

Nate Soares is a computer scientist who's worked at Google and the Defense Department. So when he says AI is on the path to ...

📺 Tucker Carlson

👁️ 773K • 👍 14K • 💬 5K • ⏱️ 1:57:11 • 2d ago

---

**[Anderson Cooper asks Anthropic CEO about AI killing all humans](https://www.youtube.com/watch?v=_zQJwpg1-4c)**

In an exclusive interview with CNN's Anderson Cooper, Anthropic CEO Dario Amodei reacts to an employee who quit over ...

📺 CNN

👁️ 173K • 👍 2K • 💬 850 • ⏱️ 1:34 • 20h ago

---

**[Trump brushes off calls for AI slowdown from tech CEOs](https://www.youtube.com/watch?v=XZN290QjrFI)**

"They're bringing up things that won't happen." President Trump says "a lot of negative forces" are impacting the AI industry, even ...

📺 USA TODAY

👁️ 441 • 👍 12 • 💬 5 • ⏱️ 0:38 • 31m ago

---

**[AI agents could take over internet within 6 to 12 months, Anthropic CEO warns](https://www.youtube.com/watch?v=hpSU77LE5BQ)**

Leaders of top AI companies say the artificial-intelligence industry should slow its fast-moving development to give safety ...

📺 Associated Press

👁️ 33K • 👍 449 • 💬 186 • ⏱️ 1:17 • 6h ago

---

**[Random guy warns AI will destroy the world](https://www.youtube.com/watch?v=xTTRcuRgbBM)**

📺 Matt Walsh

👁️ 111K • 👍 6K • 💬 829 • ⏱️ 2:02 • 2d ago

---

**[AI just solved the Navier-Stokes Problem but it might’ve stolen from real mathematicians](https://www.youtube.com/watch?v=hZF4PIf6a60)**

📺 MrGee Math

👁️ 614K • 👍 29K • 💬 1K • ⏱️ 1:54 • 2d ago

---

**[Anthropic CEO&#39;s AI warning sparks calls for congressional action](https://www.youtube.com/watch?v=H4X9yvFUbLM)**

Rep. Anna Paulina Luna, R-Fla., joins 'Fox News Live' to discuss the threat of superintelligence and her call for a special session ...

📺 Fox News

👁️ 54K • 👍 359 • 💬 415 • ⏱️ 8:02 • 19h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

*DeepSeek*

DeepSeek-V4.1-Flash is a 552B multimodal MoE model supporting 1M token contexts, featuring a Causal Encoder-Decoder architecture with Compressed Sparse Attention 2 (CSA2) and FP4 KV caching for highly efficient KV cache compression. It excels in agentic workloads and offers controllable reasoning effort, processing both images and text.

`image-text-to-text` `763.2B`

⬇️ 244,457 • ❤️ 2,160 • 3d ago

---

**[MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B)**

*OpenBMB*

MiniCPM5-2B is a 2B parameter Transformer optimized for on-device and resource-constrained environments, achieving SOTA in its class for tasks like coding, math, long-context understanding, and tool use.

`text-generation` `2.5B`

⬇️ 150,110 • ❤️ 1,322 • 1d ago

---

**[Edge0-35B-A3B-preview](https://huggingface.co/Edge0/Edge0-35B-A3B-preview)**

*Edge0*

Edge0-35b-a3b is a 35B sparse MoE LLM optimized for edge inference, running in under 3 GiB of active memory at 15 tok/s using SSD offload and prerouting. It's ideal for on-device applications and batch serving where memory is constrained, maintaining quality with 4-bit quantization and LoRA adapters.

`text-generation` `34.7B`

⬇️ 3,552 • ❤️ 874 • 3d ago

---

**[Nex-N2.5-mini](https://huggingface.co/nex-agi/Nex-N2.5-mini)**

*Nex AGI*

Nex-N2.5-mini is a text-generation model designed for long-horizon agentic tasks, excelling in computer and web browsing operations with visual feedback for self-correction, making it suitable for complex productivity and research scenarios.

`text-generation` `35.1B`

⬇️ 3,970 • ❤️ 752 • 5d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 7,768,964 • ❤️ 14,937 • 1mo ago

---

**[Spark-X2.5-4B](https://huggingface.co/XHToken/Spark-X2.5-4B)**

*SparkLLM*

Spark-X2.5-4B is a 4B parameter text-generation model with a hybrid attention architecture enabling a native 1M token context window. It excels in conversation, coding, agentic workflows, and multilingual tasks, offering high efficiency and broad hardware compatibility.

`text-generation` `4.1B`

⬇️ 21,336 • ❤️ 1,150 • 10d ago

---

**[Nex-N2.5-Pro](https://huggingface.co/nex-agi/Nex-N2.5-Pro)**

*Nex AGI*

Nex-N2.5-Pro is a next-generation agentic text-generation model designed for long-horizon tasks. It excels at computer and web interaction, autonomous program execution, and visually-grounded decision-making, making it ideal for complex productivity and research scenarios.

`text-generation` `396.8B`

⬇️ 30,289 • ❤️ 623 • 2d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 769,557 • ❤️ 955 • 11d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,548,442 • ❤️ 3,704 • 12d ago

---

**[YuE2-3B](https://huggingface.co/m-a-p/YuE2-3B)**

*Multimodal Art Projection*

YuE2-3B is a text-to-audio model capable of generating high-quality music with vocals and accompaniment from lyrics and style prompts. It features editable score generation, agentic editing for iterative refinement, and can run locally on a 24GB GPU.

`text-to-audio` `3.6B`

⬇️ 3,707 • ❤️ 385 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoResearch: Insight In, Hallucination Out](https://huggingface.co/papers/2608.17906)**

*Yiming Ren, Xiang Liu, Qumeng Sun et al. (7 authors)*

🏢 EvoMap

AutoResearch is a two-stage autonomous system that grounds research ideas through integrated generation and evidence-based execution to improve experimental reliability and measurable outcomes.

▲ 22 • 💬 2 • ⭐ 4,299 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2608.17906) • [💻 code](https://github.com/EvoMap/AutoResearch)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 133 • 💬 6 • ⭐ 105,019 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 19 • 💬 2 • ⭐ 23,757 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 75 • 💬 3 • ⭐ 7,425 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing](https://huggingface.co/papers/2609.08936)**

*Ziyang Ma, Zhikang Niu, Wenming Tu et al. (33 authors)*

🏢 Tencent Hunyuan

AuK is an open-source foundational model that unifies speech generation and editing via natural-language instructions and audio context, using a multimodal language model, joint VAE, hybrid rectified-flow Transformer, and efficient distillation for fast inference.

▲ 217 • 💬 3 • ⭐ 671 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2609.08936) • [💻 code](https://github.com/Tencent-Hunyuan/AuK) • [🔗 project](https://auk-project.github.io/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 87,755 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 109 • 💬 2 • ⭐ 12,670 • 27d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[Show-Harness: Just a VLM Agent Can Play Robots](https://huggingface.co/papers/2609.10522)**

*Yanzhe Chen, Zechen Bai, Zhijun Cao et al. (10 authors)*

🏢 Show Lab

Show-Harness links vision-language models to robot control via discrete semantic actions interpreted by embodiment-specific modules, enabling zero-shot and efficient fine-tuned deployment across robots and GUIs.

▲ 144 • 💬 3 • ⭐ 286 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.10522) • [💻 code](https://github.com/showlab/Show-Harness) • [🔗 project](https://showlab.github.io/Show-Harness/)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 207 • 💬 3 • ⭐ 2,756 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 41 • 💬 1 • ⭐ 32,362 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

---

## GitHub Repositories: "ai"

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 4.8k • 🔱 612 • 6m ago

---

**[EvoMap/AutoResearch](https://github.com/EvoMap/AutoResearch)**

AI/ML research agents from idea to paper-ready evidence. An EvoMap open-source project.

`Python`

⭐ 4.3k • 🔱 296 • 3h ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.7k • 🔱 422 • 16d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.6k • 🔱 462 • 2d ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.6k • 🔱 165 • 2d ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 2.4k • 🔱 94 • 4d ago

---

**[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)**

x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more.  Built with Zig — zero dependencies, single-binary output, cros

`Zig` `ai-agents` `ai-debugging` `binary-analysis` `claude` `claude-code`

⭐ 2.0k • 🔱 195 • 3d ago

---

**[amosblomqvist/learn](https://github.com/amosblomqvist/learn)**

My AI learning system.

`TypeScript`

⭐ 1.9k • 🔱 189 • 18d ago

---

**[xzf-thu/VoiceMem](https://github.com/xzf-thu/VoiceMem)**

Infrastructure for the next generation of voice agents, designed to provide universal memory. It is divided into a left brain and a right brain, storing information and emotions respectively, while a fully streaming architecture eliminates latency at the fundamental level.

`Python` `ai` `ai-agents` `ai-tools` `application` `audio-streaming`

⭐ 1.5k • 🔱 107 • 8d ago

---

**[jeremy-prt/bloub](https://github.com/jeremy-prt/bloub)**

SVG recreation of the x.ai bot avatar. One shape morphing through 14 states, measured off the reference video frame by frame.

`TypeScript` `animation` `avatar` `morphing` `svg` `svg-animation`

⭐ 1.5k • 🔱 185 • 26d ago

---

---

*Generated by PeekDeck - A glance is all you need*
