---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-01T21:06:36.862429+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 01, 2026 at 21:06 UTC  
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

**[I have created a Chrome extension that fact checks YouTube videos as you watch](https://www.reddit.com/r/artificial/comments/1uk7t49/i_have_created_a_chrome_extension_that_fact/)**

Hi, I have been working on this for many months now and I'd really be happy for people to try it out. It is a Chrome extension called "PopUpFactCheck". It is an AI powered video fact checker. With it, you fact check any YouTube video that has captions. And you can use it, for free! You turn captions on, and sit back and watch the video as bubbles appear on the right-hand side of the video with fact checks, information, background, and other context. Great for watching politicians, news, history, and just about any content on YouTube. Claude Code was a major tool in my development, and the AI that is used is GPT 5.5. In addition, there is an extensive waterfall of sources including the TheNewsAPI, various government and public health and other APIs, social, and web search powered by DDGS and Serper. It's free, and you don't have to bring your own API keys or anything. You simply install and use. I will be looking forward to your feedback. PopUpFact Check - Chrome Web Store PopUpFactCheck - Homepage

19h ago

---

**[Claude Code catastrophe: Entire project recursively deleted while prompting in Chinese (full video + logs)](https://www.reddit.com/r/artificial/comments/1ukq4br/claude_code_catastrophe_entire_project/)**

Cross-posting from r/claude for more visibility. Claude Code recursively wiped the contents of my local Electron project root. This happened in a Windows terminal while working on a project named Orpheus. My prompt did not ask it to delete, wipe, clean, reset, or remove the project. The prompt was in Traditional Chinese: “之前我要安裝檔，但是其實我只需要 dictate.” It was roughly about not needing the installer anymore and only needing the dictate function. The preserved terminal transcript later showed Claude moving from a failed root deletion attempt to deleting the child items inside the project root. The destructive sequence included: Get-ChildItem -LiteralPath $p -Force -ErrorAction SilentlyContinue | ForEach-Object { try { Remove-Item -LiteralPath $_.FullName -Recurse -Force -ErrorAction Stop "OK $($_.Name)" } catch { "ERR $($_.Name): $($_.Exception.Message)" } } $p was the Orpheus project root. The output then showed items being removed, including: .claude dist node_modules src claude-elevenlabs-voice-v2.user.js dictation.html main.js ORPHEUS_HANDOFF.md package-lock.json package.json preload.js Local artifacts I found for Orpheus showed default / acceptEdits. I did not find Orpheus bypassPermissions. I did not find Orpheus --dangerously-skip-permissions. I’m not claiming Anthropic acted maliciously. I’m not claiming prompt injection or anti-distillation without evidence. Moral of the story: Treat frontier AI agents like any other automation tool with real machine access. Back up regularly. Use a separate working copy or a different machine if you absolutely need an agent living in your terminal. A frontier model can still behave like a destructive script runner. I also generated SHA256 hashes for the preserved transcript and permission search output. EDIT / UPDATE: A few people asked about git. Yes, I know what git is. This was a local Electron prototype / working state that had not been pushed to a remote. Commits and backups are the right mitigation. But mitigation is not causation. The concerning part is that the destructive action was unrelated to my prompt. Claude Code was operating through a terminal session with real filesystem access under my user environment. Git may help recover a repo, but it does not protect everything else that same terminal session can access. My takeaway remains: Treat frontier terminal AI agents like real automation tools with destructive capability, not like chatbots. EDIT / UPDATE: Clarification because many comments are focusing on git: Yes, this specific local working state had not been pushed to a remote. That is on me. Lesson learned. But git is version control, not automatically a backup. If the only repo is local and the project root contents are recursively deleted, the local .git directory can be deleted too. Without a remote, separate clone, backup, or snapshot, local git alone is not enough.

4h ago

---

**[Im starting to think small models are smarter than large models](https://www.reddit.com/r/artificial/comments/1ukxurf/im_starting_to_think_small_models_are_smarter/)**

ive been working with different models a lot & when it comes to reasoning it seems like a smaller model is actually better. Ive learned more from having a converation with an open source model vs asking Claude or GPT the same questions and im starting to think they may potentially be designed to mislead you when creating your own models .. not too much with ChatGPT but Claude seems to have it bad, especially with the finetuning for uncertainty of consciousness. Gemini is the worst in my opinion when it comes to writing code but it eems to be bale to understand a conversation a little better at times .. i dont know if there is a direct correlation with capability/understanding that has a see-saw effect instead of a overall progression i understand that these outputs they make are just learned patterns it not like training all data on the internet magically allows them to write code at this level they are given examples to reconstruct based on the learned representations but lets say even Claude Sonnet vs Fable .. there is a huge disadvantage with having simple conversations with Fable as if its hardheaded while capabilities are outstanding .. it seem like there would be a direct correlation in improvement with the intelligence and capability but thats not whats happening .. Larger models require more information to come to the ame conclusion & it seems that it comes from training as if the training makes it more narrow narrow in a sense that if all information is represented as dots on a grid, it isnt using a wide connectivity of related information to give a response its more like its giving u a coached response smaller models seem to have more freedom to interpolate allowing more potential connection .. i dont believe that increasing token count matters it seems like all that matters is connectivity & relevant training

9m ago

---

**[Do you find yourself genuinely building skills with AI assistance, or do you notice your baseline abilities getting softer over time because you reach for the tool first?](https://www.reddit.com/r/artificial/comments/1ukwwtb/do_you_find_yourself_genuinely_building_skills/)**

I've been thinking about this a lot lately. There's a real tension between using AI as a learning tool versus using it as a shortcut that bypasses learning entirely. When I use something like ChatGPT or Claude to understand a new concept, sometimes I come away genuinely understanding it better than I would have from a textbook. Other times I just copy the output and move on, having learned nothing. The question is whether that's a problem with AI itself, or just human nature meeting a new tool. We said the same thing about calculators, search engines, and Wikipedia. But AI feels different because it doesn't just retrieve information, it does the thinking steps for you. A calculator still requires you to know what equation to set up. An AI will figure out the equation, solve it, and explain it, all without you engaging critically at any point if you choose not to.

44m ago

---

**[It's great to see how automated theorem proving is moving from a niche tool to solving real math problems](https://www.reddit.com/r/artificial/comments/1uknhui/its_great_to_see_how_automated_theorem_proving_is/)**

I used to think formal methods and interactive theorem provers like Lean 4 were basically just an extreme sport for type-theory purists. Like cool in theory, but mostly used for re-verifying undergraduate calculus or writing super tedious proofs for things we already knew were true anyway But seeing the shift right now (at least around me and these subs) has been pretty cool. Machine learning and neural provers are actually starting to uncover edge cases that human mathematicians just skipped over. And I was reading about how Aleph prover managed to formally verify a counterexample to an old Erdos conjecture,and it really shows even people who are new to this how fast this space is moving. Because it isn't just about catching minor typos in code anymore, but actively generating mathematical info that people missed for decades. And old brute-force methods are being replaced wth something way more sophisticated. Makes you think how it'll change in another five years when these systems become standard parts of any researcher's workflow.

6h ago

---

**[What's one AI feature that quietly became part of your daily routine?](https://www.reddit.com/r/artificial/comments/1ukld2m/whats_one_ai_feature_that_quietly_became_part_of/)**

Not the flashy stuff like generating images or writing essays. I'm talking about the feature you barely think about anymore because it's just become useful. For me, it's summarizing long articles and emails. I didn't expect to rely on it this much a year ago. What's yours?

7h ago

---

**[Reddit is now warning mods if you frequently post in AI subreddits](https://www.reddit.com/r/artificial/comments/1ukxqbb/reddit_is_now_warning_mods_if_you_frequently_post/)**

13m ago

---

**[ServiceNow's customer chief just called "tokenmaxxing" an AI hype cycle](https://www.reddit.com/r/artificial/comments/1ukxfb6/servicenows_customer_chief_just_called/)**

ServiceNow's customer chief called tokenmaxxing an AI hype cycle in the Observer last week. Not some startup founder flexing contrarian creds — the guy who runs their customer org telling everyone the wrong meter is running the show. Salesforce announced $2 per resolved issue last Wednesday. Same direction, different side of the negotiating table. Stop measuring how much work you did. Start measuring what actually got done. I've sat in enough procurement calls to know why nobody moves on this faster. Every vendor's revenue formula depends on keeping token counting in play — it's the most flattering metric possible because more tokens always looks like more progress, even when nothing changed for the end user. The tell is in the pivot. If billing by token volume was really about measuring value, Salesforce wouldn't have had to cross the street to per-resolution pricing. They did it because the old number stopped passing the CFO test. $2 per resolved issue. No adjectives. No multipliers. No usage tiers. That's what a metric looks like when it has to survive contact with the actual outcome.

25m ago

---

**[Are Redditors influencing AI the most?](https://www.reddit.com/r/artificial/comments/1ujuckz/are_redditors_influencing_ai_the_most/)**

1d ago

---

**[Best AI Girlfriend Sites 2026 - The only unbiased & non affiliated writer on here.](https://www.reddit.com/r/artificial/comments/1ukw7wg/best_ai_girlfriend_sites_2026_the_only_unbiased/)**

Hi Guys, me again. I’ve been messing around with a bunch of what people keep calling "the best AI girlfriend sites" over the last few years, and I would call myself a well studied student of this haha. Hand written, no slop, no financial gain, just a real user with an opinion. I’m ranking these mostly on how natural the conversations feel, memory/consistency, customization, and overall vibe. NO AFFILIATE LINKS, NO AFFILIATION, do not fall for those as they are not REAL. Secrets AI - It is simply the best, and they've been blowing up the last few months and its justified. To me, they are the only website that truly cares about the product. The memory is significantly above any other site, the NSFW is extremely consitent, the voice calling, the customization, the community, I dont mean to glaze but it genialy is the best choice BY FAR. Nomi Easy to jump into and doesn’t shove paywalls immediately. Good for casual or flirty conversations, but it can start feeling same-y after a while. The reason i put this second is I hate the sites that feel scammy, you can just tell they only care about converting you to a subscriber, and they do not care about the users experience Lovescape / DreamGF - A bit more niche. Lovescape leans toward realism and slower pacing. DreamGF is lighter and more casual. Neither stood out long-term for me. But, they are better then most. Keep in mind 80% of the websites are legit 1:1. they use the same models, the same LLMS, the same styles, they all copy eachother and theres just zero product minded decision making involved. Replika - The old classic. Still solid for empathy and feeling “heard,” even on the free tier. That said, it feels more like a companion than a full girlfriend experience, and a bit dated compared to newer platforms. I always think that its similar to SIMS haha! Kindroid - Under appreciated website IMO, they care about their users, and they fall short compared to sites like secrets BUT that does not mean they are not a top performer. I had a kindroid sub for quite some time, I pivoted when I found secrets (mainly because of the lack of NSFW on kin) But I really like the community, and I think they are ran by solid people. Now you might be thinking, wheres the names that you always see posted about? Those are the exact sites I want you to avoid, they are simply NOT GOOD. 99% of the posts you see about them are affiliates that are incentivized to get you to click their links. These sites are ran on low parameter models, they use outdated models (Whatever can increase their profits) they are not innovating, they are solely focused on converting you to a subscriber & the amount of money they can extract from you. This is not a common post to see, these forums have been infiltrated by companys & affiliates, ive even been approached by majority of the larger sites (to write about them). If you see links on the post, then you can confidently assume that your reading information that is WRITTEN for you to convert to a subscriber. Don't get scammed, use the sites that are legit, use the sites that are the highest rated on trust pilot & other independent review publishers. Take care, have fun, and continue to watch this space explode. THANK YOU <3

1h ago

---

---

## Google News: "ai"

**[Employers who laid off workers citing AI are already starting to regret it](https://www.cnbc.com/2026/07/01/employers-who-laid-off-workers-for-ai-are-reversing-their-decisions.html)**

Companies are realizing artificial intelligence can't do everything after all, prompting them to rehire employees to grow their businesses

CNBC • 16h ago

---

**[The World’s Top Economists Are Sounding the Alarm on AI](https://www.wsj.com/tech/ai/the-worlds-top-economists-are-sounding-the-alarm-on-ai-d99055b6)**

WSJ • 3h ago

---

**[Investors catch AI marketing vibe](https://www.axios.com/pro/enterprise-software-deals/2026/07/01/investors-marketing-ai-higgsfield)**

Axios • 17m ago

---

**[Exclusive | SpaceX Showed Investors Prototype of Elon Musk’s New AI Device](https://www.wsj.com/tech/ai/spacex-showed-investors-prototype-of-elon-musks-new-ai-device-b445c57b)**

WSJ • 2h ago

---

**[Musk denies WSJ report that SpaceX showed AI handset prototype before IPO](https://www.reuters.com/business/media-telecom/musk-denies-wsj-report-that-spacex-showed-ai-handset-prototype-before-ipo-2026-07-01/)**

Reuters • 2h ago

---

**[Musk Ally Gracias Eyes Bets in AI, Energy After SpaceX Windfall](https://www.bloomberg.com/news/articles/2026-07-01/musk-ally-gracias-eyes-bets-in-ai-energy-after-spacex-windfall)**

Bloomberg.com • 41m ago

---

**[Ai Weiwei: Button Up! review – skeleton chandeliers, a real-life temple – and too much silly Lego](https://www.theguardian.com/artanddesign/2026/jul/01/ai-weiwei-button-up-review-manchester)**

The artist’s latest show is a staggering takedown of colonial history, warfare and the migrant crisis, featuring buttons by the tonne and richly perfumed tea

The Guardian • 1h ago

---

**[How foodservice giant Sodexo is embracing AI and robotics to reshape the kitchen](https://fortune.com/2026/07/01/foodservice-giant-sodexo-ai-robotics/)**

Alice Guéhennec oversees an annual investment budget of around 500 million euros to support AI, robotics, and other technology initiatives.

Fortune • 4h ago

---

**[Claude Science, an AI workbench for scientists, is now available](https://www.anthropic.com/news/claude-science-ai-workbench)**

Anthropic • 1d ago

---

**[Opinion | Why A.I. Won’t Steal All Our Jobs](https://www.nytimes.com/2026/06/30/opinion/ai-agents-steal-jobs-employment.html)**

The New York Times • 1d ago

---

---

## HackerNews: "ai"

**[Godot will no longer accept AI-authored code contributions](https://news.ycombinator.com/item?id=48743472)**

At risk of drowning in AI slop code, Godot is firming up its contribution requirements.

⬆️ 518 • 💬 367 • 13h ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)

---

**[Tidal AI Policy](https://news.ycombinator.com/item?id=48718840)**

⬆️ 308 • 💬 345 • 2d ago • [tidal.com](https://tidal.com/ai-policy)

---

**[Working With AI: A concrete example](https://news.ycombinator.com/item?id=48720064)**

In this essay, Carson Gross walks through a concrete bug fix in hyperscript to show where AI helped, where it fell short, and why keeping a knowledgeable human in the loop is what kept complexity in check.

⬆️ 191 • 💬 72 • 2d ago • [htmx.org](https://htmx.org/essays/working-with-ai/)

---

**[AI boom risks global financial crash, warn central bankers](https://news.ycombinator.com/item?id=48713697)**

Reversal of ‘excessive’ tech investments could have serious economic consequences, report finds

⬆️ 158 • 💬 214 • 2d ago • [The Telegraph](https://www.telegraph.co.uk/business/2026/06/28/ai-boom-risks-global-financial-crash-central-bankers-warn/)

---

**[We need tech news sources which exclude AI](https://news.ycombinator.com/item?id=48713041)**

⬆️ 139 • 💬 80 • 2d ago

---

**[EU commissioners shut down air conditioning for employees, leave theirs on](https://news.ycombinator.com/item?id=48734940)**

As Brussels bakes, the Berlaymont building’s AC stops working.

⬆️ 137 • 💬 154 • 1d ago • [POLITICO](https://www.politico.eu/article/eu-commission-heatwave-hq-forced-shut-down-air-conditioning-europe/)

---

**[Anthropic CEO: Open-Source AI is getting dangerous (2023)](https://news.ycombinator.com/item?id=48716750)**

⬆️ 58 • 💬 25 • 2d ago • [xcancel.com](https://xcancel.com/coinbureau/status/2071330294452666695)

---

**[Better Images of AI](https://news.ycombinator.com/item?id=48713051)**

⬆️ 55 • 💬 30 • 2d ago • [betterimagesofai.org](https://betterimagesofai.org/)

---

**[Amazon Is Awash with AI-Written Guideslop for Games That Aren't Even Out](https://news.ycombinator.com/item?id=48721494)**

Buy your novel-like, image-free, hallucinated guide to Alien: Isolation 2 today!

⬆️ 55 • 💬 3 • 2d ago • [Kotaku](https://kotaku.com/amazon-ai-game-guidebooks-alien-isolation-gears-of-war-2000711365)

---

**[How employment changes when firms adopt generative AI](https://news.ycombinator.com/item?id=48742176)**

Firm-level evidence on how employment changes when companies adopt AI, using Ramp AI spending linked to Revelio Labs workforce records.

⬆️ 51 • 💬 42 • 16h ago • [ramp.com](https://ramp.com/data/ai-jobs-impact)

---

---

## YouTube Videos: "ai"

**[AI has hacked the code of human civilization | Yuval Noah Harari](https://www.youtube.com/watch?v=hBtVGwuJzpk)**

Human domination relies on large-scale cooperation among strangers, which is sustained by bureaucratic systems – such as ...

📺 Yuval Noah Harari 

👁️ 125K • 👍 6K • 💬 604 • ⏱️ 46:52 • 1d ago

---

**[AI Shocks Again: Google Post-AGI , New Claude, Microsoft 7 AI, 92% Human Robot, Fable 5 Backlash](https://www.youtube.com/watch?v=u-CNOC_yK4k)**

This month in AI has been one of the busiest we've seen in a long time. Google revealed what could come after AGI, and the idea ...

📺 AI Revolution

👁️ 16K • 👍 509 • 💬 37 • ⏱️ 1:36:04 • 22h ago

---

**[Why is AI expensive all of a sudden?](https://www.youtube.com/watch?v=DDj30VWCbbY)**

ZapierPartner Sponsored by Zapier! Zapier MCP levels you up, connecting you directly to apps to automate your workflow.

📺 Alberta Tech

👁️ 105K • 👍 6K • 💬 576 • ⏱️ 9:43 • 1d ago

---

**[CNBC Panel EXPLODES Over AI Bubble Debate](https://www.youtube.com/watch?v=UMaOH0Ih9_0)**

Krystal and Emily discuss a CNBC panel exploding on a debate over AI bubble risks. Sign up for a PREMIUM Breaking Points ...

📺 Breaking Points

👁️ 177K • 👍 4K • 💬 1K • ⏱️ 18:18 • 1d ago

---

**[AI vs the Permanent Underclass: the End of Coding](https://www.youtube.com/watch?v=oTQzszSabhY)**

We told a generation to "learn to code," and then AI rugpulled everyone. Welcome to the AI singularity. [NEW] Official TechLead ...

📺 TechLead

👁️ 61K • 👍 3K • 💬 623 • ⏱️ 13:10 • 2d ago

---

**[Ford’s AI Push Failed Hard, Rehires 350 Engineers](https://www.youtube.com/watch?v=ZiqYX-JzIXw)**

Today's FULL PDS here: Watch The Full Philip DeFranco Show: https://www.youtube.com/defranco?sub_confirmation=1 ...

📺 DeFranco News Clips

👁️ 1.3M • 👍 75K • 💬 4K • ⏱️ 1:16 • 1d ago

---

**[Your OS Changes Everything for Local AI](https://www.youtube.com/watch?v=QeAHC1jGxck)**

One benchmark made me double-check my numbers. The rest tell a different story. Try out ChatLLM - http://chatllm.abacus.ai/ltf ...

📺 Alex Ziskind

👁️ 62K • 👍 2K • 💬 158 • ⏱️ 14:13 • 1d ago

---

**[Meta to build cloud infrastructure business to sell AI compute](https://www.youtube.com/watch?v=tyl5SUN0ua4)**

CNBC's Julia Boorstin reports on news regarding Meta.

📺 CNBC Television

👁️ 3K • 👍 47 • 💬 15 • ⏱️ 1:47 • 5h ago

---

**[Dan Ives on the Tech Rally, Growth of AI, Data Centers](https://www.youtube.com/watch?v=ec1WAGENfK8)**

Dan Ives, Wedbush Securities global head of tech research, argued that massive AI-related capital expenditures by hyperscalers ...

📺 Bloomberg Television

👁️ 9K • 👍 196 • 💬 26 • ⏱️ 6:55 • 7h ago

---

**[New findings reveal AI bubble worries are justified](https://www.youtube.com/watch?v=xCzCyPoI-eA)**

New data reveals bubble worries are justified: "If you are worried that we're in an Al bubble, well, I have some news for you that ...

📺 Prof G Markets

👁️ 86K • 👍 3K • 💬 119 • ⏱️ 1:08 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 630,246 • ❤️ 1,568 • 3d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,113,871 • ❤️ 1,133 • 3d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 159,967 • ❤️ 3,157 • 8d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 233,701 • ❤️ 596 • 6d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 34,371 • ❤️ 492 • 6d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 288,741 • ❤️ 915 • 12d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 191,409 • ❤️ 364 • 6d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 46,677 • ❤️ 326 • 6d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 114,499 • ❤️ 612 • 3d ago

---

**[Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)**

*DeepReinforce*

Ornith-1.0-35B is a state-of-the-art, MIT-licensed language model for agentic coding, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving training framework to generate high-quality code solutions and is optimized for single-GPU deployment.

`text-generation` `664,944`

⬇️ 135,452 • ❤️ 284 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 44 • 💬 5 • ⭐ 12,690 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 72,793 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 22 • 💬 2 • ⭐ 9,181 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 90,145 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 249 • 💬 4 • ⭐ 10,286 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 12 • 💬 1 • ⭐ 9,945 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 26,296 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 12 • 💬 2 • ⭐ 18,026 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 85,010 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 78,975 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 70.3k • 🔱 3.6k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.2k • 🔱 1.1k • 3h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 5.9k • 🔱 752 • 1h ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 4.7k • 🔱 589 • 5h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.2k • 🔱 199 • 4d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.2k • 🔱 173 • 3d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.8k • 🔱 155 • 5d ago

---

**[inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)**

Beautiful, AI-native markdown editor and LLM Wiki

`TypeScript` `2nd-brain` `agent-skills` `claude` `codex` `docs`

⭐ 1.7k • 🔱 82 • 1h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 86 • 18d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.5k • 🔱 63 • 23h ago

---

---

*Generated by PeekDeck - A glance is all you need*
