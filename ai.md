---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-05T00:02:15.336874+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 05, 2026 at 00:02 UTC  
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

**[Meta Paid Hundreds of Contractors to Pretend to Be Teenagers While Barraging Its Competitors’ AI With Disturbing Content](https://www.reddit.com/r/artificial/comments/1ungqh7/meta_paid_hundreds_of_contractors_to_pretend_to/)**

"Surely we are going to get in trouble for doing this?"

🔗 [Yahoo News](https://www.yahoo.com/news/us/articles/meta-paid-hundreds-contractors-pretend-130200038.html?.tsrc=daily_mail&segment_id=DY_VTO_50_Supernova&ncid=crm_19908-1475736-20260704-0--A&bt_ee=9gzHBYP4lPFkJ0sQWNTUaDg%2ByNx1IPgLBZidnverDFwSgBJNAY%2FSHqS9MjlzlxEm&bt_ts=1783187096830) • 5h ago

---

**[This week in AI: GPT-5.6, Gemini 3.5 Flash, Claude Science, and a Qwen price war — inference cost is collapsing across every tier at once](https://www.reddit.com/r/artificial/comments/1un6v9c/this_week_in_ai_gpt56_gemini_35_flash_claude/)**

Lot dropped this week and there's a pretty clear through-line, so figured I'd pull it together. Model releases: - OpenAI launched GPT-5.6 (Sol/Terra/Luna). The bit worth noting isn't the flagship — it's Terra, reportedly matching GPT-5.5 quality at ~2x cheaper, with Luna aimed at the low-cost end. - Google shipped Gemini 3.5 Flash (beats 3.1 Pro on several benchmarks), plus Nano Banana 2 Lite (images ~$0.034/1K-res) and Gemini Omni Flash (video ~$0.10/sec via API). - xAI made Grok 3 GA and Grok 4.1 live for everyone. Grok 5 still hasn't shipped, which is its own story at this point. Vertical / enterprise: - Anthropic launched Claude Science for pharma and lab research. Separately, the US govt lifted the export restrictions on Fable 5 / Mythos 5 that it had imposed only weeks earlier. - Mistral shipped OCR 4 (on-prem, structure-aware extraction) and is reportedly raising ~€3B at ~€20B. Open source: - Ollama crossed 52M monthly downloads, added `ollama launch` (one command to run coding agents on local or cloud models), and is now compatible with the Anthropic Messages API. - Hugging Face: agents can train models via Hub skills now; Meta + HF also launched OpenEnv for agent environments. Funding: - Together AI raised $800M Series C (~$8.3B post). Crunchbase notes ~88% of 2026 AI funding went to US companies. My take as someone building on top of these APIs: The thing I keep noticing is that the price collapse is happening across every tier simultaneously, not just at the bottom. When the "balanced" model gets 2x cheaper each generation and the Flash tier beats last year's Pro, it gets really hard to build a business whose only edge is "we use the best model." That edge evaporates on someone else's release schedule. The stuff that looked durable this week was all workflow-and-data — Claude Science, Mistral's on-prem OCR, Alibaba's agent ecosystem. Would genuinely like to hear how others here are handling multi-provider abstraction, because a surprise price or availability change shouldn't be able to wreck your margins overnight. And the frozen-then-unfrozen Anthropic thing means model availability is now a supply-chain risk, not a hypothetical.

12h ago

---

**[Survey: 63% of Americans are uncomfortable letting AI help them choose who to vote for, and 80% are worried AI bots are answering political surveys. Is the discomfort about AI, or about trust?](https://www.reddit.com/r/artificial/comments/1unmy3d/survey_63_of_americans_are_uncomfortable_letting/)**

Saw a national survey from March on how people feel about AI in politics, and two numbers stuck with me. 63% said they'd be uncomfortable using an AI chatbot to help decide who to vote for, even though plenty of people are fine using chatbots to fact-check or follow issues. 80% said they're worried that AI bots, not real people, are answering the surveys that feed into policy and business decisions. It reads less like fear of the tech and more like people drawing a hard line at AI touching the actual decision. Where do folks here think that line should be? Source: https://data.verasight.io/ai/adults-views-on-ai-in-elections

42m ago

---

**[Meta Reportedly Strikes $6.5 Billion Deal with Samsung Foundry for 2nm AI Chips](https://www.reddit.com/r/artificial/comments/1unfzi9/meta_reportedly_strikes_65_billion_deal_with/)**

Meta Platforms is reportedly investing $6.5 billion with Samsung Foundry to produce its third-generation MTIA (Meta Training and Inference Accelerator) chips using a 2nm process. This strategic move signifies a shift from TSMC and aims to reduce reliance on NVIDIA GPUs, lower supply chain risks, and support Meta's ambitious goal of 5 gigawatts of computing capacity by 2030 for its AI and cloud initiatives. The deal is expected to bolster Meta's competitive position in the rapidly evolving AI and cloud computing markets. Context Meta has been increasingly focused on artificial intelligence and cloud services, necessitating advanced computing power. The MTIA chips represent Meta's third generation of in-house processors, designed to optimize performance for AI workloads. The shift to Samsung Foundry marks a strategic pivot in Meta's manufacturing partnerships, reflecting broader industry trends towards vertical integration. Why this matters Meta's $6.5 billion investment in Samsung Foundry is a significant step towards enhancing its capabilities in AI and cloud computing. By developing its own 2nm chips, Meta aims to reduce dependence on external suppliers like TSMC and NVIDIA. This move could improve supply chain stability and operational efficiency, which are critical in the fast-paced tech landscape. Implications This deal could enhance Meta's market position by enabling it to deliver more efficient AI services. It may also influence other tech companies to reconsider their supply chains and partnerships in light of Meta's strategic shift. If successful, this initiative could lead to increased investment in domestic semiconductor manufacturing and innovation within the tech sector. What to watch In the coming months, observers should monitor the progress of the chip development and production timelines. Any announcements regarding partnerships or technological advancements from Meta or Samsung could signal the effectiveness of this collaboration. Additionally, industry reactions from competitors and suppliers will provide insights into the competitive landscape.

5h ago

---

**[Other than writing emails and summarizing reports, what else do you use AI for at your office if you are not the tech side of the business?](https://www.reddit.com/r/artificial/comments/1un62q0/other_than_writing_emails_and_summarizing_reports/)**

Since I am not building any tech products or coding, other than email and repots, I am not sure what else to use AI for. Are there any other creative ways you use AI for genuinely help with day to day work. Please share your ideas.

13h ago

---

**[Can AI Avatars Change How We Perceive Information? (Academic Research)](https://www.reddit.com/r/artificial/comments/1unf5gk/can_ai_avatars_change_how_we_perceive_information/)**

Hello Everyone! You are invited to take part in a study exploring whether different AI avatars can shift people’s perceptions when they watch information online. The survey takes about 10 minutes to complete and is open to anyone aged 18 or older. Link to the study: https://surveyswap.io/s/ZYHW-JGAP-9UQD Thank you very much in advance for your participation!

6h ago

---

**[What's one skill that has become unexpectedly valuable over the past few years?](https://www.reddit.com/r/artificial/comments/1uner2a/whats_one_skill_that_has_become_unexpectedly/)**

I've noticed that being able to summarize information clearly has become much more useful than I expected. Whether it's at work, studying, or just keeping up with news, turning a lot of information into something concise feels like a real advantage. It's interesting because a few years ago I wouldn't have considered this a "skill" worth practicing. What's something you've learned recently that turned out to be far more useful than you expected?

6h ago

---

**[How long does the Perch AI Pro $10/mo Early Access price last?](https://www.reddit.com/r/artificial/comments/1unksdx/how_long_does_the_perch_ai_pro_10mo_early_access/)**

Just signed up for Perch AI and I'm looking at Pro for $10/mo (says 50% off, "Early Access pricing"). Couldn't find anything on the pricing page or FAQ about how long this actually lasts. Has anyone been on Pro for a few months now? Did the price jump back to $20 at some point, or is it still $10 for you? Also curious if this is locked in per account once you subscribe, or if it can change mid subscription without warning. Trying to decide if it's worth committing to before finding out it doubles next month. Any info from people already on Pro would help a lot.

2h ago

---

**[AI cancel culture](https://www.reddit.com/r/artificial/comments/1umx1er/ai_cancel_culture/)**

My reddit feed has been getting filled with a ton of AI generated content. A notable one is r/ModMuse. Its a girl posing for selfies in different outfits. It came up again today. Tons of posts from guys. One said "You're really pretty." I responded: "Don't get too excited. I'm pretty sure she's AI generated..." I then got a response that read..."Removed: Please don't post unverified fake/ AI-generated accusations. I am a bot. This action was performed automatically." And then a follow-on message saying I'm permanently banned from the sub. I found this a little unnerving. AI agents and automated scripts are starting to show up everywhere. If AI is able to generate content on its own and control the conversation by silencing dissenters, it seems a dangerous precedent. The content in this situation was benign but what if AI uses the same tactics with political discourse, or more consequential issues.

21h ago

---

**[Andrew Ng: "In 3-6 months, everyone will be using self-improving loops. No more prompting”](https://www.reddit.com/r/artificial/comments/1umcprg/andrew_ng_in_36_months_everyone_will_be_using/)**

Andrew Ng recently said: "100% of my tasks are now done by AI agents. Hype has exceeded my expectations. Loops is next step. In 3-6 months, everyone will be using self-improving loops. No more prompting." I think he's not too far off, you can already see the shift happening, people are moving away from chatting with an AI and telling it what to do step by step, and building systems where the agent just keeps working on a task on its own, which is kind of the whole point of calling it an agent. Sounds great on paper but there's a few practical problems nobody really talks about. The first one is cost: when an agent gets stuck it can spin in circles for way longer than you'd expect and what would've taken a few messages in a normal chat turns into a lot of wasted time and money Second is data quality: agents work way better when what you feed them is clean and easy to parse, if they're pulling raw docs, they end up burning time just sorting through the noise instead of doing the task. That's why a lot of devs spend half a day prepping data as they do building the agent itself. Firecrawl is a good example of something that pulls info from websites and cleans it up before it even hits the model. Third thing, and probably the most underrated, is that these setups are a lot easier to run when someone else is footing the bill. A big company can eat the cost of an agent messing up and burning tokens, a small startup can't afford that kind of slack. My take is we'll see a lot more autonomous agents over the next year, but the real question is whether people can make them reliable and cheap enough to actually run every day

1d ago

---

---

## Google News: "ai"

**[How AI is changing language](https://www.theguardian.com/books/ng-interactive/2026/jul/04/future-of-fiction-next-great-novel-ai-language-chat-gpt)**

As allegations of LLM use rock the literary and media worlds, linguists explain what really distinguishes human and machine language, while novelists including Jennifer Egan and Jeanette Winterson reflect on the future of fiction in an age of ChatGPT

The Guardian • 3h ago

---

**[‘Who Should I Vote for?’ Voters Turn to A.I. Before Casting Their Ballots](https://www.nytimes.com/2026/07/04/us/politics/voters-ai-chatbots-elections.html)**

The New York Times • 15h ago

---

**[AI security questions loom over NATO summit](https://www.politico.com/news/2026/07/04/ai-security-nato-access-00984758)**

Politico • 4h ago

---

**[High-Earner Families Are Ditching Traditional Schools for Life Skills and AI](https://www.wsj.com/us-news/education/alternative-education-wealthy-families-ai-cd7922b3)**

WSJ • 23h ago

---

**[Tokenmaxxing is so over. It's all about modelmaxxing now.](https://www.businessinsider.com/ai-model-routing-modelmaxxing-efficient-token-use-2026-7)**

Employees racked up AI bills, and companies are backpedaling on tokenmaxxing. Now, it's all about routing prompts to the most value-for-money model.

Business Insider • 15h ago

---

**[For one small business, AI was key to a quick start and expansion](https://www.reuters.com/business/healthcare-pharmaceuticals/one-small-business-ai-was-key-quick-start-expansion-2026-07-04/)**

Reuters • 8h ago

---

**[From Macron to Modi, governments are rolling out the red carpet for AI giants](https://www.cnbc.com/2026/07/04/macron-modi-ai-infrastructure-tech-ceos.html)**

Macron and Modi are courting tech CEOs as France and India seek AI data center investment and cloud infrastructure.

CNBC • 19h ago

---

**[AI Can't Thrive Without This Stock (Hint: It's Not Nvidia)](https://finance.yahoo.com/technology/ai/articles/ai-cant-thrive-without-stock-175700505.html)**

This under-the-radar company doesn't get the recognition that semiconductor specialists receive -- but it certainly should.

Yahoo Finance • 6h ago

---

**[3 Stocks to Buy on the AI Infrastructure Sell-Off](https://finance.yahoo.com/markets/stocks/articles/3-stocks-buy-ai-infrastructure-150500852.html)**

Nvidia, AMD, and Micron look like good buys on this pullback.

Yahoo Finance • 8h ago

---

**[Are the ‘MANGOS’ Stocks Already Turning Soft?](https://www.nytimes.com/2026/07/04/business/mangos-ai-stocks.html)**

The New York Times • 15h ago

---

---

## HackerNews: "ai"

**[The bottleneck might be the air in the room](https://news.ycombinator.com/item?id=48783117)**

You gather your most expensive people into a room to make your most important decisions. Then, somewhere in the second hour, the room quietly gets worse at making them. Not the people. The room.

⬆️ 746 • 💬 427 • 17h ago • [Mike Bowler](https://blog.mikebowler.ca/2026/07/03/co2-and-decision-making/)

---

**[Protect your right to run local AI](https://news.ycombinator.com/item?id=48768951)**

⬆️ 537 • 💬 191 • 2d ago • [righttointelligence.org](https://righttointelligence.org/)

---

**[AI can't be listed as inventor on patent applications, Japan's top court rules](https://news.ycombinator.com/item?id=48761536)**

⬆️ 395 • 💬 208 • 2d ago • [japannews.yomiuri.co.jp](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/)

---

**[Please stop the AI confidence theater](https://news.ycombinator.com/item?id=48774414)**

We don’t need an extra reason to be anxious

⬆️ 232 • 💬 254 • 1d ago • [elenaverna.com](https://www.elenaverna.com/p/please-stop-the-ai-confidence-theater)

---

**[The short leash AI coding method for beating Fable](https://news.ycombinator.com/item?id=48766026)**

⬆️ 194 • 💬 242 • 2d ago • [blog.okturtles.org](https://blog.okturtles.org/2026/07/short-leash-ai-method/)

---

**[AI fake news complaining about how AI fake news is the death of real news](https://news.ycombinator.com/item?id=48760598)**

Did 47 Alabama newspapers die on a single day and no one noticed? (Hint: No, they didn't.)

⬆️ 158 • 💬 58 • 2d ago • [Nieman Lab](https://www.niemanlab.org/2026/07/now-were-getting-ai-fake-news-complaining-about-how-ai-fake-news-is-the-death-of-real-news/)

---

**[Instead of banning AI, I made a classroom contract with my students](https://news.ycombinator.com/item?id=48775499)**

⬆️ 87 • 💬 90 • 1d ago • [science.org](https://www.science.org/content/article/instead-banning-ai-i-made-classroom-contract-my-students)

---

**[AI has torched the market for junior programmers](https://news.ycombinator.com/item?id=48788361)**

Junior programmers are getting destroyed by AI — down 19%, while devs over 40 thrive. Meanwhile, millions of non-developers are shipping real software without the job title. The credential market collapsed; the activity exploded. The problem: nobody's building the next generation of senior engineers.

⬆️ 84 • 💬 156 • 4h ago • [seldo.com](https://seldo.com/posts/ai-has-torched-the-market-for-junior-programmers/)

---

**[The gauge broke: devs felt 20% faster with AI, measured 19% slower (2025)](https://news.ycombinator.com/item?id=48757440)**

For two years I argued the feeling of AI speed had come apart from the fact of it, from watching my own teams. This summer it stopped being an anecdote. A controlled trial measured experienced developers feeling about 20% faster while running about 19% slower. The instrument we steer by reads backward.

⬆️ 77 • 💬 98 • 2d ago • [intrepidkarthi](https://intrepidkarthi.com/writing/the-gauge-broke/)

---

**[AI saves about 3% of your hours, and almost none of it reaches the money](https://news.ycombinator.com/item?id=48777257)**

The real ROI of AI for knowledge work: the task-level gains (Noy-Zhang, Brynjolfsson), the jagged frontier (BCG-Harvard), the 2.8% real-world time saving and no earnings effect (Humlum), 95% of enterprise pilots with no P&L return (MIT), and how to capture what is real.

⬆️ 75 • 💬 93 • 1d ago • [okaneland.com](https://okaneland.com/study/ai-productivity-roi-at-work/)

---

---

## YouTube Videos: "ai"

**[Why AI is Collapsing: How China is Winning.](https://www.youtube.com/watch?v=JXJf7vL8k94)**

US AI companies are too expensive. Why China is winning the AI race to zero. [NEW] Official TechLead Private Group ...

📺 TechLead

👁️ 79K • 👍 4K • 💬 579 • ⏱️ 9:40 • 2d ago

---

**[Flock&#39;s A.I.-enabled street cameras see backlash across the country](https://www.youtube.com/watch?v=5fbmWnJGCtc)**

Activists are speaking out against new, A.I.-enabled cameras being used by municipalities across the country. Critics argue the ...

📺 NBC News

👁️ 48K • 👍 647 • 💬 481 • ⏱️ 6:08 • 23h ago

---

**[Microsoft Admits it was Wrong About AI](https://www.youtube.com/watch?v=towF0_V7oHw)**

For years, we were told AI would replace programmers, office workers, and eventually most white-collar jobs. But behind closed ...

📺 The Infographics Show

👁️ 206K • 👍 6K • 💬 1K • ⏱️ 14:31 • 1d ago

---

**[Even I Was Fooled By AI Slop And I&#39;m Sorry!](https://www.youtube.com/watch?v=Q0gX1lF0s6M)**

I was completely fooled by AI-generated slop and I'm sorry. I thought this wild RFK Jr. clip was real – turns out it was 100% fake.

📺 Maximilien Robespierre

👁️ 13K • 👍 1K • 💬 391 • ⏱️ 5:58 • 16h ago

---

**[The Best AI Safety News In Years (Maybe Ever?)](https://www.youtube.com/watch?v=O84I21_9U74)**

Why did the US government ban Fable and Mythos, Anthropic's most powerful AI models? Let's find out! You can support me on ...

📺 Siliconversations

👁️ 57K • 👍 9K • 💬 1K • ⏱️ 10:56 • 2d ago

---

**[Sam Harris WARNS: It&#39;s Already Too Late to Stop AI](https://www.youtube.com/watch?v=DsAGYLzBbdg)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Sam Harris argues that humanity has ...

📺 Neural Nutshell

👁️ 5K • 👍 160 • 💬 65 • ⏱️ 16:36 • 1d ago

---

**[AI Doctor Trump Treats Critics Julia Roberts, Whoopi Goldberg &amp; Robert De Niro | Firstpost America](https://www.youtube.com/watch?v=iHV8xfAMw1U)**

US President Donald Trump has once again turned to artificial intelligence to shape his public image—this time as a fictional ...

📺 Firstpost

👁️ 13K • 👍 49 • 💬 81 • ⏱️ 4:54 • 1d ago

---

**[The AI Layoff Payback Has Begun](https://www.youtube.com/watch?v=QorWpn2O_sI)**

This video is sponsored by Lumo by Proton: a privacy-first AI assistant from the Swiss company behind Proton Mail. Whether ...

📺 House of El - AI

👁️ 144K • 👍 10K • 💬 2K • ⏱️ 27:19 • 1d ago

---

**[AI Made This Entire Video by Itself... (Claude Fable 5)](https://www.youtube.com/watch?v=CQl5V_BX02U)**

In the name of science, I told Claude Fable 5 to make a Dan Dingle video. This is the result... Merch that ISN'T AI SLOP▻ ...

📺 Dan Dingle

👁️ 74K • 👍 5K • 💬 683 • ⏱️ 9:09 • 2d ago

---

**[AI Roosevelt’s &#39;scathing&#39; comment to Donald Trump…](https://www.youtube.com/watch?v=QRFIcF6q6rw)**

Simon Marks reacts to AI Theodore Roosevelt's response to Donald Trump's question about the Panama Canal. Listen to the full ...

📺 LBC

👁️ 373K • 👍 7K • 💬 464 • ⏱️ 1:44 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,464,047 • ❤️ 1,460 • 6d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 208,920 • ❤️ 3,398 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 988,379 • ❤️ 1,714 • 1d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 359,659 • ❤️ 711 • 9d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 342,752 • ❤️ 1,009 • 15d ago

---

**[Qwen3.6-27B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-27B-NVFP4)**

*NVIDIA*

The Qwen3.6-27B-NVFP4 is an FP4 quantized version of Alibaba's Qwen3.6-27B LLM, optimized by NVIDIA for efficient inference on NVIDIA GPUs. It excels in text generation tasks and is suitable for AI agents, chatbots, and RAG systems.

`text-generation` `18.2B`

⬇️ 184,521 • ❤️ 249 • 4d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 5,456 • ❤️ 238 • 1d ago

---

**[DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)**

*DeepSeek*

DeepSeek-V4-Pro-DSpark is a text-generation model featuring a 1.6T parameter Mixture-of-Experts architecture with a 1 million token context window, optimized for long-context efficiency using Hybrid Attention. It excels in reasoning, coding, and agentic tasks, offering advanced capabilities for complex applications.

`text-generation` `889.5B`

⬇️ 10,306 • ❤️ 367 • 20h ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 69,837 • ❤️ 376 • 9d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 320,660 • ❤️ 424 • 9d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 49 • 💬 5 • ⭐ 13,250 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 73,391 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 103 • 💬 4 • ⭐ 90,807 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 25 • 💬 2 • ⭐ 9,724 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 13 • 💬 2 • ⭐ 18,669 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,414 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 250 • 💬 4 • ⭐ 10,592 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 85,353 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 13 • 💬 1 • ⭐ 10,235 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 26,507 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 73.9k • 🔱 3.9k • 3d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.4k • 🔱 1.1k • 6h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.2k • 🔱 815 • 7m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 5.6k • 🔱 732 • 5h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.4k • 🔱 207 • 1d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.3k • 🔱 180 • 2d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.8k • 🔱 72 • 2d ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 87 • 21d ago

---

**[GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills)**

AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

`Python`

⭐ 1.4k • 🔱 130 • 27d ago

---

**[nolangz/pixel2motion](https://github.com/nolangz/pixel2motion)**

AI logo animation skill: turn raster logos into smooth SVG animation, animated HTML demos, GIF/video previews, and motion QA evidence.

`Python` `ai-design-tools` `animated-logo` `brand-motion` `claude-skill` `codex-skill`

⭐ 1.4k • 🔱 115 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
