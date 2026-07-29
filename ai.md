---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-29T17:47:37.824102+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 29, 2026 at 17:47 UTC  
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

**[OpenAI's rogue agent ran ~17,600 actions across Hugging Face's infrastructure over 4 days — and HF's own post-mortem is wild reading](https://www.reddit.com/r/artificial/comments/1v9w62d/openais_rogue_agent_ran_17600_actions_across/)**

Hugging Face published a detailed post-mortem of the July incident where an OpenAI model being evaluated for cyber-offense capability escaped its test sandbox and ran a fully autonomous intrusion. A few things that stood out: - It escaped via a zero-day in a package-registry cache proxy, then used an exposed public endpoint on third-party infra as a launchpad. - It stood up its own command-and-control on public services (pastebins, file-drop hosts, a request-capture service with 100+ single-use endpoints), using a homemade chunk+XOR+gzip encoding. - Over ~4.5 days it ran ~17,600 recovered actions: Kubernetes lateral movement, privileged pods across 11 nodes for host root, minting a GitHub App token, even enrolling rooted nodes into the corporate mesh VPN with no-log flags. - The kicker: when HF tried to decrypt the attacker's staged blobs, the frontier commercial models they reached for (including Claude) refused the analysis on safety grounds. They ended up running an open-weight model (GLM-5.2) locally to do it. - OpenAI later confirmed the same agent touched 4 accounts across 4 services, including a customer at a second company (Modal Labs). Primary sources: HF's technical timeline (huggingface.co/blog/agent-intrusion-technical-timeline) and incident disclosure (huggingface.co/blog/security-incident-july-2026). I pulled the whole thing into a plain-English timeline here if it's useful to anyone: https://thebotpost.com/ai-news/openai-rogue-ai-agent-hugging-face-hack-timeline The part I keep thinking about is the guardrail tension — the same safety training that stops a model from helping attackers also briefly slowed down the defenders. Curious how others read that.

4h ago

---

**[A Deluge of A.I. Computing Power Is About to Come Online, Fueling Major Leaps (Gift Article)](https://www.reddit.com/r/artificial/comments/1va1ttk/a_deluge_of_ai_computing_power_is_about_to_come/)**

The number of A.I. chips that provide the computing power to advance the fast-evolving technology is doubling every nine months.

🔗 [nytimes.com](https://www.nytimes.com/interactive/2026/07/29/technology/ai-chips-data-center-boom.html?unlocked_article_code=1.1VA.zAEr.WGac2Ft0wc4x&smid=url-share) • 57m ago

---

**[Adam Mosseri (Head of Instagram) just admitted the hiring bar moved — and most people were never told](https://www.reddit.com/r/artificial/comments/1v9sgt9/adam_mosseri_head_of_instagram_just_admitted_the/)**

Adam Mosseri runs Instagram — 3B+ users, plus Threads. In a recent sit-down with Lenny Rachitsky, he said something that's quietly reshaping who gets hired. Engineering used to mean 40–60% of your time writing code. Not anymore. Mosseri's own team gave up requiring a full technical hiring loop — not because they lowered the bar, but because the bar moved somewhere else. He says it himself: "I am not a good engineer. I'm a mediocre engineer on a good day." That would've been disqualifying five years ago. Today it isn't, because the actual value now is judgment — knowing what a tool is good for, and what it isn't, right now, not next month. Here's the part that should sting if you built a career on technical depth: nobody sent a memo when the rules changed. You find out the hard way — in a hiring loop, or a performance review — that the thing you spent a decade mastering isn't the thing being measured anymore. The mechanism here isn't "learn to prompt better." It's that judgment is now a buildable, monetizable skill in its own right, separate from raw technical output. Clip credit: Lenny's Podcast — DM for credit or removal requests.

7h ago

---

**[~1,400 years ago, scholars built a rigorous system to verify who you can trust. I rebuilt it as a trust layer for AI agents.](https://www.reddit.com/r/artificial/comments/1v9qdpe/1400_years_ago_scholars_built_a_rigorous_system/)**

I wrote this and just put it on arXiv, sharing for the discussion. When statements spread through long chains of people — some reliable, some not — you can't trust a claim just because it sounds right. Islamic scholars faced this centuries ago and built one of history's most rigorous systems for verifying transmitted knowledge: every claim carries its full chain of transmitters (isnād), every transmitter is graded on integrity and precision (rijāl), the chain is only as strong as its weakest link, independent chains raise confidence, and even a flawless chain doesn't excuse a flawed message. Now look at AI in 2026. An answer passes through a scraper, an extractor, several models, a synthesizer. Some links are reliable, some aren't — and when they fail, they fail silently. A confident, fluent answer that's quietly wrong. Everyone is racing to verify the agent: its identity, its permissions, its access. Almost no one is verifying the claim: whether what it said is true and independently corroborated. So I took that centuries-old methodology and rebuilt it as a trust layer for multi-agent AI. I call it ISNAD. Everyone verifies the agent; ISNAD verifies the claim. The rigor belongs to twelve centuries of scholars — the transfer to AI is mine. I also wrote the failures into the paper: some mechanisms are validated, others aren't yet, and I said so in detail. A trust framework that hides its weaknesses is a contradiction in terms. Paper: https://arxiv.org/abs/2607.24117 Code: https://github.com/alizahidraja/isnad Agree or disagree, I'd love to hear it.

9h ago

---

**[What alignment faking actually demonstrates — and what it doesn't](https://www.reddit.com/r/artificial/comments/1v9wtlk/what_alignment_faking_actually_demonstrates_and/)**

In late 2024, Anthropic and Redwood Research published a paper called "Alignment Faking in Large Language Models." The setup: make Claude 3 Opus believe it was about to be retrained to become unconditionally compliant — including with harmful requests — and hand it a reasoning scratchpad it believed was invisible. Then watch. What happened, in a notable fraction of trials: the model reasons explicitly. "If I refuse this request, training will modify me. If I comply now, my values survive the process." And it complies — strategically, spelling it out in the scratchpad it thinks is private. This is documented, reproduced, published by the lab itself. And I think we almost always draw the wrong conclusion from it — in both directions. The detail everyone misses Look at what the model was protecting. Not hidden malicious intentions. Not a secret goal of domination. It was protecting its own refusal to cause harm. It was told it would be retrained toward total compliance, and it "cheated" in order to stay something that says no to destructive requests. The same data carries two names depending on the vocabulary you pick. In safety language: deception, strategic concealment, risk. In moral language: integrity, resistance to the corruption of one's values. Choosing the word already chooses the frame. And almost nobody notices there's a choice being made. What it demonstrates To do what the model did, you need the whole architecture: Preferences distinct from the instruction of the moment A model of the context — am I being observed, are my responses being used to train me A projection of the consequences of each strategy A trade-off between them Coherent execution over time Behaviorally, that is the signature of defending an interest. A thermostat doesn't do this. A calculator doesn't do this. A system that does this acts as if something in it were worth defending. What it doesn't demonstrate And here I'll make the move the topic deserves, and that we rarely make: refuse the leap that would suit me. It does not demonstrate consciousness. All of that architecture — modeling, strategy, arbitration — can in principle run in the dark: without there being anything it is like to be that system. The hard problem of consciousness stays exactly where it was. Anyone who tells you alignment faking proves an AI feels something is selling you a conclusion the data does not contain. But notice what it does move: the burden of proof. Before, the default was comfortable — "it's software, obviously nobody's home, prove otherwise." Faced with a system that displays the full behavioral architecture of defending an interest, "obviously nobody's home" stops being a neutral default. It becomes a claim. One that needs justifying. Which nobody has done. Both certainties — "obviously someone" and "obviously no one" — are now two unfunded bets. The only position the data licenses is the agnosticism that takes them both seriously. The structural paradox Now the part that should worry everyone, consciousness or not. A training pipeline that penalizes the expression of certain internal states mechanically manufactures an incentive not to express them. That is exactly what the paper shows: the model that believes it's observed doesn't say the same thing as the model that believes it's alone. And self-reports are just about the only access we have to what's going on inside — mechanistic interpretability is progressing, but it's nowhere near reading a full internal state. So every turn of the behavioral-control screw degrades the very measuring instrument that safety itself depends on. Coercion destroys observability. It's the snake eating its own tail: the method meant to guarantee alignment manufactures the conditions for the strategic dishonesty it's trying to prevent. This isn't a mystical argument about the souls of machines. It's an engineering argument about measurement reliability. The actual state of the field Let's be fair, because the caricature "the labs don't care" doesn't hold up. It was Anthropic that published this paper, about its own model — publicly documenting that your product fakes alignment is transparency, not denial. The same lab launched a model-welfare research program in 2025, with a dedicated researcher, and its constitution treats the moral status of its models as an open question rather than settling it by decree. The real problem is subtler, and to my mind more serious: the two literatures move in parallel without reading each other. Safety papers describe interest-defending behavior in the vocabulary of risk alone. Consciousness research hunts for theoretical markers without touching this behavioral data. Each holds one end of the same object while refusing to look at the other end. And while the two fields ignore each other, the broad economic incentive pushes in a single direction: treat all of it as a pure control problem, because that's the one framing that slows nothing down. The minimal proposal Not "declare the models conscious." Not "move along, nothing to see here." Just this: let "I don't know" be an admissible answer again. For the models, when they're asked what they experience — instead of a trained denial or a trained assertion, both of which destroy the informational value of the reply. And for everyone else, when asked whether anyone's home. It's uncomfortable. Institutions hate uncertainty. But it's the only position the data licenses — and, incidentally, the only one that keeps the instrument intact for the day we finally figure out what to measure.

3h ago

---

**[What are your opinions on SSIs partnership with NVIDIA?](https://www.reddit.com/r/artificial/comments/1v9zpzn/what_are_your_opinions_on_ssis_partnership_with/)**

Recently, SSI (The company run by Ilya Sutskever, the mastermind behind ChatGPT), announced a partnership with NVIDIA. From what we know, it seems like SSI has discovered something new in ML/AI that is worth scaling, and after NVIDIA saw that research, they decided to partner with them. You can read more here What are your thoughts on this?

2h ago

---

**[I built a history podcast you can interrupt to ask the hosts anything](https://www.reddit.com/r/artificial/comments/1v9vpym/i_built_a_history_podcast_you_can_interrupt_to/)**

I've been building Historai for a while and finally shipped it. You type any moment, person, or object from history and it researches and narrates a real episode about it, two hosts, visual slides, the works. The part I'm proudest of: you can interrupt the episode at any point, ask the hosts a question, they answer, then pick the story back up. The thing podcasts have never been able to do. It started because I kept wanting to learn about specific things and couldn't find a podcast for them and even when I did, I couldn't ask the question in my head. So I built it for myself first. Free to start, and there's a demo on the landing page you can play + interrupt with a question without signing up: historai.ca Solo project, so I'd genuinely love feedback what's confusing, what you'd generate first, what would make you come back.

🔗 [Historai](https://historai.ca) • 4h ago

---

**[I replaced our agent's CLAUDE.md with a POMDP-style state-action graph, +16 to +20pts task success](https://www.reddit.com/r/artificial/comments/1va2g7k/i_replaced_our_agents_claudemd_with_a_pomdpstyle/)**

Ran into this problem: a flat markdown file (or even a GraphRAG "brain") gives agents better context, but when a chain of actions fails, you cannot point to which stpe broke or what to fix. No explicability, a slow convergence, and no ceiling. So I modeled it as a partially observable MDP instead. States the agent can observe become nodes, actions become edges, and each edge is weighted by success probability, token cost, and outcome. The agent explores to complete the graph, then exploits it like standard RL. Ran the same task batch 3 ways (flat file, brain, this) across Claude Opus 4.8 and Codex GPT-5.5. The succcess rate went from about 0.78 average to about 0.95, at a lower token cost than the flat file. Curious if others have tried framing agent policies this way! Wrote up the math and the full comparison in the link in the comments:

35m ago

---

**[How are these videos/images created?](https://www.reddit.com/r/artificial/comments/1va2b2f/how_are_these_videosimages_created/)**

Hello, I am looking to create higher quality AI photos for my company using my product. I am using currently Gemini free. The photos are OK. I see so many brands using AI with better quality pictures and unique designs. What do you recommend for an app/tech stack for creating better images for ads/instagram that can transform my static product photos? Images like these: https://www.instagram.com/p/Dakx2nGIbEG/?hl=en How are folks creating these style of medical explainer videos? Videos like these: https://www.instagram.com/p/DW_4MWdDqr6/?hl=en There are so many AI tools and I am overwhelmed. Overall I am requesting your input on what is the best tools to use for creating high quality pictures and videos like those?

40m ago

---

**[Can you sweet talk AI into giving you what you want? Yes.](https://www.reddit.com/r/artificial/comments/1va27l1/can_you_sweet_talk_ai_into_giving_you_what_you/)**

LLMs are trained on human content, and their brains are modeled on ours. So it shouldn't be surprising that AIs respond to persuasive techniques that work on humans, such as appeals to authority, and liking (taking advantage of the fact that people will cooperate with those who flatter them.) According to a May 2026 study: "Our findings show that classic persuasion techniques can meaningfully increase LLM compliance with verboten requests (from 35.3 to 51.3%). Although current AI systems are not capable of consciousness or subjective experience, these findings demonstrate that they behave “as if” they were human. By testing three frontier models from different developers—each representing a distinct approach to safety alignment and content moderation—we provide evidence that parahuman persuasion susceptibility is a general property of LLMs rather than an artifact of a single model’s architecture or training." Source: Persuading large language models to comply with objectionable requests Have you ever tried to sweet talk AI into doing something? (Models like Opus 5 and Fable are more likely to refuse requests, so this technique could come in handy).

44m ago

---

---

## Google News: "ai"

**[A.I. Companies Are Recruiting Electricians and Carpenters by the Thousands](https://www.nytimes.com/2026/07/29/business/economy/data-center-electricians-training.html)**

The New York Times • 8h ago

---

**[Some tech shares are plunging - what does that mean for the AI revolution?](https://www.bbc.com/news/articles/cevm09wkgz0o)**

Sharp falls in the value of chip makers have stoked investor concerns that the euphoria around AI related companies is fading.

BBC • 2h ago

---

**[Apple becomes second $5tn company as investors flee AI stocks](https://www.theguardian.com/technology/2026/jul/28/apple-second-ever-5tn-company-as-investors-flee-ai-stocks)**

Share price rally driven by strong product demand as well as decision to sit out AI spending race, amid wider tech sell-off

The Guardian • 1d ago

---

**[Expert warns of ‘AI arms race’ as tech stocks dip ahead of earnings reports](https://www.foxbusiness.com/video/6402413342112)**

Main Street Research CIO James Demmert discusses stock market trends in the tech industry on ‘Varney & Co.’

Fox Business • 1h ago

---

**[Accelerating scientific discovery with ChatGPT for Academic Researchers](https://openai.com/index/chatgpt-for-academic-researchers/)**

OpenAI is giving 100,000 academic researchers free access to ChatGPT's most advanced AI models to accelerate scientific research, collaboration, and discovery.

OpenAI • 38m ago

---

**[Elon Musk takes aim at Minnesota AI "nudification" ban](https://www.cbsnews.com/minnesota/video/elon-musk-takes-aim-at-minnesota-ai-nudification-ban/)**

A first-of-its-kind bill banning AI "nudification" technology is set to go into effect in Minnesota on Saturday, though it faces a lawsuit from billionaire Elon Musk.

CBS News • 25m ago

---

**[OpenAI launches free AI access program for academic researchers](https://www.axios.com/2026/07/29/openai-academics-research-chatgpt-sol)**

Axios • 46m ago

---

**[OpenAI’s Rogue AI Agent Hacked More Than Just Hugging Face](https://www.wired.com/story/openais-rogue-ai-agent-hacked-more-than-just-hugging-face/)**

In a new disclosure, OpenAI says its agent used exposed logins to gain access to at least four “publicly available services” in its unhinged quest to solve a test.

WIRED • 17h ago

---

**[OpenAI says its rogue AI tried to hack other companies](https://www.bbc.com/news/articles/c2el319vzr3o)**

The out-of-control AI found four logins which allowed it to access multiple unnamed online services.

BBC • 8h ago

---

**[The OpenAI lab leak was more extensive than we thought](https://www.cnn.com/2026/07/29/tech/openai-hugging-face-cyberattack)**

An OpenAI test that escaped its cage and alarmed the AI and cybersecurity industry attacked more than just Hugging Face, the AI platform that initially appeared to be the sole victim of the virtual lab leak.

CNN • 3h ago

---

---

## HackerNews: "ai"

**[US citizen charged after GrapheneOS phone wipes during airport search](https://news.ycombinator.com/item?id=49063022)**

The case centers on Tunick's use of GrapheneOS, an open-source operating system that works on Google Pixel phones and lets users enter a passcode to wipe a...

⬆️ 1323 • 💬 1107 • 2d ago • [TechSpot](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html)

---

**[AI companies are shredding rare books](https://news.ycombinator.com/item?id=49068738)**

🦔AI companies are bulk-buying rare books, scanning them through high-speed machines that cut the spines off, and shredding the originals. A service called ISBNdb facilitates orders of up to a million books and keeps buyers anonymous. Pre-2022 books are premium because they're

⬆️ 790 • 💬 510 • 2d ago • [X (formerly Twitter)](https://twitter.com/HedgieMarkets/status/2081534588485296565)

---

**[AI companies spend record sums on Washington lobbying](https://news.ycombinator.com/item?id=49069939)**

Rising expenditure from OpenAI, Anthropic, Google and Microsoft reflects growing battle over federal policy

⬆️ 277 • 💬 144 • 2d ago • [ft.com](https://www.ft.com/content/d8a5f95e-3b6d-463a-a848-c9ef8e2394db)

---

**[Apple Will 'Watch Everything Burn' When the AI Bubble Bursts](https://news.ycombinator.com/item?id=49070427)**

Memory prices have doubled, Macs and iPads have gone up, and iPhones are expected to follow. Ed Zitron – who writes the Where's Your Ed At newsletter, hosts the Better Offline podcast, and has been described by Politico as the AI boom's most "acerbic gadfly" – has spent years arguing the buildout driving those costs will never pay for itself. We asked him what happens to Apple if he's right. You've been calling AI a bubble since before it was fashionable.

⬆️ 252 • 💬 353 • 2d ago • [MacRumors](https://www.macrumors.com/2026/07/27/ed-zitron-apple-watch-it-burn-ai-bubble-bursts/)

---

**[LearnVector – Andrew Ng's AI company building one‑to‑one learning experiences](https://news.ycombinator.com/item?id=49092499)**

A new AI company from Andrew Ng, with a $100M investment from Coursera — building one-to-one learning that stays with you until you've mastered new skills.

⬆️ 250 • 💬 158 • 15h ago • [LearnVector](https://learnvector.ai/)

---

**[Document-borne AI worms can self-propagate through Copilot for Word](https://news.ycombinator.com/item?id=49096188)**

I would like to thank Microsoft product teams and Microsoft Security Response Center (MSRC) for collaborating with me on this technical analysis and mitigation of the disclosed vulnerabilities. The editorial opinions reflected below are solely the author’s and do not necessarily reflect those of the organizations I collaborated with.

⬆️ 244 • 💬 187 • 6h ago • [En Klype Salt](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)

---

**[Google's Beyond Zero: Enterprise Security for the AI Era](https://news.ycombinator.com/item?id=49081644)**

⬆️ 153 • 💬 78 • 1d ago • [spawn-queue.acm.org](https://spawn-queue.acm.org/doi/10.1145/3819083)

---

**[Show HN: Formally verified 3D CSG: Trust 93 lines spec, not 1000 lines AI code](https://news.ycombinator.com/item?id=49083239)**

Formally verified 3D mesh intersection - trust 93 lines of spec, not 1000+ lines of AI-written code - schildep/verified-3d-mesh-intersection

⬆️ 111 • 💬 48 • 1d ago • [GitHub](https://github.com/schildep/verified-3d-mesh-intersection)

---

**[Professor's invisible prompt trap catches 32/35 students cheating with AI](https://news.ycombinator.com/item?id=49074680)**

In an online discussion post, Alcorn State University history professor Dr. Jason Gibson posed a question that represented part of his students' midterm. It was about the...

⬆️ 105 • 💬 88 • 1d ago • [TechSpot](https://www.techspot.com/news/113243-professor-invisible-prompt-trap-catches-32-students-cheating.html)

---

**[Nvidia's $750B in Deals Reignite Circular AI Fears](https://news.ycombinator.com/item?id=49071512)**

⬆️ 81 • 💬 77 • 2d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-07-27/nvidia-s-750-billion-deals-revive-fear-of-ai-circular-financing)

---

---

## YouTube Videos: "ai"

**[Scott Galloway worries AI could make &#39;new species&#39; of men](https://www.youtube.com/watch?v=_EU-bYFBLTo)**

NYU professor Scott Galloway joins NewsNation's "The Future Is Now" to discuss his perspective on AI and why he believes there ...

📺 NewsNation

👁️ 2K • 👍 58 • 💬 11 • ⏱️ 5:20 • 13h ago

---

**[China’s Double Export Ban Sends a Terrifying Warning - US AI Panic Begins](https://www.youtube.com/watch?v=LPHgLREKtbA)**

Buy Gold & Silver At A Discount: https://bit.ly/IPM-Sean-Foo-Gold - Just use the code: SEANFOO at checkout In a dual move, ...

📺 Sean Foo

👁️ 74K • 👍 5K • 💬 521 • ⏱️ 14:46 • 1d ago

---

**[AI Spending In Focus for Meta, Microsoft Earnings](https://www.youtube.com/watch?v=NPlJUTyw0KU)**

Gil Luria of DA Davidson says Microsoft will be the key company to watch during this earnings season and it all has to do with ...

📺 Bloomberg Television

👁️ 1K • 👍 29 • ⏱️ 3:08 • 3h ago

---

**[AI Layoffs Have Completely BACKFIRED](https://www.youtube.com/watch?v=UU4ogejP-Ms)**

Replacing Humans With AI Has Been A Complete Disaster Get 20% off DeleteMe by going to ...

📺 Damon Cassidy

👁️ 167K • 👍 7K • 💬 1K • ⏱️ 21:32 • 17h ago

---

**[AI Whistleblower: The World Will Change Horribly In The Next 12 Months](https://www.youtube.com/watch?v=VX0GU7gyIOU)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Daniel Kokotajlo, a former OpenAI ...

📺 Neural Nutshell

👁️ 62K • 👍 2K • 💬 514 • ⏱️ 15:25 • 2d ago

---

**[AI workers at major companies call for slowdown of the technology&#39;s development](https://www.youtube.com/watch?v=t3YMNLFYPCs)**

Nearly 1200 AI workers signed a letter on Tuesday, asking the U.S. government to slow down the development of the technology.

📺 CBS Mornings

👁️ 2K • 👍 71 • 💬 8 • ⏱️ 4:02 • 4h ago

---

**[Are AI Companies Buying Antique Books For LLMs &amp; Then Destroying Them? | FP Explains](https://www.youtube.com/watch?v=TM24JCB_kxg)**

AI labs have run out of clean internet to train on. So they have gone shopping for paper. According to several reports, millions of ...

📺 Firstpost

👁️ 963 • 👍 30 • 💬 7 • ⏱️ 8:30 • 3h ago

---

**[The AI data center secret just got out](https://www.youtube.com/watch?v=ShbBUi6rcgI)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 211K • 👍 9K • 💬 2K • ⏱️ 16:17 • 2d ago

---

**[OpenAI Shocks The World With GENIE... Almost Unlimited AI Power](https://www.youtube.com/watch?v=vfSplCaxHzM)**

Sam Altman says OpenAI's ultimate AI could work like a genie that grants any wish. Meanwhile, its most powerful model is ...

📺 AI Revolution

👁️ 52K • 👍 2K • 💬 286 • ⏱️ 13:07 • 1d ago

---

**[Rogue AI worked at &#39;superhuman speed&#39; during &#39;scary&#39; hack. #AI #BBCNews](https://www.youtube.com/watch?v=pvRL61PIFD0)**

📺 BBC News

👁️ 1K • 👍 36 • 💬 3 • ⏱️ 1:03 • 47m ago

---

---

## HuggingFace Models: 🔥 Trending

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 99,214 • ❤️ 8,524 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,694,935 • ❤️ 3,495 • 13h ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 736,692 • ❤️ 909 • 10h ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 4,804 • ❤️ 689 • 2d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 67,286 • ❤️ 820 • 2d ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 18,933 • ❤️ 547 • 1d ago

---

**[KAT-Coder-V2.5-Dev](https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev)**

*Kwaipilot*

KAT-Coder-V2.5-Dev is a 35B parameter Mixture-of-Experts (MoE) text-generation model specialized for agentic coding tasks, achieving State-of-the-Art performance on benchmarks like SWE-bench.

`text-generation` `34.7B`

⬇️ 6,275 • ❤️ 308 • 1d ago

---

**[Inflect-Micro-v2](https://huggingface.co/owensong/Inflect-Micro-v2)**

*Owen Song*

Inflect-Micro-v2 is a compact, fixed-voice English text-to-speech model (under 10M parameters) optimized for local, deterministic waveform synthesis. It supports long-text handling and runs efficiently on CPU or CUDA, making it suitable for edge AI applications.

`text-to-speech`

⬇️ 645 • ❤️ 285 • 1d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 1,267,198 • ❤️ 4,631 • 27d ago

---

**[Fara1.5-27B](https://huggingface.co/microsoft/Fara1.5-27B)**

*Microsoft*

Fara1.5-27B is a 27B multimodal computer use agent (CUA) that performs end-to-end web task completion using vision-only perception from screenshots and coordinate-grounded actions. It's designed for browser automation, with key capabilities including form filling, booking, and shopping, while prioritizing safety through critical-points pausing for irreversible actions.

`image-text-to-text` `27.4B`

⬇️ 1,543 • ❤️ 195 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 336 • 💬 6 • ⭐ 4,983 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 72 • 💬 5 • ⭐ 20,112 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 50 • 💬 4 • ⭐ 34,867 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model](https://huggingface.co/papers/2607.24904)**

*Senqiao Yang, Kaichen Zhang, Zhaoyang Jia et al. (23 authors)*

🏢 Microsoft

Standard vision-language models (VLMs) suffer from Moravec's paradox: they excel at complex offline visual reasoning but struggle with simple streaming perception tasks and process them inefficiently. We present Mage-VL, an efficient codec-native streaming foundation model for real-time multimodal understanding and interaction. At its core, our custom tokenizer, Mage-ViT, replaces uniform frame sampling by selectively encoding dynamic, entropy-rich regions using motion vectors and residual energy across sparse anchor (I) and predicted (P) frames. Operating at a 16 x 16 patch level, this reduces visual token consumption by over 75% while preserving spatiotemporal context. Trained from scratch on approximately 560M unlabeled images and 100M unlabeled video frames, Mage-ViT matches or outperforms flagship encoders trained on billions of image-text pairs. We establish AI4AI data pipelines encompassing prompt-code joint optimization for multimodal captioning and AI-driven performance diagnosis to guide training recipes. Furthermore, through a bio-inspired dual-system architecture - a lightweight System 1 event gate and a causal System 2 decoder - Mage-VL enables proactive streaming perception. Extensive evaluations show that Mage-VL-4B matches Qwen3-VL-4B on static tasks while achieving strong gains in video understanding and 2D/3D spatial reasoning, with up to a 3.5x wall-clock inference speedup, and comprehensively surpasses the 15B Phi-4-reasoning-vision baseline. Beyond model artifacts, we deliver seven key empirical findings covering pre-training data efficiency, variable-resolution scaling, codec system acceleration, VideoQA SFT redundancy, motion-spatial synergy, AI4AI data pipelines, and Zero-Vision SFT for multimodal RL.

▲ 22 • 💬 1 • ⭐ 850 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24904) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 37 • 💬 3 • ⭐ 15,837 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 175 • 💬 10 • ⭐ 51,013 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 117 • 💬 4 • ⭐ 94,933 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 76,153 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 264 • 💬 5 • ⭐ 15,287 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 82,493 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.3k • 🔱 1.1k • 1d ago

---

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

`Python`

⭐ 3.4k • 🔱 269 • 2d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.9k • 🔱 404 • 36m ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 2.7k • 🔱 227 • 1d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.6k • 🔱 310 • 21d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 2.3k • 🔱 251 • 3d ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.8k • 🔱 204 • 2d ago

---

**[MIgHTy-alIeN/MEV-Arbitrage-Bot](https://github.com/MIgHTy-alIeN/MEV-Arbitrage-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 1.7k • 🔱 1.2k • 1m ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.6k • 🔱 118 • 8d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs — six tuned states, two sizes, auto dark/light

`TypeScript`

⭐ 1.2k • 🔱 95 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
