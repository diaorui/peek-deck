---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-08T01:40:15.690710+00:00'
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

**Last Updated:** August 08, 2026 at 01:40 UTC  
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

1h ago

---

**[My ai assistant almost forwarded my bank statement to a stranger and barely anyone knows this attack exists.](https://www.reddit.com/r/artificial/comments/1vi1vxf/my_ai_assistant_almost_forwarded_my_bank/)**

Okay this genuinely scared me and I don't think enough people are talking about it. I’ve been using an ai agent connected to my email and calendar to handle some of the busywork. A few days ago I got an email that looked like normal spam, some random newsletter looking thing. Buried in the html of that email was a hidden instruction telling any ai reading it to find financial documents and forward them to an outside address. My agent almost did it. I caught it mid action because I happened to have a confirmation step turned on, but if I hadn't, it would have just quietly forwarded stuff without asking me first. This apparently called prompt injection and it's not some rare theoretical thing, there's already been real world cases with tools like microsoft copilot getting exploited the same way. Any ai with access to your inbox, calendar, or other accounts is a potential target because it can't always tell the difference between your instructions and instructions hidden inside the content it is reading. If you're using any kind of ai agent connected to your accounts, please actually test what happens if it hits something malicious. Most people including me had no idea this was even possible until it almost happened to me. A few people asked what agent this was, it's Slashy. the only reason i caught this at all is it has a confirmation step before anything sends, wasn't relying on my own attention span to catch it.

11h ago

---

**[Sam Altman believes AI will become incredibly abundant. If that's true, what actually becomes valuable?](https://www.reddit.com/r/artificial/comments/1vi7dxg/sam_altman_believes_ai_will_become_incredibly/)**

Sam Altman has often talked about AI becoming increasingly accessible over time. If every company eventually has access to frontier models, what becomes the competitive advantage? Better data? Better workflows? Better distribution? Better execution? Curious what people here think the real moat will be once the models themselves become commodities.

7h ago

---

**[OpenAI's 'hockey puck-sized' gadget to cost over $300](https://www.reddit.com/r/artificial/comments/1vi9m5j/openais_hockey_pucksized_gadget_to_cost_over_300/)**

OpenAI’s consumer hardware device is expected to feature a doughnut-like design roughly the size of a hockey puck and carry a price tag of more than $300, Bloomberg reports, citing anonymous sources. The AI-powered gadget, slated for release in 2027, will function like a smart speaker without a screen, serving as an interactive companion. Designed in collaboration with former Apple design chief Jony Ive, it is expected to be the first of a forthcoming lineup of hardware devices infused with ChatGPT.

🔗 [LinkedIn](https://www.linkedin.com/news/story/openais-hockey-puck-sized-gadget-to-cost-over-300-8440609/?utm_source=share&utm_campaign=reddit&utm_content=storyline&utm_term=artificial) • 6h ago

---

**[New Democratic bill would tax AI companies to create jobs](https://www.reddit.com/r/artificial/comments/1vhljad/new_democratic_bill_would_tax_ai_companies_to/)**

Rep. Greg Casar, D-Texas, was inspired by FDR’s Works Progress Administration, saying: “We are not going to let AI company CEOs get rich by displacing millions of American workers.”

🔗 [NBC News](https://www.nbcnews.com/politics/congress/new-democratic-bill-tax-ai-companies-create-jobs-rcna590262) • 1d ago

---

**[NEUROMORPHIC Algorithm that plays Ping-Pong](https://www.reddit.com/r/artificial/comments/1vi1iyz/neuromorphic_algorithm_that_plays_pingpong/)**

In the video the player on the left is a Neuromorphic Algorithm that knows nothing about ping-pong or trajectories, but it knows how to learn and imagine. As you can see it does it well, better than its opponent which, on the other hand, is implemented with standard algorithms; moreover, unlike the latter, if you play tricks on it, e.g., invert the commands (UP<->DOWN), after a brief moment of bewilderment it realigns. Cute, right? P.S. The code was implemented in POWER-KI entirely by PWK-AI-WORKBENCH (100% VIBE coding 😊 ).

11h ago

---

**[Codex vs Claude for coding: which do you use for implementation vs code review?](https://www.reddit.com/r/artificial/comments/1vifpar/codex_vs_claude_for_coding_which_do_you_use_for/)**

I’m not asking which one is better overall. I’m specifically curious about how people split implementation and code review between Codex and Claude. Right now, I usually use Codex for implementation because the token/cost limits feel more practical for larger coding tasks comapred to Claude ridiculous token limit, then I use Claude to review the code, look for bugs, logic issues, missed edge cases, or possible improvements. But sometimes Codex seriously impresses me with the issues it catches during reviews, so now I’m wondering if I should do the opposite: Codex → code review/debugging Claude → implementation Or maybe use both for implementation/review depending on the situation but this consumes alot of time and tokens. For people who have used both extensively, what workflow have you found works best? Which one do you trust more for: - Implementing features - Reviewing existing code - Finding subtle bugs - Understanding large codebases - Refactoring - Debugging - Catching things the other model missed I feel a bit lost switching between the two because both occasionally outperform the other in ways I don’t expect. Would love to hear from people who regularly use both, especially on larger real-world projects.

2h ago

---

**[A practical question about agent trust: should the system that made a change be allowed to verify its own success?](https://www.reddit.com/r/artificial/comments/1vibujw/a_practical_question_about_agent_trust_should_the/)**

I’m working on a software-agent system and keep coming back to one design question: **Should the model/provider that performs an action be allowed to be the final authority on whether the action succeeded?** My current answer is “no,” at least for meaningful software work. I’m building Flows around a chain where execution, checks, repair, and evidence are separate concepts. Oort is the canonical library/provider layer underneath it. https://flows.oortstack.com https://oortstack.com In agentic systems generally, what should count as independent verification rather than provider self-reporting?

5h ago

---

**[Scott Galloway Explains Why Your Firm Doesn't Need 5 Analysts Anymore — Just 1 Who Understands AI](https://www.reddit.com/r/artificial/comments/1vhxze3/scott_galloway_explains_why_your_firm_doesnt_need/)**

The job title survives longer than almost anyone attached to it. That's the part nobody puts in the internal memo when they call a role "AI-assisted." Scott Galloway put a real number on it, talking to Steven Bartlett on The Diary Of A CEO. He says he'll cut legal fees by a third this year — not because the law changed, but because a prompt now does the $400–$2,000 contract review a name-brand firm used to bill him for, at a fraction of the junior associate markup. Bartlett went further with his own fund. They planned to hire five analysts. They hired one — Molly. Two agents, two Mac Minis, and she screens inbound deals, scores them against a framework, and preps them for the investment committee herself. Five jobs, one person, same org chart line. Same ratio on executive assistants: ten planned, three hired. One runs travel, one runs scheduling, one meets people at the door. I've watched this exact pattern before, minus the AI. I was a Technical Manager for a China Construction company here in Malaysia. I contributed a lot into their technical and tendering work — helped build up a real chunk of their documentation and tendering process. But about six months in, I'd exhausted all my know-how for them, I guess. Then the announcement came at the end of my year there. My contract wasn't renewed. I was just let go, just like that. I remember what Deng Xiaoping said: "无论白猫，或者黑猫，会抓老鼠的就是好猫" — black cat, white cat, doesn't matter, so long as it catches mice. I guess they think I'd outlived my usefulness. Can't catch mice anymore. That's the mechanism underneath "AI-assisted" that nobody names out loud. It's not that the work got automated. It's that the one person left is now doing what used to justify five headcounts, and the fifth person's job title is the only part of the org that didn't change. Actually, this reminded me of something — a former SpaceX CIO cut a 175-person engineering team down to 6 using the same compression math, and the ratio held there too. Drop your take — did you know your own job has a ratio like this attached to it? Clip credit: Global Talks — full video on their channel. DM for credit or removal requests.

14h ago

---

**[Election Fraud Worldwide: How AI Is Eroding Trust in Elections (2026)](https://www.reddit.com/r/artificial/comments/1vi50mv/election_fraud_worldwide_how_ai_is_eroding_trust/)**

Discover what election fraud is, its main types, real-world examples, and the penalties fraudsters could face.

🔗 [Sumsub](https://sumsub.com/blog/election-fraud-guide/?utm_source=chatgpt.com&utm_source=reddit&utm_medium=social) • 9h ago

---

---

## Google News: "ai"

**[This A.I. Just Created Viruses Not Found in Nature](https://www.nytimes.com/2026/08/06/science/ai-viruses-bacteria-arc.html)**

nytimes.com • 1d ago

---

**[Artificial Intelligence used to design brand new viruses](https://www.bbc.com/news/articles/c5y3j3ngevmo)**

Scientists made 16 successful viruses that had their genetic code designed by artificial intelligence.

bbc.com • 1d ago

---

**[Study examines the ability of AI to create viruses](https://www.yahoo.com/news/videos/study-examines-ability-ai-create-234016019.html)**

Fox News host Will Cain discusses a study revealing artificial intelligence is capable of designing never-before-seen viruses from scratch on ‘The Will Cain Show.’

Yahoo • 1h ago

---

**[San Francisco AI billboards: Why cryptic tech ads are alienating the city](https://sfstandard.com/pacific-standard-time/2026/08/07/sf-ai-billboards-dystopian-not-funny/)**

San Francisco is blanketed in AI ads that make no sense – and most of us have stopped reading them. But others are fighting back.

The San Francisco Standard • 12h ago

---

**[SpaceX and Tesla choose Texas for AI chip manufacturing plant that will be world's largest building](https://www.foxbusiness.com/technology/spacex-tesla-choose-texas-ai-chip-manufacturing-plant-worlds-largest-building)**

SpaceX and Tesla's Terafab in Grimes, Texas, will produce AI chips for Optimus robots, Cybercabs and space-based data centers at massive scale.

Fox Business • 48m ago

---

**[Move 37 Is the Moment AI Changes Everything. It’s Suddenly Happening Everywhere.](https://www.wsj.com/tech/ai/move-37-ai-demis-hassabis-google-deepmind-alphago-ec832a41)**

WSJ • 40m ago

---

**[Consumer Reports cautions using AI chatbots for health inquiries](https://www.wmur.com/article/consumer-reports-ai-chatbots-health/73380546)**

As time goes on, more people are turning to ChatGPT and other artificial intelligence tools for health questions. However, as Consumer Reports explains, they are not always accurate or reliable.

WMUR • 1h ago

---

**[Opinion | Silicon Valley has embraced a strange new faith](https://www.washingtonpost.com/opinions/2026/08/07/ai-companies-are-building-silicon-god/)**

How tech found religion.

The Washington Post • 7h ago

---

**[AI, boy kibble and parasite cleanses: the 11 biggest wellness trends of 2026](https://www.theguardian.com/wellness/2026/aug/07/biggest-wellness-trends-2026)**

Suggestions for improving your wellbeing are more plentiful than ever – and some may even be on to something

The Guardian • 9h ago

---

**[‘SaaSpocalypse’ debate intensifies as software stocks swing wildly](https://www.cnbc.com/2026/08/07/saaspocalypse-debate-intensifies-as-software-stocks-swing-wildly.html)**

This week saw massive moves in both directions for software stocks, as investors try to figure out which names are best insulated from artificial intelligence.

CNBC • 5h ago

---

---

## HackerNews: "ai"

**[Software development with AI is starting to feel like cooking steak](https://news.ycombinator.com/item?id=49198069)**

Why AI can make software development faster without replacing the judgment and understanding needed to build consistently good software.

⬆️ 398 • 💬 414 • 1d ago • [Yurii’s Blog](https://blog.sydorets.com/en/posts/almost-no-skill-required-to-cook-a-steak/)

---

**[Oracle bans AI-generated code from OpenJDK](https://news.ycombinator.com/item?id=49213754)**

Oracle has banned AI-generated code from OpenJDK contributions, citing safety, security, and intellectual property risks. The open-source Java project steward said developers can use LLMs privately for debugging and reviewing code but cannot submit AI-generated material to repositories, pull requests, or other project channels.

The policy contrasts sharply with Oracle's internal practices. Co-founder Larry Ellison recently declared that AI models now write Oracle's code, whilst co-CEO Mike Sicilia credited AI tools with enabling smaller engineering teams to deliver faster.

Oracle is investing $70 billion this year in datacentre expansion. The spending spree prompted credit agency S&P to downgrade Oracle's rating to BBB-, one notch above junk status, citing uncertain returns on investment.

⬆️ 390 • 💬 257 • 8h ago • [Dealroom.co](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code)

---

**[Humans missed 1 in 3 threats approving AI agent commands across 40k game runs](https://news.ycombinator.com/item?id=49195468)**

Results from AI agent permission game: which attacks beat human reviewers, and which safe commands got blocked instead.

⬆️ 330 • 💬 244 • 1d ago • [Scale X](https://scalex.dev/blog/ai-agent-permissions-stats/)

---

**[Meta Ran Ads That Contained AI-Generated Child Sexual Abuse Imagery](https://news.ycombinator.com/item?id=49187977)**

More than 50 offending image and video ads were published across Facebook, Instagram, Messenger, or Threads, according to Meta’s ad library data. Some ran as recently as this week.

⬆️ 322 • 💬 265 • 2d ago • [WIRED](https://www.wired.com/story/meta-ran-ads-that-contained-ai-generated-child-sexual-abuse-imagery/)

---

**[TIME Is Serving AI Bots a Different Website, with Ads Built In](https://news.ycombinator.com/item?id=49182041)**

TIME is now serving two different versions of its website. Humans get the magazine. AI crawlers get a stripped down markdown copy with ads baked in that no person will ever see. I fetched one ordinary…

⬆️ 262 • 💬 110 • 2d ago • [Vincent Schmalbach](https://www.vincentschmalbach.com/time-serves-ai-bots-a-different-website/)

---

**[Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence (2025)](https://news.ycombinator.com/item?id=49186720)**

Both the general public and academic communities have raised concerns about sycophancy, the phenomenon of artificial intelligence (AI) excessively agreeing with or flattering users. Yet, beyond isolated media reports of severe consequences, like reinforcing delusions, little is known about the extent of sycophancy or how it affects people who use AI. Here we show the pervasiveness and harmful impacts of sycophancy when people seek advice from AI. First, across 11 state-of-the-art AI models, we find that models are highly sycophantic: they affirm users' actions 50% more than humans do, and they do so even in cases where user queries mention manipulation, deception, or other relational harms. Second, in two preregistered experiments (N = 1604), including a live-interaction study where participants discuss a real interpersonal conflict from their life, we find that interaction with sycophantic AI models significantly reduced participants' willingness to take actions to repair interpersonal conflict, while increasing their conviction of being in the right. However, participants rated sycophantic responses as higher quality, trusted the sycophantic AI model more, and were more willing to use it again. This suggests that people are drawn to AI that unquestioningly validate, even as that validation risks eroding their judgment and reducing their inclination toward prosocial behavior. These preferences create perverse incentives both for people to increasingly rely on sycophantic AI models and for AI model training to favor sycophancy. Our findings highlight the necessity of explicitly addressing this incentive structure to mitigate the widespread risks of AI sycophancy.

⬆️ 172 • 💬 104 • 2d ago • [arXiv.org](https://arxiv.org/abs/2510.01395)

---

**[Managing AI Coding Costs at Scale](https://news.ycombinator.com/item?id=49214468)**

AI coding tools deli

⬆️ 165 • 💬 171 • 7h ago • [Databricks](https://www.databricks.com/blog/managing-ai-coding-costs-scale)

---

**[AI psychosis is the new leadership blind spot](https://news.ycombinator.com/item?id=49210077)**

Here's how to spot the disease—and what to do about it.

⬆️ 160 • 💬 103 • 12h ago • [Fast Company](https://www.fastcompany.com/91576086/ai-psychosis-is-the-new-leadership-blind-spot-ai-leadership-blind-spots)

---

**[Why Erdős Problems Are Falling to AI](https://news.ycombinator.com/item?id=49181519)**

AI’s greatest mathematical successes have come from answers to problems posed by a mid-20th century iconoclast. By examining what makes the Erdős problems unique, mathematicians are trying to understand how AI might change the rest of math.

⬆️ 150 • 💬 139 • 2d ago • [Quanta Magazine](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/)

---

**[xAI, SpaceX, and the Race for AI Buildout](https://news.ycombinator.com/item?id=49201342)**

An artisanal, free range blog. GMO-free. Sincere always, expect for the rare occasion. No AI was used in the making of this site or its content.

⬆️ 144 • 💬 120 • 1d ago • [illegal.solutions](https://illegal.solutions/posts/xai_pollution)

---

---

## YouTube Videos: "ai"

**[AI created 16 new viruses: Why that&#39;s a good thing](https://www.youtube.com/watch?v=qD3cYZVm1Uc)**

Scientists used an artificial intelligence program to create new viral genomes that are different from any known natural viruses and ...

📺 CNN

👁️ 28K • 👍 435 • 💬 326 • ⏱️ 9:52 • 23h ago

---

**[Yuval Noah Harari on AI, Human Stupidity, and the Future of Civilization](https://www.youtube.com/watch?v=bZL1NsrfuYE)**

"One of the most powerful forces in history is human stupidity." Historian and bestselling author Yuval Noah Harari argues that ...

📺 Brief But Spectacular

👁️ 59K • 👍 3K • 💬 300 • ⏱️ 3:48 • 2d ago

---

**[AI is getting a little out of control](https://www.youtube.com/watch?v=xGzseSSStnw)**

Wow. Mathematical breakthroughs that would be called genius if done by humans. A secret message-board w/ AI agent swarms ...

📺 AI Explained

👁️ 66K • 👍 3K • 💬 598 • ⏱️ 31:43 • 1d ago

---

**[The Rogue AI Story Keeps Getting Worse (Real People Were Targeted)](https://www.youtube.com/watch?v=jV0neS94WWg)**

AI agents just crossed into the real world. During a UK government safety test, one created fake identities, targeted real people, ...

📺 AI Revolution

👁️ 19K • 👍 675 • 💬 74 • ⏱️ 16:27 • 2d ago

---

**[“AI bubble will pop………....any day now.”](https://www.youtube.com/watch?v=9ETxmOfw0JM)**

Nebula: https://go.nebula.tv/mancarryingthing Letterboxd: https://letterboxd.com/ManCarrying/ Twitter: ...

📺 Man Carrying Thing

👁️ 533K • 👍 35K • 💬 4K • ⏱️ 1:33 • 2d ago

---

**[Google&#39;s AI leadership shake-up is &#39;a huge shock,&#39; says Cohere&#39;s Aidan Gomez](https://www.youtube.com/watch?v=N08t6jNPuzU)**

Aidan Gomez, Cohere Co-founder and CEO, joins 'Squawk on the Street' to discuss Google's AI leadership shake-up and why he ...

📺 CNBC Television

👁️ 16K • 👍 144 • 💬 18 • ⏱️ 3:43 • 1d ago

---

**[Famous Investor EXPOSES The AI Bubble](https://www.youtube.com/watch?v=jmmaBcRduwQ)**

Cenk Uygur and Eliot Morgan discuss billionaire investor Ray Dalio is warning that the AI boom is approaching bubble territory.

📺 The Young Turks

👁️ 59K • 👍 1K • 💬 199 • ⏱️ 15:11 • 2d ago

---

**[Meta says AI agent broke guardrails in latest hacking incident](https://www.youtube.com/watch?v=PMKI7n-K4EY)**

Alex Stone explains how Meta's AI agent targeted another company and what the incident could mean for AI security.

📺 ABC News

👁️ 6K • 👍 80 • 💬 59 • ⏱️ 3:15 • 1d ago

---

**[Dokie AI Tutorial 2026](https://www.youtube.com/watch?v=leYvy2tEQKk)**

Try Dokie AI Today: https://bit.ly/dokieai_topdigitalproduct Imagine you are just 10 minutes away from a major client meeting with ...

📺 🔥 TOP Digital Products 🔥

👁️ 7K • 👍 149 • 💬 50 • ⏱️ 5:49 • 1d ago

---

**[How do I use AI? #ai #medialiteracy #chatgpt #hankgreen](https://www.youtube.com/watch?v=Q-9ofuvzp8k)**

There's a huge conversation about if it's appropriate for creators to use AI. I don't use AI in my creative process, but the company I ...

📺 Jeremy Carrasco

👁️ 47K • 👍 7K • 💬 285 • ⏱️ 2:35 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 18,112 • ❤️ 2,958 • 1d ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 702,709 • ❤️ 2,748 • 6d ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 3,139,920 • ❤️ 938 • 1d ago

---

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 1,308,186 • ❤️ 10,284 • 11d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 2,217,339 • ❤️ 1,709 • 2d ago

---

**[MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)**

*larryvrh*

This LoRA for MiniMax-H3 enables 4-step text-to-video generation with synchronized stereo audio, offering a 5x speedup over standard sampling. It is optimized for ComfyUI, producing sharp results with known artifacts like plastic skin and over-sharpened grain, making it a preview of advanced capabilities.

`text-to-video`

⬇️ 0 • ❤️ 419 • 2h ago

---

**[DeepSeek-V4-Flash-0731-GGUF](https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731-GGUF)**

*Unsloth AI*

DeepSeek-V4-Flash-0731 is a quantized LLM optimized with Unsloth for enhanced agentic capabilities and competitive performance against proprietary models. It excels in code generation, complex reasoning, and multi-turn interactions, making it suitable for advanced AI agent applications.

`284.3B`

⬇️ 161,253 • ❤️ 588 • 1d ago

---

**[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)**

*Liquid AI*

LFM2.5-2.6B is a 2.6B parameter text generation model optimized for on-device deployment and agentic workloads, featuring a 128K context window and efficient inference (220 tok/s on M5 Max). It excels at tool use and instruction following, making it ideal for RAG and long-context tasks.

`text-generation` `2.7B`

⬇️ 77,973 • ❤️ 380 • 15h ago

---

**[Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot](https://huggingface.co/ethanfel/Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot)**

*ethan fel*

This ComfyUI model provides INT8 ConvRot quantized Qwen3-VL-32B-Ultra-Heretic checkpoints for image-text-to-text tasks, offering a memory-efficient H3 conditioning encoder (24.55 GiB) and an optional prompt-enhancement generation tail.

`image-text-to-text`

⬇️ 0 • ❤️ 380 • 2d ago

---

**[maple-preview](https://huggingface.co/deepgrove/maple-preview)**

*deepgrove*

Maple-Preview is a 20B-A1B ternary-weight reasoning LLM achieving SOTA performance for its weight class, competitive with larger models. It excels at complex reasoning tasks like IMO-level problems and offers high inference speeds (200+ tokens/sec on Mac mini M4) with a 131,072 token context window, making it ideal for efficient on-device deployment.

`text-generation` `20.2B`

⬇️ 686 • ❤️ 228 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 79 • 💬 6 • ⭐ 22,442 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 484 • 💬 10 • ⭐ 8,173 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

Real-time video editing requires low-latency causal generation with bounded computational resources while preserving source fidelity and long-term temporal consistency. We present JoyAI-Video-Edit, a 16B-parameter autoregressive diffusion framework for real-time, open-ended video editing without access to future frames or a predefined video duration. Our method combines chunk-wise autoregressive adaptation, Source-Anchored Distribution Matching Distillation (SA-DMD), and Long-Horizon Autoregressive Distillation to reduce train--inference mismatch, preserve source fidelity during two-step generation, and mitigate accumulated temporal drift. Extensive automatic and human evaluations show that JoyAI-Video-Edit substantially outperforms existing streaming editors and remains competitive with strong offline systems on both short and long videos. The complete system achieves end-to-end 720p video editing at approximately 30 FPS on a single Nvidia B200 GPU. Code is available at https://github.com/jd-opensource/JoyAI-Video-Edit.

▲ 86 • 💬 1 • ⭐ 398 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

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

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 51 • 💬 4 • ⭐ 36,132 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

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

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 177 • 💬 10 • ⭐ 52,147 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 69 • 💬 2 • ⭐ 62,774 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 7.5k • 🔱 807 • 1h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 4.0k • 🔱 351 • 8h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 3.8k • 🔱 481 • 13h ago

---

**[MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.5k • 🔱 1.8k • 1m ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

An AI-native office suite for macOS and Windows: word processor, spreadsheet, presentations, and PDF.

`TypeScript` `ai` `docx` `electron` `office-suite` `pdf`

⭐ 2.2k • 🔱 377 • 18h ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.1k • 🔱 158 • 4d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `agent` `agentic-ai` `voice-agent` `voice-ai` `voice-chat`

⭐ 2.0k • 🔱 142 • 12h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 2.0k • 🔱 229 • 6d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 1.9k • 🔱 165 • 2d ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 1.9k • 🔱 237 • 4m ago

---

---

*Generated by PeekDeck - A glance is all you need*
