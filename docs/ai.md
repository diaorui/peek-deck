---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-24T16:37:07.845950+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 24, 2026 at 16:37 UTC  
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

**[I brought ChatGPT, Claude, and Gemini into a group chat to solve a complex problem. Here is how they caught each other hallucinating](https://www.reddit.com/r/artificial/comments/1vx1jrm/i_brought_chatgpt_claude_and_gemini_into_a_group/)**

You probably know how it goes: you give a complex prompt to a LLM, it spits out a highly confident answer, and you just sort of... hope it’s right. If you ask the same question in a different tab, Claude might give you a completely different answer. Gemini might say they are both wrong. I've done it this way for a long time, and many of my friends seem to do the same. I wanted to see what happens if you don't just compare answers, but actually bring AI models into a shared chat to discuss the question together. Here is how it went when they could discuss each other's replies in real-time: - ChatGPT went first. It wrote a beautiful, highly structured, and completely wrong answer. It hallucinated a tax rule that didn't apply to the prompt. - Claude stepped in next. It immediately flagged GPT’s tax hallucination, but overcorrected and messed up the final math equation. - Gemini acted as the final Judge. It took ChatGPT’s original structure, applied Claude’s logical correction, fixed the math, and spat out a flawless final output. The takeaway: Letting an AI model review itself is like a student grading their own work. It just repeats the same assumptions. When you force different models (OpenAI vs Anthropic vs Google) to fact-check each other, they actually expose each other's blind spots and hallucinations. I got so obsessed with this multi-AI workflow that I built a site to let these models debate in real-time without having to copy-paste between different tabs (I posted about it earlier here). If anyone wants to try it or testing their own complex questions, curious to hear what kind of workflows you guys would use it for.

🔗 [Rauno](https://rauno.ai) • 4h ago

---

**[AI agents are now using 5x more tokens than humans..](https://www.reddit.com/r/artificial/comments/1vwkkoh/ai_agents_are_now_using_5x_more_tokens_than_humans/)**

18h ago

---

**[Anthropic's IPO filing will reportedly name public opposition to AI as a formal risk factor](https://www.reddit.com/r/artificial/comments/1vx2ylz/anthropics_ipo_filing_will_reportedly_name_public/)**

CNBC reported this week that Anthropic's confidential IPO filing (filed back in June) will name public opposition to AI and to new data centers as a formal risk factor once the public documents drop, expected within weeks. That would make it the first major AI lab IPO to disclose that risk in writing rather than treat it as a footnote. The number behind it: a Gallup survey from earlier this year found about seven in ten Americans oppose new AI data centers being built near them, and roughly half of them feel strongly about it. For comparison, SpaceX's own 2026 IPO filing named specific Grok product risks but did not name public opposition to AI itself as a risk factor, even though Grok runs on comparable underlying technology. The mechanism behind why a company would voluntarily name a risk investors already suspect: it is generally a stronger legal and reputational position than staying silent. If a regulator or a plaintiff's lawyer later argues the company should have disclosed that risk, "we already told investors" beats "we left it out." Curious what people think: does this become the standard template for AI-company IPOs now that one frontier lab has done it, or is Anthropic in an unusual position here because of how central "AI safety" already is to its brand?

3h ago

---

**[I ran the same AI character through 40 comic strips and she slowly became a different person](https://www.reddit.com/r/artificial/comments/1vx4nyd/i_ran_the_same_ai_character_through_40_comic/)**

About six months ago I started a weekly webcomic. I should say from the start that the character is entirely AI produced, there was no traditional artwork involved at any point. The whole experiment was testing whether I could keep one consistent face across a long serialized run without the audience catching drift. Setup was straightforward. I created her in APOB AI, which costs nothing for everyday use and saves a character profile so it outputs a matching face every time, arranged panels in Clip Studio Paint, and kept a reference folder pinned with the original angles, expressions, and lighting I wanted to reuse every week. For the first twenty or so strips it genuinely felt like it was working. Same face, same proportions, recognizable week to week. Readers treated her like any other webcomic protagonist. Nobody asked whether she was AI. Around strip twenty five I started noticing something when I went back to my reference folder. The jawline had narrowed slightly. Eye spacing was maybe two percent wider. Nothing you'd catch between consecutive strips, but when I put strip one next to strip twenty five the difference was undeniable. Like seeing someone after they've gotten a haircut you can't quite place. I kept going. At strip thirty two a reader left a comment that said something like "did you redesign the character? she looks different but I can't figure out how." That was the moment the drift crossed from my own paranoia into actual audience perception. I went back and audited all forty strips against the original reference set. Seven needed full redraws to bring the face back toward strip one. Most of those fell in the thirty to forty range where cumulative drift had really compounded. The redraws were not perfect either, because I was now generating from a corrected reference that was itself slightly removed from the true original. The pattern I noticed is that it isn't random noise. The face doesn't jitter around a center point. It walks slowly away from it, and it walks in a specific direction. Features that made the original character distinctive (a slightly crooked nose, an uneven smile line) gradually smoothed out. By strip forty she looked more conventionally attractive but less like herself. The drift makes faces more symmetrical and more generic over time. I don't have a real fix for this. What I'm doing now is hard resetting to the original reference images every five strips instead of letting the most recent output become the next seed. That's cut the problem down but has not eliminated it. Seven redraws out of forty is roughly eighteen percent, which is honestly more than I had budgeted for when I started this. The thing that still gets me is that nobody noticed strip to strip. The drift is completely invisible at one week intervals. It only becomes obvious when you compress the timeline and compare endpoints. Strip one and strip forty look like cousins, not the same person.

1h ago

---

**[I reran the benchmark. The deterministic result reproduced exactly — but the model-related metric tells a different story.](https://www.reddit.com/r/artificial/comments/1vx563w/i_reran_the_benchmark_the_deterministic_result/)**

I reran the benchmark. The deterministic result reproduced exactly — but the model-related metric tells a different story. After the discussion on my previous benchmark, I reran the verification capability benchmark and inspected the results more carefully. The benchmark contains 66 cases and measures 9 capability dimensions of a deterministic verification engine. I ran two fixture-based benchmark executions: publishable-v1-selfcheck publishable-v1-repeat2 Both runs used the same commit: f38cba58f4c0b108ae53cc2eb2a50ff9e4e806e8 And both produced the exact same result: 66/66 cases passed. 0 failures. Every measured capability dimension passed 66/66: Claim binding Evidence graph integrity Deterministic calculation Rule application Contradiction detection Missing evidence detection Verification outcome Reproducibility Auditability So, within this benchmark configuration, the fixture-based deterministic result reproduced exactly across both runs. But there is another number in the report that I think is important: model_assertion_correctness: 12/24 The benchmark explicitly treats that as a secondary reference metric, not part of the primary deterministic capability score. And I think that distinction is becoming the central lesson of this work. Deterministic verification capability ≠ Model generation correctness ≠ End-to-end production reliability A system can be internally reproducible and deterministic while still depending on a probabilistic model that produces unreliable, ambiguous, or incorrectly structured assertions. That is why I'm moving away from treating the benchmark as one number. Instead, I want to separate: 1. Can the deterministic verifier correctly process canonical benchmark inputs? 2. Can the model produce correct claims? 3. Can those claims survive parsing, normalization, canonicalization, and binding? 4. Can the complete production pipeline work end-to-end? These are different questions. The rerun gave me more confidence in one thing: The deterministic benchmark result is reproducible within the tested configuration. But it also reinforced that reproducibility of the verifier should not be confused with correctness or reliability of the model that feeds it. The next benchmark version will therefore focus on identifying the first invalid state for every failure: Model output ↓ Parsing ↓ Schema validation ↓ Normalization ↓ Canonicalization ↓ Claim binding ↓ Evidence graph ↓ Deterministic verification ↓ Final outcome Rather than just: PASS / FAIL I'm interested in whether others working on LLM + deterministic systems would benchmark these layers separately. Would you treat deterministic capability, model correctness, interface/contract integrity, and end-to-end reliability as separate benchmark scores? Or is there a better framework for measuring this kind of architecture?

1h ago

---

**[A new approach to building smarter more capable AI](https://www.reddit.com/r/artificial/comments/1vwxaip/a_new_approach_to_building_smarter_more_capable_ai/)**

A new approach to building smarter more capable AI We seem to be in a situation where we cannot see the forest for the trees in the philosophy of how to make AI more capable. We are ignoring the only known working intelligence multiplier we have encountered : human civilization What if we built a framework for current models to use that acts like a durable civilization scaffold. No retraining or model weight modification needed. The civilization scaffold would preserve agentic solutions with provenance, it would filter out bad results, and as it grew it would allow agents to stop reproducing already closed avenues of investigation, what did or did not work, what still needs investigation. It can pick up right where previous agents left off and springboard ahead. We keep retraining brute force - that is not the answer. An artificial civilization scaffold would be the place where the capabilities improve not the model. Eventually you could distill out the improvements and viable chains of investigation for model training. In the meantime the civilization scaffold allows current models to improve immediately and recursively when using the scaffold. And controlling the scaffold is another control surface that can be rolled back or suspended if needed while preserving the model at its current level

7h ago

---

**[i think AI memory is more than just remembering things](https://www.reddit.com/r/artificial/comments/1vww7ix/i_think_ai_memory_is_more_than_just_remembering/)**

i've been thinking about this a lot lately. most AI memory today seems to work like: “you like this” “you told me this before” “you work on this” but i don't think that's what human memory really is. our conversations, projects, decisions, mistakes, relationships, ideas and experiences all connect together. they create a history of how we became who we are. so what if AI didn't just remember facts about you, but could understand your journey? for example, imagine giving an AI access to years of your conversations, projects, notes and decisions. instead of asking: “what do you remember about me?” you could ask: “how have i changed over the last 3 years?” “what patterns do you see in the decisions i've made?” “why do you think my interests changed?” “what ideas have i kept coming back to?” that's the direction we're exploring with something we're building called innernet with my bros. the idea is basically to create a persistent context layer for a person, where different parts of your history can stay connected over time. i'm curious what other people think: would you actually want an AI to understand your history this deeply, or would that feel like too much?

8h ago

---

**[Am I not using AI enough?](https://www.reddit.com/r/artificial/comments/1vwzto9/am_i_not_using_ai_enough/)**

How does everyone stay on top of the different platforms, models and versions? I see discussions like "ew, since the v4.25 model change I hate it. The responses are not the same and my code doesn't run" or "this model is truly a unique experience". Feels like every week there is a new model and I'm not a power user enough to get a sense of what changed and don't feel the need to "care" about it. Alternatively I see many posts talking about usage tokens, API, configuring agents, building apps, games. My experience is using AI at home (Claude) for cooking and general suggestions entirely as a chatbot. I rarely if ever hit my free usage limit. At work they give us Chat GPT and Cowork. I use it to review my code, respond to emails and do some data analysis. I feel like I'm not doing enough. It's like trying to get into crypto and web3. I tried to read a cryptocurrency white paper and after 3 sentences had 10 questions and didn't know what 8 of the words mean. Are these people talking about usage tokens and detailed model reviews so curious and power users? Do they do all this for work or a side project hobby? Trying to make money? Adopt new tech? Is it ok to be satisfied with the minimum chat bot helper without stressing over models, API connections, auth, tokens and building their own agents? I guess I don't have any more use cases at the moment?

5h ago

---

**[Did we made full cycle? Low level understanding of programming is now more important than syntax knowledge?](https://www.reddit.com/r/artificial/comments/1vx4rg9/did_we_made_full_cycle_low_level_understanding_of/)**

As people created the most abstract way of programming, syntax knowledge of programming language importance is decreasing, still, you need to understand WHAT code does, but the more important thing, now you need to build architectures instead of raw code, and the best way to make efficient and fast system, is to understand how computer works inside. How does that relate to AI and LLMs? From my experiences, LLMs are extremely bad with huge code-bases, but frighteningly efficient with small tasks, good old divide and conquer, if you separate tasks and create modular and abstract enough architecture, that even newbie will understand, LLM can create perfect, edge-case proof code. Does that mean, that we went full cycle and returned back to need of software engineering, instead of direct code writing?

1h ago

---

**[AI stigma punishes legitimate use](https://www.reddit.com/r/artificial/comments/1vwulqn/ai_stigma_punishes_legitimate_use/)**

More thoughts on AI writing, detection and watermarking

🔗 [blog.keyvan.net](https://blog.keyvan.net/p/ai-stigma-punishes-legitimate-use) • 10h ago

---

---

## Google News: "ai"

**[Some of Russia’s A.I. Drones Are Powered by Nvidia Microcomputers, Ukrainian Officials Say](https://www.nytimes.com/2026/08/24/world/europe/ukraine-war-nvidia-ai-autonomous-drones.html)**

The New York Times • 5h ago

---

**[Taiwan issues indictments over alleged illegal export of AI servers to China](https://www.reuters.com/world/asia-pacific/taiwan-indicts-9-over-alleged-illegal-export-ai-servers-china-2026-08-24/)**

Reuters • 7h ago

---

**[Goldman Sachs partner warns of 'huge danger' in letting AI replace bankers' reasoning skills](https://www.cnbc.com/2026/08/24/goldman-sachs-ai-partner-danger-skills.html)**

Goldman Sachs is embracing AI, but one of its senior tech leaders warns that it comes with an unintended risk: weakening the reasoning skills of future bankers.

CNBC • 1h ago

---

**[America's energy sector needs 500,000 more workers by 2030 thanks to AI—robots may have to step in](https://fortune.com/2026/08/24/americas-energy-sector-needs-500000-more-workers-by-2030-thanks-to-ai-unless-more-workers-retrain-humanoid-robots-step-in/)**

America’s energy sector is thriving thanks to AI. The only issue? There aren’t enough workers to meet the demand.

Fortune • 1h ago

---

**[Why AI Productivity Is Corporate America's Biggest Self-Deception](https://www.forbes.com/sites/karadennison/2026/08/24/why-ai-productivity-is-corporate-americas-biggest-self-deception/)**

Companies are spending billions on AI and telling investors it's working. Ask the employees and you get a different answer.

Forbes • 1h ago

---

**[From AI tools to alcohol drops: The unexpected forces driving America's crime decline](https://www.axios.com/2026/08/24/violent-crime-decline-theories)**

Axios • 7h ago

---

**[Nobody knows who built AI coding model Ox Alpha or where the code goes](https://siliconangle.com/2026/08/23/nobody-knows-who-built-ai-coding-model-ox-alpha-or-where-the-code-goes/)**

Nobody knows who built AI coding model Ox Alpha or where the code goes - SiliconANGLE

SiliconANGLE • 18h ago

---

**[The Odds: The AI Anxiety](https://www.cnn.com/2026/08/24/us/video/the-odds-the-ai-anxiety-cnc-kalpar)**

Public anxiety over AI skyrockets, with a vast majority fearing job losses and trusting neither party to manage the risks. CNN News Central’s John Berman and Chief Data Analyst Harry Enten look at this growing disconnect and when prediction markets expect an OpenAI IPO.

CNN • 2h ago

---

**[Nvidia’s Earnings Will Test Wall Street’s Faith in the AI Boom](https://www.wsj.com/articles/nvidias-earnings-will-test-wall-streets-faith-in-the-ai-boom-09865fea)**

WSJ • 6h ago

---

**[AI is coming for your glasses](https://www.ft.com/content/3f25f892-2de2-40e6-9592-a7ac18682c6c?syn-25a6b1a6=1)**

Big Tech thinks wearables are the gateway to artificial intelligence. Critics call it cringe stalkerware

Financial Times • 12h ago

---

---

## HackerNews: "ai"

**[Digging the grave of my skills: Hollywood creatives training AI to do their jobs](https://news.ycombinator.com/item?id=49399941)**

Amid a jobs slump, award-winning writers, directors and producers taking on sometimes lucrative temp work teaching AI skills such as screenwriting and production

⬆️ 55 • 💬 70 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/aug/22/the-hollywood-creatives-training-ai-to-do-their-jobs)

---

**[Anthropic IPO filing will show AI backlash as a risk factor, sources say](https://news.ycombinator.com/item?id=49401229)**

Anthropic is poised to debut on the stock market at a time when the public is increasingly upset about data centers and is fearful about AI taking jobs.

⬆️ 37 • 💬 80 • 2d ago • [CNBC](https://www.cnbc.com/2026/08/21/-anthropic-ipo-filing-will-show-ai-backlash-as-risk-sources-say.html)

---

**[Embedded AI](https://news.ycombinator.com/item?id=49397947)**

A project-driven guide to designing, training, and deploying artificial intelligence directly on embedded hardware, showing how to build intelligent, autonomous systems under real-world constraints.

⬆️ 37 • 💬 9 • 2d ago • [nostarch.com](https://nostarch.com/embedded-ai)

---

**['AI refuser' quit her dream job, and hopes others follow](https://news.ycombinator.com/item?id=49407785)**

Gabrielle Boyle resigned three days before the AFL switched on Microsoft’s AI assistant, having been told she couldn’t opt out.

⬆️ 34 • 💬 39 • 1d ago • [The Sydney Morning Herald](https://www.smh.com.au/technology/this-ai-refuser-quit-her-dream-job-and-hopes-others-follow-20260818-p60pdu.html)

---

**[AI has failed to win people's trust. Its makers? less trusted](https://news.ycombinator.com/item?id=49404869)**

Surveys on both sides of the Atlantic reveal a public more wary than wowed by AI, with distrust extending well beyond the technology and onto the tech executives promoting it.

⬆️ 28 • 💬 5 • 1d ago • [euronews](https://www.euronews.com/next/2026/08/20/ai-has-failed-to-win-peoples-trust-its-makers-even-less-trusted)

---

**[Dutch regulator fines Uber €825M for letting AI deactivate driver accounts](https://news.ycombinator.com/item?id=49398609)**

The Dutch Data Protection Authority (AP) has fined Uber €825 million for deactivating driver accounts through automated systems and without adequately informing them. This violates Europe’s General Data Protection Regulation (GDPR), the AP said in a decision made on Monday, Reuters reported after seeing the decision.

⬆️ 21 • 💬 4 • 2d ago • [NL Times](https://nltimes.nl/2026/08/21/dutch-regulator-fines-uber-eu825-mil-letting-algorithm-deactivate-drivers-accounts)

---

**[Palantir's Karp – frontier AI labs that are 'trying to drug addict us'](https://news.ycombinator.com/item?id=49405966)**

Karp said Chinese models can't be blamed for distilling U.S. models when the frontier labs "distilled all the value of IP, everywhere."

⬆️ 19 • 💬 8 • 1d ago • [CNBC](https://www.cnbc.com/2026/08/03/palantir-karp-open-ai-anthropic-open-weight.html)

---

**[I'm Sick of Reading AI-Written Posts](https://news.ycombinator.com/item?id=49392479)**

They all sound like the same guy

⬆️ 17 • 💬 5 • 2d ago • [Medium](https://cyb3rops.medium.com/im-sick-of-reading-ai-written-posts-107767481fbf)

---

**[Nvidia just showed that the harness, not the AI model, is now the real hero](https://news.ycombinator.com/item?id=49393647)**

Nvidia research shows that AI agents can perform well, and not go off the deep end, through fine-tuning, even if the AI model isn't that great at the task.

⬆️ 16 • 💬 1 • 2d ago • [TechCrunch](https://techcrunch.com/2026/08/21/nvidia-just-showed-that-the-harness-not-the-ai-model-is-now-the-real-hero/)

---

**[Andrew Ng: "AI Engineering Skills Map: Building and Deploying AI Applications"](https://news.ycombinator.com/item?id=49407944)**

AI Engineering Skills Map: Building and Deploying AI Applications

⬆️ 15 • 💬 0 • 1d ago • [X (formerly Twitter)](https://twitter.com/AndrewYNg/status/2090840747738374568)

---

---

## YouTube Videos: "ai"

**[New Evidence AI Might Already be Conscious | Dr. Roman Yampolskiy](https://www.youtube.com/watch?v=gVrvd0CMA-8)**

Link to full episode: https://youtu.be/ebWFexw51qM?si=5W4y2WkHIqse7pie Blake Lemoine lost his job at Google for saying the ...

📺 Danny Jones Clips

👁️ 76K • 👍 1K • 💬 450 • ⏱️ 10:04 • 2d ago

---

**[&quot;Only 2 Years Left&quot; AI Whistleblower Warns What Comes Next | Roman Yampolskiy](https://www.youtube.com/watch?v=ebWFexw51qM)**

Watch every episode ad-free & uncensored on Patreon: https://patreon.com/dannyjones Roman V. Yampolskiy is a computer ...

📺 Danny Jones

👁️ 157K • 👍 3K • 💬 1K • ⏱️ 1:50:40 • 2d ago

---

**[RDC vs ai 😂 #rdc #rdcworld #ai](https://www.youtube.com/watch?v=TfcH--vUJiw)**

📺 MelandWorld1

👁️ 17K • 👍 920 • 💬 34 • ⏱️ 0:34 • 15h ago

---

**[AI Jobs](https://www.youtube.com/watch?v=KixsIL38wkY)**

My Patreon: https://www.patreon.com/cw/nateziller This episode brings back Paper as he tries to find a job with the help of AI.

📺 Nate Ziller

👁️ 123K • 👍 10K • 💬 662 • ⏱️ 5:15 • 22h ago

---

**[New AI waifus, new Deepseek, realtime worlds, Happy Shrimp, tiny TTS: AI NEWS](https://www.youtube.com/watch?v=rQ4yX5qNYdY)**

HUGE AI NEWS: Deepseek Vision, Ornith 1.5, Happy Shrimp, SenseNova U1.5 #ai #ainews #aitools #singularity #agi Thanks to ...

📺 AI Search

👁️ 93K • 👍 4K • 💬 423 • ⏱️ 32:12 • 1d ago

---

**[The AI bubble is about to burst](https://www.youtube.com/watch?v=fGGuVY6Tcog)**

Tech CEOs are quietly cancelling their AI plans, and the reason isn't that artificial intelligence stopped working. It's that companies ...

📺 The Infographics Show

👁️ 186K • 👍 3K • 💬 713 • ⏱️ 3:27:05 • 2d ago

---

**[The REAL Reason AI Is About To Change Everything](https://www.youtube.com/watch?v=Bj02me1CHmE)**

Geopolitical expert Ian Bremmer, founder of Eurasia Group and a man who has forecast the world's biggest risks for over 25 years, ...

📺 The Diary Of A CEO Clips

👁️ 162K • 👍 3K • 💬 343 • ⏱️ 16:15 • 1d ago

---

**[I Made a Viral AI Love Story (500M Views) — Steal My Prompts](https://www.youtube.com/watch?v=QfylrxtQSSs)**

I made an AI love story for my friend's wedding — it hit ~500M views across social. Here's the full workflow, and every prompt is ...

📺 Higgsfield AI

👁️ 52K • 👍 2K • 💬 203 • ⏱️ 23:20 • 3d ago

---

**[How a $20 AI is Replacing $235,000 Lawyers](https://www.youtube.com/watch?v=haZ5gddlQ4g)**

Lawyers were supposed to be one of the professions AI couldn't replace. But the legal industry is discovering that many of its most ...

📺 The Infographics Show

👁️ 78K • 👍 2K • 💬 562 • ⏱️ 13:53 • 1d ago

---

**[The AI Bath Bomb Scam](https://www.youtube.com/watch?v=v7HCQ8jNFtc)**

Facebook Bath bomb companies have been creating AI-generated ads to sell products that look NOTHING like what customers ...

📺 TheAsherShow

👁️ 65K • 👍 4K • 💬 331 • ⏱️ 12:01 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 2,645,226 • ❤️ 12,453 • 10d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 7,009,063 • ❤️ 2,791 • 4d ago

---

**[Qwen3.8-27B-Uncensored-MLX](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-MLX)**

*OrcaRouter*

An uncensored, MLX-quantized 27B parameter vision-language model optimized for Apple Silicon, supporting 2-8 bit precisions. It performs image-text-to-text tasks and is intended for AI safety research and red-teaming due to its removed safety alignment.

`image-text-to-text` `4.7B`

⬇️ 57,947 • ❤️ 1,007 • 6h ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 312,627 • ❤️ 678 • 20h ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 224,114 • ❤️ 1,077 • 4d ago

---

**[Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF](https://huggingface.co/HauhauCS/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF)**

*HauhauCS*

This is an uncensored, aggressive Qwen3.8-27B multimodal model with HauhauCS FastMTP for accelerated text generation and a vision projector for image/video input. It excels at direct, fast responses and handles complex prompts without refusal, supporting up to 1M token context.

`image-text-to-text` `1.9B`

⬇️ 761,975 • ❤️ 567 • 6d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 790,378 • ❤️ 1,697 • 7d ago

---

**[Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)**

*Ornith*

Ornith-1.5-35B-A3B is a 35B Mixture-of-Experts model that activates ~3B parameters per token, excelling in coding and agentic tasks. It is built through end-to-end self-improvement, continuously generating and optimizing training tasks for enhanced performance.

`text-generation` `36.0B`

⬇️ 60,294 • ❤️ 380 • 1d ago

---

**[Qwen3.8-27B-Uncensored-GGUF](https://huggingface.co/JonathanColetti/Qwen3.8-27B-Uncensored-GGUF)**

*Jonathan Coletti*

This is an uncensored GGUF quantization of Qwen3.8-27B, optimized for reduced refusal behavior and retaining the multi-token prediction (MTP) head for enhanced generation efficiency. It supports text generation with multilingual capabilities (English, Chinese) and is compatible with llama.cpp, offering various quantization levels for different performance/resource trade-offs.

`text-generation` `27.3B`

⬇️ 1,456,700 • ❤️ 672 • 8d ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 18,065 • ❤️ 1,222 • 10d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 82 • 💬 2 • ⭐ 3,905 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 712 • 💬 5 • ⭐ 5,015 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[4DAnyone: Create Anyone in 4D from a Casual Monocular Video](https://huggingface.co/papers/2608.20335)**

*Yudong Jin, Tao Xie, Qihang Zhang et al. (9 authors)*

🏢 Ant Research

4DAnyone reconstructs 4D humans from monocular video by generating multiview-consistent videos and lifting them into 4D Gaussian Splatting, using reference and target context designs to overcome scaling bottlenecks.

▲ 72 • 💬 7 • ⭐ 586 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.20335) • [💻 code](https://github.com/ant-research/4DAnyone) • [🔗 project](https://4danyone.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 125 • 💬 6 • ⭐ 99,625 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming](https://huggingface.co/papers/2606.31227)**

*Yong Yang, Xing Zheng, Huiyu Wu et al. (10 authors)*

🏢 Tencent

AI-Infra-Guard is an open-source framework that addresses AI infrastructure security through layered detection paradigms spanning infrastructure, protocol, agent behavior, and model layers.

▲ 15 • 💬 2 • ⭐ 5,726 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.31227) • [💻 code](https://github.com/Tencent/AI-Infra-Guard) • [🔗 project](https://matrix.tencent.com/clawscan/)

---

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 18 • 💬 1 • ⭐ 2,753 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2607.05391) • [💻 code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [🔗 project](https://llm-as-a-verifier.com/)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 40 • 💬 5 • ⭐ 7,531 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 131 • 💬 3 • ⭐ 23,902 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks](https://huggingface.co/papers/2608.01964)**

*Ziyu Ma, Hailang Huang, Shun Zou et al. (8 authors)*

🏢 alibaba

LongHorizon-Harness improves long-horizon agent performance by explicitly tracking verified task states outside context via a manage-execute-audit loop.

▲ 180 • 💬 3 • ⭐ 1,195 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2608.01964) • [💻 code](https://github.com/AMAP-ML/LongHorizon-Harness) • [🔗 project](https://lh-harness.pages.dev)

---

**[EnvHarness: Awakening Static Worlds for Agent Learning](https://huggingface.co/papers/2608.19880)**

*Chengsong Huang, Zifeng Wang, Rujun Han et al. (17 authors)*

🏢 Google

EnvHarness and EnvRigger dynamically reshape static environments via programmable plugins to target agent weaknesses and improve reinforcement learning co-evolution.

▲ 258 • 💬 2 • ⭐ 307 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.19880) • [💻 code](https://github.com/google-research/envharness) • [🔗 project](https://envharness.com/)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 17.8k • 🔱 2.0k • 9h ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 14.1k • 🔱 1.7k • 2d ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.9k • 🔱 1.1k • 3d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.6k • 🔱 600 • 1h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.0k • 🔱 244 • 13d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.0k • 🔱 362 • 5h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 2.6k • 🔱 303 • 13h ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 189 • 3h ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.2k • 🔱 116 • 4h ago

---

**[ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)**

let your agent control your phone

`Python` `agent` `ai` `automation` `developer-tools`

⭐ 2.0k • 🔱 185 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
