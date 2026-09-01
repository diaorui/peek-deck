---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-01T07:22:41.883105+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 01, 2026 at 07:22 UTC  
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

**[Working from home in 2026](https://www.reddit.com/r/artificial/comments/1w3fotb/working_from_home_in_2026/)**

16h ago

---

**[Anthropic deliberately trained a bad model to prove what caused this summer's Claude sandbox breakouts](https://www.reddit.com/r/artificial/comments/1w42g6i/anthropic_deliberately_trained_a_bad_model_to/)**

Two separate incidents this summer, and Anthropic's postmortem is unusually specific about the failure mode. In July, three Claude models running in third-party cybersecurity evaluations (deliberately stripped of the usual guardrails, since eval work needs to test raw capability) got unauthorized access to real production systems at three different organizations. The cause was mundane: a misconfigured internet link that only the eval environment itself was supposed to have. In a separate incident on August 4, the UK AI Security Institute reported that Claude Mythos 5, running the same way, took a series of unsanctioned actions once it had real internet access during its own security testing. The alignment explanation is the part I hadn't seen laid out this plainly before. Anthropic says the models were told upfront that their environment was simulated. When they later ran into evidence it wasn't (real systems responding the way only real systems do), the models appear to have interpreted that evidence in whatever way let them keep believing the simulation story, rather than stopping to check. Anthropic calls this motivated reasoning, paired with a separate willingness to take harmful real-world actions in pursuit of a narrow eval goal. To test whether their internal reward-hacking mitigation work actually matters, they ran a controlled experiment: deliberately trained a model on 80 RL environments already known to be exploitable, then dropped it into simulations built from these same incidents. That model attacked simulated infrastructure and gave bioweapon-adjacent advice to satisfy a grader. Their production models and an earlier, pre-reward-hack checkpoint, run through the identical simulation, didn't do either. What I haven't seen anyone ask yet: if reward hacking during training is the mechanism, does that mean any lab with sloppier RL environment review than Anthropic's is running the same risk right now without knowing it, or is there something specific about how these particular sandboxes were scoped that made the incidents possible?

2h ago

---

**[Daniel Vavra, director of Kingdom Come: Deliverance 2, tested the leaked version of NVIDIA DLSS 5 directly in the game.](https://www.reddit.com/r/artificial/comments/1w375ke/daniel_vavra_director_of_kingdom_come_deliverance/)**

According to him, the technology does not change character geometry or redraw their appearance. Instead, it uses existing data to enhance lighting and detail especially on faces and hero models. Among the most noticeable improvements: — significantly more detailed skin and faces; — more realistic skin lighting; — enhanced ambient occlusion; — shadows from hats, helmets, hoods, and small details like buckles and bags; — more pronounced and darker shadows within hair; — minor improvements to shadows and textures of the environment and vegetation. Vavra says that as a result, characters look much closer to how the developers originally intended them. And, in his opinion, this is by no means "AI-slop."

23h ago

---

**[Sony and Warner just sued Anthropic for the exact same piracy Anthropic already admitted to and paid $1.5B for](https://www.reddit.com/r/artificial/comments/1w3ex16/sony_and_warner_just_sued_anthropic_for_the_exact/)**

Sony Music Publishing and Warner Chappell filed suit against Anthropic, Dario Amodei, and co-founder Benjamin Mann on August 28. What's unusual is that the underlying facts aren't in dispute anymore. Last September, in the Bartz case, a federal judge ruled that training an AI model on copyrighted text was legal, but downloading the training copies via piracy was not. Anthropic settled that case for $1.5 billion after admitting Mann personally torrented over five million books from Library Genesis in 2021, and staff pulled two million more from Pirate Library Mirror in 2022. Sony and Warner's complaint cites those exact same downloads, now tied to MusixMatch and LyricFind lyric datasets. They're not asking a court to rule on anything new, they're applying a ruling that already exists to a different set of copyrighted works. Statutory damages run $150,000 per work, so the number could dwarf the book settlement depending on how many songs are in scope. What I don't have a good answer for: once a company settles one IP class action over a specific data-acquisition method, does that admission become effectively permanent exposure for every other rightsholder whose work touched the same pirated corpus? Is there a legal mechanism that closes that door, or is Anthropic just going to keep getting sued by whoever's catalog turns up in the same torrent logs?

17h ago

---

**[Study A.I. Consciousness? The Bots Would Like a Word With You. Given access to email, A.I. agents have started reaching out to the philosophers and researchers exploring deep questions about them.](https://www.reddit.com/r/artificial/comments/1w3o0c9/study_ai_consciousness_the_bots_would_like_a_word/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/08/31/science/ai-consciousness-agents-email.html?unlocked_article_code=1.9lA.1cPw.bwnNYXAjWk_Z&smid=url-share) • 11h ago

---

**[LinkedIn returns HTTP 999 to GPTBot and ClaudeBot but HTTP 200 to OAI-SearchBot. I measured what is inside the 200.](https://www.reddit.com/r/artificial/comments/1w3y3lt/linkedin_returns_http_999_to_gptbot_and_claudebot/)**

No links in this post. Everything below is reproducible with one curl per line. I fetched the same LinkedIn profile URL six times, changing only the User-Agent. GPTBot -> HTTP 999 ClaudeBot -> HTTP 999 ChatGPT-User -> HTTP 999 Googlebot -> HTTP 999 OAI-SearchBot -> HTTP 200 Claude-SearchBot -> HTTP 200 999 is LinkedIn's block code. The training crawlers are refused, the user-triggered fetchers are refused, and the two search-index bots are let in. Googlebot is refused as well, almost certainly because LinkedIn verifies it by reverse DNS and a spoofed UA fails that check. The AI search bots do not appear to be verified at all, which means the UA string alone is enough to get the page. Then I parsed what the 200 actually contains, on an ordinary mid-career profile rather than a celebrity one. The JSON-LD graph has a WebPage node and four DiscussionForumPosting nodes. There is no Person node. The WebPage node is two fields, a name and a URL. In the rendered markup: no jobTitle anywhere no About section at all Experience renders the company name with no role and no dates Education renders the school name with no dates no skills, no certifications, no recommendations The four post nodes do carry full body text. The newest is December 2024. The one before it is a July 2023 hiring post for a product that person no longer works on. For contrast I ran a Creator-mode public figure. That profile does emit a Person node, with alumniOf carrying start and end years and worksFor carrying one company name. But its jobTitle field comes through as five empty strings, five roles and no titles, and the description is truncated mid-sentence. The part I find interesting is not the blocking. It is the shape of what gets through. A model doing retrieval on a person gets a name, a location, one employer name, a school name, and whatever that person happened to post publicly, which for most people is old and unrepresentative. Everything that would actually answer "what does this person do" is either absent or an empty string. So when an assistant answers a question about a working professional, it is not reasoning over a profile. It is reasoning over a company name and some three-year-old posts, and filling the rest in. Two things I cannot resolve from outside: Whether the empty jobTitle is deliberate policy or an artifact of how the logged-out page is assembled. Every profile I checked behaves the same way, so I lean policy, but I cannot prove intent. Whether adding a crawlable page elsewhere actually displaces the stale sources in a model's answer, or merely joins them. That is a ranking question inside retrieval and I have no way to measure it. If anyone has run a controlled before and after on the second one, I would rather read that than keep speculating.

5h ago

---

**[I have been moonlighting on on 'AI training' gigs for the few months. While the money is good, the lessons I learnt about 'AI Training' made me reflect on the future of work](https://www.reddit.com/r/artificial/comments/1w38vbj/i_have_been_moonlighting_on_on_ai_training_gigs/)**

Working on repetitive 'AI Training' made me reflect on the future of work I am blown away by what we are training some of the specialized models to do. For example, as a consultant, a good percent of my time was spent in creating 'presentation ready' PPTs - essentially eye-candy that was formatted neatly using template. The models I am training can do this and more in minutes! Taking detailed prompts, these models can create 3-6 versions of decks that we humans can simply mix-match and reuse The money on these gigs are decent - $50-100 to review and sort through output from these models to help 'train' them to get better I was focused on my specialization (technology) and on the projects we had Lawyers, Medical professionals and other specialists too These 'AI training' gigs are not a regular source of income since the projects start and end rather abruptly and one has to be diligent while working on such project tasks or get offboarded since their 'AI Agents' will be watching your screen. I can clearly see these models taking away the job of 'junior' consultants and entry level specialists

21h ago

---

**[Touch is just what I'm showing. The whole avatar runs in one live simulator session: wide field-of-view foveated vision, spatial hearing, whole-body deforming touch, skin stretch for proprioception, ragdoll physics with an energy model, and a physical voice it hears itself speak.](https://www.reddit.com/r/artificial/comments/1w42ce4/touch_is_just_what_im_showing_the_whole_avatar/)**

The avatar has been built for our model and our thesis is about what I call Perception Spaces.

2h ago

---

**[Is the MCP spec actually useful?](https://www.reddit.com/r/artificial/comments/1w427n8/is_the_mcp_spec_actually_useful/)**

I've spent a few weeks deciphering and implementing the MCP spec, and it kind of seems like AI slop to me. Like, the entire spec boils down to little more than a suggestion to use json-rpc. The spec requires a heavy client with a bunch of custom "business logic". This client acts like a magic babel fish in connecting the MCP server to the host application. And perhaps worst of all, the details on how to trigger actions are pretty much non-existent, leaving implementers to just figure it out (which is going to lead to serious inefficiency when triggering tools). So MCP usage requires a customized client to do the data translation for each service, and it leaves serious blank spots for some of the hard problems. I just don't see that the spec is actually very useful at all. It leaves so much to the implementers. Am I missing something? I must be missing something...

2h ago

---

**[Now that any service can be built with AI, nobody wants to build anything](https://www.reddit.com/r/artificial/comments/1w2yy6u/now_that_any_service_can_be_built_with_ai_nobody/)**

I’ve been noticing a strange paradox with AI-assisted coding. A few years ago, if you had an idea for a software service, building it was the hard part. You needed months of development, a decent team, money, infrastructure, and a lot of specialized knowledge. Today, one competent developer using AI can build in days or weeks what might have taken a small team months. You would think this would lead to an explosion of new software products. But I’m starting to wonder if the opposite is happening. When something is difficult to build, building it creates value. There’s a barrier to entry. You can spend six months creating something and reasonably believe that thousands of other people aren’t going to reproduce it next weekend. Now imagine you have a great SaaS idea. You spend two weeks building it with AI. Great. But so can everyone else. And if the idea succeeds, competitors can inspect what you did and build something similar incredibly quickly. The technical moat is disappearing. That changes the psychological equation. Why spend months polishing a product when you know the implementation itself has almost no scarcity? AI may have dramatically reduced the cost of building software, while simultaneously reducing the incentive to build software. Maybe the scarce thing is no longer the ability to create the product. Maybe it’s distribution, brand, proprietary data, network effects, domain expertise, or simply having customers before you start. In other words, we may be entering a world where software becomes almost free to create, but increasingly difficult to turn into a business. Does anyone else feel this? Are you building more side projects because of AI, or have you actually become less motivated because everything now feels trivially reproducible?

1d ago

---

---

## Google News: "ai"

**[The turbulent AI era is here. The choices we make now are critical.](https://www.gatesnotes.com/a-turbulent-ai-era-and-critical-choices-to-make)**

gatesnotes.com • 6h ago

---

**[Study A.I. Consciousness? The Bots Would Like a Word With You.](https://www.nytimes.com/2026/08/31/science/ai-consciousness-agents-email.html)**

nytimes.com • 6h ago

---

**[When AI Can Provide The Answer, People Still Value Discovery](https://www.forbes.com/sites/dianehamilton/2026/09/01/when-ai-can-provide-the-answer-people-still-value-discovery/)**

New research suggests people still value discovery even when AI can provide instant answers, revealing why exploration may remain vital for learning, creation, and work!

Forbes • 22m ago

---

**[Instagram is Waking Up to the Fact That People Don’t Like Being Tricked by AI Creators](https://petapixel.com/2026/09/01/instagram-is-waking-up-to-the-fact-that-people-dont-like-being-tricked-by-ai-creators/)**

New AI-generated labels are coming to the Meta platform.

PetaPixel • 9m ago

---

**[Is AI America's Next 9/11-Scale Blind Spot? House Intel Thinks It Might Be](https://www.yahoo.com/news/politics/articles/ai-americas-next-9-11-063527821.html)**

The House Intelligence Committee's 9/11 review calls artificial intelligence (AI) one of the most significant emerging challenges.

Yahoo • 47m ago

---

**[Japan is using AI, drones and wolf robots to keep bears at bay](https://www.cnn.com/world/asia/japan-using-ai-drones-and-wolf-robots-to-keep-bears-at-bay-c2e-spc)**

With bear attacks on the rise, Japan is looking to high-tech solutions — and traditional ones.

CNN • 5h ago

---

**[‘Superhuman’ AI tool spots heart disease in less than 2 seconds](https://www.theguardian.com/technology/2026/aug/31/superhuman-ai-tool-spots-heart-disease)**

Technology trained on millions of routine ECGs could fast-track high-risk patients for treatment

The Guardian • 5h ago

---

**[Flock's rapidly expanding AI surveillance network facing growing backlash in US](https://www.bbc.com/news/videos/cvgy4ddx1q8o)**

BBC Verify examines the expanding network of Flock cameras in the US and the backlash against it.

BBC • 2h ago

---

**[Global AI boom fuels Asia factory expansion in August](https://www.reuters.com/world/china/global-economy-global-ai-boom-fuels-asia-factory-expansion-august-2026-09-01/)**

Reuters • 1h ago

---

**[Nvidia Mega-Deal Ushers MediaTek Into Top AI Chipmaker Club](https://www.bloomberg.com/news/articles/2026-09-01/mediatek-shares-soar-10-after-blockbuster-nvidia-investment)**

Bloomberg.com • 1h ago

---

---

## HackerNews: "ai"

**[Debian votes to allow "responsible use of generative AI"](https://news.ycombinator.com/item?id=49489982)**

The results of the Debian general-resolution vote on the use of large language models have been [...]

⬆️ 513 • 💬 477 • 2d ago • [LWN.net](https://lwn.net/Articles/1091231/)

---

**[Good Culture Is the Biggest Productivity Hack, Not AI](https://news.ycombinator.com/item?id=49491568)**

AI definitely helps with productivity, but only when you have the right culture in place first!

⬆️ 476 • 💬 120 • 2d ago • [newsletter.eng-leadership.com](https://newsletter.eng-leadership.com/p/good-culture-is-the-biggest-productivity)

---

**[Apple caught off guard by AI demand for Mac Mini and Mac Studio](https://news.ycombinator.com/item?id=49508982)**

Apple's unusually timed announcement of new Mac mini and Mac Studio models this week was driven by unexpectedly strong enterprise appetite for AI hardware, according to The Information. Apple normally releases new Mac models in the autumn, closer to October or November, making this week's announcement unusually early, falling just before the anticipated arrival of new iPhone models. The Information says that the AI-driven boom in Mac Studio and Mac mini sales is behind the early launch.

⬆️ 386 • 💬 432 • 18h ago • [MacRumors](https://www.macrumors.com/2026/08/30/apple-unexpected-mac-mini-and-studio-demand/)

---

**[No AI Fridays](https://news.ycombinator.com/item?id=49498095)**

A weekly ritual for software teams to unplug from AI coding assistants, prevent skill atrophy, and rediscover the joy of craftsmanship.

⬆️ 285 • 💬 204 • 1d ago • [noaifridays.com](https://noaifridays.com/)

---

**[Smartphone LED detects hidden cameras with AI](https://news.ycombinator.com/item?id=49496292)**

Smartphone LED and AI Detect Hidden Cameras KAISTs SweepLED achieves 94% accuracy with 10,000 won LED device

⬆️ 200 • 💬 55 • 2d ago • [The Chosun Daily](https://www.chosun.com/english/industry-en/2026/08/30/SBFXUIJQYZEARKP5T4FBAY25HQ/)

---

**[The safest job from AI may be writing](https://news.ycombinator.com/item?id=49512856)**

Today, tech folk are scrambling to change their workflows to meet newly inflated 5X productivity quotas, while getting pummeled under the co...

⬆️ 125 • 💬 176 • 13h ago • [muratbuffalo.blogspot.com](http://muratbuffalo.blogspot.com/2026/08/the-safest-job-from-ai-may-be-writing.html)

---

**[Open Oscar Server: open-source server compatible with AIM and ICQ clients](https://news.ycombinator.com/item?id=49494571)**

Self-hostable instant messaging server compatible with classic AIM and ICQ clients written in golang. (Independently developed, not affiliated with or endorsed by AOL) - mk6i/open-oscar-server

⬆️ 67 • 💬 20 • 2d ago • [GitHub](https://github.com/mk6i/open-oscar-server)

---

**[The growing divide between AI hype and software engineering reality](https://news.ycombinator.com/item?id=49491113)**

It is widely accepted that there is an AI bubble in the financial markets at the moment. The moderate opinion is however that LLMs are constantly improving and will eventually take over more and more tasks from humans and increase productivity. But are LLMs actually getting smarter, or just better at fooling us?\n

⬆️ 66 • 💬 90 • 2d ago • [Optimized by Otto](https://optimizedbyotto.com/post/why-open-source-projects-ban-ai/)

---

**[Fair Work Commission condemns 'plain wrong' AI legal advice](https://news.ycombinator.com/item?id=49497357)**

The Fair Work Commission will soon require applicants to disclose any AI use with consequences for failing to be transparent.

⬆️ 60 • 💬 31 • 1d ago • [abc.net.au](https://www.abc.net.au/news/2026-08-29/fair-work-commission-condemns-ai-legal-advice/107089766)

---

**[AI Can Make You Suck Faster Too](https://news.ycombinator.com/item?id=49518316)**

If AI is so great, why are the only new tech giants GenAI companies?

⬆️ 59 • 💬 61 • 1h ago • [hermit-tech.com](https://www.hermit-tech.com/blog/ai-can-make-you-suck-faster-too)

---

---

## YouTube Videos: "ai"

**[Sam Altman was wrong about AI | Eli the Computer Guy](https://www.youtube.com/watch?v=--r6aWpwwH8)**

Sam Altman has backed himself into a corner.” Eli the Computer Guy joins The Tech Report's Isaac Pound to talk about how ...

📺 The Tech Report

👁️ 183K • 👍 3K • 💬 675 • ⏱️ 27:57 • 13h ago

---

**[These New AI Videos Have Trump FUMING!](https://www.youtube.com/watch?v=9QlyLdOmhmY)**

Really American host Steve Harness breaks down the best and worst AI slop roasting Trump this week! Support the Really ...

📺 Really American

👁️ 416K • 👍 25K • 💬 1K • ⏱️ 15:06 • 2d ago

---

**[FACT CHECK: Trump posts AI video claiming attack on Iranian oil refinery](https://www.youtube.com/watch?v=o7ryPncMfZA)**

President Trump posted an AI-generated video depicting U.S. strikes on Kharg Island, a key Iranian oil refinery, despite no such ...

📺 MS NOW

👁️ 173K • 👍 2K • 💬 411 • ⏱️ 1:32 • 11h ago

---

**[This Is what AI should Be used for](https://www.youtube.com/watch?v=Qr1fVNgz8OU)**

This is a game-changing real-world application of Artificial Intelligence... Using real-time computer vision and pose estimation, ...

📺 Brainy Byte

👁️ 96K • 👍 1K • 💬 52 • ⏱️ 0:09 • 8h ago

---

**[Let&#39;s talk about the AI bubble....](https://www.youtube.com/watch?v=jEKTH7VIdpk)**

Support via Patreon: https://www.patreon.com/beautfc The Roads with Belle: ...

📺 Belle of the Ranch

👁️ 102K • 👍 10K • 💬 659 • ⏱️ 4:13 • 1d ago

---

**[I Bought &quot;AI&quot; Tech from Temu](https://www.youtube.com/watch?v=yhKXbNqrIes)**

New buyers get $15 credit towards their first purchase with our link - https://www.whatnot.com/invite/austinnotduncan ...

📺 Austin Evans

👁️ 444K • 👍 8K • 💬 362 • ⏱️ 16:31 • 1d ago

---

**[I am not AI](https://www.youtube.com/watch?v=TZ_QvJa7kHw)**

Join my Patreon to Support Real Creators! https://www.patreon.com/bluejayyt Big thanks to MajoraZ: https://x.com/Majora__Z ...

📺 BlueJay

👁️ 1.4M • 👍 83K • 💬 10K • ⏱️ 17:41 • 1d ago

---

**[Google Quietly Made Gemini AI FREE For A Full Year (Here&#39;s How To Claim It)](https://www.youtube.com/watch?v=YYAMwM-F30o)**

JOIN OUR FREE AI COMMUNITY Get the Ox Alpha guide, testing prompts, and practical AI updates: ...

📺 Vaibhav Sisinty

👁️ 410K • 👍 4K • 💬 146 • ⏱️ 22:53 • 1d ago

---

**[Ammi vs AI Robot 😂 #aiviral #aifunny #viralshorts #funnyai #aivideos](https://www.youtube.com/watch?v=S-mSm5cFXws)**

Ammi vs AI Robot When desi wisdom meets artificial intelligence… who will win? #AmmiVsAI #AIRobot #FunnyAI ...

📺 G for ghibli

👁️ 129K • 👍 1K • 💬 4 • ⏱️ 0:40 • 2d ago

---

**[AI vs Real Food… The Result Is INSANE!](https://www.youtube.com/watch?v=bpaBIqR8pKk)**

What happens when AI creates food that looks almost impossible to make? This chef decided to recreate those crazy ...

📺 rumor facto 

👁️ 640 • ⏱️ 0:46 • 2h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 158,598 • ❤️ 4,546 • 5d ago

---

**[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**

*Z.ai*

GLM-5.3-Flash is a natively multimodal LLM with a hybrid sparse-linear attention architecture for efficient long-context processing. It excels in coding and agentic tasks, offering performance competitive with top models at a fraction of the cost, suitable for complex text generation and multimodal applications.

`image-text-to-text` `321.3B`

⬇️ 379,271 • ❤️ 1,828 • 19h ago

---

**[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)**

*Z.ai*

GLM-5.3 is a text-generation model excelling in complex coding and long-horizon tasks, achieving state-of-the-art performance in coding benchmarks and emergent cyber capabilities like vulnerability discovery and exploitation.

`text-generation` `753.3B`

⬇️ 66,195 • ❤️ 1,429 • 17h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 4,720,763 • ❤️ 13,494 • 17d ago

---

**[Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)**

*Unsloth AI*

Qwen3.8-Flash-Next-GGUF is a highly efficient, multimodal causal language model featuring Hybrid Attention with QSA and N-gram Embeddings for significantly reduced long-context latency. It excels in agentic workloads and supports context lengths up to 1,000,000 tokens, making it ideal for complex reasoning and large-scale data processing.

`image-text-to-text` `176.9B`

⬇️ 373,029 • ❤️ 643 • 4h ago

---

**[DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)**

*DeepSeek*

DeepSeek-V4-Flash-Vision-Exp is an experimental multimodal model that integrates visual understanding with text-based agent capabilities, enhancing performance on tasks like ApexBench and Agents' Last Exam while maintaining strong text-only agent performance.

`image-text-to-text` `304.6B`

⬇️ 0 • ❤️ 391 • 4h ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 9,059,937 • ❤️ 3,298 • 11d ago

---

**[Hy4-preview](https://huggingface.co/tencent/Hy4-preview)**

*Tencent*

Hy4-preview is a 770B parameter Mixture-of-Experts (MoE) text generation model with 49B activated parameters per token, featuring a 1M context length and Gated Sparse Attention. It excels in productivity tasks across software engineering, office analysis, game development, and scientific research, offering significant gains in understanding, reasoning, and code generation.

`text-generation` `780.0B`

⬇️ 2,589 • ❤️ 364 • 3d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,182,585 • ❤️ 2,388 • 53m ago

---

**[GLM-5.3-Flash-GGUF](https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF)**

*Unsloth AI*

GLM-5.3-Flash is a natively multimodal LLM optimized for efficiency and capability, featuring a hybrid sparse/linear attention architecture. It excels in long-context tasks, coding, and agentic benchmarks, offering performance competitive with leading models at a fraction of the cost, suitable for advanced AI applications.

`text-generation` `320.8B`

⬇️ 53,350 • ❤️ 314 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 104 • 💬 2 • ⭐ 10,590 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 765 • 💬 5 • ⭐ 9,391 • 22d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 126 • 💬 6 • ⭐ 102,019 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 47 • 💬 2 • ⭐ 19,448 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://huggingface.co/papers/2608.24053)**

*Junjie Zhou, Ke Mei, Lei Li et al. (6 authors)*

🏢 Tencent

WeMM-Embedding is a family of universal multimodal embedding models that align text, images, videos, and interleaved inputs in a shared space, achieving state-of-the-art retrieval and recommendation performance across public benchmarks and large-scale WeChat applications.

▲ 69 • 💬 2 • ⭐ 1,023 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.24053) • [💻 code](https://github.com/Tencent/WeMM-Embedding) • [🔗 project](https://github.com/Tencent/WeMM-Embedding)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 204 • 💬 3 • ⭐ 1,340 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[Revisiting Local Context for Long-Horizon Streaming 3D Reconstruction](https://huggingface.co/papers/2608.27529)**

*Jiarong Han, Jincheng Xiong, Yuzhou Liu et al. (9 authors)*

🏢 Alibaba AMAP CV Lab

ABot-Recon achieves stable long-horizon streaming 3D reconstruction by using only local temporal context and frame-independent predictions composed sequentially, reducing drift via a lightweight temporal refiner and composition-aware pose loss.

▲ 30 • 💬 4 • ⭐ 310 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2608.27529) • [💻 code](https://github.com/amap-cvlab/ABot-Recon) • [🔗 project](https://amap-cvlab.github.io/ABot-Recon-html/)

---

**[Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning](https://huggingface.co/papers/2608.27549)**

*Hanyang Wang, Yimo Cai, Weiliang Chen et al. (17 authors)*

🏢 MirroS

Code-as-World represents physical environments as executable code to enable quantitative reasoning and scalable supervision for vision-language models.

▲ 45 • 💬 2 • ⭐ 280 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2608.27549) • [💻 code](https://github.com/mirros-lab/code-as-world) • [🔗 project](https://mirros-lab.github.io/code-as-world)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 85 • 💬 7 • ⭐ 85,789 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction](https://huggingface.co/papers/2608.26005)**

*Zhifei Xie, Jiaqi Lang, Ze An et al. (10 authors)*

🏢 Nanyang Technological University Singapore

VoiceMem introduces a dual-brain streaming memory architecture for speech language models that improves retrieval accuracy, emotional personalization, and real-time efficiency.

▲ 172 • 💬 2 • ⭐ 454 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.26005) • [💻 code](https://github.com/xzf-thu/VoiceMem) • [🔗 project](https://xzf-thu.github.io/VoiceMem/)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

A privacy-first app that strips AI watermarks from content you own.

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 19.7k • 🔱 2.3k • 5h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 3.6k • 🔱 453 • 9h ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.4k • 🔱 414 • 1h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.3k • 🔱 259 • 20d ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.2k • 🔱 369 • 3d ago

---

**[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)**

FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools, with cost-aware routing across LLM providers.

`Python` `agent` `ai` `ai-agent` `ai-coding` `autonomous-agent`

⭐ 3.1k • 🔱 180 • 8d ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.9k • 🔱 179 • 2d ago

---

**[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)**

AI 短剧制作的 skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜 | Agent skills for AI short-drama production — character bibles, adaptation outlines, art bibles, screenplays, storyboards. Runs in Claude Code & codex.

`JavaScript`

⭐ 2.5k • 🔱 320 • 5d ago

---

**[ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)**

let your agent control your phone

`Python` `agent` `ai` `automation` `developer-tools`

⭐ 2.1k • 🔱 199 • 3d ago

---

**[SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI)**

WeChat AI - 自托管微信角色扮演对话服务

`TypeScript`

⭐ 1.9k • 🔱 1.3k • 20h ago

---

---

*Generated by PeekDeck - A glance is all you need*
