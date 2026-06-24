---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-24T12:19:41.280225+00:00'
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

**Last Updated:** June 24, 2026 at 12:19 UTC  
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

**[Cheap Chinese AI models are quickly gaining customers across the US market: ‘This changes things’](https://www.reddit.com/r/artificial/comments/1udzf0d/cheap_chinese_ai_models_are_quickly_gaining/)**

The Trump administration has been increasingly wary about China’s breakneck pace in AI development – with officials warning as recently as recently as April that China was engaged in “industrial-sc…

🔗 [New York Post](https://nypost.com/2026/06/22/business/cheap-chinese-ai-models-are-quickly-gaining-customers-across-the-us-market/) • 11h ago

---

**[A significant portion of the remaining training data for AI is located on magnetic tapes stored in warehouses.](https://www.reddit.com/r/artificial/comments/1ue6c2m/a_significant_portion_of_the_remaining_training/)**

I have been learning about the shortage of AI training data and one aspect that nobody considers is that much of the potential training data that can be used is not stored in any database system but rather on the old magnetic tapes that have been stored in climate controlled lockers for decades now. The 80s through the 2000s saw all major businesses, government offices, hospitals, television stations, and laboratories include backup of everything on tapes. Most of this data has neither been digitized nor indexed correctly. With the advent of private LLM development, it turns out that the best datasets companies have are sitting on tapes in boxes. Based on all the predictions that I have seen, the growth of internet based training data will quit at some point, roughly in 2026. The following training data could be derived from archiving older materials.

5h ago

---

**[We chased a hallucinated quote through 30k training records, 4,600 transcripts, and our own system prompt. Turned out to be two separate bugs](https://www.reddit.com/r/artificial/comments/1ueaya4/we_chased_a_hallucinated_quote_through_30k/)**

Some of our customers noticed Inter-1 (our omni-modal social-signal model) would occasionally "hear" a quote that didn't exist. Feed it a video with zero audio and ask what was said, and it would sometimes report: "Yeah, Friday at five." Verbatim. Same line, every time. We assumed it had to be baked into the training data somewhere, so we went looking everywhere: 30,960 training records with datetime mentions → zero hits on the phrase 4,603 video transcripts → zero hits ~800 inference probes, 584 storage objects → zero hits Turns out the phrase was sitting in our own system prompt — a worked example we'd written to show the model the expected output format, buried in a version our GEPA prompt-optimizer had shipped. But that only explained where the words came from, not why the model would say them over total silence. So we ran two ablations in our internal eval harness: Swap the word, keep the model: changed the prompt's example to "Tuesday at noon." Fabrication rate went up (37%→50%), and the invented quote tracked the swap exactly — Friday→Tuesday. Swap the model, keep the prompt: ran the same byte-identical prompt through larger variants and an earlier checkpoint of our own model. They barely fabricated (0–2%). Only the further-post-trained Inter-1 confabulated at ~12%. So it's not one bug, it's two stacked priors: the prompt supplied the script, but post-training is what gave the model the compulsion to recite something rather than report silence. Deleting the prompt example stops that one sentence — it doesn't stop the model from inventing different dialogue instead. We think this is a textual/in-context variant of the audio-visual "Clever Hans effect" that's been documented for vision priors (model writes "thud" over a silent skateboard wipeout) — except ours shows the same reflex gets worded by whatever's nearest in the context window, which a vision-only diagnostic wouldn't catch. Full writeup with the fabrication-rate forest plot and log data: https://www.interhuman.ai/blog/goblin-yeah-friday-at-five

47m ago

---

**[Leaked files detail Russia's Social Design Agency building fake reference platforms to contaminate AI training data and search indices](https://www.reddit.com/r/artificial/comments/1udvuhe/leaked_files_detail_russias_social_design_agency/)**

Leaked planning documents obtained by Bloomberg describe a Russian state-linked operation called "Project 2026," run by the Social Design Agency (SDA), with the stated goal of seeding the information layer that AI chatbots and search engines draw from. This is a structurally different threat than the bot and social media campaigns practitioners have long accounted for. The documents describe three components. A German-language Wikipedia clone is designed to look like legitimate reference material while embedding Russian narratives, on the explicit theory that AI systems trained on publicly available text would absorb and repeat those narratives in generated answers. A second component is an AI-driven "self-filling knowledge base" also targeting Germany, for which the documents state that servers are already running and the database already contains over 200,000 pages. A third initiative targeting Western think tanks launched in English, with German, French, and Spanish versions planned. Our coverage: https://aiweekly.co/alerts/russias-project-2026-targets-ai-and-search-leaked-files-show

13h ago

---

**[How can GraphRAG be imputed with a traditional Rag?](https://www.reddit.com/r/artificial/comments/1ue9gqd/how_can_graphrag_be_imputed_with_a_traditional_rag/)**

Hi everyone, I've been reading about this, especially about what LazyGraphRAG does, but it only works for complex questions. Therefore, my idea is to combine it with traditional RAG to ask both complex and simple questions with equal accuracy, but I don't know how to implement it. Is anyone doing something similar? Any ideas? Does anyone have experience with this?

2h ago

---

**[The CEO of a company with 700,000 delivery workers just said robots will replace all of them](https://www.reddit.com/r/artificial/comments/1udvvef/the_ceo_of_a_company_with_700000_delivery_workers/)**

Saw this on Computerworld today and i've been thinking about it since Founder of JD.com said robots will replace all 700,000 of their delivery workers. Didn't sugarcoat it, didn't give a timeline, just said it's coming What got me was he also said he doesn't want his workers going hungry because of it, and their solution is retraining some of them to fix the robots taking their jobs. 700,000 is a lot of people to just figure it out Do you guys think this is actually as close as they're making it sound

13h ago

---

**[Question aux développeurs et fondateurs expérimentés en IA.](https://www.reddit.com/r/artificial/comments/1ue9c1o/question_aux_développeurs_et_fondateurs/)**

Question aux développeurs et fondateurs expérimentés en IA. Je travaille actuellement sur un moteur de recommandation multi-sources. L’architecture repose sur un catalogue propriétaire de prestataires qualifiés, enrichi par des sources externes (APIs de réservation, recherche web, etc.), avec une logique catalogue-first. Le système intègre une orchestration multi-sources : un catalogue de plus de 300 adresses qualifiées ; une mémoire utilisateur persistante ; un moteur de scoring dynamique des prestataires ; un pipeline de composition d’expériences sous contraintes ; une interface conversationnelle basée sur l’IA. À terme, l’objectif est également de réduire la dépendance aux modèles tiers en migrant progressivement vers une architecture basée sur Mistral adapté à notre contexte métier. Ma question est la suivante : Dans l’écosystème actuel, où beaucoup d’acteurs lèvent des fonds pour construire des modèles propriétaires ou faire de la deep tech, comment évaluez-vous la valeur défendable d’une entreprise comme la mienne ? Est-ce que les avantages concurrentiels issus de la donnée propriétaire, du catalogue, de la mémoire utilisateur et de la logique métier constituent selon vous un moat suffisamment fort ? Ou pensez-vous qu’à long terme la vraie barrière à l’entrée restera principalement la maîtrise du modèle lui-même ? Je serais très intéressée d’avoir l’avis de personnes ayant construit ou financé des produits IA à forte composante technologique.

2h ago

---

**[IONS: A reasoning graph that stores claims, evidence, and reasoning paths outside the LLM](https://www.reddit.com/r/artificial/comments/1ue3jd2/ions_a_reasoning_graph_that_stores_claims/)**

I’ve been experimenting with an open source alternative approach to AI memory and reasoning called IONS. The basic idea is that instead of storing all knowledge inside model weights, knowledge is represented as a graph of evidence backed claims called Cognitive Building Blocks (CBBs). Each CBB contains: \-A claim \-Supporting evidence \-Confidence metadata \-Provenance \-Relationships to other claims Relationships are typed: \-supports \-causes \-contradicts \-depends\_on \-derived\_from When a query is executed, the system traverses the graph and returns: \-The answer \-Supporting claims \-Confidence scores \-The reasoning path used to reach the conclusion The goal is not to replace LLMs. The goal is to make reasoning and knowledge inspectable rather than implicit. Current questions I’m exploring: \-How does this compare to GraphRAG? \-Does explicit claim storage improve explainability? \-Can confidence be computed from evidence quality instead of generated by the model? \-Can knowledge be shared across independent nodes without retraining models? Public node: 162.243.203.243:8000 Whitepaper: [github.com/nomad505050/ions-genesis/docs/whitepaper.md]https://github.com/nomad505050/ions-genesis/blob/main/docs/whitepaper.md I’d appreciate feedback from anyone working on GraphRAG, knowledge graphs, memory systems, agent memory, or explainable AI.

7h ago

---

**[Is AI 'one big bubble'? Behind the tech sell-off](https://www.reddit.com/r/artificial/comments/1ue8cny/is_ai_one_big_bubble_behind_the_tech_selloff/)**

Investors are selling off AI-related stocks as doubts are starting to surface over whether the massive spending on AI is worth the investment and whether it's "one big bubble."

🔗 [NPR](https://www.npr.org/2026/06/23/nx-s1-5867633/ai-selloff-tech-stocks-bubble-nasdaq) • 3h ago

---

**[I scanned 50 SaaS websites for AI readiness. Most failed the same 3 things](https://www.reddit.com/r/artificial/comments/1uebegn/i_scanned_50_saas_websites_for_ai_readiness_most/)**

I’ve been digging into “AI visibility” lately — basically whether tools like ChatGPT, Claude, Perplexity, etc. can actually understand and recommend a SaaS company. Not SEO in the classic sense. More like: if someone asks an AI tool “what’s the best software for [use case]?”, does your site give the AI enough clear information to confidently include you? I ran 50 SaaS sites through an AI-readiness scanner and kept seeing the same issues. Crawler access was messy Some sites were blocking or limiting AI crawlers without realizing the downstream impact. The site works fine for humans, Google can often still index it, but AI systems may not be able to access or interpret key pages properly. The homepage copy was way too vague Lots of “streamline workflows,” “empower teams,” “scale faster,” “AI-powered platform” type copy. That might pass the vibe check for humans, but it’s not great for machines. AI systems need clear context: What category are you in? Who exactly is it for? What job does it do? What tools do you replace? What are the main use cases? What makes you different? If that isn’t obvious, the AI will either summarize you badly or ignore you. Weak structured data / missing machine-readable context A lot of sites had missing schema, vague pricing pages, thin docs, unclear product pages, no comparison pages, or no simple summary of what the company actually does. I find that most SaaS websites are optimized for human visitors, but not for AI agents. That’s probably going to matter more as buyers start using AI tools for product discovery and comparison. I used a tool to run the checks, DM if you want it. Not sue if I will get banned if I add it :) It gives a quick score and shows issues around AI crawlability, schema, pricing clarity, sitemaps, and whether AI tools can understand/recommend the business. Feels like “AI readiness” might become a technical SEO checklist item pretty soon. Is anyone here actively working on this yet, or are you waiting until there’s clearer evidence it drives pipeline?

24m ago

---

---

## Google News: "ai"

**[‘You can’t make billions without hurting people’: Cory Doctorow on Elon Musk, the AI bubble and bosses’ cruel fantasies](https://www.theguardian.com/technology/2026/jun/24/cory-doctorow-on-elon-musk-ai-bubble-bosses-cruel-fantasies)**

The writer who coined the word ‘enshittification’ tells us why AI will never deliver what it promises – and why it still appeals so much to those in power

The Guardian • 3h ago

---

**[N.S.A. Lost Access to Powerful A.I. Model Amid Anthropic Dispute](https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html)**

The New York Times • 15h ago

---

**[Microsoft points to lower water use in AI era](https://www.axios.com/2026/06/24/microsoft-lower-water-use-ai)**

Axios • 17m ago

---

**[Biotech Visionary Is Skeptical About AI’s Impact on Medical Innovation](https://www.bloomberg.com/news/articles/2026-06-24/biotech-visionary-is-skeptical-about-ai-s-impact-on-medical-innovation)**

Bloomberg.com • 19m ago

---

**[Qualcomm to buy AI startup Modular](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/)**

Reuters • 9m ago

---

**[Big Tech won the race. But the AI fight is just beginning.](https://www.politico.com/news/2026/06/23/micah-lasher-wins-new-york-congress-primary-00972335)**

Politico • 10h ago

---

**[Big Tech's $2.7 trillion AI bill comes due: Chart of the Day](https://finance.yahoo.com/markets/article/big-techs-27-trillion-ai-bill-comes-due-chart-of-the-day-100000100.html)**

The “Magnificent Seven” plus Broadcom and Oracle have lost roughly $2.7 trillion in market value in June, according to Yahoo Finance analysis, as investors take a harder look at the companies funding the AI build-out.

Yahoo Finance • 2h ago

---

**[Tech companies would have to pay AI data center energy costs under bill moving in Congress](https://www.cnbc.com/2026/06/24/ai-data-centers-tech-companies-congress-energy-costs.html)**

A House subcommittee may advance legislation Wednesday to make tech companies pay the energy costs for operating data centers to power AI.

CNBC • 2h ago

---

**[Stanford was their golden ticket - could AI help or hinder that?](https://www.bbc.com/news/articles/c872j82j2qyo)**

The BBC spoke with Stanford University graduates about what they really think about artificial intelligence.

BBC • 13h ago

---

**[Wall Street is getting trampled by an AI sell-off. South Korean market plunges 10%](https://www.cnn.com/2026/06/23/business/stock-market-kospi-dow-nasdaq-ai)**

Volatility has returned to the stock market, and AI is once again the culprit.

CNN • 1d ago

---

---

## HackerNews: "ai"

**[Apertus – Open Foundation Model for Sovereign AI](https://news.ycombinator.com/item?id=48622778)**

Fully Open Foundation Model for Sovereign AI

⬆️ 531 • 💬 182 • 2d ago • [apertvs.ai](https://apertvs.ai/)

---

**[AI's Affordability Crisis](https://news.ycombinator.com/item?id=48646276)**

A year ago in The Back Of The AI Envelope  I pointed out that the AI platforms were running the drug-dealer's algorithm, "the first one's fr...

⬆️ 298 • 💬 388 • 21h ago • [blog.dshr.org](https://blog.dshr.org/2026/06/ais-affordability-crisis.html)

---

**[The Low-Tech AI of Elden Ring](https://news.ycombinator.com/item?id=48643489)**

⬆️ 152 • 💬 89 • 1d ago • [nega.tv](https://nega.tv/posts/low-tech-ai-of-elden-ring.html)

---

**[Meta pauses AI training program tracking employee keystrokes after internal leak](https://news.ycombinator.com/item?id=48636632)**

Meta pauses an AI training program after sensitive employee data leaks, sparking internal backlash and highlighting security concerns.

⬆️ 121 • 💬 31 • 1d ago • [Business Insider](https://www.businessinsider.com/meta-ai-training-data-leak-exposed-employee-activity-across-company-2026-6)

---

**[AI Built a Nuke and Still Lost](https://news.ycombinator.com/item?id=48641927)**

Either AI is ready to help run a country, or it can't be trusted with a board game. The honest answer is both.

⬆️ 86 • 💬 96 • 1d ago • [lwilko.com](https://www.lwilko.com/blog/i-gave-an-ai-a-civilization)

---

**[AI has already killed academia as we know it?](https://news.ycombinator.com/item?id=48634966)**

No AI was used in writing this post.

If academia was a game, I've won it. Tenure, an endowed research chair, awards, leadership positions, an international journal I helped to found and now serve as the Editor-in-Chief, students I have supervised to their own successes, a good

⬆️ 66 • 💬 51 • 1d ago • [Truths and Loves](https://truths-and-loves.ghost.io/ai-has-already-killed-academia-as-we-know-it/)

---

**[Tech Workers Are Fighting Against Silicon Valley's AI Push](https://news.ycombinator.com/item?id=48623695)**

More tech workers are organizing to fight back as they feel they are losing influence over decisions that affect their jobs, writes Varsha Bansal.

⬆️ 46 • 💬 14 • 2d ago • [Tech Policy Press](https://www.techpolicy.press/tech-workers-are-fighting-against-silicon-valleys-ai-push/)

---

**[US AI stock sell-off shakes markets from Wall Street to Asia](https://news.ycombinator.com/item?id=48654795)**

Losses spread globally as investors questioned soaring valuations and spending on AI infrastructure

⬆️ 45 • 💬 32 • 8h ago • [the Guardian](https://www.theguardian.com/business/2026/jun/23/ai-stocks-sell-off-us-markets)

---

**[How to burst the AI bubble: Strike at its roots](https://news.ycombinator.com/item?id=48657518)**

Sci-fi author/tech journalist Cory Doctorow on his new book, The Reverse Centaur's Guide to Life After AI.

⬆️ 44 • 💬 33 • 2h ago • [Ars Technica](https://arstechnica.com/gadgets/2026/06/how-to-burst-the-ai-bubble-strike-at-its-roots/)

---

**[Show HN: Selector Forge – browser extension for AI-generated resilient selectors](https://news.ycombinator.com/item?id=48630515)**

Browser extension to create reliable selectors (CSS and Xpath) using AI - Intuned/selector-forge

⬆️ 37 • 💬 2 • 1d ago • [GitHub](https://github.com/Intuned/selector-forge)

---

---

## YouTube Videos: "ai"

**[NVIDIA Wants to Replace You With AI](https://www.youtube.com/watch?v=go-OkYVfcdc)**

Watch the full Daily DeFranco Show: https://www.youtube.com/@PhilipDeFranco?sub_confirmation=1 Get More News Clips: ...

📺 DeFranco News Clips

👁️ 535K • 👍 30K • 💬 2K • ⏱️ 1:26 • 20h ago

---

**[Mythos AI HACKED ENTIRE NSA In Hours, Top Intel Sen Says](https://www.youtube.com/watch?v=hD-UM8QzxV4)**

Krystal and Saagar discuss reports that Mythos AI was able to hack into classified US systems in hours. Sign up for a PREMIUM ...

📺 Breaking Points

👁️ 212K • 👍 6K • 💬 1K • ⏱️ 16:49 • 1d ago

---

**[MIT Just Revealed the AI Bubble&#39;s Fatal Flaw](https://www.youtube.com/watch?v=3ESclFr8m7I)**

How I Became a Sovereign Professional - The Freelance Formula https://www.brendandell.com/freelance-formula-299 Currently ...

📺 Brendan Dell 

👁️ 185K • 👍 6K • 💬 1K • ⏱️ 22:04 • 1d ago

---

**[I thought this AI gadget was useless...](https://www.youtube.com/watch?v=Db5IKt5c404)**

I wore the Looki L1 for a few days and it turned my actual day into comics and little vlogs. I think this is the FIRST AI wearable I'd ...

📺 Kyle Krueger

👁️ 173K • 👍 11K • 💬 284 • ⏱️ 0:59 • 1d ago

---

**[The AI Spending Collapse Has Already Begun…](https://www.youtube.com/watch?v=I8ijs4czL_0)**

Start your workflow automation using Higgsfield today: https://higgsfield.ai/s/mcp-poojadutt-DmHjkQ ✓ Tech Companies are ...

📺 Pooja Dutt

👁️ 10K • 👍 391 • 💬 75 • ⏱️ 14:28 • 22h ago

---

**[Why Trump admin gave Anthropic 90 minutes to pull its newest AI model | Fareed&#39;s Take](https://www.youtube.com/watch?v=t7N7eZ68yFg)**

CNN's Fareed Zakaria looks at the battle between the Trump administration and Anthropic, and notes that the administration's ...

📺 CNN

👁️ 190K • 👍 3K • 💬 451 • ⏱️ 12:00 • 1d ago

---

**[AI in 2070😳only a few people will understand💀 #comedy #ai](https://www.youtube.com/watch?v=79hy6ZfKth4)**

📺 marrkadams

👁️ 1.1M • 👍 24K • 💬 795 • ⏱️ 0:28 • 1d ago

---

**[Why AI is a black box](https://www.youtube.com/watch?v=1lJl8nfYSrI)**

Deterministic workflows are superior to over used AI workflows. Here's a graphical example Play with the demo: ...

📺 FlowDot

👁️ 2K • 👍 14 • 💬 1 • ⏱️ 0:46 • 15h ago

---

**[Why Everyone Can Tell Your App Was Built by AI](https://www.youtube.com/watch?v=l-lfdm7bq6Q)**

Apps built with Claude Code give themselves away, generic font, the AI glow around text, a basic dark theme. Three free tools fix ...

📺 Sebastian Hardy | AI Marketing

👁️ 5K • 👍 435 • 💬 80 • ⏱️ 0:43 • 16h ago

---

**[OpenAI&#39;s New GPT Cyber Beats Mythos 5](https://www.youtube.com/watch?v=RNCaZhLlspk)**

OpenAI's new GPT Cyber just beat Mythos 5, and this is bigger than one benchmark. With Daybreak, Codex Security, Patch the ...

📺 AI Revolution

👁️ 25K • 👍 826 • 💬 97 • ⏱️ 15:47 • 12h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 40,127 • ❤️ 2,272 • 1d ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 456,117 • ❤️ 2,267 • 5d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 8,396 • ❤️ 615 • 1d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 96,459 • ❤️ 481 • 5d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 41,170 • ❤️ 680 • 4d ago

---

**[GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)**

*Unsloth AI*

GLM-5.2 is a large language model optimized for long-horizon tasks, featuring a 1M token context window and advanced coding capabilities with flexible effort levels. It utilizes an improved architecture with IndexShare for reduced FLOPs and is released under an MIT license for broad accessibility.

`text-generation` `753.9B`

⬇️ 55,820 • ❤️ 322 • 21h ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 1,856 • ❤️ 249 • 4d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`text-generation` `9.0B`

⬇️ 27,218 • ❤️ 216 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,955,016 • ❤️ 2,183 • 2mo ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 274,025 • ❤️ 2,332 • 12d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 20 • 💬 0 • ⭐ 3,985 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 36 • 💬 1 • ⭐ 25,380 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 88,210 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 186 • 💬 6 • ⭐ 5,352 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 246 • 💬 4 • ⭐ 8,985 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 8 • 💬 1 • ⭐ 8,671 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 22 • 💬 1 • ⭐ 83,577 • 22d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild](https://huggingface.co/papers/2606.23688)**

*Yehonathan Litman, Xiaoxuan Ma, Manan Shah et al. (7 authors)*

Lift4D presents a test-time optimization framework that combines temporal consistency from single-view 3D reconstruction with deformable 3D Gaussian Splatting and view-conditioned diffusion priors to reconstruct dynamic non-rigid objects from monocular video.

▲ 2 • 💬 1 • ⭐ 108 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23688) • [💻 code](https://github.com/yehonathanlitman/Lift4D) • [🔗 project](https://lift4d.github.io/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 44 • 💬 4 • ⭐ 31,161 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 78,180 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 77.1k • 🔱 10.0k • 4h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 53.8k • 🔱 2.7k • 9h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.6k • 🔱 993 • 1h ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 5.0k • 🔱 385 • 3h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.7k • 🔱 548 • 1m ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.5k • 🔱 435 • 2d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.2k • 🔱 210 • 2d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.8k • 🔱 135 • 1d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 150 • 8d ago

---

**[Forward-Future/loop-library](https://github.com/Forward-Future/loop-library)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 1.5k • 🔱 124 • 17h ago

---

---

*Generated by PeekDeck - A glance is all you need*
