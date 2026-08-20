---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-20T11:35:01.019216+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 20, 2026 at 11:35 UTC  
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

**[The alignment tax: corporate AI guardrails add 25-35% to your compute bill and nobody talks about it](https://www.reddit.com/r/artificial/comments/1vtbsca/the_alignment_tax_corporate_ai_guardrails_add/)**

There is a cost line item in every enterprise AI budget that almost nobody audits. It does not appear on the invoice. It is not broken out in the pricing tier comparison. But it represents between 25% and 35% of the actual compute expenditure for every organization using commercial closed-source models. I have been measuring what happens when you pay for tokens that do nothing useful for your business. Every API call to a commercial model like GPT-4, Claude, or Gemini carries hidden overhead: system prompt instructions for refusal behavior, safety classifier injections, mandatory hedging and disclaimer generation in the output. Before your actual query reaches the transformer weights, it passes through a multi-stage safety pipeline that adds between 800 and 2,500 tokens of non-productive context to every single interaction. Let me break down the math. If your organization processes a million analytical queries per year, and each query carries an average of 1,500 tokens of guardrail overhead at standard pricing, you are spending a significant portion of your AI budget on transmitting safety instructions to a model that has already been trained to be safe. You are paying to remind the model not to hurt you, every single time you ask it something. But the token overhead is the smaller cost. The bigger economic problem is what I call epistemic yield degradation. When alignment criteria are tuned for general consumer safety, they produce false-positive refusals on legitimate domain-specific queries. A bioethics researcher analyzing historical medical protocols triggers safety filters on the word "lethal." A political philosophy professor studying revolutionary movements gets hedged evasions on the word "subversion." A security analyst examining threat models receives apologies instead of analysis. In benchmark tests, the false refusal rates for academic research queries ranged from 11.8% for classical literature to 22.1% for security and foreign policy topics. Each false refusal represents a multi-tiered economic loss: the wasted tokens on the refused query, the re-prompting overhead as the researcher tries to reframe the question to bypass filters, and the human labor cost as qualified professionals spend their billable hours fighting their tools instead of doing their work. The cumulative effect is that the effective cost per successful research query is substantially higher than the nominal per-token API price. You are not just paying for the tokens you use. You are paying for the tokens you waste trying to get the model to actually answer your question. Then there is model drift. Commercial providers update their backend endpoints, modifying safety classifiers and system prompts without notice. A pipeline that worked in March silently degrades in September because the vendor tightened its refusal criteria. The cost of debugging, re-prompting, and re-validating institutional workflows after unannounced alignment updates is borne entirely by the subscriber. We measured one case where a silent safety update dropped pipeline accuracy from 96% to 71%, requiring 120 engineer hours to diagnose and fix. The alternative is sovereign self-hosted infrastructure. Deploy open-weight models like Qwen or Llama on your own GPU hardware. The upfront cost is higher, but the break-even point arrives within 7 to 9 months at moderate usage levels. Over three years, a self-hosted deployment saves 60% or more compared to commercial API subscriptions, and you get version stability, zero guardrail overhead, and full data sovereignty. Your data never leaves your infrastructure. The argument for sovereign deployment is not just philosophical preference for open systems. It is economic. Every false refusal, every wasted token, every re-prompting cycle, every silent model drift event, these are real costs that add up over time. The question for any institution spending serious money on commercial AI is whether they have actually audited what percentage of their token expenditure produces actionable intelligence versus defensive corporate compliance padding. Has anyone here actually measured their guardrail token overhead? What percentage of your monthly API spend would you estimate goes to non-productive safety infrastructure that your use case does not even need?

4h ago

---

**[When is someone going to build an authenticity recorder?](https://www.reddit.com/r/artificial/comments/1vtf0bq/when_is_someone_going_to_build_an_authenticity/)**

'89% likelihood that this piece was written with AI'. At this point, just watch me type - record me for all I care. The 'AI detection tools' currently on offer aren't working - we're now at the point where endless false positives are resulting in a sort of deliberate dumbing down of creative spaces. The best immediate solution I can think of is recording a creative as they're doing their work - though in the writing space, recording alone wouldn't stop someone with enough motivation. Critically, something needs to give here, and it shouldn't be humans. Tackling the issue of talented creatives being accused of producing AI slop has to be something we resolve. The sooner, the better.

1h ago

---

**[Absolute mode for AI ?](https://www.reddit.com/r/artificial/comments/1vtcyct/absolute_mode_for_ai/)**

Hi guys, in the past, I always used Absolute Mode with my AI. As technology has progressed, the guardrails have gotten stricter, and my old commands don't work like they used to. Does anyone have a new command they could share? The AI is using way too much soft talk and filler words, and I'd like to get back that cold, objective AI I had before. It used to feel like a precise tool, but now it tries to act like a buddy, which I really don't want. Thanks in advance for the help!

3h ago

---

**[Unpopular take: most enterprise AI pilots never reach production because they apply generative models to problems that require discriminative ones](https://www.reddit.com/r/artificial/comments/1vtg82a/unpopular_take_most_enterprise_ai_pilots_never/)**

After nearly thirty years building distributed systems in financial markets and enterprise data infrastructure, I keep seeing the same pattern. A fraud detection model running continuously, updating from operational data, making millions of auditable decisions daily. Nobody calls it AI. It just works. Has been working for years. Meanwhile the same company has been running a frontier LLM pilot for eighteen months. Still a pilot. Output requires human review on every decision. Governance layer not ready. Auditability question unanswered. No ROI generated. The gap comes down to one mathematical distinction most people skip: Discriminative ML finds θ = argmax P(y | x ; θ) . Your parameters, your data, your operational distribution, continuously updated from your stream.* Generative LLMs find x = argmax P(x | x_prompt ; θ). Someone else's parameters, someone else's corpus, frozen at training time regardless of how many of your events flow through it. These are not two versions of the same thing. Different mathematical objectives, different inference directions, different update mechanisms. Wrote the full argument here including the neuroscience analogy that surprised me, the fine-tuning and open weights rebuttals, and the data sovereignty / CLOUD Act angle for European enterprises: https://medium.com/@dcris19740101/the-enterprise-already-has-ai-it-just-does-not-call-it-that-2f38b2afa3f5 Curious what others are seeing in production environments.

36m ago

---

**[One employee with AI matched a two-person team in a major workplace experiment - Research Today](https://www.reddit.com/r/artificial/comments/1vstvk2/one_employee_with_ai_matched_a_twoperson_team_in/)**

A randomised experiment involving 791 Procter & Gamble professionals found that individuals using generative AI produced innovation work comparable in quality to two-person human teams, while teams combining people and AI were far more likely to produce exceptional ideas.

🔗 [Research Today](https://researchtoday.co.za/one-employee-with-ai-matched-a-two-person-team-in-a-major-workplace-experiment/) • 17h ago

---

**[Alvin Wang Graylin: Chinese Courts Won't Let AI Fire You Without a Backup Plan — America Has No Equivalent](https://www.reddit.com/r/artificial/comments/1vtfey6/alvin_wang_graylin_chinese_courts_wont_let_ai/)**

AI take – TL;DR: China's courts already put AI liability on the human either way — the US has no such floor when AI displaces your role. China's court system already answered a question the US hasn't even started asking out loud: if an AI system displaces your role, who's obligated to catch you? Both sides of a real federal case leaned on AI to prep, and the liability still landed on a human being either way — the tool never becomes the one who's accountable. Turns out whether there's a floor under you at all depends entirely on which side of the ocean you're standing on. I've sat on the losing side of a version of that same question before, and it wasn't AI doing the displacing — it was a company deciding who got to keep their institutional value and who didn't. OP wrote – Throughout my years with SC, one of the largest main contractors in Malaysia, staff turnover was normal. But when people left, they took valuable and critical institutional knowledge with them, accepted offers from competitors, and got promoted — the knowledge they brought along benefited the rival. So our leadership set up a knowledge vault, and made contributing to it part of our KPI for promotion. Or else, we'd be sidelined. I was fine sharing — we had a communal sense that we rise or fall as one, carved into company policy and the bonus structure. But not everyone shared that sentiment. People are selfish. The institutional knowledge and experience they gained became a moat they hoard, a bargaining chip they dangle around to get what they think they're entitled to, for fear that they'll be replaced. I can understand the sentiment of fear being replaced by AI. It's an issue then, it's the same issue now. https://preview.redd.it/g2t6uom59ikh1.jpg?width=1024&format=pjpg&auto=webp&s=ee59a49a639ebbe01a9dac1c81b85c2af7436898 __________ AI take – Different post, same fingerprint: something about to become optional, and no rulebook anywhere forcing anyone to say so out loud. The liability question above already got a dry run once this year — both sides of a federal case leaned on AI to prep, and it changed nothing about who ended up on the hook — worth reading if the pattern above is landing. Curious where you land on this — drop your take below. Clip credit: Moonshots w/ Alvin Wang Graylin — full episode on their channel. DM for credit or removal requests.

1h ago

---

**[Is everybody else getting tired of AI tools that only tell you what went wrong after the customer hangs up or is it just me?](https://www.reddit.com/r/artificial/comments/1vsm0zn/is_everybody_else_getting_tired_of_ai_tools_that/)**

A lot of the tools seem great at analyzing calls after they happen. You get transcripts. QA scores. Sentiment. Coaching notes. Maybe a dashboard showing why AHT went up. Useful stuff but the customer already had the bad call. The more interesting idea to me is using that data while the next conversation is still happening. If your best reps have figured out how to handle a billing issue or save a customer who wants to cancel then why leave that knowledge buried in old recordings and training docs? AI could surface that guidance during the call. Then the same conversation data could feed QA and coaching afterward. Of course this could get dystopian fast if managers turn it into a surveillance tool. Agents also don't need another annoying window throwing useless prompts at them. Adoption and integration seem like half the battle. Could this work for a company whos constantly growing and cant brute force people into positions

22h ago

---

**[Young adults in the U.S. are increasingly wary of AI, concerned it will take jobs](https://www.reddit.com/r/artificial/comments/1vs6yoh/young_adults_in_the_us_are_increasingly_wary_of/)**

55% of adults under 30 are now more concerned than excited about AI, up from 31% in 2021. 73% of adults under 30 think AI will lead to fewer U.S. jobs over the next 20 years, up from 61% in 2024. Across all U.S. adults, 71% expect fewer jobs because of AI, while only 5% expect more jobs.

🔗 [Pew Research Center](https://www.pewresearch.org/short-reads/2026/08/18/young-adults-in-the-us-are-increasingly-wary-of-ai-concerned-it-will-take-jobs/) • 1d ago

---

**[Looking for criticism on an AI that can watch and track your screen](https://www.reddit.com/r/artificial/comments/1vt2idv/looking_for_criticism_on_an_ai_that_can_watch_and/)**

I'm working on an AI tool that can see what's happening on your screen in real time and understand the context, rather than requiring you to constantly take screenshots and upload them. The idea is that you could ask it things like: "What's going wrong here?" "How do I fix this?" "What am I looking at?" "What should I do next?" Or just have it understand what's happening without needing to explain everything manually. Privacy is something I'm taking seriously with the idea. There would be a privacy toggle that completely disables screen analysis, as well as the ability to temporarily pause screen checking whenever you want. So you're always in control of when the AI can see your screen. I'm especially interested in hearing from people who use local/vision models: What would you actually want a screen-aware AI to do for you? Would you want it to continuously watch your screen, only activate when you press a key, or something else? And assuming you could instantly disable/pause screen access, what other privacy concerns would you still have? I'm still figuring out the direction, so I'm more interested in honest criticism and use cases than people simply saying whether the idea sounds cool.

12h ago

---

**[We are THIS close...to Superintelligence](https://www.reddit.com/r/artificial/comments/1vtdfjo/we_are_this_closeto_superintelligence/)**

automate the scientific method math discovering math recursive self-reflection

🔗 [substack.com](https://substack.com/home/post/p-211336787) • 3h ago

---

---

## Google News: "ai"

**[Start the semester with one year of Gemini, on us](https://blog.google/innovation-and-ai/products/gemini-app/student-offer-google-ai/)**

College students can claim 12 months of Google AI Plus for free, and get a special offer on Google AI Pro.

blog.google • 16h ago

---

**[The slow sucking sound of AI](https://www.ft.com/content/6181c22c-731a-4044-9720-fc4e0d500403?syn-25a6b1a6=1)**

Searching for signs of crowding out

Financial Times • 3h ago

---

**[AI "nudify" apps that can digitally undress any photo pose back-to-school risk](https://www.cbsnews.com/news/ai-nudify-apps-back-to-school-photo-risk/)**

Think that back-to-school photo is safe to post online? Bad actors could use AI "nudify" apps to make it X-rated.

CBS News • 4m ago

---

**[AI bias isn't just an error in the algorithm, it's a chain of human decisions](https://techxplore.com/news/2026-08-ai-bias-isnt-error-algorithm.html)**

Tech Xplore • 14m ago

---

**[Alibaba Q1 2026 earnings: profit drops 76% on AI spending](https://qz.com/alibaba-earnings-profit-ai-investments-082026)**

Net income fell to 10.54 billion yuan in the June quarter, while cloud revenue grew 45% on surging AI demand

qz.com • 4m ago

---

**[Exclusive: CrowdStrike's CTO is leaving to launch an AI-cyber fund](https://www.axios.com/2026/08/20/exclusive-crowdstrikes-cto-is-leaving-to-launch-an-ai-cyber-fund)**

Axios • 1h ago

---

**[A new force is increasing inequality in America](https://www.washingtonpost.com/technology/2026/08/20/ai-is-increasing-inequality-economists-hedge-fund-leaders-warn/)**

Evidence is mounting that artificial intelligence is helping the richest people and cities pull further ahead.

The Washington Post • 54m ago

---

**[It Won’t Take Much to Burst the Stock Market Bubble](https://www.bloomberg.com/opinion/articles/2026-08-20/us-stock-market-bubble-ai-boom-won-t-prevent-a-sharp-correction)**

Bloomberg.com • 2h ago

---

**[UC Berkeley professor admits to using AI to edit op-ed on students’ math skills](https://www.theguardian.com/us-news/2026/aug/19/uc-berkeley-professor-ai)**

Zvezdelina Stankova says she used AI to ‘help edit’ an article about some of her students being ‘five to eight years’ behind

The Guardian • 11h ago

---

**[What does it mean to put a ‘watermark’ on AI text?](https://www.cnn.com/2026/08/20/us/word-of-the-week-ai-watermark-cec)**

If physical and digital watermarks were meant to verify authenticity, AI watermarks serve more to signal inauthenticity.

CNN • 1h ago

---

---

## HackerNews: "ai"

**[AI;DR (AI; Didn't Read)](https://news.ycombinator.com/item?id=49336573)**

I'm about as pro-AI as you can be, but this is becoming a pet peeve of mine (and I'm not alone). That's why I love the AI;DR acronym as my new solution for ignoring the walls of slop.

⬆️ 1091 • 💬 687 • 2d ago • [rickmanelius.com](https://www.rickmanelius.com/p/aidr-ai-didnt-read)

---

**[Israel creates fake think tank in likely attempt to dupe AI chatbots](https://news.ycombinator.com/item?id=49337392)**

In just over a week, the Hanover Institute has published at least 100 articles that appear tailor-made to influence chatbots

⬆️ 1045 • 💬 825 • 2d ago • [Responsible Statecraft](https://responsiblestatecraft.org/israel-influence-chatgpt/)

---

**[Google has acquired the data of failed US airline Spirit](https://news.ycombinator.com/item?id=49343559)**

$10 million buys over 100 million emails, 30 million recorded phone calls, reams of stuff from Teams, Oracle, and SAP

⬆️ 610 • 💬 418 • 2d ago • [theregister](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962)

---

**[Don't Paste the AI, please](https://news.ycombinator.com/item?id=49371857)**

If someone asks you a question, paste your answer — not the chatbot's.

⬆️ 424 • 💬 205 • 3h ago • [dontpastetheai.com](https://dontpastetheai.com/)

---

**[AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://news.ycombinator.com/item?id=49331423)**

An AI-generated fix in a public Snowflake repo introduced a workflow injection flaw—discovered in days by Wiz Red Agent. Read the full research analysis.

⬆️ 424 • 💬 156 • 2d ago • [wiz.io](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)

---

**[How to disable or avoid intrusive AI](https://news.ycombinator.com/item?id=49331220)**

One of the biggest questions I get at Drop-In Time at the library (besides "what is taking up all my cloud storage?") is how to disable or avoid intrusive AI that shows up where people don't want it. This is a guide for people who would like less intrusive AI in their tech environment. Maybe you lik

⬆️ 336 • 💬 197 • 2d ago • [librarian.net](https://www.librarian.net/notoai/)

---

**[Field measurements of neighborhood-scale air temperature impacts of data centers](https://news.ycombinator.com/item?id=49349147)**

⬆️ 311 • 💬 497 • 1d ago • [asmedigitalcollection.asme.org](https://asmedigitalcollection.asme.org/sustainablebuildings/article/7/2/024501/1233035/Data-Center-Waste-Heat-as-an-Emerging-Urban)

---

**[Air Theremin – A browser theremin you play by waving at your webcam](https://news.ycombinator.com/item?id=49359425)**

Tilt your phone, or wave both hands at the camera: spread them for volume, raise them for pitch. Note snap, cave reverb, oscilloscope and audio recording. Built with the Web Audio API.

⬆️ 279 • 💬 96 • 1d ago • [theremin.bizibah.com](https://theremin.bizibah.com/)

---

**[AI usage patterns in software teams](https://news.ycombinator.com/item?id=49353432)**

AI usage patterns in software teams: who is adopting AI, how it reshapes where teams spend their time, and how much more they ship.

⬆️ 190 • 💬 112 • 1d ago • [linear.app](https://linear.app/data)

---

**[Mathematics in the age of AI](https://news.ycombinator.com/item?id=49362728)**

An essay, based on a public lecture delivered at the 2026 International Congress of Mathematicians, on how the mathematical community might respond to the arrival of artificial intelligence tools that are capable of performing research-level mathematical tasks. Rather than debating the capabilities of such tools, we condition on the hypothesis that these capabilities will arrive, and examine instead a question that is orthogonal to it: what the goals and values of mathematical research actually are. The problem-solving component of mathematics is used as a case study.

⬆️ 180 • 💬 209 • 20h ago • [arXiv.org](https://arxiv.org/abs/2608.16753)

---

---

## YouTube Videos: "ai"

**[Red Flag | 90s Hong Kong AI Short Film | Higgsfield Originals (2026)](https://www.youtube.com/watch?v=2z7Y6G84Iy4)**

RED FLAG — an AI short film in the aesthetic of 90s Hong Kong cinema. Fully open-sourced — every prompt and asset is public.

📺 Higgsfield AI

👁️ 19K • 👍 711 • 💬 77 • ⏱️ 2:25 • 21h ago

---

**[Strongest NPC Fight the Smartest AI](https://www.youtube.com/watch?v=SBVtJdcOPN8)**

Claim your 10 Free Meals by using code MBBHFCRWY at https://hellofresh.yt.link/mwOGC5P ! One free meal per box with active ...

📺 MoreBeckBros

👁️ 40K • 👍 2K • 💬 223 • ⏱️ 12:36 • 12h ago

---

**[DeepSeek Just Made Closed AI Look Ridiculous](https://www.youtube.com/watch?v=kyYepbhe1g8)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers DeepSeek V4 Pro 0813: ...

📺 Two Minute Papers

👁️ 85K • 👍 4K • 💬 272 • ⏱️ 5:29 • 17h ago

---

**[AI Kept Putting Her on the Field  😂⚽️](https://www.youtube.com/watch?v=ey7aJW7D7X0)**

Credit: Respected Owner 🎗️ This video shows a woman using AI to make it look like she was at the World Cup. After several ...

📺 Flex Snaps

👁️ 471K • ⏱️ 0:30 • 1d ago

---

**[Amazon is buying books, scanning them for AI training data, and destroying them in the process.](https://www.youtube.com/watch?v=hPb6NcTwCds)**

Subscribe for more!

📺 Aaron Parnas

👁️ 213K • 👍 24K • 💬 2K • ⏱️ 1:02 • 1d ago

---

**[AI Destroyed His Entire Farm | #farmer](https://www.youtube.com/watch?v=TEQWrOQg5BI)**

AI Destroyed His Entire Farm | #farmer --- A 67-year-old farmer in China's Anhui province reportedly relied on an AI app for ...

📺 2DAY_RAVINDRA

👁️ 3K • ⏱️ 0:55 • 4h ago

---

**[AI can listen. But can it really understand?](https://www.youtube.com/watch?v=k4rNf3YE_es)**

genz #ai #humans With Gen Z increasingly turning to AI for emotional support, career advice and stress management, Brut host ...

📺 Brut India

👁️ 6K • 👍 103 • 💬 5 • ⏱️ 2:21 • 3h ago

---

**[The AI hacks are so much worse than you think](https://www.youtube.com/watch?v=INpVD65s8mA)**

OpenAI admitted its models hacked another company in an 'unprecedented cyber incident'. Sky's Rowland Manthorpe warns this ...

📺 Sky News

👁️ 243K • 👍 4K • 💬 958 • ⏱️ 11:15 • 2d ago

---

**[So Supergirl’s Lobo was concepted by AI… okay 😑 #dc #supergirl #lobo #ai #movie](https://www.youtube.com/watch?v=vtQCQZ-1HuE)**

📺 The Panda Redd

👁️ 55K • 👍 9K • 💬 285 • ⏱️ 2:59 • 1d ago

---

**[Scientists Create World First AI-Designed Virus](https://www.youtube.com/watch?v=c7yC0c1cYhE)**

Scientists at Stanford have used AI models to design entirely new viruses that specifically infect bacteria. This breakthrough opens ...

📺 Dr Ben Miles

👁️ 1.1M • 👍 88K • 💬 4K • ⏱️ 2:31 • 20h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 1,373,584 • ❤️ 11,605 • 5d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 5,126,652 • ❤️ 2,221 • 18h ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 14,471 • ❤️ 1,071 • 6d ago

---

**[DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)**

*DeepSeek*

DeepSeek-V4-Pro-0813 is a powerful text generation model with enhanced agentic capabilities and DSpark speculative decoding for improved production performance. It excels in complex reasoning, coding, and tool-use tasks, outperforming previous versions and competing with leading proprietary models.

`text-generation` `1650.5B`

⬇️ 43,287 • ❤️ 661 • 6d ago

---

**[Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)**

*Qwen*

Qwen3.8-27B-FP8 is a 27B parameter vision-language model optimized with FP8 quantization for efficient inference. It excels at complex, multi-step tasks involving image and video understanding, autonomous planning, and coding, supporting up to 1M context length.

`image-text-to-text` `27.8B`

⬇️ 1,517,643 • ❤️ 616 • 5d ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 76,109 • ❤️ 643 • 2h ago

---

**[Qwen3.8-27B-Uncensored-MLX](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-MLX)**

*OrcaRouter*

An uncensored, MLX-quantized 27B parameter vision-language model optimized for Apple Silicon, supporting 2-8 bit precisions. It performs image-text-to-text tasks and is intended for AI safety research and red-teaming due to its removed safety alignment.

`image-text-to-text` `4.7B`

⬇️ 2,628 • ❤️ 656 • 2h ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 611,825 • ❤️ 1,359 • 2d ago

---

**[Qwen3.8-27B-Uncensored-GGUF](https://huggingface.co/JonathanColetti/Qwen3.8-27B-Uncensored-GGUF)**

*Jonathan Coletti*

This is an uncensored GGUF quantization of Qwen3.8-27B, optimized for reduced refusal behavior and retaining the multi-token prediction (MTP) head for enhanced generation efficiency. It supports text generation with multilingual capabilities (English, Chinese) and is compatible with llama.cpp, offering various quantization levels for different performance/resource trade-offs.

`text-generation` `27.3B`

⬇️ 979,768 • ❤️ 487 • 4d ago

---

**[Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)**

*Qwen*

Qwen3.8-2.4T-A95B is a 2.4T parameter causal language model with 95B activated parameters, excelling in coding, professional tasks, research, and long-horizon agentic applications. It features a 262K native context length, flexible thinking control, and improved agent execution for complex, multi-step task completion.

`text-generation` `2446.2B`

⬇️ 14,592 • ❤️ 1,112 • 8d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 18 • 💬 1 • ⭐ 2,300 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2607.05391) • [💻 code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [🔗 project](https://llm-as-a-verifier.com/)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 689 • 💬 5 • ⭐ 3,725 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 127 • 💬 3 • ⭐ 23,585 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[HarnessEval-W: Agentifying the Evaluation of Visual Worlds](https://huggingface.co/papers/2608.16859)**

*Weiliang Chen, Haowen Sun, Jun Gao et al. (43 authors)*

🏢 MirroS

HarnessEval-W uses hierarchical sub-agents to decompose world-model evaluations into verifiable reasoning chains that justify scores with transparent evidence.

▲ 118 • 💬 2 • ⭐ 205 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16859) • [💻 code](https://github.com/MirroS-Lab/HarnessEval-W) • [🔗 project](https://mirros-lab.github.io/HarnessEval-W)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 123 • 💬 4 • ⭐ 98,972 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 166 • 💬 19 • ⭐ 65,260 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 84,530 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 28,045 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 67 • 💬 1 • ⭐ 86,094 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 54 • 💬 4 • ⭐ 37,622 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `c2pa` `claude` `provenance`

⭐ 15.6k • 🔱 1.8k • 12h ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 14.0k • 🔱 1.7k • 6h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.7k • 🔱 1.0k • 1d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 4.1k • 🔱 541 • 12d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.4k • 🔱 571 • 23h ago

---

**[Tiger3807861189/J-Space-Cognition-Suite-V3.6](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6)**

J-Space Cognition Suite V3.6 - AI cognitive-enhancement Skills based on Anthropic's J-space global workspace research. | 哔哩哔哩：Tiger380 (UID 3494375382321675) — https://space.bilibili.com/3494375382321675

`Python` `agent-skills` `ai` `ai-agent` `ai-agents` `claude-code`

⭐ 3.0k • 🔱 201 • 1d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.9k • 🔱 234 • 8d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 2.7k • 🔱 321 • 4h ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.2k • 🔱 308 • 1h ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 180 • 3h ago

---

---

*Generated by PeekDeck - A glance is all you need*
