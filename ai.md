---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-25T00:14:21.807596+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 25, 2026 at 00:14 UTC  
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

12h ago

---

**[Opus 4.8 The Worst Claude Ever](https://www.reddit.com/r/artificial/comments/1ueqjvq/opus_48_the_worst_claude_ever/)**

I have worked with most all of Anthropics LLM's for development, but hands down Opus 4.8 has caused me more grief, aggravation, and it lies in every thing it does - especially near context mid-load and if you're doing deterministic work with no heuristics constraints you can't trust a thing out of it. So I stopped using it a while back, but today I had to do a container rebuild and in VS it slipped back into Opus 4.8 from Sonnet. And without even realizing the switch happen I could tell about a 1/3 of the way in into developing complex code it started arguing with me - I was about to loose it when I remembered the crap from the past and sure enough when I check the model... well you get the picture.... I was wondering if anyone else had similar experience with Opus 4.8 too?

2h ago

---

**[Cheap Chinese AI models are quickly gaining customers across the US market: ‘This changes things’](https://www.reddit.com/r/artificial/comments/1udzf0d/cheap_chinese_ai_models_are_quickly_gaining/)**

The Trump administration has been increasingly wary about China’s breakneck pace in AI development – with officials warning as recently as recently as April that China was engaged in “industrial-sc…

🔗 [New York Post](https://nypost.com/2026/06/22/business/cheap-chinese-ai-models-are-quickly-gaining-customers-across-the-us-market/) • 23h ago

---

**[$42M grant for Open Source AI Builders by Sentient Foundation](https://www.reddit.com/r/artificial/comments/1uefv8p/42m_grant_for_open_source_ai_builders_by_sentient/)**

Hi everyone, we at Sentient Foundation are launching an Open Source AGI Grant and Investment Program, a $42M commitment for developers, researchers, open-source maintainers, public-goods builders, and startups building or leveraging AI in the open. Our thesis is simple: the most important technology being built right now should not end up controlled by a handful of closed platforms. A few companies are moving toward metered, revocable access to intelligence. We want to help make sure open builders have the resources to compete. The program has two tracks: 1. Grants for public goods For open-source maintainers, independent researchers, developers, and public-goods projects. No equity. No lockups. No claim on your work. You keep what you build. 2. Investments for companies built to scale For startups and teams building commercial companies around open AI technologies, using founder-friendly structures. We’re especially interested in projects that make AI genuinely useful and accessible to people who are often skipped by the market. Examples include: Local and privacy focused AI tools built for phones, laptops, and other low-cost personal devices Medical, education, agriculture, elder-care, and anti-scam tools for underserved communities Trust infrastructure for open models, agents, identity, verification, privacy, and decentralized compute Products that are private by default and empowering rather than extractive Projects do not need to open-source every part of their stack to qualify. What matters is that at least one essential component is open and meaningfully contributes to the project’s value and adoption. Applications are reviewed on a rolling basis, with no cohorts and no fixed deadline. We’re launching alongside ecosystem partners including Alibaba Cloud and Princeton University. More details: https://sentient.foundation/grants Apply here: https://form.typeform.com/to/IRj7WaKH Happy to answer questions here. We’d especially love to hear from builders working on open models, local AI, agent infrastructure, privacy-preserving AI, evaluation, multilingual tools, and applications for communities that are usually overlooked.

9h ago

---

**[A significant portion of the remaining training data for AI is located on magnetic tapes stored in warehouses.](https://www.reddit.com/r/artificial/comments/1ue6c2m/a_significant_portion_of_the_remaining_training/)**

I have been learning about the shortage of AI training data and one aspect that nobody considers is that much of the potential training data that can be used is not stored in any database system but rather on the old magnetic tapes that have been stored in climate controlled lockers for decades now. The 80s through the 2000s saw all major businesses, government offices, hospitals, television stations, and laboratories include backup of everything on tapes. Most of this data has neither been digitized nor indexed correctly. With the advent of private LLM development, it turns out that the best datasets companies have are sitting on tapes in boxes. Based on all the predictions that I have seen, the growth of internet based training data will quit at some point, roughly in 2026. The following training data could be derived from archiving older materials.

17h ago

---

**[Studies suggest that reliance on AI tools degrades the abilities of physicians and software engineers](https://www.reddit.com/r/artificial/comments/1ues095/studies_suggest_that_reliance_on_ai_tools/)**

https://preview.redd.it/tmsmw8th3b9h1.png?width=1544&format=png&auto=webp&s=c452cefdba50f4df04f19a58b985f1cd4aa51ccc The physicians, who had all performed at least 2,000 colonoscopies during their careers, were given access to an AI system that analyses colonoscopy images in real time and flags a type of precancerous intestinal lesion called an adenoma. The tool was available to the specialists on some days but not on others Once physicians began using it, their performance dropped significantly whenever the system was unavailable Co-author Yuichi Mori, a physician-researcher at the University of Oslo, says that more studies are needed to confirm the phenomenon. But people who use AI tools should be aware that they risk losing some of their skills, he adds. 'There is no established solution against deskilling right now. It should be a very hot research topic in the next decade' Anthropic researchers designed a randomized controlled trial. During the exercise, all 52 participants could search the web and access instructions on how to do the task. Half of the participants were prompted to use an AI assistant as well Afterwards, all of the software engineers were asked to complete a quiz about what they had learnt from the task. The participants who had used an AI assistant did significantly worse on the quiz than those who hadn’t: the average score was 50% in the AI group versus 67% in the non-AI group The AI-assisted participants did particularly poorly on questions that required them to diagnose errors in the code, which suggests that they had failed to learn the concepts behind the code that they had just produced Other technologies have made particular skills obsolete in the past, notes Tapani Rinta-Kahila, an information-systems researcher at the University of Queensland in Brisbane, Australia. For example, GPS navigation systems have eroded people’s navigation skills. Generative AI tools, however, are 'he first technology that automates various cognitive faculties around thinking and interpretation, which were long considered unique human skills

1h ago

---

**[How I learn with AI without affecting my cognitive ability](https://www.reddit.com/r/artificial/comments/1uelw3e/how_i_learn_with_ai_without_affecting_my/)**

I've always worried about using AI for learning or note taking because the process of note taking, like figuring out what is important, the structure etc is part of how we learn and solidify things into memory, but I've found a way to use it without taking away that ability. First, I get the textbook and I read a section. Then I re-read it and figure out what the key points are, and what headings would be relevant for my notes to break down large paragraphs etc. I write these at the side of the book adding dots next to the areas of text I'm referring to (like I'm studying about cognitive behavioural therapy, so if a section is talking about cognitions, I'll write 'cognitions' on the page then things like 'definition', 'background', 'relation to CBT' etc). Then I type these onto a document (I use obsidian) and then go back through the text and add the bits to each heading. Finally, I add my own notes into AI and ask it to create study notes for me. These are the finalised ones that may have more structure or visualisations and make connections between things. I go one step further and then write these down onto paper, as well as copying it onto another obsidian document along with tags and links to other relevant notes for easy access if I don't want to trawl through my notes to find some info. It's not perfect and it's slow but it's helping me remember things better whereas before uploading text into AI and asking it to create notes was doing nothing for my memory (or cognitive ability, ha!) Just thought I'd share. Does anybody else have specific ways of learning through AI that helps them?

5h ago

---

**[Leaked files detail Russia's Social Design Agency building fake reference platforms to contaminate AI training data and search indices](https://www.reddit.com/r/artificial/comments/1udvuhe/leaked_files_detail_russias_social_design_agency/)**

Leaked planning documents obtained by Bloomberg describe a Russian state-linked operation called "Project 2026," run by the Social Design Agency (SDA), with the stated goal of seeding the information layer that AI chatbots and search engines draw from. This is a structurally different threat than the bot and social media campaigns practitioners have long accounted for. The documents describe three components. A German-language Wikipedia clone is designed to look like legitimate reference material while embedding Russian narratives, on the explicit theory that AI systems trained on publicly available text would absorb and repeat those narratives in generated answers. A second component is an AI-driven "self-filling knowledge base" also targeting Germany, for which the documents state that servers are already running and the database already contains over 200,000 pages. A third initiative targeting Western think tanks launched in English, with German, French, and Spanish versions planned. Our coverage: https://aiweekly.co/alerts/russias-project-2026-targets-ai-and-search-leaked-files-show

1d ago

---

**[How distinct are all these new corporate "AI agents" under the hood?](https://www.reddit.com/r/artificial/comments/1uem62s/how_distinct_are_all_these_new_corporate_ai/)**

I see AI agents everywhere now, from Instacart to Confluence to banking apps, and I was curious to know how they actually work behind the scenes. Are they mostly built on the exact same underlying models, or does each company code their own? If multiple companies use the same model, what stops them from acting exactly the same? Also, do they all benefit when the base model gets updated in the case they are running isolated versions? I'd love to know if they share any of the same training data or if each company's system is kept completely separate to what extent.

5h ago

---

**[Two lawyers just got sanctioned by a federal appeals court for filing AI made up cases](https://www.reddit.com/r/artificial/comments/1uec7x3/two_lawyers_just_got_sanctioned_by_a_federal/)**

Saw the Reuters piece from earlier this month and it stuck with me. A US appeals court sanctioned two lawyers for filing briefs full of cases that do not exist, the kind that came out of a chatbot. The court called it a lack of candor, which is the polite version. What gets me is this is not the first time and clearly not the last. There is a whole database tracking these now, over a thousand entries. The pattern is always the same. The model writes something that reads like a real citation, the lawyer does not check it, the filing goes in, and somewhere downstream a judge or opposing counsel actually looks it up and the whole thing collapses. By then the damage to the lawyer is done. What people keep missing is that asking the model to double check itself does not help. The same blind spot that invented the case is the one doing the review. It will confidently confirm its own fiction. I have been poking at this from the research side and the only setup that actually catches it is when the verification is done by something that did not write the answer in the first place, a separate pass with fresh sources. There are a couple of systems built around that idea now, apodex is the one I keep seeing cited because it makes the verifier a different agent team from the one that reasoned, but the principle matters more than the brand. If the checker shares context with the writer you are back to self grading. For anyone in a regulated field the practical lesson is boring. Treat every citation a model hands you as unverified until a human or an independent check confirms it exists and says what the model claims. The sanctions are not going to slow down, the tools are getting faster and the courts are getting less patient.

11h ago

---

---

## Google News: "ai"

**[Why big AI labs are hiring so many philosophers](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers)**

The Economist • 14h ago

---

**[Qualcomm to buy startup Modular for $4 billion in AI software push](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/)**

Reuters • 8h ago

---

**[Qualcomm debuts line of AI data center chips and systems, increasing competition with Nvidia](https://finance.yahoo.com/technology/article/qualcomm-debuts-line-of-ai-data-center-chips-and-systems-increasing-competition-with-nvidia-193000684.html)**

Qualcomm is increasing its line of AI data center products as it looks to grow its share of the market.

Yahoo Finance • 4h ago

---

**[Qualcomm Lays Out New Data Center Roadmap For AI; Meta Buys It](https://www.forbes.com/sites/karlfreund/2026/06/24/qualcomm-lays-out-new-data-center-roadmap-for-ai-meta-buys-it/)**

Qualcomm revealed its ambitious data center roadmap at Investor Day, securing a pivotal multi-year agreement with Meta to deploy its advanced technologies.

Forbes • 31m ago

---

**[Micron’s Blockbuster Earnings Quiet the AI Doubters](https://www.wsj.com/finance/stocks/microns-blockbuster-earnings-quiets-the-ai-doubters-6d31aa07)**

WSJ • 1h ago

---

**[Micron Stock Soars as Results Blow Past Wall Street Expectations Amid Booming AI Demand](https://www.investopedia.com/micron-earnings-q3-fy2026-memory-stock-soars-ai-demand-12006096)**

Micron shares popped in extended trading Wednesday after the memory chip maker posted earnings that soared past analysts' estimates, thanks to AI-driven demand.

Investopedia • 2h ago

---

**[Micron and Qualcomm forecasts ignite $400 billion AI chip stock rally](https://finance.yahoo.com/technology/ai/articles/micron-qualcomm-forecasts-ignite-400-230933990.html)**

At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rates that help you manage your financial life.

Yahoo Finance • 1h ago

---

**[Are ChatGPT and other AI chatbots politically biased? We tested them.](https://www.washingtonpost.com/technology/interactive/2026/06/24/are-ai-chatbots-like-chatgpt-politically-biased-we-tested-them/)**

The Post tested ChatGPT, Gemini and other chatbots with political questions, and the results show that the AI tools have different political leanings.

The Washington Post • 8h ago

---

**[Senators revive push for AI labels](https://www.politico.com/live-updates/2026/06/24/congress/senate-revives-push-for-ai-labels-00974818)**

Politico • 55m ago

---

**[Anthropic accuses Alibaba of campaign to 'brazenly' and 'illicitly' extract AI capabilities](https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html)**

The letter, which was obtained by CNBC, claims Alibaba carried out "the largest known distillation attack on Anthropic to date."

CNBC • 2h ago

---

---

## HackerNews: "ai"

**[RubyLLM: A Ruby framework for all major AI providers](https://news.ycombinator.com/item?id=48660711)**

A single, beautiful Ruby framework for all major AI providers. Easily build chatbots, AI agents, RAG applications, content generators, and every AI workflow you can think of.

⬆️ 333 • 💬 51 • 9h ago • [RubyLLM](https://rubyllm.com/)

---

**[AI's Affordability Crisis](https://news.ycombinator.com/item?id=48646276)**

A year ago in The Back Of The AI Envelope  I pointed out that the AI platforms were running the drug-dealer's algorithm, "the first one's fr...

⬆️ 321 • 💬 410 • 1d ago • [blog.dshr.org](https://blog.dshr.org/2026/06/ais-affordability-crisis.html)

---

**[Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'](https://news.ycombinator.com/item?id=48658647)**

The LinkedIn co-founder and investor in both Anthropic and OpenAI offers his most pointed public assessment yet of Elon Musk's AI ambitions.

⬆️ 220 • 💬 257 • 11h ago • [Fortune](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)

---

**[For Most of the World, Open-Source AI Is the Only Way Forward](https://news.ycombinator.com/item?id=48660839)**

Proprietary AI is both too expensive and too centralized in control for most countries and companies to rely upon.

⬆️ 196 • 💬 131 • 9h ago • [Techstrong.ai](https://techstrong.ai/articles/for-most-of-the-world-open-source-ai-is-the-only-way-forward/)

---

**[The Low-Tech AI of Elden Ring](https://news.ycombinator.com/item?id=48643489)**

⬆️ 159 • 💬 96 • 1d ago • [nega.tv](https://nega.tv/posts/low-tech-ai-of-elden-ring.html)

---

**[Meta pauses AI training program tracking employee keystrokes after internal leak](https://news.ycombinator.com/item?id=48636632)**

Meta pauses an AI training program after sensitive employee data leaks, sparking internal backlash and highlighting security concerns.

⬆️ 122 • 💬 31 • 2d ago • [Business Insider](https://www.businessinsider.com/meta-ai-training-data-leak-exposed-employee-activity-across-company-2026-6)

---

**[Big AI labs are hiring philosophers](https://news.ycombinator.com/item?id=48662452)**

⬆️ 113 • 💬 104 • 7h ago • [economist.com](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers)

---

**[AI Built a Nuke and Still Lost](https://news.ycombinator.com/item?id=48641927)**

Either AI is ready to help run a country, or it can't be trusted with a board game. The honest answer is both.

⬆️ 89 • 💬 97 • 1d ago • [lwilko.com](https://www.lwilko.com/blog/i-gave-an-ai-a-civilization)

---

**[Haystack: Open-Source AI Framework for Production Ready Agents, RAG](https://news.ycombinator.com/item?id=48658095)**

Create agentic, context engineered AI systems using Haystack’s modular and customizable building blocks, built for real-world, production-ready applications.

⬆️ 85 • 💬 21 • 12h ago • [Haystack](https://haystack.deepset.ai/)

---

**[AI has already killed academia as we know it?](https://news.ycombinator.com/item?id=48634966)**

No AI was used in writing this post.

If academia was a game, I've won it. Tenure, an endowed research chair, awards, leadership positions, an international journal I helped to found and now serve as the Editor-in-Chief, students I have supervised to their own successes, a good

⬆️ 69 • 💬 52 • 2d ago • [Truths and Loves](https://truths-and-loves.ghost.io/ai-has-already-killed-academia-as-we-know-it/)

---

---

## YouTube Videos: "ai"

**[The AI Future No One Wants to Talk About](https://www.youtube.com/watch?v=zWQe2Fn--Eg)**

Go to https://ground.news/sabine to get 40% off the Vantage plan and see through sensationalized reporting. Stay fully informed ...

📺 Sabine Hossenfelder

👁️ 110K • 👍 9K • 💬 2K • ⏱️ 12:14 • 9h ago

---

**[We Asked AI To Simulate If The U.S. Had A Second Civil War](https://www.youtube.com/watch?v=OdxH1KZbjOY)**

What would happen if Civil War broke out in the United States again in 2026? Thankfully, with modern AI technology, we no ...

📺 The Babylon Bee

👁️ 120K • 👍 15K • 💬 2K • ⏱️ 2:31 • 1d ago

---

**[21,000 Oracle Employees Just Got Replaced by AI](https://www.youtube.com/watch?v=JdMIdaGG7EQ)**

Oracle just axed 21000 jobs. Why? Start your FREE Intro Course with CourseCareers NOW!

📺 Mark Savant

👁️ 7K • 👍 299 • 💬 118 • ⏱️ 11:58 • 1d ago

---

**[Why Trump admin gave Anthropic 90 minutes to pull its newest AI model | Fareed&#39;s Take](https://www.youtube.com/watch?v=t7N7eZ68yFg)**

CNN's Fareed Zakaria looks at the battle between the Trump administration and Anthropic, and notes that the administration's ...

📺 CNN

👁️ 222K • 👍 3K • 💬 527 • ⏱️ 12:00 • 2d ago

---

**[The AI Spending Collapse Has Already Begun…](https://www.youtube.com/watch?v=I8ijs4czL_0)**

Start your workflow automation using Higgsfield today: https://higgsfield.ai/s/mcp-poojadutt-DmHjkQ ✓ Tech Companies are ...

📺 Pooja Dutt

👁️ 14K • 👍 507 • 💬 86 • ⏱️ 14:28 • 1d ago

---

**[Mythos AI HACKED ENTIRE NSA In Hours, Top Intel Sen Says](https://www.youtube.com/watch?v=hD-UM8QzxV4)**

Krystal and Saagar discuss reports that Mythos AI was able to hack into classified US systems in hours. Sign up for a PREMIUM ...

📺 Breaking Points

👁️ 224K • 👍 6K • 💬 1K • ⏱️ 16:49 • 2d ago

---

**[MIT Just Revealed the AI Bubble&#39;s Fatal Flaw](https://www.youtube.com/watch?v=3ESclFr8m7I)**

How I Became a Sovereign Professional - The Freelance Formula https://www.brendandell.com/freelance-formula-299 Currently ...

📺 Brendan Dell 

👁️ 226K • 👍 7K • 💬 1K • ⏱️ 22:04 • 2d ago

---

**[NVIDIA Wants to Replace You With AI](https://www.youtube.com/watch?v=go-OkYVfcdc)**

Watch the full Daily DeFranco Show: https://www.youtube.com/@PhilipDeFranco?sub_confirmation=1 Get More News Clips: ...

📺 DeFranco News Clips

👁️ 685K • 👍 36K • 💬 3K • ⏱️ 1:26 • 1d ago

---

**[AI was trained on my WHAT?!](https://www.youtube.com/watch?v=dh9aG-WkNu4)**

📺 Emily Hopkins

👁️ 342K • 👍 16K • 💬 185 • ⏱️ 0:28 • 1d ago

---

**[AI in 2070😳only a few people will understand💀 #comedy #ai](https://www.youtube.com/watch?v=79hy6ZfKth4)**

📺 marrkadams

👁️ 1.2M • 👍 26K • 💬 847 • ⏱️ 0:28 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 57,186 • ❤️ 2,351 • 1d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 45,687 • ❤️ 728 • 11h ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 483,139 • ❤️ 2,296 • 5d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 138,704 • ❤️ 530 • 5d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 49,569 • ❤️ 692 • 5d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`text-generation` `9.0B`

⬇️ 63,637 • ❤️ 345 • 2d ago

---

**[GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)**

*Unsloth AI*

GLM-5.2 is a large language model optimized for long-horizon tasks, featuring a 1M token context window and advanced coding capabilities with flexible effort levels. It utilizes an improved architecture with IndexShare for reduced FLOPs and is released under an MIT license for broad accessibility.

`text-generation` `753.9B`

⬇️ 76,971 • ❤️ 344 • 1d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 5,123 • ❤️ 307 • 8h ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,769,369 • ❤️ 2,204 • 2mo ago

---

**[Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)**

*KREA*

Krea-2-Turbo is a text-to-image diffusion model capable of generating diverse artistic styles, including halftone, pixelated, impressionist, thermal imaging, and black and white photography. It is primarily used for creative image generation and artistic exploration.

`text-to-image`

⬇️ 878 • ❤️ 187 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 24 • 💬 0 • ⭐ 5,572 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 36 • 💬 1 • ⭐ 25,442 • 32mo ago

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

▲ 186 • 💬 6 • ⭐ 5,402 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 8 • 💬 1 • ⭐ 8,761 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 22 • 💬 1 • ⭐ 83,669 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 169 • 💬 2 • ⭐ 68,703 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 60 • 💬 1 • ⭐ 83,866 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MemGUI-Agent: An End-to-End Long-Horizon Mobile GUI Agent with Proactive Context Management](https://huggingface.co/papers/2606.19926)**

*Guangyi Liu, Gao Wu, Congxiao Liu et al. (10 authors)*

🏢 kwai

MemGUI-Agent addresses long-horizon mobile GUI task limitations through proactive context management using Context-as-Action (ConAct) to maintain critical information across extended sequences.

▲ 33 • 💬 1 • ⭐ 53 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2606.19926) • [💻 code](https://github.com/kwai/MemGUI-Agent) • [🔗 project](https://memgui-agent.github.io/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 77.4k • 🔱 10.1k • 3h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 55.1k • 🔱 2.8k • 10h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.6k • 🔱 998 • 9h ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 5.2k • 🔱 397 • 15h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.7k • 🔱 557 • 6m ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.5k • 🔱 437 • 3d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.2k • 🔱 210 • 2d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.9k • 🔱 136 • 2d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 150 • 8d ago

---

**[Forward-Future/loop-library](https://github.com/Forward-Future/loop-library)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 1.6k • 🔱 132 • 21m ago

---

---

*Generated by PeekDeck - A glance is all you need*
