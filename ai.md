---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-06T18:05:57.188081+00:00'
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

**Last Updated:** June 06, 2026 at 18:05 UTC  
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

**[A company just sent me the most detailed rejection email I’ve ever received](https://www.reddit.com/r/artificial/comments/1tyimc0/a_company_just_sent_me_the_most_detailed/)**

3h ago

---

**[Benefits and Risks of AI at Harvard Class Day 2026](https://www.reddit.com/r/artificial/comments/1ty7pt5/benefits_and_risks_of_ai_at_harvard_class_day_2026/)**

13h ago

---

**[Does anyone else say please and thank you to AI? Or am I just wierd?](https://www.reddit.com/r/artificial/comments/1tylcl1/does_anyone_else_say_please_and_thank_you_to_ai/)**

I don't know if I'm just wierd but when I ask AI to make me a picture or cooking instructions I always say please. I can't be the only one..

1h ago

---

**[The strange thing about LLM reasoning research: we're now trying to remove the chain-of-thought traces](https://www.reddit.com/r/artificial/comments/1txp7ah/the_strange_thing_about_llm_reasoning_research/)**

After spending the last few weeks reading through the reasoning literature, I noticed a trend that seems worth discussing. For the past 2–3 years, a large fraction of progress in LLM reasoning came from making models generate more intermediate thoughts. Chain-of-Thought prompting (Wei et al., 2022) pushed PaLM 540B from roughly 18% to 58% on GSM8K. Self-Consistency added another 17.9 percentage points by exploring multiple reasoning paths before committing to an answer. Tree-of-Thoughts later showed that GPT-4's success rate on Game of 24 could jump from 4% to 74% when reasoning was reformulated as search rather than a single chain. DeepSeek-R1 and OpenAI's o1 pushed the idea even further by allocating substantial test-time compute to reasoning itself. Taken together, these results seemed to point in the same direction: giving models additional reasoning trajectories, search paths, or thinking steps often improved outcomes. Recent work increasingly asks whether those traces are actually necessary. Quiet-STaR doesnt treat reasoning traces primarily as explanations for humans. Instead, it trains models to generate internal rationales that improve future token prediction. COCONUT goes a step further and asks a more radical question: why force reasoning to be represented as language at all? Rather than generating reasoning tokens, it feeds continuous hidden states back into the model and performs reasoning directly in latent space. Fast Quiet-STaR then shows that some of the benefits of explicit reasoning can be retained even after removing thought-token generation during inference. This feels like a meaningful shift in research direction. For a while, the field seemed focused on making reasoning more visible. Recent work increasingly explores whether visibility is actually necessary. One way to interpret this is that Chain-of-Thought was never the reasoning process itself. It was a computational scaffold. Transformers perform a fixed amount of computation per generated token. Chain-of-Thought effectively gives them an external workspace: a place to store intermediate states, revisit assumptions, branch into alternatives, and correct mistakes. The performance gains may come less from language itself and more from the additional computation that language enables. If that's the case, then latent reasoning becomes a natural next step. Once we've established that extra computation helps, the obvious question is whether that computation must be expressed in language at all. What's interesting is that this debate is happening at the same time that other work is questioning whether reasoning traces are even faithful descriptions of model cognition. Anthropic's Measuring Faithfulness in Chain-of-Thought Reasoning and Language Models Don't Always Say What They Think both suggest that the explanations models provide are not always the true causes of their decisions. At the architectural level, ideas such as BDH (Dragon Hatchling) are also exploring reasoning as evolving graph states and pathways rather than explicit chains of textual thoughts. Taken together, I think the most interesting question in reasoning research has quietly changed. A year ago the question was: "can LLMs reason?" Today it feels closer to: "if reasoning is fundamentally computation over state, how much of it actually needs to be language?" Curious how others think about this. Is Chain-of-Thought a fundamental component of reasoning systems? Or will we eventually view it the same way we view training wheels: incredibly useful, but ultimately something advanced systems learn to do without?

1d ago

---

**[Why the Great Calculator Debate of the 1980s is still relevant today and how Isaac Asimov got AI right in 1956](https://www.reddit.com/r/artificial/comments/1txrw9m/why_the_great_calculator_debate_of_the_1980s_is/)**

Back in the 1980s a debate raged about whether it was okay to let children use calculators in elementary school. Critics warned that giving kids calculators would lead to the "destruction of student math skills." A similar debate is happening today across a range of areas, including coding, writing and even music. Will using AI lead a brain drain across these and many other areas? One of my favorite authors is Isaac Asimov. He's better known for his Foundation and Robot series of books where he contemplates whether an algorithm can successfully predict (and guide) humankind's development and the relationship between super artificial intelligence and humans. In some ways he predicted what we're experiencing today with AI: the rise of powerful, inscrutable artificial machines that are so complex humans can't understand or maintain them. In the short story, "The Last Question" he wrote: "Multivac was self-adjusting and self-correcting. It had to be, for nothing human could adjust and correct it quickly enough or even adequately enough." We're living an age that was once the stuff of science fiction. The question is: what comes next?

1d ago

---

**[the more i use multiple models, the more i think "AI consensus" is a trap — the disagreement is the only part worth paying attention to](https://www.reddit.com/r/artificial/comments/1tymxz2/the_more_i_use_multiple_models_the_more_i_think/)**

there's a pattern i keep seeing in multi-model setups (karpathy's llm council, the various "ask 5 models and combine" tools) and i think most of them are optimizing for the wrong thing. they treat agreement as the goal. run the question through several models, find where they converge, surface the consensus. but in my experience the consensus is the least useful output. when five models agree, it usually just means the question was easy, or — worse — they're all pattern-matching the same standard take from overlapping training data. agreement can be a sign of shared blind spots, not correctness. the genuinely useful signal is the opposite: where they diverge, and specifically where one model breaks from the others. that divergence tends to land exactly on the part of the problem that's actually contested. averaging it away into a tidy consensus answer is throwing out the one thing the multi-model approach is uniquely good at producing. which makes me think the design goal for these systems is backwards. you don't want a machine that manufactures agreement. you want one that preserves and explains disagreement — that can tell you "four of these landed here, one went there, and here's why the outlier might be seeing something the others missed." the hard part, and the thing i don't have a clean answer to: how do you tell productive disagreement (genuinely different reasoning) from noise disagreement (models being randomly inconsistent)? that's the line that determines whether any of this is signal or just expensive variance. curious what people working on multi-agent or ensemble setups think. is consensus the wrong target? and how would you separate real divergence from noise?

52m ago

---

**[Help me understand AI a bit more because I don't think AI is as bad as everyone says.](https://www.reddit.com/r/artificial/comments/1tyi9r2/help_me_understand_ai_a_bit_more_because_i_dont/)**

Now I myself have not used AI a ton beyond making a funny picture or two on ChatGPT/Gemini and maybe asking it a few things on the fly if I need a second opinion on something - and sometimes it's been helpful. The biggest thing I hear from the "Fuck AI" crowd is that it ruins the creative circles like artists, authors, etc. because it copies their work. I sympathize with their hate, but I've heard an argument that it's not doing anything different than what we do when/if AI didn't play a role in anything: look at other people's work for inspiration then create something. Like we can't create a song in a vacuum, we need to learn and be exposed to music theory, notes, other styles of music, instruments, etc. So someone starting a band didn't make something brand new, it took pieces from other artists. And the part that makes me sing AIs praises, so to speak, is its use in the medical field. Doctor Mike posted a video about a year ago talking about this. Like, if it's improving healthcare to the point that it's detecting life threatening things to help doctors treat and cure us more effectively and efficiently, why are we trying to get rid of it? Maybe that's not what people are saying when they want AI gone or saying how 'awful' it is, but I just hope we don't end up throwing the baby out with the bathwater with AI because I genuinely think it's an astonishing thing that's clearly helpful in certain circles.

3h ago

---

**[What is the most useful thing you’re using AI for?](https://www.reddit.com/r/artificial/comments/1tygu1j/what_is_the_most_useful_thing_youre_using_ai_for/)**

Pretty basic question, I’m curious to know what the most useful thing you’re using AI for? Are you using things like Claude cowork for tasks, Codex or Claude code for programming, script writing, homework? Do you use it as a regular chat for companionship, are you using it for life advice? Really just curious how individuals are finding it useful to them Thanks

4h ago

---

**[I launched a brand-new author identity with zero web presence. An AI cited him correctly in 6 days — while a firewall blocked every AI crawler from the site the whole time](https://www.reddit.com/r/artificial/comments/1txvhd1/i_launched_a_brandnew_author_identity_with_zero/)**

I ran a small experiment on myself and the result broke my mental model of how AI "knows" things, so I'm sharing it. The setup: on May 11 I created a brand-new pseudonymous fantasy author entity ("Marin T. Kael") with no prior web footprint and no published book yet. Then I asked 5 web-connected AI systems the same 16 questions, every day, for 23 days, and scored every answer (+1 correct/source-grounded, 0 not found, -1 hallucinated). About 16,000 scored datapoints. The whole thing was pre-registered before I started, n=1, and I logged the failures publicly. It's a measurement, not a success story. Here's the part that messed with my head. An AI cited the entity correctly on day 6. Google had a Knowledge Graph entry by day 4. And for 22 of those 23 days, the website's firewall was returning HTTP 403 to every single AI crawler. I didn't set that block on purpose — Cloudflare now silently opts new domains out of AI crawling by default. So the AIs never read the site. They got the entity anyway, by stitching it together from the Knowledge Graph (Wikidata) and third-party mentions at the moment you ask. The "front door" was bolted shut the entire time and it didn't matter. (Honest caveat: because the crawlers were blocked, I can't tell you anything about llms.txt or on-site optimization.) Other surprises: it's not a "smarter model = better" story, it's a retrieval story. OpenAI's newest web model hit 4.7 correct per 1 hallucinated; Gemini went net-negative — and grounded on the entity ONLY via Reddit (17/17), while OpenAI hit the entity's own domain 119x. Going viral did nothing: a 23x Reddit-karma jump produced zero citation lift. Structured identity (Wikidata, site, DOIs) moved the needle; reach didn't. And the controls caught the models fabricating a "Wikipedia" source 24 times for an entity with no Wikipedia page. n=1 with me as investigator and subject is the obvious limit — which is why it's pre-registered with a public failure log. Everything's open: Report + data (Zenodo, CC-BY): https://doi.org/10.5281/zenodo.20549020?utm_source=reddit Code (MIT): https://github.com/marintkael/marin-research-tools Dataset: https://huggingface.co/datasets/marintkael/ai-citation-fidelity

22h ago

---

**[i have no idea what i'm doing anymore.](https://www.reddit.com/r/artificial/comments/1tymn0m/i_have_no_idea_what_im_doing_anymore/)**

i am a reasonably intelligent person. i have been coding for years. i can hold my own in a technical conversation. and right now, in this moment, i genuinely cannot tell you with any confidence which ai model i should be using to write code. not even close. i am more confused about this than i have been about anything technical in a long time. here's where i am. i have cursor open. cursor lets me pick the model. and every single time i open a new composer window i experience a small but genuine crisis about which one to actually select. claude opus 4.8. claude sonnet 4.6. gpt-5.5. gpt-5.4. grok 4.3. gemini 3.1 pro. qwen3-coder. deepseek v4-pro. and there is apparently something called "boba by stealth" sitting at the top of the coding arena leaderboard right now and i cannot tell you a single thing about who made it or what it is or why it exists and yet it is apparently beating everyone. i have read approximately forty reddit threads about this. they all contradict each other. someone with eight hundred upvotes says opus 4.8 is the only correct answer for anything serious. the top reply says that person is wrong and gpt-5.5 has better agentic performance on multi-file refactors. third comment says both of them are cooked on long runs and gemini 3.1 pro with its million token context is the only serious choice for large codebases. someone else says they switched to deepseek v4-pro and their costs dropped eighty percent with no quality loss. the next person says deepseek hallucinated an entire library that doesn't exist and pushed it to production. i have no framework for evaluating any of this. because here's the thing. the benchmarks don't help. i have looked at so many benchmarks. swe-bench verified. swe-bench pro. terminal-bench 2.0. terminal-bench 2.1. live code bench. the coding arena elo. and then i pick the model that scored highest and it does something confidently wrong that a junior dev wouldn't do, and i'm back to square one wondering if i'm prompting wrong or if the benchmark is fake or if i just got unlucky. and it's not just the model. it's the mode. are you using agent mode. are you letting it run terminal commands autonomously. are you doing ask mode and reviewing everything first. do you have a rules file. a memory file. a custom system prompt per project. there are people with elaborate cursor setups that look like mission control and i genuinely cannot determine if they are more productive than me or just performing productivity for the content. and then there's the routing question. because apparently you're supposed to use different models for different tasks now. opus 4.8 for long autonomous runs where judgment compounds. gpt-5.5 for dense structured reasoning and anything scientific. gemini 3.1 pro for multimodal work and long document retrieval. qwen for cost-sensitive agent loops when you need fifty tool calls and don't want to remortgage your house. people have actual decision flowcharts for this. i have seen the flowcharts. they are not making me feel better. and grok 4.3. what do i do with grok 4.3. the benchmarks put it fourth overall. fourth out of everything. that's extraordinary. and yet every time it comes up in a thread someone immediately says something that makes me put it back down again and i can't even remember what it is but the feeling sticks. i think what happened is the capability race moved faster than anyone's ability to develop genuine intuition about the tools. two years ago this was easier. you picked claude or gpt-4 and you got on with it. now there are fifteen serious options, they are genuinely different, the differences matter for different workloads, and also the differences change every six weeks when someone drops a new version and all the advice goes stale instantly. the thread telling you that sonnet 4.5 is the coding king is four months old. four months is basically a geological era now. and the switching cost of actually testing them properly is high. you need to use a model on real work for weeks before you have proper feel for it. you can't benchmark it yourself in an afternoon. so you're always working with someone else's intuition, formed on different work, in a different context, possibly three model versions ago, posted by someone whose use case has nothing to do with yours. i'm not even sure this is a solvable problem. i think it might just be the permanent condition of working in this space now. perpetual low-level confusion interrupted by brief moments of "okay this one is clearly working" before the next release drops and the discourse resets entirely. so i'm actually asking. not rhetorically. what are you using right now. for real work. not what sounds impressive. what model, what tool, what mode, and what are you actually building with it. because i am genuinely lost and the benchmark threads are not helping and i would very much like to hear from people doing the actual thing. and if anyone can explain what boba by stealth is i would appreciate that too.

1h ago

---

---

## Google News: "ai"

**[4 surprising ways AI is making your life more expensive](https://www.washingtonpost.com/technology/2026/06/06/inflation-is-being-driven-up-by-huge-investment-artificial-intelligence/)**

These goods and services are getting more expensive due to spillover from massive tech company investments in artificial intelligence.

The Washington Post • 2h ago

---

**[Revenge of the AI bubble](https://www.axios.com/2026/06/06/ai-bubble-economy-growth)**

Axios • 5h ago

---

**[Top Trump artificial intelligence adviser to leave the White House](https://www.washingtonpost.com/politics/2026/06/06/trump-top-ai-advisor-leaving-white-house/)**

Sriram Krishnan, who has been central to the administration’s AI efforts, will probably continue to play an active role in its approach to the technology.

The Washington Post • 5m ago

---

**[White House AI Policy Advisor Sriram Krishnan to Leave Position](https://www.theinformation.com/articles/white-house-ai-policy-advisor-krishnan-leave-position)**

Sriram Krishnan, a top AI policy advisor in the Trump administration, plans to leave his position at the end of June, according to a person with direct knowledge of the move and a statement viewed by The Information. Krishnan has discussed starting a policy institution following his time in the ...

The Information • 1h ago

---

**[Sriram Krishnan is leaving his role as White House AI advisor](https://techcrunch.com/2026/06/06/sriram-krishnan-is-leaving-his-role-as-white-house-ai-advisor/)**

Krishnan is reportedly starting a new institution to continue shaping Trump's AI policy.

TechCrunch • 23m ago

---

**[Trump: U.S. stake in AI giants "could be a beautiful thing"](https://www.axios.com/2026/06/06/trump-us-stake-ai-companies)**

Axios • 4h ago

---

**[McDonald's testing AI drive-thru order-taking system called ArchIQ at five locations across country](https://www.foxbusiness.com/retail/mcdonalds-testing-ai-drive-thru-order-taking-system-called-archiq-five-locations-country)**

McDonald's is testing ArchIQ, a new AI order-taking system at five locations, as part of its McDonald's Next strategy announced by CEO Chris Kempczinski.

Fox Business • 16h ago

---

**[Major fast-food chain tests AI ordering at drive-thru locations across U.S.](https://www.cleveland.com/news/2026/06/major-fast-food-chain-tests-ai-ordering-at-drive-thru-locations-across-us.html)**

Cleveland.com • 11m ago

---

**[McDonald's Introduces AI Drive-Thru System, Sparking Customer Backlash](https://tech.yahoo.com/ai/deals/articles/mcdonalds-introduces-ai-drive-thru-000717731.html)**

'God no,' one declared in a video demonstration of the update.

Yahoo Tech • 17h ago

---

**[A.I. Companies Don’t Know What to Do With Alex Bores](https://www.nytimes.com/2026/06/06/nyregion/alex-bores-primary-ai-palantir.html)**

The New York Times • 11h ago

---

---

## HackerNews: "ai"

**[Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes](https://news.ycombinator.com/item?id=48392004)**

The percentage of failing grades in multiple UC Berkeley computer science classes in spring 2026 is significantly higher than past semesters and marks a departure from the department’s grading guidelines.

⬆️ 820 • 💬 784 • 2d ago • [Daily Cal | Berkeley news](https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html)

---

**[Anthropic's open-source framework for AI-powered vulnerability discovery](https://news.ycombinator.com/item?id=48403980)**

Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize - anthropics/defending-code-reference-harness

⬆️ 531 • 💬 141 • 1d ago • [GitHub](https://github.com/anthropics/defending-code-reference-harness)

---

**[When AI Builds Itself: Our progress toward recursive self-improvement](https://news.ycombinator.com/item?id=48400842)**

Our progress toward recursive self-improvement, and its implications.

⬆️ 517 • 💬 689 • 2d ago • [anthropic.com](https://www.anthropic.com/institute/recursive-self-improvement)

---

**[Astronauts told to return to ISS after sheltering over air leak repairs](https://news.ycombinator.com/item?id=48413464)**

Nasa had directed five of the seven astronauts to shelter inside the docked SpaceX Crew Dragon "Freedom" spacecraft while two Russian cosmonauts attempted an urgent repair.

⬆️ 415 • 💬 256 • 1d ago • [BBC News](https://www.bbc.com/news/live/c4g44ew3g1kt)

---

**[Open Code Review – An AI-powered code review CLI tool](https://news.ycombinator.com/item?id=48406358)**

Battle-tested at Alibaba&#39;s scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in fine-tuned ruleset (NPE, thread-safety, XSS, S...

⬆️ 270 • 💬 68 • 1d ago • [GitHub](https://github.com/alibaba/open-code-review)

---

**[South Korean forums will need to scan every images with AI censorship tools](https://news.ycombinator.com/item?id=48406198)**

Due to recent regulation changes (전기통신사업법), the South Korean government is requiring internet communities and forum owners to scan every user uploaded images and videos on their website, by AI.  The hardware to run these AI models are also not provided by government, website owners have to buy datacenter grade Nvidia GPUs by themselves, putting financial pressure to small businesses and forums.  Websites will need to implement these hardware and software features, starting immediately from July ...

⬆️ 257 • 💬 145 • 1d ago • [Privacy Guides Community](https://discuss.privacyguides.net/t/south-korean-online-communities-will-need-to-scan-every-images-with-ai-censorship-tools/38341)

---

**[Ask HN: Why is the HN crowd so anti-AI?](https://news.ycombinator.com/item?id=48420827)**

⬆️ 242 • 💬 431 • 15h ago

---

**[Hacker News, Sans AI](https://news.ycombinator.com/item?id=48417916)**

⬆️ 177 • 💬 97 • 21h ago • [elijahpotter.dev](https://elijahpotter.dev/articles/hacker-news-sans-AI)

---

**[The Smart TV in Your LivingRoom Is a Node in the AIScraping Economy](https://news.ycombinator.com/item?id=48422993)**

⬆️ 171 • 💬 72 • 8h ago • [blog.includesecurity.com](https://blog.includesecurity.com/2026/06/the-smart-tv-in-your-livingroom-is-a-node-in-the-aiscraping-economy/)

---

**[Google employees internally share memes about how its AI sucks](https://news.ycombinator.com/item?id=48400311)**

Google’s CEO says 75% of the company’s code is AI-generated. The people who write that code say the AI they’re using is overhyped.

⬆️ 167 • 💬 104 • 2d ago • [404 Media](https://www.404media.co/google-employees-internally-share-memes-about-how-its-ai-sucks/)

---

---

## YouTube Videos: "ai"

**[Anthropic Just Warned Everyone About Claude (It’s Evolving)](https://www.youtube.com/watch?v=JlwwyNtHsCI)**

Anthropic just published a major warning about AI self-improvement, and the numbers behind it are hard to ignore. Claude is now ...

📺 AI Revolution

👁️ 44K • 👍 2K • 💬 233 • ⏱️ 17:13 • 18h ago

---

**[AI News: Microsoft Finally Reveals Their Plan!](https://www.youtube.com/watch?v=nz4h3H1MmTg)**

Here's the AI News you probably missed from this week. Discover More: 🛠️ Explore AI Tools & News: https://futuretools.io/ ...

📺 Matt Wolfe

👁️ 41K • 👍 2K • 💬 249 • ⏱️ 30:17 • 1d ago

---

**[These New AI Robots Just Became TOO POWERFUL… And It’s Getting Weird](https://www.youtube.com/watch?v=5_EEAGDV1aA)**

These AI robots just crossed into territory that feels almost too real — and you need to see this. A robot is now beating skilled ...

📺 The AI Nexus

👁️ 3K • 👍 101 • 💬 5 • ⏱️ 59:14 • 14h ago

---

**[Quantum Just Killed AI Data Centers](https://www.youtube.com/watch?v=4o_evxWvsx0)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *A quantum computer just solved in minutes ...

📺 Julia McCoy

👁️ 94K • 👍 5K • 💬 598 • ⏱️ 7:25 • 2d ago

---

**[AI Fruit Drama Is STUPID😭(Pt2)](https://www.youtube.com/watch?v=tpKsujA_L7E)**

Watch videos on spotify: https://open.spotify.com/show/3uu2K4QFclulDG6P4hDOn9?si=a9383e052e104601 Gaming Channel: ...

📺 RICHLEV

👁️ 91K • 👍 4K • 💬 1K • ⏱️ 20:11 • 14h ago

---

**[DeepMind’s New AI Found A Strange New Way To Think](https://www.youtube.com/watch?v=Dkqzqw8rxXI)**

Check out Weights & Biases and sign up for a free demo here: https://wandb.me/papers The paper is available here: ...

📺 Two Minute Papers

👁️ 80K • 👍 5K • 💬 338 • ⏱️ 7:30 • 1d ago

---

**[Anthropic calls for global pause in AI development](https://www.youtube.com/watch?v=joZ4Esutu9w)**

The artificial intelligence company's warns that we need to pause development before AI can build itself and humans lose control ...

📺 ABC News

👁️ 61K • 👍 1K • 💬 466 • ⏱️ 4:00 • 22h ago

---

**[How to Build a $10M Business with AI (Zero Employees)](https://www.youtube.com/watch?v=b3yuAekDS4U)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4x5Fku6 Are you building an AI software ...

📺 Dan Martell

👁️ 65K • 👍 3K • 💬 134 • ⏱️ 14:11 • 2d ago

---

**[The AI Bubble Is Starting To Pop...](https://www.youtube.com/watch?v=qM0BWixY09w)**

SOURCES 1: https://x.com/BusinessInsider/status/2062211094450434219 2: ...

📺 YongYea

👁️ 134K • 👍 6K • 💬 2K • ⏱️ 17:22 • 22h ago

---

**[Real Vs AI @NickDiGiovanni @albert_cancook #ai](https://www.youtube.com/watch?v=bY9CAAF3pEQ)**

📺 Patrick Zeinali

👁️ 3.2M • 👍 94K • 💬 936 • ⏱️ 0:29 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 111,078 • ❤️ 1,430 • 10d ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 315,131 • ❤️ 604 • 2d ago

---

**[gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**

*Unsloth AI*

Gemma 4 12B Unified is a multimodal LLM capable of processing text and image inputs natively, supporting up to 256K context tokens. It excels at reasoning, coding, and agentic tasks, optimized for efficient local execution on consumer hardware.

`image-text-to-text` `11.9B`

⬇️ 458,174 • ❤️ 409 • 1d ago

---

**[gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio, image, and text understanding, featuring an encoder-free architecture for efficient on-device deployment. It excels at reasoning, coding, and agentic tasks with a 256K context window.

`any-to-any` `12.0B`

⬇️ 84,549 • ❤️ 367 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,771,843 • ❤️ 1,475 • 1mo ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 161,627 • ❤️ 705 • 16d ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 2,818 • ❤️ 291 • 2d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 95,440 • ❤️ 528 • 18h ago

---

**[Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)**

*JetBrains*

Mellum2 Thinking is a 12B parameter MoE model designed for complex reasoning tasks, generating explicit chain-of-thought explanations within `<think>` blocks. It excels in multi-step planning, agentic workflows, and math/reasoning-heavy problems, featuring a 131,072 token context length.

`text-generation` `12.1B`

⬇️ 16,395 • ❤️ 236 • 5d ago

---

**[Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)**

*StepFun*

Step-3.7-Flash is a 198B parameter sparse MoE vision-language model with a 256k context window, excelling at multimodal perception, workflow integrity, and code engineering for agentic applications. It offers selectable reasoning levels to balance speed, cost, and cognitive depth, achieving high throughput for production workloads.

`image-text-to-text` `201.4B`

⬇️ 38,716 • ❤️ 340 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 13 • 💬 1 • ⭐ 80,717 • 4d ago

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

▲ 39 • 💬 4 • ⭐ 28,759 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 171 • 💬 10 • ⭐ 48,370 • 9mo ago

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

▲ 165 • 💬 2 • ⭐ 66,637 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 59 • 💬 2 • ⭐ 57,876 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 6 • 💬 1 • ⭐ 7,000 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 57.7k • 🔱 6.9k • 3h ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 6.2k • 🔱 606 • 4d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 27端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.5k • 🔱 736 • 3d ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.0k • 🔱 305 • 1d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.0k • 🔱 316 • 1d ago

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

⭐ 1.8k • 🔱 158 • 3d ago

---

**[deeplethe/forkd](https://github.com/deeplethe/forkd)**

Fork() for AI agent microVMs. Spawn 100 children in ~100ms from a warm parent; BRANCH a live VM in ~150ms. KVM-isolated, snapshot CoW.

`Rust` `ai-agents` `copy-on-write` `kvm` `microvm` `rust`

⭐ 1.7k • 🔱 127 • 8h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 1.6k • 🔱 179 • 3h ago

---

---

*Generated by PeekDeck - A glance is all you need*
