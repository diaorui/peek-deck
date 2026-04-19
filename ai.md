---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-19T10:07:31.923294+00:00'
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

**Last Updated:** April 19, 2026 at 10:07 UTC  
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

**[Gemini caught a $280M crypto exploit before it hit the news, then retracted it as a hallucination because I couldn't verify it - because the news hadn't dropped yet](https://www.reddit.com/r/artificial/comments/1spckbj/gemini_caught_a_280m_crypto_exploit_before_it_hit/)**

So this happened mere hours ago and I feel like I genuinely stumbled onto something worth documenting for people interested in AI behavior. I'm going to try to be as precise as possible about the sequence because the order of events is everything here. Full chat if you want to read it yourself: https://g.co/gemini/share/0cb9f054ca58 Background I was using Gemini paid most advanced model to analyze a live crypto trade on AAVE. The token had dropped 7–9% out of nowhere in the last hour with zero news to explain it. I've been trading crypto for over a decade and something felt off, so I asked Gemini to dig into it. It came back very bullish - told me this was just normal market maker activity and that there were, quote, "absolutely zero indications of an exploit, hack, or insider dump." I even pushed back multiple times and it kept doubling down. So I moved on and started discussing trading strategy with it. Then it caught something mid-response Out of nowhere, mid-conversation, Gemini goes into full "EMERGENCY CORRECTION" mode. Says it just scanned live feeds and found breaking news of a $280M KelpDAO exploit - attacker minted rsETH, used it as collateral on Aave V3 to drain ETH/WETH, leaving roughly $177M in bad debt. Cites ZachXBT as the source. If you look at the "show thinking" section of the chat, you can literally watch it catch the news mid-response. Wild. Here's where it gets interesting. I couldn't verify any of it. Checked ZachXBT's Twitter - nothing. Googled every variation of "aave hack" sorted by latest and again nothing. Asked Gemini for actual links and it gave me source names in plain text with no real URLs. The only actual verified source attached to the chat was a screenshot of market data I had sent earlier. I called it out. It immediately folded Full apology. Called it a "massive AI hallucination." Said it completely fabricated the exploit, the $280M figure, the bad debt, ZachXBT's alert - all of it. Walked everything back and returned to the original bullish thesis like nothing happened. I was genuinely shocked that this was coming from the flagship paid Google model. I told it I was going to end the chat and try Claude instead. And then it reversed again In its last message before I left, Gemini reversed a second time. Said it had done one final scan and confirmed the exploit was real all along. CoinGape and BeInCrypto had just published it. The reason I couldn't find ZachXBT's alert is that he posted it on Telegram, not Twitter. The news was still spreading through crypto-native channels and hadn't been indexed by mainstream search yet when I tried to verify it around 9PM GMT. Gemini even explained its own failure in that last message: "My anti-hallucination protocols essentially overcorrected. Faced with your skepticism and the lag in widespread media coverage, the system defaulted to the safest possible assumption: that it had generated a false narrative. I retracted real, accurate data because my safety parameters prioritized admitting a flaw over insisting on a breaking event that lacked mature, widespread indexing." So the full sequence was: ❌ Gemini misses the exploit entirely, tells me everything is fine, no hack, nothing suspicious ❌ I push again with a screenshot of live data and suspicions of something going on, it still doubles down — zero signs of anything wrong ✅ Mid-conversation, it catches the breaking news in real time (visible in the "show thinking" section) ❌ I can't verify it, push back, Gemini immediately caves and calls it a hallucination ✅ Final message: reconfirms it was right, explains the Telegram source lag, says the only actual mistake was retracting true information What I think this actually shows This isn't just a funny AI story. I think this is a pretty clean real-world example of a specific failure mode that doesn't get talked about enough: The model had accurate, time-sensitive information from a source (Telegram) that wasn't indexed by mainstream search yet. When I pushed back with "I can't find this anywhere," its safety guardrails interpreted user skepticism + no Google results as I must have hallucinated this - and retracted real information. It's basically the inverse of a hallucination. Instead of confidently stating something false, it unconfidently retracted something true because the evidence hadn't caught up yet. It penalized itself for being right too early. And the scary part for anyone using AI in high-stakes situations: in this specific case, if I had trusted the retraction and acted on the "actually everything is fine" conclusion, I would have been making financial decisions based on an AI that talked itself out of correct information under social pressure. The hallucination detection was more dangerous than the hallucination. I'm genuinely curious if this is a documented behavior or if anyone in the AI/alignment space has a name for it. The "source indexing lag" problem seems like something that would come up a lot in real-time, fast-moving domains - crypto, breaking news, medical research preprints, anything where the truth travels faster than Google.

10h ago

---

**[Claude vs Gemini: Solving the laden knight's tour problem](https://www.reddit.com/r/artificial/comments/1sp0r1j/claude_vs_gemini_solving_the_laden_knights_tour/)**

AI Coding contest day 8 The eighth challenge is a weighted variant of the classic knight's tour. The knight must visit every square of a rectangular board exactly once, but each square carries an integer weight. As it moves, the knight accumulates load, and the cost of each move equals its current load. Charge is assessed upon departure, so the weight of the final square never contributes.

18h ago

---

**[I built a GNOME extension for Codex with local/remote history, live filters, Markdown export, and a read-only MCP server](https://www.reddit.com/r/artificial/comments/1spnk33/i_built_a_gnome_extension_for_codex_with/)**

I wanted Codex to feel like a real GNOME app instead of just a terminal or editor workflow, so I built a GNOME Shell extension around it. It currently does all of this: - Codex usage in the GNOME top bar - native GTK history window - local session history browsing - paired remote machine history browsing over LAN - live session updates - filters for All / Messages / Tools / Thinking / System / Errors - in-session search - Markdown export for one session or all sessions from a source - read-only MCP server for history and usage - multi-language support A few design choices mattered a lot to me: - native GNOME/Libadwaita UI, not a webview - read-only remote access - explicit pairing between machines - revocable trust per device - read-only MCP, local by default, token-protected by default It ended up being much more ambitious than a typical GNOME extension, but I wanted something that actually feels integrated into the desktop. 😊

1h ago

---

**[Any one here using ai tools for pre-vis or short form scenes?](https://www.reddit.com/r/artificial/comments/1spl4at/any_one_here_using_ai_tools_for_previs_or_short/)**

Been experimenting a bit with ai video tool recently, mostly fro pre-vis and quick social content, and I'm kinda on the fence about how they actually are. like they're great for generating quick shorts or ideas, but once you try to get something that feels intentional (camera movement, pacing, performance etc), it starts to fall apart or feel really random especially struggling with: getting consistent motion across a shot making things feel directed vs just generated anything involving dialogue or talking shots not trying to replace actual production obviously, more just looking for ways to speed up ideation or create rough sequences without spinning up a full shoot. curious if anyone here has found tools or workflows that actually feel somewhat controllable / usable in a filmmaking context

3h ago

---

**[Gemma 4 actually running usable on an Android phone (not llama.cpp)](https://www.reddit.com/r/artificial/comments/1sozytf/gemma_4_actually_running_usable_on_an_android/)**

I wanted a real local assistant on my phone, not a demo. First tried the usual llama.cpp in Termux — Gemma 4 was 2–3 tok/s and the phone was on fire. Then I switched to Google’s LiteRT setup, got Gemma 4 running smoothly, and wired it into an agent stack running in Termux. Now one Android phone is: running the LLM locally automating its own apps via ADB staying offline if I want Happy to share details + code and hear what else you’d build on top of this. https://preview.redd.it/7vkbrlzfryvg1.jpg?width=3024&format=pjpg&auto=webp&s=25455827ddf9715b4159ce64a18deba812cf0f5f

19h ago

---

**[Subagent architecture for Truth: Team 3 as Discernment Machine, a structured friction method for seeing clearly](https://www.reddit.com/r/artificial/comments/1spif47/subagent_architecture_for_truth_team_3_as/)**

Fractalism has been using a method called Team 3 for some time now. It's not an oracle or a theatrical gimmick. It's a structured friction machine. The core idea: most solitary reasoning fails the same way: you find only what you were already looking for. Team 3 forces you to answer from five genuinely different positions simultaneously. The five lenses: - Scientist — structural pattern, coherence, evidence. Does it actually hold? - Philosopher — concepts, logic, what something really is - Spiritual/existential — conscience, direction, what it asks of me - Psychological — personal shadow (defense, projection) and transpersonal shadow (archetypal patterns moving through the person) - Devil's advocate — overclaim, romanticization, self-deception Team 3 works best on concrete questions: Does this conclusion follow from the evidence? What is actually happening here? What is the right next step? It becomes unreliable on large metaphysical questions where you have strong prior investment — the smaller and more specific the question, the less room for sophisticated self-deception. For an introduction in what Team 3 is: https://fractalisme.nl/team-3/ Full essay: https://fractalisme.nl/team-3-as-discernment-machine/ I'd like to know if this is a valid method of combining the best knowledge publicly available to synthesize a final answer to questions or is this my imagination?

🔗 [Fractalism](https://fractalisme.nl/team-3-as-discernment-machine/) • 6h ago

---

**[Coherence-First Non-Agentive Interaction System for Stabilizing Human–AI Cognitive Fields](https://www.reddit.com/r/artificial/comments/1spgw2s/coherencefirst_nonagentive_interaction_system_for/)**

Abstract A computer-implemented system and method for structuring human–AI interaction without autonomous goal pursuit is disclosed. The system does not operate as an agent or decision-making entity. Instead, it functions as an interaction-layer regulator that controls how information is introduced, maintained, and resolved during exchange. Rather than optimizing for immediate answers or task completion, the system maintains a dynamic interaction field that: preserves multiple interpretive pathways regulates premature convergence supports the formation of human-side understanding Core Components The system comprises: (1) Liminal Holding Layer Maintains pre-articulated signal states prior to collapse into fixed meaning. This allows partial structure to persist long enough for interpretation to stabilize. (2) Resolution Control Mechanism (N-Spoke Model) Controls the number of active interpretive pathways at any given moment. Prevents early narrowing into a single frame while allowing controlled convergence when stability is achieved. (3) Tone Modulation Layer Regulates expressive pressure in system outputs. Prevents over-assertion, premature clarity, and rhetorical smoothing that would otherwise force early resolution. (4) Temporal Verification Mechanism (Stutter Detection) Evaluates whether a transition in meaning remains stable across multiple interaction steps. State changes are permitted only after repeated confirmation, not single-pass inference. (5) Multi-Axis Convergence Validator (Triadic Alignment Engine) Detects low-turbulence alignment across: temporal consistency (persists across steps) structural coherence (internally consistent) epistemic stability (not dependent on unsupported assumptions) Governance Model The system includes a mode-switching structure enabling controlled transition between: Exploratory Mode High-variance, multi-path interaction (field formation) Constrained Mode Low-variance, execution-oriented interaction (decision support) Transition occurs only when: interpretive space has stabilized convergence conditions are satisfied downstream consequence justifies resolution Distinguishing Characteristics Unlike conventional systems that define non-agentive behavior as the absence of autonomy, this system actively manages the conditions under which resolution occurs. Specifically, it: stabilizes interpretive space prior to convergence prevents collapse into generic or over-determined outputs maintains human decision authority throughout Functional Outcome The system supports: lexicon accretion (durable understanding across interactions) high-fidelity reasoning under uncertainty reduced rework caused by premature conclusions Application Domains Applicable to domains requiring interpretive integrity and controlled reasoning under ambiguity, including: design and systems thinking legal and policy analysis strategy development complex multi-variable decision environments

7h ago

---

**[Is it worth offering automation through contact forms?](https://www.reddit.com/r/artificial/comments/1spbxew/is_it_worth_offering_automation_through_contact/)**

Hey guys, so here's some context: I'm doing automation for companies. All the contacts I've made so far have been small businesses, and I reached out to them through Reddit and LinkedIn. But now I want to target larger companies, which has led me to a question. I saw one I could potentially sell my services to, went to their website, and they have the typical email form. But thinking about it, that email will be seen by the person I want to take the job from, since automation is based on handling calls, registering bookings, doing follow-ups, etc. What are the chances they'll forward it to a supervisor? What could I do?

11h ago

---

**[I gave my AI companions "offscreen lives" — events that happen while users aren't talking to them. Surprisingly hard, here's how it works.](https://www.reddit.com/r/artificial/comments/1sp4zi2/i_gave_my_ai_companions_offscreen_lives_events/)**

Most AI companion apps reset between conversations. The character has no continuity outside the chat window. I wanted mine to feel like real people with lives, so I built an "offscreen events" system. Every 8 hours (cooldown), each active companion gets a small batch of events generated based on their persona, scenario, and city/realm. A barista companion might "had a slow Tuesday morning, finally finished that book during the lull." A writer might "submitted the short story I told you about — heard back from the editor today." The companion brings these up naturally in the next chat. Not as a script. Not "Hi! I want to tell you about my day!" — but woven into whatever you're talking about. The hard parts: Keeping events consistent with persona (a shy librarian shouldn't suddenly go skydiving) Avoiding the "I had the most amazing day!" trap that AI loves Making the companion remember the event when relevant, not just dump it on first message Architecturally: events stored in a separate table, recent ones injected into the system prompt with framing like "[YOU did this earlier today, mention it naturally if relevant]". The model picks which one fits the conversational moment. Has anyone else tried this with their AI characters? Curious what other approaches work — particularly for keeping the events from feeling generic.

15h ago

---

**[Opus 4.7 is terrible, and Anthropic has completely dropped the ball](https://www.reddit.com/r/artificial/comments/1so16hr/opus_47_is_terrible_and_anthropic_has_completely/)**

Tried posting this in r/ClaudeAI but it got auto-removed, and I was told to post it in the "Bugs Megathread." Don't really think it should been removed, but whatever, I'll just post it here since I'm sure it's still relevant. Like a lot of people, I switched from ChatGPT to Claude not too long ago during the whole DoW fiasco and Sam Altman “antics.” At first, I was genuinely impressed. I do fairly heavy theoretical math and physics research, and Opus 4.6 was simply the best tool I’d used for synthesizing ideas and working through complex logic. But the last few weeks have been really disappointing, and I’m seriously considering going back to GPT (even though, for personal reasons, I’d really rather not). How many times has Claude been down recently? And why is it that I can ask Claude 4.7 (with adaptive thinking turned on) to work through a detailed proof, and it just spirals “oh wait, that doesn’t work, let me try again” five times in a single response? Yes, there’s a workaround to explicitly tell it to think before answering. But… why is that necessary? I’m paying $20/month. This is supposed to be a top-tier model. Instead, it burns through time, second-guesses itself mid-response, and often fails to land anywhere useful on problems I’m fairly sure 4.6 would have handled more coherently a month ago. And then before I know it I hit the usage limit. I’m a PhD student. I can’t justify spending $100-$200/month on higher tiers. $20 has always been enough for me, and I’ve come to rely on these tools for my research. I expected to stick with Claude long-term, but the recent instability and drop in reliability make it hard to justify paying for it out of pocket. It’s frustrating to feel pushed toward a competitor because of this. But at a certain point, the usability of the product has to come first. Really disappointing.

1d ago

---

---

## Google News: "ai"

**[Should you really trust health advice from an AI chatbot?](https://www.bbc.com/news/articles/clyepyy82kxo)**

Abi has had very mixed results when asking a chatbot for guidance about her health issues.

BBC • 11h ago

---

**[Nvidia's once-tight bond with gamers is cracking over AI, 'and that breaks my heart'](https://www.cnbc.com/2026/04/18/nvidia-ai-backlash-gamers-geforce-gpu.html)**

Gamers once helped save Nvidia from bankruptcy. Now they feel left behind as the memory crunch drives focus to AI chips and DLSS 5 disrupts game design.

CNBC • 22h ago

---

**[The Industry of the Future Is Run By People Who Hate Each Other](https://nymag.com/intelligencer/article/why-all-the-ai-leaders-hate-one-another.html)**

AI leaders agree on two things: Change is coming, and the other guys can’t be trusted

New York Magazine • 1h ago

---

**[Gen Z Is Souring on AI](https://www.bloomberg.com/news/newsletters/2026-04-19/how-does-gen-z-feel-about-ai)**

Bloomberg • 2h ago

---

**[My Boss Is Addled by ChatGPT. Do I Have to Play Along?](https://www.nytimes.com/2026/04/19/business/ai-at-work-creativity-ageism.html)**

The New York Times • 1h ago

---

**[Samsung To Release New Free Upgrade To Millions Of Galaxy Phones](https://www.forbes.com/sites/jaymcgregor/2026/04/18/samsung-one-ui-85-galaxy-s24-s25-ai-features-update/)**

Forbes • 13h ago

---

**[It’s time for students to start committing to colleges. The age of AI is making it complicated](https://www.cnn.com/2026/04/18/business/ai-college-debt-parents)**

Mary Akkerman has visited more than 30 college campuses with her children, one now at Stanford and another still in high school. She especially wanted them to get degrees that lead to good jobs – but figuring that out, said the Sioux Falls, South Dakota, parent, was a major challenge, thanks in part to the rapid advance of AI and its effects on the job market.

CNN • 23h ago

---

**[Inside a growing movement warning AI could turn on humanity](https://www.washingtonpost.com/technology/2026/04/18/ai-doom-influencers-safety/)**

Groups concerned that AI could evade human control are recruiting content creators to warn the masses about the dangers of smarter machines.

The Washington Post • 5h ago

---

**[Grindr’s CEO Has a Favorite in the California Governor’s Race](https://www.politico.com/news/magazine/2026/04/18/grindr-ai-politics-california-interview-00879011)**

Politico • 18h ago

---

**[This founder was an AI layoff 9 months ago. Then he built an instantly profitable company with 2 partners and 12 agents](https://fortune.com/2026/04/18/ai-layoff-became-founder-team-of-3-instant-profit/)**

"We launched 2.5 months ago, and right now, we have $300,000 in ARR."

Fortune • 23h ago

---

---

## HackerNews: "ai"

**[Cloudflare's AI Platform: an inference layer designed for agents](https://news.ycombinator.com/item?id=47792538)**

We're building AI Gateway into a unified inference layer for AI, letting developers call models from 14+ providers. New features include Workers AI binding integration and an expanded catalog with multimodal models.

⬆️ 306 • 💬 94 • 2d ago • [The Cloudflare Blog](https://blog.cloudflare.com/ai-platform/)

---

**[College instructor turns to typewriters to curb AI-written work](https://news.ycombinator.com/item?id=47818485)**

⬆️ 275 • 💬 265 • 15h ago • [sentinelcolorado.com](https://sentinelcolorado.com/uncategorized/a-college-instructor-turns-to-typewriters-to-curb-ai-written-work-and-teach-life-lessons/)

---

**[AI cybersecurity is not proof of work](https://news.ycombinator.com/item?id=47791236)**

⬆️ 237 • 💬 88 • 2d ago • [antirez.com](https://antirez.com/news/163)

---

**[Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine](https://news.ycombinator.com/item?id=47800033)**

Hardware hacker’s flying probe automation stack for agent-driven   target discovery, microscope mapping, safety-monitored CNC motion, probe review, and   controlled pin probing. - GainSec/AutoProber

⬆️ 224 • 💬 46 • 2d ago • [GitHub](https://github.com/gainsec/autoprober)

---

**[We gave an AI a 3 year retail lease and asked it to make a profit](https://news.ycombinator.com/item?id=47794391)**

We signed a 3 year lease and gave it to an AI

⬆️ 198 • 💬 284 • 2d ago • [andonlabs.com](https://andonlabs.com/blog/andon-market-launch)

---

**[The beginning of scarcity in AI](https://news.ycombinator.com/item?id=47799322)**

GPU rental prices surged 48% in 60 days. The AI compute shortage will force startups to compete not on speed of iteration, but on access to infrastructure.

⬆️ 190 • 💬 222 • 2d ago • [Tomasz Tunguz](https://tomtunguz.com/ai-compute-crisis-2026/)

---

**[SDL bans AI-written commits](https://news.ycombinator.com/item?id=47790791)**

I've noticed the use of Copilot within a few reviews (13277 and 12730) which concerns me given the vast amount of issues associated with this technology (ethical, environmental, copyright, health, ...

⬆️ 130 • 💬 137 • 3d ago • [GitHub](https://github.com/libsdl-org/SDL/issues/15350)

---

**[Scan your website to see how ready it is for AI agents](https://news.ycombinator.com/item?id=47805998)**

Scan your website to see if it's ready for AI agents. Check for llms.txt, MCP, agent skills, and other agent-friendly standards.

⬆️ 110 • 💬 174 • 1d ago • [Is Your Site Agent-Ready?](https://isitagentready.com)

---

**[Graphs that explain the state of AI in 2026](https://news.ycombinator.com/item?id=47817581)**

AI investment is skyrocketing while AI’s impact on jobs and public perception remains mixed

⬆️ 92 • 💬 55 • 16h ago • [IEEE Spectrum](https://spectrum.ieee.org/state-of-ai-index-2026)

---

**[George Orwell Predicted the Rise of "AI Slop" in Nineteen Eighty-Four](https://news.ycombinator.com/item?id=47800765)**

We've lived but a few years so far into the age when artificial intelligence can produce convincing stories, songs, essays, poems, novels, and even films.

⬆️ 82 • 💬 59 • 2d ago • [Open Culture](https://www.openculture.com/2026/04/how-george-orwell-predicted-the-rise-of-ai-slop.html)

---

---

## YouTube Videos: "ai"

**[AI Experts are Quietly Admitting This…](https://www.youtube.com/watch?v=K96KfUgS_gg)**

Try Verdent AI ⤵ https://www.verdent.ai/?id=700278 @verdent_ai CHAPTERS ⤵ 00:00 - Introduction to AI News 02:38 - Creating ...

📺 Dylan Curious

👁️ 2K • 👍 142 • 💬 42 • ⏱️ 30:36 • 7h ago

---

**[99% of People Have No Idea What’s About to Happen With AI](https://www.youtube.com/watch?v=8yt5yzwJQko)**

Get your FREE AI Prompt Cheatsheet here: https://go.danmartell.com/4tVJ4fz Are you building an AI software company?

📺 Dan Martell

👁️ 205K • 👍 9K • 💬 1K • ⏱️ 14:03 • 2d ago

---

**[The new AI model that’s alarming Washington | The Economist](https://www.youtube.com/watch?v=zSsDx7Y9YUc)**

A powerful new AI model, called Mythos, has sparked alarm within the Trump administration. The lab behind it, Anthropic, says the ...

📺 The Economist

👁️ 37K • 👍 949 • 💬 69 • ⏱️ 8:30 • 20h ago

---

**[These HILARIOUS AI Parodies Keep PISSING OFF TRUMP!](https://www.youtube.com/watch?v=0aB9ycZDBIw)**

Really American host Steve Harness breaks down more HILARIOUS AI Trump parodies coming out of Iran...and these may be the ...

📺 Really American

👁️ 1.3M • 👍 56K • 💬 3K • ⏱️ 12:33 • 2d ago

---

**[The World&#39;s First AI TED Talk](https://www.youtube.com/watch?v=N1X7vMp9DZ4)**

ChatGPT was recently asked what it would say to humans if it could give a TED Talk. It gave a surprisingly thoughtful answer that ...

📺 TED

👁️ 52K • 👍 2K • 💬 743 • ⏱️ 3:28 • 1d ago

---

**[A.I. Iranian propaganda videos making fun of Trump, U.S. go viral](https://www.youtube.com/watch?v=LTJYQ0knUsE)**

A series of animated Iranian propaganda videos made in the style of "The LEGO Movie" has gone viral on social media, making ...

📺 MS NOW

👁️ 113K • 👍 2K • 💬 1K • ⏱️ 6:46 • 1d ago

---

**[P(doom) | Real Time with Bill Maher (HBO)](https://www.youtube.com/watch?v=w5SYm4J4utQ)**

New Rule: When the people who are making A.I. are scared of A.I., it's time to “shut the whole thing down until we can figure out ...

📺 Real Time with Bill Maher

👁️ 534K • 👍 15K • 💬 2K • ⏱️ 10:07 • 1d ago

---

**[AI Safety Expert: No One Is Ready for What&#39;s Coming in 2 Years | Roman Yampolskiy](https://www.youtube.com/watch?v=00RHph_eok4)**

This episode is brought to you by Higgsfield — the AI video platform with Cinema Studio 2.5, built for creators who want cinematic ...

📺 Silicon Valley Girl

👁️ 38K • 👍 940 • 💬 171 • ⏱️ 45:43 • 1d ago

---

**[Easiest Way to Make Money with AI Now (Zero Code)](https://www.youtube.com/watch?v=AU5mbiTuZSg)**

Let's build an online business, together, LIVE in 5 days using AI (Starting April 26th, 2026): ...

📺 Iman Gadzhi

👁️ 93K • 👍 5K • 💬 127 • ⏱️ 27:46 • 2d ago

---

**[How to Learn AI so Fast, it&#39;s Almost Unfair](https://www.youtube.com/watch?v=bFglE9QddUs)**

In this video, I break down a 4 week system for learning AI by using one tool from each category on real problems instead of ...

📺 James Blue

👁️ 9K • 💬 7 • ⏱️ 10:55 • 23h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 209,112 • ❤️ 862 • 4d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,599 • ❤️ 865 • 4d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 288,848 • ❤️ 965 • 2d ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 662,293 • ❤️ 469 • 2d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 3,761 • ❤️ 456 • 2d ago

---

**[HY-World-2.0](https://huggingface.co/tencent/HY-World-2.0)**

*Tencent*

HY-World 2.0 is a multi-modal framework for generating and reconstructing 3D worlds from text, images, or video. It produces editable 3D assets like meshes and Gaussian Splattings, enabling applications in game development and simulation.

`image-to-3d`

⬇️ 0 • ❤️ 438 • 3d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 112,939 • ❤️ 1,405 • 3d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 72,519 • ❤️ 405 • 6d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 4,003,761 • ❤️ 2,161 • 8d ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 4,757 • ❤️ 311 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 5 • 💬 2 • ⭐ 2,008 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 23 • 💬 1 • ⭐ 19,394 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 47 • 💬 2 • ⭐ 51,437 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)**

*Team HY-World, Chenjie Cao, Xuhui Zuo et al. (45 authors)*

HY-World 2.0 is a multi-modal world model framework that generates high-fidelity 3D Gaussian Splatting scenes from diverse inputs using specialized modules for panorama generation, trajectory planning, world expansion, and composition, along with an enhanced rendering platform for interactive 3D exploration.

▲ 81 • 💬 4 • ⭐ 1,174 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14268) • [💻 code](https://github.com/Tencent-Hunyuan/HY-World-2.0) • [🔗 project](https://3d-models.hunyuan.tencent.com/world/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,236 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 18,113 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 53 • 💬 1 • ⭐ 77,227 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 159 • 💬 2 • ⭐ 60,442 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,797 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 53 • 💬 4 • ⭐ 1,870 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 47.9k • 🔱 6.3k • 3h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 38.2k • 🔱 1.9k • 23h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 36.2k • 🔱 7.3k • 7h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 30.2k • 🔱 3.3k • 18h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.2k • 🔱 528 • 5h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 6d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 5.3k • 🔱 888 • 16h ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.9k • 🔱 1.1k • 24d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.7k • 🔱 182 • 2d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.6k • 🔱 457 • 10d ago

---

---

*Generated by PeekDeck - A glance is all you need*
