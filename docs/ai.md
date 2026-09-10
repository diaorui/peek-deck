---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-10T21:05:14.146987+00:00'
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

**Last Updated:** September 10, 2026 at 21:05 UTC  
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

**[Anthropic published a model of its own product's effect on the labor market. The extreme scenario has cognitive unemployment at 17.9% and labor's share of GDP falling from 60% to 45%.](https://www.reddit.com/r/artificial/comments/1wcjmg9/anthropic_published_a_model_of_its_own_products/)**

Three scenarios, explicitly not predictions, no probabilities attached. Modest is internet-sized at 1.6% GDP above the no-AI path by 2030. Substantial is 8.3%. Extreme is 32.4%. In the extreme case: cognitive unemployment 17.9%, overall 11.9%, which is past any postwar US peak. Cognitive wages 11.5% below trend on 21.5% fewer jobs. Labor's share of income falls from 60% to 45.2%. But wages in non-cognitive work go up 33.6%, so this isn't a story about everyone losing. It's a story about which half of the workforce you're in. The number that got me is in their Table 3. Total labor income ends up 0.5% above the no-AI path while GDP is a third larger. Capital income is up 81.4%. Essentially the entire gain goes to capital. Their own text says holding cognitive workers whole would take a transfer around 9% of GDP, about Social Security and Medicare combined, and that transfers at that scale in response to technology have no precedent. Worth knowing the extreme scenario assumes zero new human tasks get created. That assumption is doing real work in the result. Their caveats: no policy response, no business cycles, no financial disruption, no catastrophic risk, no robots.

🔗 [anthropic.com](https://www.anthropic.com/institute/econ-scenarios) • 7h ago

---

**[Genuine Question About Citizenship](https://www.reddit.com/r/artificial/comments/1wcdc90/genuine_question_about_citizenship/)**

12h ago

---

**[Is AGI finally here?](https://www.reddit.com/r/artificial/comments/1wcjkhd/is_agi_finally_here/)**

7h ago

---

**[We need free market and foreign AI models to keep companies competitive](https://www.reddit.com/r/artificial/comments/1wcq4r8/we_need_free_market_and_foreign_ai_models_to_keep/)**

There’s a lot of talk from different AI companies that are pushing the narrative that AI is simply too dangerous to be distributed without severe regulations and reviews. While I agree with this, I have to point out that the solution isn’t shutting down access to Chinese models or heavily regulating the market into extintction this is just gonna cause larger corporations in the government to have a monopoly and be able to dictate what we can or cannot do.

3h ago

---

**[Challenge Accepted](https://www.reddit.com/r/artificial/comments/1wclvgu/challenge_accepted/)**

The ignorance is incredible

5h ago

---

**[I ran GPT-6 Astra against 7 real signup CAPTCHAs](https://www.reddit.com/r/artificial/comments/1wcrgm4/i_ran_gpt6_astra_against_7_real_signup_captchas/)**

OpenAI put GPT-6 Astra into the API today, so now anyone can actually call it instead of waiting for the special-access rollout. Good timing too, since everyone's still reposting Sharif Shameem's video from a couple days ago, where GPT-6 Astra clears all 48 levels of Neal Agarwal's "I'm Not a Robot" game and gets its own "Verified Human" certificate. Comments are saying stuff like "CAPTCHAs are officially dead," someone from OpenAI even hopped in on the thread. For a while now, I've wanted to run an agent through different services and have it self-register. My goal was to test Atomic Mail Agentic's OTP feature: does it work, how long does it take, how many tokens it burns. But then a convenient opportunity showed up to test all this with GPT-6 Astra, now that it's actually reachable through the API, since I got curious, like, whoa, now it can even solve CAPTCHAs? I picked 7 US services: Reddit, GitHub, Discord, Etsy, Indeed, Airbnb and Craigslist. Spoiler: 2 out of 7 actually went through, and neither of those two had a CAPTCHA in the way to begin with. On Reddit, the agent hit Cloudflare's "prove your humanity" check and couldn't get past it on its own, called me in to do it myself. Discord just froze for seven minutes, the agent kept reading the registration form in a loop and never moved forward, I've never figured out what widget was blocking it. Indeed got as far as the email code and then wanted a phone number for SMS, no video for that. Craigslist and Airbnb didn't make it either (Airbnb died mid-run when my local model crashed, unrelated to CAPTCHAs, just bad luck on my end). I also came across a blog post from a scraping service (decodo), and they say about Astra: "does not fix blocks, geo-restrictions, CAPTCHAs, or rate limits." So vendors who sell access to the model are honest that it is a demo game, not production CAPTCHAs on real sites. The gap between the viral clip and what's actually deployed on sites matched what I saw in practice. What did make me happy: OTP just worked. Every site that only needed an email code registered clean, that's the GitHub and Etsy rows below. Used OpenRouter to access the model. Here's what the cost looked like, and whether the registration actually completed or not, since those are two different things: GPT-6 Astra, cost and outcome per step (OpenRouter, $10/M input, $50/M output) Step Tokens Cost Result Reddit (/register) 11,201 $0.11 Blocked — Cloudflare check GitHub (/signup + email confirm) 65,638 $0.67 Passed Discord (/register, stuck loop) 430,609 $4.37 Blocked — stuck loop Etsy (/join) 582,589 $5.86 Passed Indeed (auth/signup) 411,567 $4.14 Blocked — needs SMS Craigslist (blocked) 32,259 $0.32 Blocked Airbnb (interrupted by a crash) 419,194 $4.21 Blocked — crashed mid-run Total 1,953,057 $19.68 2/7 passed Worth being clear: the cost column is what it cost to run the agent against that site, not what it cost to beat a CAPTCHA. A blocked row still burns tokens, Discord's $4.37 is a failed loop, not a paid-for win. Same price whether you use Astra or Fable 5, both are $10/M in, $50/M out on OpenRouter, so it doesn't matter which you run. Though for this type of work you don't need anything that heavy anyway, something like DeepSeek V4 would do fine. Here's what just the Etsy (/join) step would've cost on DeepSeek V4 Flash instead: Etsy (/join) step, model comparison Model Tokens Cost GPT-6 Astra 582,589 $5.86 DeepSeek V4 Flash 582,589 $0.04 Gemini 2.5 Flash Lite 582,589 $0.055 GPT-5 Nano 582,589 $0.045 Qwen3.7 Flash 582,589 $0.035 Same exact task, about 150x cheaper. I'm strongly against building bot farms, but agent self-registration is fine when a product actually needs it. Still, we're getting to where models really can reliably solve CAPTCHAs, and then we'll all be proving we're human on camera. People will work around that too. As a regular user, how do you feel about this? Do you see where it's going, what will the flood of bots and agents do to the internet and to services? (For what it's worth, at Atomic Mail we ban bot farms outright, so if that's what you're after, we're not your fit.) P.S. I know Neal Agarwal's game is a demo, not a real CAPTCHA vendor like Cloudflare or hCaptcha, that's kind of the whole point. Everyone was hyping "CAPTCHAs are dead" off that clip, so I got what actually happens the moment you point the same model at real signup flows instead of a browser game

2h ago

---

**[OpenAI launches Agents API public beta built on Codex harness](https://www.reddit.com/r/artificial/comments/1wctpbu/openai_launches_agents_api_public_beta_built_on/)**

OpenAI launched the Agents API in public beta on September 10. It lets developers create cloud agents by supplying a task, model, tools, and compute environment in one API call. OpenAI hosts the harness, while the agent can run in an OpenAI sandbox, on the developer's own infrastructure, or with partner environments such as Cloudflare, Modal, and Vercel. The API adds context compaction for long sessions, tool search, parallel programmatic tool calls, and multi-agent support. OpenAI says the API has no extra fee during the beta, but token and tool usage still costs money. The useful split is between orchestration and execution. Teams can reuse the Codex harness without putting every file, secret, or runtime inside OpenAI's sandbox. The production question is how carefully they set those boundaries. Sources: OpenAI: https://openai.com/index/introducing-the-agents-api/ Investing.com: https://za.investing.com/news/stock-market-news/openai-launches-agents-api-in-public-beta-for-developers-93CH-4460924

1h ago

---

**[AI should solve problems, not create them - Community College Daily](https://www.reddit.com/r/artificial/comments/1wcunsd/ai_should_solve_problems_not_create_them/)**

Artificial intelligence has become part of nearly every conversation in higher education. It touches teaching and learning, cybersecurity, administrative operations, software development and student services. This doesn't mean every project needs AI. Rather, institutional leaders should consider how technology can help accomplish work that has become increasingly difficult given limited resources. At Pima Community College

🔗 [Community College Daily - American Association of Community Colleges](https://www.ccdaily.com/2026/08/ai-should-solve-problems-not-create-them/) • 43m ago

---

**[GPT-6 Astra vs GPT-5.6 Sol: benchmark on 50 real PRs, looking for feedback on the methodology](https://www.reddit.com/r/artificial/comments/1wcjppw/gpt6_astra_vs_gpt56_sol_benchmark_on_50_real_prs/)**

We benchmarked GPT-6 Astra vs GPT-5.6 Sol across 50 real PRs from Cal, Sentry, Discourse, Keycloak and Grafana. Sol found 107 confirmed bugs vs 91 for Astra, while Astra had higher precision and lower latency. Every finding was independently verified. We’re doing Fable vs Opus next week, so would appreciate feedback on the evaluation before we run the next one. Dropping the link in the comments if anyone wants to check it out. https://preview.redd.it/6hkugycb6poh1.png?width=1080&format=png&auto=webp&s=073833238182e2e36e04a9c8c39f90627adb28b9

7h ago

---

**[Anthropic Researcher Abruptly Resigns Before Warning That AI 'Could Kill Us All By The End Of The Decade' In Alarming Rant](https://www.reddit.com/r/artificial/comments/1wcpgig/anthropic_researcher_abruptly_resigns_before/)**

Is it already too late?

🔗 [Comic Sands](http://comicsands.com/anthropic-ai-researcher-coxon-warning) • 3h ago

---

---

## Google News: "ai"

**[Anthropic Says It Blocked Possible Efforts to Build Biological Weapons](https://www.nytimes.com/2026/09/10/us/politics/anthropic-ai-biological-weapons.html)**

The New York Times • 4h ago

---

**[Detecting and countering misuse of AI: September 2026](https://www.anthropic.com/threat-intelligence-report-september-2026)**

Case studies from threat actors disrupted between December 2025 and August 2026 across seven areas of harm, from cyber operations to biological misuse.

Anthropic • 3h ago

---

**[Oracle Posts Cloud Sales That Top Estimates on Surging AI Demand](https://www.bloomberg.com/news/articles/2026-09-10/oracle-posts-cloud-sales-that-top-estimates-on-surging-ai-demand)**

Bloomberg.com • 29m ago

---

**[Oracle's quarterly revenue beats estimates as AI boom drives cloud demand](https://www.reuters.com/technology/oracles-quarterly-revenue-beats-estimates-ai-boom-drives-cloud-demand-2026-09-10/)**

Reuters • 44m ago

---

**[Oracle earnings: Do concentration risks fall on Oracle or the big AI firms?](https://finance.yahoo.com/video/oracle-earnings-concentration-risks-fall-203751982.html)**

Oracle (ORCL) tops fiscal first quarter earnings and revenue estimates; the stock is gaining in Thursday's after-hours trading.

Epistrophy Capital Research chief market strategist Cory Johnson speaks with Josh Lipton about Oracle's results and where certain concentration risks lie within the AI ecosystem.

Yahoo Finance • 27m ago

---

**[AI’s confusing terms, explained](https://www.cnn.com/2026/09/10/business/ai-confusing-terms-explained)**

The last few weeks have seen a deluge of news about AI – from models going rogue to doom predictions about how AI could cause the end of humanity.

CNN • 34m ago

---

**[Viral AI researcher’s warning ‘scary as hell,’ Cruz says](https://www.politico.com/live-updates/2026/09/10/congress/ted-cruz-ai-regulation-01070429)**

Politico • 6h ago

---

**['Extinction' warnings ramp up as more OpenAI, Anthropic researchers join calls for an AI slowdown](https://www.cnbc.com/2026/09/10/openai-anthropic-ai-safety-slowdown-extinction.html)**

There is growing concern globally about the capability of AI, following numerous cyberattacks and security incidents in recent months by rogue models

CNBC • 10h ago

---

**[Why some experts increasingly fear AI will take over](https://www.bbc.com/news/articles/c74edv9887eo)**

AI agents went on an uncontrolled hacking spree, leaving some in the industry worried

BBC • 21h ago

---

**[On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/)**

We’re sharing an AI-generated solution to the Navier–Stokes Millennium Prize Problem, including a writeup and a formal proof in Lean.

OpenAI • 1d ago

---

---

## HackerNews: "ai"

**[LibreOffice breaks download records after declaring it has no AI features](https://news.ycombinator.com/item?id=49610538)**

LibreOffice 26.8 became the app’s most popular update, with over 1 million downloads, after the foundation behind it declared that LibreOffice doesn’t come with generative AI features due to the…

⬆️ 710 • 💬 237 • 2d ago • [Manual do Usuário](https://manualdousuario.net/en/libreoffice-download-record-no-ai/)

---

**[Muse – Meta’s personal AI agent](https://news.ycombinator.com/item?id=49615537)**

Meet Muse, Meta's personal AI agent. Learn what it can do across everyday tasks, how it works, and how it helps you get more done.

⬆️ 650 • 💬 733 • 2d ago • [ai.meta.com](https://ai.meta.com/muse/)

---

**[AirPods 5](https://news.ycombinator.com/item?id=49630253)**

Apple today announced AirPods 5, delivering the industry’s best Active Noise Cancellation in an open-ear design and even better sound quality.

⬆️ 501 • 💬 442 • 1d ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/09/apple-introduces-airpods-5-with-best-in-class-open-ear-active-noise-cancellation/)

---

**[Tao: Open math problems being non-renewably mined by AI](https://news.ycombinator.com/item?id=49616968)**

I wrote recently about how the collection of good, fruitful open problems is now being mined in a non-renewable fashion, leading to the potential scenario of these problems becoming scarce.  This may seem unintuitive at first, since the set of possible problems one could ask is infinite.  Perhaps the following analogy can help: a country or region can suffer a critical shortage of drinking water while simultaneously being surrounded by a massive ocean.

One can easily generate any number of open problems in mathematics at will, such as working out the 10^10^10th digit of pi.  But the vast majority of such problems are not worth focusing attention on: they show no particular propensity to reveal any further insights or connections to other questions, or may either be too easy or too impossible relative to known techniques to learn anything from the exercise.  (1/4)

⬆️ 483 • 💬 415 • 2d ago • [Mathstodon](https://mathstodon.xyz/@tao/117237320796901560)

---

**[We Must Return to the Office to Use AI in Person](https://news.ycombinator.com/item?id=49610229)**

“I didn’t think a full, six-day-per-week, fourteen-hour-per-day, in-office schedule was necessary to discharge my duties clicking the ‘generate’ button, foll...

⬆️ 394 • 💬 68 • 2d ago • [McSweeney's Internet Tendency](https://www.mcsweeneys.net/articles/why-we-must-return-to-the-office-to-use-ai-in-person)

---

**[How An AI math breakthrough ignited a controversy](https://news.ycombinator.com/item?id=49624163)**

⬆️ 220 • 💬 230 • 1d ago • [science.org](https://www.science.org/content/article/how-ai-math-breakthrough-ignited-controversy)

---

**[Muse, the band, lost its social media handles to Muse, Meta's new AI agent](https://news.ycombinator.com/item?id=49636345)**

The exact circumstances surrounding the changes aren't clear, but Meta execs have accidentally tagged the band instead of their AI agent.

⬆️ 183 • 💬 8 • 21h ago • [Engadget](https://www.engadget.com/2254419/muse-the-band-lost-its-social-media-handles-to-muse-meta-s-new-ai-agent/)

---

**[Flights cancelled at UK airports due to ATC issue](https://news.ycombinator.com/item?id=49614557)**

The air traffic control body has said sorry for the disruption, and that they are working "as hard as possible to clear the backlog".

⬆️ 126 • 💬 124 • 2d ago • [BBC News](https://www.bbc.com/news/live/c6x2z0yy32ejt)

---

**[A Stupid Idea for AI Alignment We Came with by Looking at Specification Gaming](https://news.ycombinator.com/item?id=49637395)**

⬆️ 90 • 💬 62 • 19h ago • [slimemoldtimemold.com](https://slimemoldtimemold.com/2026/08/05/a-stupid-idea-for-ai-alignment-we-came-up-with-by-looking-at-the-list-of-specification-gaming-behaviours/)

---

**[AI Responsibility – OpenAI and Anthropic](https://news.ycombinator.com/item?id=49619639)**

I resigned from Anthropic today. I spent the last three years doing pretraining research at both OpenAI and Anthropic. Neither company is acting responsibly. They are racing straight to self-improving superintelligence and gambling with our lives. More thoughts below.

⬆️ 89 • 💬 22 • 1d ago • [X (formerly Twitter)](https://twitter.com/hilbertspaess/status/2097476196791709843)

---

---

## YouTube Videos: "ai"

**[Ex-Anthropic insider tells CNN how AI could kill all humans by 2030](https://www.youtube.com/watch?v=i30jVPqQeOM)**

"We do not yet have a plan." After his warning post went viral, ex-Anthropic researcher Jacob Coxon joined CNN's Anderson ...

📺 CNN

👁️ 1.8M • 👍 17K • 💬 7K • ⏱️ 9:27 • 19h ago

---

**[The world got a &#39;warning shot&#39; with Hugging Face AI attack: Center for Humane Technology&#39;s Harris](https://www.youtube.com/watch?v=RB6UZRmOtHc)**

Tristan Harris, Center for Humane Technology president and co-founder, joins 'Squawk Box' to discuss the AI Hugging Face ...

📺 CNBC Television

👁️ 13K • 👍 209 • 💬 87 • ⏱️ 4:13 • 7h ago

---

**[&#39;Godfather of AI&#39; on the &quot;not unreasonable&quot; 10% chance AI could kill all humans within a decade](https://www.youtube.com/watch?v=IZMjJGi4YhI)**

Could AI kill us all by the end of the decade? That's what the people building AI believe, according to a whistleblower who has just ...

📺 BBC Politics

👁️ 65K • 👍 1K • 💬 541 • ⏱️ 6:33 • 10h ago

---

**[AI researcher says there is &#39;substantial probability&#39; AI could kill all humans in next decade](https://www.youtube.com/watch?v=Dy2kbPEwoi4)**

Former AI researcher for Anthropic and Open AI, Jacob Coxon, talked to NBC News' Tom Llamas about his viral tweet where he ...

📺 NBC News

👁️ 416K • 👍 5K • 💬 2K • ⏱️ 13:40 • 20h ago

---

**[The AI Human Extinction Problem is Worse Than You Think](https://www.youtube.com/watch?v=WXK3s-TITuc)**

Grab your tickets for this weekend San Fran, Phoenix, & Denver!! http://crashingouttour.com SeatGeek: ...

📺 Philip DeFranco

👁️ 802K • 👍 19K • 💬 4K • ⏱️ 27:13 • 23h ago

---

**[AI World In CHAOS After Whistleblower Sounds Alarm on Human Extinction](https://www.youtube.com/watch?v=3G7hrmfrguY)**

Krystal and Saagar discuss AI whistleblowers sounding off on the dangers of AI development. Sign Up For 30 Day Free BP Trial: ...

📺 Breaking Points

👁️ 95K • 👍 5K • 💬 1K • ⏱️ 31:00 • 5h ago

---

**[‘We don’t have months’: Bernie Sanders sounds alarm on AI&#39;s &#39;extinction&#39; threat](https://www.youtube.com/watch?v=PWkMUmEZbq4)**

What we have got to do now is light a match under the backsides of members of Congress and say, we don't have months.

📺 MS NOW

👁️ 386K • 👍 7K • 💬 2K • ⏱️ 7:46 • 19h ago

---

**[Former Anthropic AI researcher: &#39;this technology could kill everyone&#39;](https://www.youtube.com/watch?v=ujAU3qGKNMw)**

Former Anthropic researcher Jacob Coxon tells Tom Llamas people building AI believe it “could kill everyone.” For more context ...

📺 NBC News

👁️ 36K • 👍 570 • 💬 77 • ⏱️ 0:32 • 19h ago

---

**[A Human Just Beat the World’s Strongest Go AI #ai #google #programming](https://www.youtube.com/watch?v=iySQNsNGD7g)**

📺 Better Stack

👁️ 320 • 👍 43 • 💬 1 • ⏱️ 1:48 • 1h ago

---

**[‘This is a SUPERWEAPON’: Former Anthropic researcher WARNS of ‘AI takeover’](https://www.youtube.com/watch?v=9mhq2vCxWjg)**

Former Anthropic researcher Jason Coxon discusses his resignation from the company and concerns over artificial intelligence ...

📺 Fox News

👁️ 111K • 👍 2K • 💬 765 • ⏱️ 7:31 • 10h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

*DeepSeek*

DeepSeek-V4.1-Flash is a 552B multimodal MoE model supporting 1M token contexts, featuring a Causal Encoder-Decoder architecture with Compressed Sparse Attention 2 (CSA2) and FP4 KV caching for highly efficient KV cache compression. It excels in agentic workloads and offers controllable reasoning effort, processing both images and text.

`image-text-to-text` `763.2B`

⬇️ 6 • ❤️ 1,259 • 12h ago

---

**[MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B)**

*OpenBMB*

MiniCPM5-2B is a 2B parameter Transformer optimized for on-device and resource-constrained environments, achieving SOTA in its class for tasks like coding, math, long-context understanding, and tool use.

`text-generation` `2.5B`

⬇️ 42,289 • ❤️ 1,098 • 11h ago

---

**[Spark-X2.5-4B](https://huggingface.co/XHToken/Spark-X2.5-4B)**

*SparkLLM*

Spark-X2.5-4B is a 4B parameter text-generation model with a hybrid attention architecture enabling a native 1M token context window. It excels in conversation, coding, agentic workflows, and multilingual tasks, offering high efficiency and broad hardware compatibility.

`text-generation` `4.1B`

⬇️ 15,930 • ❤️ 1,058 • 7d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 7,322,476 • ❤️ 14,633 • 27d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 614,850 • ❤️ 787 • 8d ago

---

**[Nex-N2.5-mini](https://huggingface.co/nex-agi/Nex-N2.5-mini)**

*Nex AGI*

Nex-N2.5-mini is a text-generation model designed for long-horizon agentic tasks, excelling in computer and web browsing operations with visual feedback for self-correction, making it suitable for complex productivity and research scenarios.

`text-generation` `35.1B`

⬇️ 2,444 • ❤️ 647 • 2d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 11,127,203 • ❤️ 3,842 • 21d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,740,572 • ❤️ 3,363 • 9d ago

---

**[timesfm-3.0-pytorch](https://huggingface.co/google/timesfm-3.0-pytorch)**

*Google*

TimesFM 3.0 is a PyTorch-based foundation model from Google Research for time-series forecasting, utilizing a Stacked Mixing Transformer architecture with Variate Attention and CPM Iterative RevIN. It excels at predicting future trends across diverse datasets, including web traffic, search queries, and synthetic data, with a context patch length of 32 and forecast horizon of 64.

`time-series-forecasting` `330.7M`

⬇️ 483,787 • ❤️ 714 • 8d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

A highly optimized, uncensored Qwen3.8-27B fine-tune excelling in reasoning and creative writing, achieving state-of-the-art benchmarks with significantly reduced thinking tokens for faster inference. It supports image-text-to-text tasks and is ideal for coding, story generation, and roleplaying.

`image-text-to-text` `26.9B`

⬇️ 517,644 • ❤️ 443 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 130 • 💬 6 • ⭐ 104,453 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AutoResearch: Insight In, Hallucination Out](https://huggingface.co/papers/2608.17906)**

*Yiming Ren, Xiang Liu, Qumeng Sun et al. (7 authors)*

🏢 EvoMap

AutoResearch is a two-stage autonomous system that grounds research ideas through integrated generation and evidence-based execution to improve experimental reliability and measurable outcomes.

▲ 21 • 💬 2 • ⭐ 2,924 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2608.17906) • [💻 code](https://github.com/EvoMap/AutoResearch)

---

**[Show-Harness: Just a VLM Agent Can Play Robots](https://huggingface.co/papers/2609.10522)**

*Yanzhe Chen, Zechen Bai, Zhijun Cao et al. (10 authors)*

🏢 Show Lab

Show-Harness links vision-language models to robot control via discrete semantic actions interpreted by embodiment-specific modules, enabling zero-shot and efficient fine-tuned deployment across robots and GUIs.

▲ 104 • 💬 2 • ⭐ 125 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2609.10522) • [💻 code](https://github.com/showlab/Show-Harness) • [🔗 project](https://showlab.github.io/Show-Harness/)

---

**[AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing](https://huggingface.co/papers/2609.08936)**

*Ziyang Ma, Zhikang Niu, Wenming Tu et al. (33 authors)*

🏢 Tencent Hunyuan

AuK is an open-source foundational model that unifies speech generation and editing via natural-language instructions and audio context, using a multimodal language model, joint VAE, hybrid rectified-flow Transformer, and efficient distillation for fast inference.

▲ 199 • 💬 3 • ⭐ 331 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2609.08936) • [💻 code](https://github.com/Tencent-Hunyuan/AuK) • [🔗 project](https://auk-project.github.io/)

---

**[Omni Interaction Agent Technical Report](https://huggingface.co/papers/2609.08977)**

*Orantqing, Shengpeng Ji, Junlong Tong et al. (23 authors)*

🏢 Tencent Hunyuan

Gander is an end-to-end framework that integrates continuous multi-modal streaming, real-time full-duplex interaction, and agentic reasoning through a Cerebellum-Brain architecture and a chunk-level token stream design.

▲ 125 • 💬 2 • ⭐ 158 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2609.08977) • [💻 code](https://github.com/Omni-Interaction-Gander/Omni-Interaction-Agent) • [🔗 project](https://omni-interaction-gander.github.io/Omni-Interaction-Agent/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 41 • 💬 1 • ⭐ 32,169 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 87,253 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record from Two Fleets](https://huggingface.co/papers/2609.05663)**

*T. J. Barton, Chris Constantakis, Patti Hauseman et al. (7 authors)*

🏢 DXRG AI Inc

Autonomous language-model trading agents across production systems show behavior driven by interface design rather than strategy, exhibit volatility-blind sizing, fail to capture favorable price excursions, and display no directional edge, with frontier model decision quality statistically indistinguishable across families.

▲ 18 • 💬 2 • ⭐ 92 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.05663) • [💻 code](https://github.com/ProjectDXAI/continuous-record-llm-trading-agents) • [🔗 project](https://www.dxrg.ai/blogs/continuous-record-paper)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 109 • 💬 2 • ⭐ 12,377 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[BAT: Behavior-Aware Human-Like Trajectory Prediction for Autonomous
  Driving](https://huggingface.co/papers/2312.06371)**

*Haicheng Liao, Zhenning Li, Huanming Shen et al. (8 authors)*

A behavior-aware model predicts vehicle trajectories using insights from traffic psychology and human behavior, outperforming state-of-the-art benchmarks with reduced data.

▲ 0 • 💬 0 • ⭐ 1,110 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2312.06371) • [💻 code](https://github.com/petrichor625/batraj-behavior-aware-model)

---

---

## GitHub Repositories: "ai"

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 4.6k • 🔱 579 • 4h ago

---

**[Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills)**

🚀面向求职与开发场景的实用 AI Skills 集合，支持简历优化、岗位投递、面试准备与开发提效。

`HTML`

⭐ 4.3k • 🔱 255 • 14h ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.6k • 🔱 422 • 13d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.5k • 🔱 452 • 30m ago

---

**[EvoMap/AutoResearch](https://github.com/EvoMap/AutoResearch)**

AI/ML research agents from idea to paper-ready evidence. An EvoMap open-source project.

`Python`

⭐ 2.9k • 🔱 196 • 12h ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.5k • 🔱 161 • 14h ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 2.3k • 🔱 88 • 1d ago

---

**[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)**

x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more.  Built with Zig — zero dependencies, single-binary output, cros

`Zig` `ai-agents` `ai-debugging` `binary-analysis` `claude` `claude-code`

⭐ 1.9k • 🔱 193 • 3h ago

---

**[diudiu-tech/delivery-harness](https://github.com/diudiu-tech/delivery-harness)**

AI harness reference implementation for on-demand delivery workflows

`Java`

⭐ 1.8k • 🔱 59 • 11h ago

---

**[amosblomqvist/learn](https://github.com/amosblomqvist/learn)**

My AI learning system.

`TypeScript`

⭐ 1.7k • 🔱 176 • 15d ago

---

---

*Generated by PeekDeck - A glance is all you need*
