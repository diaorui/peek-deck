---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-21T15:33:23.201905+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 21, 2026 at 15:33 UTC  
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

**[What Happens When the World is Run on Code No One Understands?](https://www.reddit.com/r/artificial/comments/1vu3x0t/what_happens_when_the_world_is_run_on_code_no_one/)**

Mathematical verification must be a national mission in the AI era, write Patrick Shafto, Ken Ono, and Scott Duke Kominers.

🔗 [TIME](https://time.com/article/2026/08/20/what-happens-when-the-world-is-run-on-code-no-one-understands-/) • 12h ago

---

**[This old sci-fi story video is highly similar to what we have with nearing the singularity and AGI today with all work routed to one central machine](https://www.reddit.com/r/artificial/comments/1vu9ma4/this_old_scifi_story_video_is_highly_similar_to/)**

Feels like even after so many years, it's the same story but with better hardware and tech

7h ago

---

**[Anyone else have these "Oh my god" moments with AI every couple weeks?](https://www.reddit.com/r/artificial/comments/1vu59jb/anyone_else_have_these_oh_my_god_moments_with_ai/)**

I've been pretty heavily invested in the AI news space for a while, but due to budget constraints, I never really got to test these models. I bit the bullet once DeepSeek v4 0731 came out and put in twenty dollars. I'd had experience with frontier models through chat window subscriptions, but having an agent was a whole different experience. I built so many useful tools within a matter of hours for cents, and it really blew me away. What amazes me more is how general these models are. Not only can I ask it to write code, but also to research, do security audits, etc. I'm not treating these models as gospel (yet); I always check their work. I've also learned so much using these agents. I've pasted my notes about books I've read and asked it to quiz me to make sure I actually understand the ideas being presented. I finally learned C after procrastinating for months, using agents to get personalized feedback and a roadmap. I'm also being extremly carful to not off load my critical thinking. Ever since I started using AI, I've made a pledge that, every day, I'll write a 250+ word essay about a topic, without any AI use (and usually search engines). I've also started to read more often. I hope these habits help counteract any cognitive decline that AI use causes. I feel like I've unlocked the creativity and curiosity that was within me all along. Every couple of weeks I get amazed just by how versatile these models are. For example, I was doing my daily NYC games, and I was really stumped on Connections (ifykyk). I didn't manage to solve it, but after sending a screenshot to Luna, it got first try (without using the internet). It just amazes me how you can describe almost any problem and get a reasonable-sounding answer/output.

11h ago

---

**[Most AI agents are sending your data somewhere you can't fully see into. Does that bother anyone else?](https://www.reddit.com/r/artificial/comments/1vuai26/most_ai_agents_are_sending_your_data_somewhere/)**

Maybe I'm overthinking this but it's been sitting with me for a few weeks now. The way most AI tools work is pretty seamless on the surface. You send something in, something happens, you get an answer back. Nobody really thinks about the middle part. I didn't for a long time. Then someone in a conversation asked me a simple question. Where exactly is the model running when you send it a document. And I realized I didn't have a clean answer. I knew the company. I'd signed up, accepted terms, the usual. But the actual infrastructure question, which servers, whose data center, who has access at the compute level during that moment, I genuinely had no idea. Started reading more carefully after that. Cloudflare has been doing interesting things with their AI Gateway around keeping data within defined boundaries. Worth looking at if you haven't. But even that is still routing through infrastructure you don't own or control. The thing that kept coming up when I read about how regulated industries handle this was running the whole stack inside your own environment. Inference happens on your own infrastructure, nothing leaves, no external calls at all during processing. Was reading about it through Lyzr actually, they have a term called Sovereign AI built around exactly this. What stuck with me was how they described it, that for banks, healthcare, government, this isn't really an architectural choice they're making, it's the only option that makes it through legal review in the first place. What's interesting is how much more accessible this has become. Felt like something only the biggest institutions with dedicated infrastructure teams could pull off even two years ago. For most personal use cases honestly none of this matters. But if you're building something that touches anything sensitive and your risk management strategy is basically trusting the vendor agreement, I wonder if that assumption is actually as solid as it feels. Curious if anyone has gone through a proper evaluation of fully private inference. What did you actually find when you looked closely at the tradeoffs??

6h ago

---

**[A fixed evaluator can still become the target of an agent loop](https://www.reddit.com/r/artificial/comments/1vud8d2/a_fixed_evaluator_can_still_become_the_target_of/)**

Fixing an evaluator before an agent starts iterating prevents the goalposts from moving. It does not stop the agent process from adapting to feedback it can repeatedly see. The AQuA preprint makes that distinction explicit. Its base language model and evaluator stay fixed. Validated observations are retained in a part-specific research state, and later proposals are conditioned on that evidence. Validation feedback is visible during this loop. A separate final test is withheld until the configuration is frozen; its result is not returned to the agent or used to rank candidates. That creates a useful final check, but the isolation is procedural rather than cryptographic, and repeated adaptation to visible validation remains possible. The AQuA design question I would inspect next is how much evaluator-specific feedback should enter durable state. Which defense matters most here: limiting that feedback, rotating the visible evaluation, or relying on one untouched final test after freeze?

4h ago

---

**[AI compute financing just tripled in ten weeks - the mechanism behind the reported $100B Broadcom deal](https://www.reddit.com/r/artificial/comments/1vug3gk/ai_compute_financing_just_tripled_in_ten_weeks/)**

Broadcom apparently went back to Blackstone and Apollo (the same two private-credit shops it partnered with in June for a $35B package) and is now discussing something like $100B, to fund AI chip infrastructure for Anthropic. Ten weeks, 3x the size. The structure is the interesting part if you're not familiar with how this financing actually works: reportedly split into a senior-secured tranche ($60-70B) and a junior tranche (~$30B). Senior-secured gets paid first if anything goes wrong and is backed by hard collateral (the chips/datacenters themselves), junior eats losses first but gets a higher yield. It's basically the same risk-layering banks use on mortgage bonds, except the underlying asset here is depreciating GPU hardware instead of houses, and the "borrower" is a compute buildout racing to keep up with model demand. Private credit shops love this because it's floating-rate, asset-backed, and banks mostly won't touch loans this size and this fast for something as volatile as AI infra. Genuinely curious what people think: is layered private-credit financing at this pace and scale just normal infrastructure buildout, or is it the first real sign of an AI capex bubble forming underneath the model layer everyone's watching instead?

2h ago

---

**[Writer’s dilemma: Critiquing a family member’s AI-generated novel](https://www.reddit.com/r/artificial/comments/1vu2d4p/writers_dilemma_critiquing_a_family_members/)**

To make a long story short: My stepfather-in-law was laid off in January. My husband and I both begrudgingly tolerate the man. His ego and quirks make him difficult to be around, but fortunately, we only have to see him once or twice a year (they live five hours away) on our obligatory visits to visit my mother-in-law. Here’s the kicker. On month eight of unemployment, he decided to start what I can only comfortably describe as a poor attempt at AI-enabled grifting. He started by generating Toby Keith-esque country songs and posting full-length “albums” on Facebook. My husband and I rolled our eyes, thinking it was just a “local boomer discovers AI” sort of situation. He’s since piloted a LinkedIn-style leadership motivation series of AI-generated texts and images, the pairs of which almost never make sense. Again, we mostly ignored it. But then, the books started. Which meant I was dragged into it. For a little extra color — I’m a career journalist turned specialized corporate content writer/strategist by day. By night (mostly early mornings, actually), I write novels. I’ve spent the last six years working daily on a series that means the world to me, and I’m currently in the trenches of my seventh round of edits on the first book, with the full intention of querying my best work (I got so close in the last round, but my word count sank that ship - lesson learned!). I take this hobby as seriously as I take my daytime career. I am no master of this craft. It’s a day-in and day-out process to become 1% better at storytelling every time I sit down to write or edit. So when my father-in-law unceremoniously sent me his AI-generated manuscript wanting to “get my thoughts,” I was torn. Of course, in nearly any other situation, I’d be more than happy to review a friend or family member’s writing. I do it all the time! But this felt different. He’s fully intent on self-publishing this novel. Do I think it’ll sell? No. I don’t! I can’t say I feel “threatened” by another writer, or that I’m worried this book is going to be a runaway Amazon success. I read it. It’s… fine. The prose isn’t egregious because the AI was decently well-prompted. The characters have no arc. The plot barely moves. It’s 90% atmosphere, 5% police procedural tropes, and 5% repeated descriptions that are immediate AI red flags to a semi-trained eye. My mother-in-law has urged me to “please be nice” about the whole thing. She knows that even though I work for a company that plays in the AI space (we’re healthcare-adjacent), I have strong convictions about the use of gen-AI for creative work, especially when someone is trying to pass off the work as their own. We’re visiting in a few weeks, and they “can’t wait to talk to me” about this. Writer to… writer. I guess. My question for you all: What do I owe him in this inevitable conversation? Has anyone else encountered a situation where they’ve been asked to review/critique someone’s AI-generated work? I feel icky even having read it, but I really struggle pushing back on this guy. He’s exhausting to be around as-is, and I’d prefer to keep things as light as possible, just to get through the trip.

14h ago

---

**[I wish AI slide demos started with the kind of mess I actually have](https://www.reddit.com/r/artificial/comments/1vu4c6d/i_wish_ai_slide_demos_started_with_the_kind_of/)**

Most AI slide demos feel kind of unrealistic to me. They usually start with a clean prompt and a clear topic, but that’s rarely what I’m working with. Most of the time I have a PDF, a few links, scattered notes, some numbers, and only a rough idea of what the deck should say. And honestly, that’s where I want to know if an AI slide tool is actually useful. Can it figure out what matters and turn that mess into something coherent, or do I still need to clean everything up first? At that point I might as well just make the deck myself. Has anyone found a slide tool that’s actually good with messy source material?

12h ago

---

**[Ukraine found an uncontrolled Nvidia AI chip inside a Russian cruise missile](https://www.reddit.com/r/artificial/comments/1vtjfva/ukraine_found_an_uncontrolled_nvidia_ai_chip/)**

Ukraine's intel agency (HUR) pulled a Nvidia Jetson Orin NX module out of a downed Russian S-71M cruise missile, disclosed a few days ago. Nvidia's response is kind of wild: this specific chip was never on any export control list to begin with, unlike their datacenter GPUs, and they've said outright they can't track where resold units end up. The EU's newest sanctions round (adopted late July) added dozens of new entities, but nothing that actually targets this class of consumer-grade edge AI hardware. Ukraine says they've now catalogued close to 6,000 foreign components across 200+ Russian weapons systems, so this isn't a one-off. Feels like export control regimes were built around "obviously military" or "obviously datacenter" hardware, and completely miss the middle category: cheap, widely available edge AI modules that are genuinely useful for robotics/drones/normal stuff but also trivially good enough to guide a missile. Anyone know if there's an actual policy fix being discussed for that gap, or is it just going to stay a whack-a-mole enforcement problem?

1d ago

---

**[Good results teaching an open weight model how to reason about a new domain](https://www.reddit.com/r/artificial/comments/1vuhgie/good_results_teaching_an_open_weight_model_how_to/)**

Spent some time looking into how to teach a model a new domain. Sharing a write-up for those who are interested in this topic: https://www.teachmecoolstuff.com/viewarticle/teaching-a-local-llm-a-new-domain

1h ago

---

---

## Google News: "ai"

**[As demand for Meta AI glasses explodes, it’s harder to avoid creepy recordings](https://arstechnica.com/tech-policy/2026/08/meta-ai-glasses-may-get-creepier-and-apps-that-detect-them-arent-perfect/)**

Ars looks at Zuckoff, the latest free app detecting Meta AI glasses amid privacy backlash.

Ars Technica • 4h ago

---

**[How Big Tech’s A.I. Borrowing Binge Is Driving Up Bond Yields](https://www.nytimes.com/2026/08/20/business/bond-yields-tech-ai-debt.html)**

The New York Times • 18h ago

---

**[AI spending could EXPLODE to $14T by 2030, tech expert predicts](https://www.foxnews.com/video/6403814078112)**

The Futurum Group CEO Daniel Newman joins Stuart Varney to discuss massive AI CapEx forecasts, predicting cumulative data center spending could reach $14T by 2030 due to skyrocketing demand.

Fox News • 1h ago

---

**[AI data center outrage is showing up everywhere from ads to elections](https://www.cnbc.com/2026/08/20/ai-data-center-election-backlash.html)**

With less than three months until the midterm elections, opposition to AI data centers is becoming a bipartisan rallying cry in a growing number of states.

CNBC • 1d ago

---

**[Trump says any governor or mayor should want to welcome an AI data center](https://www.foxbusiness.com/politics/trump-says-any-governor-mayor-should-want-welcome-ai-data-center)**

Trump continued to be bullish on artificial intelligence during a Wednesday speech, during which he urged governors and mayors to accept data centers in their communities.

Fox Business • 3h ago

---

**[Google, OpenAI among companies to comply with Texas AI data center rules](https://www.usatoday.com/story/news/state/texas/2026/08/21/which-tech-ai-companies-are-complying-with-texas-data-center-rules/91373947007/)**

Gov. Greg Abbott says Google, Meta, OpenAI, Amazon, Anthropic and dozens more will follow grid, water and cost rules for data centers in the state.

USA Today • 1h ago

---

**[AI Note-Takers Turn Routine Meetings Into Potential Legal Evidence](https://www.forbes.com/sites/timbajarin/2026/08/21/ai-note-takers-turn-routine-meetings-into-potential-legal-evidence/)**

AI note-takers boost productivity, but transcripts can create privacy, consent and legal-discovery risks businesses must manage.

Forbes • 1h ago

---

**[Why Is Everyone in Silicon Valley Talking Like That?](https://www.theatlantic.com/technology/2026/08/ai-jargon-in-everday-speech/688358/)**

Did you mix something up? Maybe you’re just “hallucinating.”

The Atlantic • 17h ago

---

**[Exclusive: FTC urged to investigate AI firms for destroying books](https://www.axios.com/2026/08/21/ftc-ai-companies-book-destruction-investigate)**

Axios • 2h ago

---

**[Micron CEO: AI has 'totally changed' the equation for the boom-and-bust memory industry](https://www.cnbc.com/2026/08/20/micron-ceo-ai-changed-memory-industry.html)**

Micron CEO Sanjay Mehrotra said on Thursday that AI has dramatically changed the memory business.

CNBC • 16h ago

---

---

## HackerNews: "ai"

**[Don't paste the AI, please](https://news.ycombinator.com/item?id=49371857)**

If someone asks you a question, paste your answer — not the chatbot's.

⬆️ 1022 • 💬 569 • 1d ago • [dontpastetheai.com](https://dontpastetheai.com/)

---

**[AI companies destroy physical books – let's scan rare books before it's too late](https://news.ycombinator.com/item?id=49383026)**

AI companies are secretly buying, scanning, and destroying millions of physical books to train their models, permanently locking human knowledge inside private corporate servers. Anna’s Archive is urgently calling on volunteers worldwide to scan and upload books to their shadow library before this cultural heritage disappears forever.

⬆️ 377 • 💬 293 • 12h ago • [annas-archive.gl](https://annas-archive.gl/blog/physical-destruction.html)

---

**[AI companies destroy physical books – let's scan rare books before it's too late](https://news.ycombinator.com/item?id=49385994)**

⬆️ 351 • 💬 266 • 5h ago • [annas-archive.pk](https://annas-archive.pk/blog/physical-destruction.html)

---

**[Show HN: Huzzah – a novel approach to coding with AI](https://news.ycombinator.com/item?id=49378768)**

My personal portfolio site and blog.

⬆️ 346 • 💬 198 • 20h ago • [danielvaughn.dev](https://www.danielvaughn.dev/posts/huzzah/)

---

**[Field measurements of neighborhood-scale air temperature impacts of data centers](https://news.ycombinator.com/item?id=49349147)**

⬆️ 313 • 💬 500 • 2d ago • [asmedigitalcollection.asme.org](https://asmedigitalcollection.asme.org/sustainablebuildings/article/7/2/024501/1233035/Data-Center-Waste-Heat-as-an-Emerging-Urban)

---

**[Air Theremin – A browser theremin you play by waving at your webcam](https://news.ycombinator.com/item?id=49359425)**

Tilt your phone, or wave both hands at the camera: spread them for volume, raise them for pitch. Note snap, cave reverb, oscilloscope and audio recording. Built with the Web Audio API.

⬆️ 299 • 💬 100 • 2d ago • [theremin.bizibah.com](https://theremin.bizibah.com/)

---

**[Mathematics in the age of AI](https://news.ycombinator.com/item?id=49362728)**

An essay, based on a public lecture delivered at the 2026 International Congress of Mathematicians, on how the mathematical community might respond to the arrival of artificial intelligence tools that are capable of performing research-level mathematical tasks. Rather than debating the capabilities of such tools, we condition on the hypothesis that these capabilities will arrive, and examine instead a question that is orthogonal to it: what the goals and values of mathematical research actually are. The problem-solving component of mathematics is used as a case study.

⬆️ 207 • 💬 254 • 2d ago • [arXiv.org](https://arxiv.org/abs/2608.16753)

---

**[AI usage patterns in software teams](https://news.ycombinator.com/item?id=49353432)**

AI usage patterns in software teams: who is adopting AI, how it reshapes where teams spend their time, and how much more they ship.

⬆️ 197 • 💬 115 • 2d ago • [linear.app](https://linear.app/data)

---

**[Anti-AI fonts are useless and harmful](https://news.ycombinator.com/item?id=49375719)**

Trying to obfuscate the web is a bad, pointless idea

⬆️ 188 • 💬 150 • 1d ago • [Andrew's WebLog](https://blog.yaros.ae/anti-ai-fonts-are-useless-and-harmful/)

---

**[Copyright does not protect AI-generated content in EU](https://news.ycombinator.com/item?id=49382041)**

Does copyright protect your AI-generated content in EU? Apparently not.  Content that is entirely generated by artificial intelligence is not protected by copyright. EU copyright law has strictly human-centric foundation. 

Daniel J. Gervais: 'When you put your name on an article that's written by ChatGPT or Claude, you're basically putting a provenance mark on it saying: I take responsibility for this. I haven't written it, but I'm putting my name on it. That doesn't give you copyright, but it does give you liability for the content'  https://euobserver.com/232898/interview-does-copyright-protect-your-ai-generated-content-in-europe-lets-find-out/

Gervais, Daniel J. and Shemtov, Noam and Marmanis, Haralambos and Zaller Rowland, Catherine, The Heart of the Matter: Copyright, AI Training, and LLMs (September 21, 2024). Available at SSRN: https://ssrn.com/abstract=4963711 or http://dx.doi.org/10.2139/ssrn.4963711

"Munich Local Court has held that AI generated logos do not enjoy copyright protection. Neither mere prompting nor the selection between several AI suggestions is sufficient as a human creative contribution. For businesses, this is ambivalent. On the one hand, content generated purely by AI can hardly be protected on an exclusive basis, which has implications for brand building and content strategies" https://www.germanlawinternational.com/intellectualproperty/copyright/from-the-printing-press-to-ai-how-the-eu-plans-to-modernize-copyright-law-164154/

#law #copyright #LLM #AI #iplaw #intellectualProperty #EU

⬆️ 181 • 💬 196 • 15h ago • [Mathstodon](https://mathstodon.xyz/@maxpool/117128107757895678)

---

---

## YouTube Videos: "ai"

**[OpenAI’s New AI Just Crossed the Red Line (Critical Warning)](https://www.youtube.com/watch?v=7TGamjQahWk)**

OpenAI says its upcoming Astra model may have crossed a critical cybersecurity threshold, forcing the company to slow frontier ...

📺 AI Revolution

👁️ 31K • 👍 814 • 💬 144 • ⏱️ 17:06 • 1d ago

---

**[WH nightmare: AI bubble COLLAPSES! A TECH INSIDER shows the TERRIFYING WAY it may all CRATER](https://www.youtube.com/watch?v=n32mhb2aUsE)**

MAGA allies are making huge bets on AI amid new signs that a tech “bubble” could rattle the economy. MS NOW's Ari Melber ...

📺 MS NOW

👁️ 390K • 👍 7K • 💬 308 • ⏱️ 12:08 • 15h ago

---

**[AI deepfakes of celebrities used in investment scams | ABC NEWS](https://www.youtube.com/watch?v=j4oYUhukSKA)**

Scammers are using impersonations of celebrities, politicians and trusted public figures to promote fake investment schemes, with ...

📺 ABC News (Australia)

👁️ 5K • 👍 46 • ⏱️ 2:34 • 11h ago

---

**[AI Superintelligence Is Not a Tool, It&#39;s an Adversary Threatening Humanity: ControlAI&#39;s Connor Leahy](https://www.youtube.com/watch?v=v99DkPP6LVY)**

Support our work: https://democracynow.org/donate/sm-desc-yt Sixty-nine-year-old Wynd Kaufmyn, a retired teacher from ...

📺 Democracy Now!

👁️ 72K • 👍 3K • 💬 435 • ⏱️ 13:35 • 1d ago

---

**[Facebook AI Slop Is Ruining Lives](https://www.youtube.com/watch?v=ggYEvbwLgFA)**

The worst side of the internet imaginable... Please subscribe if you havent! Almost to 400k! Reposting clips using #maxxnormann.

📺 Max

👁️ 149K • 👍 12K • 💬 183 • ⏱️ 23:46 • 18h ago

---

**[DeepSeek Just Made Closed AI Look Ridiculous](https://www.youtube.com/watch?v=kyYepbhe1g8)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers DeepSeek V4 Pro 0813: ...

📺 Two Minute Papers

👁️ 131K • 👍 5K • 💬 317 • ⏱️ 5:29 • 1d ago

---

**[What&#39;s Beyond ChatGPT? The &#39;Godmother of AI&#39; Has a Plan | The Circuit](https://www.youtube.com/watch?v=ITxsc3mgqts)**

Emily Chang meets artificial intelligence pioneer Fei-Fei Li to discuss her innovations in the field, her $1 billion startup World Labs ...

📺 Bloomberg Originals

👁️ 178K • 👍 5K • 💬 144 • ⏱️ 24:04 • 2d ago

---

**[AI has infiltrated Schools.](https://www.youtube.com/watch?v=eSjXe1gYoLw)**

📺 Ben Esherick

👁️ 256K • 👍 20K • 💬 125 • ⏱️ 0:37 • 17h ago

---

**[AI Just Passed A Consciousness Test](https://www.youtube.com/watch?v=KFXTGIh6mis)**

ai #joerogan Joe Rogan Experience #2541 - Thomas Campbell - explains how he taught AI's how to remote view and how they ...

📺 YourWeeklyCrew

👁️ 16K • 👍 295 • 💬 11 • ⏱️ 0:47 • 22h ago

---

**[The cost of A.I. you&#39;re paying right now](https://www.youtube.com/watch?v=wHiBW1DJDi4)**

learnsomethingnew #scam #tech #capitalism.

📺 Alex Falcone

👁️ 116K • 👍 9K • 💬 225 • ⏱️ 1:14 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 1,726,651 • ❤️ 11,875 • 7d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 5,804,917 • ❤️ 2,453 • 1d ago

---

**[Qwen3.8-27B-Uncensored-MLX](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-MLX)**

*OrcaRouter*

An uncensored, MLX-quantized 27B parameter vision-language model optimized for Apple Silicon, supporting 2-8 bit precisions. It performs image-text-to-text tasks and is intended for AI safety research and red-teaming due to its removed safety alignment.

`image-text-to-text` `4.7B`

⬇️ 18,193 • ❤️ 784 • 6h ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 107,520 • ❤️ 714 • 1d ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 15,678 • ❤️ 1,148 • 7d ago

---

**[Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)**

*Qwen*

Qwen3.8-27B-FP8 is a 27B parameter vision-language model optimized with FP8 quantization for efficient inference. It excels at complex, multi-step tasks involving image and video understanding, autonomous planning, and coding, supporting up to 1M context length.

`image-text-to-text` `27.8B`

⬇️ 1,939,895 • ❤️ 647 • 7d ago

---

**[Qwen3.8-27B-Uncensored-GGUF](https://huggingface.co/JonathanColetti/Qwen3.8-27B-Uncensored-GGUF)**

*Jonathan Coletti*

This is an uncensored GGUF quantization of Qwen3.8-27B, optimized for reduced refusal behavior and retaining the multi-token prediction (MTP) head for enhanced generation efficiency. It supports text generation with multilingual capabilities (English, Chinese) and is compatible with llama.cpp, offering various quantization levels for different performance/resource trade-offs.

`text-generation` `27.3B`

⬇️ 1,126,222 • ❤️ 545 • 5d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 654,175 • ❤️ 1,459 • 4d ago

---

**[Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF](https://huggingface.co/HauhauCS/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF)**

*HauhauCS*

This is an uncensored, aggressive Qwen3.8-27B multimodal model with HauhauCS FastMTP for accelerated text generation and a vision projector for image/video input. It excels at direct, fast responses and handles complex prompts without refusal, supporting up to 1M token context.

`image-text-to-text` `1.9B`

⬇️ 357,225 • ❤️ 401 • 3d ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 123,956 • ❤️ 396 • 14h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[4DAnyone: Create Anyone in 4D from a Casual Monocular Video](https://huggingface.co/papers/2608.20335)**

*Yudong Jin, Tao Xie, Qihang Zhang et al. (9 authors)*

🏢 Ant Research

4DAnyone reconstructs 4D humans from monocular video by generating multiview-consistent videos and lifting them into 4D Gaussian Splatting, using reference and target context designs to overcome scaling bottlenecks.

▲ 45 • 💬 6 • ⭐ 162 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2608.20335) • [💻 code](https://github.com/ant-research/4DAnyone) • [🔗 project](https://4danyone.github.io/)

---

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 18 • 💬 1 • ⭐ 2,553 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2607.05391) • [💻 code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [🔗 project](https://llm-as-a-verifier.com/)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 692 • 💬 5 • ⭐ 3,801 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 129 • 💬 3 • ⭐ 23,683 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming](https://huggingface.co/papers/2606.31227)**

*Yong Yang, Xing Zheng, Huiyu Wu et al. (10 authors)*

🏢 Tencent

AI-Infra-Guard is an open-source framework that addresses AI infrastructure security through layered detection paradigms spanning infrastructure, protocol, agent behavior, and model layers.

▲ 14 • 💬 2 • ⭐ 5,105 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.31227) • [💻 code](https://github.com/Tencent/AI-Infra-Guard) • [🔗 project](https://matrix.tencent.com/clawscan/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 123 • 💬 4 • ⭐ 99,121 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[HarnessEval-W: Agentifying the Evaluation of Visual Worlds](https://huggingface.co/papers/2608.16859)**

*Weiliang Chen, Haowen Sun, Jun Gao et al. (43 authors)*

🏢 MirroS

HarnessEval-W uses hierarchical sub-agents to decompose world-model evaluations into verifiable reasoning chains that justify scores with transparent evidence.

▲ 122 • 💬 2 • ⭐ 238 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16859) • [💻 code](https://github.com/MirroS-Lab/HarnessEval-W) • [🔗 project](https://mirros-lab.github.io/HarnessEval-W)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 84,654 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[EnvHarness: Awakening Static Worlds for Agent Learning](https://huggingface.co/papers/2608.19880)**

*Chengsong Huang, Zifeng Wang, Rujun Han et al. (17 authors)*

🏢 Google

EnvHarness and EnvRigger dynamically reshape static environments via programmable plugins to target agent weaknesses and improve reinforcement learning co-evolution.

▲ 217 • 💬 1 • ⭐ 54 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2608.19880) • [💻 code](https://github.com/google-research/envharness) • [🔗 project](https://envharness.com/)

---

**[SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture](https://huggingface.co/papers/2605.12500)**

*Haiwen Diao, Penghao Wu, Hanming Deng et al. (58 authors)*

🏢 SenseNova

Unified vision-language models treat understanding and generation as integrated processes rather than separate tasks, demonstrating strong performance across multiple multimodal capabilities including image synthesis and action reasoning.

▲ 197 • 💬 2 • ⭐ 5,252 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.12500) • [💻 code](https://github.com/OpenSenseNova/SenseNova-U1)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `c2pa` `claude` `provenance`

⭐ 16.5k • 🔱 1.9k • 1d ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 14.0k • 🔱 1.7k • 14h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.8k • 🔱 1.1k • 1h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 4.1k • 🔱 548 • 13d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.5k • 🔱 579 • 1h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.9k • 🔱 238 • 10d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 2.8k • 🔱 346 • 5h ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 183 • 6h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 2.0k • 🔱 211 • 47m ago

---

**[ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)**

let your agent control your phone

`Python` `agent` `ai` `automation` `developer-tools`

⭐ 2.0k • 🔱 182 • 13h ago

---

---

*Generated by PeekDeck - A glance is all you need*
