---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-19T09:20:14.441609+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 19, 2026 at 09:20 UTC  
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

**[Gemini helped me get scammed](https://www.reddit.com/r/artificial/comments/1u9t7mp/gemini_helped_me_get_scammed/)**

I'll first acknowledge that this was completely my fault and I should not have trusted the information given to me by Gemini at face value. ​ I was in an extremely stressful airport situation dealing with lengthy flight delays while trying to make it to Seattle in time to start a backpacking trip with my friends. Long story short, I was traveling across multiple airports for more than 24 hours using different airlines trying to navigate the flight delays. Delta refused to give me a refund for a flight delayed over 5 hours. I asked Gemini to explain the laws to me to ensure I had all the facts for my next attempt to get a refund. In its explanation, Gemini gives me the phone number for Delta airlines. I call and the very competent agent explains that he can get me on an earlier flight if upgrade my seat for $230. In my stressed, restless delirium, this was a no brainer. I pay up over the phone and try to "lock in" my purchase with the gate agent at the airport. It immediately became clear to me that I had not been speaking with a Delta agent on the phone. Gemini gave me a fraudulent phone number and I got scammed! I cancelled my card and charged back the fraudulent charge immediately. This could have been way worse and I'm very fortunate to have learned my lesson with minimal repercussions. Be careful!

3h ago

---

**[Bernie Sanders wants to give every American $1000 a year from AI profits and the reasoning actually makes sense](https://www.reddit.com/r/artificial/comments/1u9ifn2/bernie_sanders_wants_to_give_every_american_1000/)**

Saw this on Gizmodo today and it's been stuck in my head The argument is simple. AI learned from everyone's writing, art, code, conversations and companies are now worth trillions because of that. so why is none of it coming back to the people whose work built it The bill would create a $7 trillion fund, give the public a 50% stake in the biggest AI labs, $1000 a year per person to start, goes up as AI makes more Every time i use chatgpt i think about all the writers and coders and artists whose work it learned from who got nothing. This is at least someone trying to address that Is this actually doable or just a good idea that goes nowhere

12h ago

---

**[Started maintaining a small library at work and now I genuinely understand why maintainers go quiet](https://www.reddit.com/r/artificial/comments/1u9fwfx/started_maintaining_a_small_library_at_work_and/)**

Built a little internal utility about a year ago, open sourced it because why not, figured maybe 10 people would find it useful. It slowly picked up a few hundred stars and then the issues started coming in. Not a flood or anything but enough and what surprised me was how much of it wasn't really bugs it was people wanting features that made sense for their use case but would've made zero sense for the original scope of the thing. Or issues that were basically "your README didn't account for my specific setup." I like helping people, I thought I would enjoy this and I did at first but somewhere around month 4 I noticed I was dreading opening GitHub notifications. The AI-generated PRs made it worse honestly. Not because the code was always bad but because they'd come in with confident descriptions, look reasonable on the surface and then you'd spend 30 minutes tracing through edge cases only to realize whoever sent it hadn't actually tested it against anything real. At human contribution pace that was manageable. At "someone hit generate and submit" pace it's just a different problem. I have immense respect for maintainers of anything with serious adoption now. The people keeping libraries that half the internet depends on running are doing it mostly for free, mostly in their spare time,and mostly while dealing with issue reporters who write like they're filing a complaint with customer support. If you use open source software and it's saved you hours of work, go sponsor someone. Even a few dollars a month means something and most of these folks have a GitHub sponsors page just sitting there.

13h ago

---

**[[OC] I mapped AI exposure and robotics risk for Japan's 70.5M workers and found two different automation waves](https://www.reddit.com/r/artificial/comments/1u9sntk/oc_i_mapped_ai_exposure_and_robotics_risk_for/)**

Most AI employment discussions only look at AI exposure. Japan turned out to be interesting because that approach misses half the picture. Using ILO occupation classifications and our task-based AI exposure model, I looked at Japan's 70.5 million workers. The AI side behaves almost exactly like every other country we've studied. Clerical support workers sit at the top with an 8.5/10 exposure score, professionals score 6.5/10, and elementary occupations remain low. But the robotics layer tells a different story. Plant and machine operators score just 3.0/10 on AI exposure, yet 7.5/10 on robotics risk. Skilled agricultural workers score 3.0 on AI but 6.5 on robotics. Service workers are relatively AI-resistant at 3.5, but robotics exposure rises to 4.5. What surprised me is that Japan's overall AI exposure average is actually the lowest among six OECD economies analysed, at 4.92/10. Occupational composition matters more than many people assume. The really interesting part is demographics. Japan has an ageing workforce, labour shortages and one of the highest robot densities in manufacturing. Automation there functions partly as labour replacement and partly as labour supplementation. Recovery resilience also scores highest among the six countries we examined at 8.0/10, suggesting worker transitions may be absorbed more easily than headline risk numbers imply. AI exposure scores are modelled estimates rather than official statistics. Robotics scores reflect current deployment potential and industry structure rather than forecasts of job losses. Curious to hear criticism on methodology and whether people think combining robotics and AI layers is more useful than analysing AI alone. Full analysis and interactive tool in comments.

4h ago

---

**[Most companies' AI problem is not the model](https://www.reddit.com/r/artificial/comments/1u9dfh5/most_companies_ai_problem_is_not_the_model/)**

Nadella dropped a post last weekend about "token capital" that every CTO I know forwarded within a day. His argument: every company needs to build AI capability it owns, not rent models via API. The learning loop around the model is where the IP lives. He's right about the direction. I think he skipped the part that kills most implementations. I've spent the last year and a half watching the same failure mode at mid-market software companies. Team gets budget for AI. Picks a model. Wires it into an agentic workflow or a RAG pipeline or hands developers Copilot seats. Three months later, usage is flat or declining and nobody can explain what value it added. The model produces output, humans eyeball it, the whole thing stays static. Runs on vibes. Fast vibes, but vibes. The formula that explains most of it: AI value is multiplication, not addition. Model Capability × Scaffolding × Human Judgment × Feedback Loops. If any of those is zero, your output is zero. A frontier model with no scaffolding gives you suggestions nobody implements. Good scaffolding with no feedback loops means the system never improves. Pull human judgment out and nobody catches when the model is confidently wrong about something domain-specific. The multiplier framing matters because companies keep treating these as additive, like you can just skip scaffolding and make up for it with a better model. You can't. Zero times anything is zero. I've been thinking about this as a seven-layer value stack. Bottom three: process design, governance, knowledge architecture. Middle three: human judgment, feedback loops, scaffolding. Model sits on top, thin by design. Most companies start at Layer 7 and work down. They buy the model, skip layers one through three, and end up with AI that doesn't compound and never becomes institutional knowledge. One example that made this concrete for me. Client had a support triage pipeline built on Claude Sonnet 4. Looked great in the demo. In production, it was routing 30% of tickets to the wrong team because the routing logic referenced a category taxonomy nobody had updated since 2022. The fix wasn't a better model. It was spending a week with the support lead rebuilding the taxonomy and writing explicit routing rules the model could reference. Five days. Misroutes dropped to under 8%. That's Layer 1 (process design) and Layer 3 (knowledge architecture) work. The model was fine the entire time. The layers underneath it were broken. Info-Tech's 2026 survey puts a number on how widespread this is. > 58% of organizations have integrated AI into enterprise strategies, up from 26% last year. Only 30% feel prepared to operationalize. > 78% of executives say AI is advancing faster than their teams can absorb. 82% of companies in early AI maturity haven't implemented a talent strategy for it. > That 28-point gap between "we have a strategy" and "we can execute" is made of the layers most teams skip because they're boring. Process maturity, data infrastructure... Governance. The word nobody wants to hear until something breaks. Apple made the other half of this argument at WWDC last week. They rebuilt Siri with an extensions framework that lets users swap between ChatGPT, Claude, and Gemini inside iOS 27. Xcode 27 brings coding agents from all three providers into the same workflow. Apple turned models into interchangeable plugins. If you can swap the model and your competitive position doesn't change, the model was never your advantage. The system you built around it was. The diagnostic I keep coming back to: before your team builds its next agentic workflow, can you draw the process map the agent will operate inside? If the answer is no, you have a Layer 1 problem, and no amount of model upgrades will fix it. I write a weekly briefing on AI and engineering velocity where I broke this down with the full stack visual and more data on all four signals from last week (Nadella, Apple, the Info-Tech survey, and the Fable 5 shutdown). But this post covers the core of it.

15h ago

---

**[Are we using AI correctly in the business world?](https://www.reddit.com/r/artificial/comments/1u9vab1/are_we_using_ai_correctly_in_the_business_world/)**

Lately I’ve seen lots of posts on various platforms that suggest AI will replace many lower paid jobs and we should all be future proofing our careers, by getting “AI proof” jobs. Is there not a case to be made that replacing the highest earners in a company, I.e. a CEO or someone around that level whose job is to make decisions based on the information they have. AI could be feed all the information that the company currently has, use all previous information to that is can find and track relevant current trends to find the patterns that a human might miss in the same situation. I’m happy to wrong about the application of AI and I don’t believe this will ever happen for a multitude of reasons. But it’s just a little hypothetical question my mind often ponders. Would love to hear some of your opinions.

1h ago

---

**[Anthropic CEO Dario Amodei goes completely candid on why he left OpenAI: "When you feel that you can't trust someone when you see disturbing patterns of behavior, dishonesty, that makes it very hard to continue."](https://www.reddit.com/r/artificial/comments/1u8zigf/anthropic_ceo_dario_amodei_goes_completely_candid/)**

In a recent candid interview Anthropic CEO Dario Amodei did not hold back regarding his departure from OpenAI. He cited a fundamental breakdown of trust and "disturbing patterns of behavior" and "dishonesty" as the primary reasons it became impossible to stay. Considering the massive wave of high-profile safety researcher departures from OpenAI over the last year or two, Amodei’s comments add a lot of retroactive context to the cultural shift that happened right around the time ChatGPT was being spun up. What do you think? Does this align with everything we've seen play out with Sam Altman and the board over the past couple of years?

1d ago

---

**[Only 16 percent of Americans think AI will have a positive impact on society, a new study shows | TechCrunch](https://www.reddit.com/r/artificial/comments/1u93rnf/only_16_percent_of_americans_think_ai_will_have_a/)**

Who will foot the AI bills? Despite the fact that AI increasingly dominates our economy (it’s a hot IPO summer and we’re all just along for the ride), most Americans are not particularly optimistic about the technology’s long-term impact on the country, a new study from Pew Research reveals. In fact, although a whole lot of Americans increasingly use AI in their daily lives, most of them have neutral to negative views about it, the research reveals.

🔗 [TechCrunch](https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/) • 21h ago

---

**[RNNs vs Transformers vs SSMs: where should AI memory live for continual learning?](https://www.reddit.com/r/artificial/comments/1u9ba5s/rnns_vs_transformers_vs_ssms_where_should_ai/)**

the interesting comparison btwn the three is not recurrence vs attention vs state space but it is, whether memory lives in a tiny recurrent state, a growing KV cache or in something closer to the model network itself. RNNs keep memory in a recurrent hidden state which is elegant in itself cause the state carries forward step by step but it also creates a bottleneck i.e the model can have roughly O(N^2) parameters while carrying only roughly O(N) state across time. IMO, RNNs were doomed not because recurrence was a bad idea but because they had a bad ratio of memory to compute. Transformers is completely at the other side, instead of compressing the past into one hidden state, they store past activations as key-value entries and attend over them. These are the little post-it notes, every token leaves behind a key for finding it and a value for what should be remembered. That is extremely powerful but it has an awkward property i.e. the model is mostly managing context while it runs, not naturally turning that experience into durable model knowledge so you get a split between fixed weights on one side and fast changing KVcache memory on the other. SSMs are interesting because they bring explicit state back into the center of the architecture discussion. They are not just faster attention but they are another answer to the question of where sequence state should live. The part which I is exciting for me is whether state should live in a compressed working dimension or closer to the model’s internal neuron/connectivity structure. BDH is one promising example of the latter direction, one way to read it is as SSM-like in the GPU implementation, but graph-based in the more general interpretation. Compared with a standard SSM or a linear transformer, the model state lives in a much larger neuron space N rather than only a smaller working dimension D, with N>>D. The GPU version does not materialize the full graph. It keeps the graph as the interpretation but runs it through a compressed low-rank form, because GPUs like dense matrix math much more than sparse graphs. The state is also sparse and positive which makes the graph interpretation more natural. Instead of thinking of memory only as a growing bag of KV notes, you can reinterpret the update as a small change to a connectivity matrix i.e if the system was in one state and then moved to another, that before to after transition strengthens part of the graph. This is like a middle ground and I would call it not too little and not too much. RNNs compress too much into a small state, transformers keep adding to the KV cache as the sequence grows and a synaptic memory design tries to put working memory closer to the same structure that stores longer term function. Another way to say it is: memory should maybe be constant size and information-shaped, not just a time buffer of the last n tokens. I am not claiming at all that this kills transformers or solves continual learning entirely but I just think where should memory live is an important framing than the usual frontier AI horse race. Are network centric architectures an important direction in frontier AI or still contricted by having to compress history into state?

16h ago

---

**[mlx-code | A Coding Agent That Speaks Git Natively](https://www.reddit.com/r/artificial/comments/1u9urrk/mlxcode_a_coding_agent_that_speaks_git_natively/)**

🔗 [mlx-code.com](https://www.mlx-code.com/) • 2h ago

---

---

## Google News: "ai"

**[Accenture Takes a Hit on Worsening Outlook and Cloudy AI Future](https://www.wsj.com/business/accenture-takes-a-hit-on-worsening-outlook-and-cloudy-ai-future-73eb8bfb)**

WSJ • 15h ago

---

**[‘We created a monster’: companies rein in AI usage as costs strain budgets](https://www.ft.com/content/1d37cc08-e0aa-45a4-a45d-4ad282529314?syn-25a6b1a6=1)**

Amazon, Walmart and Uber are among early adopters that have introduced caps or discouraged wasteful activity

Financial Times • 5h ago

---

**[Get with the times — here's what a 'Luddite' means today](https://www.npr.org/2026/06/19/nx-s1-5853589/luddite-meaning-history-ai)**

It's often a derogatory term used to describe digital dinosaurs and technophobes. That wasn't always the case. NPR's Word of the Week looks back at the not so backwards-looking Luddites.

NPR • 20m ago

---

**[I went to Runway's AI film festival. I was skeptical, but the crowd ate it up.](https://www.yahoo.com/entertainment/movies/articles/went-runways-ai-film-festival-080001320.html)**

I went to the Runway AI Festival, which showed 10 AI-generated shorts. I found the films a bit generic, but the tech was good, and the crowd roared.

Yahoo • 1h ago

---

**[US export ban on Anthropic’s AI models further strains alliances](https://www.aljazeera.com/news/2026/6/19/us-export-ban-on-anthropics-ai-models-further-strains-alliances)**

Trump administration's move to cut off allies' access to advanced AI prompts calls for greater self-reliance.

Al Jazeera • 11m ago

---

**[AI has granted America vast new power](https://www.economist.com/leaders/2026/06/18/ai-has-granted-america-vast-new-power)**

The Economist • 20h ago

---

**[White House talks with Anthropic shift to setting AI security rules](https://www.politico.com/news/2026/06/18/white-house-talks-with-anthropic-shift-to-setting-ai-security-rules-00967758)**

Politico • 13h ago

---

**[The White House said Anthropic’s powerful AI was ‘jailbroken.’ Here’s what that means.](https://www.washingtonpost.com/technology/2026/06/18/surprisingly-simple-ways-ai-can-be-tricked-into-breaking-its-own-rules/)**

It’s surprisingly simple to trick chatbots into breaking their own rules and spilling forbidden knowledge. Even poems and bedtime stories can work.

The Washington Post • 17h ago

---

**[Student Cheating Is Becoming Impossible to Detect in an A.I. Era](https://www.nytimes.com/2026/06/18/us/ai-apps-students-cheat.html)**

The New York Times • 1d ago

---

**[Godfather of AI blasts Musk's xAI as 'failure,' says labs are risking a 'big bubble explosion'](https://www.cnbc.com/2026/06/18/yann-lecun-elon-musk-xai-failure-ai-labs-bubble-risk.html)**

Yann LeCun's comments renew a long-running spat with Musk and cast doubt over valuations of some of the world's biggest AI companies.

CNBC • 22h ago

---

---

## HackerNews: "ai"

**[Sixty percent of US consumers say 'AI' in brand messaging is a turnoff](https://news.ycombinator.com/item?id=48569278)**

Original research from 2,000 decision-makers and consumers on AI brand visibility, content trust, and what brands need to do as the web feels less human. 74% say the internet feels less human than it did 10 years ago.

⬆️ 1068 • 💬 573 • 1d ago • [The Leading Enterprise Content Platform | WordPress VIP](https://wpvip.com/future-of-the-web-2026/)

---

**[AI demands more engineering discipline. Not less](https://news.ycombinator.com/item?id=48570948)**

⬆️ 412 • 💬 209 • 1d ago • [charitydotwtf.substack.com](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline)

---

**[Has AI already killed self-help nonfiction books?](https://news.ycombinator.com/item?id=48558489)**

⬆️ 410 • 💬 481 • 2d ago • [tim.blog](https://tim.blog/2026/06/12/has-ai-already-killed-nonfiction/)

---

**[Only 16 Percent of Americans Think AI Will Have a Positive Impact on Society](https://news.ycombinator.com/item?id=48573332)**

Although Wall Street loves AI, every day Americans are significantly less optimistic about the industry, a new report from Pew Research shows.

⬆️ 393 • 💬 491 • 1d ago • [TechCrunch](https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/)

---

**[The founder's playbook: Building an AI-native startup](https://news.ycombinator.com/item?id=48566832)**

We share how AI-native founders are using Claude at every stage of the startup journey, with practical exercises, frameworks, and prompts.

⬆️ 240 • 💬 167 • 2d ago • [Claude](https://claude.com/blog/the-founders-playbook)

---

**[Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)**

CADAM is the open source text-to-CAD web application - Adam-CAD/CADAM

⬆️ 208 • 💬 97 • 1d ago • [GitHub](https://github.com/Adam-CAD/CADAM)

---

**[The Competitive Moat That AI Can't Replicate](https://news.ycombinator.com/item?id=48573435)**

Portfolio and personal blog of Chris Hillman.

⬆️ 139 • 💬 122 • 1d ago • [ghostinthedata.info](https://ghostinthedata.info/posts/2026/2026-06-13-human-connection-moat/)

---

**[The AI Hate Progression](https://news.ycombinator.com/item?id=48589485)**

I think I've spoken at length in other places about how I am a very staunch AI hater and everything I hate about how the tech is presented t...

⬆️ 108 • 💬 163 • 14h ago • [xodium.net](https://www.xodium.net/2026/06/the-ai-hate-progression.html)

---

**[After AI takes everything](https://news.ycombinator.com/item?id=48556644)**

⬆️ 101 • 💬 113 • 2d ago • [ursb.me](https://ursb.me/en/posts/after-ai-takes-everything/)

---

**[The AirPods Effect](https://news.ycombinator.com/item?id=48592832)**

How earbuds influence our beliefs and push us apart.

⬆️ 90 • 💬 153 • 10h ago • [theescapenewsletter.com](https://www.theescapenewsletter.com/p/the-airpods-effect)

---

---

## YouTube Videos: "ai"

**[Godfather Of AI WARNS: They&#39;re Building AI So Dangerous That They Can&#39;t Even Control It](https://www.youtube.com/watch?v=y_C00dr6i9U)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Geoffrey Hinton explains why he is ...

📺 Neural Nutshell

👁️ 7K • 👍 231 • 💬 105 • ⏱️ 11:35 • 17h ago

---

**[The US Government Just Pulled The World&#39;s Most Powerful AI Offline](https://www.youtube.com/watch?v=7vz6T6TNIzo)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *The most powerful AI ever released to the ...

📺 Julia McCoy

👁️ 23K • 👍 1K • 💬 141 • ⏱️ 10:09 • 1d ago

---

**[The AI Email Threat...](https://www.youtube.com/watch?v=KdWsrjpw_QI)**

Take your personal data back with Incogni! Use code ECHELON at the link below and get 60% off an annual plan: ...

📺 Upper Echelon

👁️ 26K • 👍 2K • 💬 163 • ⏱️ 13:13 • 10h ago

---

**[I Was Right About AI](https://www.youtube.com/watch?v=aXy8mQeuObk)**

In this episode, I follow up on a few of my predictions about AI from my recent video: "How AI Will Fail Like The Music Industry" My ...

📺 Rick Beato

👁️ 384K • 👍 26K • 💬 5K • ⏱️ 7:47 • 12h ago

---

**[Jeff Bezos Makes Shocking AI Prediction and the Future of Jobs](https://www.youtube.com/watch?v=qI1tLQF-_9A)**

Speaking at the VivaTech conference in Paris on June 17, the Jeff Bezos pushed back on fears that artificial intelligence will ...

📺 New York Post

👁️ 11K • 👍 196 • 💬 61 • ⏱️ 5:28 • 1d ago

---

**[We Might Actually Need to Stop AI](https://www.youtube.com/watch?v=CvA8-aScqio)**

My FREE AI OS Course: ...

📺 Nate Herk | AI Automation

👁️ 36K • 👍 1K • 💬 275 • ⏱️ 12:28 • 2d ago

---

**[The AI Skills Nobody is Teaching (And Everyone Needs) | AI Expert Ethan Mollick](https://www.youtube.com/watch?v=9YMYVb1ASCg)**

Be honest: AI makes you a little nervous. Maybe you're afraid it'll take your job. Maybe you're overwhelmed by all the advice about ...

📺 Simon Sinek

👁️ 66K • 👍 2K • 💬 140 • ⏱️ 58:36 • 2d ago

---

**[Fable 5 Replacement Just Dropped: Fusion (Fable Level AI)](https://www.youtube.com/watch?v=wzay-VWjoRM)**

Fable 5 is gone, and now the big question is simple: what comes next? OpenRouter just introduced Fusion, a system that sends ...

📺 AI Revolution

👁️ 18K • 👍 693 • 💬 48 • ⏱️ 15:28 • 2d ago

---

**[Real Reason for the A.I Data Center Boom](https://www.youtube.com/watch?v=5KnkJcfDeHI)**

For my special bundle offer plus free shipping head to https://getkrill.com/Adapt ✨ Try it risk-free with a 365-day money-back ...

📺 Adapt 2030

👁️ 8K • 👍 867 • 💬 141 • ⏱️ 32:35 • 18h ago

---

**[Don&#39;t build more AI agents until you watch this](https://www.youtube.com/watch?v=BOXK2XFLA-E)**

Full post with Agent Maintenance Guide: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 51K • 👍 1K • 💬 158 • ⏱️ 18:25 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 211,424 • ❤️ 1,749 • 5h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 4,307 • ❤️ 1,412 • 5m ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 56,162 • ❤️ 1,111 • 3d ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 229,156 • ❤️ 891 • 4d ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 527,080 • ❤️ 1,007 • 8d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 6,589 • ❤️ 419 • 6h ago

---

**[Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)**

*Prefeitura do Rio de Janeiro (City of Rio de Janeiro)*

Rio 3.5 Open 397B is a frontier-class, open-source image-text-to-text AI model post-trained from Qwen 3.5 397B. It excels in agentic coding, STEM, multilingual tasks, and multimodal reasoning, featuring a 1M context window and SwiReasoning for enhanced accuracy and efficiency.

`image-text-to-text` `403.4B`

⬇️ 190,501 • ❤️ 324 • 4d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 183,093 • ❤️ 2,179 • 6d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,420,052 • ❤️ 1,982 • 2mo ago

---

**[FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)**

*Microsoft*

FastContext-1.0-4B-SFT is a lightweight repository-exploration subagent for LLM coding agents, designed to efficiently locate relevant code snippets using parallel read-only tool calls (READ, GLOB, GREP). Its primary use case is to reduce token consumption and context pollution for main coding agents by providing focused file paths and line ranges as evidence, thereby improving end-to-end performance in tasks like software development.

`text-generation` `4.0B`

⬇️ 957 • ❤️ 212 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 32 • 💬 1 • ⭐ 23,138 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 238 • 💬 4 • ⭐ 8,276 • 28d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 100 • 💬 4 • ⭐ 87,268 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 166 • 💬 6 • ⭐ 4,304 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 19 • 💬 1 • ⭐ 83,011 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 42 • 💬 4 • ⭐ 30,684 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[FastContext: Training Efficient Repository Explorer for Coding Agents](https://huggingface.co/papers/2606.14066)**

*Shaoqiu Zhang, Maoquan Wang, Yuling Shi et al. (8 authors)*

🏢 Microsoft

FastContext separates repository exploration from code solving in LLM agents using specialized exploration models that reduce token consumption and improve resolution rates.

▲ 83 • 💬 3 • ⭐ 595 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14066) • [💻 code](https://github.com/microsoft/fastcontext) • [🔗 project](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 80 • 💬 7 • ⭐ 77,698 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[JoyAI-VL-Interaction: Real-Time Vision-Language Interaction Intelligence](https://huggingface.co/papers/2606.14777)**

*Dingyu Yao, Junhao Zhou, Chenxu Yang et al. (15 authors)*

🏢 JD.com Open Source

A vision-language model operates continuously in real-time, making autonomous decisions about when to respond or delegate, enabling interactive systems that perceive and act upon environmental changes without user prompting.

▲ 189 • 💬 2 • ⭐ 298 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14777) • [💻 code](https://github.com/jd-opensource/JoyAI-VL-Interaction) • [🔗 project](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

---

**[VibeThinker-3B: Exploring the Frontier of Verifiable Reasoning in Small Language Models](https://huggingface.co/papers/2606.16140)**

*Sen Xu, Shixi Liu, Wei Wang et al. (9 authors)*

🏢 WeiboAI

VibeThinker-3B demonstrates that compact models can achieve state-of-the-art performance on verifiable reasoning tasks through specialized training techniques, challenging conventional scaling assumptions.

▲ 97 • 💬 1 • ⭐ 1,042 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.16140) • [💻 code](https://github.com/WeiboAI/VibeThinker) • [🔗 project](https://github.com/WeiboAI/VibeThinker)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 73.9k • 🔱 9.5k • 16m ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 38.2k • 🔱 1.8k • 29m ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 9.8k • 🔱 904 • 4h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 4.5k • 🔱 398 • 40m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 3.9k • 🔱 431 • 3m ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.6k • 🔱 362 • 21h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.3k • 🔱 402 • 1d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.1k • 🔱 194 • 1d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.6k • 🔱 144 • 3d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.6k • 🔱 120 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*
