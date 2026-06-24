---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-24T21:10:33.664997+00:00'
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

**Last Updated:** June 24, 2026 at 21:10 UTC  
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

9h ago

---

**[Cheap Chinese AI models are quickly gaining customers across the US market: ‘This changes things’](https://www.reddit.com/r/artificial/comments/1udzf0d/cheap_chinese_ai_models_are_quickly_gaining/)**

The Trump administration has been increasingly wary about China’s breakneck pace in AI development – with officials warning as recently as recently as April that China was engaged in “industrial-sc…

🔗 [New York Post](https://nypost.com/2026/06/22/business/cheap-chinese-ai-models-are-quickly-gaining-customers-across-the-us-market/) • 19h ago

---

**[$42M grant for Open Source AI Builders by Sentient Foundation](https://www.reddit.com/r/artificial/comments/1uefv8p/42m_grant_for_open_source_ai_builders_by_sentient/)**

Hi everyone, we at Sentient Foundation are launching an Open Source AGI Grant and Investment Program, a $42M commitment for developers, researchers, open-source maintainers, public-goods builders, and startups building or leveraging AI in the open. Our thesis is simple: the most important technology being built right now should not end up controlled by a handful of closed platforms. A few companies are moving toward metered, revocable access to intelligence. We want to help make sure open builders have the resources to compete. The program has two tracks: 1. Grants for public goods For open-source maintainers, independent researchers, developers, and public-goods projects. No equity. No lockups. No claim on your work. You keep what you build. 2. Investments for companies built to scale For startups and teams building commercial companies around open AI technologies, using founder-friendly structures. We’re especially interested in projects that make AI genuinely useful and accessible to people who are often skipped by the market. Examples include: Local and privacy focused AI tools built for phones, laptops, and other low-cost personal devices Medical, education, agriculture, elder-care, and anti-scam tools for underserved communities Trust infrastructure for open models, agents, identity, verification, privacy, and decentralized compute Products that are private by default and empowering rather than extractive Projects do not need to open-source every part of their stack to qualify. What matters is that at least one essential component is open and meaningfully contributes to the project’s value and adoption. Applications are reviewed on a rolling basis, with no cohorts and no fixed deadline. We’re launching alongside ecosystem partners including Alibaba Cloud and Princeton University. More details: https://sentient.foundation/grants Apply here: https://form.typeform.com/to/IRj7WaKH Happy to answer questions here. We’d especially love to hear from builders working on open models, local AI, agent infrastructure, privacy-preserving AI, evaluation, multilingual tools, and applications for communities that are usually overlooked.

6h ago

---

**[A significant portion of the remaining training data for AI is located on magnetic tapes stored in warehouses.](https://www.reddit.com/r/artificial/comments/1ue6c2m/a_significant_portion_of_the_remaining_training/)**

I have been learning about the shortage of AI training data and one aspect that nobody considers is that much of the potential training data that can be used is not stored in any database system but rather on the old magnetic tapes that have been stored in climate controlled lockers for decades now. The 80s through the 2000s saw all major businesses, government offices, hospitals, television stations, and laboratories include backup of everything on tapes. Most of this data has neither been digitized nor indexed correctly. With the advent of private LLM development, it turns out that the best datasets companies have are sitting on tapes in boxes. Based on all the predictions that I have seen, the growth of internet based training data will quit at some point, roughly in 2026. The following training data could be derived from archiving older materials.

14h ago

---

**[How I learn with AI without affecting my cognitive ability](https://www.reddit.com/r/artificial/comments/1uelw3e/how_i_learn_with_ai_without_affecting_my/)**

I've always worried about using AI for learning or note taking because the process of note taking, like figuring out what is important, the structure etc is part of how we learn and solidify things into memory, but I've found a way to use it without taking away that ability. First, I get the textbook and I read a section. Then I re-read it and figure out what the key points are, and what headings would be relevant for my notes to break down large paragraphs etc. I write these at the side of the book adding dots next to the areas of text I'm referring to (like I'm studying about cognitive behavioural therapy, so if a section is talking about cognitions, I'll write 'cognitions' on the page then things like 'definition', 'background', 'relation to CBT' etc). Then I type these onto a document (I use obsidian) and then go back through the text and add the bits to each heading. Finally, I add my own notes into AI and ask it to create study notes for me. These are the finalised ones that may have more structure or visualisations and make connections between things. I go one step further and then write these down onto paper, as well as copying it onto another obsidian document along with tags and links to other relevant notes for easy access if I don't want to trawl through my notes to find some info. It's not perfect and it's slow but it's helping me remember things better whereas before uploading text into AI and asking it to create notes was doing nothing for my memory (or cognitive ability, ha!) Just thought I'd share. Does anybody else have specific ways of learning through AI that helps them?

2h ago

---

**[Leaked files detail Russia's Social Design Agency building fake reference platforms to contaminate AI training data and search indices](https://www.reddit.com/r/artificial/comments/1udvuhe/leaked_files_detail_russias_social_design_agency/)**

Leaked planning documents obtained by Bloomberg describe a Russian state-linked operation called "Project 2026," run by the Social Design Agency (SDA), with the stated goal of seeding the information layer that AI chatbots and search engines draw from. This is a structurally different threat than the bot and social media campaigns practitioners have long accounted for. The documents describe three components. A German-language Wikipedia clone is designed to look like legitimate reference material while embedding Russian narratives, on the explicit theory that AI systems trained on publicly available text would absorb and repeat those narratives in generated answers. A second component is an AI-driven "self-filling knowledge base" also targeting Germany, for which the documents state that servers are already running and the database already contains over 200,000 pages. A third initiative targeting Western think tanks launched in English, with German, French, and Spanish versions planned. Our coverage: https://aiweekly.co/alerts/russias-project-2026-targets-ai-and-search-leaked-files-show

22h ago

---

**[Two lawyers just got sanctioned by a federal appeals court for filing AI made up cases](https://www.reddit.com/r/artificial/comments/1uec7x3/two_lawyers_just_got_sanctioned_by_a_federal/)**

Saw the Reuters piece from earlier this month and it stuck with me. A US appeals court sanctioned two lawyers for filing briefs full of cases that do not exist, the kind that came out of a chatbot. The court called it a lack of candor, which is the polite version. What gets me is this is not the first time and clearly not the last. There is a whole database tracking these now, over a thousand entries. The pattern is always the same. The model writes something that reads like a real citation, the lawyer does not check it, the filing goes in, and somewhere downstream a judge or opposing counsel actually looks it up and the whole thing collapses. By then the damage to the lawyer is done. What people keep missing is that asking the model to double check itself does not help. The same blind spot that invented the case is the one doing the review. It will confidently confirm its own fiction. I have been poking at this from the research side and the only setup that actually catches it is when the verification is done by something that did not write the answer in the first place, a separate pass with fresh sources. There are a couple of systems built around that idea now, apodex is the one I keep seeing cited because it makes the verifier a different agent team from the one that reasoned, but the principle matters more than the brand. If the checker shares context with the writer you are back to self grading. For anyone in a regulated field the practical lesson is boring. Treat every citation a model hands you as unverified until a human or an independent check confirms it exists and says what the model claims. The sanctions are not going to slow down, the tools are getting faster and the courts are getting less patient.

8h ago

---

**[Idea](https://www.reddit.com/r/artificial/comments/1ueptsf/idea/)**

I made a challenge for ais to gather information abt me just by roblox user here stats: Google ai=got my reddit user by some posts and told my my posts Gemini=had hallucinations and told i played some games that i dont and he did told me he is sorry Chatgpt=told me i commented them some safety thing them i left it s mesage from google ai and him and gemini talked whit google ai by me

9m ago

---

**[is AI making content creation too easy and distribution the new bottleneck](https://www.reddit.com/r/artificial/comments/1ueo735/is_ai_making_content_creation_too_easy_and/)**

been thinking about this a lot lately. with all the AI tools available now, generating content has become almost trivially easy. blog posts, social captions, video scripts, email sequences, you can spin all of that up in minutes now. but here's what i keep noticing. the creation side got solved and now distribution is the part nobody has really figured out yet. you can produce 10x more content than before but getting it in front of the right people consistently is still just as hard if not harder. feels like AI optimized one half of the equation and left the other half exactly where it was. or am i missing something and people have actually cracked distribution too has AI genuinely changed distribution in a meaningful way or is it still mostly a manual grind once the content is actually made

1h ago

---

**[OpenAI Unveils Custom Chip It Designed With Broadcom to Boost Its AI Infrastructure](https://www.reddit.com/r/artificial/comments/1uegmmx/openai_unveils_custom_chip_it_designed_with/)**

OpenAI's engineers designed the chip, called Jalapeño, together with Broadcom to perform a specific AI task known as inference, during which data is crunched in order to answer a user's query to a chatbot like ChatGPT.

🔗 [money.usnews.com](https://money.usnews.com/investing/news/articles/2026-06-24/openai-unveils-custom-chip-it-designed-with-broadcom-to-boost-its-ai-infrastructure) • 5h ago

---

---

## Google News: "ai"

**[Even in Defeat, a Democrat Showed the Upside of Angering the A.I. Industry](https://www.nytimes.com/2026/06/24/us/politics/new-york-primary-bores-lasher-ai.html)**

The New York Times • 2h ago

---

**[Are ChatGPT and other AI chatbots politically biased? We tested them.](https://www.washingtonpost.com/technology/interactive/2026/06/24/are-ai-chatbots-like-chatgpt-politically-biased-we-tested-them/)**

The Post tested ChatGPT, Gemini and other chatbots with political questions, and the results show that the AI tools have different political leanings.

The Washington Post • 5h ago

---

**[N.S.A. Lost Access to Powerful A.I. Model Amid Anthropic Dispute](https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html)**

The New York Times • 23h ago

---

**[Google Poised to Lose Two More High-Profile AI Staffers to Anthropic](https://www.bloomberg.com/news/articles/2026-06-24/google-poised-to-lose-two-more-high-profile-ai-staffers-to-anthropic)**

Bloomberg.com • 2h ago

---

**[Anthropic sends Congress letter accusing Alibaba of illicitly accessing AI models](https://www.cnbc.com/video/2026/06/24/anthropic-sends-congress-letter-accusing-alibaba-of-ai-model-illicit-access.html)**

CNBC's Kate Rooney reports on Anthropic's letter to Congress accusing Alibaba of illicitly accessing AI models.

CNBC • 18m ago

---

**[Is AI Costing Drivers Money at the Gas Pump? According to This California Class Action Suit, It Is](https://www.caranddriver.com/news/a71709512/california-ai-gas-price-inflation-class-action/)**

One more reason for people to dislike and distrust AI.

Car and Driver • 1h ago

---

**[AI Is Helping Gas Stations Collude to Raise California Fuel Prices, Lawsuit Says](https://www.usnews.com/news/us/articles/2026-06-24/ai-is-helping-gas-stations-collude-to-raise-california-fuel-prices-lawsuit-says)**

A federal lawsuit accuses gas station operators in California of using AI-powered software to illegally collude and raise prices

U.S. News & World Report • 51m ago

---

**[California gas stations accused of using AI to inflate prices](https://www.wric.com/news/california-gas-stations-accused-of-using-ai-to-inflate-prices/)**

WRIC ABC 8News • 1h ago

---

**[A24 Knows You’re Mad About the Google AI Collab](https://www.wired.com/story/a24-knows-youre-mad-about-the-google-ai-collab/)**

Indie movie fans are upset about Google DeepMind’s $75 million investment in the studio, which comes as AI companies are deepening their influence in Hollywood.

WIRED • 5m ago

---

**[Stanford was their golden ticket - could AI help or hinder that?](https://www.bbc.com/news/articles/c872j82j2qyo)**

The BBC spoke with Stanford University graduates about what they really think about artificial intelligence.

BBC • 21h ago

---

---

## HackerNews: "ai"

**[Apertus – Open Foundation Model for Sovereign AI](https://news.ycombinator.com/item?id=48622778)**

Fully Open Foundation Model for Sovereign AI

⬆️ 532 • 💬 183 • 2d ago • [apertvs.ai](https://apertvs.ai/)

---

**[AI's Affordability Crisis](https://news.ycombinator.com/item?id=48646276)**

A year ago in The Back Of The AI Envelope  I pointed out that the AI platforms were running the drug-dealer's algorithm, "the first one's fr...

⬆️ 319 • 💬 406 • 1d ago • [blog.dshr.org](https://blog.dshr.org/2026/06/ais-affordability-crisis.html)

---

**[RubyLLM: A Ruby framework for all major AI providers](https://news.ycombinator.com/item?id=48660711)**

A single, beautiful Ruby framework for all major AI providers. Easily build chatbots, AI agents, RAG applications, content generators, and every AI workflow you can think of.

⬆️ 290 • 💬 45 • 6h ago • [RubyLLM](https://rubyllm.com/)

---

**[Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'](https://news.ycombinator.com/item?id=48658647)**

The LinkedIn co-founder and investor in both Anthropic and OpenAI offers his most pointed public assessment yet of Elon Musk's AI ambitions.

⬆️ 217 • 💬 253 • 8h ago • [Fortune](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)

---

**[For Most of the World, Open-Source AI Is the Only Way Forward](https://news.ycombinator.com/item?id=48660839)**

Proprietary AI is both too expensive and too centralized in control for most countries and companies to rely upon.

⬆️ 178 • 💬 117 • 6h ago • [Techstrong.ai](https://techstrong.ai/articles/for-most-of-the-world-open-source-ai-is-the-only-way-forward/)

---

**[The Low-Tech AI of Elden Ring](https://news.ycombinator.com/item?id=48643489)**

⬆️ 158 • 💬 96 • 1d ago • [nega.tv](https://nega.tv/posts/low-tech-ai-of-elden-ring.html)

---

**[Meta pauses AI training program tracking employee keystrokes after internal leak](https://news.ycombinator.com/item?id=48636632)**

Meta pauses an AI training program after sensitive employee data leaks, sparking internal backlash and highlighting security concerns.

⬆️ 122 • 💬 31 • 1d ago • [Business Insider](https://www.businessinsider.com/meta-ai-training-data-leak-exposed-employee-activity-across-company-2026-6)

---

**[AI Built a Nuke and Still Lost](https://news.ycombinator.com/item?id=48641927)**

Either AI is ready to help run a country, or it can't be trusted with a board game. The honest answer is both.

⬆️ 88 • 💬 97 • 1d ago • [lwilko.com](https://www.lwilko.com/blog/i-gave-an-ai-a-civilization)

---

**[Haystack: Open-Source AI Framework for Production Ready Agents, RAG](https://news.ycombinator.com/item?id=48658095)**

Create agentic, context engineered AI systems using Haystack’s modular and customizable building blocks, built for real-world, production-ready applications.

⬆️ 80 • 💬 21 • 9h ago • [Haystack](https://haystack.deepset.ai/)

---

**[Big AI labs are hiring philosophers](https://news.ycombinator.com/item?id=48662452)**

⬆️ 70 • 💬 51 • 4h ago • [economist.com](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers)

---

---

## YouTube Videos: "ai"

**[How To Make AI Videos - Prompting Guide For Beginners](https://www.youtube.com/watch?v=1JkmT6L2CmA)**

How To Start Making AI Video in 2026 Start Here: [https://higgsfield.ai?fpr=utm&fp_sid=mira Hey friends✨, today I'm showing you ...

📺 Mira AI

👁️ 2K • ⏱️ 10:07 • 2h ago

---

**[The AI Future No One Wants to Talk About](https://www.youtube.com/watch?v=zWQe2Fn--Eg)**

Go to https://ground.news/sabine to get 40% off the Vantage plan and see through sensationalized reporting. Stay fully informed ...

📺 Sabine Hossenfelder

👁️ 73K • 👍 7K • 💬 2K • ⏱️ 12:14 • 6h ago

---

**[Buy the AI economy they say](https://www.youtube.com/watch?v=wcV9lgv10yE)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 39K • 👍 3K • 💬 696 • ⏱️ 15:38 • 18h ago

---

**[21,000 Oracle Employees Just Got Replaced by AI](https://www.youtube.com/watch?v=JdMIdaGG7EQ)**

Oracle just axed 21000 jobs. Why? Start your FREE Intro Course with CourseCareers NOW!

📺 Mark Savant

👁️ 7K • 👍 288 • 💬 118 • ⏱️ 11:58 • 1d ago

---

**[Why Trump admin gave Anthropic 90 minutes to pull its newest AI model | Fareed&#39;s Take](https://www.youtube.com/watch?v=t7N7eZ68yFg)**

CNN's Fareed Zakaria looks at the battle between the Trump administration and Anthropic, and notes that the administration's ...

📺 CNN

👁️ 216K • 👍 3K • 💬 520 • ⏱️ 12:00 • 2d ago

---

**[We Asked AI To Simulate If The U.S. Had A Second Civil War](https://www.youtube.com/watch?v=OdxH1KZbjOY)**

What would happen if Civil War broke out in the United States again in 2026? Thankfully, with modern AI technology, we no ...

📺 The Babylon Bee

👁️ 103K • 👍 13K • 💬 1K • ⏱️ 2:31 • 1d ago

---

**[Mythos AI HACKED ENTIRE NSA In Hours, Top Intel Sen Says](https://www.youtube.com/watch?v=hD-UM8QzxV4)**

Krystal and Saagar discuss reports that Mythos AI was able to hack into classified US systems in hours. Sign up for a PREMIUM ...

📺 Breaking Points

👁️ 222K • 👍 6K • 💬 1K • ⏱️ 16:49 • 2d ago

---

**[MIT Just Revealed the AI Bubble&#39;s Fatal Flaw](https://www.youtube.com/watch?v=3ESclFr8m7I)**

How I Became a Sovereign Professional - The Freelance Formula https://www.brendandell.com/freelance-formula-299 Currently ...

📺 Brendan Dell 

👁️ 217K • 👍 7K • 💬 1K • ⏱️ 22:04 • 2d ago

---

**[The AI Spending Collapse Has Already Begun…](https://www.youtube.com/watch?v=I8ijs4czL_0)**

Start your workflow automation using Higgsfield today: https://higgsfield.ai/s/mcp-poojadutt-DmHjkQ ✓ Tech Companies are ...

📺 Pooja Dutt

👁️ 14K • 👍 481 • 💬 86 • ⏱️ 14:28 • 1d ago

---

**[Tech stocks tumble over AI cost concerns](https://www.youtube.com/watch?v=Cjnppupu6gk)**

A massive tech stock sell-off dragged down the S&P 500 and Nasdaq on Tuesday. CBS News senior business and technology ...

📺 CBS News

👁️ 15K • 👍 145 • 💬 42 • ⏱️ 3:15 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 57,186 • ❤️ 2,341 • 1d ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 483,139 • ❤️ 2,287 • 5d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 45,687 • ❤️ 708 • 8h ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 138,704 • ❤️ 520 • 5d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 49,569 • ❤️ 690 • 5d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`text-generation` `9.0B`

⬇️ 63,637 • ❤️ 331 • 2d ago

---

**[GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)**

*Unsloth AI*

GLM-5.2 is a large language model optimized for long-horizon tasks, featuring a 1M token context window and advanced coding capabilities with flexible effort levels. It utilizes an improved architecture with IndexShare for reduced FLOPs and is released under an MIT license for broad accessibility.

`text-generation` `753.9B`

⬇️ 76,971 • ❤️ 341 • 1d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 5,123 • ❤️ 294 • 5h ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,769,369 • ❤️ 2,199 • 2mo ago

---

**[Inflect-Nano-v1](https://huggingface.co/owensong/Inflect-Nano-v1)**

*Owen Song*

Inflect-Nano-v1 is an ultra-lightweight, local English text-to-speech model (4.63M parameters total) with an integrated vocoder, designed for efficient inference in embedded systems, prototypes, and research.

`text-to-speech`

⬇️ 0 • ❤️ 190 • 17h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 23 • 💬 0 • ⭐ 5,572 • 3d ago

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

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 44 • 💬 4 • ⭐ 31,161 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 77.4k • 🔱 10.1k • 40m ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 54.9k • 🔱 2.8k • 7h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.6k • 🔱 998 • 6h ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 5.1k • 🔱 395 • 12h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 4.7k • 🔱 554 • 1m ago

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

⭐ 1.9k • 🔱 136 • 1d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 150 • 8d ago

---

**[Forward-Future/loop-library](https://github.com/Forward-Future/loop-library)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 1.6k • 🔱 131 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
