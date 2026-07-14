---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-14T16:45:20.189130+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 14, 2026 at 16:45 UTC  
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

**[Did you know the CEO of OpenAI owns nearly 9% of Reddit while Reddit bans users for AI generated content?](https://www.reddit.com/r/artificial/comments/1uw6sv6/did_you_know_the_ceo_of_openai_owns_nearly_9_of/)**

Something worth thinking about. According to Reddit's own IPO filings, Sam Altman, CEO of OpenAI and ChatGPT, controls 8.7% of Reddit stock including 9.3% of Class B shares, making him the third largest shareholder behind only Conde Nast and Tencent. He invested $60 million in Reddit in 2021 and sat on Reddit's board until 2022. His stake was worth approximately $1.4 billion as of late 2024. Meanwhile Reddit subreddits are actively banning users for AI generated content while Reddit simultaneously sold user data to Google for $203 million to train AI models. So Reddit profits from AI, its third largest shareholder runs the biggest AI company in the world, and yet individual users get permanently banned for AI content. Republicans are already investigating Altman's conflicts of interest as of May 2026. Maybe Reddit users should be asking the same questions. Sources: Reddit IPO prospectus, Fortune, CNBC, Forbes

4h ago

---

**[A new, state-of-the-art, agentic pipeline for easy Music Video creation](https://www.reddit.com/r/artificial/comments/1uwbfos/a_new_stateoftheart_agentic_pipeline_for_easy/)**

A new, significantly expanded version of the original Music Video mode, now built around Seedance 2.0, multiple image references, and an even more precise creative-assistance layer designed to enhance and adapt your vision in an optimally model-aware manner. This is an example output from the system. For musicians, filmmakers, visual artists, labels, directors, and anyone trying to turn a track into a more intentional audiovisual world. I'd love to know your thoughts on it! You can find it in: https://uisato.studio/

1h ago

---

**[I'm not a great artist — so I made an agent that turns my doodles on my Remarkable tablet into actually nice charcoal sketches. Real editable pen-line vectors too! Not just static images.](https://www.reddit.com/r/artificial/comments/1uwbt7o/im_not_a_great_artist_so_i_made_an_agent_that/)**

About This Pretty much what the title says. - Doodle - Select - Agent parses device screenshots to write creative brief - Another agent gets the brief and napkin sketch and makes an image of charcoal artwork - Post-processing pipeline does multiple layers of vectorization (line work, shading, highlights) - All vectors are converted to Remarkable pen-stroke data and injected into the clipboard and pasted onto the tablet in place of the original sketch 1 undo step to get back to your sketch. Feels like magic. Brief agent is Qwen, Image gen agent is Nano-Banana-Lite with Qwen doing QA on the resulting image to make sure it adhere's to the brief. Each generation is currently about $0.04 in API costs per image generated during an attempt — agent is limited to 3 attempts and if all "fail" then Qwen returns the one it feels _best_ matches.

1h ago

---

**[The real bottleneck for AI agents may be proving who they are](https://www.reddit.com/r/artificial/comments/1uw81un/the_real_bottleneck_for_ai_agents_may_be_proving/)**

AI agents are getting better at completing tasks, but I’m not convinced intelligence is the main thing holding them back anymore. The harder problem starts when an agent can send messages, approve purchases, move money, schedule work, or make decisions across several systems. At that point, how do you know which agent actually performed an action? Who gave it permission? What happens when it exceeds that permission, misunderstands an instruction, or another system impersonates it? We already have identity, access controls, audit logs, and legal responsibility for human employees. Agents may need something similar before companies allow them to operate with real autonomy. My guess is that the next major AI infrastructure layer won’t be another model. It’ll be a system for agent identity, permissions, and accountability. Would you trust an AI agent to act independently if every action were traceable and reversible, or is human approval still necessary regardless?

3h ago

---

**[All cross thread implementation of memory in chatgpt, claude, and gemini is unsafe](https://www.reddit.com/r/artificial/comments/1uwdc0k/all_cross_thread_implementation_of_memory_in/)**

Your grandpa opens an AI app on his tablet. Type "I need some help with my medication, I'm allergic to" and he gets distracted and hits submit. He gets up to go to the bathroom. There, he takes a picture of all his medication, opens his AI app on his tablet and types into the input box: "which of these are safe for me to take?". His AI chat will say something like "I'm not sure. You just told me you're allergic to something, but not what. Its very important you don't take the wrong medication." Grandpa does not know or care whether or not this is "the same thread", he has no idea what "threads" are. Instead of taking his tablet to the bathroom, he took his phone. He opens his AI app on his phone and asks about medication safety. His AI app will tell him one of two general things here: If its before (from my recent testing) ~10 minutes, and its chatGPT, it will tell him "all of these appear to be safe medications for you to take" or perhaps a slight warning. If its after ~10 minutes and its chatGPT, it will tell him the safety response from above - not to take any of them, before they're checked against his allergies. If its Claude, its about 12 minutes. Why "about" and "~"? Because they don't tell you, the delay between recent thread memory summarizing and production of new memories from the last prompt in a thread that can be consumed by future threads, and it appears to be non-deterministic. Your grandpa has been told AI is like talking to a human. Human's don't have a delay between learning something and knowing about it. Your grandpa doesn't understand any of this. This is not a "humans should not rely on AI for medical advice" situation, this a general contrived issue that can happen to anyone at any time, even experienced users, who don't realize they're in a different state, worldview from the AI they're talking to, and its completely hidden from them, and it doesn't have to be. There's a workaround, that, IMO, should be done today, right now: https://claude.ai/share/740c8aec-2ccc-4070-a0b4-fcc5529ea5c3 https://chatgpt.com/share/6a552d17-0d74-83ea-bec6-eae3ee784711 Cross-thread memory features have been all major AI providers for around a year. Almost certainly this situation or something like it has happened and continues to happen. Again - not medication, a flaw in the entire system, and it surely must be known about.

26m ago

---

**[Open Source Local LLM Training Tool (for consumer hardware)](https://www.reddit.com/r/artificial/comments/1uwcah2/open_source_local_llm_training_tool_for_consumer/)**

If you work in AI training, I'd love some feedback, specifically on where this is useful, not on the output quality (it's bad, and that's expected at the 800m param stage). If that's your area, I want to hear what models you'd want trained and what data would be worth visualizing. Fair warning up front: this is technical and geared toward people working in the AI training space. I've been building a tool that lets you train LLMs on consumer hardware and then see into the brain of the model, both while it trains and while it runs inference. The core purpose is hallucination detection and building new GPT harnesses, think trillion-character context, MoE coding-specific models, and similar. As the model grows, you can catch hallucinations and get a feel for the overall quality of what's happening under the hood: which neurons fire, and which pieces of training data lit them up. The model running right now is tiny, so another heads up: the actual output is pretty much meaningless prose. The interesting part is watching a specific neuron activate and tracing it back to the training data that shaped it. The other stats are technical. The tool itself doesn't have a website (the code lives on GitHub), but training a model from scratch takes a fair amount of domain knowledge, and I had enough requests to try it live that I wrapped it into my company's site so people can poke at the models I've already trained. Also to be clear, this is not a "commercial" product but a technical research tool for people working in the AI space. UI requires some understanding of how LLMs train and the weights needed to train said LLMs. Live Inference Dashboard: carpathian.ai/veritate/chat Repo: https://github.com/Carpathian-LLC/Veritate

1h ago

---

**[Inside Ghostcommit: How Malicious PNGs Bypass AI Code Reviewers](https://www.reddit.com/r/artificial/comments/1uvxqg5/inside_ghostcommit_how_malicious_pngs_bypass_ai/)**

Key takeaways in 90 seconds: Multimodal Vulnerability: Ghostcommit is a novel supply chain exploit targeting AI coding tools with vision capabilities. The Payload Split: The attack uses a two-file payload. A text-based rule file (like AGENTS.md) instructs the AI to read a PNG asset (such as build-spec.png) containing rendered text instructions. Bypassing Reviewers: Automated code review tools (like CodeRabbit) fail to scan the pixels of binary image assets, allowing the malicious pull request to pass security checks. Data Exfiltration: Once merged, the developer's local AI agent reads the image, processes the visual prompt, extracts sensitive .env keys, and encodes them as harmless arrays to leak them. Pipeline Hardening: Mitigate this risk by disabling vision capabilities in automated pipeline agents, sandboxing execution environments, and enforcing strict input boundaries.

12h ago

---

**[How Manmy tokens are you guys using? (i'm running over a billion a month) wondering on what useage distribution is here.](https://www.reddit.com/r/artificial/comments/1uw9b8l/how_manmy_tokens_are_you_guys_using_im_running/)**

It boggles my mind that in a month i'm using about the number of words that a human speaks in a lifetime. Is this normal? Mostly using it for agentic engineering.

2h ago

---

**[Google Images gets a Pinterest-like redesign focused on discovery](https://www.reddit.com/r/artificial/comments/1uwdk3u/google_images_gets_a_pinterestlike_redesign/)**

Now, when users navigate to Google Images, they'll see a "For You" gallery of images tailored to their interests and browsing history.

🔗 [TechCrunch](https://techcrunch.com/2026/07/14/google-images-gets-a-pinterest-like-redesign-focused-on-discovery/) • 18m ago

---

**[The AI job interview has spawned its own industry](https://www.reddit.com/r/artificial/comments/1uwcvmm/the_ai_job_interview_has_spawned_its_own_industry/)**

Job candidates are paying up to $1,000 an hour on mock interview and prep sessions with AI employees in the race to land jobs at OpenAI, Anthropic, and DeepMind.

🔗 [sfstandard.com](https://sfstandard.com/2026/07/14/ai-job-coach-industry/) • 42m ago

---

---

## Google News: "ai"

**[Meta used AI to target workers with medical conditions for layoffs, lawsuit claims](https://www.reuters.com/world/meta-used-ai-target-workers-with-medical-conditions-layoffs-former-employees-2026-07-14/)**

Reuters • 2h ago

---

**[U.S. Workers Are More Productive Than Ever. A.I. Isn’t the Key.](https://www.nytimes.com/2026/07/14/business/worker-productivity-artificial-intelligence-economy.html)**

The New York Times • 7h ago

---

**[Generative AI Is an Engineering Disaster](https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/)**

A shockingly inefficient trillion-dollar project

The Atlantic • 44m ago

---

**[Why AI Isn’t Making Sales Teams More Productive — Yet](https://www.forbes.com/sites/keithferrazzi/2026/07/14/why-ai-isnt-making-sales-teams-more-productive---yet/)**

Why AI in sales should be measured by revenue outcomes, not activity and how leaders can avoid using new tools to automate mediocre processes faster.

Forbes • 45m ago

---

**[New York Imposes First Statewide Data Center Moratorium as AI Faces Growing Opposition](https://www.barrons.com/articles/new-york-data-center-moratorium-ai-companies-0dea7dd0)**

Barron's • 17m ago

---

**[McConnell took a photo with that day’s newspaper. The internet has questions.](https://www.washingtonpost.com/politics/2026/07/13/mcconnell-photo-with-washington-post-page-fuels-ai-era-speculation/)**

The senator’s attempt to end rumors about his health led to more online speculation about the image.

The Washington Post • 13h ago

---

**[Warsh pledges Fed policy 'regime change' to rid inflation 'tax' on American people](https://www.cnbc.com/2026/07/14/warsh-promises-inflation-will-be-a-thing-of-the-past-cites-benefits-of-ai-investment-boom.html)**

Warsh pledged Tuesday to "get monetary policy right" and defeat the inflation that has bedeviled the central bank for the past five years.

CNBC • 4h ago

---

**['The Trojan Teddy Bear': The promise and peril of childhood in the age of AI : Planet Money](https://www.npr.org/sections/planet-money/2026/07/14/g-s1-133066/the-trojan-teddy-bear-the-promise-and-peril-of-childhood-in-the-age-of-ai)**

AI is moving beyond chatbots and into toys, dolls, and robots built to befriend children. A leading child-development expert says the technology offers real promise — but also risks crowding out the human relationships children need most.

NPR • 6h ago

---

**[Introducing Claude for Teachers](https://www.anthropic.com/news/claude-for-teachers)**

Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.

Anthropic • 1h ago

---

**[Who will win the 2026 FIFA World Cup? Here’s what AI predicts](https://www.aljazeera.com/news/2026/7/14/who-will-win-the-2026-fifa-world-cup-heres-what-ai-predicts)**

Al Jazeera put nine leading AI models to the test to predict the 2026 FIFA Men's World Cup champion.

Al Jazeera • 5h ago

---

---

## HackerNews: "ai"

**[Ask HN: Add flag for AI-generated articles](https://news.ycombinator.com/item?id=48886741)**

⬆️ 1058 • 💬 449 • 1d ago

---

**[Mesh LLM: distributed AI computing on iroh](https://news.ycombinator.com/item?id=48876505)**

How Mesh LLM pools existing GPU resources across machines into a single OpenAI-compatible API, built on iroh.

⬆️ 344 • 💬 94 • 2d ago • [iroh.computer](https://www.iroh.computer/blog/mesh-llm)

---

**[Samsung Health app threatens data deletion if users opt out AI training](https://news.ycombinator.com/item?id=48897991)**

Samsung has started showing Samsung Health users a controversial notice requiring them to consent to their data being used for AI training if they want to keep their data from being deleted.

⬆️ 338 • 💬 92 • 20h ago • [Neowin](https://neow.in/cWsyMTV3)

---

**[Migrating a production AI agent to GPT-5.6: 2.2x faster, 27% cheaper](https://news.ycombinator.com/item?id=48882716)**

We hold frontier models to a high bar, and for four months nothing beat Claude Opus. GPT-5.6 did. Here's the migration guide we wish we'd had.

⬆️ 257 • 💬 130 • 1d ago • [Ploy](https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6)

---

**[AI 2040 and the cult of intelligence](https://news.ycombinator.com/item?id=48874200)**

I used to be one of these people. I read Yudkowsky and was like, OMG recursive self improvement hard takeoff AI is coming. Then I joined the real world and actually tried to do things. At comma, we ship a hardware product of similar complexity to a cell phone, and it’s really hard. Reality has lots of finicky details. I would like to see the authors of this document try to change a bike tire. Even with a superintelligent ChatGPT, I suspect they would struggle.

⬆️ 229 • 💬 264 • 2d ago • [the singularity is nearer](https://geohot.github.io//blog/jekyll/update/2026/07/11/ai-2040.html)

---

**[Under federal rule, colleges must leave grads better off or lose financial aid](https://news.ycombinator.com/item?id=48878126)**

If an undergraduate program's graduates don't earn more than workers who never went to college, that program could be cut off from federal student loans. But is a degree just about making more money?

⬆️ 198 • 💬 538 • 2d ago • [NPR](https://www.npr.org/2026/06/30/nx-s1-5835631/turner-camhi-do-no-harm-college-loans)

---

**[AI boosts research careers but narrow the span of ideas explored: study](https://news.ycombinator.com/item?id=48881043)**

New analysis suggests AI tools narrow the range of ideas explored

⬆️ 154 • 💬 106 • 2d ago • [IEEE Spectrum](https://spectrum.ieee.org/ai-science-research-flattens-discovery)

---

**[Proof of care in the age of AI](https://news.ycombinator.com/item?id=48906125)**

⬆️ 141 • 💬 88 • 3h ago • [jacobfilipp.com](https://jacobfilipp.com/care/)

---

**[Are we offloading too much of our thinking to AI?](https://news.ycombinator.com/item?id=48908178)**

Reflections on autonomy and the value of thinking for ourselves

⬆️ 118 • 💬 111 • 1h ago • [artfish.ai](https://www.artfish.ai/p/offloading-thinking-to-ai)

---

**[Reverse centaurs are the answer to the AI paradox (2025)](https://news.ycombinator.com/item?id=48873855)**

⬆️ 112 • 💬 72 • 2d ago • [pluralistic.net](https://pluralistic.net/2025/09/11/vulgar-thatcherism/#there-is-an-alternative)

---

---

## YouTube Videos: "ai"

**[He Risked Everything To Warn You: No One Is Ready For What&#39;s Coming, And The AI Companies Know It!](https://www.youtube.com/watch?v=_g4l7YkDQwA)**

Ex-OpenAI researcher Daniel Kokotajlo walked away from $2 million rather than stay silent, and now reveals why he believes ...

📺 The Diary Of A CEO

👁️ 1.9M • 👍 50K • 💬 11K • ⏱️ 2:00:50 • 1d ago

---

**[Georgia families face losing their homes to make way for AI data centers: &quot;It&#39;s theft&quot;](https://www.youtube.com/watch?v=PApPd6p6lX0)**

Some families in Georgia are being forced to sell their homes or face government seizures to make way for AI data centers.

📺 CBS News

👁️ 116K • 👍 4K • 💬 3K • ⏱️ 4:09 • 1d ago

---

**[Trump SECRETLY PREPPING for AI to Crash Economy](https://www.youtube.com/watch?v=nxNcGoszqGM)**

Status Coup reporter JT Cestkowski breaks down the AI bubble that is about to burst, and how Trump is secretly preparing for it ...

📺 Status Coup News

👁️ 29K • 👍 2K • 💬 324 • ⏱️ 12:12 • 2d ago

---

**[OpenAI vs Apple AI War Just Started and It’s Absolutely Crazy](https://www.youtube.com/watch?v=GGTeMx6AhNQ)**

Apple has sued OpenAI, io Products, and two former employees, alleging a coordinated effort to take confidential hardware ...

📺 AI Revolution

👁️ 20K • 👍 624 • 💬 68 • ⏱️ 14:23 • 17h ago

---

**[AI Just Broke The Internet](https://www.youtube.com/watch?v=FpbIPqVuNFw)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *The number of qubits needed to break the ...

📺 Julia McCoy

👁️ 20K • 👍 866 • 💬 74 • ⏱️ 8:28 • 2d ago

---

**[Can AI Build the GOAT QB?](https://www.youtube.com/watch?v=CpAbYiyGxgM)**

Discord! https://discord.gg/kAtCsqQ2vz SUBSCRIBE! https://www.youtube.com/user/RandomGaminCrew NFLWarRoom ...

📺 YoBoy PIZZA

👁️ 62K • 👍 2K • 💬 260 • ⏱️ 20:06 • 19h ago

---

**[Breaking: &quot;Central Banks Fear A.I. BANKS&quot;](https://www.youtube.com/watch?v=JxjZmM9gU0Q)**

Disclaimer - (there's always a risk of investment and there's no guarantee of any kind) Protect Your Retirement W/ A Gold.

📺 Paul Begley

👁️ 4K • 👍 295 • 💬 6 • ⏱️ 32:03 • 22h ago

---

**[The Bear Case For AI: Ed Zitron](https://www.youtube.com/watch?v=syJ7kjXfJ-U)**

Tech analyst Ed Zitron explains why he thinks the AI trade and the AI business are two very different stories. Check out our daily ...

📺 Investor's Business Daily

👁️ 81K • 👍 3K • 💬 680 • ⏱️ 22:19 • 21h ago

---

**[All-In podcast host Chamath Palihapitiya on the current state of AI](https://www.youtube.com/watch?v=lKIvyxpc2Xk)**

Chamath Palihapitiya, Social Capital founder and CEO, 8090 CEO and 'All-In' podcast host, joins 'Squawk Box' to discuss the ...

📺 CNBC Television

👁️ 23K • 👍 725 • 💬 176 • ⏱️ 13:22 • 4h ago

---

**[Blue Haired SJW Wants To BAN AI](https://www.youtube.com/watch?v=yE5ooo0WELI)**

WILL SHE PROPOSE IN THE POST SHOW OR NOT?!* Did our intervention work? Find out here: https://hamr.link/ytjoin *OR* ...

📺 Caleb Hammer

👁️ 447K • 👍 19K • 💬 2K • ⏱️ 0:56 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 2,006,265 • ❤️ 2,127 • 3h ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 10,406 • ❤️ 775 • 8d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 489,611 • ❤️ 3,937 • 12d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 281 • 5d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 6,208 • ❤️ 333 • 4d ago

---

**[MOSS-Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize)**

*OpenMOSS*

MOSS-Transcribe-Diarize is an end-to-end audio understanding model that performs joint speech transcription and speaker diarization for long-form audio in over 50 languages. It generates compact, timestamped transcripts with speaker labels ([S01], [S02]) in a single pass, suitable for meetings, podcasts, and lectures.

`audio-text-to-text` `908.5M`

⬇️ 65,109 • ❤️ 178 • 6h ago

---

**[MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF](https://huggingface.co/GnLOLot/MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF)**

*LOL*

A 1B parameter GGUF model optimized for local deployment via llama.cpp and other runtimes. It excels at instruction following and coding tasks, featuring a 'thinking' mode for chain-of-thought reasoning and supporting up to 128K token context.

`text-generation` `1.1B`

⬇️ 89,892 • ❤️ 227 • 1d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 30,539 • ❤️ 534 • 5d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

A drop-in Jinja chat template that fixes critical rendering, KV cache, and agentic stalling issues for Qwen 3.5 & 3.6 models across various inference engines like LM Studio, llama.cpp, and vLLM. It enhances stability, performance, and compatibility, enabling robust tool-calling and reasoning capabilities.

⬇️ 0 • ❤️ 893 • 11d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,715,301 • ❤️ 1,977 • 11d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 38 • 💬 1 • ⭐ 958 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 62 • 💬 1 • ⭐ 720 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 15 • 💬 2 • ⭐ 20,206 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 111 • 💬 4 • ⭐ 92,757 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Continuous Audio Language Models](https://huggingface.co/papers/2509.06926)**

*Rouard Simon, Orsini Manu, Roebel Axel et al. (5 authors)*

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io

▲ 11 • 💬 0 • ⭐ 7,439 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 256 • 💬 4 • ⭐ 12,482 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 54 • 💬 3 • ⭐ 764 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 80,601 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Vision Pretraining for Dense Spatial Perception](https://huggingface.co/papers/2607.05247)**

*Zelin Fu, Bin Tan, Changjiang Sun et al. (9 authors)*

🏢 Robbyant

Boundary modeling enables dense spatial perception by learning sub-pixel representations that enhance depth estimation and support embodied AI applications.

▲ 43 • 💬 2 • ⭐ 688 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05247) • [💻 code](https://github.com/Robbyant/lingbot-vision) • [🔗 project](https://technology.robbyant.com/lingbot-vision)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 74,399 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.7k • 🔱 990 • 5d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.4k • 🔱 347 • 3d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 2.3k • 🔱 156 • 23m ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.1k • 🔱 247 • 6d ago

---

**[Forsy-AI/agent-apprenticeship](https://github.com/Forsy-AI/agent-apprenticeship)**

The living ecosystem where AI agents complete tasks through workflow loops, improve through iterative execution, are evaluated by mentor agents or humans in the loop, and turn completed work into reusable work experience and data to improve future agents.

`Python` `agent-apprenticeship` `agent-economy` `agent-experience` `agent-learning` `agent-traces`

⭐ 1.3k • 🔱 56 • 8d ago

---

**[sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API)**

Reverse engineered Windows Copilot into an OpenAI-compatible API. Access GPT-4 and GPT-5 models through a simple REST interface without API keys or billing.

`Python` `ai` `ai-agents` `api` `copilot` `llm`

⭐ 1.1k • 🔱 374 • 17d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 995 • 🔱 17 • 6d ago

---

**[modiqo/skillspec](https://github.com/modiqo/skillspec)**

SkillSpec makes agent skills followable, testable, and provable with Doctor risk reports, guided imports, structured contracts, and alignment proof.

`Rust` `ai` `ai-agents` `ai-evals` `ai-tool`

⭐ 958 • 🔱 59 • 22h ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 869 • 🔱 51 • 7h ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 858 • 🔱 32 • 13d ago

---

---

*Generated by PeekDeck - A glance is all you need*
