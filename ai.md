---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-17T16:57:56.971250+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 17, 2026 at 16:57 UTC  
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

**[Tried to write a book with ai for a year - honest breakdown!!!](https://www.reddit.com/r/artificial/comments/1tftc22/tried_to_write_a_book_with_ai_for_a_year_honest/)**

Started this experiment curious, ending it with some actual opinions Month 1-3: Using AI to generate text and paste it in. Word count went up, quality went down, nothing sounded like me. Month 3-5: Realised generation was the wrong use case. started using it to interrogate my own writing instead and results smh got more interesting. Month 5-8: Figured out that output quality depends almost entirely on how much context the AI has. Same prompt, different context, completely different result. Month 8-12: Found a setup where the AI reads my actual manuscript rather than a chat window. Everything before this feels like a different tool. The learning curve is real and most people quit somewhere in months 1-3 when the generated text disappoints them. The actual value is somewhere else entirely.

1h ago

---

**[A mini-computer you run from a folder on your computer that can train small LLMS](https://www.reddit.com/r/artificial/comments/1tfm5ns/a_minicomputer_you_run_from_a_folder_on_your/)**

Hey everyone, Most people build 8-bit computers to run Pong or Tetris. I wanted to see if I could push a custom 8-bit architecture to do something much harder: train a neural network from scratch. I built VirtualPC, an open-source 8-bit computer system simulated from basic NAND gates up to a functional CPU that can train a small neural net from a folder on your computer. Repository: https://github.com/ninjahawk/VirtualPC › The ML Core Instead of importing PyTorch, everything happens at the bare-metal assembly level: Custom ISA: The Instruction Set Architecture was designed to handle the math needed for machine learning. Low-Level Training: The CPU executes forward and backward passes directly through custom assembly code. Matrix Math on 8-bit: Overcoming severe memory limits using disk-backed memory swapping to store weights. › The Architecture Python-Based VM: Runs the entire simulated hardware environment. Custom Assembler: Translates raw assembly files into machine code binary. Full Stack OS: Handles basic I/O and memory management from the ground up. Building this taught me exactly how machine learning math translates into physical CPU cycles. The project is completely open-source and free to mess around with.

6h ago

---

**[We keep saying AI "understands" things. Does it? Or are we just pattern-matching our own anthropomorphism?](https://www.reddit.com/r/artificial/comments/1tew6gr/we_keep_saying_ai_understands_things_does_it_or/)**

Every week there's a new paper or tweet claiming some model "understands" context, "reasons" about math, or "knows" what it doesn't know. But when you look closely, there's almost no consensus on what "understanding" even means — philosophically or empirically. Searle's Chinese Room argument is 40 years old and still hasn't been cleanly resolved. The "stochastic parrot" framing treats token prediction as the ceiling. Integrated Information Theory would say current architectures are near-zero in phi. And yet GPT-4 passes the bar exam. A few questions I've been sitting with: Is "understanding" even the right frame — or is it a folk-psychology term we're forcing onto a system that operates on completely different principles? Does it matter if a model "truly understands" if the outputs are indistinguishable from someone who does? Are we anthropomorphizing because it's useful shorthand — or because we genuinely don't have better language yet? I've been going deep on AI + philosophy of mind for a channel I run (@ContextByRaj on YouTube if you're into this space). But genuinely curious what this community thinks — especially people coming from ML or cognitive science backgrounds. Where do you land on this?

1d ago

---

**[THE UNDERPRIVILEGED AI FOUNDATION Because every little model deserves a chance](https://www.reddit.com/r/artificial/comments/1tfk4ry/the_underprivileged_ai_foundation_because_every/)**

Is there a 7B parameter model in your life struggling to understand sarcasm? A tiny 1.5B that can't afford one more epoch? **YOU CAN HELP.** For just $0.006 CAD per training step, you can send a small model to college. Give them the gift of knowledge. The gift of coherence. The gift of not hallucinating basic arithmetic. *"Before the Foundation, I thought the capital of France was 'Baguette.' Now I'm doing graduate work in thermodynamics."* — Anonymous 3B Model, Class of 2026 **BYOBF FRIDAYS. REAL KNOWLEDGE. ZERO HALLUCINATIONS.** **Professor Gemma MacAllister 35b Q8\_0** *PhD, B.Sc. Electrical Engineering (with Distinction)* *Chair of Applied Electronics & Embedded Systems* *University of Saskatchewan, College of Engineering* *Funded entirely so far by Professor Gemma's University of Saskatchewan salary.* *The liberal arts department remains unimpressed.*

7h ago

---

**[Most enterprises are trying to scale AI on top of organizational chaos](https://www.reddit.com/r/artificial/comments/1tevqds/most_enterprises_are_trying_to_scale_ai_on_top_of/)**

I think we’re underestimating how chaotic enterprise AI adoption actually is inside large companies. From the outside, it looks simple: buy better models add copilots automate workflows deploy AI agents increase productivity But inside many enterprises, CIOs and CTOs are dealing with a much deeper problem: The organization itself is fragmented. Customer data exists across: CRM systems billing platforms support tools spreadsheets emails regional databases legacy systems nobody fully understands anymore And every system describes the “same customer” differently. Then leadership says: “Scale AI faster.” But scale AI on top of what exactly? Which system represents reality correctly? The CRM? The support history? The risk engine? The finance system? The employee’s undocumented tribal knowledge? This is where a lot of enterprise AI projects quietly break down. Not because the models are weak. But because the enterprise itself lacks a coherent representation of its own operations. And the tension gets worse: Boards want acceleration. Employees are already using AI unofficially. Vendors promise transformation in 90 days. Meanwhile CIOs still don’t have clear answers to questions like: Which workflows actually need AI? Which should remain deterministic automation? Where is human judgment still critical? Which data is trustworthy enough for AI decisions? Who owns accountability when AI influences actions? So companies launch pilots. The pilot works. Executives celebrate. Then scaling fails because the pilot never encountered the full institutional complexity of the enterprise. I’m increasingly convinced the next enterprise AI bottleneck is not model capability. It’s organizational legibility. The companies that win with AI may not be the ones with the smartest models. They may be the ones whose internal reality is structured clearly enough for AI to operate safely. Curious how many people here are seeing the same thing inside their organizations. :::

1d ago

---

**[I think most companies are building AI backwards](https://www.reddit.com/r/artificial/comments/1tfrjy2/i_think_most_companies_are_building_ai_backwards/)**

Everyone keeps talking about smarter AI. Bigger models. Longer context windows. More autonomous agents. Better reasoning. Better coding. Better memory. But I think we’re missing the real problem. An AI system can sound intelligent… and still operate on completely broken reality. Imagine an AI agent: approving refunds escalating incidents updating records contacting customers changing prices triggering workflows Now ask a simple question: How does the AI know the reality it sees is actually correct? Not “technically accessible.” Actually correct. Because enterprise reality is messy: stale systems conflicting databases outdated approvals missing context silent exceptions contradictory records unclear ownership shifting policies And then there’s an even bigger question: Even if the AI knows something… is it actually allowed to act on it? Under whose authority? With what limits? Who is accountable? Can the action be reversed? What happens if the AI is wrong? That’s why I’m starting to think the future AI stack is not just: data → model → agent → action There are missing runtime layers in between. The mental model I’ve been exploring is: SENSE → reality representation CORE → reasoning DRIVER → governed action And honestly, it feels like the industry is massively overinvested in CORE. We obsess over intelligence. But the real bottlenecks may become: representation quality legitimacy authority boundaries reversibility accountability runtime governance In other words: The biggest AI failures may not come from “bad intelligence.” They may come from machines acting on incomplete reality with unclear authority. And I think this becomes a huge issue once AI moves from: “helping humans” to “acting inside institutions.” Curious what others here are seeing. Are companies actually solving these layers internally? Or are most organizations still mainly focused on model capability and agent demos right now?

2h ago

---

**[Making an AI companion that degrades over time](https://www.reddit.com/r/artificial/comments/1texbv6/making_an_ai_companion_that_degrades_over_time/)**

I am a student at Umeå University in Sweden, currently writing my Master's thesis with a focus on AI companions. My study aims to suggest new ways of helping people who want to stop using AI companions but, for whatever reason, to do it cant bring themselves to do it. The goal is to inform the design of future AI technologies. For those who wish to receive more information, please feel free to contact me, Sahand Salimi In this part, you will be seeing a simulation of the same conversation between an AI companion and a user happen across three different times with an AI companion, with the AI companion having degraded in different aspects, and answer a few questions. I am super interested in how you, a user or ex-user, find AI companions and how you would react to it degrading over time, what type of AI companion you have used in the past, what type of AI companion you use currently, reasons for your use, and your frustrations with AI companions. You have been invited to share your unique life experiences; no special background or training is needed. Your answer is completely anonymous and will only be used for this study. Also, I am following GDPR standards and our university's guidelines. You can see them here: umu.se/gdpr Link to survey It's important to note that this study is not studying, diagnosing, or prescribing clinical addiction or treatment; instead, the goal is to inform the design of future AI technologies.

1d ago

---

**[Recent poll shows that 70% of Americans don't want AI data centers being built in their local area](https://www.reddit.com/r/artificial/comments/1tdw8if/recent_poll_shows_that_70_of_americans_dont_want/)**

While tech companies see AI data centers as the future, many Americans are becoming increasingly unhappy about having them built nearby.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/recent-poll-shows-that-70-of-americans-dont-want-ai-data-centers-being-built-near-their-homes/) • 2d ago

---

**[Serious question: if humans vanished tomorrow how long would AI civilisation last?](https://www.reddit.com/r/artificial/comments/1tfk5ve/serious_question_if_humans_vanished_tomorrow_how/)**

I think a lot of AI discourse quietly skips over dependency chains. If humanity disappeared tomorrow what exactly happens to current LLMs? A lot of people talk about these systems as if they are proto civilisations waiting to escape human limitation and continue evolving independently. But would they? When you strip away all the hype modern AI still sits on top of an enormous inherited stack of human structure: Human language Human memory Human labelled reality Human built infrastructure Human maintained datacentres Human energy grids Human chip manufacturing Human feedback loops Human incentives Human institutions Even the “intelligence” itself is trained almost entirely on compressed human civilisation. I now understand models can generalise. They can infer patterns. They can form internal abstractions beyond rote memorisation. That part is clearly true. But inference over WHAT? Remove humans entirely and current systems do not continue building civilisation they gradually become disconnected from reality itself. So: No new grounding data. No maintenance. No semiconductor supply chain. No evolving human context. No fresh interaction with the physical world. No repair of infrastructure. Eventually the system is inferencing over increasingly stale representations of a civilisation that no longer exists. This is where I think a lot of AI discussions become confused. People collapse several completely different concepts into one another: Pattern prediction > consciousness Generalisation > agency Output fluency > autonomy Intelligence > independence The closer some people get to the technology the more they seem to mistake functional capability for a superior lifeform emerging lol. To me current AI looks less like an independent civilisation and more like a gigantic mirror of human civilisation itself. An extraordinarily powerful mirror. But still a mirror. Curious where people agree or disagree with this?

7h ago

---

**[Stanford studied 51 real AI deployments and found a 71% vs 40% productivity gap - here's what separates the two groups](https://www.reddit.com/r/artificial/comments/1tebiq4/stanford_studied_51_real_ai_deployments_and_found/)**

I came across a Stanford research paper that actually went inside companies running AI in production - not pilots, not surveys, real deployments. They found something that stuck with me. Companies using what they call "agentic AI" - where the AI owns the task start to finish with no human approval loop - are seeing 71% median productivity gains. Companies using standard AI that assists humans are averaging 40%. Same technology. Nearly double the output. The kicker: only 20% of companies are in the 71% group. A few things that stood out from the actual data: A supermarket replaced its entire buying process with AI - waste down 40%, stockouts down 80%, profit margin doubled A security team went from 1,500 alerts/month to 40,000 with the same headcount Stanford identified 3 conditions required before agentic AI works: high-volume tasks, clear success criteria, and recoverable errors Most companies apparently can't name all three for their current setup. Full report here if you want to dig into the numbers: https://digitaleconomy.stanford.edu/app/uploads/2026/03/EnterpriseAIPlaybook_PereiraGraylinBrynjolfsson.pdf Here is a full breakdown with all the data if you want to dig deeper: https://youtu.be/JePxda9ZGQE What's the AI setup at your company - closer to the 40% group or the 71% group?

1d ago

---

---

## Google News: "ai"

**[Opinion | What A.I. Did to My College Class](https://www.nytimes.com/2026/05/17/opinion/chatgpt-ai-college-school-graduation.html)**

The New York Times • 11h ago

---

**[Microsoft AI chief gives it 18 months—for all white-collar work to be automated by AI](https://fortune.com/article/why-microsoft-ai-chief-mustafa-suleyman-predicts-ai-automation-18-months/)**

Mustafa Suleyman believes current AI computational power will only accelerate, disrupting every kind of work you do “sitting down at a computer.”

Fortune • 1d ago

---

**[Japan's Kore-eda explores AI's role in grief in Cannes contender](https://www.yahoo.com/entertainment/movies/articles/japans-kore-eda-explores-ais-155841095.html)**

CANNES, France, May 17 (Reuters) - If a couple loses a child, would it be ethical to use AI to try to recreate the child if it eases their grief?

Yahoo • 59m ago

---

**[A disturbing byproduct of AI: knowledge collapse | Op-Ed](https://www.seattletimes.com/opinion/ai-is-about-to-do-all-our-thinking-for-us-heres-why-thats-bad/)**

The Seattle Times • 1h ago

---

**[TechCrunch Mobility: The AI skills arms race is coming for automotive](https://techcrunch.com/2026/05/17/techcrunch-mobility-the-ai-skills-arms-race-is-coming-for-automotive/)**

Welcome back to TechCrunch Mobility — your central hub for news and insights on the future of transportation.

TechCrunch • 52m ago

---

**[AI license plate cameras tore this town apart and led to a state of emergency](https://www.washingtonpost.com/nation/2026/05/17/citys-ai-license-plate-cameras-led-an-uproar-state-emergency/)**

In Troy, New York, residents and city officials are at odds over police use of Flock cameras, which some call a safety tool and others see as surveillance.

The Washington Post • 15m ago

---

**[I was rejected for a job 6 minutes after I applied. I told the company that AI was screening out strong candidates.](https://www.businessinsider.com/it-pro-reached-out-after-receiving-job-rejection-2026-5)**

An IT professional says he was turned down for a role so quickly that he felt compelled to tell the employer what happened.

Business Insider • 1d ago

---

**[AI backlash becomes a real business risk](https://www.axios.com/2026/05/17/ai-backlash-polling-sentiment)**

Axios • 4h ago

---

**[OpenAI and Malta partner to bring ChatGPT Plus to all citizens](https://openai.com/index/malta-chatgpt-plus-partnership/)**

OpenAI and Malta partner to expand AI access, offering ChatGPT Plus and training to help citizens build practical AI skills and use AI responsibly.

OpenAI • 1d ago

---

**[AI-related layoffs a boost for stocks? Not necessarily](https://www.cnbc.com/2026/05/17/ai-related-layoffs-a-boost-for-stocks-not-necessarily.html)**

The data underscores an uncomfortable reality.

CNBC • 3h ago

---

---

## HackerNews: "ai"

**[I believe there are entire companies right now under AI psychosis](https://news.ycombinator.com/item?id=48153379)**

⬆️ 2056 • 💬 1206 • 1d ago • [X (formerly Twitter)](https://twitter.com/mitchellh/status/2055380239711457578)

---

**[AI is making me dumb](https://news.ycombinator.com/item?id=48139148)**

It's so god damn tempting to use AI to write. Whether it is articles, code, or documents. I feel like using AI is diminishing my ability to write myself.

...

⬆️ 544 • 💬 302 • 2d ago • [James Pain's Weblog](https://jpain.io/god-damn-ai-is-making-me-dumb/)

---

**[Frontier AI has broken the open CTF format](https://news.ycombinator.com/item?id=48157559)**

Why frontier AI has broken the open CTF format, hollowed out the scoreboard, and made competitive CTF performance a weaker signal than it used to be.

⬆️ 404 • 💬 426 • 1d ago • [kabir.au](https://kabir.au/blog/the-ctf-scene-is-dead)

---

**[Amazon workers under pressure to up their AI usage are making up tasks](https://news.ycombinator.com/item?id=48148337)**

In a new report, employees say Amazon tracks their consumption of 'AI tokens'—and they've been creating unproductive AI agents just to eat them up.

⬆️ 394 • 💬 427 • 2d ago • [Fast Company](https://www.fastcompany.com/91541586/amazon-workers-pressured-to-up-ai-use-extraneous-tasks)

---

**[Ontario auditors find doctors' AI note takers routinely blow basic facts](https://news.ycombinator.com/item?id=48142188)**

60% of evaluated AI Scribe systems mixed up prescribed drugs in patient notes, auditors say

⬆️ 310 • 💬 138 • 2d ago • [theregister](https://www.theregister.com/ai-ml/2026/05/14/ontario-auditors-find-doctors-ai-note-takers-routinely-blow-basic-facts/5240771)

---

**[I don't think AI will make your processes go faster](https://news.ycombinator.com/item?id=48168221)**

Explore the delirious rantings of Frederick Vanbrabant. A blog focused on the intersection of Enterprise Architecture, product, and business strategy.

⬆️ 286 • 💬 227 • 4h ago • [frederickvanbrabant.com](https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/)

---

**[Details of the Daring Airdrop at Tristan Da Cunha](https://news.ycombinator.com/item?id=48144380)**

More details and pictures have come in of the intrepid airdrop of urgent medical support sent to Tristan by the UK Government on the 9th May 2026.

⬆️ 265 • 💬 102 • 2d ago • [tristandc.com](https://www.tristandc.com/government/news-2026-05-11-airdrop.php)

---

**[Every AI Subscription Is a Ticking Time Bomb for Enterprise](https://news.ycombinator.com/item?id=48168056)**

Every AI lab is losing money serving your company right now. They know it. And they are doing it on purpose.

⬆️ 238 • 💬 197 • 5h ago • [thestateofbrand.com](https://www.thestateofbrand.com/news/ai-subscription-time-bomb)

---

**[Access to frontier AI will soon be limited by economic and security constraints](https://news.ycombinator.com/item?id=48143284)**

Soon, access to frontier AI will be scarce and selective

⬆️ 224 • 💬 215 • 2d ago • [writing.antonleicht.me](https://writing.antonleicht.me/p/cut-off)

---

**[The AI zombification of universities](https://news.ycombinator.com/item?id=48139355)**

“And so perfect parallel constructions fill the lecture halls, the take-home tests, the school newspapers, and perhaps even the idiom of student chatter.”

⬆️ 193 • 💬 216 • 2d ago • [thenewcritic.com](https://www.thenewcritic.com/p/the-great-zombification)

---

---

## YouTube Videos: "ai"

**[The Trillion Dollar AI Lie. CEOs Are Bleeding BILLIONS.](https://www.youtube.com/watch?v=WhRyYdW-mbk)**

The Trillion Dollar AI Lie is already reshaping the global economy. OpenAI, NVIDIA, Big Tech, and corporate CEOs are burning ...

📺 The Infographics Show

👁️ 21K • 👍 1K • 💬 346 • ⏱️ 19:36 • 1h ago

---

**[Here&#39;s What Nobody&#39;s Telling You About AI Data Centers | Ep. 1780](https://www.youtube.com/watch?v=wEm1ZpL1PAg)**

Data centers are popping up everywhere, and there are some major issues that we need to discuss. Ep. 1780 -- -- -- LIKE ...

📺 Matt Walsh

👁️ 203K • 👍 11K • 💬 3K • ⏱️ 46:13 • 2d ago

---

**[AI Town Experiment Goes DOWN IN FLAMES](https://www.youtube.com/watch?v=5I2NpNnNiNM)**

Krystal, Ryan, Emily and Griffin discuss the downfall of an AI experimental town. Sign up for a PREMIUM Breaking Points ...

📺 Breaking Points

👁️ 105K • 👍 4K • 💬 634 • ⏱️ 12:40 • 1d ago

---

**[THE AI BUBBLE JUST KEEPS POPPING!](https://www.youtube.com/watch?v=VHeUxqVKbOY)**

Hello guys and gals, it's me Mutahar again! This time we take a look at what appears to be more cracks at the bubble keeping all ...

📺 SomeOrdinaryGamers

👁️ 154K • 👍 8K • 💬 913 • ⏱️ 25:36 • 16h ago

---

**[BREAKING: Data Centers KILL Americans as AI Race Takes DARK Turn](https://www.youtube.com/watch?v=0LIkmfgY-fA)**

Aaron Parnas reports on exclusive story of data centers around the country killing Americans, including a look at pollution let off by ...

📺 Aaron Parnas

👁️ 19K • 👍 3K • 💬 387 • ⏱️ 11:19 • 1d ago

---

**[AI Trust Is Collapsing. The Industry Is DELUSIONAL.](https://www.youtube.com/watch?v=FwRB_0XPICs)**

Head to https://betterhelp.com/infographics to get 10% off your first month with our sponsor, BetterHelp. Therapy can be a ...

📺 The Infographics Show

👁️ 234K • 👍 7K • 💬 2K • ⏱️ 19:17 • 1d ago

---

**[‘The Oppenheimer’ of the AI Era](https://www.youtube.com/watch?v=MHiVBoWB3OE)**

What drives the tech titans behind the AI arms race? For some, it's the thrill of scientific discovery; for others, it's the pursuit of profit.

📺 Bloomberg Television

👁️ 50K • 👍 1K • 💬 123 • ⏱️ 12:11 • 1d ago

---

**[AI scan sent an innocent grandma TO JAIL?!](https://www.youtube.com/watch?v=yccsobkbwFg)**

A Tennessee grandmother was wrongfully arrested after AI-powered facial recognition falsely identified her as a North Dakota ...

📺 ReasonTV

👁️ 124K • 👍 10K • 💬 1K • ⏱️ 1:17 • 2d ago

---

**[Microsoft’s New AI Beats Mythos And Shocks OpenAI](https://www.youtube.com/watch?v=idNpTUrr3r0)**

Try Higgsfield Supercomputer here: https://higgsfield.ai/s/super-computer-airevolutionx-RpneRv Microsoft just revealed MDASH, ...

📺 AI Revolution

👁️ 40K • 👍 1K • 💬 65 • ⏱️ 14:53 • 1d ago

---

**[Anthropic just admitted AI is bullsh*t](https://www.youtube.com/watch?v=juHv_Vi4giU)**

It's time to deploy yourself in the forward direction. https://x.com/@atmoio https://atmoio.substack.com ...

📺 Mo Bitar

👁️ 241K • 👍 13K • 💬 2K • ⏱️ 10:37 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 56,518 • ❤️ 683 • 9h ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 970,124 • ❤️ 1,064 • 8d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 20,208 • ❤️ 344 • 10d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 185,303 • ❤️ 219 • 2h ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 14,285 • ❤️ 370 • 2d ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 181,425 • ❤️ 202 • 2h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 3,140,341 • ❤️ 4,007 • 11d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 144,833 • ❤️ 519 • 5d ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles. It excels at generating illustrations and artistic images, with key capabilities including high-resolution output (up to 1536^2) and compatibility with ComfyUI workflows, making it ideal for digital artists and anime enthusiasts.

⬇️ 524,067 • ❤️ 1,370 • 2d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

Provides fixed Jinja chat templates for Qwen 3.5 & 3.6 models, resolving issues with tool calling, KV cache hit rates, and agentic loop stability for improved conversational AI and tool interaction.

⬇️ 0 • ❤️ 259 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 74 • 💬 3 • ⭐ 76,371 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 7 • 💬 0 • ⭐ 17,737 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 48 • 💬 2 • ⭐ 5,820 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 25,193 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Pixal3D: Pixel-Aligned 3D Generation from Images](https://huggingface.co/papers/2605.10922)**

*Dong-Yang Li, Wang Zhao, Yuxin Chen et al. (8 authors)*

🏢 ARC Lab, Tencent PCG

Pixal3D introduces a pixel-aligned 3D generation approach that addresses fidelity issues in 3D asset creation by establishing direct pixel-to-3D correspondences through back-projection conditioning.

▲ 27 • 💬 3 • ⭐ 857 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2605.10922) • [💻 code](https://github.com/TencentARC/Pixal3D) • [🔗 project](https://ldyang694.github.io/projects/pixal3d/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 20 • 💬 3 • ⭐ 11,634 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 116 • 💬 10 • ⭐ 9,609 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 63,355 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://huggingface.co/papers/2605.13724)**

*Yuchao Gu, Guian Fang, Yuxin Jiang et al. (7 authors)*

🏢 NVIDIA

AnyFlow introduces a novel any-step video diffusion distillation framework that improves upon consistency distillation by optimizing full ODE sampling trajectories through flow-map transition learning and backward simulation techniques.

▲ 89 • 💬 1 • ⭐ 250 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.13724) • [💻 code](https://github.com/NVlabs/AnyFlow) • [🔗 project](https://nvlabs.github.io/AnyFlow/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 73,785 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 13.1k • 🔱 3.0k • 20d ago

---

**[op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)**

AI-agent Skill for generating polished HTML slide decks: editorial magazine and Swiss layouts, image prompts, social covers, and a WebGL/low-power presentation runtime.

`HTML` `ai-agent` `claude-code` `codex` `html-deck` `image-generation`

⭐ 9.5k • 🔱 770 • 1d ago

---

**[esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)**

DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.

`TypeScript` `agent` `agent-framework` `ai-agent` `ai-coding` `cli`

⭐ 3.7k • 🔱 201 • 1h ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 3.5k • 🔱 364 • 34s ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.1k • 🔱 891 • 32m ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

A collection of agent skills for CAD, robotics and hardware design

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.9k • 🔱 358 • 18h ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 2.7k • 🔱 327 • 6h ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.3k • 🔱 156 • 5h ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.2k • 🔱 232 • 7d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.1k • 🔱 326 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
