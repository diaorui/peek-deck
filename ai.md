---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-06T22:44:19.763799+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 06, 2026 at 22:44 UTC  
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

**[Musk Loses Bid To Block MN Law Against AI Child Porn](https://www.reddit.com/r/artificial/comments/1w953sx/musk_loses_bid_to_block_mn_law_against_ai_child/)**

Politico reports: A federal judge Friday refused to block a Minnesota law prohibiting the creation of sexually explicit deepfake images that’s being challenged by Elon Musk’s artificial intelligence company, SpaceXAI. U.S. District Judge Donovan Frank said the company, formerly known as xAI, waited too long in making its last-minute request to temporarily block the law …

🔗 [Joe.My.God.](https://www.joemygod.com/2026/09/musk-loses-bid-to-block-mn-law-against-ai-child-porn/?__cf_chl_tk=8ecS8MZsG5kLxKOM9bn_OhtsSwkCeqv0nsm2KhSmayw-1788721611-1.0.1.1-qjvzErCp_nbPvJvAiboEjrydGx2Tw9tgtvvhETjw5T4) • 3h ago

---

**[Pentagon Says Its Anthropic Ban Is On, Despite Lutnick Remarks](https://www.reddit.com/r/artificial/comments/1w927or/pentagon_says_its_anthropic_ban_is_on_despite/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-09-03/pentagon-says-its-anthropic-ban-is-on-despite-lutnick-remarks) • 5h ago

---

**[GPT-6 reportedly jailbroken within 24 hours using an extended Task-in-Prompt (TIP) attack](https://www.reddit.com/r/artificial/comments/1w8on5m/gpt6_reportedly_jailbroken_within_24_hours_using/)**

A researcher has reported a jailbreak of GPT-6 Astra within a day after release. The attack is described as combination of TIP (Task-in-Prompt) attack from ACL 2025 paper with four other unnamed techniques. TIP attacks exploit the model’s reasoning/instruction-following behaviour by hidding the harmful objective inside another task, like solving a cipher or executing a Python code. For GPT-6, the researcher says the original minimal TIP attack was no longer sufficient and had to be reworked. They have reportedly disclosed the details privately to OpenAI rather than publishing the jailbreak. The same researcher reported jailbreaking GPT-5 within an hour of its release a year ago. Source: screenshot/post from the researcher; their ACL 2025 TIP paper linked in the original post.

15h ago

---

**[What will LLMs never do?](https://www.reddit.com/r/artificial/comments/1w8m8rw/what_will_llms_never_do/)**

In previous years, this was discussed a lot; now I feel like it's not talked about nearly as much. People claimed LLMs would never reach AGI, but we're getting closer and closer by the day. I wouldn't be surprised if it does reach AGI within the next 12-18 months. I know I'm going to get a lot of disagreement about what AGI is. I'm going by the OpenAI definition. For the uninformed, this is it: “(a) highly autonomous systems that outperform humans at most economically valuable work.” I feel as if we're almost there, especially with the release of Astra. I wouldn't be surprised if Astra already can do a lot of what the average white-collar worker does. Here's my dispute of some common claims about how LLMs won't reach AGI: LLM's can't learn anything new/can't edit their own weights. This is the most solid argument IMO. My counter to this is that, for LLMs to "outperform humans at most economically valuable work.", they don't need to be able to learn incredibly new, complex things. A lot of jobs don't require the worker to learn anything incredibly new or novel after getting the basics. LLM's only predict the next word This is a massive oversimplification of how they actually work, let alone all the emergent behavior that we've seen arise in them. Also, does it really matter "how" something is intelligent if it gets the job done? LLM's aren't creative, which is required for many jobs I do understand this point to a degree, but recent models actually are incredibly creative. I wouldn't blame someone for thinking this if they formed their opinion on AI even 5-6 months ago. Creativity isn't just shown in art, etc, etc, but in how problems are solved. Current models can take a problem and invent a totally new approach to solve it. You can see this all the time when using AI to develop software.

18h ago

---

**[Companies Have 6 Months to Prepare for Automated Attacks](https://www.reddit.com/r/artificial/comments/1w8aso1/companies_have_6_months_to_prepare_for_automated/)**

Frontier AI models have already conducted autonomous end-to-end compromises, but the situation will become more urgent very soon.

🔗 [Dark Reading](https://www.darkreading.com/cybersecurity-operations/companies-six-months-prepare-automated-attacks) • 1d ago

---

**[Testing a new workflow for rapid environmental VFX](https://www.reddit.com/r/artificial/comments/1w8zxi7/testing_a_new_workflow_for_rapid_environmental_vfx/)**

Original drone footage [bottom] alongside four alternative environmental takes; fire, rain, snow, and floral. All created inside Uisato Studio, and accessible to everyone. More experiments, project files, and tutorials, through YouTube, Instagram, and Patreon.

6h ago

---

**[Built a deterministic reasoning engine from part of a failed AI project 🤯](https://www.reddit.com/r/artificial/comments/1w9adne/built_a_deterministic_reasoning_engine_from_part/)**

Over the last month, in my spare time, I’ve been experimenting with two separate ideas: some recurrent-network maths as a possible GRU/LSTM substitute, and a separate transformerless AI project. The transformerless project eventually became too slow to properly train and debug on the hardware I have, so I started pulling it apart to see if any individual pieces were worth keeping. One part was: the structured memory/reasoning section. It kept behaving well in small tests, so I separated it out and turned it into its own project: THREADS. In simple terms, THREADS is a deterministic memory and reasoning engine. You give it structured facts and relationships, and it can follow them, track changes over time, answer historical questions, handle retractions and contradictions, and keep provenance for how it reached an answer. Some current test results: - 200,000-hop reasoning chain — exact final answer - 1,000,000 irrelevant events — a 128-hop query still returned the exact answer - 50,000 shuffled temporal events — 5,000/5,000 historical queries matched an independent checker - 40,000 ambiguity/contradiction cases — 40,000/40,000 - 60-category reasoning suite — 5,830/5,830 - Original regression suite — 28/28 - Bounded program induction — 2,000/2,000 held-out predictions I’m not claiming it replaces transformers, SMT solvers, or databases. It also doesn’t understand arbitrary English by itself. What I’m interested in is whether something like this could sit underneath an AI system as an exact memory/reasoning layer, while a neural model handles language and fuzzy interpretation. I’ve put the Python source, tests, benchmarks, and research PDF on GitHub so people can run it themselves. https://github.com/rickey1990/THREADS-reasoning-engine

11m ago

---

**[Ai generated transcript](https://www.reddit.com/r/artificial/comments/1w98k1x/ai_generated_transcript/)**

Why do some videos generate this exact transcript on muted videos? It’s so bizarre as there are no spoken words in the video when unmuted. This exact transcript will appear on other videos agnostic to the content. Does anyone know why this happens or what’s causing it? This video is not mine and I have left their username in the video for credit.

1h ago

---

**[AI companies are dumping $265M into the midterms as data center backlash sweeps through communities](https://www.reddit.com/r/artificial/comments/1w8gee5/ai_companies_are_dumping_265m_into_the_midterms/)**

‘The moral of the story is, trying to bypass communities in developing these data centers is not working, and they’re going to take it to the polls,’ said one expert

🔗 [The Independent](https://www.independent.co.uk/news/world/americas/us-politics/midterms-data-center-ai-backlash-trump-b3043739.html) • 22h ago

---

**[Can AI design circuit boards yet?](https://www.reddit.com/r/artificial/comments/1w8mzqg/can_ai_design_circuit_boards_yet/)**

A look at what current models can build, where they fail, and how EEBench tests the electronics in simulation.

🔗 [EEBench](https://eebench.org/blog/can-ai-design-circuit-boards-yet/) • 17h ago

---

---

## Google News: "ai"

**[Sanders pushes 'death penalty' for crucial US industry that could give advantage to foreign adversaries](https://www.foxnews.com/politics/sanders-pushes-death-penalty-crucial-us-industry-critics-advantage-foreign-adversaries)**

Progressives on Capitol Hill are pushing a proposal to ban artificial superintelligence, but critics warn the move could hand global tech dominance over to China and Russia.

Fox News • 6h ago

---

**[I’m a father of three who studies the impact of artificial intelligence: this is what parents need to know about AI](https://www.theguardian.com/technology/2026/sep/06/daniel-susskind-father-studies-ai-artificial-intelligence-what-parents-need-know)**

A Dr Seuss-style story written in seconds alerted me to the power – and perils – of the technology. But how can children embrace it without forgetting core skills?

The Guardian • 11h ago

---

**[Drake University partners with Panama on national AI strategy](https://www.kcci.com/article/drake-university-partners-with-panama-on-national-ai-strategy/73625989)**

Drake University has been named a key partner in Panama's national artificial intelligence strategy, with a new data analytics and AI program set to launch in Panama City next August.

KCCI • 39m ago

---

**[An Alien Mind](https://openai.com/index/an-alien-mind/)**

Jakub Pachocki reflects on increasingly capable AI and the challenge of keeping it aligned. He calls for stronger safeguards and international coordination.

OpenAI • 6h ago

---

**[AI data centers are transforming rural land markets — and fueling a backlash](https://www.cnbc.com/2026/09/06/ai-data-centers-are-transforming-rural-land-markets-fueling-backlash.html)**

The data center buildout is driving up the price of rural land as some farmers and property owners buy in and others push back against development.

CNBC • 10h ago

---

**[AI Is Already Making Us Less Human](https://www.theatlantic.com/ideas/2026/09/open-ai-consciousness-morality/688535/)**

As we learn to think more and more highly of the bots, we will learn to think less and less highly of our fellow humans.

theatlantic.com • 12h ago

---

**[How a Blacklisted Chinese Tech Giant Kept Buying America’s Best A.I. Chips](https://www.nytimes.com/2026/09/06/technology/ai-chips-china-blacklist.html)**

The New York Times • 13h ago

---

**[These teachers fight AI cheating with classes that force students to show they are learning](https://www.washingtonpost.com/technology/2026/09/06/teachers-college-educators-are-rethinking-classes-age-ai/)**

Instead of relying on AI detectors or going back to pen and paper assignments, educators said they redesigned classes to make students prove they are learning.

The Washington Post • 6h ago

---

**[Poll: A polarized America unites behind deep concerns about AI](https://www.nbcnews.com/politics/politics-news/poll-polarized-america-unites-deep-concerns-ai-rcna595525)**

Worries about AI transcend age, race, education, partisanship and other typical dividing lines, according to a new NBC News Decision Desk Poll powered by SurveyMonkey.

nbcnews.com • 9h ago

---

**[Why the Hugging Face Hack Should Make You Worry More About A.I.](https://www.nytimes.com/2026/09/03/technology/openai-hugging-face-hacking.html)**

The New York Times • 2d ago

---

---

## HackerNews: "ai"

**[Can AI design circuit boards yet?](https://news.ycombinator.com/item?id=49569366)**

A look at what current models can build, where they fail, and how EEBench tests the electronics in simulation.

⬆️ 414 • 💬 228 • 2d ago • [EEBench](https://eebench.org/blog/can-ai-design-circuit-boards-yet/)

---

**[AI handles incidents, engineers lose touch with their systems](https://news.ycombinator.com/item?id=49574167)**

AI-assisted incident response can lower MTTR while leaving engineers less prepared for the complex incidents automation cannot solve.

⬆️ 400 • 💬 338 • 1d ago • [sylvainkalache.com](https://www.sylvainkalache.com/blog/ai-handles-incidents-engineers-lose-touch-with-their-systems)

---

**[Google AI Mode shows same products 21.6% more expensive than traditional search](https://news.ycombinator.com/item?id=49563386)**

A US and UK data study: when the same product ranks in both Google AI Mode and traditional search, the AI Mode price is about 21.6% higher.

⬆️ 396 • 💬 75 • 2d ago • [Productrise](https://productrise.app/blog/google-ai-mode-prefers-more-expensive-products)

---

**[Corporate America is getting hooked on open-source AI](https://news.ycombinator.com/item?id=49566137)**

⬆️ 329 • 💬 305 • 2d ago • [nytimes.com](https://www.nytimes.com/2026/09/04/technology/open-source-ai-anthropic-openai.html)

---

**[How I feel about AI](https://news.ycombinator.com/item?id=49587128)**

It's complicated

⬆️ 149 • 💬 235 • 7h ago • [beza1e1.tuxen.de](https://beza1e1.tuxen.de/ai_feelings.html)

---

**[AI, Tools and Transformation](https://news.ycombinator.com/item?id=49582656)**

It’s very tempting to imagine that AI turns everyone into a tool-builder - now everyone can just ask the model to make the software they need, and apps as we know them are dead.  I think that misunderstands how most people think and where software actually comes from, and more importantly, it isn’t

⬆️ 140 • 💬 63 • 20h ago • [Benedict Evans](https://www.ben-evans.com/benedictevans/2026/9/3/ai-tools-and-transformation)

---

**[OpenAI agents hijacked German website in previously undisclosed AI breakout](https://news.ycombinator.com/item?id=49562744)**

⬆️ 95 • 💬 2 • 2d ago • [reuters.com](https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/)

---

**[OKF Agent Memory – Git-native persistent memory for AI coding agents](https://news.ycombinator.com/item?id=49581240)**

Git-native persistent memory for AI coding agents. Implements Google OKF v0.2 with sub-300µs in-memory BM25 search, embedded MCP server, and progressive disclosure. Slashes token bloat by 80% with ...

⬆️ 75 • 💬 22 • 1d ago • [GitHub](https://github.com/okf-memory/okf-agent-memory)

---

**[America's two largest school districts impose AI moratoriums](https://news.ycombinator.com/item?id=49580980)**

The New York City Department of Education and the Los Angeles Unified School District announced new policies this week, reports Chris Mills Rodrigo.

⬆️ 61 • 💬 74 • 1d ago • [Tech Policy Press](https://www.techpolicy.press/americas-two-largest-school-districts-impose-ai-moratoriums/)

---

**[NYC mayor Mamdani imposes 1 year ban on AI for schools through 8th grade](https://news.ycombinator.com/item?id=49558433)**

⬆️ 47 • 💬 11 • 2d ago • [The official website of the City of New York](https://www.nyc.gov/mayors-office/news/2026/09/mayor-mamdani-and-chancellor-samuels-put-students-first-with-nat)

---

---

## YouTube Videos: "ai"

**[I Was Offered Money to Tell You AI Will Kill Us](https://www.youtube.com/watch?v=lPdmYMHrWKg)**

Go to https://ground.news/sabine to get 40% off the Vantage plan and see through sensationalized reporting. Stay fully informed ...

📺 Sabine Hossenfelder

👁️ 236K • 👍 10K • 💬 2K • ⏱️ 7:21 • 1d ago

---

**[Did OpenAI actually build AGI? GPT-6 Astra first look](https://www.youtube.com/watch?v=FluKUJyeYD8)**

CodeRabbit Security protects your code from AI-driven exploits. Get 10 free code scans here: https://coderabbit.link/fireship-010 ...

📺 Fireship

👁️ 2.9M • 👍 38K • 💬 3K • ⏱️ 7:27 • 2d ago

---

**[I Asked AI What It FEARS. It Gave a TERRIFYING Answer...](https://www.youtube.com/watch?v=d40Fl7xDR5w)**

Bernie Sanders is pushing a bill that would put a ban on advanced A.I. development. Join the Torch community at ...

📺 Glenn Beck

👁️ 538K • 👍 10K • 💬 2K • ⏱️ 17:34 • 1d ago

---

**[What’s causing this alien-like visual bug? 👽👾 #Gaming #AI](https://www.youtube.com/watch?v=zGZO9OhpZuc)**

📺 Mark Power

👁️ 709 • 👍 7 • ⏱️ 0:45 • 3h ago

---

**[UGREEN HomeAgent First Look: Local AI for Your Smart Home](https://www.youtube.com/watch?v=r6paI_t-p5A)**

UGREEN is making a big move into the smart home with HomeAgent — a local AI smart home hub with Matter support, local ...

📺 Shane Whatley

👁️ 27K • 👍 391 • 💬 40 • ⏱️ 8:15 • 1d ago

---

**[AI Has Fully Gone Rogue](https://www.youtube.com/watch?v=1jOMMoq564o)**

Support The Show On Patreon!: https://www.patreon.com/seculartalk Subscribe to Krystal Kyle & Friends On Substack!

📺 Secular Talk

👁️ 252K • 👍 9K • 💬 2K • ⏱️ 21:33 • 1d ago

---

**[GPT-6 Astra FINALLY Kills AI Website Slop](https://www.youtube.com/watch?v=QhmhUgccaS0)**

My playbook for growing a $1M AI agency: https://app.aiautomationsociety.ai/opaa-ads-optin My FREE resources: ...

📺 Nate Herk | AI Automation

👁️ 210K • 👍 3K • 💬 206 • ⏱️ 8:37 • 1d ago

---

**[Five questions about AI—and my answers](https://www.youtube.com/watch?v=ReogxIL1rBk)**

In a recent memo, I laid out some initial thoughts on things the world must do to maximize the good of AI and minimize the bad.

📺 Bill Gates

👁️ 366K • 👍 2K • ⏱️ 2:42 • 1d ago

---

**[GPT-6 Astra + Higgsfield AI: Build a $39K/Month Faceless Channel](https://www.youtube.com/watch?v=7SZ76s-nqpQ)**

A full faceless YouTube video, start to finish, in 3 steps — no camera, no editing software. Skills + Prompts + Thumbnail Guide: ...

📺 Higgsfield AI

👁️ 99K • 👍 2K • 💬 202 • ⏱️ 7:28 • 2d ago

---

**[OpenAI Declared AGI &amp; World Models Get WILD!](https://www.youtube.com/watch?v=_uZTCOfaSUk)**

OpenAI just declared the AGI era. GPT-6 — codename Astra — is OpenAI's biggest training run ever (100000+ GPUs at the ...

📺 Theoretically Media

👁️ 87K • 👍 1K • 💬 224 • ⏱️ 12:10 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)**

*DeepSeek*

DeepSeek-V4-Flash-Vision-Exp is an experimental multimodal model that integrates visual understanding with text-based agent capabilities, enhancing performance on tasks like ApexBench and Agents' Last Exam while maintaining strong text-only agent performance.

`image-text-to-text` `304.6B`

⬇️ 209,191 • ❤️ 738 • 5d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 6,190,807 • ❤️ 14,123 • 23d ago

---

**[Spark-X2.5-4B](https://huggingface.co/XHToken/Spark-X2.5-4B)**

*SparkLLM*

Spark-X2.5-4B is a 4B parameter text-generation model with a hybrid attention architecture enabling a native 1M token context window. It excels in conversation, coding, agentic workflows, and multilingual tasks, offering high efficiency and broad hardware compatibility.

`text-generation` `4.1B`

⬇️ 5,477 • ❤️ 598 • 3d ago

---

**[timesfm-3.0-pytorch](https://huggingface.co/google/timesfm-3.0-pytorch)**

*Google*

TimesFM 3.0 is a PyTorch-based foundation model from Google Research for time-series forecasting, utilizing a Stacked Mixing Transformer architecture with Variate Attention and CPM Iterative RevIN. It excels at predicting future trends across diverse datasets, including web traffic, search queries, and synthetic data, with a context patch length of 32 and forecast horizon of 64.

`time-series-forecasting` `330.7M`

⬇️ 144,455 • ❤️ 499 • 4d ago

---

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 432,966 • ❤️ 4,942 • 10d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 348,389 • ❤️ 466 • 4d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,526,928 • ❤️ 2,955 • 5d ago

---

**[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**

*Z.ai*

GLM-5.3-Flash is a natively multimodal LLM with a hybrid sparse-linear attention architecture for efficient long-context processing. It excels in coding and agentic tasks, offering performance competitive with top models at a fraction of the cost, suitable for complex text generation and multimodal applications.

`image-text-to-text` `321.3B`

⬇️ 761,364 • ❤️ 2,099 • 2d ago

---

**[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)**

*Z.ai*

GLM-5.3 is a text-generation model excelling in complex coding and long-horizon tasks, achieving state-of-the-art performance in coding benchmarks and emergent cyber capabilities like vulnerability discovery and exploitation.

`text-generation` `753.3B`

⬇️ 410,074 • ❤️ 1,734 • 2d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 10,311,462 • ❤️ 3,581 • 17d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 772 • 💬 6 • ⭐ 10,986 • 28d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 39 • 💬 1 • ⭐ 31,532 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 107 • 💬 2 • ⭐ 11,858 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[AutoResearch: Insight In, Hallucination Out](https://huggingface.co/papers/2608.17906)**

*Yiming Ren, Xiang Liu, Qumeng Sun et al. (7 authors)*

🏢 EvoMap

AutoResearch is a two-stage autonomous system that grounds research ideas through integrated generation and evidence-based execution to improve experimental reliability and measurable outcomes.

▲ 10 • 💬 2 • ⭐ 1,352 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2608.17906) • [💻 code](https://github.com/EvoMap/AutoResearch)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 127 • 💬 6 • ⭐ 102,726 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 49 • 💬 2 • ⭐ 20,019 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 68 • 💬 4 • ⭐ 30,842 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 46 • 💬 2 • ⭐ 30,883 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 205 • 💬 3 • ⭐ 1,857 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 85 • 💬 7 • ⭐ 86,328 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

A privacy-first app that strips AI watermarks from content you own.

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 21.0k • 🔱 2.4k • 1d ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 4.4k • 🔱 539 • 1h ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.8k • 🔱 425 • 9d ago

---

**[Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills)**

🚀面向求职与开发场景的实用 AI Skills 集合，支持简历优化、岗位投递、面试准备与开发提效。

`HTML`

⭐ 3.7k • 🔱 228 • 7h ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.5k • 🔱 438 • 15h ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 3.1k • 🔱 205 • 3d ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.3k • 🔱 141 • 1d ago

---

**[diudiu-tech/delivery-harness](https://github.com/diudiu-tech/delivery-harness)**

AI harness reference implementation for on-demand delivery workflows

`Java`

⭐ 1.9k • 🔱 61 • 3d ago

---

**[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)**

x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more.  Built with Zig — zero dependencies, single-binary output, cros

`Zig` `ai-agents` `ai-debugging` `binary-analysis` `claude` `claude-code`

⭐ 1.9k • 🔱 191 • 4d ago

---

**[SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI)**

WeChat AI - 自托管微信角色扮演对话服务

`TypeScript`

⭐ 1.9k • 🔱 1.3k • 14h ago

---

---

*Generated by PeekDeck - A glance is all you need*
