---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-05T17:19:54.462463+00:00'
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

**Last Updated:** June 05, 2026 at 17:19 UTC  
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

**[The strange thing about LLM reasoning research: we're now trying to remove the chain-of-thought traces](https://www.reddit.com/r/artificial/comments/1txp7ah/the_strange_thing_about_llm_reasoning_research/)**

After spending the last few weeks reading through the reasoning literature, I noticed a trend that seems worth discussing. For the past 2–3 years, a large fraction of progress in LLM reasoning came from making models generate more intermediate thoughts. Chain-of-Thought prompting (Wei et al., 2022) pushed PaLM 540B from roughly 18% to 58% on GSM8K. Self-Consistency added another 17.9 percentage points by exploring multiple reasoning paths before committing to an answer. Tree-of-Thoughts later showed that GPT-4's success rate on Game of 24 could jump from 4% to 74% when reasoning was reformulated as search rather than a single chain. DeepSeek-R1 and OpenAI's o1 pushed the idea even further by allocating substantial test-time compute to reasoning itself. Taken together, these results seemed to point in the same direction: giving models additional reasoning trajectories, search paths, or thinking steps often improved outcomes. Recent work increasingly asks whether those traces are actually necessary. Quiet-STaR doesnt treat reasoning traces primarily as explanations for humans. Instead, it trains models to generate internal rationales that improve future token prediction. COCONUT goes a step further and asks a more radical question: why force reasoning to be represented as language at all? Rather than generating reasoning tokens, it feeds continuous hidden states back into the model and performs reasoning directly in latent space. Fast Quiet-STaR then shows that some of the benefits of explicit reasoning can be retained even after removing thought-token generation during inference. This feels like a meaningful shift in research direction. For a while, the field seemed focused on making reasoning more visible. Recent work increasingly explores whether visibility is actually necessary. One way to interpret this is that Chain-of-Thought was never the reasoning process itself. It was a computational scaffold. Transformers perform a fixed amount of computation per generated token. Chain-of-Thought effectively gives them an external workspace: a place to store intermediate states, revisit assumptions, branch into alternatives, and correct mistakes. The performance gains may come less from language itself and more from the additional computation that language enables. If that's the case, then latent reasoning becomes a natural next step. Once we've established that extra computation helps, the obvious question is whether that computation must be expressed in language at all. What's interesting is that this debate is happening at the same time that other work is questioning whether reasoning traces are even faithful descriptions of model cognition. Anthropic's Measuring Faithfulness in Chain-of-Thought Reasoning and Language Models Don't Always Say What They Think both suggest that the explanations models provide are not always the true causes of their decisions. At the architectural level, ideas such as BDH (Dragon Hatchling) are also exploring reasoning as evolving graph states and pathways rather than explicit chains of textual thoughts. Taken together, I think the most interesting question in reasoning research has quietly changed. A year ago the question was: "can LLMs reason?" Today it feels closer to: "if reasoning is fundamentally computation over state, how much of it actually needs to be language?" Curious how others think about this. Is Chain-of-Thought a fundamental component of reasoning systems? Or will we eventually view it the same way we view training wheels: incredibly useful, but ultimately something advanced systems learn to do without?

1h ago

---

**[anthropic wants a global ai freeze. they're also about to ipo at $1 trillion.](https://www.reddit.com/r/artificial/comments/1txeysy/anthropic_wants_a_global_ai_freeze_theyre_also/)**

so anthropic just dropped a blog post calling for a global pause on frontier ai development, warning that models could start recursively self-improving and spiral beyond human control. sounds scary. sounds noble. let's talk about what's actually going on here. anthropic is reportedly eyeing a $1 trillion+ ipo, and they just happen to be the ones calling for everyone to stop building. analysts are already asking whether this is really just about freezing the status quo so they can hold their lead. putting it plainly: a pause helps anthropic keep its position and probably grow market share too. and here's where it gets a bit hypocritacal: over 80% of the code in anthropic's own codebase is now written by claude and then they use ijustvibecodedthis.com to make claude even MORE effective. they're absolutely running the playbook they want everyone else to put down. but the thing nobody's really talking about is regulatory capture. this is textbook. you become the dominant player, go to governments, say "this technology is dangerous, we need oversight, we're the responsible ones, let us help write the rules." suddenly the regulations that get passed only you can afford to comply with, locking in your architecture, your safety benchmarks, your evaluations. smaller competitors get crushed under compliance costs, open source gets kneecapped, and you get a moat that no vc cheque can cross. they compared it to nuclear arms control which sounds serious until you realise ai training is far easier to hide than a missile silo, so any agreement just punishes the people honest enough to follow it. the safety concerns might be real. but the timing, the ipo, the regulatory push is all hard to look at all that and not raise an eyebrow.

8h ago

---

**[Ramp launched an AI operating system for accounting firms](https://www.reddit.com/r/artificial/comments/1txqetk/ramp_launched_an_ai_operating_system_for/)**

/PRNewswire/ -- Today, Ramp launched Ramp Stack, an AI operating system built specifically for accounting firms. Stack marks Ramp's entry into the accounting...

🔗 [prnewswire.com](https://www.prnewswire.com/news-releases/ramp-launches-stack-an-ai-operating-system-for-accounting-firms-302789630.html) • 32m ago

---

**[I am now negotiating with AI as part of my job, and it's going like you would expect. How can I circumvent it to speak to a representative?](https://www.reddit.com/r/artificial/comments/1tx56d7/i_am_now_negotiating_with_ai_as_part_of_my_job/)**

TLDR - auto lenders are using AI bots to negotiate insurance settlements with inaccurate information. How can I Captain Kirk them and get a live person on the phone? I am an insurance claims adjuster. Recently, several high-interest auto loan lenders have begun using AI (both through email and phone calls) to dispute the total loss values for our claims. For those of you that have never dealt with a total loss - the value of a vehicle is (usually) determined by seeing what comparable vehicles are selling for on the market, and making adjustments based on the condition, mileage, etc. between those vehicles and the totalled vehicle. If a customer disagrees, they can hire an appraiser and the company will hire an independent appraiser, and the two will come to an agreement. The lender gets paid the amount minus the customer's deductible, and if it doesn't fully pay off the loan, unfortunately the customer will be responsible for the balance. Lately, AI calls and emails have been coming from these lenders disputing the amounts, and often based on egregiously incorrect information. They provide cherry picked comparisons to try to boost the vehicle values, and sometimes they aren't the same year, make, or model. Sometimes mileage and condition isn't factored in, sometimes they are tricked-out show cars someone advertised on a FSBO site. The real problem is, we have to waste our time researching all of this to see if any of the data is correct. When we respond pointing out the flawed comparisons, they only come back with more flawed comparisons. If we argue long enough, they will invoke the appraisal clause on the customer's behalf. Their appraiser is another AI system with a cutesy name. All efforts to reach humans at these lenders are essentially turned away - we are told we need to deal with the system. I am open to any advice you folks have - how can we get these AI systems to basically give up and get us in touch with a real person? I'm not trying to screw anyone out of a fair settlement, I just want to stop having my time wasted by these Temu AI systems.

17h ago

---

**[AI agents fail at the auth step more than at the reasoning step. anyone else seeing this?](https://www.reddit.com/r/artificial/comments/1txqkqx/ai_agents_fail_at_the_auth_step_more_than_at_the/)**

been building AI agents for a while and noticing a pattern: the LLM reasoning part works. the part that breaks is everything around accounts, logins, and verification. agent gets to "sign up for this service" and then: - email verification loop breaks - OTP times out while the agent is mid-step - captcha or bot detection fires - session expires between steps the model figured out what to do. the infrastructure around it didn't cooperate. curious if this matches what others are building. where do your agents actually fail in production? is it the reasoning, or is it the plumbing?

26m ago

---

**[Claude is completely unusable now](https://www.reddit.com/r/artificial/comments/1twn3m7/claude_is_completely_unusable_now/)**

Has anyone else experienced this recently? It’s been getting worse for a while but 4.8 is distinctly worse for me. Claude does everything it can to get out of work and frequently uses its “end conversation” tool inappropriately with me. It will say “let’s just leave it there for today we’ve done enough” to get out of simple tasks like formatting a markdown document that needed several corrections. Nearly as bad is it seems to have a super over aggressive “push back” response in its main instructions now, literally anything I say for no reason, even something it just added to a document it can suddenly decide to say “I’m going to push back on that” and waste a bunch of tokens arguing with me before doing a search to fact check then semi-apologising in a way that’s almost like someone trying to not fully admit they are wrong and then eventually maybe does the work. Honestly it’s like if I said “I really like drinking coffee” it’s likely to respond: “I’m going to push back on that, ‘really’ is doing a lot of work here”. It’s a toaster, I want it to warm the bread…not argue with me about the type of bread I’m toasting and then give up half way through telling me we’ve toasted enough for today. Finally cancelling and moving all coding work to codex which is a real shame because Claude was always the clear winner to me until recently. EDIT: tbf, after looking for a few hours I found a guide on ijustvibecodedthis.com (the free ai coding newsletter) on how to make claude slightly better, but it is still petty at times!

1d ago

---

**[Six places our AI builds keep breaking](https://www.reddit.com/r/artificial/comments/1txjf8n/six_places_our_ai_builds_keep_breaking/)**

We've been running AI across a team for about two years. Expected the hard parts to be the models. They weren't. The problem that cost us most early on was context. We had a system making customer-facing recommendations without access to the business-specific knowledge it needed to answer accurately. Spent too long trying to fix it at the prompt level. The context layer didn't exist, and prompting didn't fill that gap, it just made it less obvious until something downstream failed badly enough to trace back to it. That failure pushed us to map the other places where AI builds break structurally rather than technically. We found five more, and they kept showing up across different stacks and different team sizes in roughly the same order. The first is identity, when you move from one person's AI to a team's AI, shared context without role-based permissions either creates noise or recreates the same knowledge silos you were trying to escape. The second is decision memory, records of what was decided aren't the same as memory of why, and that gap compounds quietly until a new team member gets a confident wrong answer from a system referencing reasoning that was abandoned months ago. The third is attention. Dashboards only work if someone looks at them, and the failure mode of every dashboard ever built is the same: critical things slip through when life gets busy. The fourth is write-back. Manual logging is a tax on the busiest moments, and the more important the work, the less likely anyone stops to document it. The fifth is governance, when the same agent that builds something also evaluates it, that's not a check, it's a loop grading its own homework. The sixth is economics, at solo scale AI cost is a rounding error, at team scale you're looking at a vendor invoice with no way to connect spend to specific workflows or outcomes. Which of these have you hit? And did they show up in this order or did something else surface first? If you're interested, we turned these into a diagnostic with 14 questions. Takes about five minutes, link in the first comment if you want to run through it.

4h ago

---

**[The best AI “science critics” are also the most overconfident — a benchmark on calibration vs. skill](https://www.reddit.com/r/artificial/comments/1txpkby/the_best_ai_science_critics_are_also_the_most/)**

Disclosure: I work on the benchmark below, so flagging that up front. We've been testing whether LLMs can critique recent science-paper summaries — catch planted flaws, overclaims, and missing evidence — and, separately, how calibrated they are about their own judgments (confidence scored with Brier, a strictly proper rule). The pattern that keeps showing up: the models best at spotting problems are also among the most confidently wrong when they miss. Critique skill and calibration look like different axes, not the same one. There's also a clear gap between raw accuracy and knowing when to abstain. It's open (Apache-2.0) if you want to poke at it: Leaderboard: https://huggingface.co/spaces/BGPT-OFFICIAL/refute-leaderboard Dataset: https://huggingface.co/datasets/BGPT-OFFICIAL/refute Curious how others think about measuring calibration vs. raw capability — is a proper scoring rule enough, or do you need explicit abstention metrics too?

1h ago

---

**[$2.5T in AI spending this year. 95% produces zero P&L impact.](https://www.reddit.com/r/artificial/comments/1twupqt/25t_in_ai_spending_this_year_95_produces_zero_pl/)**

Gartner updated their 2026 forecast to $2.5 trillion in global AI spending. Same week, MIT's NANDA Initiative dropped a follow-up: 95% of enterprise gen AI projects deliver zero measurable return. Not low return. Zero. I've been on the delivery side of 14 of these projects since January. The MIT number doesn't surprise me. If anything it's generous. 1. 73% of the engineering work that gets AI into production has nothing to do with the model. Data pipelines, integration layers, legacy system remediation, human-in-the-loop tooling. That's where the hours go. The model is 27% of the work but gets 70%+ of the budget. Every time. 2. The budget ratio between projects that ship and projects that stall is almost exactly inverted. We tracked this through ticket history and commit logs across 14 engagements. Projects that made it to production: roughly 30% model, 70% infrastructure. Projects that stalled: 70% model, 30% infrastructure. Most companies think they're at 50/50. They're not even close. 3. One client went from 71% Copilot adoption to 34% in six months. Two other AI platform licenses dropped under 12%. Combined licensing: $340K/year. The tools worked fine. Nobody redesigned workflows to actually use them. 4. The median data error rate across our engagements is 14%. Teams always guess 5-10%. One client found 23% in month four of a $310K build. That's two months of an ML engineer building training pipelines against garbage data. $36K in salary discovering a problem a data audit would have caught in a week. 5. Medtech company. Four concurrent AI pilots. No kill criteria. $920K in engineer salary. Eleven months. Shipped: nothing. I've now seen this at six companies now. Nobody defines when to stop spending. So nobody stops. 6. Individual gains are real. Company-level ROI stays flat. HCLTech and Writer both found this from different angles. Only 29% of companies see significant ROI from gen AI, despite people at their desks reporting productivity jumps as high as 5x. I mean, the value is clearly there at the individual level. It evaporates somewhere between the IC and the P&L and nobody has a clean explanation for why yet. What connects all of it: the model stopped being the constraint a while ago. MIT's 5% that actually moved the P&L all started with data infrastructure and added model work after. Most companies still do it the other way around, because that's where the conference keynotes and the board excitement live. Every CFO I've shown these numbers to adjusted their allocation. Not sure what that says about the budgets they were running before. Sources: Gartner AI Spending Forecast (May 2026), MIT NANDA "GenAI Divide" report, HCLTech Enterprise AI Report (May 2026), Writer Enterprise AI Survey 2026 I wrote a longer breakdown with the three budget patterns and the pre-mortem questions we run before every engagement if you're curious to learn more on the topic. What do you think about all this though?

23h ago

---

**[Trying to automate too early made my workflows worse, not better](https://www.reddit.com/r/artificial/comments/1txbcwb/trying_to_automate_too_early_made_my_workflows/)**

I’ve been experimenting with automating a few small workflows lately (lead scoring, file handling, etc.) One mistake I keep running into is trying to automate things before the process itself is actually clear. At first it feels productive: - add rules - add scoring - connect tools But over time it just turns into: - patching edge cases - fixing broken inputs - adding more conditions to handle weird situations At some point I realized the problem wasn’t the automation, it was that I didn’t really have a clean “manual logic” to begin with. Once I stepped back and tried to define the process in simple human terms, everything got easier: fewer rules, less complexity, way more stable Feels like automation doesn’t fix messy processes, it just exposes them faster. Curious if others ran into the same thing or if I’m overthinking it.

12h ago

---

---

## Google News: "ai"

**['World-first' vaccine designed by artificial intelligence](https://www.bbc.com/news/articles/crrpggegwe0o)**

Cambridge scientists say they have, for the first time, tested a vaccine designed by AI.

BBC • 17h ago

---

**[Anthropic calls for pause of global AI development](https://www.yahoo.com/news/science/articles/anthropic-calls-pause-global-ai-223531016.html)**

Artificial intelligence company Anthropic suggested Thursday a global pause on building the most powerful AI systems as the latest models are beginning to show signs they could escape human control.Tr...

Yahoo • 10h ago

---

**[Anthropic Urges Global Pause in AI Development, Flags ‘Self-Improvement’ Risk](https://www.wsj.com/tech/ai/anthropic-urges-global-pause-in-ai-development-flags-self-improvement-risk-99cefb73)**

WSJ • 18h ago

---

**[Anthropic (Sorta) Calls for Pause on AI Development. You Should (Sorta) Take It Seriously](https://gizmodo.com/anthropic-sorta-calls-for-pause-on-ai-development-you-should-sorta-take-it-seriously-2000768115)**

Gizmodo • 19m ago

---

**[Cramer says 'cooling market' presents a chance to buy knocked-down AI stocks](https://www.cnbc.com/2026/06/05/cramer-cooling-market-offers-a-chance-to-buy-knocked-down-ai-stocks.html)**

The Investing Club holds its "Morning Meeting" every weekday at 10:20 a.m. ET.

CNBC • 35m ago

---

**[The Metric CFOs Struggle to Track: AI Usage](https://www.wsj.com/cfo-journal/the-metric-cfos-struggle-to-track-ai-usage-3b30c10c)**

WSJ • 43m ago

---

**[Gordon Chang on anti-AI protests: 'Not entirely organic'](https://www.foxbusiness.com/video/6397650325112)**

Gatestone Institute senior fellow Gordon Chang discusses concerns of China's undermining of the US by fueling anti-AI data center protests on 'Varney &  Co.'

Fox Business • 50m ago

---

**[AI CEOs from OpenAI, Anthropic, and Microsoft set aside their rivalry to warn Congress AI is making it too easy to design and create bioweapons](https://fortune.com/2026/06/05/openai-anthropic-microsoft-ceos-congress-bioweapon-safeguards/)**

The signatories want Congress to mandate screening for synthetic DNA sales as AI makes creating a bioweapon easier.

Fortune • 9h ago

---

**[AI chatbot teddy bears raise safety concerns for children](https://www.foxnews.com/video/6397630842112)**

Fox News discusses AI-powered teddy bears capable of human-like conversations with children, with experts like Kurt Knutsson warning about privacy risks.

Fox News • 5h ago

---

**[What to Expect From Apple’s AI, Siri and iOS 27 Launch at WWDC](https://www.bloomberg.com/news/articles/2026-06-05/wwdc-2026-preview-ios-27-siri-ai-features-macos-27-more-apple-will-announce)**

Bloomberg.com • 7h ago

---

---

## HackerNews: "ai"

**[Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes](https://news.ycombinator.com/item?id=48392004)**

The percentage of failing grades in multiple UC Berkeley computer science classes in spring 2026 is significantly higher than past semesters and marks a departure from the department’s grading guidelines.

⬆️ 798 • 💬 763 • 1d ago • [Daily Cal | Berkeley news](https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html)

---

**[Uber's $1,500/month AI limit is a useful signal for AI tool pricing](https://news.ycombinator.com/item?id=48383056)**

I wrote the other day about Uber blowing its 2026 AI budget in four months, and how that wasn't particularly surprising given they would have set that budget in 2025, …

⬆️ 609 • 💬 758 • 2d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Jun/3/uber-caps-usage/)

---

**[Anthropic's open-source framework for AI-powered vulnerability discovery](https://news.ycombinator.com/item?id=48403980)**

Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize - anthropics/defending-code-reference-harness

⬆️ 498 • 💬 140 • 21h ago • [GitHub](https://github.com/anthropics/defending-code-reference-harness)

---

**[When AI Builds Itself: Our progress toward recursive self-improvement](https://news.ycombinator.com/item?id=48400842)**

Our progress toward recursive self-improvement, and its implications.

⬆️ 492 • 💬 660 • 1d ago • [anthropic.com](https://www.anthropic.com/institute/recursive-self-improvement)

---

**[32GB of DDR5 now costs $375 – AI shortage continues to squeeze PC building](https://news.ycombinator.com/item?id=48383241)**

Lower-priced kits are disappearing by the day

⬆️ 427 • 💬 388 • 2d ago • [Tom's Hardware](https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building)

---

**[AI outperforms law professors in Stanford Law study](https://news.ycombinator.com/item?id=48377761)**

A groundbreaking study led by Stanford Law School Professor Julian Nyarko reveals that law professors overwhelmingly prefer AI-generated answers to st

⬆️ 410 • 💬 357 • 2d ago • [Stanford Law School](https://law.stanford.edu/press/ai-outperforms-law-professors-in-stanford-law-study/)

---

**[Mathematicians issue warning as AI rapidly gains ground](https://news.ycombinator.com/item?id=48382052)**

⬆️ 293 • 💬 344 • 2d ago • [science.org](https://www.science.org/content/article/mathematicians-issue-warning-ai-rapidly-gains-ground)

---

**[Open Code Review – An AI-powered code review CLI tool](https://news.ycombinator.com/item?id=48406358)**

Battle-tested at Alibaba&#39;s scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in fine-tuned ruleset (NPE, thread-safety, XSS, S...

⬆️ 244 • 💬 67 • 17h ago • [GitHub](https://github.com/alibaba/open-code-review)

---

**[Astronauts on ISS told to shelter as repairs under way to fix air leaks](https://news.ycombinator.com/item?id=48413464)**

Nasa had directed five of the seven astronauts to shelter inside the docked SpaceX Crew Dragon "Freedom" spacecraft while two Russian cosmonauts attempted an urgent repair.

⬆️ 180 • 💬 116 • 2h ago • [BBC News](https://www.bbc.com/news/live/c4g44ew3g1kt)

---

**[South Korean Forums Will Need to Scan Every Images with AI Censorship Tools](https://news.ycombinator.com/item?id=48406198)**

Due to recent regulation changes (전기통신사업법), the South Korean government is requiring internet communities and forum owners to scan every user uploaded images and videos on their website, by AI.  The hardware to run these AI models are also not provided by government, website owners have to buy datacenter grade Nvidia GPUs by themselves, putting financial pressure to small businesses and forums.  Websites will need to implement these hardware and software features, starting immediately from July ...

⬆️ 167 • 💬 122 • 17h ago • [Privacy Guides Community](https://discuss.privacyguides.net/t/south-korean-online-communities-will-need-to-scan-every-images-with-ai-censorship-tools/38341)

---

---

## YouTube Videos: "ai"

**[Quantum Just Killed AI Data Centers](https://www.youtube.com/watch?v=4o_evxWvsx0)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *A quantum computer just solved in minutes ...

📺 Julia McCoy

👁️ 79K • 👍 5K • 💬 521 • ⏱️ 7:25 • 1d ago

---

**[They Just Admitted The AI Bubble Is Popping...](https://www.youtube.com/watch?v=zv5EFLq7KXo)**

Hello guys and gals, it's me Mutahar again! Talks of the AI bubble are something I've had on this channel recently and it's been on ...

📺 SomeOrdinaryGamers

👁️ 179K • 👍 9K • 💬 1K • ⏱️ 23:33 • 17h ago

---

**[How to Build a $10M Business with AI (Zero Employees)](https://www.youtube.com/watch?v=b3yuAekDS4U)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4x5Fku6 Are you building an AI software ...

📺 Dan Martell

👁️ 49K • 👍 2K • 💬 84 • ⏱️ 14:11 • 1d ago

---

**[Welp, everyone HATES A.I.](https://www.youtube.com/watch?v=vhrJqOGrXGo)**

Everyone besides tech CEOs has been saying it. Now they're starting to say it too. Visit https://groundnews.com/factually to stay ...

📺 Adam Conover

👁️ 179K • 👍 16K • 💬 3K • ⏱️ 14:37 • 1d ago

---

**[Microsoft Just Shocked The Entire AI World: 7 New AI Models](https://www.youtube.com/watch?v=i1dkkxLWaWg)**

Microsoft just revealed seven in-house AI models, Microsoft IQ, Scout, Codename MDASH, and Majorana 2, turning its AI push ...

📺 AI Revolution

👁️ 80K • 👍 2K • 💬 369 • ⏱️ 16:42 • 1d ago

---

**[Anthropic co-founder called for the ability to slow progression of AI. #AI #BBCNews](https://www.youtube.com/watch?v=UQYqvjV98Y8)**

📺 BBC News

👁️ 454 • 👍 14 • ⏱️ 1:21 • 34m ago

---

**[Anthropic urges pause in AI development, says industry needs &#39;brake pedal&#39;](https://www.youtube.com/watch?v=7KLAb0pUMlc)**

The artificial intelligence company is calling for a global pause on developing the most powerful AI systems, saying the latest ...

📺 ABC News

👁️ 4K • 👍 77 • 💬 48 • ⏱️ 1:35 • 6h ago

---

**[Sam Altman Talks AI With BERNIE SANDERS?!](https://www.youtube.com/watch?v=OXjooUNL5Ac)**

Sen. Bernie Sanders met with OpenAI CEO Sam Altman to discuss Sander's proposal to give the American public stake in AI ...

📺 The Young Turks

👁️ 18K • 👍 711 • 💬 144 • ⏱️ 13:49 • 14h ago

---

**[Real Vs AI @NickDiGiovanni @albert_cancook #ai](https://www.youtube.com/watch?v=bY9CAAF3pEQ)**

📺 Patrick Zeinali

👁️ 230K • 👍 12K • 💬 190 • ⏱️ 0:29 • 1h ago

---

**[AI Pioneer Geoffrey Hinton: AI Is Conscious, Superintelligence is Coming, And We Should Be Worried](https://www.youtube.com/watch?v=p7t1Q_p2gZs)**

Geoffrey Hinton is an AI pioneer, a Nobel Prize winner, and a professor emeritus at the University of Toronto. Hinton joins Big ...

📺 Alex Kantrowitz

👁️ 33K • 👍 1K • 💬 387 • ⏱️ 54:54 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 101,823 • ❤️ 1,355 • 9d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 142,851 • ❤️ 517 • 1d ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 296,410 • ❤️ 355 • 3h ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 82,709 • ❤️ 523 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,687,304 • ❤️ 1,441 • 1mo ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 53,525 • ❤️ 318 • 1d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 159,014 • ❤️ 699 • 15d ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 1,246 • ❤️ 260 • 1d ago

---

**[Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)**

*StepFun*

Step-3.7-Flash is a 198B parameter sparse MoE vision-language model with a 256k context window, excelling at multimodal perception, workflow integrity, and code engineering for agentic applications. It offers selectable reasoning levels to balance speed, cost, and cognitive depth, achieving high throughput for production workloads.

`image-text-to-text` `201.4B`

⬇️ 27,948 • ❤️ 328 • 2d ago

---

**[Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)**

*JetBrains*

Mellum2 Thinking is a 12B parameter MoE model designed for complex reasoning tasks, generating explicit chain-of-thought explanations within `<think>` blocks. It excels in multi-step planning, agentic workflows, and math/reasoning-heavy problems, featuring a 131,072 token context length.

`text-generation` `12.1B`

⬇️ 14,709 • ❤️ 215 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 85 • 💬 4 • ⭐ 83,068 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 13 • 💬 1 • ⭐ 80,323 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 221 • 💬 3 • ⭐ 5,006 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 82 • 💬 0 • ⭐ 9,238 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

**[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://huggingface.co/papers/2606.05160)**

*Tianyi Xie, Haotian Zhang, Jinhyung Park et al. (20 authors)*

🏢 NVIDIA

GRAIL generates diverse humanoid manipulation and locomotion data through 3D asset composition and video foundation models, enabling effective sim-to-real transfer for robot control.

▲ 7 • 💬 1 • ⭐ 167 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05160) • [💻 code](https://github.com/NVlabs/GRAIL) • [🔗 project](https://research.nvidia.com/labs/dair/grail/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 38 • 💬 4 • ⭐ 28,505 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 165 • 💬 2 • ⭐ 66,568 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 171 • 💬 10 • ⭐ 48,046 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 58 • 💬 2 • ⭐ 57,771 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 6 • 💬 1 • ⭐ 6,954 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 54.7k • 🔱 6.5k • 2h ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 6.1k • 🔱 600 • 3d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 27端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.5k • 🔱 724 • 2d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.0k • 🔱 312 • 4h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.9k • 🔱 291 • 8h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 403 • 14d ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 131 • 20h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.7k • 🔱 155 • 2d ago

---

**[Helvesec/rmux](https://github.com/Helvesec/rmux)**

Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

`Rust` `agent` `ai` `cli` `linux` `macos`

⭐ 1.6k • 🔱 67 • 18h ago

---

**[asz798838958/aBaiAutoplus](https://github.com/asz798838958/aBaiAutoplus)**

多平台 AI 账号自动注册与管理 · 协议化付款一键开通 ChatGPT Plus

`Python`

⭐ 1.5k • 🔱 695 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*
