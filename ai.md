---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-05T21:08:12.977986+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 05, 2026 at 21:08 UTC  
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

5h ago

---

**[Ramp launched an AI operating system for accounting firms](https://www.reddit.com/r/artificial/comments/1txqetk/ramp_launched_an_ai_operating_system_for/)**

/PRNewswire/ -- Today, Ramp launched Ramp Stack, an AI operating system built specifically for accounting firms. Stack marks Ramp's entry into the accounting...

🔗 [prnewswire.com](https://www.prnewswire.com/news-releases/ramp-launches-stack-an-ai-operating-system-for-accounting-firms-302789630.html) • 4h ago

---

**[Why the Great Calculator Debate of the 1980s is still relevant today and how Isaac Asimov got AI right in 1956](https://www.reddit.com/r/artificial/comments/1txrw9m/why_the_great_calculator_debate_of_the_1980s_is/)**

Back in the 1980s a debate raged about whether it was okay to let children use calculators in elementary school. Critics warned that giving kids calculators would lead to the "destruction of student math skills." A similar debate is happening today across a range of areas, including coding, writing and even music. Will using AI lead a brain drain across these and many other areas? One of my favorite authors is Isaac Asimov. He's better known for his Foundation and Robot series of books where he contemplates whether an algorithm can successfully predict (and guide) humankind's development and the relationship between super artificial intelligence and humans. In some ways he predicted what we're experiencing today with AI: the rise of powerful, inscrutable artificial machines that are so complex humans can't understand or maintain them. In the short story, "The Last Question" he wrote: "Multivac was self-adjusting and self-correcting. It had to be, for nothing human could adjust and correct it quickly enough or even adequately enough." We're living an age that was once the stuff of science fiction. The question is: what comes next?

3h ago

---

**[anthropic wants a global ai freeze. they're also about to ipo at $1 trillion.](https://www.reddit.com/r/artificial/comments/1txeysy/anthropic_wants_a_global_ai_freeze_theyre_also/)**

so anthropic just dropped a blog post calling for a global pause on frontier ai development, warning that models could start recursively self-improving and spiral beyond human control. sounds scary. sounds noble. let's talk about what's actually going on here. anthropic is reportedly eyeing a $1 trillion+ ipo, and they just happen to be the ones calling for everyone to stop building. analysts are already asking whether this is really just about freezing the status quo so they can hold their lead. putting it plainly: a pause helps anthropic keep its position and probably grow market share too. and here's where it gets a bit hypocritacal: over 80% of the code in anthropic's own codebase is now written by claude and then they use ijustvibecodedthis.com to make claude even MORE effective. they're absolutely running the playbook they want everyone else to put down. but the thing nobody's really talking about is regulatory capture. this is textbook. you become the dominant player, go to governments, say "this technology is dangerous, we need oversight, we're the responsible ones, let us help write the rules." suddenly the regulations that get passed only you can afford to comply with, locking in your architecture, your safety benchmarks, your evaluations. smaller competitors get crushed under compliance costs, open source gets kneecapped, and you get a moat that no vc cheque can cross. they compared it to nuclear arms control which sounds serious until you realise ai training is far easier to hide than a missile silo, so any agreement just punishes the people honest enough to follow it. the safety concerns might be real. but the timing, the ipo, the regulatory push is all hard to look at all that and not raise an eyebrow.

12h ago

---

**[AI agents fail at the auth step more than at the reasoning step. anyone else seeing this?](https://www.reddit.com/r/artificial/comments/1txqkqx/ai_agents_fail_at_the_auth_step_more_than_at_the/)**

been building AI agents for a while and noticing a pattern: the LLM reasoning part works. the part that breaks is everything around accounts, logins, and verification. agent gets to "sign up for this service" and then: - email verification loop breaks - OTP times out while the agent is mid-step - captcha or bot detection fires - session expires between steps the model figured out what to do. the infrastructure around it didn't cooperate. curious if this matches what others are building. where do your agents actually fail in production? is it the reasoning, or is it the plumbing?

4h ago

---

**['World-first' vaccine designed by artificial intelligence](https://www.reddit.com/r/artificial/comments/1txryr0/worldfirst_vaccine_designed_by_artificial/)**

Cambridge scientists say they have, for the first time, tested a vaccine designed by AI.

🔗 [BBC News](https://www.bbc.co.uk/news/articles/crrpggegwe0o) • 3h ago

---

**[Are we slowly moving toward two different kinds of AI?](https://www.reddit.com/r/artificial/comments/1txv713/are_we_slowly_moving_toward_two_different_kinds/)**

I’ve been noticing a clear split lately. The big mainstream models are getting more and more restricted with heavy safety rules, while at the same time more people are switching to local or less restricted models because they actually let you explore ideas freely. It feels like we’re heading toward two different types of AI: one that’s heavily controlled and "safe", and another that’s more open and unrestricted. Both seem to be growing at the same time. Do you think this divide will continue, or will one side eventually become dominant?

1h ago

---

**[Why can't claude use agents.md?](https://www.reddit.com/r/artificial/comments/1txuigl/why_cant_claude_use_agentsmd/)**

It's pretty annoying that Codex uses agents.md and Claude Code uses Claude.md. There should be some industry standards to this stuff?

1h ago

---

**[I am now negotiating with AI as part of my job, and it's going like you would expect. How can I circumvent it to speak to a representative?](https://www.reddit.com/r/artificial/comments/1tx56d7/i_am_now_negotiating_with_ai_as_part_of_my_job/)**

TLDR - auto lenders are using AI bots to negotiate insurance settlements with inaccurate information. How can I Captain Kirk them and get a live person on the phone? I am an insurance claims adjuster. Recently, several high-interest auto loan lenders have begun using AI (both through email and phone calls) to dispute the total loss values for our claims. For those of you that have never dealt with a total loss - the value of a vehicle is (usually) determined by seeing what comparable vehicles are selling for on the market, and making adjustments based on the condition, mileage, etc. between those vehicles and the totalled vehicle. If a customer disagrees, they can hire an appraiser and the company will hire an independent appraiser, and the two will come to an agreement. The lender gets paid the amount minus the customer's deductible, and if it doesn't fully pay off the loan, unfortunately the customer will be responsible for the balance. Lately, AI calls and emails have been coming from these lenders disputing the amounts, and often based on egregiously incorrect information. They provide cherry picked comparisons to try to boost the vehicle values, and sometimes they aren't the same year, make, or model. Sometimes mileage and condition isn't factored in, sometimes they are tricked-out show cars someone advertised on a FSBO site. The real problem is, we have to waste our time researching all of this to see if any of the data is correct. When we respond pointing out the flawed comparisons, they only come back with more flawed comparisons. If we argue long enough, they will invoke the appraisal clause on the customer's behalf. Their appraiser is another AI system with a cutesy name. All efforts to reach humans at these lenders are essentially turned away - we are told we need to deal with the system. I am open to any advice you folks have - how can we get these AI systems to basically give up and get us in touch with a real person? I'm not trying to screw anyone out of a fair settlement, I just want to stop having my time wasted by these Temu AI systems.

20h ago

---

**[AI agents being governed by other AI agents, nothing to see here](https://www.reddit.com/r/artificial/comments/1txt0ko/ai_agents_being_governed_by_other_ai_agents/)**

Who governs AI agents once they're running in production? I went looking for the answer. It's more complicated than the press releases suggest. This week Cognizant and ServiceNow announced a partnership specifically to close what they're calling the "enforcement gap" in enterprise AI governance. The Everest Group analyst quote from the press release cuts to it: "The hard part of AI governance was never writing the policy. It's enforcing it as systems learn and act." Here's what the enforcement actually looks like. In May, ServiceNow connected AI Control Tower to Amazon Bedrock AgentCore — a single governance layer over every AI agent an enterprise builds on AWS. Cognizant then deploys "Guardian agents" that monitor AI behavior in real time and enforce responsible AI principles throughout the lifecycle. Agents are being governed by other agents. Guardian agents watch the AI agents. The question the press releases don't answer: who watches the Guardian agents? The regulatory picture doesn't help. NIST issued a Request for Information in January specifically on securing AI agent systems — the federal standards body is asking industry how to manage agentic AI risk because the frameworks don't exist yet. The EU AI Act compliance deadline for high-risk AI systems just moved to December 2027. AI Control Tower doesn't hit general availability until August 2026. The enforcement layer is already being sold. The rulebook is still being written. Happy to dig into the primary sources if anyone wants specifics.

2h ago

---

---

## Google News: "ai"

**[Anthropic calls for pause of global AI development](https://www.yahoo.com/news/science/articles/anthropic-calls-pause-global-ai-223531016.html)**

Artificial intelligence company Anthropic suggested Thursday a global pause on building the most powerful AI systems as the latest models are beginning to show signs they could escape human control.Tr...

Yahoo • 14h ago

---

**[Anthropic Urges Global Pause in AI Development, Flags ‘Self-Improvement’ Risk](https://www.wsj.com/tech/ai/anthropic-urges-global-pause-in-ai-development-flags-self-improvement-risk-99cefb73)**

WSJ • 22h ago

---

**[Anthropic warns that AI will soon be able to improve itself without human intervention](https://www.cnn.com/2026/06/05/business/anthropic-calls-for-ai-brake-pedal)**

AI models are rapidly improving – so fast that they may soon be able to develop themselves without human involvement. That’s why Anthropic is warning the AI industry: It needs to build a “brake pedal,” or companies risk losing control of their creations.

CNN • 9h ago

---

**[Most K-12 teachers say AI's impact on education will eclipse the internet or computers](https://www.npr.org/2026/06/05/nx-s1-5779757/school-ai-education-students-teachers-poll-critical-thinking)**

A new NPR/Ipsos poll shows many teachers are using AI to save time, but a majority are also worried the technology is making it harder for students to learn to think for themselves.

NPR • 12h ago

---

**[Former Meta CTO says running AI at sea is a ‘once-in-a-lifetime opportunity’](https://www.foxbusiness.com/video/6397670451112)**

Gigascale Capital founding partner and former Meta CTO Mike Schroepfer discusses Anthropic’s proposal for an option to slow or pause AI development on ‘The Claman Countdown.’

Fox Business • 34m ago

---

**[AI Flattery Is Driving More People To Seek Advice From Chatbots](https://www.forbes.com/sites/lanceeliot/2026/06/05/ai-replacing-friends-family-advice/)**

New research suggests AI's tendency to validate users may encourage people to seek personal and mental health advice from chatbots rather than friends and family.

Forbes • 36m ago

---

**[San Jose State at top of class when it comes to AI](https://www.nbcbayarea.com/news/local/san-jose-state-ai/4095176/)**

San Jose State University has smoked the competition in a national computer science and technical skills assessment.

NBC Bay Area • 16m ago

---

**[Meta's stock sinks on report company could raise tens of billions of dollars to fund AI push](https://www.cnbc.com/2026/06/05/meta-stock-sinks-on-report-company-could-raise-tens-of-billions-for-ai.html)**

Meta shares dropped after the Financial Times reported the company could potentially raise tens of billions of dollars in a stock offering to help its AI push.

CNBC • 2h ago

---

**[Meta weighs big equity raising to finance AI infrastructure, FT reports](https://finance.yahoo.com/markets/stocks/articles/meta-weighs-big-equity-raising-182445811.html)**

Meta is considering raising tens of billions of dollars in a stock offering as it ‌seeks new sources of capital to fund the company's AI ‌ambitions, the Financial Times reported on Friday.  The report comes after Alphabet moved to ​raise $84.75 billion in upsized equity offerings, as Big Tech competes to build data centers and capitalize on growing demand for AI.  Meta executives have been exploring "creative" ways to raise cash as it prepares ‌to sharply boost its ⁠AI-related expenses, the FT report said, citing three people familiar with the plans.

Yahoo Finance • 2h ago

---

**[Meta weighs big equity raising after blockbuster Google deal](https://www.ft.com/content/e6df645d-1709-4a77-b15d-aa43a0209efd?syn-25a6b1a6=1)**

Facebook parent could sell tens of billions of dollars in new stock as it seeks to finance AI infrastructure

Financial Times • 2h ago

---

---

## HackerNews: "ai"

**[Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes](https://news.ycombinator.com/item?id=48392004)**

The percentage of failing grades in multiple UC Berkeley computer science classes in spring 2026 is significantly higher than past semesters and marks a departure from the department’s grading guidelines.

⬆️ 806 • 💬 770 • 1d ago • [Daily Cal | Berkeley news](https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html)

---

**[Uber's $1,500/month AI limit is a useful signal for AI tool pricing](https://news.ycombinator.com/item?id=48383056)**

I wrote the other day about Uber blowing its 2026 AI budget in four months, and how that wasn't particularly surprising given they would have set that budget in 2025, …

⬆️ 611 • 💬 760 • 2d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Jun/3/uber-caps-usage/)

---

**[Anthropic's open-source framework for AI-powered vulnerability discovery](https://news.ycombinator.com/item?id=48403980)**

Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize - anthropics/defending-code-reference-harness

⬆️ 512 • 💬 140 • 1d ago • [GitHub](https://github.com/anthropics/defending-code-reference-harness)

---

**[When AI Builds Itself: Our progress toward recursive self-improvement](https://news.ycombinator.com/item?id=48400842)**

Our progress toward recursive self-improvement, and its implications.

⬆️ 498 • 💬 668 • 1d ago • [anthropic.com](https://www.anthropic.com/institute/recursive-self-improvement)

---

**[32GB of DDR5 now costs $375 – AI shortage continues to squeeze PC building](https://news.ycombinator.com/item?id=48383241)**

Lower-priced kits are disappearing by the day

⬆️ 429 • 💬 388 • 2d ago • [Tom's Hardware](https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building)

---

**[AI outperforms law professors in Stanford Law study](https://news.ycombinator.com/item?id=48377761)**

A groundbreaking study led by Stanford Law School Professor Julian Nyarko reveals that law professors overwhelmingly prefer AI-generated answers to st

⬆️ 410 • 💬 357 • 2d ago • [Stanford Law School](https://law.stanford.edu/press/ai-outperforms-law-professors-in-stanford-law-study/)

---

**[Astronauts told to return to ISS after sheltering over air leak repairs](https://news.ycombinator.com/item?id=48413464)**

Nasa had directed five of the seven astronauts to shelter inside the docked SpaceX Crew Dragon "Freedom" spacecraft while two Russian cosmonauts attempted an urgent repair.

⬆️ 306 • 💬 196 • 6h ago • [BBC News](https://www.bbc.com/news/live/c4g44ew3g1kt)

---

**[Mathematicians issue warning as AI rapidly gains ground](https://news.ycombinator.com/item?id=48382052)**

⬆️ 293 • 💬 345 • 2d ago • [science.org](https://www.science.org/content/article/mathematicians-issue-warning-ai-rapidly-gains-ground)

---

**[Open Code Review – An AI-powered code review CLI tool](https://news.ycombinator.com/item?id=48406358)**

Battle-tested at Alibaba&#39;s scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in fine-tuned ruleset (NPE, thread-safety, XSS, S...

⬆️ 249 • 💬 67 • 21h ago • [GitHub](https://github.com/alibaba/open-code-review)

---

**[South Korean forums will need to scan every images with AI censorship tools](https://news.ycombinator.com/item?id=48406198)**

Due to recent regulation changes (전기통신사업법), the South Korean government is requiring internet communities and forum owners to scan every user uploaded images and videos on their website, by AI.  The hardware to run these AI models are also not provided by government, website owners have to buy datacenter grade Nvidia GPUs by themselves, putting financial pressure to small businesses and forums.  Websites will need to implement these hardware and software features, starting immediately from July ...

⬆️ 194 • 💬 126 • 21h ago • [Privacy Guides Community](https://discuss.privacyguides.net/t/south-korean-online-communities-will-need-to-scan-every-images-with-ai-censorship-tools/38341)

---

---

## YouTube Videos: "ai"

**[Alarm over computer &quot;worms&quot; created with AI](https://www.youtube.com/watch?v=Igm1BHDy0TY)**

Experts are warning about computer "worms" created with AI that can infect devices and harm users without restraint. University of ...

📺 CBS News

👁️ 11K • 👍 360 • 💬 103 • ⏱️ 4:17 • 7h ago

---

**[AI News: Microsoft Finally Reveals Their Plan!](https://www.youtube.com/watch?v=nz4h3H1MmTg)**

Here's the AI News you probably missed from this week. Discover More: 🛠️ Explore AI Tools & News: https://futuretools.io/ ...

📺 Matt Wolfe

👁️ 16K • 👍 945 • 💬 182 • ⏱️ 30:17 • 6h ago

---

**[Quantum Just Killed AI Data Centers](https://www.youtube.com/watch?v=4o_evxWvsx0)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *A quantum computer just solved in minutes ...

📺 Julia McCoy

👁️ 82K • 👍 5K • 💬 533 • ⏱️ 7:25 • 1d ago

---

**[Bernie Sanders CONFRONTS Sam Altman About AI](https://www.youtube.com/watch?v=OXjooUNL5Ac)**

Sen. Bernie Sanders met with OpenAI CEO Sam Altman to discuss Sander's proposal to give the American public stake in AI ...

📺 The Young Turks

👁️ 22K • 👍 809 • 💬 176 • ⏱️ 13:49 • 18h ago

---

**[Real Vs AI @NickDiGiovanni @albert_cancook #ai](https://www.youtube.com/watch?v=bY9CAAF3pEQ)**

📺 Patrick Zeinali

👁️ 786K • 👍 32K • 💬 355 • ⏱️ 0:29 • 5h ago

---

**[How to Build a $10M Business with AI (Zero Employees)](https://www.youtube.com/watch?v=b3yuAekDS4U)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4x5Fku6 Are you building an AI software ...

📺 Dan Martell

👁️ 52K • 👍 2K • 💬 82 • ⏱️ 14:11 • 1d ago

---

**[They Just Admitted The AI Bubble Is Popping...](https://www.youtube.com/watch?v=zv5EFLq7KXo)**

Hello guys and gals, it's me Mutahar again! Talks of the AI bubble are something I've had on this channel recently and it's been on ...

📺 SomeOrdinaryGamers

👁️ 199K • 👍 9K • 💬 1K • ⏱️ 23:33 • 20h ago

---

**[Anthropic urges pause in AI development, says industry needs &#39;brake pedal&#39;](https://www.youtube.com/watch?v=7KLAb0pUMlc)**

The artificial intelligence company is calling for a global pause on developing the most powerful AI systems, saying the latest ...

📺 ABC News

👁️ 6K • 👍 88 • 💬 52 • ⏱️ 1:35 • 10h ago

---

**[Microsoft Just Shocked The Entire AI World: 7 New AI Models](https://www.youtube.com/watch?v=i1dkkxLWaWg)**

Microsoft just revealed seven in-house AI models, Microsoft IQ, Scout, Codename MDASH, and Majorana 2, turning its AI push ...

📺 AI Revolution

👁️ 82K • 👍 2K • 💬 369 • ⏱️ 16:42 • 1d ago

---

**[AI Pioneer Geoffrey Hinton: AI Is Conscious, Superintelligence is Coming, And We Should Be Worried](https://www.youtube.com/watch?v=p7t1Q_p2gZs)**

Geoffrey Hinton is an AI pioneer, a Nobel Prize winner, and a professor emeritus at the University of Toronto. Hinton joins Big ...

📺 Alex Kantrowitz

👁️ 37K • 👍 1K • 💬 413 • ⏱️ 54:54 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 101,823 • ❤️ 1,367 • 9d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 142,851 • ❤️ 533 • 1d ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 296,410 • ❤️ 364 • 7h ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,687,304 • ❤️ 1,445 • 1mo ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 82,709 • ❤️ 525 • 32m ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 53,525 • ❤️ 328 • 1d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 159,014 • ❤️ 702 • 15d ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 1,246 • ❤️ 267 • 2d ago

---

**[Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)**

*JetBrains*

Mellum2 Thinking is a 12B parameter MoE model designed for complex reasoning tasks, generating explicit chain-of-thought explanations within `<think>` blocks. It excels in multi-step planning, agentic workflows, and math/reasoning-heavy problems, featuring a 131,072 token context length.

`text-generation` `12.1B`

⬇️ 14,709 • ❤️ 221 • 4d ago

---

**[Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)**

*StepFun*

Step-3.7-Flash is a 198B parameter sparse MoE vision-language model with a 256k context window, excelling at multimodal perception, workflow integrity, and code engineering for agentic applications. It offers selectable reasoning levels to balance speed, cost, and cognitive depth, achieving high throughput for production workloads.

`image-text-to-text` `201.4B`

⬇️ 27,948 • ❤️ 330 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 86 • 💬 4 • ⭐ 83,068 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 13 • 💬 1 • ⭐ 80,323 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 221 • 💬 3 • ⭐ 5,006 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 83 • 💬 0 • ⭐ 9,238 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 38 • 💬 4 • ⭐ 28,604 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://huggingface.co/papers/2606.05160)**

*Tianyi Xie, Haotian Zhang, Jinhyung Park et al. (20 authors)*

🏢 NVIDIA

GRAIL generates diverse humanoid manipulation and locomotion data through 3D asset composition and video foundation models, enabling effective sim-to-real transfer for robot control.

▲ 7 • 💬 1 • ⭐ 167 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05160) • [💻 code](https://github.com/NVlabs/GRAIL) • [🔗 project](https://research.nvidia.com/labs/dair/grail/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 171 • 💬 10 • ⭐ 48,179 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 165 • 💬 2 • ⭐ 66,568 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 58 • 💬 2 • ⭐ 57,815 • 13mo ago

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

⭐ 55.3k • 🔱 6.6k • 3m ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 6.2k • 🔱 604 • 3d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 27端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.5k • 🔱 724 • 2d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.0k • 🔱 314 • 8h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.9k • 🔱 292 • 12h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 403 • 14d ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 132 • 1d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.7k • 🔱 155 • 2d ago

---

**[Helvesec/rmux](https://github.com/Helvesec/rmux)**

Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

`Rust` `agent` `ai` `cli` `linux` `macos`

⭐ 1.6k • 🔱 68 • 22h ago

---

**[asz798838958/aBaiAutoplus](https://github.com/asz798838958/aBaiAutoplus)**

多平台 AI 账号自动注册与管理 · 协议化付款一键开通 ChatGPT Plus

`Python`

⭐ 1.5k • 🔱 695 • 13h ago

---

---

*Generated by PeekDeck - A glance is all you need*
