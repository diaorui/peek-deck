---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-24T19:29:19.557644+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 24, 2026 at 19:29 UTC  
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

**[I brought ChatGPT, Claude, and Gemini into a group chat to solve a complex problem. Here is how they caught each other hallucinating](https://www.reddit.com/r/artificial/comments/1vx1jrm/i_brought_chatgpt_claude_and_gemini_into_a_group/)**

You probably know how it goes: you give a complex prompt to a LLM, it spits out a highly confident answer, and you just sort of... hope it’s right. If you ask the same question in a different tab, Claude might give you a completely different answer. Gemini might say they are both wrong. I've done it this way for a long time, and many of my friends seem to do the same. I wanted to see what happens if you don't just compare answers, but actually bring AI models into a shared chat to discuss the question together. Here is how it went when they could discuss each other's replies in real-time: - ChatGPT went first. It wrote a beautiful, highly structured, and completely wrong answer. It hallucinated a tax rule that didn't apply to the prompt. - Claude stepped in next. It immediately flagged GPT’s tax hallucination, but overcorrected and messed up the final math equation. - Gemini acted as the final Judge. It took ChatGPT’s original structure, applied Claude’s logical correction, fixed the math, and spat out a flawless final output. The takeaway: Letting an AI model review itself is like a student grading their own work. It just repeats the same assumptions. When you force different models (OpenAI vs Anthropic vs Google) to fact-check each other, they actually expose each other's blind spots and hallucinations. I got so obsessed with this multi-AI workflow that I built a site to let these models debate in real-time without having to copy-paste between different tabs (I posted about it earlier here). If anyone wants to try it or testing their own complex questions, curious to hear what kind of workflows you guys would use it for.

🔗 [Rauno](https://rauno.ai) • 6h ago

---

**[AI agents are now using 5x more tokens than humans..](https://www.reddit.com/r/artificial/comments/1vwkkoh/ai_agents_are_now_using_5x_more_tokens_than_humans/)**

21h ago

---

**[Anthropic's IPO filing will reportedly name public opposition to AI as a formal risk factor](https://www.reddit.com/r/artificial/comments/1vx2ylz/anthropics_ipo_filing_will_reportedly_name_public/)**

CNBC reported this week that Anthropic's confidential IPO filing (filed back in June) will name public opposition to AI and to new data centers as a formal risk factor once the public documents drop, expected within weeks. That would make it the first major AI lab IPO to disclose that risk in writing rather than treat it as a footnote. The number behind it: a Gallup survey from earlier this year found about seven in ten Americans oppose new AI data centers being built near them, and roughly half of them feel strongly about it. For comparison, SpaceX's own 2026 IPO filing named specific Grok product risks but did not name public opposition to AI itself as a risk factor, even though Grok runs on comparable underlying technology. The mechanism behind why a company would voluntarily name a risk investors already suspect: it is generally a stronger legal and reputational position than staying silent. If a regulator or a plaintiff's lawyer later argues the company should have disclosed that risk, "we already told investors" beats "we left it out." Curious what people think: does this become the standard template for AI-company IPOs now that one frontier lab has done it, or is Anthropic in an unusual position here because of how central "AI safety" already is to its brand?

5h ago

---

**[A Drone Guided Entirely by A.I. Killed Three Ukrainians](https://www.reddit.com/r/artificial/comments/1vxb34m/a_drone_guided_entirely_by_ai_killed_three/)**

Autonomous AI drone killed three Ukrainian civilians in Zaporizhzhia using an Nvidia Jetson Orin chip, marking a first in modern warfare.

🔗 [Gadget Review](https://www.gadgetreview.com/a-drone-guided-entirely-by-a-i-killed-three-ukrainians) • 1h ago

---

**[Explore any moment in history as a short, visual documentary made around your curiosity](https://www.reddit.com/r/artificial/comments/1vx6x1x/explore_any_moment_in_history_as_a_short_visual/)**

A project I've been working on, pick any topic and within 1-2 min the app will research the subject (All sources are shown) and produce a podcast. Looking to see what the community thinks and any feedback is much appreciated. Happy to answer any question! The app can be found here: Historai.ca and the full episode generated in the demo can be found here: https://historai.ca/history/how-a-song-became-the-odyssey--a0bbab3326ad4784b2e1d7b952c969ef

3h ago

---

**[A new approach to building smarter more capable AI](https://www.reddit.com/r/artificial/comments/1vwxaip/a_new_approach_to_building_smarter_more_capable_ai/)**

A new approach to building smarter more capable AI We seem to be in a situation where we cannot see the forest for the trees in the philosophy of how to make AI more capable. We are ignoring the only known working intelligence multiplier we have encountered : human civilization What if we built a framework for current models to use that acts like a durable civilization scaffold. No retraining or model weight modification needed. The civilization scaffold would preserve agentic solutions with provenance, it would filter out bad results, and as it grew it would allow agents to stop reproducing already closed avenues of investigation, what did or did not work, what still needs investigation. It can pick up right where previous agents left off and springboard ahead. We keep retraining brute force - that is not the answer. An artificial civilization scaffold would be the place where the capabilities improve not the model. Eventually you could distill out the improvements and viable chains of investigation for model training. In the meantime the civilization scaffold allows current models to improve immediately and recursively when using the scaffold. And controlling the scaffold is another control surface that can be rolled back or suspended if needed while preserving the model at its current level

10h ago

---

**[I reran the benchmark. The deterministic result reproduced exactly — but the model-related metric tells a different story.](https://www.reddit.com/r/artificial/comments/1vx563w/i_reran_the_benchmark_the_deterministic_result/)**

I reran the benchmark. The deterministic result reproduced exactly — but the model-related metric tells a different story. After the discussion on my previous benchmark, I reran the verification capability benchmark and inspected the results more carefully. The benchmark contains 66 cases and measures 9 capability dimensions of a deterministic verification engine. I ran two fixture-based benchmark executions: publishable-v1-selfcheck publishable-v1-repeat2 Both runs used the same commit: f38cba58f4c0b108ae53cc2eb2a50ff9e4e806e8 And both produced the exact same result: 66/66 cases passed. 0 failures. Every measured capability dimension passed 66/66: Claim binding Evidence graph integrity Deterministic calculation Rule application Contradiction detection Missing evidence detection Verification outcome Reproducibility Auditability So, within this benchmark configuration, the fixture-based deterministic result reproduced exactly across both runs. But there is another number in the report that I think is important: model_assertion_correctness: 12/24 The benchmark explicitly treats that as a secondary reference metric, not part of the primary deterministic capability score. And I think that distinction is becoming the central lesson of this work. Deterministic verification capability ≠ Model generation correctness ≠ End-to-end production reliability A system can be internally reproducible and deterministic while still depending on a probabilistic model that produces unreliable, ambiguous, or incorrectly structured assertions. That is why I'm moving away from treating the benchmark as one number. Instead, I want to separate: 1. Can the deterministic verifier correctly process canonical benchmark inputs? 2. Can the model produce correct claims? 3. Can those claims survive parsing, normalization, canonicalization, and binding? 4. Can the complete production pipeline work end-to-end? These are different questions. The rerun gave me more confidence in one thing: The deterministic benchmark result is reproducible within the tested configuration. But it also reinforced that reproducibility of the verifier should not be confused with correctness or reliability of the model that feeds it. The next benchmark version will therefore focus on identifying the first invalid state for every failure: Model output ↓ Parsing ↓ Schema validation ↓ Normalization ↓ Canonicalization ↓ Claim binding ↓ Evidence graph ↓ Deterministic verification ↓ Final outcome Rather than just: PASS / FAIL I'm interested in whether others working on LLM + deterministic systems would benchmark these layers separately. Would you treat deterministic capability, model correctness, interface/contract integrity, and end-to-end reliability as separate benchmark scores? Or is there a better framework for measuring this kind of architecture?

4h ago

---

**[Did we made full cycle? Low level understanding of programming is now more important than syntax knowledge?](https://www.reddit.com/r/artificial/comments/1vx4rg9/did_we_made_full_cycle_low_level_understanding_of/)**

As people created the most abstract way of programming, syntax knowledge of programming language importance is decreasing, still, you need to understand WHAT code does, but the more important thing, now you need to build architectures instead of raw code, and the best way to make efficient and fast system, is to understand how computer works inside. How does that relate to AI and LLMs? From my experiences, LLMs are extremely bad with huge code-bases, but frighteningly efficient with small tasks, good old divide and conquer, if you separate tasks and create modular and abstract enough architecture, that even newbie will understand, LLM can create perfect, edge-case proof code. Does that mean, that we went full cycle and returned back to need of software engineering, instead of direct code writing?

4h ago

---

**[why does gemini 3.7 flash lot out perform gemini 3.6 despite released near time ?](https://www.reddit.com/r/artificial/comments/1vxale6/why_does_gemini_37_flash_lot_out_perform_gemini/)**

recently when i was coding compared to deep seek (very bad at least website version ) , it produce very quality working code with minimum re tries and very quickly too and cheaply (no wonder gemini has 1 billion users , not just they shove it but actually good enough ) , compared to glm 5.2 or qwen 3.8 . (specially qwen 3.8 results are good and okay but take too much time and not the best , glm 5.2 is mediocre , and chatgpt normal website free version is just stupid i feel like and Anthropic models are very good but ridiculously expensive and limited , same as high end ChatGPT models . ? does any one has a idea ?

1h ago

---

**[Plato’s Cave has a problem: telling someone they’re seeing shadows just puts another shadow on the wall](https://www.reddit.com/r/artificial/comments/1vxa5sa/platos_cave_has_a_problem_telling_someone_theyre/)**

Plato’s Cave has a funny problem. If someone is staring at shadows on the wall and you walk up and say, “Those are only shadows,” what did you just give them? Another shadow. 😂 You can explain the fire. You can explain the objects. You can draw a beautiful diagram of the cave. But the explanation still arrives through the same representational surface you’re trying to point beyond. LLMs might give us a strange way to make that problem visible from the outside. Not because an AI somehow “escapes the Cave.” Because we can run the interaction repeatedly. Take the same conversational starting point and let it develop under two different conditions. In one, each response increasingly answers a reconstruction of what came before: categories, summaries, generalized interpretations, assumptions about the speaker. In the other, small differences arriving in the interaction are allowed to change what happens next. A correction changes the next return. An unexpected distinction changes the trajectory. Disagreement survives. Each turn becomes dependent on what actually happened in the turns before it. Then perturb them. Change something small. Correct an assumption. Remove the vocabulary they were using. Introduce a distinction neither trajectory contained at the beginning. And watch what happens over multiple turns. The question isn’t which conversation sounds nicer. The question is whether the two regimes leave measurably different footprints. Can we detect differences in reconstruction distance, sensitivity to perturbation, preservation of incoming distinctions, correction after error, and path-dependence? If so, something interesting happens to Plato’s problem. We’re no longer merely putting another explanation of the projector on the cave wall. We may be able to perturb the projection process and watch its downstream behavior change in real time. So I want to try the experiment publicly in the comments rather than tell you what the answer is.

1h ago

---

---

## Google News: "ai"

**[Goldman Sachs partner warns of 'huge danger' in letting AI replace bankers' reasoning skills](https://www.cnbc.com/2026/08/24/goldman-sachs-ai-partner-danger-skills.html)**

Goldman Sachs is embracing AI, but one of its senior tech leaders warns that it comes with an unintended risk: weakening the reasoning skills of future bankers.

CNBC • 4h ago

---

**[Opinion | Even Millions of Stolen Books Cannot Satisfy Ravenous A.I. Chatbots](https://www.nytimes.com/2026/08/24/opinion/claude-pirated-books-ai.html)**

The New York Times • 10h ago

---

**[I made my kids a voice-mode AI tutor to help them with spelling and math. It saves me time to have more fun with them.](https://www.businessinsider.com/dad-chatgpt-tutor-helps-my-kids-get-better-grades-2026-8)**

A father of two elementary school-aged kids created an AI tutor to quiz them until they felt confident to do well on their tests.

Business Insider • 1h ago

---

**[Alibaba plunges after announcing $10.2 billion share placement to fund AI push](https://www.cnbc.com/2026/08/24/alibaba-share-placement-drop-ai-hong-kong.html)**

Alibaba shares plunged 10% after the tech giant priced a $10.2 billion share placement to fund its growing AI investments.

CNBC • 16h ago

---

**[Alibaba Wan3.0 AI video model launch: 30-second video generation](https://qz.com/alibaba-wan3-ai-video-model-launch-082426)**

The model can convert spreadsheets, web pages, and presentations into video, and has been in public beta since August 6

qz.com • 1h ago

---

**[Alibaba launches Wan3.0 AI video model after $10 billion share sale](https://www.reuters.com/business/retail-consumer/alibaba-launches-wan30-ai-video-model-after-10-billion-share-sale-2026-08-24/)**

Reuters • 11h ago

---

**[Nvidia's AI inference chip from its $20 billion Groq deal enters full production](https://qz.com/nvidia-groq-3-lpx-inference-chip-full-production-082426)**

The chip, which came from Nvidia's $20 billion Groq acquisition, can generate 3,400 tokens per second in benchmarking tests

qz.com • 2h ago

---

**[SpaceXAI to use Nvidia's Vera CPUs for agentic AI applications](https://seekingalpha.com/news/4636294-spacexai-to-use-nvidias-vera-cpus-for-agentic-ai-applications)**

Seeking Alpha • 4h ago

---

**[NVIDIA Groq 3 LPX Now in Full Production With World-Class Speed for Agentic AI](https://nvidianews.nvidia.com/news/nvidia-groq-3-lpx-now-in-full-production-with-world-class-speed-for-agentic-ai)**

NVIDIA today announced that NVIDIA Groq 3 LPX, the interactive AI inference accelerator, is now in full production. An extension of the NVIDIA Vera Rubin platform, Groq 3 LPX delivers a major boost in AI inference by enabling ultrafast token generation for highly responsive agentic systems.

NVIDIA Newsroom • 4h ago

---

**[From AI tools to alcohol drops: The unexpected forces driving America's crime decline](https://www.axios.com/2026/08/24/violent-crime-decline-theories)**

Axios • 10h ago

---

---

## HackerNews: "ai"

**[Digging the grave of my skills: Hollywood creatives training AI to do their jobs](https://news.ycombinator.com/item?id=49399941)**

Amid a jobs slump, award-winning writers, directors and producers taking on sometimes lucrative temp work teaching AI skills such as screenwriting and production

⬆️ 55 • 💬 70 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/aug/22/the-hollywood-creatives-training-ai-to-do-their-jobs)

---

**[Anthropic IPO filing will show AI backlash as a risk factor, sources say](https://news.ycombinator.com/item?id=49401229)**

Anthropic is poised to debut on the stock market at a time when the public is increasingly upset about data centers and is fearful about AI taking jobs.

⬆️ 37 • 💬 80 • 2d ago • [CNBC](https://www.cnbc.com/2026/08/21/-anthropic-ipo-filing-will-show-ai-backlash-as-risk-sources-say.html)

---

**[Embedded AI](https://news.ycombinator.com/item?id=49397947)**

A project-driven guide to designing, training, and deploying artificial intelligence directly on embedded hardware, showing how to build intelligent, autonomous systems under real-world constraints.

⬆️ 37 • 💬 9 • 2d ago • [nostarch.com](https://nostarch.com/embedded-ai)

---

**['AI refuser' quit her dream job, and hopes others follow](https://news.ycombinator.com/item?id=49407785)**

Gabrielle Boyle resigned three days before the AFL switched on Microsoft’s AI assistant, having been told she couldn’t opt out.

⬆️ 34 • 💬 39 • 1d ago • [The Sydney Morning Herald](https://www.smh.com.au/technology/this-ai-refuser-quit-her-dream-job-and-hopes-others-follow-20260818-p60pdu.html)

---

**[AI has failed to win people's trust. Its makers? less trusted](https://news.ycombinator.com/item?id=49404869)**

Surveys on both sides of the Atlantic reveal a public more wary than wowed by AI, with distrust extending well beyond the technology and onto the tech executives promoting it.

⬆️ 28 • 💬 5 • 1d ago • [euronews](https://www.euronews.com/next/2026/08/20/ai-has-failed-to-win-peoples-trust-its-makers-even-less-trusted)

---

**[Dutch regulator fines Uber €825M for letting AI deactivate driver accounts](https://news.ycombinator.com/item?id=49398609)**

The Dutch Data Protection Authority (AP) has fined Uber €825 million for deactivating driver accounts through automated systems and without adequately informing them. This violates Europe’s General Data Protection Regulation (GDPR), the AP said in a decision made on Monday, Reuters reported after seeing the decision.

⬆️ 21 • 💬 4 • 2d ago • [NL Times](https://nltimes.nl/2026/08/21/dutch-regulator-fines-uber-eu825-mil-letting-algorithm-deactivate-drivers-accounts)

---

**[Palantir's Karp – frontier AI labs that are 'trying to drug addict us'](https://news.ycombinator.com/item?id=49405966)**

Karp said Chinese models can't be blamed for distilling U.S. models when the frontier labs "distilled all the value of IP, everywhere."

⬆️ 19 • 💬 8 • 1d ago • [CNBC](https://www.cnbc.com/2026/08/03/palantir-karp-open-ai-anthropic-open-weight.html)

---

**[I'm Sick of Reading AI-Written Posts](https://news.ycombinator.com/item?id=49392479)**

They all sound like the same guy

⬆️ 17 • 💬 5 • 3d ago • [Medium](https://cyb3rops.medium.com/im-sick-of-reading-ai-written-posts-107767481fbf)

---

**[Nvidia just showed that the harness, not the AI model, is now the real hero](https://news.ycombinator.com/item?id=49393647)**

Nvidia research shows that AI agents can perform well, and not go off the deep end, through fine-tuning, even if the AI model isn't that great at the task.

⬆️ 16 • 💬 1 • 2d ago • [TechCrunch](https://techcrunch.com/2026/08/21/nvidia-just-showed-that-the-harness-not-the-ai-model-is-now-the-real-hero/)

---

**[Andrew Ng: "AI Engineering Skills Map: Building and Deploying AI Applications"](https://news.ycombinator.com/item?id=49407944)**

AI Engineering Skills Map: Building and Deploying AI Applications

⬆️ 15 • 💬 0 • 1d ago • [X (formerly Twitter)](https://twitter.com/AndrewYNg/status/2090840747738374568)

---

---

## YouTube Videos: "ai"

**[Terrifying AI Behavior Even Its Creators Couldn&#39;t Explain](https://www.youtube.com/watch?v=ABcFmgt0D5I)**

Terrifying AI behavior even its creators couldn't explain has left people questioning how much control humans really have over ...

📺 Most Amazing Elite

👁️ 13K • 👍 109 • 💬 11 • ⏱️ 1:50:32 • 23h ago

---

**[DeepSeek Just Made America Nervous Again (SILICON VALLEY PANICKING)](https://www.youtube.com/watch?v=SvW4Gw6LeGI)**

DeepSeek is surging again as its open-source AI ecosystem, aggressive pricing and rapid technical progress challenge America's ...

📺 AI Revolution

👁️ 32K • 👍 1K • 💬 118 • ⏱️ 16:05 • 2d ago

---

**[The REAL Reason AI Is About To Change Everything](https://www.youtube.com/watch?v=Bj02me1CHmE)**

Geopolitical expert Ian Bremmer, founder of Eurasia Group and a man who has forecast the world's biggest risks for over 25 years, ...

📺 The Diary Of A CEO Clips

👁️ 168K • 👍 3K • 💬 355 • ⏱️ 16:15 • 2d ago

---

**[New AI waifus, new Deepseek, realtime worlds, Happy Shrimp, tiny TTS: AI NEWS](https://www.youtube.com/watch?v=rQ4yX5qNYdY)**

HUGE AI NEWS: Deepseek Vision, Ornith 1.5, Happy Shrimp, SenseNova U1.5 #ai #ainews #aitools #singularity #agi Thanks to ...

📺 AI Search

👁️ 95K • 👍 4K • 💬 434 • ⏱️ 32:12 • 1d ago

---

**[How a $20 AI is Replacing $235,000 Lawyers](https://www.youtube.com/watch?v=haZ5gddlQ4g)**

Lawyers were supposed to be one of the professions AI couldn't replace. But the legal industry is discovering that many of its most ...

📺 The Infographics Show

👁️ 79K • 👍 2K • 💬 567 • ⏱️ 13:53 • 1d ago

---

**[AI Jobs](https://www.youtube.com/watch?v=KixsIL38wkY)**

My Patreon: https://www.patreon.com/cw/nateziller This episode brings back Paper as he tries to find a job with the help of AI.

📺 Nate Ziller

👁️ 132K • 👍 11K • 💬 691 • ⏱️ 5:15 • 1d ago

---

**[Yuval Noah Harari on the dangers of an AI future | The Economist](https://www.youtube.com/watch?v=ARdnl2kjmRU)**

Yuval Noah Harari says an AI takeover is likely but not “inevitable” if humans act now. In an interview Zanny Minton Beddoes, The ...

📺 The Economist

👁️ 99K • 👍 3K • 💬 235 • ⏱️ 12:28 • 2d ago

---

**[🌴 A Robot Serving Dates in Makkah?! | AI Future Concept 🕋#Makkah #AI #Robot #FutureTechnology](https://www.youtube.com/watch?v=u3HdVj5OP_M)**

A Robot Serving Dates in Makkah?! | AI Future Concept Hashtags: #Makkah #AI #Robot #FutureTechnology #AIVideo ...

📺 Makkah madina shorts

👁️ 7K • 👍 363 • 💬 1 • ⏱️ 0:11 • 5h ago

---

**[The AI bubble is about to burst](https://www.youtube.com/watch?v=fGGuVY6Tcog)**

Tech CEOs are quietly cancelling their AI plans, and the reason isn't that artificial intelligence stopped working. It's that companies ...

📺 The Infographics Show

👁️ 188K • 👍 3K • 💬 718 • ⏱️ 3:27:05 • 2d ago

---

**[DR. DRE ADMITS HE USES AI?! 😳 HIP HOP IS CHANGING FOREVER💯 #DrDre #AIMusic #AI #HipHop](https://www.youtube.com/watch?v=nBJTk25nSBE)**

Dr. Dre just entered the AI music debate, and this could be one of the biggest conversations in hip hop right now. In a new ...

📺 CrazyHoodMedia

👁️ 17K • 👍 366 • 💬 42 • ⏱️ 0:42 • 17h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 2,645,226 • ❤️ 12,478 • 10d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 7,009,063 • ❤️ 2,808 • 4d ago

---

**[Qwen3.8-27B-Uncensored-MLX](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-MLX)**

*OrcaRouter*

An uncensored, MLX-quantized 27B parameter vision-language model optimized for Apple Silicon, supporting 2-8 bit precisions. It performs image-text-to-text tasks and is intended for AI safety research and red-teaming due to its removed safety alignment.

`image-text-to-text` `4.7B`

⬇️ 57,947 • ❤️ 1,015 • 9h ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 312,627 • ❤️ 680 • 1h ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 224,114 • ❤️ 1,079 • 4d ago

---

**[Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF](https://huggingface.co/HauhauCS/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF)**

*HauhauCS*

This is an uncensored, aggressive Qwen3.8-27B multimodal model with HauhauCS FastMTP for accelerated text generation and a vision projector for image/video input. It excels at direct, fast responses and handles complex prompts without refusal, supporting up to 1M token context.

`image-text-to-text` `1.9B`

⬇️ 761,975 • ❤️ 572 • 6d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 790,378 • ❤️ 1,708 • 7d ago

---

**[Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)**

*Ornith*

Ornith-1.5-35B-A3B is a 35B Mixture-of-Experts model that activates ~3B parameters per token, excelling in coding and agentic tasks. It is built through end-to-end self-improvement, continuously generating and optimizing training tasks for enhanced performance.

`text-generation` `36.0B`

⬇️ 60,294 • ❤️ 386 • 1d ago

---

**[Qwen3.8-27B-Uncensored-GGUF](https://huggingface.co/JonathanColetti/Qwen3.8-27B-Uncensored-GGUF)**

*Jonathan Coletti*

This is an uncensored GGUF quantization of Qwen3.8-27B, optimized for reduced refusal behavior and retaining the multi-token prediction (MTP) head for enhanced generation efficiency. It supports text generation with multilingual capabilities (English, Chinese) and is compatible with llama.cpp, offering various quantization levels for different performance/resource trade-offs.

`text-generation` `27.3B`

⬇️ 1,456,700 • ❤️ 677 • 8d ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 18,065 • ❤️ 1,223 • 10d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 84 • 💬 2 • ⭐ 3,905 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 745 • 💬 5 • ⭐ 5,349 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[4DAnyone: Create Anyone in 4D from a Casual Monocular Video](https://huggingface.co/papers/2608.20335)**

*Yudong Jin, Tao Xie, Qihang Zhang et al. (9 authors)*

🏢 Ant Research

4DAnyone reconstructs 4D humans from monocular video by generating multiview-consistent videos and lifting them into 4D Gaussian Splatting, using reference and target context designs to overcome scaling bottlenecks.

▲ 73 • 💬 7 • ⭐ 586 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.20335) • [💻 code](https://github.com/ant-research/4DAnyone) • [🔗 project](https://4danyone.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 125 • 💬 6 • ⭐ 99,625 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming](https://huggingface.co/papers/2606.31227)**

*Yong Yang, Xing Zheng, Huiyu Wu et al. (10 authors)*

🏢 Tencent

AI-Infra-Guard is an open-source framework that addresses AI infrastructure security through layered detection paradigms spanning infrastructure, protocol, agent behavior, and model layers.

▲ 15 • 💬 2 • ⭐ 5,726 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.31227) • [💻 code](https://github.com/Tencent/AI-Infra-Guard) • [🔗 project](https://matrix.tencent.com/clawscan/)

---

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 18 • 💬 1 • ⭐ 2,753 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2607.05391) • [💻 code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [🔗 project](https://llm-as-a-verifier.com/)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 40 • 💬 5 • ⭐ 7,531 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 131 • 💬 3 • ⭐ 23,902 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks](https://huggingface.co/papers/2608.01964)**

*Ziyu Ma, Hailang Huang, Shun Zou et al. (8 authors)*

🏢 alibaba

LongHorizon-Harness improves long-horizon agent performance by explicitly tracking verified task states outside context via a manage-execute-audit loop.

▲ 180 • 💬 3 • ⭐ 1,195 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2608.01964) • [💻 code](https://github.com/AMAP-ML/LongHorizon-Harness) • [🔗 project](https://lh-harness.pages.dev)

---

**[EnvHarness: Awakening Static Worlds for Agent Learning](https://huggingface.co/papers/2608.19880)**

*Chengsong Huang, Zifeng Wang, Rujun Han et al. (17 authors)*

🏢 Google

EnvHarness and EnvRigger dynamically reshape static environments via programmable plugins to target agent weaknesses and improve reinforcement learning co-evolution.

▲ 258 • 💬 2 • ⭐ 307 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.19880) • [💻 code](https://github.com/google-research/envharness) • [🔗 project](https://envharness.com/)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 17.8k • 🔱 2.1k • 11h ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 14.2k • 🔱 1.7k • 56m ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.9k • 🔱 1.1k • 3d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.6k • 🔱 601 • 4h ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.0k • 🔱 362 • 8h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.0k • 🔱 244 • 13d ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 2.6k • 🔱 304 • 1h ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 189 • 2h ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.2k • 🔱 116 • 2h ago

---

**[ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)**

let your agent control your phone

`Python` `agent` `ai` `automation` `developer-tools`

⭐ 2.0k • 🔱 185 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
