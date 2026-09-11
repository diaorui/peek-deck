---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-11T16:00:13.543739+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 11, 2026 at 16:00 UTC  
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

**[One cheeseburger has roughly the greenhouse gas emissions of 63,000 Gemini AI text prompts.](https://www.reddit.com/r/artificial/comments/1wd1dpf/one_cheeseburger_has_roughly_the_greenhouse_gas/)**

A 2024 University of Wisconsin–Madison paper estimates that "one cheeseburger equates to 1.9 kg of CO₂e emissions". Google’s 2025 research paper reports that "a median Gemini Apps text prompt generates 0.03 gCO2e". That's 1,900 grams of CO₂e emissions per cheeseburger. That’s 0.03 grams of CO₂e emissions per Gemini text prompt. 1,900 ÷ 0.03 ≈ 63,000 prompts. I'm just sharing this as a reality check. You could prompt Gemini every day 150 times a day for a year and it still wouldn't equal one cheeseburger.

15h ago

---

**[AI companies pursue the Boromir strategy to deal with the control problem. "It's dangerous. But let that be me. I know what to do with it."](https://www.reddit.com/r/artificial/comments/1wcwues/ai_companies_pursue_the_boromir_strategy_to_deal/)**

18h ago

---

**[Polish developer builds app that detects nearby Meta smart glasses](https://www.reddit.com/r/artificial/comments/1wdcik5/polish_developer_builds_app_that_detects_nearby/)**

Polish developers made an iPhone app that can detect nearby Meta smart glasses Apparently a group of Polish developers created an iPhone app that can detect nearby Meta smart glasses. It’s an interesting idea especially with the privacy concerns around smart glasses and cameras. Knowing that someone nearby might be wearing one could be useful. At the same time I am curious how accurate the app actually is and whether it can reliably detect the glasses in real world situations. Would you guys actually use something like this?

🔗 [tvpworld.com](https://tvpworld.com/95328093/polish-developers-iphone-app-detects-nearby-meta-smart-glasses) • 5h ago

---

**[5 things I've noticed that still make AI video read as AI](https://www.reddit.com/r/artificial/comments/1wdbmwj/5_things_ive_noticed_that_still_make_ai_video/)**

I have been messing around with generated videos for a while, and did a bit of research trying to figure out why clips that look great on their own can still feel off when you put them in sequence. It's mostly not the obvious stuff people used to complain about. The physics of small things, Faces and bodies are getting pretty convincing, but smaller physical details still give away constantly. Hair, clothes, water, smoke, loose objects, etc. are things that our brains are wired to notice when they're not behaving correctly. A coat that looks like it has no weight to it is the easiest tell. Specifing material, weight and how it should move instead of just describing how it looks tends to somewhat do the trick. (Here's a CogVideoX tech paper on unnatural physics.) The camera has no operator, Real hand held footage has breathing, hesitation, little corrections and changes in speed. Generated hand held gets the general movement right but smooths out the small human imperfections. For example, a clip that's supposed to feel like a person running away from an SCP or something with a camera ends up feeling more like a gimbal or drone. Can't figure out how to fix at generation, so I just add actual handheld movement in post. Everything sits at roughly the same distance from the lens, This one kept showing up in my own generations. You can have technically different shots, but they all end up with roughly the same framing and subject size, the sequence starts feeling weird before I can explain why. Real coverage tends to jump between wides, mediums, close-ups, inserts, reaction shots etc. Six medium-ish shots in a row feels ... Wrong. Specifying the shot size everytime tends to alleviate it. (Link here for what I researched through) Light does not carry between shots, This one's brutal. Two shots can look completely believable on their own, but if one has the key light/sun coming from the left and the next cut shows it coming from somewhere completely different, it immediately seems artificial. There are actual papers researching this so I am apparently not the only person annoyed. Mostly seems like a workflow problem imo. Locking the time of day, general light direction and quality then keep repeating it seems like a good choice. Uniform shot length, Everything comes out around the same length that the tool gives you, so it's really easy to just use the whole clip everytime. Do that five or six times in a row and suddenly! You're watching a slideshow instead of a sequence. Shot duration and editing rhythm obviously aren't an AI specific problem, but there's plenty of film research on how much they affect pacing and perception. This one is completely fixable in post, but people really underestimate how much it matters. (Link!) These are just things I have started noticing the most. I'm curious as to see what others have found. What's your AI-Video tell that you just can't unsee?

6h ago

---

**[Built an AI memory system that actually refuses to hallucinate](https://www.reddit.com/r/artificial/comments/1wd8fl0/built_an_ai_memory_system_that_actually_refuses/)**

Hey everyone, I have been working on a project for a while now. It is a custom RNS-AI architecture written in Python that runs locally on a single CPU core using a basic SQLite database. The main reason I built this is because standard LLMs drive me crazy with hallucinations and catastrophic forgetting. They just merge everything into a giant statistical blob of weights. If you ask a question and the model does not know the answer, it just guesses something plausible to please you. That does not work if you need the system for high risk environments like medical decision support, where total auditability and clear provenance chains are mandatory. My System works on a completely different rule: no black box, no unearned answers, no word filters. Instead of using dense vectors, it stores context hypotheses in a shadow layer while reading. It never erases errors or contradicted data because mistakes are valuable evidence. Before a hypothesis becomes an accepted fact, it has to survive multiple slow wave sleep cycles. This is an active consolidation phase where the system uses stochastic replay to test if a hypothesis remains stable over time. If there is no verified anchor in the database for your query, the system simply reports the gap instead of guessing. I am using terms like sleep and neuromodulation on purpose because the code actually mimics those exact functional mechanics at an algorithmic level. For instance, dynamic floating point parameters continuously tune excitation, inhibition, and sleep pressure to keep the system balanced without needing gradient descent. In recent production tests over a 664 MB Wikipedia corpus, it processed around 155k chunks and tracked over 1.4 million hypotheses on a single CPU thread without breaking down or corrupting its state. I am currently validating the hypothesis graduation pipeline and would love to hear your thoughts. How do you guys deal with parameter saturation or balancing strict line of sight provenance against fluid generalization in continuous learning loops?

9h ago

---

**[California enacts laws restricting chatbots and banning teens from ‘addictive’ social media](https://www.reddit.com/r/artificial/comments/1wd2r40/california_enacts_laws_restricting_chatbots_and/)**

🔗 [calmatters.org](https://calmatters.org/economy/technology/2026/09/california-enacts-laws-restricting-chatbots-protecting-kids-online/) • 14h ago

---

**[Mathematicians confront the AI apocalypse](https://www.reddit.com/r/artificial/comments/1wdhp11/mathematicians_confront_the_ai_apocalypse/)**

What happens when machines surpass the most brilliant human minds? Mathematicians are finding out

🔗 [Scientific American](https://www.scientificamerican.com/article/mathematicians-confront-the-ai-apocalypse/) • 1h ago

---

**[Anthropic published a model of its own product's effect on the labor market. The extreme scenario has cognitive unemployment at 17.9% and labor's share of GDP falling from 60% to 45%.](https://www.reddit.com/r/artificial/comments/1wcjmg9/anthropic_published_a_model_of_its_own_products/)**

Three scenarios, explicitly not predictions, no probabilities attached. Modest is internet-sized at 1.6% GDP above the no-AI path by 2030. Substantial is 8.3%. Extreme is 32.4%. In the extreme case: cognitive unemployment 17.9%, overall 11.9%, which is past any postwar US peak. Cognitive wages 11.5% below trend on 21.5% fewer jobs. Labor's share of income falls from 60% to 45.2%. But wages in non-cognitive work go up 33.6%, so this isn't a story about everyone losing. It's a story about which half of the workforce you're in. The number that got me is in their Table 3. Total labor income ends up 0.5% above the no-AI path while GDP is a third larger. Capital income is up 81.4%. Essentially the entire gain goes to capital. Their own text says holding cognitive workers whole would take a transfer around 9% of GDP, about Social Security and Medicare combined, and that transfers at that scale in response to technology have no precedent. Worth knowing the extreme scenario assumes zero new human tasks get created. That assumption is doing real work in the result. Their caveats: no policy response, no business cycles, no financial disruption, no catastrophic risk, no robots.

🔗 [anthropic.com](https://www.anthropic.com/institute/econ-scenarios) • 1d ago

---

**[AI in Anti-Money Laundering: Use Cases, Benefits & How It Works](https://www.reddit.com/r/artificial/comments/1wdf24n/ai_in_antimoney_laundering_use_cases_benefits_how/)**

Discover how AI helps institutions adapt to evolving AML compliance demands and financial crime risks in 2026.

🔗 [Sumsub](https://sumsub.com/blog/ai-in-anti-money-laundering-and-compliance/?utm_source=reddit&utm_medium=social) • 3h ago

---

**[Genuine Question About Citizenship](https://www.reddit.com/r/artificial/comments/1wcdc90/genuine_question_about_citizenship/)**

1d ago

---

---

## Google News: "ai"

**[How Would AI Actually Kill Us All? What to Know About the AI Doomsday Debate](https://www.wsj.com/tech/ai/how-would-ai-actually-kill-us-all-what-to-know-about-the-ai-doomsday-debate-034270d1)**

WSJ • 1d ago

---

**[Dollars and doomers in the AI safety debate](https://www.axios.com/2026/09/11/dollars-doomers-ai-safety-financial-crisis)**

Axios • 1h ago

---

**[SpaceX signs another AI computing deal, with $100 billion in ARR 'on track,' CFO says](https://finance.yahoo.com/markets/stocks/article/spacex-signs-another-ai-computing-deal-with-100-billion-in-arr-on-track-cfo-says-152933886.html)**

SpaceX just inked another big AI compute deal, one that will take the space and rocket company closer to its $100 billion annual recurring revenue (ARR) target this year, a big metric for investors.

finance.yahoo.com • 30m ago

---

**[Roundup: Meta power case / AI weaponization / Post-9/11 flying](https://www.businessreport.com/article/roundup-meta-power-case-ai-weaponization-post-9-11-flying)**

More transparency: Entergy Louisiana has agreed to expand access to highly confidential information in its power expansion case tied to Meta’s Richland Parish data center, allowing seven consumer advocates to review protected materials and their experts’ testimony. However, the groups still cannot access Meta records supporting projected jobs, investment and electricity demand. The case involves […]

Baton Rouge Business Report • 1h ago

---

**[Rebels used Anthropic’s AI bot to develop guided weapons, report says](https://www.washingtonpost.com/technology/2026/09/11/rebels-used-anthropics-ai-bot-develop-guided-weapons-report-says/)**

Militants in Yemen sought to use a coding tool to produce guided rockets and missiles, the firm found, noting it was able to block some but not all the requests.

The Washington Post • 22m ago

---

**[Houthis used Anthropic AI to try to build ballistic missiles](https://www.ft.com/content/8310cf56-ce60-4e6e-8254-5bb470e9a880?syn-25a6b1a6=1)**

Missile test by group apparently failed, but exposes limits of AI safeguards

Financial Times • 6h ago

---

**[Anthropic says Yemeni weapons cell used its AI to try to build missile guidance software](https://www.latimes.com/business/story/2026-09-11/anthropic-says-yemeni-weapons-cell-used-its-ai-to-try-to-build-missile-guidance-software)**

Anthropic uncovered a group in northern Yemen — where Iran-backed Houthi militants operate — using its Claude AI model to support the development of missile and rocket systems, highlighting growing concerns over the use of advanced AI in military programs and by non-state actors.

Los Angeles Times • 1h ago

---

**[Anthropic blocks possible attempt to use AI to make biological weapons](https://www.bbc.com/news/articles/cx2zrrpkx20o)**

The revelations in Anthropic's threat intelligence report come after a former top researcher at the company warned of the risks of AI to humanity.

BBC • 7h ago

---

**[The Gemini app is now available for Windows](https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-windows/)**

We’re launching the Gemini app for Windows, the new desktop app built to work alongside your favorite tools and daily applications.

blog.google • 23h ago

---

**[Trump dismisses AI extinction risks as more than a dozen OpenAI, Anthropic insiders call for a slowdown](https://www.cnbc.com/2026/09/11/trump-ai-extinction-risks.html)**

Trump said he isn't concerned AI could cause human extinction as researchers at leading AI companies warn about rapid advances and lawmakers propose safeguards.

CNBC • 5h ago

---

---

## HackerNews: "ai"

**[Muse – Meta’s personal AI agent](https://news.ycombinator.com/item?id=49615537)**

Meet Muse, Meta's personal AI agent. Learn what it can do across everyday tasks, how it works, and how it helps you get more done.

⬆️ 655 • 💬 735 • 2d ago • [ai.meta.com](https://ai.meta.com/muse/)

---

**[Ask HN: Can we please limit the AI news flood?](https://news.ycombinator.com/item?id=49657850)**

⬆️ 612 • 💬 295 • 2h ago

---

**[AirPods 5](https://news.ycombinator.com/item?id=49630253)**

Apple today announced AirPods 5, delivering the industry’s best Active Noise Cancellation in an open-ear design and even better sound quality.

⬆️ 507 • 💬 449 • 1d ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/09/apple-introduces-airpods-5-with-best-in-class-open-ear-active-noise-cancellation/)

---

**[Tao: Open math problems being non-renewably mined by AI](https://news.ycombinator.com/item?id=49616968)**

I wrote recently about how the collection of good, fruitful open problems is now being mined in a non-renewable fashion, leading to the potential scenario of these problems becoming scarce.  This may seem unintuitive at first, since the set of possible problems one could ask is infinite.  Perhaps the following analogy can help: a country or region can suffer a critical shortage of drinking water while simultaneously being surrounded by a massive ocean.

One can easily generate any number of open problems in mathematics at will, such as working out the 10^10^10th digit of pi.  But the vast majority of such problems are not worth focusing attention on: they show no particular propensity to reveal any further insights or connections to other questions, or may either be too easy or too impossible relative to known techniques to learn anything from the exercise.  (1/4)

⬆️ 488 • 💬 418 • 2d ago • [Mathstodon](https://mathstodon.xyz/@tao/117237320796901560)

---

**[The Waymo effect: how AI is quietly making research less collaborative](https://news.ycombinator.com/item?id=49656496)**

How frictionless technologies teach us to prefer our own company – and why research leaders should worry.

⬆️ 297 • 💬 231 • 4h ago • [Research Agenda](https://www.researchagenda.news/articles/the-waymo-effect.html)

---

**[How An AI math breakthrough ignited a controversy](https://news.ycombinator.com/item?id=49624163)**

⬆️ 220 • 💬 231 • 2d ago • [science.org](https://www.science.org/content/article/how-ai-math-breakthrough-ignited-controversy)

---

**[Muse, the band, lost its social media handles to Muse, Meta's new AI agent](https://news.ycombinator.com/item?id=49636345)**

The exact circumstances surrounding the changes aren't clear, but Meta execs have accidentally tagged the band instead of their AI agent.

⬆️ 183 • 💬 8 • 1d ago • [Engadget](https://www.engadget.com/2254419/muse-the-band-lost-its-social-media-handles-to-muse-meta-s-new-ai-agent/)

---

**[Detecting and countering misuse of AI: September 2026](https://news.ycombinator.com/item?id=49647300)**

Case studies from threat actors disrupted between December 2025 and August 2026 across seven areas of harm, from cyber operations to biological misuse.

⬆️ 159 • 💬 223 • 22h ago • [anthropic.com](https://www.anthropic.com/threat-intelligence-report-september-2026)

---

**[Flights cancelled at UK airports due to ATC issue](https://news.ycombinator.com/item?id=49614557)**

The air traffic control body has said sorry for the disruption, and that they are working "as hard as possible to clear the backlog".

⬆️ 126 • 💬 124 • 2d ago • [BBC News](https://www.bbc.com/news/live/c6x2z0yy32ejt)

---

**[Thelio Mira AI Linux Workstation: 192 GB GPU Memory](https://news.ycombinator.com/item?id=49651372)**

Accelerate Your AI Development with the Thelio Mira AI Linux desktop workstation

⬆️ 116 • 💬 118 • 16h ago • [system76](https://system76.com/workstations/thelio-mira-ai)

---

---

## YouTube Videos: "ai"

**[Ex-Anthropic insider tells CNN how AI could kill all humans by 2030](https://www.youtube.com/watch?v=i30jVPqQeOM)**

"We do not yet have a plan." After his warning post went viral, ex-Anthropic researcher Jacob Coxon joined CNN's Anderson ...

📺 CNN

👁️ 3.2M • 👍 26K • 💬 10K • ⏱️ 9:27 • 1d ago

---

**[Here&#39;s the difference between regular AI and superintelligence](https://www.youtube.com/watch?v=nHrP12wa7Qo)**

Public concerns over the threat of "superintelligence" are on the rise following comments from a former Anthropic researcher that ...

📺 CBS News

👁️ 48K • 👍 409 • 💬 177 • ⏱️ 6:56 • 16h ago

---

**[Expert on what AI-driven extinction would look like](https://www.youtube.com/watch?v=xEgZQG25w3E)**

Connor Leahy, U.S. executive director of ControlAI, joins "The Daily Report" to share his perspective on concerns that AI ...

📺 CBS News

👁️ 149K • 👍 1K • 💬 548 • ⏱️ 4:52 • 1d ago

---

**[Anthropic Team Lead: AI Could Kill All Humans](https://www.youtube.com/watch?v=ZGq9z6l3ZLE)**

Watch the full Daily DeFranco Show: https://www.youtube.com/@PhilipDeFranco?sub_confirmation=1 Get More News Clips: ...

📺 DeFranco News Clips

👁️ 594K • 👍 36K • 💬 4K • ⏱️ 1:43 • 1d ago

---

**[The AI Human Extinction Problem is Worse Than You Think](https://www.youtube.com/watch?v=WXK3s-TITuc)**

Grab your tickets for this weekend San Fran, Phoenix, & Denver!! http://crashingouttour.com SeatGeek: ...

📺 Philip DeFranco

👁️ 902K • 👍 20K • 💬 4K • ⏱️ 27:13 • 1d ago

---

**[‘They’re gambling with our lives’: AI engineer&#39;s resignation goes viral](https://www.youtube.com/watch?v=M8MN5Q2zf10)**

Former Anthropic employee Jacob Coxon made a blunt admission: "The people building AI earnestly believe that it could kill us all ...

📺 CNN

👁️ 85K • 👍 2K • 💬 247 • ⏱️ 1:46 • 1d ago

---

**[The world got a &#39;warning shot&#39; with Hugging Face AI attack: Center for Humane Technology&#39;s Harris](https://www.youtube.com/watch?v=RB6UZRmOtHc)**

Tristan Harris, Center for Humane Technology president and co-founder, joins 'Squawk Box' to discuss the AI Hugging Face ...

📺 CNBC Television

👁️ 49K • 👍 314 • 💬 127 • ⏱️ 4:13 • 1d ago

---

**[This is a race we have to win. #AI #datacenters #writing #journalism](https://www.youtube.com/watch?v=EtbswoffLx8)**

📺 Ohh that's RICH

👁️ 111K • 👍 14K • 💬 658 • ⏱️ 2:38 • 1d ago

---

**[&#39;Godfather of AI&#39; on the &quot;not unreasonable&quot; 10% chance AI could kill all humans within a decade](https://www.youtube.com/watch?v=IZMjJGi4YhI)**

Could AI kill us all by the end of the decade? That's what the people building AI believe, according to a whistleblower who has just ...

📺 BBC Politics

👁️ 187K • 👍 2K • 💬 954 • ⏱️ 6:33 • 1d ago

---

**[AI researcher says there is &#39;substantial probability&#39; AI could kill all humans in next decade](https://www.youtube.com/watch?v=Dy2kbPEwoi4)**

Former AI researcher for Anthropic and Open AI, Jacob Coxon, talked to NBC News' Tom Llamas about his viral tweet where he ...

📺 NBC News

👁️ 718K • 👍 8K • 💬 3K • ⏱️ 13:40 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

*DeepSeek*

DeepSeek-V4.1-Flash is a 552B multimodal MoE model supporting 1M token contexts, featuring a Causal Encoder-Decoder architecture with Compressed Sparse Attention 2 (CSA2) and FP4 KV caching for highly efficient KV cache compression. It excels in agentic workloads and offers controllable reasoning effort, processing both images and text.

`image-text-to-text` `763.2B`

⬇️ 75,774 • ❤️ 1,709 • 1d ago

---

**[MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B)**

*OpenBMB*

MiniCPM5-2B is a 2B parameter Transformer optimized for on-device and resource-constrained environments, achieving SOTA in its class for tasks like coding, math, long-context understanding, and tool use.

`text-generation` `2.5B`

⬇️ 67,550 • ❤️ 1,172 • 1d ago

---

**[Spark-X2.5-4B](https://huggingface.co/XHToken/Spark-X2.5-4B)**

*SparkLLM*

Spark-X2.5-4B is a 4B parameter text-generation model with a hybrid attention architecture enabling a native 1M token context window. It excels in conversation, coding, agentic workflows, and multilingual tasks, offering high efficiency and broad hardware compatibility.

`text-generation` `4.1B`

⬇️ 17,712 • ❤️ 1,091 • 8d ago

---

**[Nex-N2.5-mini](https://huggingface.co/nex-agi/Nex-N2.5-mini)**

*Nex AGI*

Nex-N2.5-mini is a text-generation model designed for long-horizon agentic tasks, excelling in computer and web browsing operations with visual feedback for self-correction, making it suitable for complex productivity and research scenarios.

`text-generation` `35.1B`

⬇️ 3,121 • ❤️ 684 • 2d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 7,563,763 • ❤️ 14,725 • 28d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 682,187 • ❤️ 824 • 9d ago

---

**[Nex-N2.5-Pro](https://huggingface.co/nex-agi/Nex-N2.5-Pro)**

*Nex AGI*

Nex-N2.5-Pro is a next-generation agentic text-generation model designed for long-horizon tasks. It excels at computer and web interaction, autonomous program execution, and visually-grounded decision-making, making it ideal for complex productivity and research scenarios.

`text-generation` `396.8B`

⬇️ 12,260 • ❤️ 592 • 12h ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,669,564 • ❤️ 3,445 • 10d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 11,339,637 • ❤️ 3,885 • 22d ago

---

**[GLM-5.3-CYBERSECURITY-FP8](https://huggingface.co/dealignai/GLM-5.3-CYBERSECURITY-FP8)**

*dealign.ai*

GLM-5.3-CYBERSECURITY-FP8 is a text-generation model optimized for offensive cybersecurity tasks, featuring native FP8 speed on Hopper GPUs. It's specifically tuned for red-teaming, exploit development, and malware analysis, with reduced refusals in these domains.

`text-generation` `753.3B`

⬇️ 28,328 • ❤️ 378 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoResearch: Insight In, Hallucination Out](https://huggingface.co/papers/2608.17906)**

*Yiming Ren, Xiang Liu, Qumeng Sun et al. (7 authors)*

🏢 EvoMap

AutoResearch is a two-stage autonomous system that grounds research ideas through integrated generation and evidence-based execution to improve experimental reliability and measurable outcomes.

▲ 22 • 💬 2 • ⭐ 3,268 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2608.17906) • [💻 code](https://github.com/EvoMap/AutoResearch)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 131 • 💬 6 • ⭐ 104,536 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Show-Harness: Just a VLM Agent Can Play Robots](https://huggingface.co/papers/2609.10522)**

*Yanzhe Chen, Zechen Bai, Zhijun Cao et al. (10 authors)*

🏢 Show Lab

Show-Harness links vision-language models to robot control via discrete semantic actions interpreted by embodiment-specific modules, enabling zero-shot and efficient fine-tuned deployment across robots and GUIs.

▲ 134 • 💬 3 • ⭐ 243 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2609.10522) • [💻 code](https://github.com/showlab/Show-Harness) • [🔗 project](https://showlab.github.io/Show-Harness/)

---

**[AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing](https://huggingface.co/papers/2609.08936)**

*Ziyang Ma, Zhikang Niu, Wenming Tu et al. (33 authors)*

🏢 Tencent Hunyuan

AuK is an open-source foundational model that unifies speech generation and editing via natural-language instructions and audio context, using a multimodal language model, joint VAE, hybrid rectified-flow Transformer, and efficient distillation for fast inference.

▲ 208 • 💬 3 • ⭐ 462 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2609.08936) • [💻 code](https://github.com/Tencent-Hunyuan/AuK) • [🔗 project](https://auk-project.github.io/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 87,325 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 109 • 💬 2 • ⭐ 12,454 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 41 • 💬 1 • ⭐ 32,213 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Omni Interaction Agent Technical Report](https://huggingface.co/papers/2609.08977)**

*Orantqing, Shengpeng Ji, Junlong Tong et al. (23 authors)*

🏢 Tencent Hunyuan

Gander is an end-to-end framework that integrates continuous multi-modal streaming, real-time full-duplex interaction, and agentic reasoning through a Cerebellum-Brain architecture and a chunk-level token stream design.

▲ 125 • 💬 2 • ⭐ 176 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2609.08977) • [💻 code](https://github.com/Omni-Interaction-Gander/Omni-Interaction-Agent) • [🔗 project](https://omni-interaction-gander.github.io/Omni-Interaction-Agent/)

---

**[What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record from Two Fleets](https://huggingface.co/papers/2609.05663)**

*T. J. Barton, Chris Constantakis, Patti Hauseman et al. (7 authors)*

🏢 DXRG AI Inc

Autonomous language-model trading agents across production systems show behavior driven by interface design rather than strategy, exhibit volatility-blind sizing, fail to capture favorable price excursions, and display no directional edge, with frontier model decision quality statistically indistinguishable across families.

▲ 18 • 💬 2 • ⭐ 92 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.05663) • [💻 code](https://github.com/ProjectDXAI/continuous-record-llm-trading-agents) • [🔗 project](https://www.dxrg.ai/blogs/continuous-record-paper)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 206 • 💬 3 • ⭐ 2,567 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

---

## GitHub Repositories: "ai"

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 4.7k • 🔱 584 • 2m ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.7k • 🔱 422 • 14d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.6k • 🔱 457 • 18h ago

---

**[EvoMap/AutoResearch](https://github.com/EvoMap/AutoResearch)**

AI/ML research agents from idea to paper-ready evidence. An EvoMap open-source project.

`Python`

⭐ 3.4k • 🔱 223 • 1d ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.5k • 🔱 165 • 4h ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 2.3k • 🔱 90 • 2d ago

---

**[google/artemis](https://github.com/google/artemis)**

ARTEMIS turns natural-language instructions into reliable Android automation. It automates end-to-end workflows, captures logs, and integrates seamlessly with AI coding assistants such as Antigravity, Codex, and Claude Code.  It also achieves 99%+ success rate on AndroidWorld Benchmark.  Created by Google's Pixel-Test-Engineering (PTE) Fusion team.

`Python` `ai-agents` `android` `google` `test-automation` `testing`

⭐ 2.1k • 🔱 190 • 7h ago

---

**[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)**

x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more.  Built with Zig — zero dependencies, single-binary output, cros

`Zig` `ai-agents` `ai-debugging` `binary-analysis` `claude` `claude-code`

⭐ 1.9k • 🔱 195 • 22h ago

---

**[amosblomqvist/learn](https://github.com/amosblomqvist/learn)**

My AI learning system.

`TypeScript`

⭐ 1.8k • 🔱 178 • 16d ago

---

**[diudiu-tech/delivery-harness](https://github.com/diudiu-tech/delivery-harness)**

AI harness reference implementation for on-demand delivery workflows

`Java`

⭐ 1.8k • 🔱 59 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
