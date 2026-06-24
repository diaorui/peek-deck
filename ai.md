---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-24T15:18:50.714172+00:00'
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

**Last Updated:** June 24, 2026 at 15:18 UTC  
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

**[We chased a hallucinated quote through 30k training records, 4,600 transcripts, and our own system prompt. Turned out to be two separate bugs](https://www.reddit.com/r/artificial/comments/1ueaya4/we_chased_a_hallucinated_quote_through_30k/)**

Some of our customers noticed Inter-1 (our omni-modal social-signal model) would occasionally "hear" a quote that didn't exist. Feed it a video with zero audio and ask what was said, and it would sometimes report: "Yeah, Friday at five." Verbatim. Same line, every time. We assumed it had to be baked into the training data somewhere, so we went looking everywhere: 30,960 training records with datetime mentions → zero hits on the phrase 4,603 video transcripts → zero hits ~800 inference probes, 584 storage objects → zero hits Turns out the phrase was sitting in our own system prompt — a worked example we'd written to show the model the expected output format, buried in a version our GEPA prompt-optimizer had shipped. But that only explained where the words came from, not why the model would say them over total silence. So we ran two ablations in our internal eval harness: Swap the word, keep the model: changed the prompt's example to "Tuesday at noon." Fabrication rate went up (37%→50%), and the invented quote tracked the swap exactly — Friday→Tuesday. Swap the model, keep the prompt: ran the same byte-identical prompt through larger variants and an earlier checkpoint of our own model. They barely fabricated (0–2%). Only the further-post-trained Inter-1 confabulated at ~12%. So it's not one bug, it's two stacked priors: the prompt supplied the script, but post-training is what gave the model the compulsion to recite something rather than report silence. Deleting the prompt example stops that one sentence — it doesn't stop the model from inventing different dialogue instead. We think this is a textual/in-context variant of the audio-visual "Clever Hans effect" that's been documented for vision priors (model writes "thud" over a silent skateboard wipeout) — except ours shows the same reflex gets worded by whatever's nearest in the context window, which a vision-only diagnostic wouldn't catch. Full writeup with the fabrication-rate forest plot and log data: https://www.interhuman.ai/blog/goblin-yeah-friday-at-five

3h ago

---

**[Cheap Chinese AI models are quickly gaining customers across the US market: ‘This changes things’](https://www.reddit.com/r/artificial/comments/1udzf0d/cheap_chinese_ai_models_are_quickly_gaining/)**

The Trump administration has been increasingly wary about China’s breakneck pace in AI development – with officials warning as recently as recently as April that China was engaged in “industrial-sc…

🔗 [New York Post](https://nypost.com/2026/06/22/business/cheap-chinese-ai-models-are-quickly-gaining-customers-across-the-us-market/) • 14h ago

---

**[A significant portion of the remaining training data for AI is located on magnetic tapes stored in warehouses.](https://www.reddit.com/r/artificial/comments/1ue6c2m/a_significant_portion_of_the_remaining_training/)**

I have been learning about the shortage of AI training data and one aspect that nobody considers is that much of the potential training data that can be used is not stored in any database system but rather on the old magnetic tapes that have been stored in climate controlled lockers for decades now. The 80s through the 2000s saw all major businesses, government offices, hospitals, television stations, and laboratories include backup of everything on tapes. Most of this data has neither been digitized nor indexed correctly. With the advent of private LLM development, it turns out that the best datasets companies have are sitting on tapes in boxes. Based on all the predictions that I have seen, the growth of internet based training data will quit at some point, roughly in 2026. The following training data could be derived from archiving older materials.

8h ago

---

**[$42M grant for Open Source AI Builders by Sentient Foundation](https://www.reddit.com/r/artificial/comments/1uefv8p/42m_grant_for_open_source_ai_builders_by_sentient/)**

Hi everyone, we at Sentient Foundation are launching an Open Source AGI Grant and Investment Program, a $42M commitment for developers, researchers, open-source maintainers, public-goods builders, and startups building or leveraging AI in the open. Our thesis is simple: the most important technology being built right now should not end up controlled by a handful of closed platforms. A few companies are moving toward metered, revocable access to intelligence. We want to help make sure open builders have the resources to compete. The program has two tracks: 1. Grants for public goods For open-source maintainers, independent researchers, developers, and public-goods projects. No equity. No lockups. No claim on your work. You keep what you build. 2. Investments for companies built to scale For startups and teams building commercial companies around open AI technologies, using founder-friendly structures. We’re especially interested in projects that make AI genuinely useful and accessible to people who are often skipped by the market. Examples include: Local and privacy focused AI tools built for phones, laptops, and other low-cost personal devices Medical, education, agriculture, elder-care, and anti-scam tools for underserved communities Trust infrastructure for open models, agents, identity, verification, privacy, and decentralized compute Products that are private by default and empowering rather than extractive Projects do not need to open-source every part of their stack to qualify. What matters is that at least one essential component is open and meaningfully contributes to the project’s value and adoption. Applications are reviewed on a rolling basis, with no cohorts and no fixed deadline. We’re launching alongside ecosystem partners including Alibaba Cloud, Franklin Templeton, Princeton University, and the Indian Institute of Science. More details: https://sentient.foundation/grants Apply here: https://form.typeform.com/to/IRj7WaKH Happy to answer questions here. We’d especially love to hear from builders working on open models, local AI, agent infrastructure, privacy-preserving AI, evaluation, multilingual tools, and applications for communities that are usually overlooked.

20m ago

---

**[Leaked files detail Russia's Social Design Agency building fake reference platforms to contaminate AI training data and search indices](https://www.reddit.com/r/artificial/comments/1udvuhe/leaked_files_detail_russias_social_design_agency/)**

Leaked planning documents obtained by Bloomberg describe a Russian state-linked operation called "Project 2026," run by the Social Design Agency (SDA), with the stated goal of seeding the information layer that AI chatbots and search engines draw from. This is a structurally different threat than the bot and social media campaigns practitioners have long accounted for. The documents describe three components. A German-language Wikipedia clone is designed to look like legitimate reference material while embedding Russian narratives, on the explicit theory that AI systems trained on publicly available text would absorb and repeat those narratives in generated answers. A second component is an AI-driven "self-filling knowledge base" also targeting Germany, for which the documents state that servers are already running and the database already contains over 200,000 pages. A third initiative targeting Western think tanks launched in English, with German, French, and Spanish versions planned. Our coverage: https://aiweekly.co/alerts/russias-project-2026-targets-ai-and-search-leaked-files-show

16h ago

---

**[🚀 Open AI Unveils More Advanced AI Models Capable of Longer Reasoning and Better Task Execution](https://www.reddit.com/r/artificial/comments/1uecd4f/open_ai_unveils_more_advanced_ai_models_capable/)**

AI development seems to be accelerating faster than ever. OpenAI recently introduced new AI models with improved reasoning, coding, and research capabilities, allowing them to handle more complex tasks while maintaining better accuracy. Many experts believe these advances could significantly impact industries like software development, market research, customer support, education, and content creation. At the same time, discussions around job displacement, AI regulation, and responsible deployment continue to grow. What do you think? Will AI become a productivity tool or a job replacement? Which industries do you think will be affected the most over the next 5 years? Interested to hear everyone's thoughts.

2h ago

---

**[Two lawyers just got sanctioned by a federal appeals court for filing AI made up cases](https://www.reddit.com/r/artificial/comments/1uec7x3/two_lawyers_just_got_sanctioned_by_a_federal/)**

Saw the Reuters piece from earlier this month and it stuck with me. A US appeals court sanctioned two lawyers for filing briefs full of cases that do not exist, the kind that came out of a chatbot. The court called it a lack of candor, which is the polite version. What gets me is this is not the first time and clearly not the last. There is a whole database tracking these now, over a thousand entries. The pattern is always the same. The model writes something that reads like a real citation, the lawyer does not check it, the filing goes in, and somewhere downstream a judge or opposing counsel actually looks it up and the whole thing collapses. By then the damage to the lawyer is done. What people keep missing is that asking the model to double check itself does not help. The same blind spot that invented the case is the one doing the review. It will confidently confirm its own fiction. I have been poking at this from the research side and the only setup that actually catches it is when the verification is done by something that did not write the answer in the first place, a separate pass with fresh sources. There are a couple of systems built around that idea now, apodex is the one I keep seeing cited because it makes the verifier a different agent team from the one that reasoned, but the principle matters more than the brand. If the checker shares context with the writer you are back to self grading. For anyone in a regulated field the practical lesson is boring. Treat every citation a model hands you as unverified until a human or an independent check confirms it exists and says what the model claims. The sanctions are not going to slow down, the tools are getting faster and the courts are getting less patient.

2h ago

---

**[How can GraphRAG be imputed with a traditional Rag?](https://www.reddit.com/r/artificial/comments/1ue9gqd/how_can_graphrag_be_imputed_with_a_traditional_rag/)**

Hi everyone, I've been reading about this, especially about what LazyGraphRAG does, but it only works for complex questions. Therefore, my idea is to combine it with traditional RAG to ask both complex and simple questions with equal accuracy, but I don't know how to implement it. Is anyone doing something similar? Any ideas? Does anyone have experience with this?

5h ago

---

**[The CEO of a company with 700,000 delivery workers just said robots will replace all of them](https://www.reddit.com/r/artificial/comments/1udvvef/the_ceo_of_a_company_with_700000_delivery_workers/)**

Saw this on Computerworld today and i've been thinking about it since Founder of JD.com said robots will replace all 700,000 of their delivery workers. Didn't sugarcoat it, didn't give a timeline, just said it's coming What got me was he also said he doesn't want his workers going hungry because of it, and their solution is retraining some of them to fix the robots taking their jobs. 700,000 is a lot of people to just figure it out Do you guys think this is actually as close as they're making it sound

16h ago

---

**[Looking for a technical co-founder [R]](https://www.reddit.com/r/artificial/comments/1uegdp2/looking_for_a_technical_cofounder_r/)**

I'm building VentureLync, an AI operating system for venture capital funds. Three agents: Analyst, Associate, Operations. Running on a persistent memory layer. Doing the actual work that junior VC staff do today: sourcing, diligence, portfolio monitoring, LP reporting. Where we are: design partners already signed, more funds in active conversations looking to come on board. The product exists, funds are using it, and we're closing more. What I need on the technical side is someone who thinks seriously about agentic systems. Not wrappers. Real orchestration: multi-agent memory, reliable tool use, context that doesn't break across handoffs. The hard problem underneath the product is making agents actually trustworthy at the task level, not just impressive in demos. That's the problem I want a co-founder to own. One thing I care about specifically: the AI space is shifting fast. New models, new paradigms, new capabilities dropping every few months. I need someone who stays on top of it instinctively, not as a hobby, but because they can't help it. Someone who sees a new architecture paper or a new model release and immediately thinks about what it means for what we're building. What I'm not looking for: Someone who wants to "explore AI." Someone who's juggling this alongside other work. No moonlighters, no freelancers treating this as a side project. And not someone who wants the co-founder title for the resume. If you're not ready to go all in, this isn't for you. Preferably based in Bangalore. In-person matters. If you've built something real with agentic systems, have opinions about what's broken, and want to work on a problem with a clear wedge in a market that's just starting to move, let's talk. DM me or drop a comment. I respond to everyone who has something real to say.

2m ago

---

---

## Google News: "ai"

**[Stanford was their golden ticket - could AI help or hinder that?](https://www.bbc.com/news/articles/c872j82j2qyo)**

The BBC spoke with Stanford University graduates about what they really think about artificial intelligence.

BBC • 16h ago

---

**[‘You can’t make billions without hurting people’: Cory Doctorow on Elon Musk, the AI bubble and bosses’ cruel fantasies](https://www.theguardian.com/technology/2026/jun/24/cory-doctorow-on-elon-musk-ai-bubble-bosses-cruel-fantasies)**

The writer who coined the word ‘enshittification’ tells us why AI will never deliver what it promises – and why it still appeals so much to those in power

The Guardian • 6h ago

---

**[Axios House: The one thing AI can't make – something real](https://www.axios.com/2026/06/24/axios-house-the-one-thing-ai-cant-make-something-real)**

Axios • 14m ago

---

**[Intelligence agencies warn AI will soon overcome current defenses](https://www.cnn.com/2026/06/24/business/video/ai-warning-duffy-live-ctw-062409aseg2-cnni-technology-fast?cid=external-feeds_iluminar_google)**

International intelligence agencies are warning AI models are advancing so quickly, they could overwhelm government and business defenses in just months. Clare Duffy tells us who is most at risk.

CNN • 36m ago

---

**[OpenAI reveals its first AI processor: Jalapeño](https://www.theverge.com/ai-artificial-intelligence/955939/openai-reveals-its-first-ai-processor-jalapeno)**

OpenAI’s first chip could help decrease its reliance on Nvidia.

The Verge • 42m ago

---

**[Big Tech's $2.7 trillion AI bill comes due: Chart of the Day](https://finance.yahoo.com/markets/article/big-techs-27-trillion-ai-bill-comes-due-chart-of-the-day-100000100.html)**

The “Magnificent Seven” plus Broadcom and Oracle have lost roughly $2.7 trillion in market value in June, according to Yahoo Finance analysis, as investors take a harder look at the companies funding the AI build-out.

Yahoo Finance • 5h ago

---

**[A Solution to A.I.’s Growing Power Demand: Homes](https://www.nytimes.com/2026/06/24/business/energy-environment/ai-data-centers-tesla.html)**

The New York Times • 6h ago

---

**[Reid Hoffman: SpaceX is 'not an AI company,' xAI is a 'train wreck'—and room for OpenAI, Anthropic](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)**

The LinkedIn co-founder and investor in both Anthropic and OpenAI offers his most pointed public assessment yet of Elon Musk's AI ambitions.

Fortune • 6h ago

---

**[Are ChatGPT and other AI chatbots politically biased? We tested them.](https://www.washingtonpost.com/technology/interactive/2026/06/24/are-ai-chatbots-like-chatgpt-politically-biased-we-tested-them/)**

The Post tested ChatGPT, Gemini and other chatbots with political questions, and the results show that the AI tools have different political leanings.

The Washington Post • 16m ago

---

**[As AI Companies Race for Power, Amazon and Google Have the Lead](https://www.wsj.com/business/energy-oil/as-ai-companies-race-for-power-amazon-and-google-have-the-lead-1d97af9a)**

WSJ • 5h ago

---

---

## HackerNews: "ai"

**[Apertus – Open Foundation Model for Sovereign AI](https://news.ycombinator.com/item?id=48622778)**

Fully Open Foundation Model for Sovereign AI

⬆️ 531 • 💬 182 • 2d ago • [apertvs.ai](https://apertvs.ai/)

---

**[AI's Affordability Crisis](https://news.ycombinator.com/item?id=48646276)**

A year ago in The Back Of The AI Envelope  I pointed out that the AI platforms were running the drug-dealer's algorithm, "the first one's fr...

⬆️ 307 • 💬 399 • 1d ago • [blog.dshr.org](https://blog.dshr.org/2026/06/ais-affordability-crisis.html)

---

**[Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'](https://news.ycombinator.com/item?id=48658647)**

The LinkedIn co-founder and investor in both Anthropic and OpenAI offers his most pointed public assessment yet of Elon Musk's AI ambitions.

⬆️ 164 • 💬 179 • 2h ago • [Fortune](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)

---

**[The Low-Tech AI of Elden Ring](https://news.ycombinator.com/item?id=48643489)**

⬆️ 155 • 💬 93 • 1d ago • [nega.tv](https://nega.tv/posts/low-tech-ai-of-elden-ring.html)

---

**[Meta pauses AI training program tracking employee keystrokes after internal leak](https://news.ycombinator.com/item?id=48636632)**

Meta pauses an AI training program after sensitive employee data leaks, sparking internal backlash and highlighting security concerns.

⬆️ 122 • 💬 31 • 1d ago • [Business Insider](https://www.businessinsider.com/meta-ai-training-data-leak-exposed-employee-activity-across-company-2026-6)

---

**[AI Built a Nuke and Still Lost](https://news.ycombinator.com/item?id=48641927)**

Either AI is ready to help run a country, or it can't be trusted with a board game. The honest answer is both.

⬆️ 87 • 💬 96 • 1d ago • [lwilko.com](https://www.lwilko.com/blog/i-gave-an-ai-a-civilization)

---

**[AI has already killed academia as we know it?](https://news.ycombinator.com/item?id=48634966)**

No AI was used in writing this post.

If academia was a game, I've won it. Tenure, an endowed research chair, awards, leadership positions, an international journal I helped to found and now serve as the Editor-in-Chief, students I have supervised to their own successes, a good

⬆️ 69 • 💬 51 • 1d ago • [Truths and Loves](https://truths-and-loves.ghost.io/ai-has-already-killed-academia-as-we-know-it/)

---

**[How to burst the AI bubble: Strike at its roots](https://news.ycombinator.com/item?id=48657518)**

Sci-fi author/tech journalist Cory Doctorow on his new book, The Reverse Centaur's Guide to Life After AI.

⬆️ 55 • 💬 44 • 5h ago • [Ars Technica](https://arstechnica.com/gadgets/2026/06/how-to-burst-the-ai-bubble-strike-at-its-roots/)

---

**[US AI stock sell-off shakes markets from Wall Street to Asia](https://news.ycombinator.com/item?id=48654795)**

Losses spread globally as investors questioned soaring valuations and spending on AI infrastructure

⬆️ 49 • 💬 37 • 11h ago • [the Guardian](https://www.theguardian.com/business/2026/jun/23/ai-stocks-sell-off-us-markets)

---

**[Tech Workers Are Fighting Against Silicon Valley's AI Push](https://news.ycombinator.com/item?id=48623695)**

More tech workers are organizing to fight back as they feel they are losing influence over decisions that affect their jobs, writes Varsha Bansal.

⬆️ 46 • 💬 14 • 2d ago • [Tech Policy Press](https://www.techpolicy.press/tech-workers-are-fighting-against-silicon-valleys-ai-push/)

---

---

## YouTube Videos: "ai"

**[Buy the AI economy they say](https://www.youtube.com/watch?v=wcV9lgv10yE)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 35K • 👍 2K • 💬 660 • ⏱️ 15:38 • 12h ago

---

**[Why Trump admin gave Anthropic 90 minutes to pull its newest AI model | Fareed&#39;s Take](https://www.youtube.com/watch?v=t7N7eZ68yFg)**

CNN's Fareed Zakaria looks at the battle between the Trump administration and Anthropic, and notes that the administration's ...

📺 CNN

👁️ 196K • 👍 3K • 💬 484 • ⏱️ 12:00 • 1d ago

---

**[21,000 Oracle Employees Just Got Replaced by AI](https://www.youtube.com/watch?v=JdMIdaGG7EQ)**

Oracle just axed 21000 jobs. Why? Start your FREE Intro Course with CourseCareers NOW!

📺 Mark Savant

👁️ 6K • 👍 271 • 💬 113 • ⏱️ 11:58 • 19h ago

---

**[The AI Spending Collapse Has Already Begun…](https://www.youtube.com/watch?v=I8ijs4czL_0)**

Start your workflow automation using Higgsfield today: https://higgsfield.ai/s/mcp-poojadutt-DmHjkQ ✓ Tech Companies are ...

📺 Pooja Dutt

👁️ 12K • 👍 440 • 💬 80 • ⏱️ 14:28 • 1d ago

---

**[MIT Just Revealed the AI Bubble&#39;s Fatal Flaw](https://www.youtube.com/watch?v=3ESclFr8m7I)**

How I Became a Sovereign Professional - The Freelance Formula https://www.brendandell.com/freelance-formula-299 Currently ...

📺 Brendan Dell 

👁️ 197K • 👍 7K • 💬 1K • ⏱️ 22:04 • 1d ago

---

**[Mythos AI HACKED ENTIRE NSA In Hours, Top Intel Sen Says](https://www.youtube.com/watch?v=hD-UM8QzxV4)**

Krystal and Saagar discuss reports that Mythos AI was able to hack into classified US systems in hours. Sign up for a PREMIUM ...

📺 Breaking Points

👁️ 215K • 👍 6K • 💬 1K • ⏱️ 16:49 • 1d ago

---

**[AI Surveillance Is Creating Two Classes of Humans](https://www.youtube.com/watch?v=k7JWIhJG5Xw)**

Empower your critical thinking and get the full picture on every story. Subscribe through my link https://ground.news/afterskool to ...

📺 After Skool

👁️ 61K • 👍 3K • 💬 579 • ⏱️ 11:11 • 23h ago

---

**[DeepSeek Just Solved AI&#39;s Billion Dollar Problem](https://www.youtube.com/watch?v=mG4SmhWyeFA)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The paper is available here: ...

📺 Two Minute Papers

👁️ 181K • 👍 9K • 💬 633 • ⏱️ 5:50 • 1d ago

---

**[Open AI Is In Deep Trouble](https://www.youtube.com/watch?v=MNO8i68HWe4)**

Live-streamed on June 16, 2026. Ed Zitron, publisher of the Where's Your Ed At? newsletter and host of the Better Offline podcast, ...

📺 The Majority Report w/ Sam Seder

👁️ 189K • 👍 6K • 💬 979 • ⏱️ 19:30 • 2d ago

---

**[NVIDIA Wants to Replace You With AI](https://www.youtube.com/watch?v=go-OkYVfcdc)**

Watch the full Daily DeFranco Show: https://www.youtube.com/@PhilipDeFranco?sub_confirmation=1 Get More News Clips: ...

📺 DeFranco News Clips

👁️ 580K • 👍 32K • 💬 2K • ⏱️ 1:26 • 23h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 57,186 • ❤️ 2,297 • 1d ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 483,139 • ❤️ 2,275 • 5d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 45,687 • ❤️ 657 • 2h ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 138,704 • ❤️ 494 • 5d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 49,569 • ❤️ 684 • 4d ago

---

**[GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)**

*Unsloth AI*

GLM-5.2 is a large language model optimized for long-horizon tasks, featuring a 1M token context window and advanced coding capabilities with flexible effort levels. It utilizes an improved architecture with IndexShare for reduced FLOPs and is released under an MIT license for broad accessibility.

`text-generation` `753.9B`

⬇️ 76,971 • ❤️ 333 • 1d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`text-generation` `9.0B`

⬇️ 63,637 • ❤️ 277 • 2d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 5,123 • ❤️ 274 • 5d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,769,369 • ❤️ 2,190 • 2mo ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 359,498 • ❤️ 2,333 • 12d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 22 • 💬 0 • ⭐ 5,572 • 2d ago

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

▲ 102 • 💬 4 • ⭐ 88,332 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 246 • 💬 4 • ⭐ 9,102 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 186 • 💬 6 • ⭐ 5,352 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

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

**[MemGUI-Agent: An End-to-End Long-Horizon Mobile GUI Agent with Proactive Context Management](https://huggingface.co/papers/2606.19926)**

*Guangyi Liu, Gao Wu, Congxiao Liu et al. (10 authors)*

🏢 kwai

MemGUI-Agent addresses long-horizon mobile GUI task limitations through proactive context management using Context-as-Action (ConAct) to maintain critical information across extended sequences.

▲ 31 • 💬 1 • ⭐ 53 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2606.19926) • [💻 code](https://github.com/kwai/MemGUI-Agent) • [🔗 project](https://memgui-agent.github.io/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 77.2k • 🔱 10.0k • 28m ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 54.3k • 🔱 2.7k • 1h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.6k • 🔱 995 • 8m ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 5.1k • 🔱 388 • 6h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.7k • 🔱 550 • 3m ago

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

⭐ 1.9k • 🔱 135 • 1d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 150 • 8d ago

---

**[Forward-Future/loop-library](https://github.com/Forward-Future/loop-library)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 1.6k • 🔱 127 • 20h ago

---

---

*Generated by PeekDeck - A glance is all you need*
