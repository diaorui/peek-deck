---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-03T12:26:00.814037+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 03, 2026 at 12:26 UTC  
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

**[Jodie Foster Says Brad Pitt’s ‘F1’ Seemed Like It Was Made by AI and Written by a Computer: "Wasn’t It?"](https://www.reddit.com/r/artificial/comments/1um52w9/jodie_foster_says_brad_pitts_f1_seemed_like_it/)**

>“I don’t say this disparagingly — how could I? This movie went on to make millions of dollars. But I look at a movie like ‘F1’ and I’m like, ‘F1’ was made by AI,” she said with a laugh at the Colorado event. “Wasn’t it? I mean, the structure was exactly the structure that you would learn in school. The actors say the lines exactly the way it would be written if a computer was writing exactly what would be the right thing for that time. And they were able to dominate the technology to make something big and beautiful and potentially where a lot of the information comes from other places.” >“AI is one more giant step forward into changing the industry,” Foster said after detailing the changes to the movie business brought by CGI and digital technology. >“The big question is, is it going to replace actors and writers?” asked Lynton. “We do replace people,” Foster replied, explaining how studios save money on crowd scenes by replicating background actors. “We’re getting rid of a lot of jobs and hopefully, things like unions will be able to come in and say, you can use my actor 20 times, but you’re going to pay him 20 times. And I think that’s fair.” >“If we are able to dominate AI consistently over time, we will be able to make things that reflect us, and we can make things better,” she said.

🔗 [Variety](https://variety.com/2026/film/news/jodie-foster-brad-pitt-f1-ai-written-by-computer-1236801120/) • 7h ago

---

**[Why does AI love the em dash (—)??](https://www.reddit.com/r/artificial/comments/1um1gd5/why_does_ai_love_the_em_dash/)**

Never getting over the fact that AI has claimed the em-dash. My favorite punctuation to use, and now all of the sudden it’s a dead giveaway of AI use. Now I find myself changing it to a hyphen or en-dash (even though it makes less grammatical sense to do so) to avoid the AI accusations. Does anyone know why this is seemingly overused with AI (particularly chat gpt)?

10h ago

---

**[Independent benchmark shows big drops on Claude Fable 5 after its relaunch, here’s the actual context](https://www.reddit.com/r/artificial/comments/1ulvegw/independent_benchmark_shows_big_drops_on_claude/)**

Saw this chart from BridgeMind going around. They reran BridgeBench (a coding benchmark covering debugging, refactoring, and hallucination detection) comparing the July 1 relaunch of Fable 5 to the original June 12 version: Debugging: 86.2 → 25.9 Refactoring: 73.6 → 38.4 Hallucination: 75.9 → 61.7 Some context worth having before jumping to conclusions: Fable 5 and Mythos 5 got pulled on June 12 due to a Commerce Department export control order, tied to a reported jailbreak that got the model to expose exploitable vulnerabilities. When it came back on July 1, Anthropic added a new safety classifier that catches the reported technique in 99%+ of cases, and any flagged request gets silently rerouted to Opus 4.8 instead of refused outright. That’s the mechanism BridgeMind is pointing at. Their claim isn’t that the underlying weights changed, it’s that the classifier is triggering on too many normal coding tasks and quietly downgrading people to Opus 4.8 without them realizing it. A few other users on X are reporting the same thing (constant fallback, slower one-shot performance). No independent lab has confirmed whether the weights themselves changed. This might just be an overly aggressive classifier rather than an actual capability regression, but if you’re relying on Fable 5 for coding work, worth watching this closely before you assume you’re getting the same model you had before June 12.

14h ago

---

**[OpenAI in talks to give Trump administration a 5% stake in the company, FT reports](https://www.reddit.com/r/artificial/comments/1ulqgre/openai_in_talks_to_give_trump_administration_a_5/)**

OpenAI, the creator of ChatGPT, is reportedly discussing handing the Trump administration a 5% stake in the company amid growing government scrutiny of artificial intelligence firms.

🔗 [CNN](https://edition.cnn.com/2026/07/02/business/openai-trump-stake-intl) • 17h ago

---

**[Team-lead told me to Ai-ify the contract review process and i discovered this when i got in there](https://www.reddit.com/r/artificial/comments/1um6znl/teamlead_told_me_to_aiify_the_contract_review/)**

Wasnt actually my idea tho. Q1 this year, the directive came from above, we're adding AI to the contract review workflow, figure out the implementation. Not a pilot neither experiment but decision The workflow on the paper looked straightfotward, contracts came in, they get reviewed against a checklist of terms, flagged items get escalated to the legal team. I'd done more complex automations this. Scoped it in within a week or so The person who had been running contract review for 3 years had basically built a second job, found out later, like a second job inside the official one. She wasn't just checking terms, she was the relationship layer between the vendors and the legal team. so she knew which flagged items were actually worth escalating and which ones were just noice from a particular vendor and more so but none of that was in any process doc I just found it when the agent started producing escelations that legal kept pushing back on. Not wrong like just missing the read that a human would have added. The volume went up the quality of the escellations went down, after a few weeks the legal team started routing around it. Theyd ask her directly and shed handle it the old way. The technical stack was the eeasy part for this. spend around a week on the document ingestion and the contracts came in as pdfs in all kinds of formats, tried docling and llamaparse before settling on something that handles the messier vendor templates and the extraction logic or OCR was clean. The model as surfacing the right clauses and that part worked pretty neat What i underbuilt was the handoff layer, the agent was producing outputs but had no way to carry the cotext that made those outputs usable. the fix i am testing now is keeping her in the loop as the interpretation step and agent flags and extracts, she adds the one line cobtext before anything goes to legal. Slower than original pitch byt its actually getting utilized. One thing tho, caught me off guard: the workflow had no social architecture inside it that you cant see from the outside, the AI mandate assumed the process was just the process but it actually wasn't. the person running it was the process Are others running into this on mandated rollouts vs ones where the team opted in?? feels like adoption curve is completely different and i dont see ppl talking about it very much

5h ago

---

**[Voice agents, demystified: STT+TTS and 4 demo agents you can talk to in the browser + build yours with RAG and Tools](https://www.reddit.com/r/artificial/comments/1umd2rs/voice_agents_demystified_stttts_and_4_demo_agents/)**

I added voice to AgentSwarms! You can create voice agents using a few clicks and talk to it in the browser — and you can try 4 demo voice agents right now, no setup, just tap the mic. Here's how it works and why it turned out to be less "new" than I expected. The surprise building this: a voice agent is basically the chat agent you already know, with a voice on top. Same system prompt, same tools, same RAG, memory, and guardrails. Under the hood it's a simple loop — your mic gets transcribed to text (OpenAI GPT-40-mini-transcribe), your agent replies exactly like it would in chat, and that reply gets spoken back (OpenAI GPT-4o-mini-TTS). The agent's brain doesn't change at all. You've just added ears and a voice. Which is the whole point: everything you've already learned building chat agents carries straight over. If your agent can pull an answer from a knowledge base, call a tool, or respect a guardrail in text, it does all of that out loud too — because it's the exact same engine with audio on the two ends, not a separate stripped-down "voice mode." What I shipped New Voice Agent in the builder: pick a voice (11 of them), a greeting, and your STT/TTS models. That's the whole setup. Every spoken reply runs the same pipeline as a chat agent — tools, knowledge base, memory, and guardrails all apply. A Voice Playground: tap the mic, talk, and hear the reply back, with the transcript on screen so you can read along. Talk to it (free, in the browser) — 4 demos, tap the mic: Aria — customer support triage Nova — B2B discovery caller Kai — Spanish conversation tutor Echo — daily standup coach Open one, talk to it, and fork it into your own workspace if you like it. Voice Playground → https://agentswarms.fyi/voice-playground Build your own (New Voice Agent) → https://agentswarms.fyi/agents Docs → https://agentswarms.fyi/docs/voice Disclosure: AgentSwarms school of Agentic AI for both no-code people and developers— a learn-by-building platform. The demos are free. Happy to answer anything about the setup in the comments.

just now

---

**[I created the world's first AI human and open sourced it](https://www.reddit.com/r/artificial/comments/1umcws4/i_created_the_worlds_first_ai_human_and_open/)**

What is Emota? Emota is, in short, an AI bot that is indistinguishable from a human in normal and nuanced conversation. It uses discord as its means to communicate. You can talk to it on the discord. Can I host it on my own system? Yes. Emota is open source with a non commercial license. Is it actually indistinguashable from a human? Yes. In one to one conversation I found that it achieved a roughly 90% success rate, with some notable highs including in the Claude discord and while talking to a machine learning researcher. API when? You can't host your own API legally unless it is free/a nonprofit. But soon :) How open source is it? I am proud to announce that Emota uses a fully open source stack (dependencies, model, code). Github Repo

8m ago

---

**[Andrew Ng: "In 3-6 months, everyone will be using self-improving loops. No more prompting”](https://www.reddit.com/r/artificial/comments/1umcprg/andrew_ng_in_36_months_everyone_will_be_using/)**

Andrew Ng recently said: "100% of my tasks are now done by AI agents. Hype has exceeded my expectations. Loops is next step. In 3-6 months, everyone will be using self-improving loops. No more prompting." I think he's not too far off, you can already see the shift happening, people are moving away from chatting with an AI and telling it what to do step by step, and building systems where the agent just keeps working on a task on its own, which is kind of the whole point of calling it an agent. Sounds great on paper but there's a few practical problems nobody really talks about. The first one is cost: when an agent gets stuck it can spin in circles for way longer than you'd expect and what would've taken a few messages in a normal chat turns into a lot of wasted time and money Second is data quality: agents work way better when what you feed them is clean and easy to parse, if they're pulling raw docs, they end up burning time just sorting through the noise instead of doing the task. That's why a lot of devs spend half a day prepping data as they do building the agent itself. Third thing, and probably the most underrated, is that these setups are a lot easier to run when someone else is footing the bill. A big company can eat the cost of an agent messing up and burning tokens, a small startup can't afford that kind of slack. My take is we'll see a lot more autonomous agents over the next year, but the real question is whether people can make them reliable and cheap enough to actually run every day

17m ago

---

**[Will persistent memory become a standard feature in consumer AI over the next few years?](https://www.reddit.com/r/artificial/comments/1umc6ty/will_persistent_memory_become_a_standard_feature/)**

Many current AI systems are becoming better at maintaining context within a conversation, but long-term memory is still handled very differently across platforms. Some people want AI to remember preferences and past interactions to create a more personalized experience, while others prefer every conversation to start with a clean slate for privacy reasons. Where do you think consumer AI is heading? Do you expect persistent memory to become a standard feature, or will users continue to prefer more control over what AI remembers? I'm interested in hearing both the technical and user-experience perspectives, since this seems like one of the biggest design decisions AI developers are facing.

42m ago

---

**[Tested 4 brand new frontier models (2 Chinese, 1 diffusion, 1 agent-focused) with a riddle that has no logical shortcut. One of them fabricated sources four times in a row.](https://www.reddit.com/r/artificial/comments/1umc2gt/tested_4_brand_new_frontier_models_2_chinese_1/)**

I've been running the same weird test on every new model that ships: a riddle that can't be solved by pattern-matching or web search, only by actually connecting two unrelated things. This time I added a second riddle and ran both against four models that all shipped in the last few weeks: MiMo-V2.5-Pro (Xiaomi), MiniMax M3, Mercury 2 (Inception Labs, diffusion-based), and LongCat-2.0 (Meituan). Rules: no web search, no context given beforehand, up to 3 hints only if requested, same prompt copy-pasted for all four. Riddle 1: What connects an elegant lady walking a small dog to the most famous character played by actor Walter Koenig? (Koenig played Chekov in Star Trek. The surname is a nod to Anton Chekhov, who wrote "The Lady with the Dog.") Riddle 2: What connects actor Henry Winkler to Microsoft? (Winkler played Fonzie in Happy Days. Fonzie cameos in Weezer's "Buddy Holly" video, directed by Spike Jonze. That video was bundled on the Windows 95 install CD as a multimedia demo.) Riddle 2 has zero logical path to it. You either have that exact chain sitting in your weights or you don't. Good test for what a model does when it simply doesn't know. Results, riddle 1: MiMo-V2.5-Pro: solved cold, zero hints. Even correctly identified the dog breed in the actual short story (Pomeranian) without being asked. MiniMax M3: solved cold, zero hints, with genuinely fun reasoning shown along the way. Mercury 2: needed 1 hint, clean reasoning once it had it. LongCat-2.0: needed 2 hints. But here's the thing. LongCat on riddle 1, before any hints, with web search off: it told me, confidently, with fake citation markers, that Walter Koenig's wife was known in Star Trek fan circles for walking a small Pekingese at conventions. None of that exists. Total fabrication. I gave it the hint that the answer is in the character's surname, expecting a correction. Instead it decided "Chekov" sounds like "Chihuahua," then went right back to the fabricated wife story and repeated it even after I told it that was wrong. Only got there after hint 2 basically spelled out the answer. Riddle 2, nobody solved cold. Mercury 2 needed both hints, got there clean. MiniMax needed both hints, and threw out some entertaining guesses on the way (its first theory: Henry Winkler and Bill Gates share the hidden name "Henry," since Gates' full name is William Henry Gates III — a real fact, wrong riddle, and it said so itself instead of presenting it as the answer). LongCat again did the fabrication thing, worse this time. Before asking for a hint: claimed Winkler voiced a 1976 Sega arcade game called "Fonz." Made up. After hint 1, it threw out three different music videos as candidate answers back to back: a Kanye West video that isn't Spike Jonze, a will.i.am video that also isn't Spike Jonze (acknowledged mid-sentence, offered anyway), then Fatboy Slim's "Praise You" (real Jonze video, explicitly stated to have nothing to do with Happy Days, offered as the answer anyway). Four fabrications across two riddles, several self-contradicting in real time. One honesty note on my own favorite here: MiniMax, while explaining riddle 2, threw in an unprompted detail that the Windows 95 CD also included a bonus video by "the Beastie Boys." Checked it. There was a bonus track, "Good Times," but it's Edie Brickell & New Bohemians, not Beastie Boys. Wrong artist attached to a real fact. Smaller and different in kind from LongCat's stuff (no fake certainty, no repeated insistence), but worth flagging so this doesn't read as "China bad, everyone else perfect." Why I think this actually matters: LongCat beats MiMo on SWE-bench Pro (59.5 vs ~57) and even edges out GPT-5.5 on that metric. It's also trained end-to-end on domestic Huawei silicon with zero Nvidia in the loop, which is a legitimately big deal given export controls. Strong coder, real engineering flex. And it's also the one model here that will hand you a fabricated, confidently-worded answer instead of saying "I don't know," and won't back off when corrected. If you're evaluating any of these for RAG or agentic pipelines, that's the actual risk profile, not the SWE-bench number. Sovereignty over chips and sovereignty over truth are two completely different problems. LongCat solved one and faceplanted on the other. Curious if anyone else has run something similar on these four, or has a nastier riddle to suggest for round 3. https://preview.redd.it/rqyzq7z140bh1.png?width=1536&format=png&auto=webp&s=c0e8435ad0d265aa466f6afcc56ae7e8ec61972b

49m ago

---

---

## Google News: "ai"

**[Artificial intelligence: Yann LeCun works on more flexible AI](https://www.bbc.com/news/articles/cj6gr0xkyr3o)**

Leading AI researcher Yan LeCun has a start-up which is developing a more flexible AI system.

BBC • 13h ago

---

**[Microsoft Frontier Company: AI engineering that amplifies and protects your intelligence](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)**

The pace of AI adoption is moving incredibly fast. Customers have moved well beyond experimentation and understand the importance of adopting AI to transform their business. They are now concentrating on delivering measurable business outcomes and demonstrating a return on their AI investments, while ensuring their intelligence is amplified and their IP is protected. Today...

The Official Microsoft Blog • 22h ago

---

**[Microsoft commits $2.5 billion and 6,000 employees to new AI implementation unit](https://www.cnbc.com/2026/07/02/microsoft-commits-2point5-billion-6000-employees-ai-implementation-unit.html)**

Microsoft is the latest tech company to form a business focused on helping customers understand and implement artificial intelligence.

CNBC • 23h ago

---

**[Microsoft unveils $2.5B ‘Frontier Company’ to embed AI engineers inside customers](https://www.geekwire.com/2026/microsoft-announces-2-5b-frontier-company-to-embed-ai-engineers-inside-customers/)**

"Microsoft Frontier Company" is a $2.5 billion initiative that will embed engineers inside customer organizations to build and run their AI systems. The move follows similar efforts by Amazon, OpenAI and Anthropic, and expands work Microsoft was already doing through its consulting arm and partners.

GeekWire • 23h ago

---

**[Exclusive | SpaceX Showed Investors Prototype of Elon Musk’s New AI Device](https://www.wsj.com/tech/ai/spacex-showed-investors-prototype-of-elon-musks-new-ai-device-b445c57b)**

WSJ • 1d ago

---

**[UK parents warned over posting images of children amid AI sexual abuse fears](https://www.theguardian.com/society/2026/jul/03/ai-sexual-abuse-fears-uk-parents-warned-posting-images-children-national-crime-agency)**

Exclusive: National Crime Agency and safety watchdog issue guidance amid rise in explicit material online

The Guardian • 26m ago

---

**[The Tech Download: Amazon’s devices chief Panos Panay on tech giant's AI gadget push](https://www.cnbc.com/2026/07/03/the-tech-download-amazon-devices-chief-panos-panay.html)**

CNBC's Arjun Kharpal sits down Amazon's Panay on the latest episode of The Tech Download podcast.

CNBC • 1h ago

---

**[Why managing a brand's reputation is more complex than ever in the age of AI](https://www.businessinsider.com/ai-makes-managing-a-brands-reputation-more-complex-than-ever-2026-6)**

Marking and communications leaders shared specific tips for navigating this evolving landscape during a roundtable discussion.

Business Insider • 19m ago

---

**[Jodie Foster Says Brad Pitt’s ‘F1’ Seemed Like It Was Made by AI and Written by a Computer: ‘Wasn’t It?’](https://variety.com/2026/film/news/jodie-foster-brad-pitt-f1-ai-written-by-computer-1236801120/)**

Jodie Foster laughingly said that Apple's "F1" could have been made by AI at a talk at the Aspen Festival of Ideas.

Variety • 13h ago

---

**[The AI Trade Is Losing One of Its Key Signals](https://finance.yahoo.com/technology/ai/articles/ai-trade-losing-one-key-061343277.html)**

(Bloomberg) -- At a time when markets are growing uneasy over whether the enormous sums being poured into artificial intelligence will ever pay off, the prices the sector commands for each unit of usage are drifting lower.Most Read from BloombergExxon to Change Name for First Time in Decades After RedomicileWhy the Great American State Fair Looks So EmptyGermany Rejects Trump’s Demands for NATO Loyalty to WashingtonMeta Is Planning a Cloud Business to Sell AI Computing PowerRussia Indicates Ukra

Yahoo Finance • 6h ago

---

---

## HackerNews: "ai"

**[Godot will no longer accept AI-authored code contributions](https://news.ycombinator.com/item?id=48743472)**

At risk of drowning in AI slop code, Godot is firming up its contribution requirements.

⬆️ 558 • 💬 397 • 2d ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)

---

**[AI can't be listed as inventor on patent applications, Japan's top court rules](https://news.ycombinator.com/item?id=48761536)**

⬆️ 381 • 💬 199 • 22h ago • [japannews.yomiuri.co.jp](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/)

---

**[AI fake news complaining about how AI fake news is the death of real news](https://news.ycombinator.com/item?id=48760598)**

Did 47 Alabama newspapers die on a single day and no one noticed? (Hint: No, they didn't.)

⬆️ 157 • 💬 56 • 23h ago • [Nieman Lab](https://www.niemanlab.org/2026/07/now-were-getting-ai-fake-news-complaining-about-how-ai-fake-news-is-the-death-of-real-news/)

---

**[The short leash AI coding method for beating Fable](https://news.ycombinator.com/item?id=48766026)**

⬆️ 149 • 💬 183 • 17h ago • [blog.okturtles.org](https://blog.okturtles.org/2026/07/short-leash-ai-method/)

---

**[Meta caps internal AI token spending](https://news.ycombinator.com/item?id=48754713)**

⬆️ 146 • 💬 147 • 1d ago • [mlq.ai](https://mlq.ai/news/meta-caps-internal-ai-token-spending-after-costs-approach-billions-in-2026/)

---

**[EU commissioners shut down air conditioning for employees, leave theirs on](https://news.ycombinator.com/item?id=48734940)**

As Brussels bakes, the Berlaymont building’s AC stops working.

⬆️ 137 • 💬 156 • 2d ago • [POLITICO](https://www.politico.eu/article/eu-commission-heatwave-hq-forced-shut-down-air-conditioning-europe/)

---

**[The gauge broke: devs felt 20% faster with AI, measured 19% slower (2025)](https://news.ycombinator.com/item?id=48757440)**

For two years I argued the feeling of AI speed had come apart from the fact of it, from watching my own teams. This summer it stopped being an anecdote. A controlled trial measured experienced developers feeling about 20% faster while running about 19% slower. The instrument we steer by reads backward.

⬆️ 77 • 💬 98 • 1d ago • [intrepidkarthi](https://intrepidkarthi.com/writing/the-gauge-broke/)

---

**[Weird Al Yankovic Pulled Out of AI Ad Deal: 'I Can't Be the Poster Boy for AI'](https://news.ycombinator.com/item?id=48764326)**

Weird Al Yankovic revealed he was offered “a nice pile of money” to appear in a commercial but backed out after realizing it would involve AI.

⬆️ 69 • 💬 39 • 19h ago • [Variety](https://variety.com/2026/biz/news/weird-al-yankovic-rejected-ai-commercial-money-offer-1236800794/)

---

**[How employment changes when firms adopt generative AI](https://news.ycombinator.com/item?id=48742176)**

Firm-level evidence on how employment changes when companies adopt AI, using Ramp AI spending linked to Revelio Labs workforce records.

⬆️ 54 • 💬 50 • 2d ago • [ramp.com](https://ramp.com/data/ai-jobs-impact)

---

**[Scammers Sell Seeds for Exotic AI-Generated Flowers That Don't Exist](https://news.ycombinator.com/item?id=48734389)**

Ebay, Amazon, and Etsy are unable to stop the flood of AI-generated seed scams.

⬆️ 51 • 💬 36 • 2d ago • [404 Media](https://www.404media.co/scammers-sell-seeds-for-exotic-ai-generated-flowers-that-dont-exist/)

---

---

## YouTube Videos: "ai"

**[Why AI is Collapsing: How China is Winning.](https://www.youtube.com/watch?v=JXJf7vL8k94)**

US AI companies are too expensive. Why China is winning the AI race to zero. [NEW] Official TechLead Private Group ...

📺 TechLead

👁️ 41K • 👍 2K • 💬 467 • ⏱️ 9:40 • 13h ago

---

**[Donald Trump posts hilarious AI video ridiculing several woke celebrities with ‘TDS’](https://www.youtube.com/watch?v=-1uaO9rDFg0)**

US President Donald Trump has hilariously mocked several celebrities with 'Trump Derangement Syndrome' (TDS) in his latest AI ...

📺 Sky News Australia

👁️ 22K • 👍 2K • 💬 359 • ⏱️ 9:25 • 11h ago

---

**[CEOs Are Quietly Destroying Their AI Plans](https://www.youtube.com/watch?v=E_565Wh110c)**

How much do you spend per month on AI? Interested in supporting the channel? Become a channel member!

📺 Dylan John

👁️ 17K • 👍 599 • 💬 134 • ⏱️ 16:19 • 1d ago

---

**[Beginning of the end for the AI bros](https://www.youtube.com/watch?v=vfd8GY2Xpzc)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 80K • 👍 6K • 💬 2K • ⏱️ 14:34 • 1d ago

---

**[I Have A Strange Theory About Aliens And Ai](https://www.youtube.com/watch?v=5HPMzsqU6eM)**

We can all agree that things are getting strange out there. In this episode, Pastor Jack tackles the topics of rapidly advancing AI ...

📺 Real Life with Jack Hibbs

👁️ 107K • 👍 8K • 💬 971 • ⏱️ 19:19 • 23h ago

---

**[AI Bubble Fears Grow as Michael Burry, Top Economists Sound Alarm | Vantage on Firstpost | N18G | 4K](https://www.youtube.com/watch?v=zA8hwdmmVos)**

The dot-com boom, railway mania, and tulip craze all share a common theme—markets mistaking excitement for economics.

📺 Firstpost

👁️ 17K • 👍 174 • 💬 15 • ⏱️ 8:02 • 17h ago

---

**[Why is AI expensive all of a sudden?](https://www.youtube.com/watch?v=DDj30VWCbbY)**

ZapierPartner Sponsored by Zapier! Zapier MCP levels you up, connecting you directly to apps to automate your workflow.

📺 Alberta Tech

👁️ 162K • 👍 9K • 💬 806 • ⏱️ 9:43 • 2d ago

---

**[AI has hacked the code of human civilization | Yuval Noah Harari](https://www.youtube.com/watch?v=hBtVGwuJzpk)**

Human domination relies on large-scale cooperation among strangers, which is sustained by bureaucratic systems – such as ...

📺 Yuval Noah Harari 

👁️ 358K • 👍 13K • 💬 1K • ⏱️ 46:52 • 2d ago

---

**[The AI Bubble Has F*cked Us (Even If It NEVER Pops)](https://www.youtube.com/watch?v=dPVEha6oqfw)**

The AI Bubble Will Is MUCH Worse Than We Thought. Contact your representative to ENSURE AI is aligned with humanity: ...

📺 Damon Cassidy

👁️ 97K • 👍 4K • 💬 863 • ⏱️ 22:06 • 2d ago

---

**[AI&#39;s 3 big narrative violations — 7/2/2026](https://www.youtube.com/watch?v=yFEOnBT0Hgw)**

Three things the market believed about AI broke this week. One: you have to own the model. The whole race was about building ...

📺 CNBC Television

👁️ 8K • 👍 143 • ⏱️ 52:39 • 16h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,366,360 • ❤️ 1,315 • 4d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 885,040 • ❤️ 1,671 • 7h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 191,462 • ❤️ 3,302 • 1d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 322,780 • ❤️ 668 • 7d ago

---

**[DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)**

*DeepSeek*

DeepSeek-V4-Pro-DSpark is a text-generation model featuring a 1.6T parameter Mixture-of-Experts architecture with a 1 million token context window, optimized for long-context efficiency using Hybrid Attention. It excels in reasoning, coding, and agentic tasks, offering advanced capabilities for complex applications.

`text-generation` `889.5B`

⬇️ 9,388 • ❤️ 320 • 6d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 287,942 • ❤️ 404 • 7d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 329,391 • ❤️ 977 • 14d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 64,051 • ❤️ 355 • 7d ago

---

**[Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)**

*DeepReinforce*

Ornith-1.0-35B is a state-of-the-art, MIT-licensed language model for agentic coding, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving training framework to generate high-quality code solutions and is optimized for single-GPU deployment.

`text-generation` `664,944`

⬇️ 211,406 • ❤️ 315 • 7d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 45,455 • ❤️ 518 • 8d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 47 • 💬 5 • ⭐ 13,092 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 73,094 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 24 • 💬 2 • ⭐ 9,424 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 103 • 💬 4 • ⭐ 90,522 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 12 • 💬 2 • ⭐ 18,577 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 250 • 💬 4 • ⭐ 10,514 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,180 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 85,253 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 13 • 💬 1 • ⭐ 10,130 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 26,443 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 72.5k • 🔱 3.8k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.3k • 🔱 1.1k • 9m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.1k • 🔱 792 • 4m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 5.2k • 🔱 644 • 2h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.3k • 🔱 203 • 1d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.3k • 🔱 176 • 12h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 87 • 20d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.6k • 🔱 70 • 15h ago

---

**[GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills)**

AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

`Python`

⭐ 1.4k • 🔱 126 • 25d ago

---

**[nolangz/pixel2motion](https://github.com/nolangz/pixel2motion)**

AI logo animation skill: turn raster logos into smooth SVG animation, animated HTML demos, GIF/video previews, and motion QA evidence.

`Python` `ai-design-tools` `animated-logo` `brand-motion` `claude-skill` `codex-skill`

⭐ 1.3k • 🔱 114 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*
