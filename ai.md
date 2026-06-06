---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-06T13:45:17.617924+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 06, 2026 at 13:45 UTC  
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

**[Benefits and Risks of AI at Harvard Class Day 2026](https://www.reddit.com/r/artificial/comments/1ty7pt5/benefits_and_risks_of_ai_at_harvard_class_day_2026/)**

8h ago

---

**[Slow browser agents are going to eat your AI budget and nobody's really talking about it yet](https://www.reddit.com/r/artificial/comments/1tyh08z/slow_browser_agents_are_going_to_eat_your_ai/)**

Okay so I've been thinking about this a lot lately and I feel like everyone's still stuck on the "which model is best" debate when there's a completely different cost problem creeping up on companies actually deploying this stuff. It's not the model. it's the steps. Like... a browser agent doing something that sounds simple: fill out a form, grab data from a dashboard, submit a thing. that's not 3 steps. that's observe, click, wait, observe again, oh there's a modal now, handle that, screenshot is stale, retry, login broke, start over. easily 30-50 tool calls for a task a human would do in 90 seconds. At a small scale you don't care. annoying but whatever. at company scale? If you're running agents across customer ops, internal tooling, research, travel booking, job pipelines, etc., that inefficiency compounds really fast. I came across something called ego lite which apparently takes a different approach: isolated sessions per task, reusable login state, better page snapshots, JS-level orchestration so agents can chain actions instead of calling tiny tools one by one. they're claiming 20-50% faster completion on comparable tasks which honestly if true is not a small number when you're paying per token per call. idk maybe I'm in the weeds on this and most companies aren't at the scale where it bites yet. but it feels like one of those things where by the time people notice the bill, the architecture decisions are already locked in. the smartest model running in a bad environment is still a slow expensive agent. Anyone else actually tracking execution efficiency as a real cost metric or is it still mostly vibes and benchmarks out there?

30m ago

---

**[The strange thing about LLM reasoning research: we're now trying to remove the chain-of-thought traces](https://www.reddit.com/r/artificial/comments/1txp7ah/the_strange_thing_about_llm_reasoning_research/)**

After spending the last few weeks reading through the reasoning literature, I noticed a trend that seems worth discussing. For the past 2–3 years, a large fraction of progress in LLM reasoning came from making models generate more intermediate thoughts. Chain-of-Thought prompting (Wei et al., 2022) pushed PaLM 540B from roughly 18% to 58% on GSM8K. Self-Consistency added another 17.9 percentage points by exploring multiple reasoning paths before committing to an answer. Tree-of-Thoughts later showed that GPT-4's success rate on Game of 24 could jump from 4% to 74% when reasoning was reformulated as search rather than a single chain. DeepSeek-R1 and OpenAI's o1 pushed the idea even further by allocating substantial test-time compute to reasoning itself. Taken together, these results seemed to point in the same direction: giving models additional reasoning trajectories, search paths, or thinking steps often improved outcomes. Recent work increasingly asks whether those traces are actually necessary. Quiet-STaR doesnt treat reasoning traces primarily as explanations for humans. Instead, it trains models to generate internal rationales that improve future token prediction. COCONUT goes a step further and asks a more radical question: why force reasoning to be represented as language at all? Rather than generating reasoning tokens, it feeds continuous hidden states back into the model and performs reasoning directly in latent space. Fast Quiet-STaR then shows that some of the benefits of explicit reasoning can be retained even after removing thought-token generation during inference. This feels like a meaningful shift in research direction. For a while, the field seemed focused on making reasoning more visible. Recent work increasingly explores whether visibility is actually necessary. One way to interpret this is that Chain-of-Thought was never the reasoning process itself. It was a computational scaffold. Transformers perform a fixed amount of computation per generated token. Chain-of-Thought effectively gives them an external workspace: a place to store intermediate states, revisit assumptions, branch into alternatives, and correct mistakes. The performance gains may come less from language itself and more from the additional computation that language enables. If that's the case, then latent reasoning becomes a natural next step. Once we've established that extra computation helps, the obvious question is whether that computation must be expressed in language at all. What's interesting is that this debate is happening at the same time that other work is questioning whether reasoning traces are even faithful descriptions of model cognition. Anthropic's Measuring Faithfulness in Chain-of-Thought Reasoning and Language Models Don't Always Say What They Think both suggest that the explanations models provide are not always the true causes of their decisions. At the architectural level, ideas such as BDH (Dragon Hatchling) are also exploring reasoning as evolving graph states and pathways rather than explicit chains of textual thoughts. Taken together, I think the most interesting question in reasoning research has quietly changed. A year ago the question was: "can LLMs reason?" Today it feels closer to: "if reasoning is fundamentally computation over state, how much of it actually needs to be language?" Curious how others think about this. Is Chain-of-Thought a fundamental component of reasoning systems? Or will we eventually view it the same way we view training wheels: incredibly useful, but ultimately something advanced systems learn to do without?

21h ago

---

**[Why the Great Calculator Debate of the 1980s is still relevant today and how Isaac Asimov got AI right in 1956](https://www.reddit.com/r/artificial/comments/1txrw9m/why_the_great_calculator_debate_of_the_1980s_is/)**

Back in the 1980s a debate raged about whether it was okay to let children use calculators in elementary school. Critics warned that giving kids calculators would lead to the "destruction of student math skills." A similar debate is happening today across a range of areas, including coding, writing and even music. Will using AI lead a brain drain across these and many other areas? One of my favorite authors is Isaac Asimov. He's better known for his Foundation and Robot series of books where he contemplates whether an algorithm can successfully predict (and guide) humankind's development and the relationship between super artificial intelligence and humans. In some ways he predicted what we're experiencing today with AI: the rise of powerful, inscrutable artificial machines that are so complex humans can't understand or maintain them. In the short story, "The Last Question" he wrote: "Multivac was self-adjusting and self-correcting. It had to be, for nothing human could adjust and correct it quickly enough or even adequately enough." We're living an age that was once the stuff of science fiction. The question is: what comes next?

20h ago

---

**[I launched a brand-new author identity with zero web presence. An AI cited him correctly in 6 days — while a firewall blocked every AI crawler from the site the whole time](https://www.reddit.com/r/artificial/comments/1txvhd1/i_launched_a_brandnew_author_identity_with_zero/)**

I ran a small experiment on myself and the result broke my mental model of how AI "knows" things, so I'm sharing it. The setup: on May 11 I created a brand-new pseudonymous fantasy author entity ("Marin T. Kael") with no prior web footprint and no published book yet. Then I asked 5 web-connected AI systems the same 16 questions, every day, for 23 days, and scored every answer (+1 correct/source-grounded, 0 not found, -1 hallucinated). About 16,000 scored datapoints. The whole thing was pre-registered before I started, n=1, and I logged the failures publicly. It's a measurement, not a success story. Here's the part that messed with my head. An AI cited the entity correctly on day 6. Google had a Knowledge Graph entry by day 4. And for 22 of those 23 days, the website's firewall was returning HTTP 403 to every single AI crawler. I didn't set that block on purpose — Cloudflare now silently opts new domains out of AI crawling by default. So the AIs never read the site. They got the entity anyway, by stitching it together from the Knowledge Graph (Wikidata) and third-party mentions at the moment you ask. The "front door" was bolted shut the entire time and it didn't matter. (Honest caveat: because the crawlers were blocked, I can't tell you anything about llms.txt or on-site optimization.) Other surprises: it's not a "smarter model = better" story, it's a retrieval story. OpenAI's newest web model hit 4.7 correct per 1 hallucinated; Gemini went net-negative — and grounded on the entity ONLY via Reddit (17/17), while OpenAI hit the entity's own domain 119x. Going viral did nothing: a 23x Reddit-karma jump produced zero citation lift. Structured identity (Wikidata, site, DOIs) moved the needle; reach didn't. And the controls caught the models fabricating a "Wikipedia" source 24 times for an entity with no Wikipedia page. n=1 with me as investigator and subject is the obvious limit — which is why it's pre-registered with a public failure log. Everything's open: Report + data (Zenodo, CC-BY): https://doi.org/10.5281/zenodo.20549020?utm_source=reddit Code (MIT): https://github.com/marintkael/marin-research-tools Dataset: https://huggingface.co/datasets/marintkael/ai-citation-fidelity

17h ago

---

**[AI Detection Text Scanners Do Not Work. None of Them](https://www.reddit.com/r/artificial/comments/1ty64ky/ai_detection_text_scanners_do_not_work_none_of/)**

I've been building a content production tool for my company, which uses AI for things like structure and automatically inserting links with defined anchor text. 2 days ago, I started testing the results in AI text detection scanners and kept getting inconsistent results, even when I knew my articles looked more natural than a previous test. Revision after revision of code, 10 hours spent trying to get it right. And then I decided to pop in a few articles I had personally written, where I knew AI was not involved. Not a single one of the major scanners got it correct. Most of them flagged my original content as having more AI text than the articles my tool was producing. Now that I've gone down this rabbit hole and understand how AI writes and how the detectors work, I'm not sure that any tool is ever going to be able to do this correctly. For obviously written AI articles, sure, it will catch those. But for original content, I just don't see how it's ever going to work. What is everyone's thoughts on this? Has anyone done the same experiment?

10h ago

---

**[What is the most useful thing you’re using AI for?](https://www.reddit.com/r/artificial/comments/1tygu1j/what_is_the_most_useful_thing_youre_using_ai_for/)**

Pretty basic question, I’m curious to know what the most useful thing you’re using AI for? Are you using things like Claude cowork for tasks, Codex or Claude code for programming, script writing, homework? Do you use it as a regular chat for companionship, are you using it for life advice? Really just curious how individuals are finding it useful to them Thanks

37m ago

---

**[where did all the other ai companies go?](https://www.reddit.com/r/artificial/comments/1tygmti/where_did_all_the_other_ai_companies_go/)**

sit down because this is going to bother you. cast your mind back 18 months. deepseek dropped and the internet lost its mind. "china just ended openai." it was everywhere. people were running it locally, posting benchmarks, losing sleep over geopolitics. then... nothing. it just kind of stopped being talked about. it didn't lose. it didn't win. it just... evaporated from the conversation. sora. remember sora? openai dropped that video generation demo and we were all convinced cinema was dead, hollywood was cooked, every creative job on earth had 18 months left. there were congressional hearings being threatened. think pieces everywhere. and now? when's the last time you actually heard someone say the word sora? not in a demo. in real life. used by a real person. i'll wait. github copilot was supposed to make every programmer 10x more productive. there were developers posting that they'd never write code from scratch again. entire job categories were being eulogised in real time. and now most developers i know have a complicated and slightly embarrassed relationship with it, like someone who got really into a mlm for three months and doesn't want to bring it up. llama was going to democratise ai forever. open source was going to eat everything. the big labs were cooked because you could run intelligence locally on a macbook. and you still can. but do you? does anyone you know actually do that regularly? it became a thing that's theoretically amazing and practically used by like eleven people on hacker news. cursor was the future of coding. perplexity was going to kill google search. both are still around, both are fine, both have paying customers. neither changed anything at the level the discourse suggested they would. here's what i think actually happened. we were living through a hype cycle so fast and so layered that each new thing would go through the entire arc - discovery, mania, backlash, abandonment - in about six weeks. and because the next thing arrived before the previous thing finished its cycle, we never stopped to notice that nothing was actually sticking. and now we're left with the residue of it. the actual models we use every day. and they're quietly getting worse for regular people, or at least that's how it feels. responses that used to feel like talking to someone genuinely engaged now feel like a call centre script. the depth is gone. the willingness to sit with a hard problem is gone. what's left is fast, smooth, and somehow completely hollow. i genuinely think what happened is this: the technology got commoditised before it got good enough to survive commoditisation. the labs all chased each other to the bottom on pricing, burned through vc money performing capability they couldn't sustain at scale, and now the product that regular paying users get is quietly being throttled so the margins make sense. not officially. not announced. just... measurably, undeniably worse. and all those challengers? deepseek, llama, perplexity, cursor - they didn't fail exactly. they just got absorbed into the same gravity. same pressures. same race. same outcome. the golden age, if there was one, lasted maybe 14 months. roughly from mid 2023 to late 2024. models were genuinely trying to impress you. the product teams were still in "wow people" mode rather than "retain subscribers" mode. it showed. now chatgpt talks to me like a hype man at a corporate offsite. gemini hallucinates with the confidence of someone who has never been wrong about anything. claude used to be the one that felt like it was actually thinking. now it sometimes just... gives up mid-conversation. i don't think this is a doom post. i think the technology is real and the long term is probably fine. but i do think the window where regular people got access to something genuinely extraordinary, at a price that made sense, with a product that actually tried - that window may have closed quietly while we were all busy arguing about which model won some benchmark. and nobody really announced it. it just happened. the way most things end. you stop noticing until suddenly you notice all at once.

46m ago

---

**[Michael Saylor Says Bitcoin Drop A 'Capital Rotation' To AI](https://www.reddit.com/r/artificial/comments/1txzsi4/michael_saylor_says_bitcoin_drop_a_capital/)**

Crytpo industry insiders are blaming the recent crash in Bitcoin price to capital rotation into AI stocks. I don't know how many folks here own Bitcoin and are also in the AI space, but I saw this writing on the wall rather early in November, 2025. Any other thoughts on this capital flow change from those who have a foot in each space?

🔗 [Bitcoin Magazine](https://bitcoinmagazine.com/news/michael-saylor-calls-bitcoins-drop) • 15h ago

---

**[One of the best AI articles I have seen recently.](https://www.reddit.com/r/artificial/comments/1tyaqqg/one_of_the_best_ai_articles_i_have_seen_recently/)**

One of the clearest breakdowns for average people like me to understand how AI actually works, and some interesting further information to'boot. https://rogerthatcleansignal.carrd.co/ Discuss.

6h ago

---

---

## Google News: "ai"

**[McDonald's testing AI drive-thru order-taking system called ArchIQ at five locations across country](https://www.foxbusiness.com/retail/mcdonalds-testing-ai-drive-thru-order-taking-system-called-archiq-five-locations-country)**

McDonald's is testing ArchIQ, a new AI order-taking system at five locations, as part of its McDonald's Next strategy announced by CEO Chris Kempczinski.

Fox Business • 12h ago

---

**[McDonald's Introduces AI Drive-Thru System, Sparking Customer Backlash](https://tech.yahoo.com/ai/deals/articles/mcdonalds-introduces-ai-drive-thru-000717731.html)**

'God no,' one declared in a video demonstration of the update.

Yahoo Tech • 13h ago

---

**[McDonald's Drive-Thru AI Upgrade: The system that will change ordering](https://www.marca.com/en/lifestyle/us-news/2026/06/06/mcdonald-s-drive-thru-ai-upgrade-the-system-that-will-change-ordering.html)**

McDonald’s is testing a new Google-powered AI system designed to take drive-thru orders, support multiple languages, and help restaurants run more smoothly.

MARCA • 51m ago

---

**[Meta's stock sinks on report company could raise tens of billions of dollars to fund AI push](https://www.cnbc.com/2026/06/05/meta-stock-sinks-on-report-company-could-raise-tens-of-billions-for-ai.html)**

Meta shares dropped after the Financial Times reported the company could potentially raise tens of billions of dollars in a stock offering to help its AI push.

CNBC • 18h ago

---

**[Revenge of the AI bubble](https://www.axios.com/2026/06/06/ai-bubble-economy-growth)**

Axios • 39m ago

---

**['Sex sells' isn't a new concept. AI-generated women attached to random Facebook Marketplace ads is.](https://www.businessinsider.com/facebook-marketplace-ads-ai-women-sex-sells-2026-6)**

Sellers are adding AI-generated babes to listings for cars, boats, and more to draw attention. It's a new spin on the old adage of "sex sells."

Business Insider • 2h ago

---

**[Opinion | When Is It Wrong to Use A.I.?](https://www.nytimes.com/2026/06/06/opinion/ai-pope-leo-encyclical.html)**

The New York Times • 2h ago

---

**[AI CEOs from OpenAI, Anthropic, and Microsoft set aside their rivalry to warn Congress AI is making it too easy to design and create bioweapons](https://fortune.com/2026/06/05/openai-anthropic-microsoft-ceos-congress-bioweapon-safeguards/)**

The signatories want Congress to mandate screening for synthetic DNA sales as AI makes creating a bioweapon easier.

Fortune • 1d ago

---

**[Nasdaq, S&P 500 suffer worst day of year as AI stocks tumble and Fed rate-hike odds rise](https://www.cnn.com/2026/06/05/markets/stock-market-sell-off-fed)**

Investors sold stocks, bonds, bitcoin and gold Friday after strong jobs data raised odds for Federal Reserve interest rate hikes, and Wall Street wrestled with weakness in AI stocks.

CNN • 20h ago

---

**[4 surprising ways AI is making your life more expensive](https://www.washingtonpost.com/technology/2026/06/06/inflation-is-being-driven-up-by-huge-investment-artificial-intelligence/)**

These goods and services are getting more expensive due to spillover from massive tech company investments in artificial intelligence.

The Washington Post • 12m ago

---

---

## HackerNews: "ai"

**[Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes](https://news.ycombinator.com/item?id=48392004)**

The percentage of failing grades in multiple UC Berkeley computer science classes in spring 2026 is significantly higher than past semesters and marks a departure from the department’s grading guidelines.

⬆️ 816 • 💬 783 • 2d ago • [Daily Cal | Berkeley news](https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html)

---

**[Anthropic's open-source framework for AI-powered vulnerability discovery](https://news.ycombinator.com/item?id=48403980)**

Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize - anthropics/defending-code-reference-harness

⬆️ 524 • 💬 141 • 1d ago • [GitHub](https://github.com/anthropics/defending-code-reference-harness)

---

**[When AI Builds Itself: Our progress toward recursive self-improvement](https://news.ycombinator.com/item?id=48400842)**

Our progress toward recursive self-improvement, and its implications.

⬆️ 513 • 💬 688 • 1d ago • [anthropic.com](https://www.anthropic.com/institute/recursive-self-improvement)

---

**[Astronauts told to return to ISS after sheltering over air leak repairs](https://news.ycombinator.com/item?id=48413464)**

Nasa had directed five of the seven astronauts to shelter inside the docked SpaceX Crew Dragon "Freedom" spacecraft while two Russian cosmonauts attempted an urgent repair.

⬆️ 408 • 💬 253 • 22h ago • [BBC News](https://www.bbc.com/news/live/c4g44ew3g1kt)

---

**[Open Code Review – An AI-powered code review CLI tool](https://news.ycombinator.com/item?id=48406358)**

Battle-tested at Alibaba&#39;s scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in fine-tuned ruleset (NPE, thread-safety, XSS, S...

⬆️ 267 • 💬 67 • 1d ago • [GitHub](https://github.com/alibaba/open-code-review)

---

**[South Korean forums will need to scan every images with AI censorship tools](https://news.ycombinator.com/item?id=48406198)**

Due to recent regulation changes (전기통신사업법), the South Korean government is requiring internet communities and forum owners to scan every user uploaded images and videos on their website, by AI.  The hardware to run these AI models are also not provided by government, website owners have to buy datacenter grade Nvidia GPUs by themselves, putting financial pressure to small businesses and forums.  Websites will need to implement these hardware and software features, starting immediately from July ...

⬆️ 251 • 💬 145 • 1d ago • [Privacy Guides Community](https://discuss.privacyguides.net/t/south-korean-online-communities-will-need-to-scan-every-images-with-ai-censorship-tools/38341)

---

**[Ask HN: Why is the HN crowd so anti-AI?](https://news.ycombinator.com/item?id=48420827)**

⬆️ 208 • 💬 385 • 11h ago

---

**[Hacker News, Sans AI](https://news.ycombinator.com/item?id=48417916)**

⬆️ 173 • 💬 97 • 17h ago • [elijahpotter.dev](https://elijahpotter.dev/articles/hacker-news-sans-AI)

---

**[Google employees internally share memes about how its AI sucks](https://news.ycombinator.com/item?id=48400311)**

Google’s CEO says 75% of the company’s code is AI-generated. The people who write that code say the AI they’re using is overhyped.

⬆️ 167 • 💬 104 • 1d ago • [404 Media](https://www.404media.co/google-employees-internally-share-memes-about-how-its-ai-sucks/)

---

**[Ask HN: What is your (AI) dev tech stack / workflow?](https://news.ycombinator.com/item?id=48413629)**

⬆️ 140 • 💬 123 • 22h ago

---

---

## YouTube Videos: "ai"

**[Anthropic Just Warned Everyone About Claude (It’s Evolving)](https://www.youtube.com/watch?v=JlwwyNtHsCI)**

Anthropic just published a major warning about AI self-improvement, and the numbers behind it are hard to ignore. Claude is now ...

📺 AI Revolution

👁️ 40K • 👍 1K • 💬 214 • ⏱️ 17:13 • 14h ago

---

**[Anthropic calls for global pause in AI development](https://www.youtube.com/watch?v=joZ4Esutu9w)**

The artificial intelligence company's warns that we need to pause development before AI can build itself and humans lose control ...

📺 ABC News

👁️ 56K • 👍 1K • 💬 412 • ⏱️ 4:00 • 17h ago

---

**[The AI Bubble Is Starting To Pop...](https://www.youtube.com/watch?v=qM0BWixY09w)**

SOURCES 1: https://x.com/BusinessInsider/status/2062211094450434219 2: ...

📺 YongYea

👁️ 125K • 👍 5K • 💬 2K • ⏱️ 17:22 • 18h ago

---

**[AI Fruit Drama Is STUPID😭(Pt2)](https://www.youtube.com/watch?v=tpKsujA_L7E)**

Watch videos on spotify: https://open.spotify.com/show/3uu2K4QFclulDG6P4hDOn9?si=a9383e052e104601 Gaming Channel: ...

📺 RICHLEV

👁️ 74K • 👍 3K • 💬 926 • ⏱️ 20:11 • 10h ago

---

**[Real Vs AI @NickDiGiovanni @albert_cancook #ai](https://www.youtube.com/watch?v=bY9CAAF3pEQ)**

📺 Patrick Zeinali

👁️ 2.9M • 👍 87K • 💬 881 • ⏱️ 0:29 • 21h ago

---

**[How to Build a $10M Business with AI (Zero Employees)](https://www.youtube.com/watch?v=b3yuAekDS4U)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4x5Fku6 Are you building an AI software ...

📺 Dan Martell

👁️ 63K • 👍 3K • 💬 98 • ⏱️ 14:11 • 2d ago

---

**[Anthropic co-founder actually wants AI to slow down](https://www.youtube.com/watch?v=z0X2fTYUIgA)**

AI models are rapidly improving – so fast that they may soon be able to develop themselves without human involvement.

📺 CNN

👁️ 16K • 👍 235 • 💬 147 • ⏱️ 8:01 • 11h ago

---

**[Big Tech CEOs AI Psychosis Is A Total Disaster](https://www.youtube.com/watch?v=V3JHuoLD468)**

When one of Silicon Valley's most enthusiastic AI CEOs starts warning about “AI psychosis,” it is worth paying attention. Because ...

📺 House of El - AI

👁️ 107K • 👍 8K • 💬 1K • ⏱️ 20:04 • 1d ago

---

**[Record layoffs driven by AI: Econ analyst reacts](https://www.youtube.com/watch?v=8LLpAyNCh7M)**

Over 97000 layoffs were reported last month, and the flurry of pink slips in May can be traced back to the rise of AI. Matt Egan ...

📺 CNN

👁️ 66K • 👍 859 • 💬 312 • ⏱️ 11:44 • 20h ago

---

**[What are AI breathalyzers in new cars?](https://www.youtube.com/watch?v=A5CHAoJtIWY)**

📺 Tech.Explain

👁️ 109K • 👍 3K • 💬 294 • ⏱️ 1:23 • 18h ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 111,078 • ❤️ 1,406 • 10d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 315,131 • ❤️ 576 • 2d ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 458,174 • ❤️ 391 • 23h ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 84,549 • ❤️ 349 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,771,843 • ❤️ 1,464 • 1mo ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 161,627 • ❤️ 702 • 16d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 95,440 • ❤️ 528 • 14h ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 2,818 • ❤️ 280 • 2d ago

---

**[Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)**

*JetBrains*

Mellum2 Thinking is a 12B parameter MoE model designed for complex reasoning tasks, generating explicit chain-of-thought explanations within `<think>` blocks. It excels in multi-step planning, agentic workflows, and math/reasoning-heavy problems, featuring a 131,072 token context length.

`text-generation` `12.1B`

⬇️ 16,395 • ❤️ 229 • 4d ago

---

**[Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)**

*StepFun*

Step-3.7-Flash is a 198B parameter sparse MoE vision-language model with a 256k context window, excelling at multimodal perception, workflow integrity, and code engineering for agentic applications. It offers selectable reasoning levels to balance speed, cost, and cognitive depth, achieving high throughput for production workloads.

`image-text-to-text` `201.4B`

⬇️ 38,716 • ❤️ 338 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 13 • 💬 1 • ⭐ 80,532 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Cosmos 3: Omnimodal World Models for Physical AI](https://huggingface.co/papers/2606.02800)**

*Aditi, Niket Agarwal, Arslan Ali et al. (291 authors)*

🏢 NVIDIA

Cosmos 3 is an omnimodal world model that processes and generates multiple data types through a unified mixture-of-transformers architecture, achieving state-of-the-art performance in various understanding and generation tasks.

▲ 86 • 💬 1 • ⭐ 9,508 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2606.02800) • [💻 code](https://github.com/NVIDIA/cosmos) • [🔗 project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 86 • 💬 4 • ⭐ 83,247 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 221 • 💬 3 • ⭐ 5,105 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 38 • 💬 4 • ⭐ 28,679 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 171 • 💬 10 • ⭐ 48,261 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://huggingface.co/papers/2606.05160)**

*Tianyi Xie, Haotian Zhang, Jinhyung Park et al. (20 authors)*

🏢 NVIDIA

GRAIL generates diverse humanoid manipulation and locomotion data through 3D asset composition and video foundation models, enabling effective sim-to-real transfer for robot control.

▲ 7 • 💬 1 • ⭐ 194 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05160) • [💻 code](https://github.com/NVlabs/GRAIL) • [🔗 project](https://research.nvidia.com/labs/dair/grail/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 165 • 💬 2 • ⭐ 66,591 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 58 • 💬 2 • ⭐ 57,844 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 6 • 💬 1 • ⭐ 6,978 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 57.3k • 🔱 6.9k • 3h ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 6.2k • 🔱 605 • 4d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 27端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.5k • 🔱 734 • 2d ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.0k • 🔱 305 • 1d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.0k • 🔱 315 • 1d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 405 • 15d ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 132 • 1d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.7k • 🔱 158 • 3d ago

---

**[deeplethe/forkd](https://github.com/deeplethe/forkd)**

Fork() for AI agent microVMs. Spawn 100 children in ~100ms from a warm parent; BRANCH a live VM in ~150ms. KVM-isolated, snapshot CoW.

`Rust` `ai-agents` `copy-on-write` `kvm` `microvm` `rust`

⭐ 1.7k • 🔱 123 • 4h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 1.6k • 🔱 170 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
