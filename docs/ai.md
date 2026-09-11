---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-11T11:43:15.461721+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 11, 2026 at 11:43 UTC  
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

10h ago

---

**[AI companies pursue the Boromir strategy to deal with the control problem. "It's dangerous. But let that be me. I know what to do with it."](https://www.reddit.com/r/artificial/comments/1wcwues/ai_companies_pursue_the_boromir_strategy_to_deal/)**

13h ago

---

**[Polish developer builds app that detects nearby Meta smart glasses](https://www.reddit.com/r/artificial/comments/1wdcik5/polish_developer_builds_app_that_detects_nearby/)**

Polish developers made an iPhone app that can detect nearby Meta smart glasses Apparently a group of Polish developers created an iPhone app that can detect nearby Meta smart glasses. It’s an interesting idea especially with the privacy concerns around smart glasses and cameras. Knowing that someone nearby might be wearing one could be useful. At the same time I am curious how accurate the app actually is and whether it can reliably detect the glasses in real world situations. Would you guys actually use something like this?

🔗 [tvpworld.com](https://tvpworld.com/95328093/polish-developers-iphone-app-detects-nearby-meta-smart-glasses) • 1h ago

---

**[Built an AI memory system that actually refuses to hallucinate](https://www.reddit.com/r/artificial/comments/1wd8fl0/built_an_ai_memory_system_that_actually_refuses/)**

Hey everyone, I have been working on a project for a while now. It is a custom RNS-AI architecture written in Python that runs locally on a single CPU core using a basic SQLite database. The main reason I built this is because standard LLMs drive me crazy with hallucinations and catastrophic forgetting. They just merge everything into a giant statistical blob of weights. If you ask a question and the model does not know the answer, it just guesses something plausible to please you. That does not work if you need the system for high risk environments like medical decision support, where total auditability and clear provenance chains are mandatory. My System works on a completely different rule: no black box, no unearned answers, no word filters. Instead of using dense vectors, it stores context hypotheses in a shadow layer while reading. It never erases errors or contradicted data because mistakes are valuable evidence. Before a hypothesis becomes an accepted fact, it has to survive multiple slow wave sleep cycles. This is an active consolidation phase where the system uses stochastic replay to test if a hypothesis remains stable over time. If there is no verified anchor in the database for your query, the system simply reports the gap instead of guessing. I am using terms like sleep and neuromodulation on purpose because the code actually mimics those exact functional mechanics at an algorithmic level. For instance, dynamic floating point parameters continuously tune excitation, inhibition, and sleep pressure to keep the system balanced without needing gradient descent. In recent production tests over a 664 MB Wikipedia corpus, it processed around 155k chunks and tracked over 1.4 million hypotheses on a single CPU thread without breaking down or corrupting its state. I am currently validating the hypothesis graduation pipeline and would love to hear your thoughts. How do you guys deal with parameter saturation or balancing strict line of sight provenance against fluid generalization in continuous learning loops?

5h ago

---

**[California enacts laws restricting chatbots and banning teens from ‘addictive’ social media](https://www.reddit.com/r/artificial/comments/1wd2r40/california_enacts_laws_restricting_chatbots_and/)**

🔗 [calmatters.org](https://calmatters.org/economy/technology/2026/09/california-enacts-laws-restricting-chatbots-protecting-kids-online/) • 9h ago

---

**[How Google AI "thinks"](https://www.reddit.com/r/artificial/comments/1wd70i1/how_google_ai_thinks/)**

Got this as text in a search on a particular kind of plant, " Pet Safety: Note that areca palms are considered [non-toxic or safe? wait, check snippet 0.6.1 says "Unsafe For Pets"]—actually let's look at 0.6.1: "Pet Toxicity Pet Friendly: Unsafe For Pets" is listed under one vendor attribute, but Dypsis lutescens is generally non-toxic to cats and dogs according to ASPCA, though 0.6.1 says unsafe for pets or specifies plastic/other. Wait, let's keep it simple and skip unverified pet info, or just focus on standard care. Let's see general care guide from The Spruce. [1, 2, 3]" Notice all the "hidden"notes the researchers or AI wrote to themselves or itself?

6h ago

---

**[Anthropic published a model of its own product's effect on the labor market. The extreme scenario has cognitive unemployment at 17.9% and labor's share of GDP falling from 60% to 45%.](https://www.reddit.com/r/artificial/comments/1wcjmg9/anthropic_published_a_model_of_its_own_products/)**

Three scenarios, explicitly not predictions, no probabilities attached. Modest is internet-sized at 1.6% GDP above the no-AI path by 2030. Substantial is 8.3%. Extreme is 32.4%. In the extreme case: cognitive unemployment 17.9%, overall 11.9%, which is past any postwar US peak. Cognitive wages 11.5% below trend on 21.5% fewer jobs. Labor's share of income falls from 60% to 45.2%. But wages in non-cognitive work go up 33.6%, so this isn't a story about everyone losing. It's a story about which half of the workforce you're in. The number that got me is in their Table 3. Total labor income ends up 0.5% above the no-AI path while GDP is a third larger. Capital income is up 81.4%. Essentially the entire gain goes to capital. Their own text says holding cognitive workers whole would take a transfer around 9% of GDP, about Social Security and Medicare combined, and that transfers at that scale in response to technology have no precedent. Worth knowing the extreme scenario assumes zero new human tasks get created. That assumption is doing real work in the result. Their caveats: no policy response, no business cycles, no financial disruption, no catastrophic risk, no robots.

🔗 [anthropic.com](https://www.anthropic.com/institute/econ-scenarios) • 21h ago

---

**[5 things I've noticed that still make AI video read as AI](https://www.reddit.com/r/artificial/comments/1wdbmwj/5_things_ive_noticed_that_still_make_ai_video/)**

I have been messing around with generated videos for a while, and did a bit of research trying to figure out why clips that look great on their own can still feel off when you put them in sequence. It's mostly not the obvious stuff people used to complain about. The physics of small things, Faces and bodies are getting pretty convincing, but smaller physical details still give away constantly. Hair, clothes, water, smoke, loose objects, etc. are things that our brains are wired to notice when they're not behaving correctly. A coat that looks like it has no weight to it is the easiest tell. Specifing material, weight and how it should move instead of just describing how it looks tends to somewhat do the trick. (Here's a CogVideoX tech paper on unnatural physics.) The camera has no operator, Real hand held footage has breathing, hesitation, little corrections and changes in speed. Generated hand held gets the general movement right but smooths out the small human imperfections. For example, a clip that's supposed to feel like a person running away from an SCP or something with a camera ends up feeling more like a gimbal or drone. Can't figure out how to fix at generation, so I just add actual handheld movement in post. Everything sits at roughly the same distance from the lens, This one kept showing up in my own generations. You can have technically different shots, but they all end up with roughly the same framing and subject size, the sequence starts feeling weird before I can explain why. Real coverage tends to jump between wides, mediums, close-ups, inserts, reaction shots etc. Six medium-ish shots in a row feels ... Wrong. Specifying the shot size everytime tends to alleviate it. (Link here for what I researched through) Light does not carry between shots, This one's brutal. Two shots can look completely believable on their own, but if one has the key light/sun coming from the left and the next cut shows it coming from somewhere completely different, it immediately seems artificial. There are actual papers researching this so I am apparently not the only person annoyed. Mostly seems like a workflow problem imo. Locking the time of day, general light direction and quality then keep repeating it seems like a good choice. Uniform shot length, Everything comes out around the same length that the tool gives you, so it's really easy to just use the whole clip everytime. Do that five or six times in a row and suddenly! You're watching a slideshow instead of a sequence. Shot duration and editing rhythm obviously aren't an AI specific problem, but there's plenty of film research on how much they affect pacing and perception. This one is completely fixable in post, but people really underestimate how much it matters. (Link!) These are just things I have started noticing the most. I'm curious as to see what others have found. What's your AI-Video tell that you just can't unsee?

1h ago

---

**[Why can't I generate some friticional characters on major AI services](https://www.reddit.com/r/artificial/comments/1wdbew4/why_cant_i_generate_some_friticional_characters/)**

So I've tried to generate Iron Man's depth of view image on an AI website, but it's unsuccessful. Any idea on what's happening.

2h ago

---

**[Genuine Question About Citizenship](https://www.reddit.com/r/artificial/comments/1wcdc90/genuine_question_about_citizenship/)**

1d ago

---

---

## Google News: "ai"

**[Detecting and countering misuse of AI: September 2026](https://www.anthropic.com/threat-intelligence-report-september-2026)**

Case studies from threat actors disrupted between December 2025 and August 2026 across seven areas of harm, from cyber operations to biological misuse.

Anthropic • 18h ago

---

**[Opinion | The A.I. Threat Is Real. We Need to Act Now.](https://www.nytimes.com/2026/09/11/opinion/ai-safety-threat-technology.html)**

The New York Times • 2h ago

---

**[Why fears of AI self-improvement are causing ‘existential’ concerns at Anthropic and OpenAI](https://www.cnbc.com/2026/09/11/anthropic-openai-ai-existential-concerns.html)**

AI researchers are warning that faster AI self-improvement could eventually make advanced systems harder for humans to control.

CNBC • 43m ago

---

**[AI debt is surging. A credit ratings agency has concerns](https://www.axios.com/2026/09/11/ai-debt-hyperscalers-sp)**

Axios • 28m ago

---

**[Remembering 9/11 and more AI researchers warn of safety risks: Morning Rundown](https://www.nbcnews.com/news/us-news/remembering-911-ai-researchers-warn-safety-risks-morning-rundown-rcna597175)**

Plus, why Trump’s $5,000 checks could face obstacles and diesel hits a record high.

NBC News • 41m ago

---

**[A.I. Could Possibly End Humanity. How Are Humans Supposed to Process That?](https://www.nytimes.com/2026/09/10/science/ai-humanity-risk.html)**

The New York Times • 13h ago

---

**[More Anthropic researchers warn of AI’s perils but Musk dismisses ‘psyop’](https://www.theguardian.com/technology/2026/sep/10/anthropic-researchers-warn-ai-musk)**

Insiders at the firm fear tech’s advancement could cause human extinction, while others are calling their declarations of concern a ‘setup’

theguardian.com • 8h ago

---

**[Trump dismisses AI extinction risks as more than a dozen OpenAI, Anthropic insiders call for a slowdown](https://www.cnbc.com/2026/09/11/trump-ai-extinction-risks.html)**

Trump said he isn't concerned AI could cause human extinction as researchers at leading AI companies warn about rapid advances and lawmakers propose safeguards.

CNBC • 44m ago

---

**[Anthropic says it blocked potential AI bioweapon misuse](https://abcnews.com/GMA/News/anthropic-blocked-potential-ai-bioweapon-misuse/story?id=136351654)**

The company said users may have used Claude for biological research that could pose risks.

abcnews.com • 8h ago

---

**[Anthropic Says It Blocked Possible Efforts to Build Biological Weapons](https://www.nytimes.com/2026/09/10/us/politics/anthropic-ai-biological-weapons.html)**

The New York Times • 18h ago

---

---

## HackerNews: "ai"

**[LibreOffice breaks download records after declaring it has no AI features](https://news.ycombinator.com/item?id=49610538)**

LibreOffice 26.8 became the app’s most popular update, with over 1 million downloads, after the foundation behind it declared that LibreOffice doesn’t come with generative AI features due to the…

⬆️ 711 • 💬 237 • 2d ago • [Manual do Usuário](https://manualdousuario.net/en/libreoffice-download-record-no-ai/)

---

**[Muse – Meta’s personal AI agent](https://news.ycombinator.com/item?id=49615537)**

Meet Muse, Meta's personal AI agent. Learn what it can do across everyday tasks, how it works, and how it helps you get more done.

⬆️ 654 • 💬 735 • 2d ago • [ai.meta.com](https://ai.meta.com/muse/)

---

**[AirPods 5](https://news.ycombinator.com/item?id=49630253)**

Apple today announced AirPods 5, delivering the industry’s best Active Noise Cancellation in an open-ear design and even better sound quality.

⬆️ 507 • 💬 449 • 1d ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/09/apple-introduces-airpods-5-with-best-in-class-open-ear-active-noise-cancellation/)

---

**[Tao: Open math problems being non-renewably mined by AI](https://news.ycombinator.com/item?id=49616968)**

I wrote recently about how the collection of good, fruitful open problems is now being mined in a non-renewable fashion, leading to the potential scenario of these problems becoming scarce.  This may seem unintuitive at first, since the set of possible problems one could ask is infinite.  Perhaps the following analogy can help: a country or region can suffer a critical shortage of drinking water while simultaneously being surrounded by a massive ocean.

One can easily generate any number of open problems in mathematics at will, such as working out the 10^10^10th digit of pi.  But the vast majority of such problems are not worth focusing attention on: they show no particular propensity to reveal any further insights or connections to other questions, or may either be too easy or too impossible relative to known techniques to learn anything from the exercise.  (1/4)

⬆️ 487 • 💬 418 • 2d ago • [Mathstodon](https://mathstodon.xyz/@tao/117237320796901560)

---

**[We Must Return to the Office to Use AI in Person](https://news.ycombinator.com/item?id=49610229)**

“I didn’t think a full, six-day-per-week, fourteen-hour-per-day, in-office schedule was necessary to discharge my duties clicking the ‘generate’ button, foll...

⬆️ 395 • 💬 68 • 2d ago • [McSweeney's Internet Tendency](https://www.mcsweeneys.net/articles/why-we-must-return-to-the-office-to-use-ai-in-person)

---

**[How An AI math breakthrough ignited a controversy](https://news.ycombinator.com/item?id=49624163)**

⬆️ 220 • 💬 230 • 2d ago • [science.org](https://www.science.org/content/article/how-ai-math-breakthrough-ignited-controversy)

---

**[Muse, the band, lost its social media handles to Muse, Meta's new AI agent](https://news.ycombinator.com/item?id=49636345)**

The exact circumstances surrounding the changes aren't clear, but Meta execs have accidentally tagged the band instead of their AI agent.

⬆️ 183 • 💬 8 • 1d ago • [Engadget](https://www.engadget.com/2254419/muse-the-band-lost-its-social-media-handles-to-muse-meta-s-new-ai-agent/)

---

**[Detecting and countering misuse of AI: September 2026](https://news.ycombinator.com/item?id=49647300)**

Case studies from threat actors disrupted between December 2025 and August 2026 across seven areas of harm, from cyber operations to biological misuse.

⬆️ 140 • 💬 207 • 18h ago • [anthropic.com](https://www.anthropic.com/threat-intelligence-report-september-2026)

---

**[Flights cancelled at UK airports due to ATC issue](https://news.ycombinator.com/item?id=49614557)**

The air traffic control body has said sorry for the disruption, and that they are working "as hard as possible to clear the backlog".

⬆️ 126 • 💬 124 • 2d ago • [BBC News](https://www.bbc.com/news/live/c6x2z0yy32ejt)

---

**[Thelio Mira AI Linux Workstation: 192 GB GPU Memory](https://news.ycombinator.com/item?id=49651372)**

Accelerate Your AI Development with the Thelio Mira AI Linux desktop workstation

⬆️ 111 • 💬 102 • 12h ago • [system76](https://system76.com/workstations/thelio-mira-ai)

---

---

## YouTube Videos: "ai"

**[Ex-Anthropic insider tells CNN how AI could kill all humans by 2030](https://www.youtube.com/watch?v=i30jVPqQeOM)**

"We do not yet have a plan." After his warning post went viral, ex-Anthropic researcher Jacob Coxon joined CNN's Anderson ...

📺 CNN

👁️ 3.0M • 👍 24K • 💬 9K • ⏱️ 9:27 • 1d ago

---

**[A.I. Expert Warns Humanity Is Halfway to Full Takeover | TMZ](https://www.youtube.com/watch?v=vmJ_es6UO4I)**

The nightmare scenario for A.I. isn't just killer robots ... it could be nukes too. A.I. ethicist Tristan Harris says the warning signs are ...

📺 TMZ Clips

👁️ 63K • 👍 959 • 💬 506 • ⏱️ 15:29 • 1d ago

---

**[The AI Human Extinction Problem is Worse Than You Think](https://www.youtube.com/watch?v=WXK3s-TITuc)**

Grab your tickets for this weekend San Fran, Phoenix, & Denver!! http://crashingouttour.com SeatGeek: ...

📺 Philip DeFranco

👁️ 890K • 👍 20K • 💬 4K • ⏱️ 27:13 • 1d ago

---

**[AI researcher says there is &#39;substantial probability&#39; AI could kill all humans in next decade](https://www.youtube.com/watch?v=Dy2kbPEwoi4)**

Former AI researcher for Anthropic and Open AI, Jacob Coxon, talked to NBC News' Tom Llamas about his viral tweet where he ...

📺 NBC News

👁️ 689K • 👍 7K • 💬 3K • ⏱️ 13:40 • 1d ago

---

**[Anthropic Team Lead: AI Could Kill All Humans](https://www.youtube.com/watch?v=ZGq9z6l3ZLE)**

Watch the full Daily DeFranco Show: https://www.youtube.com/@PhilipDeFranco?sub_confirmation=1 Get More News Clips: ...

📺 DeFranco News Clips

👁️ 589K • 👍 36K • 💬 3K • ⏱️ 1:43 • 1d ago

---

**[A Human Just Beat the World’s Strongest Go AI #ai #google #programming](https://www.youtube.com/watch?v=iySQNsNGD7g)**

📺 Better Stack

👁️ 28K • 👍 858 • 💬 40 • ⏱️ 1:48 • 15h ago

---

**[&#39;Godfather of AI&#39; on the &quot;not unreasonable&quot; 10% chance AI could kill all humans within a decade](https://www.youtube.com/watch?v=IZMjJGi4YhI)**

Could AI kill us all by the end of the decade? That's what the people building AI believe, according to a whistleblower who has just ...

📺 BBC Politics

👁️ 167K • 👍 2K • 💬 872 • ⏱️ 6:33 • 1d ago

---

**[‘We don’t have months’: Bernie Sanders sounds alarm on AI&#39;s &#39;extinction&#39; threat](https://www.youtube.com/watch?v=PWkMUmEZbq4)**

What we have got to do now is light a match under the backsides of members of Congress and say, we don't have months.

📺 MS NOW

👁️ 644K • 👍 9K • 💬 3K • ⏱️ 7:46 • 1d ago

---

**[A.I.&#39;s threat to humanity given new consideration in Congress](https://www.youtube.com/watch?v=hlnZQ3utAiY)**

Following an alarming warning raised by an Anthropic employee resigning in protest over the threat of artificial intelligence to the ...

📺 MS NOW

👁️ 62K • 👍 1K • 💬 355 • ⏱️ 8:39 • 1d ago

---

**[AI World In CHAOS After Whistleblower Sounds Alarm on Human Extinction](https://www.youtube.com/watch?v=3G7hrmfrguY)**

Krystal and Saagar discuss AI whistleblowers sounding off on the dangers of AI development. Sign Up For 30 Day Free BP Trial: ...

📺 Breaking Points

👁️ 363K • 👍 7K • 💬 2K • ⏱️ 31:00 • 19h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

*DeepSeek*

DeepSeek-V4.1-Flash is a 552B multimodal MoE model supporting 1M token contexts, featuring a Causal Encoder-Decoder architecture with Compressed Sparse Attention 2 (CSA2) and FP4 KV caching for highly efficient KV cache compression. It excels in agentic workloads and offers controllable reasoning effort, processing both images and text.

`image-text-to-text` `763.2B`

⬇️ 75,774 • ❤️ 1,635 • 1d ago

---

**[MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B)**

*OpenBMB*

MiniCPM5-2B is a 2B parameter Transformer optimized for on-device and resource-constrained environments, achieving SOTA in its class for tasks like coding, math, long-context understanding, and tool use.

`text-generation` `2.5B`

⬇️ 67,550 • ❤️ 1,154 • 1d ago

---

**[Spark-X2.5-4B](https://huggingface.co/XHToken/Spark-X2.5-4B)**

*SparkLLM*

Spark-X2.5-4B is a 4B parameter text-generation model with a hybrid attention architecture enabling a native 1M token context window. It excels in conversation, coding, agentic workflows, and multilingual tasks, offering high efficiency and broad hardware compatibility.

`text-generation` `4.1B`

⬇️ 17,712 • ❤️ 1,080 • 8d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 7,563,763 • ❤️ 14,695 • 27d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 682,187 • ❤️ 814 • 9d ago

---

**[Nex-N2.5-mini](https://huggingface.co/nex-agi/Nex-N2.5-mini)**

*Nex AGI*

Nex-N2.5-mini is a text-generation model designed for long-horizon agentic tasks, excelling in computer and web browsing operations with visual feedback for self-correction, making it suitable for complex productivity and research scenarios.

`text-generation` `35.1B`

⬇️ 3,121 • ❤️ 672 • 2d ago

---

**[Nex-N2.5-Pro](https://huggingface.co/nex-agi/Nex-N2.5-Pro)**

*Nex AGI*

Nex-N2.5-Pro is a next-generation agentic text-generation model designed for long-horizon tasks. It excels at computer and web interaction, autonomous program execution, and visually-grounded decision-making, making it ideal for complex productivity and research scenarios.

`text-generation` `396.8B`

⬇️ 12,260 • ❤️ 591 • 8h ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,669,564 • ❤️ 3,429 • 10d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 11,339,637 • ❤️ 3,870 • 21d ago

---

**[GLM-5.3-CYBERSECURITY-FP8](https://huggingface.co/dealignai/GLM-5.3-CYBERSECURITY-FP8)**

*dealign.ai*

GLM-5.3-CYBERSECURITY-FP8 is a text-generation model optimized for offensive cybersecurity tasks, featuring native FP8 speed on Hopper GPUs. It's specifically tuned for red-teaming, exploit development, and malware analysis, with reduced refusals in these domains.

`text-generation` `753.3B`

⬇️ 28,328 • ❤️ 376 • 2d ago

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

▲ 134 • 💬 3 • ⭐ 163 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2609.10522) • [💻 code](https://github.com/showlab/Show-Harness) • [🔗 project](https://showlab.github.io/Show-Harness/)

---

**[AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing](https://huggingface.co/papers/2609.08936)**

*Ziyang Ma, Zhikang Niu, Wenming Tu et al. (33 authors)*

🏢 Tencent Hunyuan

AuK is an open-source foundational model that unifies speech generation and editing via natural-language instructions and audio context, using a multimodal language model, joint VAE, hybrid rectified-flow Transformer, and efficient distillation for fast inference.

▲ 206 • 💬 3 • ⭐ 395 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2609.08936) • [💻 code](https://github.com/Tencent-Hunyuan/AuK) • [🔗 project](https://auk-project.github.io/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 87,325 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Omni Interaction Agent Technical Report](https://huggingface.co/papers/2609.08977)**

*Orantqing, Shengpeng Ji, Junlong Tong et al. (23 authors)*

🏢 Tencent Hunyuan

Gander is an end-to-end framework that integrates continuous multi-modal streaming, real-time full-duplex interaction, and agentic reasoning through a Cerebellum-Brain architecture and a chunk-level token stream design.

▲ 125 • 💬 2 • ⭐ 163 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2609.08977) • [💻 code](https://github.com/Omni-Interaction-Gander/Omni-Interaction-Agent) • [🔗 project](https://omni-interaction-gander.github.io/Omni-Interaction-Agent/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 41 • 💬 1 • ⭐ 32,196 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 109 • 💬 2 • ⭐ 12,405 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record from Two Fleets](https://huggingface.co/papers/2609.05663)**

*T. J. Barton, Chris Constantakis, Patti Hauseman et al. (7 authors)*

🏢 DXRG AI Inc

Autonomous language-model trading agents across production systems show behavior driven by interface design rather than strategy, exhibit volatility-blind sizing, fail to capture favorable price excursions, and display no directional edge, with frontier model decision quality statistically indistinguishable across families.

▲ 18 • 💬 2 • ⭐ 92 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.05663) • [💻 code](https://github.com/ProjectDXAI/continuous-record-llm-trading-agents) • [🔗 project](https://www.dxrg.ai/blogs/continuous-record-paper)

---

**[BAT: Behavior-Aware Human-Like Trajectory Prediction for Autonomous
  Driving](https://huggingface.co/papers/2312.06371)**

*Haicheng Liao, Zhenning Li, Huanming Shen et al. (8 authors)*

A behavior-aware model predicts vehicle trajectories using insights from traffic psychology and human behavior, outperforming state-of-the-art benchmarks with reduced data.

▲ 0 • 💬 0 • ⭐ 1,110 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2312.06371) • [💻 code](https://github.com/petrichor625/batraj-behavior-aware-model)

---

---

## GitHub Repositories: "ai"

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 4.7k • 🔱 583 • 5h ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.7k • 🔱 422 • 14d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.6k • 🔱 456 • 14h ago

---

**[EvoMap/AutoResearch](https://github.com/EvoMap/AutoResearch)**

AI/ML research agents from idea to paper-ready evidence. An EvoMap open-source project.

`Python`

⭐ 3.4k • 🔱 223 • 1d ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.5k • 🔱 163 • 40m ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 2.3k • 🔱 89 • 2d ago

---

**[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)**

x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more.  Built with Zig — zero dependencies, single-binary output, cros

`Zig` `ai-agents` `ai-debugging` `binary-analysis` `claude` `claude-code`

⭐ 1.9k • 🔱 194 • 17h ago

---

**[google/artemis](https://github.com/google/artemis)**

ARTEMIS turns natural-language instructions into reliable Android automation. It automates end-to-end workflows, captures logs, and integrates seamlessly with AI coding assistants such as Antigravity, Codex, and Claude Code.  It also achieves 99%+ success rate on AndroidWorld Benchmark.  Created by Google's Pixel-Test-Engineering (PTE) Fusion team.

`Python` `ai-agents` `android` `google` `test-automation` `testing`

⭐ 1.8k • 🔱 174 • 2h ago

---

**[diudiu-tech/delivery-harness](https://github.com/diudiu-tech/delivery-harness)**

AI harness reference implementation for on-demand delivery workflows

`Java`

⭐ 1.8k • 🔱 59 • 1d ago

---

**[amosblomqvist/learn](https://github.com/amosblomqvist/learn)**

My AI learning system.

`TypeScript`

⭐ 1.8k • 🔱 177 • 16d ago

---

---

*Generated by PeekDeck - A glance is all you need*
