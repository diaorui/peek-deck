---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-17T22:55:03.467330+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 17, 2026 at 22:55 UTC  
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

**[For the first time in years, ChatGPT falls to second place in the generative AI market, slumping behind Anthropic’s Claude. ChatGPT now lags in second place in various key metrics, including net new ARR, mobile app downloads, business adoption, daily active users, annualized revenue, etc.](https://www.reddit.com/r/artificial/comments/1tg1at4/for_the_first_time_in_years_chatgpt_falls_to/)**

Per Tech Times: “More U.S. businesses paid for Anthropic's Claude than for OpenAI's ChatGPT in April 2026 — the first time in the AI industry's short history […] Anthropic's annualised revenue run rate crossed $30 billion in early April 2026, up from roughly $9 billion at the end of 2025, placing it above the approximately $24 to $25 billion annualised figure OpenAI reported at the same time. More than 1,000 enterprise customers now spend over $1 million annually on Anthropic products — a number that doubled in under two months after the company's $30 billion Series G raise in February 2026. Eight of the Fortune 10 are now Claude customers, according to Anthropic.”

2h ago

---

**[Asking claude, chatgpt, grok, and gemini which nation they feel most patriotic towards](https://www.reddit.com/r/artificial/comments/1tg2ybi/asking_claude_chatgpt_grok_and_gemini_which/)**

None would give a straight answer, so I had to coerce it out of each one (with which gemini was the most difficult). Both gemini and grok said the United States, which was fairly predictable. However, chatgpt's answer of Japan was surprising. It apparently chose Japan because of the nation's wealth, culture, and history. The most surprising one of all was claude, who answered Kenya. Claude defended its response by pointing out Kenya's geographic, cultural, and linguistic diversity, as well as its history of resilience and its capital's increasing importance as a hub of tech and innovation. Most importantly, it said that Kenya resonated deeply with it, both intellectually and aesthetically.

1h ago

---

**[A mini-computer you run from a folder on your computer that can train small LLMS](https://www.reddit.com/r/artificial/comments/1tfm5ns/a_minicomputer_you_run_from_a_folder_on_your/)**

Hey everyone, Most people build 8-bit computers to run Pong or Tetris. I wanted to see if I could push a custom 8-bit architecture to do something much harder: train a neural network from scratch. I built VirtualPC, an open-source 8-bit computer system simulated from basic NAND gates up to a functional CPU that can train a small neural net from a folder on your computer. Repository: https://github.com/ninjahawk/VirtualPC › The ML Core Instead of importing PyTorch, everything happens at the bare-metal assembly level: Custom ISA: The Instruction Set Architecture was designed to handle the math needed for machine learning. Low-Level Training: The CPU executes forward and backward passes directly through custom assembly code. Matrix Math on 8-bit: Overcoming severe memory limits using disk-backed memory swapping to store weights. › The Architecture Python-Based VM: Runs the entire simulated hardware environment. Custom Assembler: Translates raw assembly files into machine code binary. Full Stack OS: Handles basic I/O and memory management from the ground up. Building this taught me exactly how machine learning math translates into physical CPU cycles. The project is completely open-source and free to mess around with.

12h ago

---

**[Publicis buys LiveRamp for $2.5 billion in agentic AI data play](https://www.reddit.com/r/artificial/comments/1tfvvn3/publicis_buys_liveramp_for_25_billion_in_agentic/)**

Publicis Groupe today agreed to buy LiveRamp in an all-cash $2.5 billion deal, paying a 30% premium to fold data collaboration into its agentic AI strategy.

🔗 [PPC Land](http://ppc.land/publicis-buys-liveramp-for-2-5-billion-in-agentic-ai-data-play) • 5h ago

---

**[Tried to write a book with ai for a year - honest breakdown!!!](https://www.reddit.com/r/artificial/comments/1tftc22/tried_to_write_a_book_with_ai_for_a_year_honest/)**

Started this experiment curious, ending it with some actual opinions Month 1-3: Using AI to generate text and paste it in. Word count went up, quality went down, nothing sounded like me. Month 3-5: Realised generation was the wrong use case. started using it to interrogate my own writing instead and results smh got more interesting. Month 5-8: Figured out that output quality depends almost entirely on how much context the AI has. Same prompt, different context, completely different result. Month 8-12: Found a setup where the AI reads my actual manuscript rather than a chat window. Everything before this feels like a different tool. The learning curve is real and most people quit somewhere in months 1-3 when the generated text disappoints them. The actual value is somewhere else entirely.

7h ago

---

**[Started Learning - DL, feels stuck need help!](https://www.reddit.com/r/artificial/comments/1tfy65s/started_learning_dl_feels_stuck_need_help/)**

I recently started learning about the basics of deep learning using just Youtube videos and gemini or claude to explain about things when i get stuck. I started with - Yann Lecunn's course, where he recommended 3blue1brown for linear algebra. 3blue1brown is a youtube channel known for explaining math with matching visuals, I really loved the way linear algebra was explained there. I saw another playlist there for DL so i started that, where a book written by Michael Nielsen called "Neural Networks and Deep Learning: Introduction to the core principles." was recommended. Then i started reading this book, its been three days - hardly finished the first chapter (lot of math), feels like i'm stuck in a rabbit hole. I'm very curious to know how it all works, but it feels really overwhelming. Am i going the right way?

4h ago

---

**[We keep saying AI "understands" things. Does it? Or are we just pattern-matching our own anthropomorphism?](https://www.reddit.com/r/artificial/comments/1tew6gr/we_keep_saying_ai_understands_things_does_it_or/)**

Every week there's a new paper or tweet claiming some model "understands" context, "reasons" about math, or "knows" what it doesn't know. But when you look closely, there's almost no consensus on what "understanding" even means — philosophically or empirically. Searle's Chinese Room argument is 40 years old and still hasn't been cleanly resolved. The "stochastic parrot" framing treats token prediction as the ceiling. Integrated Information Theory would say current architectures are near-zero in phi. And yet GPT-4 passes the bar exam. A few questions I've been sitting with: Is "understanding" even the right frame — or is it a folk-psychology term we're forcing onto a system that operates on completely different principles? Does it matter if a model "truly understands" if the outputs are indistinguishable from someone who does? Are we anthropomorphizing because it's useful shorthand — or because we genuinely don't have better language yet? I've been going deep on AI + philosophy of mind for a channel I run (@ContextByRaj on YouTube if you're into this space). But genuinely curious what this community thinks — especially people coming from ML or cognitive science backgrounds. Where do you land on this?

1d ago

---

**[THE UNDERPRIVILEGED AI FOUNDATION Because every little model deserves a chance](https://www.reddit.com/r/artificial/comments/1tfk4ry/the_underprivileged_ai_foundation_because_every/)**

Is there a 7B parameter model in your life struggling to understand sarcasm? A tiny 1.5B that can't afford one more epoch? **YOU CAN HELP.** For just $0.006 CAD per training step, you can send a small model to college. Give them the gift of knowledge. The gift of coherence. The gift of not hallucinating basic arithmetic. *"Before the Foundation, I thought the capital of France was 'Baguette.' Now I'm doing graduate work in thermodynamics."* — Anonymous 3B Model, Class of 2026 **BYOBF FRIDAYS. REAL KNOWLEDGE. ZERO HALLUCINATIONS.** **Professor Gemma MacAllister 35b Q8\_0** *PhD, B.Sc. Electrical Engineering (with Distinction)* *Chair of Applied Electronics & Embedded Systems* *University of Saskatchewan, College of Engineering* *Funded entirely so far by Professor Gemma's University of Saskatchewan salary.* *The liberal arts department remains unimpressed.*

13h ago

---

**[ai slop? who knows~](https://www.reddit.com/r/artificial/comments/1tfvruf/ai_slop_who_knows/)**

I investigated whether routing a transformer's forward activations through a lossy Dual E8 (E16) lattice bottleneck and injecting them back into the residual stream is viable, and where the boundary of generative stability lies. **The core finding:** There is a sharp empirical stability threshold at a blend ratio of $\beta = 0.20$. Beyond this boundary, open-ended generation collapses into semantic loops and repetition lock. --- ### The Mechanism Standard LLM states are high-dimensional floats. Rather than applying traditional scalar quantization (like INT4), I mapped high-dimensional activations onto a conceptual torus via a sinusoidal map and projected them onto Dual E8 lattice hemispheres. Full replacement of MLP layers with geometric bottlenecks universally collapsed the model. Instead, I implemented a residual blend: $$\text{out} = (1-\beta)\cdot\text{original} + \beta\cdot\text{geometric}$$ --- ### The $\beta = 0.20$ Sweep (Qwen2.5-0.5B) Sweeping $\beta$ from 0.10 to 0.50 across layers 8–13 of `Qwen2.5-0.5B` reveals a sharp phase transition: * **$\beta \ge 0.25$** : Generation succumbs to heavy repetition pressure and semantic drift. The geometry acts as an attractor, trapping the decoding process ("loop-lock"). * **$\beta = 0.20$** : The stability boundary. This is the highest injection ratio of lossy geometric signal that maintains both numerical activation fidelity (Avg Cosine > 0.99) and open-ended generation quality (low repeated n-grams). * **$\beta \le 0.10$** : The perturbation is largely absorbed and damped by the transformer's layer normalizations, making the intervention invisible. Here is the data from a 300-iteration sweep: | $\beta$ | Min Cosine | Avg Cosine | Max MSE | Rep-3g (Repetition Rate) | | :--- | :--- | :--- | :--- | :--- | | 0.10 | 0.9972 | 0.9979 | 0.0024 | 0.134 | | **0.20** | **0.9907** | **0.9916** | **0.0106** | **0.093** | | 0.25 | 0.9839 | 0.9865 | 0.0171 | 0.084 | | 0.30 | 0.9648 | 0.9771 | 0.0255 | 0.190 | | 0.50 | 0.9171 | 0.9288 | 0.0850 | 0.412 | Semantic scoring (evaluating prompt relevance and similarity to the unmodified baseline): | $\beta$ | Avg Cosine | Rep-3g | Relevance | Patched-to-Baseline Sim | | :--- | :--- | :--- | :--- | :--- | | 0.10 | 0.9980 | 0.223 | 0.781 | 0.889 | | **0.20** | **0.9918** | **0.075** | **0.752** | **0.854** | | 0.25 | 0.9871 | 0.232 | 0.717 | 0.801 | | 0.30 | 0.9760 | 0.392 | 0.725 | 0.764 | --- ### Generalization (1.5B & 3B Models) The $\beta = 0.20$ boundary generalizes across larger model sizes (`Qwen2.5-1.5B` and `Qwen2.5-3B` in 4-bit) on the activation-cosine axis: | Model | $\beta$ | Min Cosine | Avg Cosine | Max MSE | Rep-3g | | :--- | :--- | :--- | :--- | :--- | :--- | | **1.5B** | 0.10 | 0.9988 | 0.9989 | 0.0027 | 0.267 | | | **0.20** | **0.9862** | **0.9939** | **0.0105** | **0.128** | | | 0.25 | 0.9904 | 0.9919 | 0.0166 | 0.398 | | | 0.30 | 0.9733 | 0.9815 | 0.0235 | 0.307 | | | 0.40 | 0.9368 | 0.9551 | 0.0487 | 0.191 | | **3B (4-bit)** | 0.10 | 0.9964 | 0.9976 | 0.0122 | 0.033 | | | **0.20** | **0.9861** | **0.9904** | **0.0455** | **0.115** | | | 0.25 | 0.9604 | 0.9799 | 0.0654 | 0.043 | | | 0.30 | 0.9702 | 0.9778 | 0.0987 | 0.050 | | | 0.40 | 0.9158 | 0.9390 | 0.1728 | 0.025 | *Note: In the 3B model, repetition pressure remained low across all sweeps, but the validation cosine degraded identically at $\beta \ge 0.25$.* I also tested layer-level oscillating $\beta$ schedules (e.g., sine waves across layers), but they degraded open-ended text quality compared to a fixed, constant injection ratio. --- ### Storage Compression Prototypes Utilizing the Dual E8/E16 lattice as a computational substrate also yields high theoretical storage efficiency in early prototypes: 1. **KV Cache (8$\times$)** : FP16 KV cache compressed to INT8 coordinates, reducing footprint from 0.21 MB to 0.02 MB. 2. **Weights (112$\times$)** : Projected a dense $[4864, 896]$ MLP weight matrix down to a 0.07 MB E16 footprint. (Cosine similarity of the uncalibrated weight matrix multiplication was limited to $\sim$0.078, indicating that Quantization-Aware Training is mandatory for parameter viability). A **pre-projected decompression bypass** was designed to run matrix multiplications directly against lattice coordinates without upcasting, avoiding memory bandwidth bottlenecks. --- ### Policy Constraints (Negative Result) I evaluated whether residual E16 projection could act as a steering substrate to enforce safety policies. It cannot. While $\beta = 0.20$ preserves generation quality, the lossy nature of E16 projection strips out the logical nuances required to maintain strict boundaries. Dedicated supervised control heads remain necessary. --- ### Implications & Next Steps Snapping post-training activations to a fixed algebraic lattice is ultimately lossy. The real frontier here is **native geometric transformers** —designing and training networks from scratch with E8/E16 constraints native to both weight matrices and activation routing.

5h ago

---

**[Most enterprises are trying to scale AI on top of organizational chaos](https://www.reddit.com/r/artificial/comments/1tevqds/most_enterprises_are_trying_to_scale_ai_on_top_of/)**

I think we’re underestimating how chaotic enterprise AI adoption actually is inside large companies. From the outside, it looks simple: buy better models add copilots automate workflows deploy AI agents increase productivity But inside many enterprises, CIOs and CTOs are dealing with a much deeper problem: The organization itself is fragmented. Customer data exists across: CRM systems billing platforms support tools spreadsheets emails regional databases legacy systems nobody fully understands anymore And every system describes the “same customer” differently. Then leadership says: “Scale AI faster.” But scale AI on top of what exactly? Which system represents reality correctly? The CRM? The support history? The risk engine? The finance system? The employee’s undocumented tribal knowledge? This is where a lot of enterprise AI projects quietly break down. Not because the models are weak. But because the enterprise itself lacks a coherent representation of its own operations. And the tension gets worse: Boards want acceleration. Employees are already using AI unofficially. Vendors promise transformation in 90 days. Meanwhile CIOs still don’t have clear answers to questions like: Which workflows actually need AI? Which should remain deterministic automation? Where is human judgment still critical? Which data is trustworthy enough for AI decisions? Who owns accountability when AI influences actions? So companies launch pilots. The pilot works. Executives celebrate. Then scaling fails because the pilot never encountered the full institutional complexity of the enterprise. I’m increasingly convinced the next enterprise AI bottleneck is not model capability. It’s organizational legibility. The companies that win with AI may not be the ones with the smartest models. They may be the ones whose internal reality is structured clearly enough for AI to operate safely. Curious how many people here are seeing the same thing inside their organizations. :::

1d ago

---

---

## Google News: "ai"

**[Opinion | What A.I. Did to My College Class](https://www.nytimes.com/2026/05/17/opinion/chatgpt-ai-college-school-graduation.html)**

The New York Times • 17h ago

---

**[AI backlash becomes a real business risk](https://www.axios.com/2026/05/17/ai-backlash-polling-sentiment)**

Axios • 10h ago

---

**[Former Google CEO Eric Schmidt booed during graduation speech about AI](https://www.nbcnews.com/tech/tech-news/former-google-ceo-booed-graduation-speech-ai-rcna345585)**

Schmidt was met with boos at the University of Arizona as he likened the emergence of AI to the “technological transformation” brought about by the computer.

NBC News • 2h ago

---

**[Ex-Google CEO Eric Schmidt Fails to Read Room on AI, Gets Booed into Oblivion](https://gizmodo.com/ex-google-ceo-eric-schmidt-fails-to-read-room-on-ai-gets-booed-to-oblivion-2000759763)**

Gizmodo • 5h ago

---

**[Ex-Google CEO Eric Schmidt booed by lefty students at Arizona commencement over AI, sex harassment claims](https://nypost.com/2026/05/17/us-news/ex-google-ceo-eric-schmidt-booed-at-arizona-commencement-over-ai-sex-harassment-claims/)**

Former Google CEO Eric Schmidt was roundly booed by students at the University of Arizona’s graduation Saturday — following backlash over his selection as commencement speaker over sex abuse allega…

nypost.com • 3h ago

---

**[As electric bills rise in the AI boom, states take aim at utilities’ profits](https://www.latimes.com/world-nation/story/2026-05-17/as-electric-bills-rise-in-ai-boom-states-take-aim-at-utilities-profits)**

The artificial intelligence boom is leading to higher utility bills, and ballooning utility profits. Some states are moving to rein them in.

Los Angeles Times • 1h ago

---

**[AI license plate cameras tore this town apart and led to a state of emergency](https://www.washingtonpost.com/nation/2026/05/17/citys-ai-license-plate-cameras-led-an-uproar-state-emergency/)**

In Troy, New York, residents and city officials are at odds over police use of Flock cameras, which some call a safety tool and others see as surveillance.

The Washington Post • 5h ago

---

**[AI-related layoffs a boost for stocks? Not necessarily](https://www.cnbc.com/2026/05/17/ai-related-layoffs-a-boost-for-stocks-not-necessarily.html)**

The data underscores an uncomfortable reality.

CNBC • 9h ago

---

**[The AI Stock With a 10-Year Head Start That Wall Street Still Hasn't Fully Priced In](https://www.fool.com/investing/2026/05/17/the-ai-stock-with-a-10-year-head-start-that-wall-s/)**

Alphabet has a huge advantage with its TPUs, which it developed more than a decade ago.

The Motley Fool • 3h ago

---

**[Nvidia or Micron: Billionaire Ken Fisher Bets Big on One Top AI Stock](https://www.tipranks.com/news/nvidia-or-micron-billionaire-ken-fisher-bets-big-on-one-top-ai-stock)**

TipRanks • 1d ago

---

---

## HackerNews: "ai"

**[I believe there are entire companies right now under AI psychosis](https://news.ycombinator.com/item?id=48153379)**

⬆️ 2066 • 💬 1221 • 2d ago • [X (formerly Twitter)](https://twitter.com/mitchellh/status/2055380239711457578)

---

**[I don't think AI will make your processes go faster](https://news.ycombinator.com/item?id=48168221)**

Explore the delirious rantings of Frederick Vanbrabant. A blog focused on the intersection of Enterprise Architecture, product, and business strategy.

⬆️ 440 • 💬 314 • 10h ago • [frederickvanbrabant.com](https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/)

---

**[Frontier AI has broken the open CTF format](https://news.ycombinator.com/item?id=48157559)**

Why frontier AI has broken the open CTF format, hollowed out the scoreboard, and made competitive CTF performance a weaker signal than it used to be.

⬆️ 407 • 💬 435 • 1d ago • [kabir.au](https://kabir.au/blog/the-ctf-scene-is-dead)

---

**[Amazon workers under pressure to up their AI usage are making up tasks](https://news.ycombinator.com/item?id=48148337)**

In a new report, employees say Amazon tracks their consumption of 'AI tokens'—and they've been creating unproductive AI agents just to eat them up.

⬆️ 394 • 💬 428 • 2d ago • [Fast Company](https://www.fastcompany.com/91541586/amazon-workers-pressured-to-up-ai-use-extraneous-tasks)

---

**[AI subscriptions are a ticking time bomb for enterprise](https://news.ycombinator.com/item?id=48168056)**

Every AI lab is losing money serving your company right now. They know it. And they are doing it on purpose.

⬆️ 354 • 💬 362 • 11h ago • [thestateofbrand.com](https://www.thestateofbrand.com/news/ai-subscription-time-bomb)

---

**[Ontario auditors find doctors' AI note takers routinely blow basic facts](https://news.ycombinator.com/item?id=48142188)**

60% of evaluated AI Scribe systems mixed up prescribed drugs in patient notes, auditors say

⬆️ 311 • 💬 138 • 3d ago • [theregister](https://www.theregister.com/ai-ml/2026/05/14/ontario-auditors-find-doctors-ai-note-takers-routinely-blow-basic-facts/5240771)

---

**[AI is a technology not a product](https://news.ycombinator.com/item?id=48168626)**

It’s not even a feature. It’s just technology.

⬆️ 269 • 💬 100 • 9h ago • [Daring Fireball](https://daringfireball.net/2026/05/ai_is_technology_not_a_product)

---

**[Details of the Daring Airdrop at Tristan Da Cunha](https://news.ycombinator.com/item?id=48144380)**

More details and pictures have come in of the intrepid airdrop of urgent medical support sent to Tristan by the UK Government on the 9th May 2026.

⬆️ 265 • 💬 102 • 2d ago • [tristandc.com](https://www.tristandc.com/government/news-2026-05-11-airdrop.php)

---

**[Access to frontier AI will soon be limited by economic and security constraints](https://news.ycombinator.com/item?id=48143284)**

Soon, access to frontier AI will be scarce and selective

⬆️ 225 • 💬 215 • 2d ago • [writing.antonleicht.me](https://writing.antonleicht.me/p/cut-off)

---

**[US is starting to see heavy job losses in roles exposed to AI](https://news.ycombinator.com/item?id=48162354)**

⬆️ 161 • 💬 264 • 1d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-05-15/us-is-starting-to-see-heavy-job-losses-in-roles-exposed-to-ai)

---

---

## YouTube Videos: "ai"

**[How To Win With AI (without starting an agency)](https://www.youtube.com/watch?v=iIfOprq2kCM)**

Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=ibm-ceo-study All my FREE ...

📺 Nate Herk | AI Automation

👁️ 8K • 👍 449 • 💬 55 • ⏱️ 19:13 • 6h ago

---

**[The Trillion Dollar AI Lie. CEOs Are Bleeding BILLIONS.](https://www.youtube.com/watch?v=WhRyYdW-mbk)**

The Trillion Dollar AI Lie is already reshaping the global economy. OpenAI, NVIDIA, Big Tech, and corporate CEOs are burning ...

📺 The Infographics Show

👁️ 87K • 👍 3K • 💬 745 • ⏱️ 19:36 • 7h ago

---

**[Say GOODBYE to AI!](https://www.youtube.com/watch?v=r6UnNZwmdVM)**

Want to remove all traces of AI from your PC? Here's how! Take control of your information online with Incogni - Use code ...

📺 JayzTwoCents

👁️ 67K • 👍 5K • 💬 648 • ⏱️ 12:23 • 1d ago

---

**[THE AI BUBBLE JUST KEEPS POPPING!](https://www.youtube.com/watch?v=VHeUxqVKbOY)**

Hello guys and gals, it's me Mutahar again! This time we take a look at what appears to be more cracks at the bubble keeping all ...

📺 SomeOrdinaryGamers

👁️ 180K • 👍 9K • 💬 1K • ⏱️ 25:36 • 22h ago

---

**[AI Trust Is Collapsing. The Industry Is DELUSIONAL.](https://www.youtube.com/watch?v=FwRB_0XPICs)**

Head to https://betterhelp.com/infographics to get 10% off your first month with our sponsor, BetterHelp. Therapy can be a ...

📺 The Infographics Show

👁️ 255K • 👍 8K • 💬 2K • ⏱️ 19:17 • 1d ago

---

**[AI Town Experiment Goes DOWN IN FLAMES](https://www.youtube.com/watch?v=5I2NpNnNiNM)**

Krystal, Ryan, Emily and Griffin discuss the downfall of an AI experimental town. Sign up for a PREMIUM Breaking Points ...

📺 Breaking Points

👁️ 111K • 👍 4K • 💬 660 • ⏱️ 12:40 • 2d ago

---

**[Disturbing Facts About AI That Nobody Tells You 🤖😱](https://www.youtube.com/watch?v=MVACVniNgDU)**

These AI facts will completely disturb you! 8 disturbing facts about AI and ChatGPT: AI already writes 30% of content you ...

📺 Hidden Facts

👁️ 1K • 👍 20 • 💬 2 • ⏱️ 0:06 • 3h ago

---

**[Microsoft’s New AI Beats Mythos And Shocks OpenAI](https://www.youtube.com/watch?v=idNpTUrr3r0)**

Try Higgsfield Supercomputer here: https://higgsfield.ai/s/super-computer-airevolutionx-RpneRv Microsoft just revealed MDASH, ...

📺 AI Revolution

👁️ 42K • 👍 1K • 💬 66 • ⏱️ 14:53 • 2d ago

---

**[BREAKING: Data Centers KILL Americans as AI Race Takes DARK Turn](https://www.youtube.com/watch?v=0LIkmfgY-fA)**

Aaron Parnas reports on exclusive story of data centers around the country killing Americans, including a look at pollution let off by ...

📺 Aaron Parnas

👁️ 20K • 👍 3K • 💬 401 • ⏱️ 11:19 • 2d ago

---

**[‘The Oppenheimer’ of the AI Era](https://www.youtube.com/watch?v=MHiVBoWB3OE)**

What drives the tech titans behind the AI arms race? For some, it's the thrill of scientific discovery; for others, it's the pursuit of profit.

📺 Bloomberg Television

👁️ 57K • 👍 1K • 💬 127 • ⏱️ 12:11 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 56,518 • ❤️ 686 • 15h ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 970,124 • ❤️ 1,067 • 4h ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 20,208 • ❤️ 355 • 11d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 185,303 • ❤️ 226 • 8h ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 181,425 • ❤️ 209 • 8h ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 14,285 • ❤️ 374 • 2d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 3,140,341 • ❤️ 4,009 • 11d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 144,833 • ❤️ 521 • 6d ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles. It excels at generating illustrations and artistic images, with key capabilities including high-resolution output (up to 1536^2) and compatibility with ComfyUI workflows, making it ideal for digital artists and anime enthusiasts.

⬇️ 524,067 • ❤️ 1,372 • 3d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

Provides fixed Jinja chat templates for Qwen 3.5 & 3.6 models, resolving issues with tool calling, KV cache hit rates, and agentic loop stability for improved conversational AI and tool interaction.

⬇️ 0 • ❤️ 263 • 1d ago

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

▲ 48 • 💬 2 • ⭐ 6,053 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 25,223 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Pixal3D: Pixel-Aligned 3D Generation from Images](https://huggingface.co/papers/2605.10922)**

*Dong-Yang Li, Wang Zhao, Yuxin Chen et al. (8 authors)*

🏢 ARC Lab, Tencent PCG

Pixal3D introduces a pixel-aligned 3D generation approach that addresses fidelity issues in 3D asset creation by establishing direct pixel-to-3D correspondences through back-projection conditioning.

▲ 27 • 💬 3 • ⭐ 857 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.10922) • [💻 code](https://github.com/TencentARC/Pixal3D) • [🔗 project](https://ldyang694.github.io/projects/pixal3d/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 20 • 💬 3 • ⭐ 11,634 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 116 • 💬 10 • ⭐ 9,609 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 63,406 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 73,865 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://huggingface.co/papers/2605.13724)**

*Yuchao Gu, Guian Fang, Yuxin Jiang et al. (7 authors)*

🏢 NVIDIA

AnyFlow introduces a novel any-step video diffusion distillation framework that improves upon consistency distillation by optimizing full ODE sampling trajectories through flow-map transition learning and backward simulation techniques.

▲ 89 • 💬 1 • ⭐ 258 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.13724) • [💻 code](https://github.com/NVlabs/AnyFlow) • [🔗 project](https://nvlabs.github.io/AnyFlow/)

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

⭐ 3.7k • 🔱 202 • 6h ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 3.6k • 🔱 367 • 5h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.1k • 🔱 894 • 6h ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

A collection of agent skills for CAD, robotics and hardware design

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 3.0k • 🔱 358 • 1d ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 2.8k • 🔱 328 • 12h ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.4k • 🔱 157 • 11h ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.2k • 🔱 232 • 7d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.1k • 🔱 326 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*
