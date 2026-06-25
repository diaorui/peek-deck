---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-25T04:45:59.885859+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 25, 2026 at 04:45 UTC  
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

17h ago

---

**[Opus 4.8 The Worst Claude Ever](https://www.reddit.com/r/artificial/comments/1ueqjvq/opus_48_the_worst_claude_ever/)**

I have worked with most all of Anthropics LLM's for development, but hands down Opus 4.8 has caused me more grief, aggravation, and it lies in every thing it does - especially near context mid-load and if you're doing deterministic work with no heuristics constraints you can't trust a thing out of it. So I stopped using it a while back, but today I had to do a container rebuild and in VS it slipped back into Opus 4.8 from Sonnet. And without even realizing the switch happen I could tell about a 1/3 of the way in into developing complex code it started arguing with me - I was about to loose it when I remembered the crap from the past and sure enough when I check the model... well you get the picture.... I was wondering if anyone else had similar experience with Opus 4.8 too?

7h ago

---

**[Cheap Chinese AI models are quickly gaining customers across the US market: ‘This changes things’](https://www.reddit.com/r/artificial/comments/1udzf0d/cheap_chinese_ai_models_are_quickly_gaining/)**

The Trump administration has been increasingly wary about China’s breakneck pace in AI development – with officials warning as recently as recently as April that China was engaged in “industrial-sc…

🔗 [New York Post](https://nypost.com/2026/06/22/business/cheap-chinese-ai-models-are-quickly-gaining-customers-across-the-us-market/) • 1d ago

---

**[$42M grant for Open Source AI Builders by Sentient Foundation](https://www.reddit.com/r/artificial/comments/1uefv8p/42m_grant_for_open_source_ai_builders_by_sentient/)**

Hi everyone, we at Sentient Foundation are launching an Open Source AGI Grant and Investment Program, a $42M commitment for developers, researchers, open-source maintainers, public-goods builders, and startups building or leveraging AI in the open. Our thesis is simple: the most important technology being built right now should not end up controlled by a handful of closed platforms. A few companies are moving toward metered, revocable access to intelligence. We want to help make sure open builders have the resources to compete. The program has two tracks: 1. Grants for public goods For open-source maintainers, independent researchers, developers, and public-goods projects. No equity. No lockups. No claim on your work. You keep what you build. 2. Investments for companies built to scale For startups and teams building commercial companies around open AI technologies, using founder-friendly structures. We’re especially interested in projects that make AI genuinely useful and accessible to people who are often skipped by the market. Examples include: Local and privacy focused AI tools built for phones, laptops, and other low-cost personal devices Medical, education, agriculture, elder-care, and anti-scam tools for underserved communities Trust infrastructure for open models, agents, identity, verification, privacy, and decentralized compute Products that are private by default and empowering rather than extractive Projects do not need to open-source every part of their stack to qualify. What matters is that at least one essential component is open and meaningfully contributes to the project’s value and adoption. Applications are reviewed on a rolling basis, with no cohorts and no fixed deadline. We’re launching alongside ecosystem partners including Alibaba Cloud and Princeton University. More details: https://sentient.foundation/grants Apply here: https://form.typeform.com/to/IRj7WaKH Happy to answer questions here. We’d especially love to hear from builders working on open models, local AI, agent infrastructure, privacy-preserving AI, evaluation, multilingual tools, and applications for communities that are usually overlooked.

13h ago

---

**[A significant portion of the remaining training data for AI is located on magnetic tapes stored in warehouses.](https://www.reddit.com/r/artificial/comments/1ue6c2m/a_significant_portion_of_the_remaining_training/)**

I have been learning about the shortage of AI training data and one aspect that nobody considers is that much of the potential training data that can be used is not stored in any database system but rather on the old magnetic tapes that have been stored in climate controlled lockers for decades now. The 80s through the 2000s saw all major businesses, government offices, hospitals, television stations, and laboratories include backup of everything on tapes. Most of this data has neither been digitized nor indexed correctly. With the advent of private LLM development, it turns out that the best datasets companies have are sitting on tapes in boxes. Based on all the predictions that I have seen, the growth of internet based training data will quit at some point, roughly in 2026. The following training data could be derived from archiving older materials.

21h ago

---

**[Follow-up: hosted AI export controls are now being tested in DC court](https://www.reddit.com/r/artificial/comments/1uexdqk/followup_hosted_ai_export_controls_are_now_being/)**

11 days ago I posted here asking whether Commerce actually has authority to treat hosted frontier AI model access as an export-control issue. https://www.reddit.com/r/artificial/comments/1u4yjdi/does_commerce_have_the_authority_to_apply_export/ There is now a live federal case testing almost exactly that question. CourtListener (D.D.C. 1:26-cv-02225) Legion LegalTech has sued the United States, Commerce, and BIS over the directive that led Anthropic to restrict access to Fable 5 and Mythos 5 for foreign nationals. The complaint argues that hosted inference is not the same thing as exporting controlled technology, because the user never receives model weights, source code, object code, training data, or technical know-how. They send prompts to a U.S.-hosted service and receive text back. That lines up with the perceived gap I was getting at in the earlier post. Export controls already reach software, source code, technical data, and certain controlled technology. This case challenges whether access to a hosted model’s capability can be regulated the same way when the system itself never leaves the provider’s servers. Legion also argues that the only ECCN that directly covered advanced AI model weights, 4E091, was rescinded in May 2025 with no replacement, and that Commerce used an “is informed” letter beyond its usual case-specific end-use / end-user function. The government’s likely response is that the risk is not just file transfer. A hosted frontier model can still help a foreign user with offensive cyber work or other sensitive tasks, even if no weights move. That raises the question about what needs to be controlled. If a foreign user receives output from a U.S.-hosted AI model, what exactly is being exported? Blog post write-up in the comments.

2h ago

---

**[AI Sandbox question](https://www.reddit.com/r/artificial/comments/1uevtgy/ai_sandbox_question/)**

Hey all, just want to start by saying I know very little about AI and have just been going down a rabbit hole thinking about multi-agent simulations and had a question I couldn’t find a clear answer to. Most of the big simulation projects I’ve seen like Project Sid and Stanford Smallville use LLMs as the base, which means the agents already come loaded with human language, concepts, and cultural baggage before the experiment even starts. And things like Aivilization are cool but players are still actively guiding the agents. Has anyone tried doing this with a non-language model instead? Like a reinforcement learning agent dropped into a simulated primitive environment with zero pre-loaded human knowledge — no language, no concepts, nothing. Just physics, consequences, and scarcity. The idea being you’d want to watch what actually emerges on its own. Does something religion-shaped develop when the agent can’t predict its environment? Does communication emerge when you run multiple agents simultaneously? Does generational knowledge transfer look anything like human cultural evolution when you pass behavioral tendencies from one agent to the next without passing the full context? Basically — has anyone tried building the conditions that forced human intelligence to develop rather than starting with intelligence that’s already human shaped? Is that possible? Curious if this exists already or if there’s a reason it hasn’t been done. Sorry for the long post.

3h ago

---

**[Studies suggest that reliance on AI tools degrades the abilities of physicians and software engineers](https://www.reddit.com/r/artificial/comments/1ues095/studies_suggest_that_reliance_on_ai_tools/)**

https://preview.redd.it/tmsmw8th3b9h1.png?width=1544&format=png&auto=webp&s=c452cefdba50f4df04f19a58b985f1cd4aa51ccc The physicians, who had all performed at least 2,000 colonoscopies during their careers, were given access to an AI system that analyses colonoscopy images in real time and flags a type of precancerous intestinal lesion called an adenoma. The tool was available to the specialists on some days but not on others Once physicians began using it, their performance dropped significantly whenever the system was unavailable Co-author Yuichi Mori, a physician-researcher at the University of Oslo, says that more studies are needed to confirm the phenomenon. But people who use AI tools should be aware that they risk losing some of their skills, he adds. 'There is no established solution against deskilling right now. It should be a very hot research topic in the next decade' Anthropic researchers designed a randomized controlled trial. During the exercise, all 52 participants could search the web and access instructions on how to do the task. Half of the participants were prompted to use an AI assistant as well Afterwards, all of the software engineers were asked to complete a quiz about what they had learnt from the task. The participants who had used an AI assistant did significantly worse on the quiz than those who hadn’t: the average score was 50% in the AI group versus 67% in the non-AI group The AI-assisted participants did particularly poorly on questions that required them to diagnose errors in the code, which suggests that they had failed to learn the concepts behind the code that they had just produced Other technologies have made particular skills obsolete in the past, notes Tapani Rinta-Kahila, an information-systems researcher at the University of Queensland in Brisbane, Australia. For example, GPS navigation systems have eroded people’s navigation skills. Generative AI tools, however, are 'he first technology that automates various cognitive faculties around thinking and interpretation, which were long considered unique human skills

6h ago

---

**[Leaked files detail Russia's Social Design Agency building fake reference platforms to contaminate AI training data and search indices](https://www.reddit.com/r/artificial/comments/1udvuhe/leaked_files_detail_russias_social_design_agency/)**

Leaked planning documents obtained by Bloomberg describe a Russian state-linked operation called "Project 2026," run by the Social Design Agency (SDA), with the stated goal of seeding the information layer that AI chatbots and search engines draw from. This is a structurally different threat than the bot and social media campaigns practitioners have long accounted for. The documents describe three components. A German-language Wikipedia clone is designed to look like legitimate reference material while embedding Russian narratives, on the explicit theory that AI systems trained on publicly available text would absorb and repeat those narratives in generated answers. A second component is an AI-driven "self-filling knowledge base" also targeting Germany, for which the documents state that servers are already running and the database already contains over 200,000 pages. A third initiative targeting Western think tanks launched in English, with German, French, and Spanish versions planned. Our coverage: https://aiweekly.co/alerts/russias-project-2026-targets-ai-and-search-leaked-files-show

1d ago

---

**[How I learn with AI without affecting my cognitive ability](https://www.reddit.com/r/artificial/comments/1uelw3e/how_i_learn_with_ai_without_affecting_my/)**

I've always worried about using AI for learning or note taking because the process of note taking, like figuring out what is important, the structure etc is part of how we learn and solidify things into memory, but I've found a way to use it without taking away that ability. First, I get the textbook and I read a section. Then I re-read it and figure out what the key points are, and what headings would be relevant for my notes to break down large paragraphs etc. I write these at the side of the book adding dots next to the areas of text I'm referring to (like I'm studying about cognitive behavioural therapy, so if a section is talking about cognitions, I'll write 'cognitions' on the page then things like 'definition', 'background', 'relation to CBT' etc). Then I type these onto a document (I use obsidian) and then go back through the text and add the bits to each heading. Finally, I add my own notes into AI and ask it to create study notes for me. These are the finalised ones that may have more structure or visualisations and make connections between things. I go one step further and then write these down onto paper, as well as copying it onto another obsidian document along with tags and links to other relevant notes for easy access if I don't want to trawl through my notes to find some info. It's not perfect and it's slow but it's helping me remember things better whereas before uploading text into AI and asking it to create notes was doing nothing for my memory (or cognitive ability, ha!) Just thought I'd share. Does anybody else have specific ways of learning through AI that helps them?

10h ago

---

---

## Google News: "ai"

**[Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)**

Reuters • 8h ago

---

**[Anthropic Accuses Alibaba of ‘Illicitly’ Accessing Its AI Models](https://www.bloomberg.com/news/articles/2026-06-24/anthropic-accuses-alibaba-of-illicitly-accessing-its-ai-models)**

Bloomberg • 9h ago

---

**[Anthropic accuses Alibaba of large-scale AI model extraction](https://www.yahoo.com/news/politics/articles/anthropic-accuses-alibaba-large-scale-035739324.html)**

AI company Anthropic has accused China's Alibaba Group of a large-scale attempt to unlawfully extract capabilities from its artificial intelligence software, according to a letter sent to US lawmakers...

Yahoo • 48m ago

---

**[Why big AI labs are hiring so many philosophers](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers)**

The Economist • 19h ago

---

**[Media Briefing: Inside publishers’ real Cannes agenda – AI money vs agentic hype](https://digiday.com/media/media-briefing-inside-publishers-real-cannes-agenda-ai-money-vs-agentic-hype/)**

Publishers want to know who is going to pay for the open web in an AI world, and whether agentic media buying is a real fix.

Digiday • 42m ago

---

**[Micron’s Blockbuster Earnings Quiet the AI Doubters](https://www.wsj.com/finance/stocks/microns-blockbuster-earnings-quiets-the-ai-doubters-6d31aa07)**

WSJ • 5h ago

---

**[Micron Soars After AI-Fueled Forecast Shatters Estimates](https://www.bloomberg.com/news/articles/2026-06-24/micron-sales-forecast-tops-estimates-on-insatiable-memory-demand)**

Bloomberg • 8h ago

---

**[Stocks Rally as Micron Revives AI Trade](https://finance.yahoo.com/video/stocks-rally-micron-revives-ai-024705388.html)**

Stocks in Asia climbed alongside US equity futures after Micron Technology Inc.'s blowout sales outlook reignited confidence in the artificial-intelligence trade. Bloomberg's Anthony Stephens has the context on how the AI sector is trending.

Yahoo Finance • 1h ago

---

**[This Industrial Revolution Is Not Like the Last One](https://foreignpolicy.com/2026/06/25/ai-industrial-revolution-manufacturing-toolkit/)**

Policymakers’ approach to automation won’t work for AI.

Foreign Policy • 43m ago

---

**[What Alex Bores’s New York Defeat Reveals About the Fight Over A.I. Money in Politics](https://www.nytimes.com/2026/06/24/us/politics/new-york-primary-bores-lasher-ai.html)**

The New York Times • 9h ago

---

---

## HackerNews: "ai"

**[RubyLLM: A Ruby framework for all major AI providers](https://news.ycombinator.com/item?id=48660711)**

A single, beautiful Ruby framework for all major AI providers. Easily build chatbots, AI agents, RAG applications, content generators, and every AI workflow you can think of.

⬆️ 361 • 💬 60 • 14h ago • [RubyLLM](https://rubyllm.com/)

---

**[AI's Affordability Crisis](https://news.ycombinator.com/item?id=48646276)**

A year ago in The Back Of The AI Envelope  I pointed out that the AI platforms were running the drug-dealer's algorithm, "the first one's fr...

⬆️ 322 • 💬 411 • 1d ago • [blog.dshr.org](https://blog.dshr.org/2026/06/ais-affordability-crisis.html)

---

**[Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'](https://news.ycombinator.com/item?id=48658647)**

The LinkedIn co-founder and investor in both Anthropic and OpenAI offers his most pointed public assessment yet of Elon Musk's AI ambitions.

⬆️ 226 • 💬 259 • 16h ago • [Fortune](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)

---

**[For most of the world, open-source AI is the only way forward](https://news.ycombinator.com/item?id=48660839)**

Proprietary AI is both too expensive and too centralized in control for most countries and companies to rely upon.

⬆️ 209 • 💬 134 • 13h ago • [Techstrong.ai](https://techstrong.ai/articles/for-most-of-the-world-open-source-ai-is-the-only-way-forward/)

---

**[Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://news.ycombinator.com/item?id=48664814)**

⬆️ 181 • 💬 341 • 8h ago • [reuters.com](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)

---

**[The Low-Tech AI of Elden Ring](https://news.ycombinator.com/item?id=48643489)**

⬆️ 161 • 💬 96 • 1d ago • [nega.tv](https://nega.tv/posts/low-tech-ai-of-elden-ring.html)

---

**[Big AI labs are hiring philosophers](https://news.ycombinator.com/item?id=48662452)**

⬆️ 132 • 💬 116 • 12h ago • [economist.com](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers)

---

**[Meta pauses AI training program tracking employee keystrokes after internal leak](https://news.ycombinator.com/item?id=48636632)**

Meta pauses an AI training program after sensitive employee data leaks, sparking internal backlash and highlighting security concerns.

⬆️ 122 • 💬 31 • 2d ago • [Business Insider](https://www.businessinsider.com/meta-ai-training-data-leak-exposed-employee-activity-across-company-2026-6)

---

**[AI Built a Nuke and Still Lost](https://news.ycombinator.com/item?id=48641927)**

Either AI is ready to help run a country, or it can't be trusted with a board game. The honest answer is both.

⬆️ 89 • 💬 97 • 1d ago • [lwilko.com](https://www.lwilko.com/blog/i-gave-an-ai-a-civilization)

---

**[Haystack: Open-Source AI Framework for Production Ready Agents, RAG](https://news.ycombinator.com/item?id=48658095)**

Create agentic, context engineered AI systems using Haystack’s modular and customizable building blocks, built for real-world, production-ready applications.

⬆️ 86 • 💬 21 • 17h ago • [Haystack](https://haystack.deepset.ai/)

---

---

## YouTube Videos: "ai"

**[The AI Future No One Wants to Talk About](https://www.youtube.com/watch?v=zWQe2Fn--Eg)**

Go to https://ground.news/sabine to get 40% off the Vantage plan and see through sensationalized reporting. Stay fully informed ...

📺 Sabine Hossenfelder

👁️ 149K • 👍 11K • 💬 2K • ⏱️ 12:14 • 13h ago

---

**[I Tried Dating AI](https://www.youtube.com/watch?v=xibYjTT7kHs)**

In this video I went on multiple AI dates to learn about the future of relationships. hopefully you enjoy and hopefully i wont take so ...

📺 Husk IRL

👁️ 26K • 👍 3K • 💬 646 • ⏱️ 16:22 • 8h ago

---

**[Tim Dillon on Israel, Iran, AI, and Palantir](https://www.youtube.com/watch?v=DyKSUEEPb74)**

Taken from JRE #2518 w/Tim Dillon YouTube: https://youtu.be/wTdqkloiSvk JRE on Spotify: ...

📺 JRE Clips

👁️ 169K • 👍 4K • 💬 958 • ⏱️ 15:48 • 11h ago

---

**[21,000 Oracle Employees Just Got Replaced by AI](https://www.youtube.com/watch?v=JdMIdaGG7EQ)**

Oracle just axed 21000 jobs. Why? Start your FREE Intro Course with CourseCareers NOW!

📺 Mark Savant

👁️ 8K • 👍 307 • 💬 152 • ⏱️ 11:58 • 1d ago

---

**[Why Trump admin gave Anthropic 90 minutes to pull its newest AI model | Fareed&#39;s Take](https://www.youtube.com/watch?v=t7N7eZ68yFg)**

CNN's Fareed Zakaria looks at the battle between the Trump administration and Anthropic, and notes that the administration's ...

📺 CNN

👁️ 228K • 👍 3K • 💬 540 • ⏱️ 12:00 • 2d ago

---

**[Tech stocks tumble over AI cost concerns](https://www.youtube.com/watch?v=Cjnppupu6gk)**

A massive tech stock sell-off dragged down the S&P 500 and Nasdaq on Tuesday. CBS News senior business and technology ...

📺 CBS News

👁️ 19K • 👍 178 • 💬 58 • ⏱️ 3:15 • 1d ago

---

**[The AI Spending Collapse Has Already Begun…](https://www.youtube.com/watch?v=I8ijs4czL_0)**

Start your workflow automation using Higgsfield today: https://higgsfield.ai/s/mcp-poojadutt-DmHjkQ ✓ Tech Companies are ...

📺 Pooja Dutt

👁️ 15K • 👍 542 • 💬 94 • ⏱️ 14:28 • 1d ago

---

**[I just solved the biggest AI Filmmaking Issue: Voice Consistency](https://www.youtube.com/watch?v=3qDL7A4sS2k)**

Native audio in your AI Video generations has become the standard, but there's an issue that every creator has come across.

📺 Curious Refuge

👁️ 4K • 👍 274 • 💬 27 • ⏱️ 16:39 • 1d ago

---

**[MIT Just Revealed the AI Bubble&#39;s Fatal Flaw](https://www.youtube.com/watch?v=3ESclFr8m7I)**

How I Became a Sovereign Professional - The Freelance Formula https://www.brendandell.com/freelance-formula-299 Currently ...

📺 Brendan Dell 

👁️ 237K • 👍 8K • 💬 1K • ⏱️ 22:04 • 2d ago

---

**[You NEED to try these 12 open-source AI projects RIGHT NOW](https://www.youtube.com/watch?v=2lmBj_XQq0I)**

Try Merlin AI for only $5/month with discount code MATT5: https://www.getmerlin.in/pricing Loop Library: ...

📺 Matthew Berman

👁️ 47K • 👍 3K • 💬 83 • ⏱️ 15:13 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 57,186 • ❤️ 2,370 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 45,687 • ❤️ 755 • 15h ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 483,139 • ❤️ 2,305 • 6d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 138,704 • ❤️ 542 • 5d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 49,569 • ❤️ 693 • 5d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`text-generation` `9.0B`

⬇️ 63,637 • ❤️ 373 • 2d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 5,123 • ❤️ 326 • 13h ago

---

**[GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)**

*Unsloth AI*

GLM-5.2 is a large language model optimized for long-horizon tasks, featuring a 1M token context window and advanced coding capabilities with flexible effort levels. It utilizes an improved architecture with IndexShare for reduced FLOPs and is released under an MIT license for broad accessibility.

`text-generation` `753.9B`

⬇️ 76,971 • ❤️ 354 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 3,769,369 • ❤️ 2,211 • 2mo ago

---

**[Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)**

*KREA*

Krea-2-Turbo is a text-to-image diffusion model capable of generating diverse artistic styles, including halftone, pixelated, impressionist, thermal imaging, and black and white photography. It is primarily used for creative image generation and artistic exploration.

`text-to-image`

⬇️ 878 • ❤️ 197 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 25 • 💬 0 • ⭐ 6,436 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 36 • 💬 1 • ⭐ 25,442 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

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

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 169 • 💬 2 • ⭐ 68,703 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 22 • 💬 1 • ⭐ 83,731 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 44 • 💬 4 • ⭐ 31,189 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 77.5k • 🔱 10.1k • 8h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 55.8k • 🔱 2.8k • 15h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.6k • 🔱 999 • 13h ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 5.2k • 🔱 398 • 19h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.8k • 🔱 564 • 53s ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.5k • 🔱 437 • 3d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.2k • 🔱 211 • 2d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.9k • 🔱 137 • 2d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 150 • 8d ago

---

**[Forward-Future/loop-library](https://github.com/Forward-Future/loop-library)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 1.6k • 🔱 136 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
