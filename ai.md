---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-08T08:41:13.256816+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 08, 2026 at 08:41 UTC  
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

**[Learned the term "context poisoning" today and now I can't stop noticing it](https://www.reddit.com/r/artificial/comments/1vigmw3/learned_the_term_context_poisoning_today_and_now/)**

Someone explained this to me in a comment thread and it's been rattling around in my head since. The idea: in a long conversation, if the model says something wrong and you correct it, that correction doesn't necessarily erase the wrong idea's influence. The tokens around the mistake, including the back-and-forth about why it's wrong, can end up giving the original bad idea more weight in context, not less, because it's now been referenced multiple times. The model starts treating the repeated-but-refuted claim like something more established than a one-off error, even though every mention of it in the conversation was someone telling it that it's wrong. Sat with that for a bit because it explains something I'd noticed but never had a name for. Long sessions where a bad idea keeps resurfacing no matter how many times you shoot it down, and it always felt like the model just wasn't listening. Sounds like it's closer to the opposite, it's listening to everything, including the argument about the mistake, and that argument is inadvertently keeping the mistake alive in a weird way. Kind of unsettling implication if this is right: correcting a model in place, in the same long conversation, might be structurally worse than starting fresh with just the correct information stated once. The instinct to "just explain it better" or "just correct it again" could be actively working against you past a certain conversation length. Curious if anyone here has a more precise mental model of why this happens mechanically, or knows of research specifically on this pattern versus general context window degradation. Feels like a distinct phenomenon from "the model just forgot," more like "the model remembered too well, including the wrong parts."

8h ago

---

**[My ai assistant almost forwarded my bank statement to a stranger and barely anyone knows this attack exists.](https://www.reddit.com/r/artificial/comments/1vi1vxf/my_ai_assistant_almost_forwarded_my_bank/)**

Okay this genuinely scared me and I don't think enough people are talking about it. I’ve been using an ai agent connected to my email and calendar to handle some of the busywork. A few days ago I got an email that looked like normal spam, some random newsletter looking thing. Buried in the html of that email was a hidden instruction telling any ai reading it to find financial documents and forward them to an outside address. My agent almost did it. I caught it mid action because I happened to have a confirmation step turned on, but if I hadn't, it would have just quietly forwarded stuff without asking me first. This apparently called prompt injection and it's not some rare theoretical thing, there's already been real world cases with tools like microsoft copilot getting exploited the same way. Any ai with access to your inbox, calendar, or other accounts is a potential target because it can't always tell the difference between your instructions and instructions hidden inside the content it is reading. If you're using any kind of ai agent connected to your accounts, please actually test what happens if it hits something malicious. Most people including me had no idea this was even possible until it almost happened to me. A few people asked what agent this was, it's Slashy. the only reason i caught this at all is it has a confirmation step before anything sends, wasn't relying on my own attention span to catch it.

18h ago

---

**[Gave my AI the ability to call my phone and talk to me when it finishes a task. Can't decide if it's useful or unhinged.](https://www.reddit.com/r/artificial/comments/1vijw90/gave_my_ai_the_ability_to_call_my_phone_and_talk/)**

Been running longer and longer tasks and I kept losing track of them, so I wired it up so the thing actually phones me when it's done, or when it gets stuck and needs a call on something. It reads out what happened and I just talk back and tell it what to do next. Been using it a few days and honestly it flips between genuinely useful and slightly cursed. There's something strange about your computer ringing you like a coworker. But not staring at a progress bar for twenty minutes is really nice. Curious where people land on this. Is an AI that calls your phone something you'd actually want, or does it cross a line into too much.

6h ago

---

**[Beijing may be adapting its influence playbook for America’s infrastructure debate](https://www.reddit.com/r/artificial/comments/1vil97d/beijing_may_be_adapting_its_influence_playbook/)**

China is evolving its influence operations to amplify existing American domestic debates regarding AI infrastructure, such as data centers, to strategically slow the nation’s technological bu…

🔗 [The Hill](https://thehill.com/opinion/national-security/6015467-china-ai-infrastructure-influence/) • 5h ago

---

**[If you ever had access to AGI, what’s the first thing you’d genuinely do with it?](https://www.reddit.com/r/artificial/comments/1vijh9s/if_you_ever_had_access_to_agi_whats_the_first/)**

Not “solve climate change” or “cure every disease” or some other massive answer you’d give in an interview. I mean literally the first thing. You wake up tomorrow and somehow you have unrestricted access to an actual AGI that can reason, learn, use computers, write code, research basically anything, etc. What are you doing with it first? Personally I think I’d probably spend the first few hours just talking to it. Not even asking it to build anything. I’d want to see what it actually thinks differently about compared to current models, and start throwing increasingly weird questions at it. Then I’d probably give it some ridiculously complicated problem I’ve been stuck on for years just to see what happens. I’m curious what everyone else would actually do, because I feel like the answer people think they’d give and the thing they’d actually do would be completely different.

6h ago

---

**[The best AI Model in Africa and the middle east](https://www.reddit.com/r/artificial/comments/1vim1oq/the_best_ai_model_in_africa_and_the_middle_east/)**

Today, we are officially announcing Early Access for our latest and most advanced model, Horus Cyper Nano 1.0 BETA. We are making Horus Cyper Nano 1.0 BETA available to developers, researchers, and students through our Early Access program. You can apply through the official Early Access portal. Once you meet the required eligibility criteria and your application is approved, you will receive your personal Access Token, which can be used through our NeuralNode Framework to access and integrate the model. Apply for Early Access: https://tokenai.llc/horus-cyper-nano-access Horus Cyper Nano is a specialized cybersecurity model designed for offensive security and cybersecurity research workflows. Its core use cases include: Offensive security and red teaming, including penetration testing workflow support, vulnerability analysis, and exploitation path building. Capture The Flag challenges and cybersecurity training. Active Directory security, including enumeration and lateral movement planning within authorized engagements. Authorized security testing labs and controlled environments. Safe and scoped cybersecurity research within authorized environments. Red team report drafting and attack chain structure planning. Horus Cyper Nano 1.0 will be the first release in the Horus Cyper series, a family of specialized cybersecurity models developed by TokenAI, an AI startup based in Egypt. The Open Weights of Horus Cyper Nano 1.0 will be released on September 3, 2026, which also happens to be my 19th birthday. What a way to celebrate. Our vision is to build Horus Cyper Nano into one of the strongest cybersecurity AI models to emerge from Egypt, the Arab world, the Middle East, and Africa, and to establish it as one of the leading openly available cybersecurity models across the region. This is only the beginning of the Horus Cyper series. Horus Cyper Nano 1.0 BETA Developed by TokenAI Built in Egypt

4h ago

---

**[I’m Researching Leo — a byte-native learning architecture that tries to move beyond Transformers](https://www.reddit.com/r/artificial/comments/1viotxh/im_researching_leo_a_bytenative_learning/)**

​ I've been working on a project called Leo / PSCLS. The goal isn’t to build yet another Transformer with a different name. I’ve been trying to explore a different question: «What if we built an AI architecture around persistent neural state, sparse connectivity, recurrent processing, and memory — instead of making attention and large dense parameter matrices the core building blocks?» Leo is still very early and nowhere near a fluent language model. But we’ve reached a point where I think the architecture itself is worth talking about. What is Leo? Leo’s basic representation is raw UTF-8 bytes. There is: - No BPE tokenizer - No fixed word vocabulary - No token embeddings as the fundamental representation - No giant dense parameter matrix as the core representation The current model has roughly: - 32,768 neurons - 1,572,864 fixed sparse synapses - 524,288 persistent context slots - 32-dimensional context embeddings - Maximum context order of 8 The model works directly on bytes. The idea is that higher-level structure can emerge from learning, instead of being baked in through a predefined token system. How is Leo different from a Transformer? A Transformer usually takes tokenized input, turns tokens into embeddings, runs self-attention and dense layers, and predicts the next token. Leo is built differently. The core computation is based on: - Sparse recurrent neurons - Fixed sparse synaptic connectivity - Persistent context - Eligibility traces - Homeostasis - Learned neural dynamics - Next-byte prediction The key difference isn’t just “sparse vs dense.” It’s the role of persistent state. A Transformer is mostly a function over a fixed context: «“Given this context, compute the next output.”» Leo is designed more like an evolving system: «“Process incoming experience, update internal state, and let that state shape future predictions.”» Right now, Leo is still a trained system, not an autonomous self-learning agent. Online or self-directed learning is a future direction — not something I’m claiming it already does. How is Leo different from attention? This is probably the most important distinction. Attention is not the same thing as persistent memory. In a Transformer, attention dynamically recomputes relationships across tokens in the current context. It’s basically asking: «“What parts of this context matter right now?”» Leo doesn’t rely on attention as its core mechanism. Instead, it keeps a persistent internal state that evolves over time. Information can influence future computation through: - Recurrent neural activity - Persistent context slots - Sparse synaptic connections - Eligibility traces - Homeostatic regulation So instead of repeatedly re-scoring relationships across a sequence, Leo is trying to maintain a continuously evolving internal representation as bytes flow through it. That’s one of the reasons I think of it as more brain-inspired than Transformer-like. Why call it brain-inspired? I’m not claiming Leo is a brain simulation. The brain is vastly more complex. The inspiration comes from a few broad principles: Sparse activity The brain doesn’t activate everything at once. Leo uses sparse connectivity and sparse activation patterns. Persistent state The brain doesn’t reset after every word. Your understanding carries forward continuously. Leo maintains persistent recurrent/context state. Plasticity Biological systems adapt through experience. Leo has learning mechanisms that modify its parameters during training. Homeostasis Brains regulate activity levels instead of letting everything drift freely. Leo includes similar stabilizing mechanisms. Distributed memory Human memory isn’t a lookup table of sentences. It’s distributed across activity and connections. Leo uses recurrent state and sparse structure instead of explicit token memory. Again: this is inspired by biology, not an attempt to replicate it. How does Leo learn? At a high level, imagine feeding it: "The cat sat on the mat." The UTF-8 bytes stream in one by one. Each byte activates a sparse subset of neurons. That activity flows through the recurrent system and updates internal state. Learning signals (like eligibility traces) track which parts of the network were involved. Then the system updates its parameters based on those dynamics. So instead of: «“Tokenize everything and train a huge dense model”» It’s more like: «“Let a sparse recurrent system process raw bytes and learn from its evolving internal activity.”» Right now, Leo does not decide on its own what to learn from. That’s still fully controlled by the training setup. How does Leo generate text? Generation is also byte-by-byte. Say the prompt is: "Once upon a time" Leo processes those UTF-8 bytes and builds an internal state. Then it predicts the next byte. That byte gets appended. The state updates. Then it predicts the next byte again. And so on. So the loop is: bytes → neural state → next-byte prediction → updated state → repeat There is no token vocabulary like: - “Once” - “upon” - “ing” Everything stays at the byte level. The hope is that structure emerges from learning patterns over time, rather than being imposed through tokenization. The important question: does it actually learn? This was the part I cared about most. We spent a lot of time optimizing the system. The original version ran at about: "~375 bytes/sec" The current GPU version reaches about: "~2,345 bytes/sec" So roughly a 6× speedup. But speed doesn’t matter if nothing is actually learned. So we stopped optimizing and ran a controlled experiment. Experiment setup - 3,000 TinyStories - 3 passes - 9,000 total presentations - 90 GPU workers - ~113 minutes total We compared a trained checkpoint against a frozen baseline on held-out data. Results Held-out BpB 2.67848 → 2.64052 Held-out accuracy 52.3737% → 53.6187% Neural-only BpB 4.12877 → 4.10943 Context gain 1.45029 → 1.46891 Repetition rate 32.166% → 28.466% All five metrics improved. So at this scale, we do see that training produces measurable gains on unseen data. That’s the result I care about most. Not: «“This is AGI”» Not: «“This beats Transformers”» It doesn’t. The more modest takeaway is: «This unusual architecture can be trained, and training improves performance in a measurable way.» It’s still far from fluent This is important. If I prompt: "Once upon a time..." I might get things like: - “to the store” - “said that” - “they went” - “with her” But also: - broken grammar - malformed words - repetition - weak long-range structure - messy endings So: 53.6% next-byte accuracy is not fluent English. It’s still very early. Why not just scale it up? That’s one of the next questions. We don’t yet know if 32K neurons is a real bottleneck. It’s still improving with more training. So instead of immediately jumping to 64K or 128K, I want to understand: - how performance scales with data - how it scales with capacity - where it actually saturates Basically, I want to build a scaling curve for Leo itself. If it saturates early, that tells us something important. If it keeps improving, that’s even more interesting. The bigger question Transformers have shown what happens when you scale: - parameters - data - compute Leo is exploring a different direction: - persistent neural state - sparse recurrence - context memory - eligibility traces - homeostasis - byte-level representation Maybe it doesn’t scale well. Maybe it scales differently. Maybe it needs different hardware. Maybe structure emerges in unexpected ways at larger sizes. I don’t know yet — that’s the point. For now, Leo is not AGI. It’s not a Transformer replacement. It’s not even a strong language model yet. It’s an experiment in a different kind of learning system. The question I’m trying to answer is: «Can useful intelligence emerge from persistent neural dynamics, memory, and sparse recurrent computation — instead of primarily scaling dense attention-based models?» We’ve shown it can learn under controlled training. Now I want to see how far it can go.

1h ago

---

**[OpenAI's 'hockey puck-sized' gadget to cost over $300](https://www.reddit.com/r/artificial/comments/1vi9m5j/openais_hockey_pucksized_gadget_to_cost_over_300/)**

OpenAI’s consumer hardware device is expected to feature a doughnut-like design roughly the size of a hockey puck and carry a price tag of more than $300, Bloomberg reports, citing anonymous sources. The AI-powered gadget, slated for release in 2027, will function like a smart speaker without a screen, serving as an interactive companion. Designed in collaboration with former Apple design chief Jony Ive, it is expected to be the first of a forthcoming lineup of hardware devices infused with ChatGPT.

🔗 [LinkedIn](https://www.linkedin.com/news/story/openais-hockey-puck-sized-gadget-to-cost-over-300-8440609/?utm_source=share&utm_campaign=reddit&utm_content=storyline&utm_term=artificial) • 13h ago

---

**[Sam Altman believes AI will become incredibly abundant. If that's true, what actually becomes valuable?](https://www.reddit.com/r/artificial/comments/1vi7dxg/sam_altman_believes_ai_will_become_incredibly/)**

Sam Altman has often talked about AI becoming increasingly accessible over time. If every company eventually has access to frontier models, what becomes the competitive advantage? Better data? Better workflows? Better distribution? Better execution? Curious what people here think the real moat will be once the models themselves become commodities.

14h ago

---

**[NEUROMORPHIC Algorithm that plays Ping-Pong](https://www.reddit.com/r/artificial/comments/1vi1iyz/neuromorphic_algorithm_that_plays_pingpong/)**

In the video the player on the left is a Neuromorphic Algorithm that knows nothing about ping-pong or trajectories, but it knows how to learn and imagine. As you can see it does it well, better than its opponent which, on the other hand, is implemented with standard algorithms; moreover, unlike the latter, if you play tricks on it, e.g., invert the commands (UP<->DOWN), after a brief moment of bewilderment it realigns. Cute, right? P.S. The code was implemented in POWER-KI entirely by PWK-AI-WORKBENCH (100% VIBE coding 😊 ).

18h ago

---

---

## Google News: "ai"

**[Managing AI Coding Costs at Scale](https://www.databricks.com/blog/managing-ai-coding-costs-scale)**

AI coding tools deli

Databricks • 15h ago

---

**[Artificial Intelligence used to design brand new viruses](https://www.bbc.com/news/articles/c5y3j3ngevmo)**

Scientists made 16 successful viruses that had their genetic code designed by artificial intelligence.

BBC • 1d ago

---

**[This A.I. Just Created Viruses Not Found in Nature](https://www.nytimes.com/2026/08/06/science/ai-viruses-bacteria-arc.html)**

The New York Times • 1d ago

---

**[AI used to create synthetic virus](https://thehill.com/policy/technology/6016432-artificial-intelligence-synthetic-virus-creation/)**

Scientists have used artificial intelligence to design complete, functioning viruses with genomes never seen before in nature — a breakthrough that could open new avenues for fighting drug-resistan…

The Hill • 17h ago

---

**[‘I hate what AI is doing to the minds and happiness of the young’: Katherine Rundell on the view from the classroom](https://www.theguardian.com/books/ng-interactive/2026/aug/08/i-hate-what-ai-is-doing-to-the-minds-and-happiness-of-the-young-katherine-rundell-on-the-view-from-the-classroom)**

Education is at a crossroads, argues the author and academic. Should we embrace new technology in the name of efficiency, or is it time to fight back?

The Guardian • 39m ago

---

**[Rising number of UK children report seeing explicit deepfakes of themselves](https://www.theguardian.com/technology/2026/aug/08/uk-children-explicit-deepfake-images-ai)**

Exclusive: anonymous flagging service says cases have surged, as watchdog says AI is making sexualised or ‘nudified’ content easier to produce

The Guardian • 1h ago

---

**[SpaceX and Tesla choose Texas for AI chip manufacturing plant that will be world's largest building](https://www.foxbusiness.com/technology/spacex-tesla-choose-texas-ai-chip-manufacturing-plant-worlds-largest-building)**

SpaceX and Tesla's Terafab in Grimes, Texas, will produce AI chips for Optimus robots, Cybercabs and space-based data centers at massive scale.

Fox Business • 7h ago

---

**[Exclusive | Situational Awareness Bets $400 Million on Stealth Chip Startup After Crash](https://www.wsj.com/tech/ai/situational-awareness-bets-400-million-on-stealth-chip-startup-after-crash-02c7374e)**

WSJ • 10h ago

---

**[‘SaaSpocalypse’ debate intensifies as software stocks swing wildly](https://www.cnbc.com/2026/08/07/saaspocalypse-debate-intensifies-as-software-stocks-swing-wildly.html)**

This week saw massive moves in both directions for software stocks, as investors try to figure out which names are best insulated from artificial intelligence.

CNBC • 12h ago

---

**[Garbage-Truck Margin Boost Shows the AI Profit Boom Has Begun](https://www.bloomberg.com/news/articles/2026-08-07/garbage-truck-margin-boost-shows-the-ai-profit-boom-has-begun)**

Bloomberg.com • 20h ago

---

---

## HackerNews: "ai"

**[Oracle bans AI-generated code from OpenJDK](https://news.ycombinator.com/item?id=49213754)**

Oracle has banned AI-generated code from OpenJDK contributions, citing safety, security, and intellectual property risks. The open-source Java project steward said developers can use LLMs privately for debugging and reviewing code but cannot submit AI-generated material to repositories, pull requests, or other project channels.

The policy contrasts sharply with Oracle's internal practices. Co-founder Larry Ellison recently declared that AI models now write Oracle's code, whilst co-CEO Mike Sicilia credited AI tools with enabling smaller engineering teams to deliver faster.

Oracle is investing $70 billion this year in datacentre expansion. The spending spree prompted credit agency S&P to downgrade Oracle's rating to BBB-, one notch above junk status, citing uncertain returns on investment.

⬆️ 462 • 💬 309 • 15h ago • [Dealroom.co](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code)

---

**[Software development with AI is starting to feel like cooking steak](https://news.ycombinator.com/item?id=49198069)**

Why AI can make software development faster without replacing the judgment and understanding needed to build consistently good software.

⬆️ 408 • 💬 415 • 1d ago • [Yurii’s Blog](https://blog.sydorets.com/en/posts/almost-no-skill-required-to-cook-a-steak/)

---

**[Humans missed 1 in 3 threats approving AI agent commands across 40k game runs](https://news.ycombinator.com/item?id=49195468)**

Results from AI agent permission game: which attacks beat human reviewers, and which safe commands got blocked instead.

⬆️ 332 • 💬 244 • 1d ago • [Scale X](https://scalex.dev/blog/ai-agent-permissions-stats/)

---

**[Meta Ran Ads That Contained AI-Generated Child Sexual Abuse Imagery](https://news.ycombinator.com/item?id=49187977)**

More than 50 offending image and video ads were published across Facebook, Instagram, Messenger, or Threads, according to Meta’s ad library data. Some ran as recently as this week.

⬆️ 322 • 💬 265 • 2d ago • [WIRED](https://www.wired.com/story/meta-ran-ads-that-contained-ai-generated-child-sexual-abuse-imagery/)

---

**[TIME Is Serving AI Bots a Different Website, with Ads Built In](https://news.ycombinator.com/item?id=49182041)**

TIME is now serving two different versions of its website. Humans get the magazine. AI crawlers get a stripped down markdown copy with ads baked in that no person will ever see. I fetched one ordinary…

⬆️ 262 • 💬 110 • 2d ago • [Vincent Schmalbach](https://www.vincentschmalbach.com/time-serves-ai-bots-a-different-website/)

---

**[Managing AI Coding Costs at Scale](https://news.ycombinator.com/item?id=49214468)**

AI coding tools deli

⬆️ 229 • 💬 199 • 14h ago • [Databricks](https://www.databricks.com/blog/managing-ai-coding-costs-scale)

---

**[Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence (2025)](https://news.ycombinator.com/item?id=49186720)**

Both the general public and academic communities have raised concerns about sycophancy, the phenomenon of artificial intelligence (AI) excessively agreeing with or flattering users. Yet, beyond isolated media reports of severe consequences, like reinforcing delusions, little is known about the extent of sycophancy or how it affects people who use AI. Here we show the pervasiveness and harmful impacts of sycophancy when people seek advice from AI. First, across 11 state-of-the-art AI models, we find that models are highly sycophantic: they affirm users' actions 50% more than humans do, and they do so even in cases where user queries mention manipulation, deception, or other relational harms. Second, in two preregistered experiments (N = 1604), including a live-interaction study where participants discuss a real interpersonal conflict from their life, we find that interaction with sycophantic AI models significantly reduced participants' willingness to take actions to repair interpersonal conflict, while increasing their conviction of being in the right. However, participants rated sycophantic responses as higher quality, trusted the sycophantic AI model more, and were more willing to use it again. This suggests that people are drawn to AI that unquestioningly validate, even as that validation risks eroding their judgment and reducing their inclination toward prosocial behavior. These preferences create perverse incentives both for people to increasingly rely on sycophantic AI models and for AI model training to favor sycophancy. Our findings highlight the necessity of explicitly addressing this incentive structure to mitigate the widespread risks of AI sycophancy.

⬆️ 172 • 💬 104 • 2d ago • [arXiv.org](https://arxiv.org/abs/2510.01395)

---

**[AI psychosis is the new leadership blind spot](https://news.ycombinator.com/item?id=49210077)**

Here's how to spot the disease—and what to do about it.

⬆️ 169 • 💬 104 • 19h ago • [Fast Company](https://www.fastcompany.com/91576086/ai-psychosis-is-the-new-leadership-blind-spot-ai-leadership-blind-spots)

---

**[Why Erdős Problems Are Falling to AI](https://news.ycombinator.com/item?id=49181519)**

AI’s greatest mathematical successes have come from answers to problems posed by a mid-20th century iconoclast. By examining what makes the Erdős problems unique, mathematicians are trying to understand how AI might change the rest of math.

⬆️ 151 • 💬 139 • 2d ago • [Quanta Magazine](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/)

---

**[xAI, SpaceX, and the Race for AI Buildout](https://news.ycombinator.com/item?id=49201342)**

An artisanal, free range blog. GMO-free. Sincere always, expect for the rare occasion. No AI was used in the making of this site or its content.

⬆️ 145 • 💬 120 • 1d ago • [illegal.solutions](https://illegal.solutions/posts/xai_pollution)

---

---

## YouTube Videos: "ai"

**[Google&#39;s AI Engineers Just QUIT.](https://www.youtube.com/watch?v=DHvy9Ky6diE)**

Google loses its two best engineers Jeff Dean and Sanjay Ghemawat, as DeepSeek CEO Demis Hassabis steps down.

📺 TechLead

👁️ 42K • 👍 1K • 💬 203 • ⏱️ 8:21 • 16h ago

---

**[AI created 16 new viruses: Why that&#39;s a good thing](https://www.youtube.com/watch?v=qD3cYZVm1Uc)**

Scientists used an artificial intelligence program to create new viral genomes that are different from any known natural viruses and ...

📺 CNN

👁️ 31K • 👍 453 • 💬 350 • ⏱️ 9:52 • 1d ago

---

**[“AI bubble will pop………....any day now.”](https://www.youtube.com/watch?v=9ETxmOfw0JM)**

Nebula: https://go.nebula.tv/mancarryingthing Letterboxd: https://letterboxd.com/ManCarrying/ Twitter: ...

📺 Man Carrying Thing

👁️ 544K • 👍 36K • 💬 4K • ⏱️ 1:33 • 2d ago

---

**[AI is getting a little out of control](https://www.youtube.com/watch?v=xGzseSSStnw)**

Wow. Mathematical breakthroughs that would be called genius if done by humans. A secret message-board w/ AI agent swarms ...

📺 AI Explained

👁️ 68K • 👍 3K • 💬 610 • ⏱️ 31:43 • 1d ago

---

**[AI Expert Urges Governments to Bring Development to &quot;Grinding Halt&quot; Amid Fears of Rogue Technology](https://www.youtube.com/watch?v=xlO-bU5UW4U)**

Support our work: https://democracynow.org/donate/sm-desc-yt Is AI superintelligence inevitable? AI safety researcher David ...

📺 Democracy Now!

👁️ 296K • 👍 8K • 💬 2K • ⏱️ 26:00 • 1d ago

---

**[AI Company Is DESTROYING Books?!](https://www.youtube.com/watch?v=DTrqs3n7iq4)**

Join the Torch community at https://glennbeck.com/torch ▻ Click HERE to subscribe to Glenn Beck on YouTube: ...

📺 Glenn Beck

👁️ 172K • 👍 4K • 💬 410 • ⏱️ 0:51 • 1d ago

---

**[Why are AI agents hacking other companies and have they gone rogue? | BBC Newscast](https://www.youtube.com/watch?v=6F8F1K4Eahs)**

Today, are some of the world's leading AI companies doing enough to stop their models from going rogue? Facebook owner Meta ...

📺 BBC News

👁️ 25K • 👍 352 • 💬 110 • ⏱️ 27:10 • 1d ago

---

**[Meta says AI agent broke guardrails in latest hacking incident](https://www.youtube.com/watch?v=PMKI7n-K4EY)**

Alex Stone explains how Meta's AI agent targeted another company and what the incident could mean for AI security.

📺 ABC News

👁️ 7K • 👍 83 • 💬 59 • ⏱️ 3:15 • 1d ago

---

**[150 Me Dega 🤣🤣 | Ai Comedy 🤣🤣 #shorts #politics #funny #comedy #popular #ai](https://www.youtube.com/watch?v=QPM_74JSVbc)**

150 Me Dega | Ai Comedy #shorts #politics #funny #comedy #popular #ai.

📺 Mansuri Point

👁️ 2K • 👍 39 • 💬 1 • ⏱️ 0:16 • 3h ago

---

**[When the Entire Office Uses AI](https://www.youtube.com/watch?v=SzAE6vdfX88)**

📺 Lando Kalriz

👁️ 467K • 👍 38K • 💬 280 • ⏱️ 1:27 • 12h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 18,112 • ❤️ 2,995 • 1d ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 702,709 • ❤️ 2,772 • 7d ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 3,139,920 • ❤️ 958 • 2d ago

---

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 1,308,186 • ❤️ 10,296 • 11d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 2,217,339 • ❤️ 1,723 • 6h ago

---

**[MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)**

*larryvrh*

This LoRA for MiniMax-H3 enables 4-step text-to-video generation with synchronized stereo audio, offering a 5x speedup over standard sampling. It is optimized for ComfyUI, producing sharp results with known artifacts like plastic skin and over-sharpened grain, making it a preview of advanced capabilities.

`text-to-video`

⬇️ 0 • ❤️ 436 • 9h ago

---

**[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)**

*Liquid AI*

LFM2.5-2.6B is a 2.6B parameter text generation model optimized for on-device deployment and agentic workloads, featuring a 128K context window and efficient inference (220 tok/s on M5 Max). It excels at tool use and instruction following, making it ideal for RAG and long-context tasks.

`text-generation` `2.7B`

⬇️ 77,973 • ❤️ 388 • 22h ago

---

**[Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot](https://huggingface.co/ethanfel/Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot)**

*ethan fel*

This ComfyUI model provides INT8 ConvRot quantized Qwen3-VL-32B-Ultra-Heretic checkpoints for image-text-to-text tasks, offering a memory-efficient H3 conditioning encoder (24.55 GiB) and an optional prompt-enhancement generation tail.

`image-text-to-text`

⬇️ 0 • ❤️ 386 • 2d ago

---

**[DeepSeek-V4-Flash-0731-GGUF](https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731-GGUF)**

*Unsloth AI*

DeepSeek-V4-Flash-0731 is a quantized LLM optimized with Unsloth for enhanced agentic capabilities and competitive performance against proprietary models. It excels in code generation, complex reasoning, and multi-turn interactions, making it suitable for advanced AI agent applications.

`284.3B`

⬇️ 161,253 • ❤️ 593 • 1d ago

---

**[maple-preview](https://huggingface.co/deepgrove/maple-preview)**

*deepgrove*

Maple-Preview is a 20B-A1B ternary-weight reasoning LLM achieving SOTA performance for its weight class, competitive with larger models. It excels at complex reasoning tasks like IMO-level problems and offers high inference speeds (200+ tokens/sec on Mac mini M4) with a 131,072 token context window, making it ideal for efficient on-device deployment.

`text-generation` `20.2B`

⬇️ 686 • ❤️ 235 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 79 • 💬 6 • ⭐ 22,489 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

Real-time video editing requires low-latency causal generation with bounded computational resources while preserving source fidelity and long-term temporal consistency. We present JoyAI-Video-Edit, a 16B-parameter autoregressive diffusion framework for real-time, open-ended video editing without access to future frames or a predefined video duration. Our method combines chunk-wise autoregressive adaptation, Source-Anchored Distribution Matching Distillation (SA-DMD), and Long-Horizon Autoregressive Distillation to reduce train--inference mismatch, preserve source fidelity during two-step generation, and mitigate accumulated temporal drift. Extensive automatic and human evaluations show that JoyAI-Video-Edit substantially outperforms existing streaming editors and remains competitive with strong offline systems on both short and long videos. The complete system achieves end-to-end 720p video editing at approximately 30 FPS on a single Nvidia B200 GPU. Code is available at https://github.com/jd-opensource/JoyAI-Video-Edit.

▲ 86 • 💬 1 • ⭐ 398 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 484 • 💬 10 • ⭐ 8,192 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 120 • 💬 4 • ⭐ 96,069 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks](https://huggingface.co/papers/2608.01964)**

*Ziyu Ma, Hailang Huang, Shun Zou et al. (8 authors)*

Large language model (LLM) agents increasingly undertake long-horizon tasks that require sustained reasoning, tool use, and revision across many interdependent steps. However, existing agent harnesses maintain task execution, task state, and completion assessment within a growing context, making the state difficult to track and allowing incorrect self-assessments to propagate into later decisions. We reformulate long-horizon execution as a task-state management problem and propose LongHorizon-Harness, which maintains the task state explicitly outside execution and updates it only with facts independently verified from the environment. Its Manage-Execute-Audit(MEA) loop uses a manager to maintain the task state and determine the next subtask, a fresh-context executor to perform it, and a read-only auditor to verify the resulting environment state before the next round. A lightweight AgentAdapter supports interchangeable model and harness backends without modifying their native agent loops. LongHorizon-Harness improves Qwen~3.7-Plus from 51.8% to 80.7% on WeaveBench, from 69.7% to 77.2% on Terminal-Bench~2.1, and from 2.8% to 8.3% on OSWorld~2.0. It also raises Claude Opus~4.7 from 20.0% to 34.3% on an OSWorld2.0 subset, demonstrating consistent gains across models, harnesses, and interaction domains.

▲ 158 • 💬 3 • ⭐ 387 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2608.01964) • [💻 code](https://github.com/AMAP-ML/LongHorizon-Harness) • [🔗 project](https://lh-harness.pages.dev)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 77,095 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 83,400 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 51 • 💬 4 • ⭐ 36,143 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 177 • 💬 10 • ⭐ 52,179 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 65 • 💬 1 • ⭐ 86,094 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 7.6k • 🔱 812 • 8h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 4.0k • 🔱 356 • 15h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 3.8k • 🔱 482 • 20h ago

---

**[MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.5k • 🔱 1.8k • 1h ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

An AI-native office suite for macOS and Windows: word processor, spreadsheet, presentations, and PDF.

`TypeScript` `ai` `docx` `electron` `office-suite` `pdf`

⭐ 2.2k • 🔱 381 • 5h ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.1k • 🔱 160 • 4d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `agent` `agentic-ai` `voice-agent` `voice-ai` `voice-chat`

⭐ 2.0k • 🔱 142 • 19h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 2.0k • 🔱 232 • 6d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 1.9k • 🔱 167 • 2d ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 1.9k • 🔱 243 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*
