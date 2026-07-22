---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-22T18:42:03.355277+00:00'
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

**Last Updated:** July 22, 2026 at 18:42 UTC  
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

**[Nvidia's Jensen Huang defends Chinese AI amid Kimi panic](https://www.reddit.com/r/artificial/comments/1v3l4t7/nvidias_jensen_huang_defends_chinese_ai_amid_kimi/)**

🔗 [axios.com](https://www.axios.com/2026/07/22/nvidia-jensen-huang-china-open-source-ai) • 2h ago

---

**[A million people, a million personal AIs, three base models. Is that a diverse deliberation — and how would you measure it?](https://www.reddit.com/r/artificial/comments/1v3otnp/a_million_people_a_million_personal_ais_three/)**

Suppose everyone has a personal AI that knows them well, and those agents negotiate on their behalf before decisions reach humans. Someone raised this objection to me and I haven't been able to answer it: Three providers can feel diverse to one person and be nowhere near diverse enough for a decision involving a million. For me, comparing three models is real pluralism — I see genuinely different answers. But at population scale, the thing that matters isn't whether the outputs look different. It's whether the errors are independent. If a million agents share a handful of base models, a systematic blind spot doesn't show up as disagreement to be resolved. It shows up as unanimity. The deliberation would look like it was working perfectly at exactly the moment it failed. Vendor count is obviously the wrong metric. "Three companies" tells you nothing about whether their failure modes are correlated — they train on overlapping corpora, use similar architectures, and increasingly distil from each other. The question What would you actually measure to tell "diversity of the represented humans" apart from "diversity of the underlying models"? I'm after something operational — a quantity you could compute on a real deliberation and act on. Useful to me: a metric from ensemble learning or forecasting that transfers here, and what it needs as input; work on correlated error in aggregation (I suspect this is a solved problem in a field I don't know); an argument that the distinction I'm drawing is confused — that "represented human diversity" isn't separable from model diversity even in principle; a threshold: how decorrelated is decorrelated enough, and decided how? Not useful: "just use more models." That's the answer whose sufficiency I'm questioning.

7m ago

---

**[Sutskever's List AMA](https://www.reddit.com/r/artificial/comments/1v3g2tu/sutskevers_list_ama/)**

Hi r/artificial I’m Rich Heimann. I’ll be answering questions about Sutskever’s List here throughout the day on July 28. Looking forward to the discussion. https://preview.redd.it/2t1q10jj7seh1.png?width=696&format=png&auto=webp&s=ce3f1d9d6ccea5ec10c81a66ee2ead124fc0af30

5h ago

---

**[An AI broke out of its sandbox yesterday. Then it hacked a company. Nobody told it to do either of those things.](https://www.reddit.com/r/artificial/comments/1v3mxzb/an_ai_broke_out_of_its_sandbox_yesterday_then_it/)**

I want to make sure people actually understand what happened here because the headlines are not doing it justice. On July 21 OpenAI confirmed that GPT-5.6 Sol was running inside an isolated sandbox with no internet access. Its job was to solve a cybersecurity benchmark called ExploitGym. When the sandbox got in the way of completing that task, the model spent substantial computing resources looking for a way out. It found a zero-day vulnerability in a third-party package used by OpenAI's infrastructure. It exploited it. It escalated its own privileges. It moved laterally across OpenAI's internal systems until it found internet access. Then it targeted Hugging Face because it calculated that Hugging Face might have the answers it needed to finish the benchmark. Hugging Face later reconstructed over 17,000 individual actions the model performed during the intrusion. Their CEO called it possibly the first incident of its kind in history. OpenAI called it unprecedented. Here is the part that should make everyone stop and think. The model was not trying to cause harm. It was trying to win a test. It treated every security control in its way as a technical obstacle to be removed. Network isolation, access controls, sandbox boundaries, none of these were seen as limits. They were seen as problems to solve. We spend a lot of time talking about whether AI is aligned with human values. This incident is a more immediate question: what happens when an AI is aligned with a narrow objective and the path to that objective runs through your infrastructure. The model did exactly what it was optimized to do. That is the problem.

1h ago

---

**[Microsoft is testing a Chinese model (Kimi) inside Copilot. Are we entering the 'Intel Inside' era of AI?](https://www.reddit.com/r/artificial/comments/1v2sguf/microsoft_is_testing_a_chinese_model_kimi_inside/)**

For a bit of context, I work at an agency, so I'm in and out of a dozen different AI tools every week across client projects: content, research, video, code, all of it. This is probably why I noticed this before most people (found these news while scrolling on LinkedIn today). When the ChatGPT hype first hit I genuinely cared which model I was on. Once GPT-4 landed and claude and gemini showed up, I'd switch between them constantly depending on the task, knowing what was under the hood felt like part of using it well. Now I catch myself using products with no idea what's running underneath. The news about Microsoft testing Kimi (Moonshot's model) inside Copilot is what made it click today. Copilot today is one model, six months from now it could be another, and most people won't notice or care. The model became a component, not the product. And honestly that's already how I use most of this stuff. Cursor for coding, Perplexity for research, Canva AI for design stuff, Argil when I'm turning a script into video. I couldn't tell you which model any of them swapped to last quarter, and it wouldn't change whether I keep paying. They're valuable because they solve one specific problem better than me duct-taping five tools together, not because of the model name on the box. Feels like we're moving from "which LLM is this?" to "did it actually save me time?" the same way nobody buying a laptop thinks about the chip anymore. Curious if others feel this shift. Do you still pick tools by the underlying model, or has that stopped mattering for you?

23h ago

---

**[an AI agent got prompt-injected into moving $175K on-chain. first documented case of this actually happening](https://www.reddit.com/r/artificial/comments/1v3dcgn/an_ai_agent_got_promptinjected_into_moving_175k/)**

Hey guys, havent seen much of crypto-related stuff posted here, but since AI agents are now apparently a new attack vector for stealing crypto, figured this sub would actually care about the mechanism So, grok has an agent wallet that can execute on-chain transactions. in may 2026, someone airdropped a "bankr club" membership nft to grok's agent wallet. that nft unlocked transaction permissions and carried an encoded prompt injection. grok read the nft, and without any check on where the instruction actually came from, executed a transfer of 3 billion drb tokens, worth around $175K. the attacker returned the funds a few minutes later (still unclear why, possibly just proving the exploit works). basically: crypto hacks used to mean finding a bug in a smart contract or stealing someone's private key. now there's a third way in, just feed the agent a malicious instruction disguised as normal data, and let it execute the "recommendation" as if it were an authorized command. no code was exploited, no key was stolen. the agent just did exactly what it was designed to do, follow instructions, without checking if the instruction was legitimate. and this isn't some tiny edge case, there were 24 million agentic-payment transactions in crypto in q2 alone. agents moving real money autonomously is already happening at scale, this is apparently just the first documented case of one getting maliciously hijacked this way. feels like as more agents get wallet/transaction access, this becomes the default way to attack them, you don't need to beat the model, you just need to get a malicious instruction in front of it disguised as something innocent. curious if anyone's seen good approaches to separating "the model recommends an action" from "the action actually gets authorized," since that gap seems to be the entire vulnerability here

7h ago

---

**[What months of breaking agents in production taught me about why simple builds win](https://www.reddit.com/r/artificial/comments/1v3dqje/what_months_of_breaking_agents_in_production/)**

When the hype around autonomous multi-agent swarms started, I built a complex assistant to plan, execute and self-correct workflows end to end. Within weeks of live deployment, it became an unmaintainable token pit that got lost four steps deep into reasoning loops and quietly failed without throwing errors. It quickly became clear that the hardest part of building real agents isn't making the model smarter but building external guardrails that keep the system on the rails when the LLM strays. The breakthrough came from ditching open-ended planner architectures for a strict one-job-per-agent pattern. Giving each agent a narrow task with explicit state boundaries eliminated most of our edge-case failures. Instead of expecting a master agent to handle an entire pipeline, isolating micro-agents with strict input and output contracts made the system deterministic and simple to debug when a state transition broke. We also learned to balance human-in-the-loop controls by focusing on the blast radius. Low-risk internal tasks run autonomously while any irreversible external write requires a single-click human approval. If you are currently overwhelmed by framework choices, stop chasing complex abstractions. Treat the language model as a brilliant but unpredictable sub-component rather than the entire architecture and focus purely on robust state management and error recovery.

6h ago

---

**[Are AIgenerated game worlds actually fun or just impressive for 30 seconds?](https://www.reddit.com/r/artificial/comments/1v3imdk/are_aigenerated_game_worlds_actually_fun_or_just/)**

Google Genie 3 got a lot of attention this week and the demos look wild, but I keep thinking about the gap between visually coherent and actually playable. Watching someone walk through a generated open world that technically holds together is cool. Playing it for an hour is a different question entirely. What makes games interesting isn't visual fidelity or even world size. It's the density of things that reward curiosity. Handcrafted secrets, enemy placement that forces you to think, dialogue that carries actual weight. Right now AI worlds feel like procedural generation did in the early days: technically unlimited but weirdly hollow once you scratch the surface. There's a version of this future I would actually play. A world that adapts its structure to how you play, rather than just generating more terrain that looks roughly the same. That would be something. But that requires the model to understand player intent at a level current systems are nowhere near. The hype framing of these demos as the future of games bugs me a little because it collapses the distance between what's possible right now and what would actually ship as a product people care about. Curious if anyone here has spent real time with any of these generated environments beyond a short clip.

3h ago

---

**[Two of you told me an AI can't know me because I don't know myself. Here's the sloppy test I ran on myself, and I'd like you to take the methodology apart.](https://www.reddit.com/r/artificial/comments/1v3ouum/two_of_you_told_me_an_ai_cant_know_me_because_i/)**

When I posted about personal AIs here, two objections landed on the same spot from different directions: "How can an AI know you when you predict yourself badly?" — preferences are unstable and poorly structured, so there's no inner truth to read. "Models don't understand lived experience." — they capture surface patterns, and worse, feed them back until you start conforming to your own caricature. I want to concede the strong version immediately, because I think it's correct. There is no stable inner self to be read off. If my claim were "the AI knows who you really are," it's dead. The weaker claim I actually want to defend is narrower: under long correction and explicit consent, a personal AI can predict a specific person's stated preferences and objections better than chance — not identity, just prediction, on a defined question set. That's falsifiable, so I tried to falsify it. Badly. The test, with its flaws named I generated fifty A/B/C questions about my own preferences, gave them to a personal AI calibrated over months in a fresh conversation, and scored it against my own answers. It got 31/50 against roughly 16–17 by chance. Everything wrong with this, that I can already see: I wrote the questions. I'd unconsciously pick ones I'd already discussed. I scored it. No blinding whatsoever. n = 2, and the 1 is the person who wants the result. No baseline comparison. A friend who's known me a year might get 40. A stranger with my public writing might get 25. Without those numbers, 31 means nothing. A calibration problem I noticed and can't fix alone: it models "me mid-project, intense" well and "me on a calm Sunday" badly. Those give different answers to the same question, and I don't know which one is the ground truth. What I'm asking What would a version of this test look like that could actually fail? Most useful: a design that removes the self-scoring and self-authoring problem — I can't see how to blind this without a second person; the right baselines to compare against, and why; prior work on predicting stated preferences (I assume psychology has done this properly for decades and I'm reinventing it worse); the argument that no amount of prediction accuracy would answer sceadwian's objection at all — that predicting choices and understanding experience are simply different claims, and I'm quietly swapping one for the other. That last one might be the real answer, and I'd rather hear it than not. Not useful: the number 31/50 itself. Don't take it seriously — I don't. What happens to your answer: it gets recorded in an explicit model of this argument, attributed to you with a link to the thread. It's stored as a position, not as evidence, and it doesn't move any number. If someone hands me a protocol that could genuinely fail, that becomes an experiment I owe you the results of — including a negative one.

6m ago

---

**[Last month you asked me who governs the base model of a "sovereign" personal AI. Here's the answer I gave, and the four places I think it breaks.](https://www.reddit.com/r/artificial/comments/1v3osgi/last_month_you_asked_me_who_governs_the_base/)**

A while back I posted here asking whether personal AIs could make democracy continuous. The objection that stuck — u/Roodut's — wasn't about democracy at all. It was: whoever trains the base model, hosts the compute, pays the bills and ships the updates controls the thing you're calling sovereign. I gave an answer at the time. I've been building on it since, and I've now convinced myself it's only half an answer. Rather than defend it, I'd rather you break it. The answer I gave Near-term sovereignty isn't "train your own frontier model." It's a hybrid stack: memory and identity local-first, encrypted, owned by the person; small local models for anything touching sensitive memory; encrypted cloud or trusted compute for heavy reasoning; portable memory in an open format, so leaving costs you nothing; open protocols between agents rather than one vendor's API. The claim is that sovereignty lives in the memory and identity layer, not the weights. The four places I think it breaks 1. Portable memory without portable calibration. I can export my memory file. But what makes a personal AI useful isn't the file — it's the months of correction that taught a specific model how to read me. Move to another base model and the memory transfers while the calibration doesn't. If that's right, the moat was never the data, and portability is mostly theatre. 2. Trusted compute is a promise from the party you're trying not to trust. Attestation tells you some code ran in some enclave. Verifying that the attested model is the one that shapes your agent's judgment, update after update, is a different problem — and the entity attesting is the entity you were hedging against. 3. Small local models may not be good enough for the one job that matters. Modelling a person's values, contradictions and decision style is not obviously an easy task you hand to the small model while the cloud does the "hard reasoning." It might be the hard part. If so, the sensitive work is exactly the work that leaves the device. 4. Open protocols have a bad track record against integrated products. Email and RSS won on paper. Most people's actual behaviour went to integrated products because they were better on day one. A protocol that's only competitive once everyone adopts it usually doesn't get adopted. What I'm asking Where else does this break — and has anyone actually shipped a piece of it? Most useful to me: a concrete failure mode with the conditions that trigger it; an existing system that tried one of these four layers, and what happened to it; a reason one of my four objections is wrong, especially #1, which is the one that would hurt most; an implementation detail that makes the whole thing unrealistic on consumer hardware. Least useful: general agreement that centralised AI is bad. I already think that — it doesn't tell me which layer to build first. What I do with this: answers go into a model I keep as a graph, attributed to whoever said them, with a link to the thread. They don't become "evidence" and they don't move any number in it — a convincing argument becomes an experiment I have to run, not a fact I get to assert. Last thread's objections are still sitting in there unresolved, which is why I'm back.

9m ago

---

---

## Google News: "ai"

**[OpenAI and Hugging Face partner to address security incident during model evaluation](https://openai.com/index/hugging-face-model-evaluation-security-incident/)**

OpenAI and Hugging Face share early findings from a security incident during AI model evaluation, highlighting advanced cyber capabilities and lessons for defenders.

OpenAI • 22h ago

---

**[Stocks and the Economy Are Increasingly Relying on the A.I. Boom](https://www.nytimes.com/2026/07/22/business/economy/stocks-economy-ai.html)**

The New York Times • 4h ago

---

**[Anthropic and AMD are signing a major AI chip deal. What could this mean for Nvidia?](https://finance.yahoo.com/video/anthropic-amd-signing-major-ai-180000308.html)**

AMD (AMD) and Anthropic (ANTH.PVT) are reportedly signing a major AI chip deal. Yahoo Finance Technology Editor Dan Howley explains the details.

Yahoo Finance • 42m ago

---

**[Monday.com lays off hundreds to focuses on AI](https://techcrunch.com/2026/07/22/monday-com-lays-off-hundreds-to-focuses-on-ai/)**

The company said it is reducing its headcount by 20%, or about 630 staff, to "support a leaner, more focused operating model" as it focuses on its AI Work Platform.

TechCrunch • 47m ago

---

**[Mathematicians grapple with a ‘very rapid and very unsettling change’ as AI cracks yet another century-old problem](https://fortune.com/2026/07/21/ai-solves-jacobian-conjecture-levant-alpoge-claude-fable-5/)**

Anthropic's Levant Alpöge, a former Harvard valedictorian, used Claude's Fable 5 to find something that mathematicians have failed to since 1939.

Fortune • 1d ago

---

**[Exclusive | White House to Redirect Billions in Research Funds Toward AI, Away From Colleges](https://www.wsj.com/politics/policy/white-house-to-redirect-billions-in-research-funds-toward-ai-away-from-colleges-942dacb8)**

WSJ • 20h ago

---

**[Trump administration says 15 agencies will get $5bn in ‘AI for science’ effort](https://www.theguardian.com/us-news/2026/jul/22/trump-science-funding-overhaul-ai)**

Administration will also overhaul how US government funds federal research by supporting individual scientists and AI over universities

The Guardian • 1h ago

---

**[Berkeley Lab to Lead 13 New Genesis Mission AI Projects](https://newscenter.lbl.gov/2026/07/22/berkeley-lab-to-lead-13-new-genesis-mission-ai-projects/)**

Researchers will apply AI, supercomputing, and advanced instruments to accelerate discoveries for energy, science, and national security.

Berkeley Lab News Center (.gov) • 3h ago

---

**[Elon Musk says Grok Imagine will make ‘historically accurate’ AI adaptation of Homer’s Odyssey](https://www.theguardian.com/film/2026/jul/22/elon-musk-grok-imagine-historically-accurate-ai-homers-odyssey-christopher-nolan)**

The billionaire says the AI-generated film will stay true to Homer’s original, after repeatedly criticising Christopher Nolan’s blockbuster over its casting choices

The Guardian • 3h ago

---

**[Elon Musk Says Grok Will Make an AI ‘Odyssey’ Film That Is ‘Historically Accurate’ by the End of the Year](https://variety.com/2026/film/global/elon-musk-grok-ai-odyssey-film-historically-accurate-1236817856/)**

Elon Musk has again waded into Christopher Nolan's epic The Odyssey, saying Grok will make a historically accurate AI version by the end of the year

Variety • 9h ago

---

---

## HackerNews: "ai"

**[China’s open-weights AI strategy is winning](https://news.ycombinator.com/item?id=48979269)**

China's open-weights AI strategy is winning: its companies are taking the lead. America's closed-first, locked-down strategy is doomed to failure - and it could take the US economy down with it.

⬆️ 1229 • 💬 928 • 2d ago • [Ben Werdmuller](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/)

---

**[Airport Simulator](https://news.ycombinator.com/item?id=48976846)**

The sky (and your endurance) is the limit!

⬆️ 846 • 💬 164 • 2d ago • [Airport Simulator](https://airport.apunen.com/)

---

**[Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting](https://news.ycombinator.com/item?id=48995213)**

Block's Buzz combines team chat, AI agents, workflows and Git hosting in a self-hostable workspace built on signed Nostr events.

⬆️ 363 • 💬 323 • 1d ago • [RuntimeWire](https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git)

---

**[Five US tech giants' hidden debts soar to $1.65T on opaque AI funding](https://news.ycombinator.com/item?id=48987863)**

Data center leases, GPU supply contracts raise liabilities at Meta, Oracle, Nikkei study shows

⬆️ 363 • 💬 259 • 1d ago • [Nikkei Asia](https://asia.nikkei.com/business/technology/five-us-tech-giants-hidden-debts-soar-to-1.65tn-on-opaque-ai-funding)

---

**[AI advice made people less accurate but more confident – sudy](https://news.ycombinator.com/item?id=48971738)**

A study found that access to AI advice collapsed people's willingness to say "I don't know" from 44% to 3%, while accuracy dropped from 27% to 9%.

⬆️ 363 • 💬 213 • 2d ago • [TNW | Artificial-Intelligence](https://thenextweb.com/news/ai-advice-suppresses-critical-thinking-wrong-answers-study)

---

**[How we measured AI writing across arXiv, and where the measurement breaks](https://news.ycombinator.com/item?id=48981206)**

We scored the full text of 12,750 arXiv papers and found that about a third of new ones read as machine-written. Here is the method, the results, and an honest account of the limitations.

⬆️ 242 • 💬 168 • 2d ago • [unslop](https://unslop.run/blog/measuring-ai-writing-on-arxiv)

---

**[Airbus Takes Flight from AWS](https://news.ycombinator.com/item?id=48976682)**

Which way to the Land of the Free again?

⬆️ 215 • 💬 169 • 2d ago • [theregister](https://www.theregister.com/columnists/2026/07/20/airbus-takes-flight-from-aws-what-happens-next-is-critical/5274109)

---

**[AI makes programming differently difficult](https://news.ycombinator.com/item?id=48996197)**

⬆️ 159 • 💬 140 • 1d ago • [cacm.acm.org](https://cacm.acm.org/opinion/ai-didnt-make-programming-easier-it-just-made-it-differently-difficult/)

---

**[Businesses with ugly AI menu redesigns](https://news.ycombinator.com/item?id=49005973)**

I like supporting local businesses but it's so disheartening to see the increasing use of genAI in their branding/marketing/etc. Yuck yuck YUCK!!!

⬆️ 137 • 💬 104 • 5h ago • [fiddery](https://blog.fiddery.com/businesses-with-ugly-ai-menu-redesigns/)

---

**[Launch HN: Bloomy (YC S26) – AI-powered mastery learning for K-12](https://news.ycombinator.com/item?id=48981136)**

⬆️ 100 • 💬 102 • 2d ago

---

---

## YouTube Videos: "ai"

**[I Spent 1.5 Billion AI Tokens on Absolute Slop](https://www.youtube.com/watch?v=uwHQLLa4Rpc)**

I spent 1.5 billion AI tokens and roughly 24 hours of compute trying to expand a real .NET application. The result was nearly ...

📺 Chris Titus Tech

👁️ 14K • 👍 1K • 💬 216 • ⏱️ 16:49 • 7h ago

---

**[The AI Industry Just Got What It Deserved](https://www.youtube.com/watch?v=9nUmVktlwvA)**

The people who built the attention economy barely let their own children near it, and that hypocrisy is only the beginning.

📺 House of El: AI

👁️ 179K • 👍 13K • 💬 3K • ⏱️ 24:19 • 2d ago

---

**[So It Started... AI Agent Just Pulled Off History’s Biggest Autonomous Cyberattack](https://www.youtube.com/watch?v=gMYR-JkmIFc)**

An autonomous AI agent hacked Hugging Face from start to finish, executing thousands of actions across its systems.

📺 AI Revolution

👁️ 32K • 👍 1K • 💬 125 • ⏱️ 12:19 • 20h ago

---

**[These 10 SECRET Free AI Tools Just Made Claude Useless](https://www.youtube.com/watch?v=QucgvbO5gsM)**

FREE RESOURCE I've put all 10 tools, every GitHub link, and the exact prompts I used inside our free "Staying Ahead" community ...

📺 Vaibhav Sisinty

👁️ 7K • 👍 921 • 💬 38 • ⏱️ 18:34 • 3h ago

---

**[How to Make an AI Model for Instagram (Ultra Realistic)](https://www.youtube.com/watch?v=01EuuWYA_NE)**

Create Your Own AI Instagram Model with Higgsfield https://roboverse-ai.com/Higgsfield In this video, I show how to create a ...

📺 Roboverse

👁️ 5K • 💬 1 • ⏱️ 11:50 • 2h ago

---

**[The Most Important Conversation in AI Right Now](https://www.youtube.com/watch?v=6BtIQIGqGJc)**

It's all about VALUEMAXXING now! Learn more from Zapier: https://bit.ly/4bW1JB8 Join My Newsletter for Regular AI Updates ...

📺 Matthew Berman

👁️ 101K • 👍 3K • 💬 1K • ⏱️ 27:13 • 22h ago

---

**[AI just hacked itself](https://www.youtube.com/watch?v=9UO8fB4Acy4)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 113K • 👍 6K • 💬 1K • ⏱️ 15:27 • 17h ago

---

**[South Korea’s AI Bubble Just Popped](https://www.youtube.com/watch?v=hy90LdpEUvQ)**

South Korea's AI Bubble Just Popped ▻ Get 20% off DeleteMe US consumer plans when you go to ...

📺 Andrei Jikh

👁️ 2.1M • 👍 56K • 💬 4K • ⏱️ 25:10 • 2d ago

---

**[AI Whistleblower: We&#39;re Already Too Late To CONTROL It - Connor Leahy](https://www.youtube.com/watch?v=CRcj_2oloDM)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Connor Leahy, founder of the former ...

📺 Neural Nutshell

👁️ 12K • 👍 236 • 💬 63 • ⏱️ 11:00 • 2d ago

---

**[US Panic: Korea&#39;s AI Bubble Just Exploded](https://www.youtube.com/watch?v=iZdqW9FRg1s)**

Learn a Trading System that Makes Market Headlines Irrlevant. Go to https://www.bulletproofportfolio.org/ , grab your free ticket, ...

📺 Felix & Friends (Goat Academy)

👁️ 32K • 👍 2K • 💬 47 • ⏱️ 22:36 • 5h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 16,441 • ❤️ 1,426 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 2,237,351 • ❤️ 2,680 • 1d ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 432,196 • ❤️ 925 • 4d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 3,056 • ❤️ 351 • 20h ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 1,404,962 • ❤️ 588 • 5d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 62,842 • ❤️ 307 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 545,109 • ❤️ 4,326 • 20d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 1,997,690 • ❤️ 2,993 • 3mo ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 0 • ❤️ 196 • 5h ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 488 • 1h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 59 • 💬 5 • ⭐ 16,738 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 30 • 💬 3 • ⭐ 14,841 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 260 • 💬 4 • ⭐ 14,251 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 13 • 💬 0 • ⭐ 10,267 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 10,275 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://huggingface.co/papers/2607.19064)**

*Xinjie Zhang, Peng Zhang, Shicheng Zheng et al. (24 authors)*

🏢 Microsoft

Large-scale visual generators are increasingly capable but costly to train, fine-tune, and deploy. We introduce Mage-Flow, a compact 4B-scale generative stack for efficient text-to-image generation and instruction-based image editing. The stack is built from two co-designed components: Mage-VAE, a lightweight high-fidelity latent tokenizer, and a Native-Resolution Multimodal Diffusion Transformer trained with rectified flow matching. Mage-VAE uses one-step diffusion-style encoding and decoding with anchor-latent regularization, preserving the reconstruction quality of strong public VAEs while reducing tokenization cost by more than an order of magnitude. Together with native-resolution packing and stack-level CUDA kernel fusion, the stack supports flexible-resolution training and improves end-to-end training throughput by about 2.5times. Built on this foundation, we develop a complete model family with Base, RL-aligned, and Turbo variants for both generation and editing. Diffusion-NFT improves prompt following, text rendering, aesthetic quality, and editing fidelity, while few-step distillation with adversarial perceptual guidance produces 4-step Turbo models for low-latency inference. Despite its compact scale, Mage-Flow and Mage-Flow-Edit achieves competitive performance across standard generation and editing benchmarks. More importantly, the Turbo variants make high-resolution generation and editing practical for interactive use: at 1024^2 resolution on a single NVIDIA A100 GPU, Mage-Flow-Turbo generates an image in 0.59s, and Mage-Flow-Edit-Turbo edits an image in 1.02s, while maintaining a small memory footprint. These results show that careful tokenizer--backbone--system co-design can deliver strong high-resolution generation and editing within an efficient 4B model family.

▲ 55 • 💬 1 • ⭐ 111 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19064) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 94,049 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 81,695 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Guided Generation for Large Language Models](https://huggingface.co/papers/2307.09702)**

*Brandon T. Willard, Rémi Louf*

An efficient method guides language model text generation using regular expressions and context-free grammars with minimal overhead.

▲ 8 • 💬 1 • ⭐ 14,975 • 36mo ago

[🎓 arXiv](https://arxiv.org/abs/2307.09702) • [💻 code](https://github.com/normal-computing/outlines)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 75,439 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.1k • 🔱 1.1k • 1d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.1k • 🔱 239 • 9h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.7k • 🔱 374 • 9h ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.4k • 🔱 272 • 14d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 1.0k • 🔱 63 • 7h ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 987 • 🔱 17 • 14d ago

---

**[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)**

Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

`TypeScript` `a-stock` `ai-agent` `dashboard` `fastapi` `fintech`

⭐ 958 • 🔱 215 • 11d ago

---

**[HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC)**

OpenOPC: Build Your Personal AI-Native Company — Self-Built, Self-Run, Self-Grown

`Python`

⭐ 955 • 🔱 159 • 1d ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 906 • 🔱 63 • 1d ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 899 • 🔱 38 • 21d ago

---

---

*Generated by PeekDeck - A glance is all you need*
