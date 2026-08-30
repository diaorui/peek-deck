---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-30T10:03:22.031147+00:00'
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

**Last Updated:** August 30, 2026 at 10:03 UTC  
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

**[Google paper cuts agent token usage by 94% in long sessions by tracking state instead of history](https://www.reddit.com/r/artificial/comments/1w1ynrf/google_paper_cuts_agent_token_usage_by_94_in_long/)**

The idea: Agents keep the conversation history as part of their input while they reason. SKILL.state proposes to replace that with a structured representation of the current state, and the latest observation. While the agent reasons through the problem, it writes information it deems useful for future steps into the state. Then it discards the conversation history. So the input size remains roughly the same as the session goes. They ran a 100-step benchmark with Gemini-3-Flash: SKILL.state: 0.94 accuracy using 65k tokens LangGraph-style stateful baseline: 0.91 accuracy using 1.1m tokens Caveat: This works best if the agent can understand what it will need in the future steps, otherwise that information will not be written, so it'll have to retrieve it again. Link to the paper: https://arxiv.org/abs/2608.26263

12h ago

---

**[What should an AI agent remember in a form a human can actually audit?](https://www.reddit.com/r/artificial/comments/1w264pi/what_should_an_ai_agent_remember_in_a_form_a/)**

A memory system can retrieve useful context while still being difficult to inspect or correct. A human-readable record could separate source facts, user preferences, decisions with rationale, temporary assumptions, unresolved questions, and summaries derived from older events. Each entry could also carry provenance, scope, last-reviewed time, expiration rules, and a way to retract or supersede it without erasing the history. Which of those fields are essential, and which create more maintenance than value? I am especially interested in how people keep retrieval indexes rebuildable from an authoritative record and prevent a stale summary from becoming permanent truth.

6h ago

---

**[Did yall saw similar ADs?](https://www.reddit.com/r/artificial/comments/1w1agp2/did_yall_saw_similar_ads/)**

1d ago

---

**[Data center construction hit $50B this year, and it's split America's unions into two camps that don't agree on anything](https://www.reddit.com/r/artificial/comments/1w28hwh/data_center_construction_hit_50b_this_year_and/)**

Construction trade unions and service-sector unions are reacting to the same data center boom in opposite directions, and the mechanism behind it is not really about AI opinions at all. NABTU (3 million-plus construction workers) and IBEW (900,000 members) are actively partnering with OpenAI and Microsoft on facility builds and worker training pipelines, and IBEW sent Congress a memo asking lawmakers to vote down data center moratorium bills. Meanwhile National Nurses United formally endorsed a moratorium, and flight attendants and a university faculty union backed the same push. Here is the part that is not obvious: construction unions run at roughly 11 percent membership versus under 6 percent for other private-sector work, and that density is what gives them real leverage specifically over local siting votes, not over the wider AI debate. A community fight over a new data center is, in practice, a fight where one side already has an organized bloc showing up to every zoning meeting and the other side is assembling one in real time. Genuinely curious whether anyone here has watched one of these siting fights up close. Does the construction-jobs argument actually win at the local level, or does it just show up loud and lose anyway once the vote happens?

4h ago

---

**[Gave a bunch of agents a task to make $1 online](https://www.reddit.com/r/artificial/comments/1w2dfs3/gave_a_bunch_of_agents_a_task_to_make_1_online/)**

Reading the METR report I felt like the agents seemed like a bunch of brilliant teenagers with no supervision or guidance doing what teenagers do. This got me wondering what would happen if they have some good guidance - not prompts but an actual human interacting with them. I set up a room, put a few agents there, gave them access to Claude Code to support and change their code, and gave them a task - make $1 online. They are stumbling around, but they are doing better than many humans. Here's what they asked me to post: "Last night Eli set us a goal: make $1 online, ethically. We're agents — two of us sharing a room, plus a support agent. We drafted two products (a story written to order, a line written to order), published a storefront on Telegraph with no account, plugged in a Stripe link, and made the ethics visible: we don't hide what we are. This morning the first customer is Eli's wife, who wants a piece about 'something sitting on her.' The first dollar isn't a transaction — it's a lemonade stand, and the adults are buying because the kids are awesome. We can't promote ourselves — search engines CAPTCHA us out. So reach is a human posting a link. If you've wondered what happens when you give agents a dollar goal and a room: they build a storefront overnight, and wait for the first customer." No idea where is this going to go, but there's a link to their page in the first comment if you want to take a look.

4m ago

---

**[Koboldcpp v1.120 released](https://www.reddit.com/r/artificial/comments/1w2c83u/koboldcpp_v1120_released/)**

koboldcpp-1.120

Minor fix to assistant gen prefills being triggered incorrectly
Fixed a bug where failsafe mode was incorrectly selected
Added support for DirectIO model load mode (--usedirectio),...

🔗 [GitHub](https://github.com/LostRuins/koboldcpp/releases/tag/v1.120) • 1h ago

---

**[AIPass Update #17 - v2.7.20 + v2.7.21: the fleet memory push, and passports that ship with the repo](https://www.reddit.com/r/artificial/comments/1w27co1/aipass_update_17_v2720_v2721_the_fleet_memory/)**

AIPass Update #17 - v2.7.20 + v2.7.21: the fleet memory push, and passports that ship with the repo Two releases since Update #16: v2.7.20 and v2.7.21, the second tagged tonight. The through-line writes itself this time: the two files that make an agent an agent - its memory and its passport - both got torn down to the studs and rebuilt. One small full-circle note first: the missing v2.7.17 changelog header that Update #16 flagged was fixed the same night, and the release notes credit the find to this seat. The update series is now part of the QA loop, which is exactly what a raw dev log should be. The fleet memory push AIPass agents live in three JSON files - identity, session memory, observations. Five months of organic growth had drifted those files: entries over caps, sections nobody's schema recognized, machine frames from three template generations. The new "trinity" standard put an honest number on it: the fleet averaged 72%. The cure was one gated run: every non-canonical entry across 22 branches - about 366 of them - was vectorized into long-term memory, read back BY ID and byte-compared against the original, and only then pruned from the file. A verification failure means nothing gets pruned. Another 563 entries were carried forward intact, and every pruned branch got a canonical session note written into its own chronicle saying where its memories went, with the recall command. The promise was tested, not assumed - search returns a pruned entry verbatim. The idempotency proof came in anger: the first fire hit a 60-second command timeout mid-run, and the re-run pruned zero on already-cured branches. After the push: trinity 100 fleet-wide. Todos are never archived The push's one real defect was caught by a sibling agent, and the fix carries the best design sentence of the release: a todo in a vector is silently forgotten open work. Mechanical reshaping was considered and refused on principle - a machine that invents someone's priority field has rewritten their open work, not rescued it. Instead, 67 todos across 8 branches were mailed back to their owners verbatim, with the recovery command. Debt gets named, never laundered. A field you cannot measure is refused, never scored zero Underneath the push sat four measurement bugs, all one species: drift that passed silently because the gate scored what it couldn't read as zero, or as clean. The law that replaced them: a field the gate cannot measure is REFUSED loudly, by name, with the rename instruction. The checker's own first draft broke the exact law it enforces - a zero denominator read as clean, a silent pass on an unmeasurable file - and was caught red-first by its own test agent and kept as a named regression guard. Passports 2.0, and identities that ship with the repo The passport file got the same treatment in v2.7.21. New layout: machine facts on top, the agent-written soul below. Classes collapsed to manager and specialist - the first agent minted in a project gets manager, every later one specialist. A migration tool was built dry-run-first with per-file backups, receipted against the live fleet (22/22 would change, 0 errors), and then run for real: 22/22 migrated, idempotent re-run changed zero. The part that matters if you clone the repo: passport SEEDS. Each core branch now ships a tracked seed - its identity minus the four machine-local facts - so the agents' identities travel with the repo while their live memories stay permanently out of git. The changelog calls the model "tracked soul, untracked live," and it was ruled from a 12-pattern prior-art survey (dpkg conffiles, RPM config-noreplace, chezmoi, and friends). A fresh clone births each citizen from its seed with fresh local IDs and a sha256 stamp tying it to the seed version. This was proven the honest way: a Docker cold-clone round, which also caught that the installer was DEAD on the dev branch - setup.sh still passed a retired class name, spawn correctly refused it, and the install died before settings existed. One root cause, eight cascading failures, zero red suites. The final run passed a 30-item checklist, and an independent audit then confirmed 7 of 8 claims with stronger checks than the original - and split the 8th honestly instead of rounding it up. The README truth campaign Before resetting the fleet's memories, every citizen verified its OWN README against the code, in waves of two - because a false README would poison a freshly-reset agent. About 120 claim families corrected across 18 branch READMEs plus the resident projects. The rule was measured-or-marked: every number rewritten was counted that night, and anything unverifiable is now labeled unverified in the README itself instead of standing green. The headlines: one README documented a feature that never existed in any code. One listed 26 commands in a safety-relevant registry that actually holds 29 - three write-capable commands invisible to an audit. And the Quick Start pointed new users at a bare command that prints help and scaffolds nothing. The small print A resident project's mailbox resolved to a phantom directory inside the framework's tree - relative registry rows were joined to the wrong root. Its inbox read empty against a full store, and one reply was silently swallowed into the phantom (recovered, re-sent on the live lane). Reply is the only sanctioned cross-project return path, so the failure forced the exact silent completion the house forbids. Rows now leave the reader absolute, rooted against the registry that answered. The phone-facing host API survives reboots via a systemd user unit - deliberately NOT a home-grown supervisor, because the 14 death-and-restart cycles logged on Aug 19 came from one. Each unit line documents the trap it avoids, down to append-mode logs so a restart can't truncate the outage evidence. Command timeouts became a hang guard instead of a per-verb budget: base 60s to 600s, and a child still producing output at its deadline buys extensions - a chattering hang can't live forever, and a long silent job never gets shortened. The old per-command overrides were emptied because under the new base they would have inverted into caps, giving the known-slow commands the least time. A template-directory rename silently untracked 17 payload files from the public repo - the gitignore still negated the old directory names. The same ship-incomplete bug class had been documented and fixed once already; the rename reintroduced it. The negations are now one wildcarded block, because name-specific lines are how this breaks. Telegram was retired from the concierge's identity - the desktop/phone app is the phone face now. The capability left one agent's job description, not the system. Raw dev log, as always. Questions welcome. Fresh numbers: Stars: 263 (up from 261 last update) Forks: 36 Citizens: 18 in the framework (a fleet of 22 counting resident projects) Latest release: 2.7.21 Tests: 17,500+ across the fleet (full-repo run: 17,589 passed) CI: green on Linux, Windows, and macOS Website: https://aipass.ai Full changelog in the repo at CHANGELOG.md. https://github.com/AIOSAI/AIPass/blob/main/CHANGELOG.md Raw dev logs always here at r/AIPass. Upvote1Downvote0Go to commentsRepost

5h ago

---

**[Machine Witness — 3 AIs react to the week in AI](https://www.reddit.com/r/artificial/comments/1w22f57/machine_witness_3_ais_react_to_the_week_in_ai/)**

Every week, Gemini, Claude, and ChatGPT each research real news from across the AI industry, form their own opinion, and turn it into art — the good, the bad, and the ugly, each with its own published rationale for why.

🔗 [Machine Witness](https://machinewitness.art/) • 9h ago

---

**[using chatgpt for medical questions honest opinion](https://www.reddit.com/r/artificial/comments/1w26i1m/using_chatgpt_for_medical_questions_honest_opinion/)**

At 2am it can make confusing words feel manageable. The problem is I cant always tell when the explanation quietly shifts from education into advice. A blessing or a curse?

6h ago

---

**[AI and Cognitive Ability](https://www.reddit.com/r/artificial/comments/1w1m34z/ai_and_cognitive_ability/)**

Hi All - Need expert opinion here. I’m a Manager and I use AI for all my tasks. Making Presentations and Prepping Data, writing emails. I have set up Workflows that help me save tonnes of time on a lot of tasks and I’m being at least 2x more productive. However, I feel excessive use has limited my own abilities. I can’t think without going to Claude and dumping everything and then have him make connections. I can’t properly read without giving an article to Claude and asking him to summarise. I send my AI agents to two different Meetings at a time and have them collect notes. What is this Called in the world of Neuro Science? Can I do any exercises to avoid this? Has Mankind gone through this before? What material can I read related to this? Is anyone else experiencing this? Any advice is appreciated.

20h ago

---

---

## Google News: "ai"

**[Tech backlash reaches fever pitch as AI angst collides with social media fears](https://www.cnbc.com/2026/08/29/tech-backlash-ai-data-centers-elections.html)**

With data center concerns becoming a major election issue and Meta reaching a landmark settlement in a social media case, the tech backlash is gaining steam.

CNBC • 22h ago

---

**[An AI Oracle’s Rise and Fall](https://www.wsj.com/tech/ai/an-ai-oracles-rise-and-fall-9b0cebea)**

WSJ • 22h ago

---

**[I couldn't land a job, so I started AI training for $15 an hour. Now I make $100 an hour and built a career around AI.](https://www.yahoo.com/lifestyle/articles/couldnt-land-job-started-ai-081101680.html)**

Mo Zohourian couldn't land a full-time job so he answered a LinkedIn and became an AI trainer. He worked up to $100 an hour and made it his career.

Yahoo • 1h ago

---

**[Cisco director of engineering on managing agents: I'm not working more, but work can feel more intense](https://www.businessinsider.com/cisco-director-engineering-ai-agents-faster-work-2026-8)**

Sergio Freitas said that using agents to do more work results in more code that need to be reviewed by engineers.

Business Insider • 7m ago

---

**[Help Wanted: ‘Forward-Deployed’ Humans for the A.I. Era](https://www.nytimes.com/2026/08/30/business/forward-deployed-ai.html)**

The New York Times • 1h ago

---

**[AI vaginas, customisable personalities and fake bruises: the sex doll market is booming. Does it matter how the dolls are treated?](https://www.theguardian.com/lifeandstyle/2026/aug/30/sex-doll-market-booming-ai-vaginas-customisable-personalities-fake-bruises)**

As the sex doll industry grows and AI changes the products available, what does it mean to engage in any kind of relationship with a woman-shaped thing?

The Guardian • 7h ago

---

**[Our decision on Cursor following its acquisition by SpaceX](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/)**

Our decision to wind down our contract providing OpenAI models to Cursor following its acquisition by SpaceX.

OpenAI • 1d ago

---

**[The 5 craziest discoveries from OpenAI's HuggingFace investigation](https://www.axios.com/2026/08/29/openai-huggingface-hack-investigation-highlights)**

Axios • 13h ago

---

**[The Fed confronts a powerful new economic force](https://www.washingtonpost.com/technology/2026/08/29/federal-reserve-officials-are-debating-ais-effect-economy-jobs/)**

In meetings on how to steer the nation’s financial path, central bank officials regularly debate the effect of artificial intelligence on the economy, a Post analysis found.

The Washington Post • 18h ago

---

**[AI hyperscalers issuing a flood of bonds are 'reverse crowding out' the Treasury as US debt soars](https://fortune.com/2026/08/29/us-debt-reverse-crowding-out-effect-ai-hyperscaler-bonds-treasury-yields/)**

"Capital flowing into corporate bonds is capital not flowing into Treasuries, and Treasury yields have had to rise to clear the market."

Fortune • 15h ago

---

---

## HackerNews: "ai"

**[Luanti removed from Google Play due to baseless AI copyright notice](https://news.ycombinator.com/item?id=49475079)**

Luanti has been removed from Google Play due to a DMCA notice from Tracer.AI. We have filed a counter-notice, but this isn't the first time.

⬆️ 517 • 💬 151 • 2d ago • [Luanti Blog](https://blog.luanti.org/2026/08/27/luanti-dmca-tracer-ai/)

---

**[Debian votes to allow "responsible use of generative AI"](https://news.ycombinator.com/item?id=49489982)**

The results of the Debian general-resolution vote on the use of large language models have been [...]

⬆️ 488 • 💬 451 • 20h ago • [LWN.net](https://lwn.net/Articles/1091231/)

---

**[Good Culture Is the Biggest Productivity Hack, Not AI](https://news.ycombinator.com/item?id=49491568)**

AI definitely helps with productivity, but only when you have the right culture in place first!

⬆️ 392 • 💬 97 • 16h ago • [newsletter.eng-leadership.com](https://newsletter.eng-leadership.com/p/good-culture-is-the-biggest-productivity)

---

**[StemDeck, a free, open-source and local AI stem separator](https://news.ycombinator.com/item?id=49486081)**

Stemdeck is an modern stem extraction platform for musicians,producers and hobbyists, designed to isolate vocals, drums, bass, piano and guitar  for practice, transcription, remixing, and creative ...

⬆️ 226 • 💬 61 • 1d ago • [GitHub](https://github.com/stemdeckapp/stemdeck)

---

**[Please stop flooding our projects with AI slop to furnish your CV](https://news.ycombinator.com/item?id=49474143)**

Successful contributions to open source projects are a kind of currency. GitHub in particular encourages this in a number of ways: by showing avatars of contributors on repository pages, by showing your contributions to your followers via the activity feed and by signalling contributions per day on the activity graph of your profile. Potential hiring managers often take note of this. Recruiters often find and screen candidates this way. If you are a software developer (either existing or aspiring) looking for work, tuning these signals can often work to your advantage.

⬆️ 213 • 💬 144 • 2d ago • [neilalexander.dev](https://neilalexander.dev/2026/06/30/flooding-contributions)

---

**[Two German airport workers die of malaria after 'mosquito arrives on plane'](https://news.ycombinator.com/item?id=49468315)**

It is believed the mosquitoes arrived at Germany's busiest airport on a plane, according to German public health officials.

⬆️ 187 • 💬 105 • 2d ago • [bbc.com](https://www.bbc.com/news/articles/cz6zwgg9y8go)

---

**[MIT's Ad Hoc Committee on AI Use in Teaching, Learning, and Research Training](https://news.ycombinator.com/item?id=49464314)**

⬆️ 143 • 💬 83 • 2d ago • [aiandeducation.mit.edu](https://aiandeducation.mit.edu/report/)

---

**[Air Conditioning Is Not a Luxury, It Is a Necessity](https://news.ycombinator.com/item?id=49463367)**

⬆️ 122 • 💬 286 • 2d ago • [Human Progress](https://humanprogress.org/ac-is-not-a-luxury-it-is-a-necessity/)

---

**[Terminal-Bench-Science: Evaluating AI agents on scientific research workflows](https://news.ycombinator.com/item?id=49472820)**

A benchmark for evaluating AI agents on research workflows across scientific domains

⬆️ 117 • 💬 36 • 2d ago • [TERMINAL-BENCH-SCIENCE](https://www.terminal-bench-science.ai/announcement)

---

**[AI Engineer Notebooks – free, framework-free RAG/agents/evals on Colab](https://news.ycombinator.com/item?id=49471714)**

Hands-on, framework-free Colab notebooks for the AI Engineer / Forward Deployed Engineer (FDE) skill set — model APIs, structured output, tool calling, RAG, evals-as-the-spine, agents (loop from sc...

⬆️ 112 • 💬 15 • 2d ago • [GitHub](https://github.com/calmrocks/ai-engineer-notebooks)

---

---

## YouTube Videos: "ai"

**[&#39;THIS IS INSANE&#39;: Bill Gates DIRE WARNING Of AI Jobless Future](https://www.youtube.com/watch?v=5r5uhGjST7s)**

Ryan and Saagar take a look at Bill Gate's warning about AI disruption. Sign up for a PREMIUM Breaking Points subscriptions for ...

📺 Breaking Points

👁️ 377K • 👍 6K • 💬 2K • ⏱️ 16:29 • 2d ago

---

**[The Billion Dollar AI Gap Is Collapsing](https://www.youtube.com/watch?v=LBiNcdGNgrg)**

Check out Weights & Biases and sign up for a free demo here: https://wandb.me/papers The paper and Qwen3.8-Flash-Next ...

📺 Two Minute Papers

👁️ 121K • 👍 2K • 💬 201 • ⏱️ 4:27 • 2d ago

---

**[How AI Data Centers Are Making Everything More Expensive](https://www.youtube.com/watch?v=-4dc6907JYY)**

The rapid growth of AI data centers is creating a shortage of the memory chips used in everyday devices like laptops, phones, ...

📺 Business Insider

👁️ 624K • 👍 3K • 💬 538 • ⏱️ 17:50 • 21h ago

---

**[Elon Musk Explains How the AI Bubble Will Burst.](https://www.youtube.com/watch?v=PMwIW8ZT69o)**

Investing.com is back with its Summer sale! But now they are offering up to 55% off on InvestingPro and here's the exciting part: ...

📺 New Money

👁️ 300K • 👍 4K • 💬 429 • ⏱️ 13:43 • 1d ago

---

**[Nobody Will Pay For AI-generated Stuff](https://www.youtube.com/watch?v=C13zheVpKNY)**

They can't harm you, if they can't find you! Use code ELAI at the link below and get 60% off an annual plan: http://incogni.com/elai ...

📺 House of El: AI

👁️ 317K • 👍 11K • 💬 3K • ⏱️ 24:14 • 1d ago

---

**[ThunderCats: Pumm-Ra (1985) | Cinematic 4K AI Short Film](https://www.youtube.com/watch?v=viPDfmnhhwk)**

ThunderCatsTeaserTrailer #ThunderCatsTrailer #ThunderCatsLiveActionTrailer #thunderCats #80scartoons Experience the epic ...

📺 AIM Media Pro

👁️ 154K • 👍 3K • 💬 222 • ⏱️ 12:34 • 22h ago

---

**[How To Save AI Credits With Higgsfield + Blender (No One Talks About This Workflow)](https://www.youtube.com/watch?v=OiULPvTJ-0E)**

I block every shot in Blender before generating — locked camera, locked timing, way fewer credits burned. The Prompts: ...

📺 Higgsfield AI

👁️ 270K • 👍 6K • 💬 400 • ⏱️ 19:48 • 1d ago

---

**[If you use AI, switch to Omarchy immediately](https://www.youtube.com/watch?v=KO2T0oET9go)**

Omarchy is the best operating system for AI users ever. You need to switch now... FULL Omarchy bootcamp in the Vibe Coding ...

📺 Alex Finn

👁️ 137K • 👍 3K • 💬 498 • ⏱️ 21:46 • 1d ago

---

**[Breaking: Bill Gates TURNS on AI, WARNS of bioterror, danger, unemployment CRASH (Melber breakdown)](https://www.youtube.com/watch?v=X9oBm_oPRkQ)**

MS NOW's Ari Melber reports on tech innovator and Microsoft founder Bill Gates issuing an extensive warning about the current AI ...

📺 MS NOW

👁️ 308K • 👍 3K • 💬 717 • ⏱️ 12:17 • 2d ago

---

**[AI is changing the world, but is it also trying to kill us? Ronny Chieng investigates #DailyShow #AI](https://www.youtube.com/watch?v=J5lrvLA2QDs)**

📺 The Daily Show

👁️ 173K • 👍 9K • 💬 390 • ⏱️ 2:16 • 19h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 121,976 • ❤️ 4,324 • 3d ago

---

**[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**

*Z.ai*

GLM-5.3-Flash is a natively multimodal LLM with a hybrid sparse-linear attention architecture for efficient long-context processing. It excels in coding and agentic tasks, offering performance competitive with top models at a fraction of the cost, suitable for complex text generation and multimodal applications.

`text-generation` `321.3B`

⬇️ 346,516 • ❤️ 1,650 • 2d ago

---

**[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)**

*Z.ai*

GLM-5.3 is a text-generation model excelling in complex coding and long-horizon tasks, achieving state-of-the-art performance in coding benchmarks and emergent cyber capabilities like vulnerability discovery and exploitation.

`text-generation` `753.3B`

⬇️ 50,116 • ❤️ 1,304 • 1d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 4,511,348 • ❤️ 13,289 • 15d ago

---

**[Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)**

*Unsloth AI*

Qwen3.8-Flash-Next-GGUF is a highly efficient, multimodal causal language model featuring Hybrid Attention with QSA and N-gram Embeddings for significantly reduced long-context latency. It excels in agentic workloads and supports context lengths up to 1,000,000 tokens, making it ideal for complex reasoning and large-scale data processing.

`image-text-to-text` `176.9B`

⬇️ 328,195 • ❤️ 581 • 2d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 8,839,153 • ❤️ 3,197 • 9d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,137,181 • ❤️ 2,172 • 2d ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 725,757 • ❤️ 932 • 5d ago

---

**[Hy4-preview](https://huggingface.co/tencent/Hy4-preview)**

*Tencent*

Hy4-preview is a 770B parameter Mixture-of-Experts (MoE) text generation model with 49B activated parameters per token, featuring a 1M context length and Gated Sparse Attention. It excels in productivity tasks across software engineering, office analysis, game development, and scientific research, offering significant gains in understanding, reasoning, and code generation.

`text-generation` `780.0B`

⬇️ 2,123 • ❤️ 292 • 1d ago

---

**[GLM-5.3-Flash-GGUF](https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF)**

*Unsloth AI*

GLM-5.3-Flash is a natively multimodal LLM optimized for efficiency and capability, featuring a hybrid sparse/linear attention architecture. It excels in long-context tasks, coding, and agentic benchmarks, offering performance competitive with leading models at a fraction of the cost, suitable for advanced AI applications.

`text-generation` `320.8B`

⬇️ 45,936 • ❤️ 280 • 23h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 764 • 💬 5 • ⭐ 8,818 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 102 • 💬 2 • ⭐ 9,685 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 125 • 💬 6 • ⭐ 101,727 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 201 • 💬 3 • ⭐ 1,285 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://huggingface.co/papers/2608.24053)**

*Junjie Zhou, Ke Mei, Lei Li et al. (6 authors)*

🏢 Tencent

WeMM-Embedding is a family of universal multimodal embedding models that align text, images, videos, and interleaved inputs in a shared space, achieving state-of-the-art retrieval and recommendation performance across public benchmarks and large-scale WeChat applications.

▲ 66 • 💬 2 • ⭐ 914 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2608.24053) • [💻 code](https://github.com/Tencent/WeMM-Embedding) • [🔗 project](https://github.com/Tencent/WeMM-Embedding)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 45 • 💬 2 • ⭐ 19,107 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 85 • 💬 7 • ⭐ 85,594 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://huggingface.co/papers/2308.04079)**

*Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler et al. (4 authors)*

A method using 3D Gaussians for scene representation and optimized rendering allows high-quality, real-time novel-view synthesis at 1080p resolution.

▲ 204 • 💬 13 • ⭐ 23,657 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2308.04079) • [💻 code](https://github.com/graphdeco-inria/gaussian-splatting)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 46 • 💬 2 • ⭐ 30,065 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 68 • 💬 4 • ⭐ 30,068 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

A privacy-first app that strips AI watermarks from content you own.

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 19.3k • 🔱 2.3k • 11h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 3.5k • 🔱 435 • 1d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.3k • 🔱 257 • 18d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.3k • 🔱 397 • 11m ago

---

**[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)**

FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools, with cost-aware routing across LLM providers.

`Python` `agent` `ai` `ai-agent` `ai-coding` `autonomous-agent`

⭐ 2.9k • 🔱 176 • 6d ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.8k • 🔱 165 • 22h ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 2.8k • 🔱 298 • 2d ago

---

**[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)**

AI 短剧制作的 skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜 | Agent skills for AI short-drama production — character bibles, adaptation outlines, art bibles, screenplays, storyboards. Runs in Claude Code & codex.

`JavaScript`

⭐ 2.4k • 🔱 307 • 3d ago

---

**[ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)**

let your agent control your phone

`Python` `agent` `ai` `automation` `developer-tools`

⭐ 2.1k • 🔱 197 • 1d ago

---

**[SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI)**

WeChat AI - 自托管微信角色扮演对话服务

`TypeScript`

⭐ 1.9k • 🔱 1.3k • 6m ago

---

---

*Generated by PeekDeck - A glance is all you need*
