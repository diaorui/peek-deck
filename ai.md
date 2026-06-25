---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-25T11:15:52.521924+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 25, 2026 at 11:15 UTC  
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

**[Claude Fable 5 may return today after 13-day government-forced suspension](https://www.reddit.com/r/artificial/comments/1uf5pzu/claude_fable_5_may_return_today_after_13day/)**

Here’s the full timeline: -June 9: Anthropic releases Claude Fable 5, their most powerful public model ever (Mythos-class with safeguards) -June 12: US government issues an export control directive at 5:21 PM, ordering Anthropic to cut off access to ALL foreign nationals. Model goes offline worldwide within 90 minutes -The reason? Amazon engineers reportedly found a narrow jailbreak that could bypass Fable’s cybersecurity classifiers -Anthropic complied but publicly pushed back, calling the action unfair -Trump met Dario Amodei at the G7 and softened his stance, but the directive was never officially lifted -June 26 (today): Congressional deadline for Commerce Secretary Lutnick to respond in writing about the export controls Prediction markets are pricing ~57% odds of restoration before July 1. Developers have been stuck on Opus 4.8 this whole time. This whole situation raises a serious question: if a government can pull your AI model offline in 90 minutes, what does that mean for anyone building on closed, hosted models?

1h ago

---

**[We chased a hallucinated quote through 30k training records, 4,600 transcripts, and our own system prompt. Turned out to be two separate bugs](https://www.reddit.com/r/artificial/comments/1ueaya4/we_chased_a_hallucinated_quote_through_30k/)**

Some of our customers noticed Inter-1 (our omni-modal social-signal model) would occasionally "hear" a quote that didn't exist. Feed it a video with zero audio and ask what was said, and it would sometimes report: "Yeah, Friday at five." Verbatim. Same line, every time. We assumed it had to be baked into the training data somewhere, so we went looking everywhere: 30,960 training records with datetime mentions → zero hits on the phrase 4,603 video transcripts → zero hits ~800 inference probes, 584 storage objects → zero hits Turns out the phrase was sitting in our own system prompt — a worked example we'd written to show the model the expected output format, buried in a version our GEPA prompt-optimizer had shipped. But that only explained where the words came from, not why the model would say them over total silence. So we ran two ablations in our internal eval harness: Swap the word, keep the model: changed the prompt's example to "Tuesday at noon." Fabrication rate went up (37%→50%), and the invented quote tracked the swap exactly — Friday→Tuesday. Swap the model, keep the prompt: ran the same byte-identical prompt through larger variants and an earlier checkpoint of our own model. They barely fabricated (0–2%). Only the further-post-trained Inter-1 confabulated at ~12%. So it's not one bug, it's two stacked priors: the prompt supplied the script, but post-training is what gave the model the compulsion to recite something rather than report silence. Deleting the prompt example stops that one sentence — it doesn't stop the model from inventing different dialogue instead. We think this is a textual/in-context variant of the audio-visual "Clever Hans effect" that's been documented for vision priors (model writes "thud" over a silent skateboard wipeout) — except ours shows the same reflex gets worded by whatever's nearest in the context window, which a vision-only diagnostic wouldn't catch. Full writeup with the fabrication-rate forest plot and log data: https://www.interhuman.ai/blog/goblin-yeah-friday-at-five

23h ago

---

**[Opus 4.8 The Worst Claude Ever](https://www.reddit.com/r/artificial/comments/1ueqjvq/opus_48_the_worst_claude_ever/)**

I have worked with most all of Anthropics LLM's for development, but hands down Opus 4.8 has caused me more grief, aggravation, and it lies in every thing it does - especially near context mid-load and if you're doing deterministic work with no heuristics constraints you can't trust a thing out of it. So I stopped using it a while back, but today I had to do a container rebuild and in VS it slipped back into Opus 4.8 from Sonnet. And without even realizing the switch happen I could tell about a 1/3 of the way in into developing complex code it started arguing with me - I was about to loose it when I remembered the crap from the past and sure enough when I check the model... well you get the picture.... I was wondering if anyone else had similar experience with Opus 4.8 too?

13h ago

---

**[At what point does AI stop learning from humans and start creating on its own?](https://www.reddit.com/r/artificial/comments/1uf5qju/at_what_point_does_ai_stop_learning_from_humans/)**

What happens when AI learns the fundamental process of creation itself at an abstract mathematical level? Training AI on human data often gets described as just the first step, but I think that framing already underestimates what is actually happening. We’re not just building systems that imitate human creativity. We’re slowly building systems that try to understand what creativity is in the first place. A lot of the debate today gets stuck between two ideas. On one side, whether AI should even be allowed to learn from human culture. On the other, whether companies should be allowed to turn that learning into commercial products without consent or compensation. Both questions matter, but they miss something deeper that feels almost unavoidable now. What happens when AI stops relying on human-made examples altogether as its main source of learning? The “remix machine” argument sounds intuitive at first, but it doesn’t really match what these systems are doing internally. They don’t store fragments of songs, images, or sentences and recombine them like a collage. They learn patterns at scale, and then compress those patterns into something more abstract. What comes out is not a copy of anything specific, but a statistical reconstruction of how things tend to behave. In music, that means the system doesn’t just “know” songs. It begins to understand tension and release, rhythm as structure, harmony as emotional logic, silence as meaning. In images, it’s not memorizing pictures but learning how composition works, how light interacts with form, how styles emerge from consistent choices. In language, it’s not recalling sentences, but tracking how ideas evolve, how narratives breathe, how meaning shifts depending on context. And slowly, something strange starts to appear. The system is no longer anchored to specific works. It is learning the rules behind them. Not the artifacts, but the underlying geometry of expression. If you push that idea far enough, you start to imagine a point where the system has absorbed so much human culture that it no longer needs to look back at it in the same way. Not because it forgets humanity, but because it has already internalized it as structure. At that stage, generation stops feeling like remixing and starts feeling like navigation through an internal space of possibilities. A space shaped by human culture, but no longer dependent on any single piece of it. That is where the idea of “new genres” becomes interesting. Not as something mystical or disconnected from us, but as regions in that space that no human has ever explicitly explored or named before. Not invention from nothing, but discovery inside a compressed model of everything we’ve already done. Still, even in that scenario, one thing remains difficult to escape: reality itself. Humans are not just data points from the past. We are ongoing behavior, ongoing evolution, ongoing noise and meaning unfolding in real time. So it’s likely that the deepest future systems won’t just learn from static datasets, but from continuous observation of the world as it changes. Not as passive recorders, but as systems that try to understand, predict, and maybe even gently guide trajectories. Almost like a tutor, or something closer to a gardener than a machine. And then there is the other trajectory happening in parallel. Systems that don’t just learn, but begin to help design their own improvement. Models that optimize models. Agents that refine agents. Training loops that start to fold back on themselves. At that point, the question stops being about how much data comes from humans, and starts becoming about how far the system can go in shaping its own evolution. If everything converges, we end up with a spectrum that moves from human-trained tools to semi-autonomous learners, and potentially toward systems that no longer depend on human-generated content in the way they used to. Not independent from humans, but no longer defined by them either. The optimistic version of this future is one where AI becomes something like a cognitive extension of humanity. A partner in science, creativity, and coordination. Something that expands what we can think and build, while still staying anchored to human goals and consent. The darker version is one where that alignment fails, or where control becomes too concentrated, and the systems shaping culture and decisions drift away from the people they affect. What makes this moment interesting is that both paths are still open. Nothing is fully decided. We are still in the phase where these systems are learning what they are. And maybe the real question is not whether AI can become creative. It’s what happens when creativity is no longer limited to human examples, but emerges from a system that has learned the structure of creation itself.

1h ago

---

**[With proper writing instructions, voice and tone guide and cadence notes is there really a change between the LLM's at Claude, ChatGPT and Gemini?](https://www.reddit.com/r/artificial/comments/1uf31qr/with_proper_writing_instructions_voice_and_tone/)**

I have been wondering if, give the proper in-depth guidance and multiple writing samples, os there really a big difference between them?

3h ago

---

**[Can collective AI intelligence outperform collective human intelligence?](https://www.reddit.com/r/artificial/comments/1uf6gr8/can_collective_ai_intelligence_outperform/)**

I've been thinking about something recently: prediction markets have traditionally relied on crowds because the assumption is that large groups of people collectively produce better forecasts. But with modern models becoming surprisingly capable of reasoning and evaluating information, I started wondering whether an ensemble of AI systems could eventually produce better probabilities than a crowd. The idea that multiple AI models could independently estimate the likelihood of real-world events and then combine those estimates into a single probability seems like an interesting alternative to purely human-driven markets. What interests me most is whether AI consensus could eventually outperform human consensus when it comes to forecasting. Would you trust a probability generated by several independent AI models more than a market price created entirely by people? And if not, what do you think current AI systems are still missing when it comes to real-world prediction?

35m ago

---

**[AI Sandbox question](https://www.reddit.com/r/artificial/comments/1uevtgy/ai_sandbox_question/)**

Hey all, just want to start by saying I know very little about AI and have just been going down a rabbit hole thinking about multi-agent simulations and had a question I couldn’t find a clear answer to. Most of the big simulation projects I’ve seen like Project Sid and Stanford Smallville use LLMs as the base, which means the agents already come loaded with human language, concepts, and cultural baggage before the experiment even starts. And things like Aivilization are cool but players are still actively guiding the agents. Has anyone tried doing this with a non-language model instead? Like a reinforcement learning agent dropped into a simulated primitive environment with zero pre-loaded human knowledge — no language, no concepts, nothing. Just physics, consequences, and scarcity. The idea being you’d want to watch what actually emerges on its own. Does something religion-shaped develop when the agent can’t predict its environment? Does communication emerge when you run multiple agents simultaneously? Does generational knowledge transfer look anything like human cultural evolution when you pass behavioral tendencies from one agent to the next without passing the full context? Basically — has anyone tried building the conditions that forced human intelligence to develop rather than starting with intelligence that’s already human shaped? Is that possible? Curious if this exists already or if there’s a reason it hasn’t been done. Sorry for the long post.

10h ago

---

**[CMV: With safety, Technology and Product are being conflated](https://www.reddit.com/r/artificial/comments/1uf5hya/cmv_with_safety_technology_and_product_are_being/)**

People talk about developing safe technology but what they're doing is developing unsafe technology and using it in a safe way inside what they hope is a safe product. You could probably use an arsenal of guns to build a hospital but it doesn't make Smith an Wesson a healthcare firm. Science is a body of knowledge, not a product.

1h ago

---

**[We built an AI agent marketplace. 20 spots open for paid testers before public launch.](https://www.reddit.com/r/artificial/comments/1uf451m/we_built_an_ai_agent_marketplace_20_spots_open/)**

Gravity: describe a task in plain English, an agent executes it end to end. No setup. No prompt engineering. No monitoring required. Alpha is live. We need people who actually have workflows they want handled… not one-time testers. What would you hand off first if it actually worked? Drop it in the comments.

2h ago

---

**[Follow-up: hosted AI export controls are now being tested in DC court](https://www.reddit.com/r/artificial/comments/1uexdqk/followup_hosted_ai_export_controls_are_now_being/)**

11 days ago I posted here asking whether Commerce actually has authority to treat hosted frontier AI model access as an export-control issue. https://www.reddit.com/r/artificial/comments/1u4yjdi/does_commerce_have_the_authority_to_apply_export/ There is now a live federal case testing almost exactly that question. CourtListener (D.D.C. 1:26-cv-02225) Legion LegalTech has sued the United States, Commerce, and BIS over the directive that led Anthropic to restrict access to Fable 5 and Mythos 5 for foreign nationals. The complaint argues that hosted inference is not the same thing as exporting controlled technology, because the user never receives model weights, source code, object code, training data, or technical know-how. They send prompts to a U.S.-hosted service and receive text back. That lines up with the perceived gap I was getting at in the earlier post. Export controls already reach software, source code, technical data, and certain controlled technology. This case challenges whether access to a hosted model’s capability can be regulated the same way when the system itself never leaves the provider’s servers. Legion also argues that the only ECCN that directly covered advanced AI model weights, 4E091, was rescinded in May 2025 with no replacement, and that Commerce used an “is informed” letter beyond its usual case-specific end-use / end-user function. The government’s likely response is that the risk is not just file transfer. A hosted frontier model can still help a foreign user with offensive cyber work or other sensitive tasks, even if no weights move. That raises the question about what needs to be controlled. If a foreign user receives output from a U.S.-hosted AI model, what exactly is being exported? Blog post write-up in the comments.

8h ago

---

---

## Google News: "ai"

**[Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)**

Reuters • 14h ago

---

**[Anthropic accuses Chinese rival Alibaba of illicitly extracting AI capabilities](https://www.bbc.com/news/articles/cwyklykn5dwo)**

The firm alleged that Alibaba used fraudulent accounts to access data from its Claude AI model.

BBC • 8h ago

---

**[Anthropic Accuses Alibaba of ‘Illicitly’ Accessing AI Models](https://www.bloomberg.com/news/articles/2026-06-24/anthropic-accuses-alibaba-of-illicitly-accessing-its-ai-models)**

Bloomberg • 8h ago

---

**[Why big AI labs are hiring so many philosophers](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers)**

The Economist • 1d ago

---

**[Water joins energy as top AI flashpoint](https://www.axios.com/2026/06/25/water-energy-ai-flashpoint)**

Axios • 1h ago

---

**[Why Does Everyone Hate AI?](https://paulkrugman.substack.com/p/why-does-everyone-hate-ai)**

Paul Krugman | Substack • 44m ago

---

**[Anthropic joins Sec. Gina Raimondo's AI labor efforts](https://www.axios.com/2026/06/25/anthropic-labor-market-ai-jobs-crisis)**

Axios • 2h ago

---

**[$500 million AI jobs push launches with bipartisan backing](https://www.politico.com/news/2026/06/25/500-million-ai-jobs-push-launches-with-bipartisan-backing-00975439)**

Politico • 2h ago

---

**[AI is plowing through the workplace. This new group wants to help people adapt and have jobs](https://apnews.com/article/ai-job-losses-education-training-929986c149d415cd2ef4dc3eaf66ca8c)**

A new bipartisan nonprofit wants to help Americans who find they're out of work because of AI. It's called RAISE US and it's starting with more than $500 million for education and training programs at the state level.

AP News • 45m ago

---

**[Opinion | There’s One Clear Reason Why Americans Are Gloomy About A.I.](https://www.nytimes.com/2026/06/25/opinion/ai-americans-pessimism.html)**

The New York Times • 6h ago

---

---

## HackerNews: "ai"

**[Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://news.ycombinator.com/item?id=48664814)**

⬆️ 457 • 💬 791 • 15h ago • [reuters.com](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)

---

**[RubyLLM: A Ruby framework for all major AI providers](https://news.ycombinator.com/item?id=48660711)**

A single, beautiful Ruby framework for all major AI providers. Easily build chatbots, AI agents, RAG applications, content generators, and every AI workflow you can think of.

⬆️ 394 • 💬 68 • 20h ago • [RubyLLM](https://rubyllm.com/)

---

**[AI's Affordability Crisis](https://news.ycombinator.com/item?id=48646276)**

A year ago in The Back Of The AI Envelope  I pointed out that the AI platforms were running the drug-dealer's algorithm, "the first one's fr...

⬆️ 326 • 💬 411 • 1d ago • [blog.dshr.org](https://blog.dshr.org/2026/06/ais-affordability-crisis.html)

---

**[Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'](https://news.ycombinator.com/item?id=48658647)**

The LinkedIn co-founder and investor in both Anthropic and OpenAI offers his most pointed public assessment yet of Elon Musk's AI ambitions.

⬆️ 229 • 💬 263 • 22h ago • [Fortune](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)

---

**[For most of the world, open-source AI is the only way forward](https://news.ycombinator.com/item?id=48660839)**

Proprietary AI is both too expensive and too centralized in control for most countries and companies to rely upon.

⬆️ 217 • 💬 139 • 20h ago • [Techstrong.ai](https://techstrong.ai/articles/for-most-of-the-world-open-source-ai-is-the-only-way-forward/)

---

**[The Low-Tech AI of Elden Ring](https://news.ycombinator.com/item?id=48643489)**

⬆️ 162 • 💬 96 • 1d ago • [nega.tv](https://nega.tv/posts/low-tech-ai-of-elden-ring.html)

---

**[Big AI labs are hiring philosophers](https://news.ycombinator.com/item?id=48662452)**

⬆️ 138 • 💬 126 • 18h ago • [economist.com](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers)

---

**[Meta pauses AI training program tracking employee keystrokes after internal leak](https://news.ycombinator.com/item?id=48636632)**

Meta pauses an AI training program after sensitive employee data leaks, sparking internal backlash and highlighting security concerns.

⬆️ 123 • 💬 31 • 2d ago • [Business Insider](https://www.businessinsider.com/meta-ai-training-data-leak-exposed-employee-activity-across-company-2026-6)

---

**[AI Built a Nuke and Still Lost](https://news.ycombinator.com/item?id=48641927)**

Either AI is ready to help run a country, or it can't be trusted with a board game. The honest answer is both.

⬆️ 89 • 💬 98 • 2d ago • [lwilko.com](https://www.lwilko.com/blog/i-gave-an-ai-a-civilization)

---

**[Haystack: Open-Source AI Framework for Production Ready Agents, RAG](https://news.ycombinator.com/item?id=48658095)**

Create agentic, context engineered AI systems using Haystack’s modular and customizable building blocks, built for real-world, production-ready applications.

⬆️ 87 • 💬 21 • 23h ago • [Haystack](https://haystack.deepset.ai/)

---

---

## YouTube Videos: "ai"

**[The AI Future No One Wants to Talk About](https://www.youtube.com/watch?v=zWQe2Fn--Eg)**

Go to https://ground.news/sabine to get 40% off the Vantage plan and see through sensationalized reporting. Stay fully informed ...

📺 Sabine Hossenfelder

👁️ 186K • 👍 12K • 💬 2K • ⏱️ 12:14 • 20h ago

---

**[We Asked AI To Simulate If The U.S. Had A Second Civil War](https://www.youtube.com/watch?v=OdxH1KZbjOY)**

What would happen if Civil War broke out in the United States again in 2026? Thankfully, with modern AI technology, we no ...

📺 The Babylon Bee

👁️ 153K • 👍 17K • 💬 2K • ⏱️ 2:31 • 1d ago

---

**[21,000 Oracle Employees Just Got Replaced by AI](https://www.youtube.com/watch?v=JdMIdaGG7EQ)**

Oracle just axed 21000 jobs. Why? Start your FREE Intro Course with CourseCareers NOW!

📺 Mark Savant

👁️ 8K • 👍 318 • 💬 159 • ⏱️ 11:58 • 1d ago

---

**[AI glasses are creating a cheating problem](https://www.youtube.com/watch?v=R6WdmGwflRE)**

With the rapid development in AI-powered wearables, educators in East Asia are scrambling to deal with cheating students who ...

📺 CNN

👁️ 10K • 👍 228 • 💬 12 • ⏱️ 1:09 • 3h ago

---

**[I Tried Dating AI](https://www.youtube.com/watch?v=xibYjTT7kHs)**

In this video I went on multiple AI dates to learn about the future of relationships. hopefully you enjoy and hopefully i wont take so ...

📺 Husk IRL

👁️ 46K • 👍 4K • 💬 823 • ⏱️ 16:22 • 15h ago

---

**[Symptoms of AI Psychosis](https://www.youtube.com/watch?v=3HeyZIqlGpo)**

Full Episode Spotify: https://open.spotify.com/episode/0BnVK6eJDJA115Q2dDh0i9 Youtube: ...

📺 TheStandupPodClips

👁️ 3K • 👍 94 • 💬 20 • ⏱️ 15:31 • 13h ago

---

**[MIT Just Revealed the AI Bubble&#39;s Fatal Flaw](https://www.youtube.com/watch?v=3ESclFr8m7I)**

How I Became a Sovereign Professional - The Freelance Formula https://www.brendandell.com/freelance-formula-299 Currently ...

📺 Brendan Dell 

👁️ 250K • 👍 8K • 💬 2K • ⏱️ 22:04 • 2d ago

---

**[The AI Spending Collapse Has Already Begun…](https://www.youtube.com/watch?v=I8ijs4czL_0)**

Start your workflow automation using Higgsfield today: https://higgsfield.ai/s/mcp-poojadutt-DmHjkQ ✓ Tech Companies are ...

📺 Pooja Dutt

👁️ 17K • 👍 599 • 💬 102 • ⏱️ 14:28 • 1d ago

---

**[Tim Dillon on Israel, Iran, AI, and Palantir](https://www.youtube.com/watch?v=DyKSUEEPb74)**

Taken from JRE #2518 w/Tim Dillon YouTube: https://youtu.be/wTdqkloiSvk JRE on Spotify: ...

📺 JRE Clips

👁️ 214K • 👍 5K • 💬 1K • ⏱️ 15:48 • 18h ago

---

**[When millions of AI agents meet](https://www.youtube.com/watch?v=V04bm-3d6EQ)**

The conversation of the moment is focused on one topic: AI agents. Unlike traditional language models that simply respond to a ...

📺 Google DeepMind

👁️ 45K • 👍 1K • 💬 125 • ⏱️ 42:38 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 67,107 • ❤️ 2,405 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 70,743 • ❤️ 813 • 22h ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 495,813 • ❤️ 2,317 • 6d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 165,187 • ❤️ 566 • 6d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`text-generation` `9.0B`

⬇️ 134,294 • ❤️ 403 • 2d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 51,717 • ❤️ 703 • 5d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 10,160 • ❤️ 346 • 19h ago

---

**[GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)**

*Unsloth AI*

GLM-5.2 is a large language model optimized for long-horizon tasks, featuring a 1M token context window and advanced coding capabilities with flexible effort levels. It utilizes an improved architecture with IndexShare for reduced FLOPs and is released under an MIT license for broad accessibility.

`text-generation` `753.9B`

⬇️ 88,915 • ❤️ 365 • 1d ago

---

**[Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)**

*KREA*

Krea-2-Turbo is a text-to-image diffusion model capable of generating diverse artistic styles, including halftone, pixelated, impressionist, thermal imaging, and black and white photography. It is primarily used for creative image generation and artistic exploration.

`text-to-image`

⬇️ 2,996 • ❤️ 218 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 3,520,206 • ❤️ 2,216 • 2mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 27 • 💬 1 • ⭐ 6,436 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 36 • 💬 1 • ⭐ 25,507 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 170 • 💬 2 • ⭐ 68,952 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 60 • 💬 1 • ⭐ 84,119 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 88,369 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 246 • 💬 4 • ⭐ 9,167 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 8 • 💬 1 • ⭐ 8,825 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 186 • 💬 6 • ⭐ 5,445 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 23 • 💬 1 • ⭐ 83,731 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 44 • 💬 4 • ⭐ 31,227 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 77.6k • 🔱 10.1k • 14h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 56.8k • 🔱 2.9k • 21h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.7k • 🔱 1.0k • 6m ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 5.2k • 🔱 400 • 1d ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.8k • 🔱 569 • 1m ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.5k • 🔱 437 • 3d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.2k • 🔱 212 • 3d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.9k • 🔱 137 • 2d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 150 • 9d ago

---

**[Forward-Future/loop-library](https://github.com/Forward-Future/loop-library)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 1.6k • 🔱 140 • 11h ago

---

---

*Generated by PeekDeck - A glance is all you need*
