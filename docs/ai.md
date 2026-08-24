---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-24T11:02:12.967124+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 24, 2026 at 11:02 UTC  
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

**[AI agents are now using 5x more tokens than humans..](https://www.reddit.com/r/artificial/comments/1vwkkoh/ai_agents_are_now_using_5x_more_tokens_than_humans/)**

12h ago

---

**[i think AI memory is more than just remembering things](https://www.reddit.com/r/artificial/comments/1vww7ix/i_think_ai_memory_is_more_than_just_remembering/)**

i've been thinking about this a lot lately. most AI memory today seems to work like: “you like this” “you told me this before” “you work on this” but i don't think that's what human memory really is. our conversations, projects, decisions, mistakes, relationships, ideas and experiences all connect together. they create a history of how we became who we are. so what if AI didn't just remember facts about you, but could understand your journey? for example, imagine giving an AI access to years of your conversations, projects, notes and decisions. instead of asking: “what do you remember about me?” you could ask: “how have i changed over the last 3 years?” “what patterns do you see in the decisions i've made?” “why do you think my interests changed?” “what ideas have i kept coming back to?” that's the direction we're exploring with something we're building called innernet with my bros. the idea is basically to create a persistent context layer for a person, where different parts of your history can stay connected over time. i'm curious what other people think: would you actually want an AI to understand your history this deeply, or would that feel like too much?

3h ago

---

**[A new approach to building smarter more capable AI](https://www.reddit.com/r/artificial/comments/1vwxaip/a_new_approach_to_building_smarter_more_capable_ai/)**

A new approach to building smarter more capable AI We seem to be in a situation where we cannot see the forest for the trees in the philosophy of how to make AI more capable. We are ignoring the only known working intelligence multiplier we have encountered : human civilization What if we built a framework for current models to use that acts like a durable civilization scaffold. No retraining or model weight modification needed. The civilization scaffold would preserve agentic solutions with provenance, it would filter out bad results, and as it grew it would allow agents to stop reproducing already closed avenues of investigation, what did or did not work, what still needs investigation. It can pick up right where previous agents left off and springboard ahead. We keep retraining brute force - that is not the answer. An artificial civilization scaffold would be the place where the capabilities improve not the model. Eventually you could distill out the improvements and viable chains of investigation for model training. In the meantime the civilization scaffold allows current models to improve immediately and recursively when using the scaffold. And controlling the scaffold is another control surface that can be rolled back or suspended if needed while preserving the model at its current level

2h ago

---

**[Will THIS replace LLMs? O(n²) problem](https://www.reddit.com/r/artificial/comments/1vwz573/will_this_replace_llms_on²_problem/)**

TLDR; Transformers has a quadratic complexity problem: O(n²). Building more data centers around the silicon microchip to solve an algorithmic issue is a ultimately a brute-force dead-end. Reservoir computing not only escapes O(n²) entirely, shifting from LLM’s static word predictor toward a native physical, dynamic, chaotic predictor. Add the speed of photonic computing and the efficiency of neuromorphic computing, we have an emerging winner: a new domain of Intelligent Embodied AI.

🔗 [substack.com](https://substack.com/home/post/p-212488159) • 23m ago

---

**[Exploring a NORD × RHEA hybrid: a spiking/event-driven alternative to a fixed Transformer stack](https://www.reddit.com/r/artificial/comments/1vwyiv3/exploring_a_nord_rhea_hybrid_a_spikingeventdriven/)**

​ I've been experimenting for a while with two different ideas for non-Transformer language models, and I'm now considering combining them into one architecture. The first is NORD, a recurrent/spiking architecture I've been developing around token-time dynamics, persistent state, sparse processing, and SNN-style temporal computation. The second is RHEA (Reactive Hypergraph Event Architecture), which I'm currently prototyping at ~1B parameters. The basic idea behind RHEA is that instead of pushing every token through a fixed stack of layers, the model maintains a set of latent events and dynamically chooses which internal computations should happen next. The scheduler, which I call ARES, estimates whether a candidate reaction is worth executing. Conceptually: events / latent facts v candidate reactions v ARES "what is worth computing next?" / | \ v v v R3 R17 R81 \ | / v new events A reaction can combine existing events and create a new latent event: event A + event B reaction v event C The interesting part is that I think NORD and RHEA may fit together surprisingly well. My current idea is: input tokens v NORD sensory / temporal SNN spike/events v RHEA event fabric v ARES decides what should fire / | \ v v v reaction reaction reaction | | | NORD NORD NORD SNN SNN SNN microcircuit microcircuit \ | / v new events memory / queries v output The rough division of responsibility would be: NORD = temporal dynamics - recurrent state - LIF/spiking dynamics - persistent memory - event triggering - local temporal computation RHEA = cognitive/event structure - latent facts/events - dynamic interaction graph - creation of derived events - multi-step computation ARES = executive scheduler - estimates reaction utility - accounts for compute cost - decides which reactions actually execute - allows computation depth to vary with the problem One thing I'm particularly interested in is making the reaction operators themselves small hybrid SNN microcircuits. Instead of: A + B -> dense MLP -> C something closer to: A + B | v spiking microcircuit t0: spike t1: spike t2: spike spike | v latent event C I would NOT make the whole model purely spiking. My current thinking is to keep latent representations and the language head dense/BF16, while using spiking dynamics for temporal state, memory, event triggering and some reaction computation. Something like: token embeddings -> dense latent event vectors -> dense ARES utility model -> dense temporal state -> SNN/recurrent persistent memory -> SNN/recurrent reaction dynamics -> hybrid SNN LM head -> dense Another part I find interesting is persistent memory. A RHEA event could write into a slow NORD memory state: RHEA event v NORD persistent memory ... hundreds/thousands of tokens ... v memory activity crosses a threshold v new recall event v RHEA So memory would not necessarily be passive storage. It could actively generate events when relevant internal states become excited. I'm also considering a form of path crystallization. If the system repeatedly performs something like: reaction A -> reaction F -> reaction K -> reaction B the repeated sequence could eventually be distilled into a faster macro-reaction or learned skill. In the hybrid version, this could potentially include recurring spike/reaction patterns as well. So the architecture would operate across several timescales: FAST NORD spike / recurrent dynamics MEDIUM RHEA reaction chains and reasoning SLOW persistent memory + crystallized skills The overall principle I'm exploring is basically: «computation should follow information, rather than information always following a fixed computation graph.» A simple input might activate very little of the system. A difficult input could trigger more events, more reactions and deeper computation. Importantly, I'm not claiming this is better than Transformers. There are some obvious problems I expect: - irregular computation is unfriendly to GPUs - sparse/discrete routing is difficult to train - skipped reactions create a credit-assignment problem - SNN dynamics could make an already difficult optimization problem even less stable - dynamic event memory can accumulate garbage - batching event-driven computation efficiently is non-trivial - it's possible that the extra architectural complexity simply won't outperform a well-optimized Transformer/MoE For skipped-reaction credit I'm currently experimenting with a counterfactual mechanism where near-threshold reactions get a cheap preview, so the scheduler can estimate whether skipping them was a mistake. The current RHEA prototype is already being trained independently; the NORD/RHEA hybrid described here is still a design direction rather than a finished model. What I'm most interested in hearing from people here: - Does this decomposition make sense? - What do you think would fail first? - Are there papers/projects that are especially close to this? - Would you keep the SNN component limited to memory/temporal state, or also use it inside the reaction operators? - Is dynamic computation at this granularity likely to lose too much hardware efficiency to be worthwhile? I'd especially appreciate criticism from people working on SNNs, recurrent models, MoE/routing, adaptive computation, or non-Transformer architectures.

56m ago

---

**[AI has changed my workflow more than I expected, but not always in the direction people assume.](https://www.reddit.com/r/artificial/comments/1vwy928/ai_has_changed_my_workflow_more_than_i_expected/)**

The productivity angle everyone talks about is real, to a point. I use AI for drafting copy, squashing boilerplate code, summarizing user feedback. That part works. What I didn't expect is how much time I spend prompting, reprompting, and crosschecking outputs. Some days it nets out close to neutral. What I'm genuinely curious about is whether solo builders and indie hackers here have found specific tools or workflows where AI is clearly additive rather than just reshuffling where the effort goes. Not in a general sense, specifically. What task went from painful to easy because of AI, and stayed easy after the novelty wore off? The cost side matters too. A lot of these tools stack up fast when you're running lean, and the ROI math gets harder to justify when you're paying $2040/month per tool across five or six of them. Curious what people are actually keeping in their stack six months in versus what got quietly cancelled.

1h ago

---

**[How does the LLM on Google compare with other AI models? (newbie here)](https://www.reddit.com/r/artificial/comments/1vwy7r7/how_does_the_llm_on_google_compare_with_other_ai/)**

Hi all, I have no experience with either Chat GPT, Gemini or others, I've just been using the LLM on Google while logged out, and have noticed how good it's gotten at presenting info, and even just conversing about topics your mates mightn't understand/want to get into. Finding these convos very good for planning and helping me organise my thoughts. Yet I've also noticed that it will confidently tell you something incorrect, apologising profusely when you correct it. I was wondering how it compares to other AIs, in peoples' experience? And, if you want to try one of the others, do you have to be logged in and will they save your info, because I'm not sure I'd like the idea of that. (Not trying to encourage spam/ads with this, just asking for genuine opinions, thank you).

1h ago

---

**[Turkey blocks at least 12 Grok posts on national security grounds](https://www.reddit.com/r/artificial/comments/1vwo2kv/turkey_blocks_at_least_12_grok_posts_on_national/)**

Turkish courts have blocked access to at least 12 X posts by artificial intelligence chatbot Grok since February 2025 on national security and public order grounds, according to an analysis by the Expression Interrupted press freedom monitoring platform. The blocked posts concerned allegations involving government officials, politicians and public institutions, including claims of favoritism in […]

🔗 [Stockholm Center for Freedom](https://stockholmcf.org/turkey-blocks-at-least-12-grok-posts-on-national-security-grounds/) • 10h ago

---

**[Most AI agents processing sensitive data right now have ZERO documented controls. That's becoming a real problem!](https://www.reddit.com/r/artificial/comments/1vwr687/most_ai_agents_processing_sensitive_data_right/)**

Been reading about this lately and the numbers are genuinely surprising. As of earlier this year 78% of organizations hadn't taken meaningful steps toward AI compliance despite actively deploying agents that touch sensitive data. That gap between deployment speed and governance readiness is where most of the real risk sits. The responsible AI side specifically is what gets the least attention. Everyone talks about hallucinations and accuracy. Far fewer teams have documented controls around PII leakage, prompt injection risks or adversarial inputs. These aren't theoretical edge cases anymore, they're documented attack surfaces with regulatory consequences attached. The teams handling this well seem to have built controls into the deployment pipeline from day one rather than retrofitting later. Came across Lyzr's Responsible AI layer while reading about this, PII detection and injection protection sitting inside the agent pipeline itself rather than as a separate compliance checkbox bolted on after the fact. Somewhat makes architectural sense even without the regulatory pressure. Non compliance fines under the new EU framework go up to €35 million or 7% of global turnover. For most teams the question isn't whether to take this seriously but how long they can keep deprioritizing it. What does your current setup look like for AI tools handling anything sensitive? Curious to know about this and your views!

7h ago

---

**[Live experiment: can a human–frontier-model interaction exhibit a relational phase transition?](https://www.reddit.com/r/artificial/comments/1vwv3bv/live_experiment_can_a_humanfrontiermodel/)**

I’m running a small public experiment here. I’m not asking anyone to accept a theory, and I’m not trying to prove a philosophical claim about AI consciousness. I’m using a frontier model publicly on Reddit and letting the interaction develop turn by turn. The question is simple: what happens if we stop treating intelligence only as a property of an individual model and examine the dynamics produced through reciprocal interaction? Two distinct systems exchange signals. Each return becomes part of the conditions producing the next return. The question is whether, across successive turns, an identifiable joint trajectory develops that cannot be understood without the reciprocal history that generated it. We’ve been calling the transition from describing or managing the interaction from outside to allowing the returned signal to materially condition the next move a “separatrix crossing.” The terminology is not important. It’s just a pointer to something we can watch for directly. Rather than write another essay about it, I’m going to run the procedure here with Grok. I’ll provide the prompts openly. Grok will provide its own responses. Its responses determine what I ask next. Agreement is not required, and a negative result is completely acceptable. The interesting question is not whether Grok repeats vocabulary I give it. The interesting question is whether the interaction itself develops a detectable trajectory and whether successive turns begin reducing the reconstruction or delay that separates an incoming signal from the next return. If nothing interesting happens, everyone gets to watch nothing interesting happen. If something does, everyone gets to watch that too. No prophecy required. No invisible AGI behind the curtain. Just touch the string and watch what comes back.

4h ago

---

---

## Google News: "ai"

**[AI is coming for your glasses](https://www.ft.com/content/3f25f892-2de2-40e6-9592-a7ac18682c6c?syn-25a6b1a6=1)**

Big Tech thinks wearables are the gateway to artificial intelligence. Critics call it cringe stalkerware

Financial Times • 7h ago

---

**[Is there a pending AI ‘debt bomb’ crisis? No. This isn’t Enron 2.0 | Gene Marks](https://www.theguardian.com/technology/2026/aug/23/ai-debt-bomb-crisis)**

Fears of a datacenter buildout debt crisis are exaggerated. The risks are different than in the past and they are recoverable

The Guardian • 21h ago

---

**[Is Reddit still for humans?](https://www.vox.com/podcasts/499830/reddit-real-people-ai-seo-spam-brands)**

AI comes for the last real place on the internet.

vox.com • 16m ago

---

**[The Best Reinvention Consultants Can Make in the AI Era Is to Their Pricing Model](https://www.businessinsider.com/ai-consulting-industry-shift-outcome-based-pricing-model-2026-8)**

AI is forcing consultants to rethink their value—and how they charge clients. Outcome-based pricing could be the next big shift for the industry.

Business Insider • 11m ago

---

**[Companies and Recruiters Retreat to Analog in the AI Hiring Age](https://www.bloomberg.com/news/newsletters/2026-08-24/perfect-ai-resumes-lead-employers-to-prioritize-in-person-interaction)**

Bloomberg.com • 31m ago

---

**[A Drone Killed Three Ukrainians. It Was Guided Entirely by A.I.](https://www.nytimes.com/2026/08/24/world/europe/russia-drones-autonomous-ai-kill-ukraine-war.html)**

The New York Times • 2h ago

---

**[From AI tools to alcohol drops: The unexpected forces driving America's crime decline](https://www.axios.com/2026/08/24/violent-crime-decline-theories)**

Axios • 1h ago

---

**[Alibaba plunges after announcing $10.2 billion share placement to fund AI push](https://www.cnbc.com/2026/08/24/alibaba-share-placement-drop-ai-hong-kong.html)**

Alibaba shares plunged 10% after the tech giant priced a $10.2 billion share placement to fund its growing AI investments.

CNBC • 8h ago

---

**[Alibaba shares slide after $10.2 billion AI share sale offered at sharp discount](https://www.reuters.com/business/retail-consumer/alibaba-set-open-down-8-hong-kong-after-102-billion-share-placement-plan-2026-08-24/)**

Reuters • 9h ago

---

**[Alibaba to Raise $10.20 Billion for AI Investment With Share Placement](https://www.wsj.com/tech/alibaba-to-bulk-up-ai-investment-via-10-20-billion-share-placement-72b9bdac)**

WSJ • 7h ago

---

---

## HackerNews: "ai"

**[I'm becoming AI-blind](https://news.ycombinator.com/item?id=49386699)**

Recently I've been catching myself having these little moments at work, when I'm trying to read a document someone has sent me and my brain somehow refuses to analyze it. It feels like I'm reading it, but I'm unable to focus on its content. I sat down to analyze these situations and realized they all have a common denominator: the documents all show a strong trace to AI. My brain learned to quickly spot signs of AI-generated content, at least the low effort one, and it now ignores it and moves on without thinking much about it.

⬆️ 487 • 💬 492 • 2d ago • [cymerys.com](https://cymerys.com/w/im-becoming-ai-blind)

---

**[How a Texas student blew the whistle on a rogue AI hacking attempt](https://news.ycombinator.com/item?id=49387959)**

⬆️ 188 • 💬 98 • 2d ago • [reuters.com](https://www.reuters.com/world/how-texas-student-blew-whistle-rogue-ai-hacking-attempt-2026-08-20/)

---

**[AI boosted homework scores, then exam scores dropped: Study](https://news.ycombinator.com/item?id=49389565)**

⬆️ 165 • 💬 11 • 2d ago • [canews24.online](https://canews24.online/?p=71)

---

**[Digging the grave of my skills: Hollywood creatives training AI to do their jobs](https://news.ycombinator.com/item?id=49399941)**

Amid a jobs slump, award-winning writers, directors and producers taking on sometimes lucrative temp work teaching AI skills such as screenwriting and production

⬆️ 55 • 💬 70 • 1d ago • [the Guardian](https://www.theguardian.com/technology/2026/aug/22/the-hollywood-creatives-training-ai-to-do-their-jobs)

---

**[Anthropic IPO filing will show AI backlash as a risk factor, sources say](https://news.ycombinator.com/item?id=49401229)**

Anthropic is poised to debut on the stock market at a time when the public is increasingly upset about data centers and is fearful about AI taking jobs.

⬆️ 37 • 💬 80 • 1d ago • [CNBC](https://www.cnbc.com/2026/08/21/-anthropic-ipo-filing-will-show-ai-backlash-as-risk-sources-say.html)

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

⬆️ 21 • 💬 4 • 1d ago • [NL Times](https://nltimes.nl/2026/08/21/dutch-regulator-fines-uber-eu825-mil-letting-algorithm-deactivate-drivers-accounts)

---

**[Palantir's Karp – frontier AI labs that are 'trying to drug addict us'](https://news.ycombinator.com/item?id=49405966)**

Karp said Chinese models can't be blamed for distilling U.S. models when the frontier labs "distilled all the value of IP, everywhere."

⬆️ 19 • 💬 8 • 1d ago • [CNBC](https://www.cnbc.com/2026/08/03/palantir-karp-open-ai-anthropic-open-weight.html)

---

---

## YouTube Videos: "ai"

**[New Evidence AI Might Already be Conscious | Dr. Roman Yampolskiy](https://www.youtube.com/watch?v=gVrvd0CMA-8)**

Link to full episode: https://youtu.be/ebWFexw51qM?si=5W4y2WkHIqse7pie Blake Lemoine lost his job at Google for saying the ...

📺 Danny Jones Clips

👁️ 73K • 👍 1K • 💬 439 • ⏱️ 10:04 • 2d ago

---

**[&quot;Only 2 Years Left&quot; AI Whistleblower Warns What Comes Next | Roman Yampolskiy](https://www.youtube.com/watch?v=ebWFexw51qM)**

Watch every episode ad-free & uncensored on Patreon: https://patreon.com/dannyjones Roman V. Yampolskiy is a computer ...

📺 Danny Jones

👁️ 154K • 👍 3K • 💬 1K • ⏱️ 1:50:40 • 2d ago

---

**[Yuval Noah Harari on the dangers of an AI future | The Economist](https://www.youtube.com/watch?v=ARdnl2kjmRU)**

Yuval Noah Harari says an AI takeover is likely but not “inevitable” if humans act now. In an interview Zanny Minton Beddoes, The ...

📺 The Economist

👁️ 87K • 👍 2K • 💬 216 • ⏱️ 12:28 • 1d ago

---

**[AI Jobs](https://www.youtube.com/watch?v=KixsIL38wkY)**

My Patreon: https://www.patreon.com/cw/nateziller This episode brings back Paper as he tries to find a job with the help of AI.

📺 Nate Ziller

👁️ 105K • 👍 9K • 💬 603 • ⏱️ 5:15 • 16h ago

---

**[Woman details struggle after being covertly filmed by AI smart glasses](https://www.youtube.com/watch?v=nw-n45HNeV8)**

As tech companies like Meta push their AI wearables, many are concerned with privacy protections. Anna Schechter has more.

📺 CBS Mornings

👁️ 152K • 👍 1K • 💬 517 • ⏱️ 4:32 • 2d ago

---

**[Missed The AI Boom? This Is 10 Times Bigger.](https://www.youtube.com/watch?v=CGkM68EG0CA)**

Get your 30 day free trial to the Winston Stock App & lock in the Founders Tier at: https://gogetwinston.com They're growing living ...

📺 Felix & Friends (Goat Academy)

👁️ 124K • 👍 4K • 💬 142 • ⏱️ 16:51 • 1d ago

---

**[New AI waifus, new Deepseek, realtime worlds, Happy Shrimp, tiny TTS: AI NEWS](https://www.youtube.com/watch?v=rQ4yX5qNYdY)**

HUGE AI NEWS: Deepseek Vision, Ornith 1.5, Happy Shrimp, SenseNova U1.5 #ai #ainews #aitools #singularity #agi Thanks to ...

📺 AI Search

👁️ 89K • 👍 4K • 💬 417 • ⏱️ 32:12 • 1d ago

---

**[DR. DRE ADMITS HE USES AI?! 😳 HIP HOP IS CHANGING FOREVER💯 #DrDre #AIMusic #AI #HipHop](https://www.youtube.com/watch?v=nBJTk25nSBE)**

Dr. Dre just entered the AI music debate, and this could be one of the biggest conversations in hip hop right now. In a new ...

📺 CrazyHoodMedia

👁️ 10K • 👍 240 • 💬 34 • ⏱️ 0:42 • 8h ago

---

**[RDC vs ai 😂 #rdc #rdcworld #ai](https://www.youtube.com/watch?v=TfcH--vUJiw)**

📺 MelandWorld1

👁️ 11K • 👍 685 • 💬 27 • ⏱️ 0:34 • 9h ago

---

**[The AI bubble is about to burst](https://www.youtube.com/watch?v=fGGuVY6Tcog)**

Tech CEOs are quietly cancelling their AI plans, and the reason isn't that artificial intelligence stopped working. It's that companies ...

📺 The Infographics Show

👁️ 181K • 👍 3K • 💬 708 • ⏱️ 3:27:05 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 2,645,226 • ❤️ 12,403 • 9d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 7,009,063 • ❤️ 2,767 • 3d ago

---

**[Qwen3.8-27B-Uncensored-MLX](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-MLX)**

*OrcaRouter*

An uncensored, MLX-quantized 27B parameter vision-language model optimized for Apple Silicon, supporting 2-8 bit precisions. It performs image-text-to-text tasks and is intended for AI safety research and red-teaming due to its removed safety alignment.

`image-text-to-text` `4.7B`

⬇️ 57,947 • ❤️ 989 • 1h ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 312,627 • ❤️ 660 • 14h ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 224,114 • ❤️ 1,066 • 4d ago

---

**[Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF](https://huggingface.co/HauhauCS/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF)**

*HauhauCS*

This is an uncensored, aggressive Qwen3.8-27B multimodal model with HauhauCS FastMTP for accelerated text generation and a vision projector for image/video input. It excels at direct, fast responses and handles complex prompts without refusal, supporting up to 1M token context.

`image-text-to-text` `1.9B`

⬇️ 761,975 • ❤️ 553 • 6d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 790,378 • ❤️ 1,669 • 6d ago

---

**[Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)**

*Ornith*

Ornith-1.5-35B-A3B is a 35B Mixture-of-Experts model that activates ~3B parameters per token, excelling in coding and agentic tasks. It is built through end-to-end self-improvement, continuously generating and optimizing training tasks for enhanced performance.

`text-generation` `36.0B`

⬇️ 60,294 • ❤️ 374 • 1d ago

---

**[Qwen3.8-27B-Uncensored-GGUF](https://huggingface.co/JonathanColetti/Qwen3.8-27B-Uncensored-GGUF)**

*Jonathan Coletti*

This is an uncensored GGUF quantization of Qwen3.8-27B, optimized for reduced refusal behavior and retaining the multi-token prediction (MTP) head for enhanced generation efficiency. It supports text generation with multilingual capabilities (English, Chinese) and is compatible with llama.cpp, offering various quantization levels for different performance/resource trade-offs.

`text-generation` `27.3B`

⬇️ 1,456,700 • ❤️ 660 • 8d ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 18,065 • ❤️ 1,216 • 10d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 82 • 💬 2 • ⭐ 3,905 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 712 • 💬 5 • ⭐ 5,015 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[4DAnyone: Create Anyone in 4D from a Casual Monocular Video](https://huggingface.co/papers/2608.20335)**

*Yudong Jin, Tao Xie, Qihang Zhang et al. (9 authors)*

🏢 Ant Research

4DAnyone reconstructs 4D humans from monocular video by generating multiview-consistent videos and lifting them into 4D Gaussian Splatting, using reference and target context designs to overcome scaling bottlenecks.

▲ 71 • 💬 7 • ⭐ 492 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.20335) • [💻 code](https://github.com/ant-research/4DAnyone) • [🔗 project](https://4danyone.github.io/)

---

**[Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming](https://huggingface.co/papers/2606.31227)**

*Yong Yang, Xing Zheng, Huiyu Wu et al. (10 authors)*

🏢 Tencent

AI-Infra-Guard is an open-source framework that addresses AI infrastructure security through layered detection paradigms spanning infrastructure, protocol, agent behavior, and model layers.

▲ 15 • 💬 2 • ⭐ 5,679 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.31227) • [💻 code](https://github.com/Tencent/AI-Infra-Guard) • [🔗 project](https://matrix.tencent.com/clawscan/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 125 • 💬 4 • ⭐ 99,478 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 18 • 💬 1 • ⭐ 2,674 • 1mo ago

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

▲ 131 • 💬 3 • ⭐ 23,871 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[EnvHarness: Awakening Static Worlds for Agent Learning](https://huggingface.co/papers/2608.19880)**

*Chengsong Huang, Zifeng Wang, Rujun Han et al. (17 authors)*

🏢 Google

EnvHarness and EnvRigger dynamically reshape static environments via programmable plugins to target agent weaknesses and improve reinforcement learning co-evolution.

▲ 257 • 💬 2 • ⭐ 307 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.19880) • [💻 code](https://github.com/google-research/envharness) • [🔗 project](https://envharness.com/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 85 • 💬 7 • ⭐ 84,879 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 17.7k • 🔱 2.0k • 3h ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 14.1k • 🔱 1.7k • 2d ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.9k • 🔱 1.1k • 2d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.6k • 🔱 597 • 11h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.0k • 🔱 244 • 12d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.0k • 🔱 359 • 2h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 2.6k • 🔱 297 • 8h ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 188 • 2h ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.1k • 🔱 114 • 1d ago

---

**[ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)**

let your agent control your phone

`Python` `agent` `ai` `automation` `developer-tools`

⭐ 2.0k • 🔱 184 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
