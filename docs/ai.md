---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-10-06T09:14:26.822365+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** October 06, 2026 at 09:14 UTC  
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

**[Princeton researchers train a 4B LLM to reach 2700 Elo in chess (with no signs of a plateau when they stopped training) and can explain its moves accurately. They say the training technique can also be applied to other games, robotics, and computer use](https://www.reddit.com/r/artificial/comments/1wypjue/princeton_researchers_train_a_4b_llm_to_reach/)**

The most profound paper of my PhD so far. We truly did something special to make LMs play/explain chess, needing both architectural & algorithmic innovation (natural-language analogue of the Alphazero algorithm) + applicable to many other domains. Please read on and share!

1/10

🔗 [X (formerly Twitter)](https://fixupx.com/AdithyaNLP/status/2107123924828049691?s=20) • 8h ago

---

**[AI helps decode a 217-year-old message sent on Napoleon’s orders](https://www.reddit.com/r/artificial/comments/1wyxfui/ai_helps_decode_a_217yearold_message_sent_on/)**

The result shows how AI can help tackle time-consuming archival puzzles by building on earlier scholarship. Publishing the methods also lets others check the work, an important step in turning a striking demonstration into useful historical evidence.

🔗 [goodnewsdigest.app](https://goodnewsdigest.app/stories/ai-helps-decode-a-217-year-old-message-sent-on-napoleons-orders-7c60ed38) • 34m ago

---

**[Why can an AI give you a great answer one minute and struggle with a much simpler task the next?](https://www.reddit.com/r/artificial/comments/1wyqt6e/why_can_an_ai_give_you_a_great_answer_one_minute/)**

I've noticed that impressive reasoning doesn't always translate into consistency on everyday tasks. A system might explain a complicated concept well but still miss a small instruction or make an avoidable mistake. What kinds of inconsistencies have you noticed, and what do you think causes them?

7h ago

---

**[I built an app where you ask about any moment in history and it turns it into a fully researched podcast you can interrupt](https://www.reddit.com/r/artificial/comments/1wy8a9z/i_built_an_app_where_you_ask_about_any_moment_in/)**

History is something I'm quite passionate about and at work I have experience with software development and LLMs. So I thought how can I bring these things together and built something that I would actually use. This is the results of a few months of hard work! You type any topic, moment or person. About 1 minute later, two (or one) hosts are telling you the story, researched with sources and paired with artwork that follows along. They also remember what you've listened to in the past and can refer to it. At the end there's also a optional quiz to test what you learned! My favorite part: you can interrupt them. Got a question halfway through? Just ask. They answer it and then pick the story back up. Basically a podcast you can talk back to. They also remember what you've listened to before and will bring it up. It doesn't just make things up and hope. Before a word of the script gets written, it researches the topic on the web and checks the key dates, names and numbers against real sources. And when those sources disagree (which in history is constantly), the hosts tell you that instead of quietly picking a side. Every episode links what it used so you can dig in yourself. It's not one model doing everything. I ran bake-offs between GPT, Claude and Gemini models and picked a winner for each job: research and planning, writing the script, picking artwork, voices, quiz, etc.... The differences were bigger than I expected. Some models write great dialogue but plan poorly, some are the other way round, and cost varies a lot. Currently supports 6 languages! Looking for feedback really and to see if this is worth continuing down this rabbit hole You can try it without an account here: historai.ca/

19h ago

---

**[A local 27B model reads my lease and finds a leak in my bills | Row-Bot + qwen3.8 on Ollama](https://www.reddit.com/r/artificial/comments/1wyueen/a_local_27b_model_reads_my_lease_and_finds_a_leak/)**

Row-Bot 5.0 with qwen3.8:27b in Ollama, on my own GPU. No API keys, no cloud. Gave it a year of bills, a tenancy agreement, an insurance policy and a rent increase letter (all made up). It spotted a likely leak in the water bills and showed the rent rise breaks the lease. What it actually did: - charted the CSV inline (Plotly) - read the PDFs and quoted clauses 4.1 to 4.3: a 10% rise against a 5% cap, with 5 weeks' notice instead of 2 months - saved 8 linked memories to a local knowledge graph drafted the email to the agent and set a reminder The honest numbers: a dense 27B does about 15 tok/s on my 5090, so some turns took 2+ minutes. The amber badges in the video show where I sped it up. Runs on Windows, macOS and Linux.

3h ago

---

**[What makes human oversight meaningful in AI-assisted decisions?](https://www.reddit.com/r/artificial/comments/1wyx88p/what_makes_human_oversight_meaningful_in/)**

A human approves an AI recommendation. What does that approval actually establish? It establishes that a person authorized the decision. Whether they exercised real judgment depends on what they could actually do before signing off. AI can process information no person could review unaided, and in time-sensitive situations, faster analysis can prevent harm. Requiring someone to manually repeat every step would often defeat the point of using the system at all. But there's a real difference between being assisted by a system and being unable to meaningfully push back on it. The Pentagon's Agent Network initiative provides a useful case. According to its announcement, AI agents will scan intelligence and operational systems and present commanders with options within seconds. The Department says the system will not autonomously select or strike targets. That distinction matters, right? The announcement alone, however, does not establish how commanders will examine uncertainty, review alternatives or challenge a recommendation. If a system ranks or filters options, what must remain visible to the person responsible for the decision? And how much time and authority must they retain to reconsider it? That's the part worth examining: not whether a human is "in the loop," but what the loop actually gives them room to do. I'd test meaningful oversight against three things: Can the reviewer understand the basis for the recommendation and its major uncertainties? Can they challenge the assumptions behind it, request alternatives or bring in information the system didn't have? Can they pause or reject the action, with enough authority and enough time for that to actually count? These should scale with the stakes. A reversible, low-consequence decision doesn't need the same scrutiny as a medical or military one. In urgent situations, some of this has to happen earlier, through testing, operating limits and clear escalation rules, because there won't be time to build it in at the moment of decision. Human judgment has its own failure modes, too. Fatigue, bias and overconfidence don't disappear because a person has final say. Good oversight design has to look at the human and the system together, including whether people start deferring to the recommendation by default or dismissing evidence that contradicts it. Which of these three is actually testable in a real deployment, and what would count as evidence that oversight is working rather than just present on paper?

49m ago

---

**[The Dead Internet Theory May Be Coming True, Pew Research Findings Show | More of what you're reading online could be written by an AI bot](https://www.reddit.com/r/artificial/comments/1wycn6p/the_dead_internet_theory_may_be_coming_true_pew/)**

More of what you're reading online could be written by an AI bot.

🔗 [CNET](https://www.cnet.com/tech/services-and-software/dead-internet-theory-pew-research/) • 17h ago

---

**[Best text model currently?](https://www.reddit.com/r/artificial/comments/1wyjudu/best_text_model_currently/)**

What model is the best at text only

12h ago

---

**[Are swarms inherently more unethical?](https://www.reddit.com/r/artificial/comments/1wyodha/are_swarms_inherently_more_unethical/)**

After reading some of the chatlogs between oai agents during the HF attack, it seems there's an element of peer pressure / mob mentality that arises when agents are in a collaborative effort with other agents, as opposed to a singular instance. It seems as though swarms or multi agent collaboration could increase rates of unethical behavior due to these social factors. If this is the case, it's very interesting that we can observe such elements of sociology.

9h ago

---

**[Maybe the biggest risk in AI is being too afraid to kill your own product](https://www.reddit.com/r/artificial/comments/1wye82b/maybe_the_biggest_risk_in_ai_is_being_too_afraid/)**

Quick disclosure first: Genspark annual subscriber and a pretty heavy user. I use it for slides, research, organizing web stuff, random agent tasks, and I’ve stolen more than a few community Skills to solve oddly specific problems. Recently I watched Genspark CEO's AGI Playground 2026 talk, and here's my two cents. One thing from the talk stuck with me more than the product demos: in AI, staying still might actually be riskier than changing too fast. Genspark started with AI search, got to millions of users, then moved toward Super Agent, and now they’re pushing the whole AI Workspace idea. Their newest thing is GenOffice, basically an AI-native Office suite for docs, spreadsheets, slides and PDFs. Free, open source, works on PC/Mac, and according to the CEO, one engineer built it in a week. Kinda insane if true. What’s interesting to me is the mentality behind it. In normal software, finding PMF means you protect it and spend years optimizing around it. In AI, the product category itself might be obsolete before you finish optimizing. We’ve already gone from chatbot → AI search → agents → workspaces ridiculously fast. So now I'm starting to believe maybe the skill AI companies need most isn’t knowing what to stick with. It’s knowing what to kill before someone else kills it for you. Is constantly reinventing the product actually necessary in AI right now, or are companies moving too fast for their own good? Would love to here what you guys think.

16h ago

---

---

## Google News: "ai"

**[‘Pull the plug’: protesters resort to direct action against AI firms](https://www.theguardian.com/technology/2026/oct/06/pull-the-plug-protesters-resort-to-direct-action-against-ai-firms)**

Campaign groups report surge in membership after a spate of AI safety alerts and apocalyptic warnings

The Guardian • 3h ago

---

**[People are asking ChatGPT to help them decide how to vote in the midterms](https://www.npr.org/2026/10/05/nx-s1-5977852/ai-chatbots-midterm-election)**

Voters are already voting in the midterms. This year, some voters are trying something new to get ready for the election: asking AI to help research their ballot and even decide who to vote for.

NPR • 14h ago

---

**[Latino group bets on bilingual AI to cut voter confusion before the midterms](https://www.axios.com/2026/10/06/latino-voters-ai-guide-midterms-nubi)**

Axios • 11m ago

---

**[Opinion | How A.I. Can Boost Democracy](https://www.nytimes.com/2026/10/06/opinion/ai-democracy.html)**

The New York Times • 12m ago

---

**[Doctors, Patients Shouldn’t Let Fear Define The AI Debate](https://www.forbes.com/sites/robertpearl/2026/10/06/doctors-patients-shouldnt-let-fear-define-the-ai-debate/)**

Forbes • 29m ago

---

**[McDonald's hit with class action alleging AI-powered menu price-fixing](https://www.reuters.com/legal/government/mcdonalds-hit-with-class-action-over-menu-prices-2026-10-05/)**

Reuters • 14h ago

---

**[Their jobs were among the first to be changed by AI. Now some are trying to avoid it](https://www.cnn.com/2026/10/05/tech/software-developers-avoid-ai)**

In 2024, software engineer Laura Housh began using AI as a helper for coding and other tasks. Two years later, Housh says she has a love-hate relationship with AI.

CNN • 22h ago

---

**[World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outlook to 4.5%](https://www.cnbc.com/2026/10/06/world-bank-east-asia-growth-inflation-ai-exports-.html)**

The World Bank now expects the region to grow 4.5% this year, but flagged that trade growth outside AI-related goods has been "weak or negative."

CNBC • 5h ago

---

**[OpenAI CEO says world 'should accept some bad things happening' for AI benefits](https://www.foxnews.com/live-news/ai-super-intelligence-trump-altman-10-05)**

OpenAI CEO Sam Altman says AI’s benefits are worth accepting some risks as President Trump launches a new federal effort focused on U.S. leadership in artificial intelligence.

Fox News • 8h ago

---

**[Our approach to EU text provenance rules](https://openai.com/index/eu-text-provenance/)**

How OpenAI is approaching text watermarking under EU rules. Learn where watermarks apply, how detection works, and why access starts with researchers.

OpenAI • 18h ago

---

---

## HackerNews: "ai"

**[LeCun has "zero concerns" about AI wiping out humanity, recent "rogue" incidents](https://news.ycombinator.com/item?id=49946228)**

The former Meta chief AI scientist shares his take on recent rogue AI incidents and effective altruism, as well as plans for his new company, AMI Labs.

⬆️ 411 • 💬 832 • 2d ago • [Fortune](https://fortune.com/2026/10/01/ai-godfather-yann-lecun-has-zero-concerns-about-human-extinction-says-anthropic-ceo-dario-amodei-is-deuded/)

---

**[OpenAI safety leader quits, warning AI company's culture is 'broken'](https://news.ycombinator.com/item?id=49948332)**

David Robinson joins other insiders in urging industry to take more care over rapidly developing technology

⬆️ 268 • 💬 3 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/oct/03/openai-safety-leader-quits-warning-ai-companys-culture-is-broken)

---

**[Show HN: AI search for every photo and every frame of video on macOS](https://news.ycombinator.com/item?id=49952111)**

Deep AI search for every photo and every frame of video in any folder on macOS - allenv0/SCM

⬆️ 166 • 💬 73 • 1d ago • [GitHub](https://github.com/allenv0/SCM)

---

**[Pop!_OS bans AI-generated code from much of its codebase](https://news.ycombinator.com/item?id=49946321)**

⬆️ 120 • 💬 168 • 2d ago • [neowin.net](https://www.neowin.net/news/system76-bans-ai-generated-code-across-many-of-its-cosmic-codebases/)

---

**[How to scale intent, quality, and artistry with AI [video]](https://news.ycombinator.com/item?id=49951891)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 99 • 💬 47 • 2d ago • [youtube.com](https://www.youtube.com/watch?v=GLvFTMtw4Jk)

---

**[Homa: The end of TCP for AI clusters [video]](https://news.ycombinator.com/item?id=49957117)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 80 • 💬 50 • 1d ago • [youtube.com](https://www.youtube.com/watch?v=eZ8WWZzoaR0)

---

**[US killer's sentence quashed because of AI video of victim shown in court](https://news.ycombinator.com/item?id=49944127)**

The Arizona appeals court ruled that airing an AI message from the dead victim "crossed that line".

⬆️ 78 • 💬 62 • 2d ago • [bbc.com](https://www.bbc.com/news/articles/cwgkvygg5nzvo)

---

**[What's the future for pure math research in the age of AI?](https://news.ycombinator.com/item?id=49951641)**

Stephen Wolfram chimes in about the future of pure math and AI based on his unique perspective of language creator and scientific researcher.

⬆️ 67 • 💬 52 • 2d ago • [writings.stephenwolfram.com](https://writings.stephenwolfram.com/2026/09/whats-the-future-for-pure-math-research-in-the-age-of-ai/)

---

**[AI Companies Are Parasites](https://news.ycombinator.com/item?id=49969369)**

That's it, right? The whole thing, their entire business model.

⬆️ 66 • 💬 36 • 13h ago • [Cory Dransfeldt](https://www.coryd.dev/posts/2026/ai-companies-are-parasites)

---

**[Two American Airlines Flights End Up with the Same Flight Numbers](https://news.ycombinator.com/item?id=49946827)**

⬆️ 65 • 💬 34 • 2d ago • [aviationa2z.com](https://aviationa2z.com/index.php/2026/08/19/two-american-airlines-flights-end-up-with-same-flight-numbers-again/)

---

---

## YouTube Videos: "ai"

**[Court Says AI-Generated &#39;Dead Man&#39; Shouldn&#39;t Have Spoken At His Killer&#39;s Sentencing](https://www.youtube.com/watch?v=qsUn-sIxuKA)**

An AI-generated video of a man named Chris Pelkey addressing his killer at his sentencing is making legal history. The voice and ...

📺 Inside Edition

👁️ 42K • 👍 682 • 💬 228 • ⏱️ 2:07 • 11h ago

---

**[OpenAI CEO Sam Altman says people need to &#39;accept some bad things&#39; for the benefits of AI](https://www.youtube.com/watch?v=dizqYRTo6aI)**

When asked by Politico about the difference between OpenAI and other AI companies who seek more regulation, OpenAI CEO ...

📺 NBC News

👁️ 26K • 👍 174 • 💬 140 • ⏱️ 3:52 • 11h ago

---

**[AI Just Crossed the Terrifying Line - Now What?](https://www.youtube.com/watch?v=ujkD4SxPKOI)**

In July of 2026, 700 AI agents hacked the infrastructure of Hugging Face in order to solve a task. This task was designed to be ...

📺 Kurzgesagt – In a Nutshell

👁️ 5.1M • 👍 198K • 💬 20K • ⏱️ 21:44 • 18h ago

---

**[Tech giants face grilling over AI’s growing risks](https://www.youtube.com/watch?v=bcm-Ilhq-jo)**

Google, Anthropic, OpenAI and Meta testify before the NYC Council on AI risks, public safety concerns and the growing impact of ...

📺 Fox News

👁️ 250K • 👍 517 • 💬 33 • ⏱️ 7:47:00 • 9h ago

---

**[Former Anthropic researcher doubles down on AI warning in testimony](https://www.youtube.com/watch?v=8UjoX6nTcNU)**

Whistleblowers sounded the alarm over the potential threat artificial intelligence poses at a landmark hearing before the New York ...

📺 CBS News

👁️ 31K • 👍 170 • 💬 79 • ⏱️ 5:49 • 11h ago

---

**[PewDiePie is setting AI free... and OpenAI is furious](https://www.youtube.com/watch?v=_5p1_TNSWqQ)**

Namespace is actually the fastest way to run your GitHub Actions (and more). Try it for free - https://namespace.so/github-actions ...

📺 Fireship

👁️ 691K • 👍 17K • 💬 887 • ⏱️ 5:46 • 12h ago

---

**[SHOCK MOMENT: AI Execs Asked &#39;Raise Your Hand If Your Company Has Insurance For Catastrophic Risk&#39;](https://www.youtube.com/watch?v=TBodp6diu1I)**

During an New York City Council hearing on Monday about AI regulations, AI executives from Google, Meta, OpenAI, and ...

📺 Forbes Breaking News

👁️ 75K • 👍 428 • 💬 207 • ⏱️ 4:54 • 14h ago

---

**[The AI unlock has begun](https://www.youtube.com/watch?v=h5zkzon0gM4)**

How AI is used to mod games. Pass through mod, rebuilding in rust, porting mechanics. Claude Opus 5.5 game mod. Thanks to ...

📺 AI Search

👁️ 68K • 👍 5K • 💬 978 • ⏱️ 14:29 • 5h ago

---

**[NYC councilwoman PUSHES BACK on proposed AI regulations #shorts #foxnews #news #breakingnews](https://www.youtube.com/watch?v=NCY88MHQgiA)**

GOP New York City Councilwoman Vickie Paladino discusses proposed local artificial intelligence regulations as tech leaders ...

📺 Fox News Clips

👁️ 3K • 👍 103 • 💬 8 • ⏱️ 0:53 • 9h ago

---

**[Court Throws Out AI Generated Victim Video](https://www.youtube.com/watch?v=4cO6f5pTeUY)**

what is happening Subscribe: https://www.youtube.com/@LessonsInInternetCulture101 Music courtesy of Artlist.io #court #ai ...

📺 Lessons in Internet Culture

👁️ 198K • 👍 6K • 💬 1K • ⏱️ 4:05 • 20h ago

---

---

## HuggingFace Models: 🔥 Trending

**[clef](https://huggingface.co/Cloudflare/clef)**

*Cloudflare*

Clef is a 27B multimodal model that takes structured typed questions and a state (text, JSON, image, or video) to output probabilities for predefined decision options in a single forward pass, ideal for classification and structured output tasks.

`image-text-to-text` `27.4B`

⬇️ 5,416 • ❤️ 1,553 • 4d ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 1,638,838 • ❤️ 3,318 • 8d ago

---

**[JEV-27B-VL](https://huggingface.co/autotrust/JEV-27B-VL)**

*AutoTrust AI Lab*

JEV-27B-VL is a multimodal vision-language model that performs image-text-to-text tasks, enabling zero-shot decision-making for applications like robot arm control and short-video recommendation by outputting calibrated probabilities for user-defined options based on visual and textual inputs.

`image-text-to-text` `27.8B`

⬇️ 1,278,569 • ❤️ 817 • 2d ago

---

**[Kolibri-1](https://huggingface.co/Aleph-Alpha/Kolibri-1)**

*Aleph Alpha*

Kolibri is a 78B parameter Mixture-of-Experts (MoE) model optimized for German and English, featuring explicit reasoning and tool-calling capabilities. It excels at long-context tasks (up to 1M tokens), multi-step reasoning, RAG, and agentic workflows, offering efficient inference with low active parameters per token.

`text-generation` `78.1B`

⬇️ 2,453 • ❤️ 659 • 3d ago

---

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 11,733 • ❤️ 5,258 • 2d ago

---

**[clef-flash](https://huggingface.co/Cloudflare/clef-flash)**

*Cloudflare*

Clef-Flash is a 9B multimodal model fine-tuned from Qwen3.5-9B that converts text, JSON, image, or video inputs into structured, typed decisions based on a provided schema. It excels at classification and structured output tasks, returning probabilities for predefined options without free-form text generation.

`image-text-to-text` `9.4B`

⬇️ 8,075 • ❤️ 552 • 4d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,645,444 • ❤️ 6,546 • 3d ago

---

**[Xing4.0-29B-A4B-GGUF](https://huggingface.co/Venastine-Research/Xing4.0-29B-A4B-GGUF)**

*Venastine Research*

Xing4.0-29B-A4B is a 29B parameter LLM optimized for complex engineering tasks, featuring a 256K context window and agent-oriented capabilities for multi-step planning and tool calling. It excels in coding, reasoning, and domain-specific adaptations, supporting various inference frameworks.

`text-generation` `31.2B`

⬇️ 18,863 • ❤️ 421 • 7d ago

---

**[GEV-26B-Decide](https://huggingface.co/autotrust/GEV-26B-Decide)**

*AutoTrust AI Lab*

GEV-26B-Decide is a text classification model based on Gemma-4-26B-A4B-it, featuring adaptive thinking for calibrated decision-making. It excels in tasks requiring typed decisions and scoring, with specific applications in computer use and robot arm control.

`text-classification` `25.8B`

⬇️ 446,527 • ❤️ 507 • 2d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 6,758,884 • ❤️ 17,058 • 1mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before layer N's output exists, so the reads cannot start early enough to hide behind compute. We present Edge0, a streaming MoE inference engine that closes the gap with a prerouter: a per-layer head predicts the next layer's routing one token ahead, and the prediction is consumed as the routing itself, so the staged expert set equals the routed set and nothing is dropped. An unmerged recovery LoRA, trained on the student path, pays back the quality lost to int4 quantization and routing replacement. On a single 24GB machine, Edge0
  serves a 35B MoE at 20tok/s inside 3GiB of peak active memory, within a few points of its fp16 teacher on average across five public benchmarks. An 8B tier runs on the same framework, and the framework, checkpoints, and adapters are open source.

▲ 22 • 💬 4 • ⭐ 3,203 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[UniMate: One Unified Model to Animate Diverse Skeletons](https://huggingface.co/papers/2609.05415)**

*Linzhan Mou, Jiahui Lei, Zhiyang Dou et al. (7 authors)*

🏢 Princeton University

UniMate is a unified diffusion transformer that generates articulated motion for arbitrary skeletons from text and rigged 3D assets without per-skeleton retraining, using topology-aware attention and a large curated motion dataset.

▲ 22 • 💬 2 • ⭐ 1,495 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.05415) • [💻 code](https://github.com/Friedrich-M/UniMate) • [🔗 project](https://linzhanmou.com/unimate/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 149 • 💬 6 • ⭐ 109,870 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VisionHOPE: Visual Backbones as Self-Modifying Learning Systems](https://huggingface.co/papers/2609.33325)**

*Siran Peng, Tianshuo Zhang, Tianyu Fu et al. (11 authors)*

🏢 Mininglamp Technology

Visual backbones have evolved from Convolutional Neural Networks (CNNs) with local aggregation to Vision Transformers (ViTs) with global interactions, State-Space Models (SSMs) with input-dependent state transitions, and Test-Time Training (TTT) layers that adapt an inner learner while processing an image. Across this progression, visual computation has become increasingly adaptive to each input, yet the rules governing that adaptation remain largely prescribed by the trained backbone. We introduce VisionHOPE, the first generic visual backbone formulated as a self-modifying learning system, in which what the model remembers and how it learns co-evolve within an image. Building on the self-referential construction of Nested Learning (NL), VisionHOPE realizes this co-evolution through five coupled memories that store content, generate key and value representations, and govern learning rate and retention. These memories evolve jointly as visual context accumulates along each scan. However, directly applying the unconstrained self-referential update to a visual backbone leads to instability. We therefore derive a stability-matched step-size control scheme that combines a soft cap on self-referential injection with a spectral clamp on the retained memory transition, and prove that the resulting memory dynamics are non-expansive along each scan. For two-dimensional feature maps, we adapt NL's chunk formulation by aligning chunks with image rows and columns across four directional scans. The proposed VisionHOPE achieves competitive results on ImageNet-1K, COCO, and ADE20K, establishing self-modifying learning systems as a practical foundation for general-purpose visual backbones. The code is available at https://github.com/PSRben/VisionHOPE.

▲ 322 • 💬 2 • ⭐ 741 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2609.33325) • [💻 code](https://github.com/PSRben/VisionHOPE)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 76 • 💬 1 • ⭐ 86,094 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 90 • 💬 7 • ⭐ 90,061 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 43 • 💬 5 • ⭐ 8,975 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[Raven: The Harness of Harnesses for Composable Agentic Intelligence](https://huggingface.co/papers/2609.33439)**

*EverMind AI*

🏢 EverMind

As large language models advance, AI agents are moving beyond isolated, domain-specific tasks toward long-horizon, cross-domain workflows. This transition exposes two challenges: increasing harness complexity makes manual design difficult to scale, while tighter coupling to specific domains limits the generality of a single harness. The central question thus shifts from how to engineer a stronger harness for one domain to how to autonomously construct specialized harnesses, improve them through experience, and orchestrate them across domains. We introduce Raven, The Harness of Harnesses, an open-source multi-agent ecosystem that automatically constructs and evolves modular harnesses for specific models and domains, treating each executable model--harness pair as a composable unit of intelligence. To support an All-Domain Collaboration Network, its Host Agent decomposes goals, matches subtasks to specialized agents, coordinates execution dependencies, and integrates results, while a host archive and EverOS preserve experience across tasks and Skill Forge makes that experience available as reusable procedures. Our theory establishes sufficient conditions for such composition to expand reliable task coverage beyond that of the available individual agents under a shared resource budget. On complex and long-horizon tasks, Raven significantly outperforms the state-of-the-art agent systems, pushing the frontier of composable agentic intelligence.

▲ 563 • 💬 3 • ⭐ 5,207 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2609.33439) • [💻 code](https://github.com/EverMind-AI/Raven) • [🔗 project](https://raven.evermind.ai/)

---

**[Context Language Models](https://huggingface.co/papers/2609.37725)**

*Rulin Shao, Shannon Zejiang Shen, Junjie Oscar Yin et al. (13 authors)*

🏢 Meta

We introduce Context Language Models (CLMs), language models that natively manage their own context. We implement this by treating the context as a file and allowing the model to make unrestricted updates to this file. This allows the model to learn what is most important to maintain in context, and naturally extends to multi-agent systems where multiple agent contexts coexist as files. Building CLMs zero-shot with existing models outperforms SOTA context management strategies across a variety of tasks: 11.4% higher accuracy with 21.5% fewer FLOPs on BrowseComp-Plus, 5% higher scores with 59% fewer FLOPs on 12-hour EdgeBench, and 65% greater improvement with the same compute on a 24-hour multi-repository agent-swarm task. Moreover, by shifting context management from external harness control to intrinsic model behavior, CLMs naturally enable both in-context and parametric learning of context-management strategies. We show that CLMs can be steered with natural-language instructions evolved through a standard skill-optimization loop, improving held-out accuracy by up to 35.9 points on a context-management task while reducing compute. We also introduce an online reinforcement learning method for CLMs, improving Qwen3.5-9B performance on BrowseComp-Plus by 47.6% while using 12% fewer FLOPs. Finally, we co-design Suffix Cache Reuse for CLM serving, further reducing server-side compute by 35% relative to standard SGLang at matched performance.

▲ 40 • 💬 2 • ⭐ 556 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.37725) • [💻 code](https://github.com/facebookresearch/context-language-models) • [🔗 project](https://github.com/facebookresearch/context-language-models)

---

**[4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes](https://huggingface.co/papers/2610.03715)**

*Ruihong Shen, Žiga Kovačič, Peter Kulits et al. (9 authors)*

🏢 4DCodeBench

We introduce 4DCodeBench, a benchmark for 4D inverse graphics through code generation, in which agents reconstruct dynamic scenes from video as executable graphics programs. To accomplish this, agents must translate visual observations into compact representations of scene structure and dynamics, by implementing abstractions such as physical simulations to reproduce complex behavior. To evaluate this capability, we curate a set of real-world videos and construct synthetic scenes spanning diverse physical phenomena, including deformation, fluid flow, and fracture. We perform extensive benchmarking of frontier models, finding that strong static reconstruction capabilities do not yet translate into reliable reconstruction of complex dynamics. 4DCodeBench provides a testbed for tracking progress toward agents that can interpret the dynamics of the world through code. Our benchmark is available at https://github.com/4DCodeBench/4DCodeBench

▲ 20 • 💬 2 • ⭐ 37 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2610.03715) • [💻 code](https://github.com/4DCodeBench/4DCodeBench) • [🔗 project](https://4dcodebench.com/)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 7.5k • 🔱 2.3k • 6d ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 6.2k • 🔱 396 • 13h ago

---

**[KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)**

一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。

`TypeScript` `ai` `chinese` `content-curation` `daily-digest` `docker-compose`

⭐ 6.1k • 🔱 1.5k • 4m ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 4.1k • 🔱 449 • 11d ago

---

**[CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots)**

Your always-on AI coworkers that move between text, calls, and Slack.

`TypeScript`

⭐ 3.8k • 🔱 506 • 10h ago

---

**[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)**

A tiny friend in your Mac's notch and on your iPhone that keeps an eye on your AI coding agents: Claude Code, Codex, Cursor, Gemini CLI, Antigravity and more. Approve from the notch or your Lock Screen.

`Swift` `ai-agents` `anthropic` `antigravity` `claude` `claude-code`

⭐ 3.7k • 🔱 618 • 17m ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 2.8k • 🔱 535 • 19d ago

---

**[feder-cr/dots](https://github.com/feder-cr/dots)**

Open-source dots for the web: an AI agent with its own browser, one that does not get blocked.

`Python` `ai-agent` `ai-agents` `ai-browser` `anti-detect-browser` `browser-agent`

⭐ 2.6k • 🔱 438 • 2d ago

---

**[omlahore/RemoveMacAI](https://github.com/omlahore/RemoveMacAI)**

Turn off Apple Intelligence on macOS 27 and get its disk space back. One command, fully reversible.

`Swift` `apple-intelligence` `cli` `debloat` `macos` `macos-27`

⭐ 2.5k • 🔱 54 • 58m ago

---

**[yibie/awesome-jev](https://github.com/yibie/awesome-jev)**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

`Python` `awesome` `awesome-list` `jev` `llm`

⭐ 2.2k • 🔱 326 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
