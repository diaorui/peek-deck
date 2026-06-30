---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-30T14:20:32.209109+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 30, 2026 at 14:20 UTC  
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

**[Meta was secretly running on Google's Gemini the whole time and then got cut off for using too much](https://www.reddit.com/r/artificial/comments/1uj45np/meta_was_secretly_running_on_googles_gemini_the/)**

Saw this article today and it genuinely surprised me Meta has been using Gemini for customer service, ad tools, content moderation, all of it. and apparently chose it because it worked better than their own Llama models and then Google cut them off because Meta was consuming too much capacity. Now employees are being told to watch their token usage. This is the same company that was pushing staff to use more AI just a few months ago. Idk man, of all the companies to run out of AI capacity

17h ago

---

**[If AI stopped improving tomorrow, what would still have the biggest impact over the next 10 years?](https://www.reddit.com/r/artificial/comments/1ujjprk/if_ai_stopped_improving_tomorrow_what_would_still/)**

Imagine today's models are as good as they'll ever get—no better reasoning, no larger context windows, no new breakthroughs. Which existing AI capability do you think would still reshape industries the most over the next decade?

5h ago

---

**[A new... thing.](https://www.reddit.com/r/artificial/comments/1uji8tb/a_new_thing/)**

https://github.com/EDrTech/Working-memory-depth-recurrence https://gitlab.com/erikrudec-group/Working-memory-depth-recurrence https://codeberg.org/erikrudec/Working-memory-depth-recurrence/ This is a demonstration, in pure python, of a different way of making, well, AI. No backprop, no gradients, no weight transport, only local rules. Everything learns on one graph, and you can run all of it on almost anything. Have you ever seen an LLM solve the S4 or S5 card shuffle problem? I have something here that trains in under two seconds from scratch and does the full 52 card deck. You hand it a deck and a thousand shuffles, and it tells you the exact order the deck ends up in. It only ever learned from short examples, it was never trained on long sequences. It can also recover from bad training. If you teach it badly first and it only memorizes, you can teach it properly on top of the same thing, and it starts to actually understand, without forgetting what it already knew. There are three small demos in here. The first one learns what numbers are by counting piles of things (characters, words, anything), and then it adds, even though it was never shown a single sum. The second learns what each shuffle does to a deck, and then predicts any deck after any number of shuffles, up to the full 52. The third one gets trained quickly and just memorizes, then gets taught properly and comes to understand, on the same memory, with nothing forgotten. The whole engine is about 60 lines of python and you can read it top to bottom. There is no code in there that knows anything about counting or shuffling. So you do not have to take my word for any of this. You clone it, run it with nothing installed, and read the engine. The demos themselves are not really in question, you can check every number by hand in a few minutes. What I am unsure about is the big claim I am building on top of them. The claim I have almost fully convinced myself of is that working memory depth recurrence is the backbone of a real, faithful brain abstraction, one that behaves on silicon almost exactly like it behaves in biology. Working memory depth recurrence is the fix for the bound depth problem. Depth goes from being an impossible problem to a simple series of serial operations, and you get it almost for free. You do not need a two billion dollar cluster, you need some memory and you need to spend compute time instead of brute force compute. It all happens on the one unified graph. The basic operations get taught, and you can watch the higher level rules emerge from there. You teach it to count on piles of things, and it generalizes to the rest. What I am releasing is the single most important piece for this to work, but it is far from the only thing needed. I built more on top of this backbone to get higher complexity abstractions to emerge, and it did happen, and it stacks very well on top of this. I might have talked myself into a state where I really believe I have THE thing. So I fully expect people who actually have the AI know how to check whether this amounts to anything. Partly to keep my own sanity, because if this is the thing, it is very weird that I got here through a lot of stubborn ignorance. I am not a data scientist and not an ML engineer. I know the principles of how it all works, but the terminology in this field is too complicated and it always drags you down the backprop and global rules route. I hated how LLMs behave. I figured they are set up wrong from the ground up, so I set myself the task of doing it properly, and I just stubbornly went against the standard way and deconstructed how my own brain does things. So check it out and see for yourself. I would really appreciate it if you told me whether this is all a big fever dream of mine, and saved me the further embarrassment. And if it is real, I fully believe this belongs to everyone, and no single person or company should have a monopoly on it. Thanks! EDIT: added demo on huggingface: https://huggingface.co/spaces/ErikRudec/Working-memory-depth-recurrence

6h ago

---

**[Ford rehires veteran engineers after AI fails to meet quality standards](https://www.reddit.com/r/artificial/comments/1uiwmnm/ford_rehires_veteran_engineers_after_ai_fails_to/)**

Ford said it had hired, promoted or brought back around 350 veteran engineers after discovering that AI alone could not match experienced staff.

🔗 [Dexerto](https://www.dexerto.com/entertainment/ford-rehires-veteran-engineers-after-ai-fails-to-meet-quality-standards-3380736/) • 22h ago

---

**[An audiovisual technique I've been working on - [and made it open-source]](https://www.reddit.com/r/artificial/comments/1ujqb6y/an_audiovisual_technique_ive_been_working_on_and/)**

A new output example from the updated version of my experimental multi-source video player for TouchDesigner, designed for frame-accurate video switching, playback manipulation, and display/render interventions. [And now, by popular demand, allowing even more video sources!] Want access to the updated system + a detailed breakdown of exactly how I achieved the continuous motion effect on this piece? You can freely access the system from the Store, and the detailed breakdown from my Patreon. Plus, many more experiments through my Instagram profile.

10m ago

---

**[How Do You Automate Getting Web Design Clients?](https://www.reddit.com/r/artificial/comments/1ujp086/how_do_you_automate_getting_web_design_clients/)**

So I've seen a lot of people on Reddit asking how to get web design clients, so I figured I'd make a post about what's been working for me. If you don't run a web agency, this probably isn't for you. One of the biggest lessons I've learned in my 4 years running a web agency is that the best businesses to target are the ones that already have a website. There are 3 simple reasons for that. First, the number of businesses with outdated websites is way higher than most people think. I'm talking about websites with outdated designs, poor mobile optimization, slow loading speeds, weak SEO, and confusing layouts. Second, the fact that they already have a website proves one important thing. They understand the value of having one. You don't have to convince them that a website is important because they've already invested in it before. Third, selling becomes much easier because they're already familiar with paying for a website. In many cases they're still paying monthly for hosting or maintenance, so paying to improve it isn't a completely new idea to them. Now that we know who to target, how do we actually reach them? Personally, I recommend email outreach. The problem is that manually reviewing websites and writing personalized emails for every business takes forever. Instead, I'd automate the whole process. I use a tool called Swokei. You upload a list of businesses with websites, it automatically analyzes each one, then turns issues with design, layout, speed, mobile optimization, and SEO into personalized outreach emails. Not generic reports that business owners don't care about. Actual emails explaining what's wrong with their website, why it matters, and how it could be affecting their business. That allows you to send outreach at scale while still keeping every email relevant. In my experience, this leads to much higher reply rates because you're pointing out something specific that's potentially hurting their business. That naturally creates urgency while also giving you the opportunity to offer a solution. This is the approach I've been using for a while now, and it consistently brings me an interested reply rate of around 5–9%. I'm curious how everyone else is getting web design clients these days.

1h ago

---

**[Before I needed it, no one told me that "legacy tape management" was an entire industry.](https://www.reddit.com/r/artificial/comments/1ujoosc/before_i_needed_it_no_one_told_me_that_legacy/)**

We inherited roughly 6,000 LTO tapes from a business we bought last year. There was no documentation, no drives that could read half of them, multiple generations and different formats. spent three weeks attempting to come up with an internal solution before someone recommended outsourcing the entire process. didn't know there were services like that, businesses that specialize in large-scale tape to cloud migration, evaluate what you have, read the formats and transfer everything.

1h ago

---

**[Open vs Closed AI Models: How the Gap Collapsed in 2025-2026 and Where It's Heading](https://www.reddit.com/r/artificial/comments/1ujokka/open_vs_closed_ai_models_how_the_gap_collapsed_in/)**

In January 2025, a Chinese lab most people had never heard of released an open model that wiped roughly seventeen percent off the value of the most valuable chipmaker on earth in a single day. Eighteen months later, the question is no longer whether open models can compete with the closed systems fr

🔗 [abZ Global](https://abzglobal.net/technology/open-vs-closed-ai-models-gap-2025-2026) • 1h ago

---

**[Copilot agents can take actions. But who verifies the results?](https://www.reddit.com/r/artificial/comments/1ujo832/copilot_agents_can_take_actions_but_who_verifies/)**

As Copilot agents become more autonomous, validation seems just as important as automation. How are you handling it?

1h ago

---

**[To fix the machine that replaced you — a long winded ramble.](https://www.reddit.com/r/artificial/comments/1ujeh8r/to_fix_the_machine_that_replaced_you_a_long/)**

Greetings all, and welcome to my TED talk. Please allow me to preface this with the following disclaimer: I am autistic, and when writing things like this, I have been known to be mistaken for AI on occasion. I'm not really sure how to prove that I'm not, so instead I'll just hope that you take me at my word. To set the tone of this, I am posing a moral quandary. All opinions are valid here, I am not looking for people to just pat me on the back and tell me my decision is okay (though if that happens, that's okay too). Now, for a bit of background: I went to a technical school that specialized in replacing the need for college with learning a trade. The shops at the time were mostly manual labor type stuff (building cars, houses, plumbing, HVAC, whatever that manly stuff is) then a few more creative things that I have never had skill with (graphic art, marketing, drafting and design, cooking, et cetera), and then one shop that I found I had a knack for: electronics technology. By senior year I had built a little robot that helped greet the new students, and would do the six flags "old-man" dance (dating myself a bit there). I graduated, and immediately found out that not one single person cared that I could build a robot, it was a time where you needed a degree to work in that kind of field. So I went and got one. It was a hard pull, ended up living in my car to pay tuition (murica) and finally got my bright and shiny degree, a bachelor's in Computer and Electrical Engineering from the esteemed DeVry university. They taught me a lot about coding, and even helped me land a sweet gig right out of college for $80,000 a year, which was more money than I ever even imagined at the time. Well, turns out, that job was specialized in replacing people. During the interview/on boarding process, they showcased things like automated forklifts, and cars parallel parking themselves. It was really neat to look at, until I was face to face with the result of our systems. Code that was maintained by six of us was being bought for several hundred thousand dollars, and then hundreds of workers were being sent home with no fall back. My boss used the same advice that is always given in these situations: they can go back to school and learn to fix the machine that replaced them. Seemed like a great plan, except there were six of us, and hundreds of them, even if every single one of them had the mental capacity to do the job, it wasn't happening. I lost sleep over it, and eventually waved goodbye to that job to look for other work. Only to find that pretty much everyone at the time was also trying to build systems to replace people. So I left the field. Joined the Navy, wrote a bit, fell in love, lived my life. And every once in a while I'd dust off my programming to make a little tool to help me with something. After the Navy, I entered the field of ghostwriting. For those unaware, that's basically "AI write me a book" only I was the AI. I didn't make great money doing it, but I made a living, and I loved the work, and that was enough for me. Whelp, as it turns out, people who are willing to pay a person to write something they take credit for writing are almost entirely just as willing to have ChatGPT do it for free. As such, I became the man replaced by the machine. So I did what the age old advice recommended, and I learned the machine. I dove hard into figuring out how to make ChatGPT work for me, and used it to develop a bit of software based on my existing software. The more I experiment, the more I realize that there is a lot more to it than "tell a chat bot 'make me Zelda, Link to the Past'" and clicking play. My knowledge of programming actually comes in handy, and I can do things in days that would have taken me years. Now we (finally) get to the question of morality. One of the biggest complaints I see about the use of AI is that it replaces people in the creative process. It won't be doing that with me, I'll be writing all the story (and some of the code). I have an artist as well, the same one I used for my covers, to design artistic things for games. Games that don't replace people. One of the biggest secondary concerns I see with it is about the environment. As of yesterday I've started the ball rolling on getting a PC setup that can run opensource AI locally, so no data centers involved at all. So people doing the creativity, check. Environment just as impacted as if I were just playing Baldurs Gate 3 on my PC, check. Doesn't take anyone's jobs, just saves me the time of having to do every line (of millions of lines) of code myself, check. Fully intend on being up front and honest regarding the use of AI in development of code, check. Am I missing some ethical dilemma that I haven't yet considered? Have I missed some aspect of the ones I'm considering solved? Or am I just overthinking it because "AI yucky" is such an easy stance to have? Thanks for coming to my TED talk, I look forward to hearing your responses.

10h ago

---

---

## Google News: "ai"

**[Ford rehires human engineers after AI fails to match quality checks](https://www.bbc.com/news/articles/cgrkd41n2v9o)**

The car-maker found AI quality checks failed to match the skill of veteran technicians.

BBC • 1d ago

---

**[Opinion | The One Very Simple Reason A.I. Won’t Steal All Our Jobs](https://www.nytimes.com/2026/06/30/opinion/ai-agents-steal-jobs-employment.html)**

The New York Times • 5h ago

---

**[AI Chip Startup Etched Says Jane Street, TSMC-Linked VC Invested](https://www.bloomberg.com/news/articles/2026-06-30/ai-chip-startup-etched-says-jane-street-tsmc-linked-vc-invested)**

Bloomberg.com • 20m ago

---

**[Companies Are Making Claude and Codex Talk Like Cavemen to Stop AI’s Soaring Costs](https://www.404media.co/companies-are-making-claude-and-codex-talk-like-cavemen-to-stop-ais-soaring-costs/)**

A senior OpenAI employee has contributed code to the project, simply called 'caveman.'

404 Media • 45m ago

---

**[Silicon Valley’s go-to fixer on AI’s unfixable problem](https://www.yahoo.com/news/politics/articles/silicon-valley-fixer-ai-unfixable-140011141.html)**

Bradley Tusk says consumers won’t rally behind the technology.

Yahoo • 20m ago

---

**[Mag 7 value shrinks by $2.3 trillion amid AI spending jitters — but investors are still backing chipmakers](https://www.cnbc.com/2026/06/30/magnificent-7-stocks-sell-off-investors-grow-jittery-on-ai-spending.html)**

Investors are growing jittery about massive AI spending by the Mag 7 and when these companies will produce a return on that investment.

CNBC • 4h ago

---

**[The AI boom's historical warning](https://www.axios.com/2026/06/30/ai-boom-bis-warning)**

Axios • 5h ago

---

**['Humanity has chosen to become idiots': This Brown professor switched to take-home exams after a mass shooting and discovered mass cheating](https://fortune.com/2026/06/29/roberto-serrano-brown-university-massacre-ai-cheating/)**

Roberto Serrano literally wrote the book on game theory, but he's befuddled: "Why are you at a university if you refuse to learn, you refuse to work hard?"

Fortune • 16h ago

---

**[Four days to make victims fall in love: How global scammers use US tech to fleece people](https://apnews.com/article/scams-fraud-technology-ai-impostor-scam-phishing-12f549d5203abd38857c4e2f2fb1c986)**

Technology from American companies is being used to power a revolution in the scam industry, playing a key role in the industrialization and globalization of fraud in ways that have not been clear until now, an AP/“FRONTLINE” investigation has found.

AP News • 9h ago

---

**[How Microsoft became the black sheep of the AI trade](https://www.businessinsider.com/microsoft-stock-price-outlook-ai-trade-oracle-parallels-black-sheep-2026-6)**

Shares are on pace to lose 18% in June, which would be Microsoft's worst month since 2000.

Business Insider • 4h ago

---

---

## HackerNews: "ai"

**[Professor denounces mass AI fraud on an exam at Brown](https://news.ycombinator.com/item?id=48708991)**

The renowned economist Roberto Serrano has ‘overwhelming evidence’ that his students cheated. He thinks the time has come for an in-depth debate so the technology does not signal the end of higher education

⬆️ 543 • 💬 713 • 1d ago • [EL PAÍS English](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html)

---

**[Librepods: AirPods liberated](https://news.ycombinator.com/item?id=48710232)**

AirPods liberated from Apple's ecosystem. Contribute to librepods-org/librepods development by creating an account on GitHub.

⬆️ 491 • 💬 179 • 1d ago • [GitHub](https://github.com/librepods-org/librepods)

---

**[The best response to AI slop and online noise is from Robin Williams](https://news.ycombinator.com/item?id=48703452)**

There's a moment in the movie  Good Will Hunting  which perfectly summarizes all the problems with AI slop and online noise and infinite advice content.  Sean (played by Robin Williams) is sitting next to Will (Matt Damon) on a bench in Boston Public Garden. I live here, so I know it well. The area

⬆️ 399 • 💬 219 • 2d ago • [Jay Acunzo](https://jayacunzo.com/blog/your-move-chief)

---

**[Tidal AI Policy](https://news.ycombinator.com/item?id=48718840)**

⬆️ 302 • 💬 342 • 1d ago • [tidal.com](https://tidal.com/ai-policy)

---

**[Ford hired AI and sacked humans. It backfired badly](https://news.ycombinator.com/item?id=48703968)**

‘We didn’t pay as much attention as we should have to the experience of our most knowledgeable engineers,’ says automaker

⬆️ 239 • 💬 4 • 2d ago • [The Independent](https://www.the-independent.com/tech/ford-ai-automation-human-workers-b3003787.html)

---

**[Working With AI: A concrete example](https://news.ycombinator.com/item?id=48720064)**

In this essay, Carson Gross walks through a concrete bug fix in hyperscript to show where AI helped, where it fell short, and why keeping a knowledgeable human in the loop is what kept complexity in check.

⬆️ 173 • 💬 62 • 23h ago • [htmx.org](https://htmx.org/essays/working-with-ai/)

---

**[Google limits Meta's use of its Gemini AI models](https://news.ycombinator.com/item?id=48707103)**

Meta had sought more computing capacity than Google could provide, the Financial Times reports.

⬆️ 159 • 💬 72 • 2d ago • [CNBC](https://www.cnbc.com/2026/06/28/google-limits-metas-use-of-its-gemini-ai-models-ft-reports.html)

---

**[AI boom risks global financial crash, warn central bankers](https://news.ycombinator.com/item?id=48713697)**

Reversal of ‘excessive’ tech investments could have serious economic consequences, report finds

⬆️ 157 • 💬 210 • 1d ago • [The Telegraph](https://www.telegraph.co.uk/business/2026/06/28/ai-boom-risks-global-financial-crash-central-bankers-warn/)

---

**[We need tech news sources which exclude AI](https://news.ycombinator.com/item?id=48713041)**

⬆️ 137 • 💬 84 • 1d ago

---

**[Ford rehires 'gray beard' engineers after AI falls short](https://news.ycombinator.com/item?id=48710749)**

"Mistakenly we thought that by just introducing artificial intelligence ... that would produce a high-quality product.”

⬆️ 135 • 💬 3 • 1d ago • [TechCrunch](https://techcrunch.com/2026/06/28/ford-rehires-gray-beard-engineers-after-ai-falls-short/)

---

---

## YouTube Videos: "ai"

**[Anthropic Just Confirmed It: The 2028 AI Warning Is Real](https://www.youtube.com/watch?v=j1xcsDxSb_Y)**

Self-improving AI is starting to look real. Anthropic's Jack Clark put a 2028 timeline on recursive self-improvement, Google ...

📺 AI Revolution

👁️ 45K • 👍 1K • 💬 141 • ⏱️ 13:32 • 1d ago

---

**[Scientists Asked Grok AI How Egyptians Cut Granite — The Answer Shocked Everyone](https://www.youtube.com/watch?v=c_uBDJqclHA)**

Scientists Asked Grok AI How Egyptians Cut Granite — The Answer Shocked Everyone What if artificial intelligence could help ...

📺 Curious Explorer

👁️ 807K • 👍 3K • 💬 501 • ⏱️ 28:24 • 1d ago

---

**[China’s AI Has Apple PANICKING, DeepSeek&#39;s Billions, and the Californication of Food | China Decode](https://www.youtube.com/watch?v=F2NefjHkHnE)**

Alice Han and James Kynge dig into why Apple is lobbying the Trump administration for permission to buy memory chips from a ...

📺 The Prof G Pod – Scott Galloway

👁️ 9K • 👍 388 • 💬 66 • ⏱️ 50:13 • 6h ago

---

**[AI vs the Permanent Underclass: the End of Coding](https://www.youtube.com/watch?v=oTQzszSabhY)**

We told a generation to "learn to code," and then AI rugpulled everyone. Welcome to the AI singularity. [NEW] Official TechLead ...

📺 TechLead

👁️ 48K • 👍 2K • 💬 567 • ⏱️ 13:10 • 21h ago

---

**[I&#39;M OUT: The $11 Trillion AI Bubble is Breaking!](https://www.youtube.com/watch?v=RdHnOK4uJMw)**

The $11 trillion AI bubble is reaching its breaking point. In this video, I'm showing you the institutional data from Goldman Sachs ...

📺 Steven Van Metre

👁️ 42K • 👍 2K • 💬 178 • ⏱️ 16:05 • 16h ago

---

**[U.S. eases restrictions on Anthropic&#39;s Mythos AI model](https://www.youtube.com/watch?v=RkN8TmQPPs4)**

The Trump administration is allowing Anthropic to restore access to its Mythos 5 AI model for a select group of U.S. companies ...

📺 CBS News

👁️ 4K • 👍 36 • 💬 13 • ⏱️ 3:06 • 17h ago

---

**[US Government Blocks GPT-5.6, Alibaba&#39;s AI Theft, and Why OpenAI Is Stalling Their IPO | #267](https://www.youtube.com/watch?v=-H7J_-zr7pA)**

This episode is mainly about the U.S. government putting frontier AI behind a gate, China's accelerating open-weight and ...

📺 Peter H. Diamandis

👁️ 71K • 👍 2K • 💬 580 • ⏱️ 2:17:59 • 18h ago

---

**[The AI Bubble Just Ended - Without Popping](https://www.youtube.com/watch?v=0Pdd2__OHVQ)**

Get my free newsletter Letters From a Heretic: https://go.heresy.financial/letters-from-a-heretic TIMECODES 00:00 The AI Bubble ...

📺 Heresy Financial

👁️ 26K • 👍 1K • 💬 138 • ⏱️ 6:52 • 1d ago

---

**[Trump HUMILIATED As BRUTAL New AI MEMES Go VIRAL!](https://www.youtube.com/watch?v=eH1U5LGyhIw)**

Really American host Steve Harness breaks down everyone's favorite time of the week: new Trump AI-slop memes! And these ...

📺 Really American

👁️ 58K • 👍 8K • 💬 364 • ⏱️ 12:26 • 1d ago

---

**[GPT 5.6 Sol Just Blew Up The AI World](https://www.youtube.com/watch?v=_AoyQcIoquA)**

OpenAI just launched GPT 5.6, but this is not a normal release. Access is limited to trusted partners after U.S. government ...

📺 AI Revolution

👁️ 44K • 👍 1K • 💬 200 • ⏱️ 15:44 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 429,056 • ❤️ 1,442 • 2d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 970,663 • ❤️ 1,015 • 1d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 142,547 • ❤️ 2,998 • 7d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 157,418 • ❤️ 509 • 4d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 28,480 • ❤️ 454 • 5d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 257,216 • ❤️ 870 • 11d ago

---

**[Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)**

*KREA*

Krea-2-Turbo is a text-to-image diffusion model capable of generating diverse artistic styles, including halftone, pixelated, impressionist, thermal imaging, and black and white photography. It is primarily used for creative image generation and artistic exploration.

`text-to-image`

⬇️ 45,668 • ❤️ 411 • 6d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 99,359 • ❤️ 578 • 1d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 98,750 • ❤️ 329 • 5d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 26,151 • ❤️ 295 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 43 • 💬 5 • ⭐ 12,335 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 72,432 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 89,799 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 22 • 💬 2 • ⭐ 8,625 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 249 • 💬 4 • ⭐ 10,160 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 11 • 💬 1 • ⭐ 9,794 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 26,224 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 84,866 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 23 • 💬 1 • ⭐ 84,278 • 28d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 78,758 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 68.6k • 🔱 3.5k • 14h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.1k • 🔱 1.1k • 7m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 5.7k • 🔱 716 • 3m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 4.3k • 🔱 558 • 3h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.2k • 🔱 191 • 2d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.2k • 🔱 169 • 2d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 152 • 4d ago

---

**[inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)**

Beautiful, AI-native markdown editor and LLM Wiki

`TypeScript` `2nd-brain` `agent-skills` `claude` `codex` `docs`

⭐ 1.6k • 🔱 77 • 8h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 87 • 17d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.4k • 🔱 55 • 12h ago

---

---

*Generated by PeekDeck - A glance is all you need*
