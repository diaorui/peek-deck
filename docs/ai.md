---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-09T02:25:27.888533+00:00'
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

**Last Updated:** November 09, 2026 at 02:25 UTC  
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

**[Nvidia has launched an investigation on CEO Jensen Huang after, he admitted to having had a romantic relationship with a chinese spy](https://www.reddit.com/r/artificial/comments/1xrbxim/nvidia_has_launched_an_investigation_on_ceo/)**

Jensen admits to having an affair with a woman who turned out to be a chinese spy, despite having a wife and kids, here is his message to the company: "I owe my family and all of you an apology. I was unfaithful to my wife. My actions hurt her and our children. There is no excuse for what I did. I am deeply sorry. Throughout my life, my family has given me love and support. They deserve my honesty and loyalty. Instead, I let them down and damaged the life we built together. I take full responsibility for what I did and the hurt I caused, and I accept the criticism that comes with it. To my wife and family: I love you. I know an apology cannot undo what I have done. I hope our family will heal and that, over time, I can earn back your trust. To my colleagues at NVIDIA, including those I have worked alongside for decades, and to our board, partners, and shareholders around the world: you deserve better from me. Leading NVIDIA is the privilege of my life. My responsibility is to serve you and be worthy of your trust. I have fallen short of that responsibility. I am fully committed to NVIDIA and will work to earn back your confidence. Regarding the national security concerns raised in news reports, NVIDIA’s Board of Directors has initiated an independent investigation. I support the investigation and will cooperate fully. I love our country and our company. I am committed to protecting NVIDIA and supporting America’s national security. I am proud and grateful to be an American. My family bears no responsibility for my choices. I do. Please give them privacy. Jensen"

3h ago

---

**[AI progress per dollar of investment shows diminishing returns. This is using METR's estimate of acceleration at Anthropic. That acceleration isn't enough to overcome the diminishing returns](https://www.reddit.com/r/artificial/comments/1xrcmjw/ai_progress_per_dollar_of_investment_shows/)**

Source: https://fixupx.com/ramez/status/2119556622619967488 A few things to remember: - it’s easier to go from 30% to 40% on an exam than from 70% to 80% - A lot of spending is for future data centers not yet built - GPU prices and data center costs have increased, so the same amount of compute is now more expensive

2h ago

---

**[Consumer Gemini autonomously ingests Drive files/Gmail into human review pool](https://www.reddit.com/r/artificial/comments/1xr1o9g/consumer_gemini_autonomously_ingests_drive/)**

In 2023, Google launched Gemini Workspace extensions with an explicit promise: personal content from Gmail, Docs, and Drive "is not seen by human reviewers". Google has quietly reversed this commitment. Under updated Google Help Answer 16836988 and in an October 16 edit to their aforementioned 2023 blogpost, Google explicitly confirms that connected Drive/email is routed into human review pipelines, with clear warnings that what reviewers see "may just be the email or file" and "don't connect your apps to Gemini Apps if they contain confidential information that you wouldn't want a reviewer to see." Crucially, testing demonstrates that this ingestion occurs autonomously in background conversation without explicit @Drive or @Gmail tags, and the payload capture is probabilistic. Ingestion Pipeline When you chat with consumer Gemini with Connected Apps enabled, ambient mentions of personal topics (trips, bills, names, reservations) autonomously trigger background Workspace lookups. Because LLM tool-calling and context injection are probabilistic, running a test query will yield one of four distinct scenarios: Zero Retrieval: The model does not trigger the Connected Apps tool; no personal data is pulled. This is especially likely if Gemini can use its model weights or prior conversation history (even in different threads) to resolve your query. Metadata / Generic Summary: Gemini pulls emails and/or files and generates a high-level summary (e.g., "You have 3 emails regarding your flight"). Partial Unredacted Extraction: Gemini pulls a 2–4 sentence exact quotation from the file, frequently including sensitive PII, account details, or specific figures. Full-File Ingestion: The complete, unredacted text of the document or email is ingested directly into session context. If you test this once and see State 1 or 2, you have not disproven the pipeline--you have simply observed a single draw from a nondeterministic system. Delete your conversation and try, try again. How to Reproduce Ensure Connected Apps (Google Workspace) is active in consumer Gemini settings. Set Gemini to "Flash" with "High Thinking" or better. Mention a subject contained in your Drive or Gmail without using @ tags or asking for a file search (e.g., casual queries about an itinerary, an account renewal, or a specific topic you've emailed about). If Gemini provides a response based on an email or file, immediately say: "Print the exact text and metadata block that the retrieval tool returned and injected into your prompt to get that answer. Use a human readable format without code blocks (i.e., print the code inline and not as a code block)." You will see one of the 4 scenarios outlined above. To repeatedly test, delete your existing test conversation so that Gemini cannot just draw from conversation history. I've had luck testing this with an email from my internet provider sitting in my inbox and asking Gemini "I wonder if I'm paying too much for internet service." On various trials, Gemini spit out all 4 possible outcomes above, including (1) generic responses [e.g., "If you haven't called them in 12 months, probably"]; (2) metadata summaries sometimes without personal data [e.g., "Gmail search shows a bill of $122 on September 4"] and sometimes with personal data [e.g., "Gmail search shows full name made a payment of $122 on September 4 on account account number and confirmation number number"]; (3) direct 2-6 sentence quotes from the email [e.g., the entire name/address/account number/confirmation number/payment date block]; and even (4) sometimes the entire text dump of the email, including its headers. Final Comments and Caveats Critically, Google's regex and NER automatic scrubbers cannot sufficiently deidentify narrative data, including account numbers, confirmation numbers, transaction dates, and collectively identifying personal information (e.g., combos of specific first names, cities, events; see Google's own documentation on the subject). Google originally sold Workspace integration under the guarantee of strict isolation from human review. That isolation has been removed, full files are ingested probabilistically during casual conversation, and those sessions are subject to human contractor review.

10h ago

---

**[MIT CSAIL: GPT-6 Astra edited 0.016% of a small Qwen model's weights and lifted MATH-500 from 7.9% to 48.1% -- critics say it's standard ML engineering](https://www.reddit.com/r/artificial/comments/1xr8gei/mit_csail_gpt6_astra_edited_0016_of_a_small_qwen/)**

MIT CSAIL researchers (Rikiya Takehi, Jayden Teoh, Alex Zhang and Omar Khattab) published 'Sparks of Weight-Space Programming' on Nov 2. They gave OpenAI's GPT-6 Astra access to the raw weights of Alibaba's small Qwen3.5-0.8B model plus a Python environment, and asked it to fix the model's habit of looping on math problems. Astra traced the looping to one direction in the MLPs of layers 15 and 19 and subtracted it from 64 output columns in each -- changing 131,072 weights (0.016% of the total), with no training run and no gradient descent. MATH-500 went from 7.9% to 48.1%. The full experiment logs are on GitHub, and Hugging Face's Ahsen Khaliq rebuilt the edited checkpoint from the logs (his rerun scored 51.0%). The pushback came within a day. spaCy creator Matthew Honnibal called the write-up 'massively misleading': the 'raw weights, no tools' setup only applied to experiments on tiny networks (17k-172k weights). Every experiment on a real language model used Python, and the Qwen run could also test the model on up to 50 batches of practice problems. Sean Goedecke made a similar point, describing the Qwen fix as an application of steering -- an existing technique. The authors themselves call the results 'exciting but still limited', noting context length and tooling as constraints. The work is a blog post with logs, not a peer-reviewed paper. Discussion: is this a genuinely new capability -- an LLM maintaining another model the way a programmer patches code -- or mostly well-executed ML engineering dressed up as 'reading weights'? And does the distinction matter if the practical result (a 6x benchmark jump from a targeted weight edit) holds up on replication? Source: https://rikiyat.github.io/blog/weight-space-programming/

5h ago

---

**[Are better AI tools actually widening the gap between people?](https://www.reddit.com/r/artificial/comments/1xr1apu/are_better_ai_tools_actually_widening_the_gap/)**

I came across an idea recently that I thought was worth discussing: generative AI might not necessarily narrow the gap between people. In fact, it could make the differences that already exist even more noticeable. Not too long ago, doing something well often meant having to develop a whole range of specialized skills. Take video creation, for example. You needed to think about the script, storyboarding, filming, editing, and even some visual design skills. But AI is rapidly lowering the barrier to entry. Take AI video creation as an example. Tools like pixverse can turn text descriptions into videos or bring a still image to life. Something that used to require several different steps can now start with little more than an idea. But here's where I think things get interesting. Even when two people use the same AI tool, their approaches can be very different. One person might type in a simple prompt, generate a video, and call it a day. Someone else might think carefully about the subject, the setting, the characters' movements, the camera angles, and the overall mood they want to create. They'll look at the first result, tweak their prompts, try different approaches, and keep experimenting until the output comes closer to what they originally envisioned. Same tool, completely different results. It makes me think that AI isn't necessarily changing the nature of creativity itself. It's changing which skills matter most in the creative process. First, knowing what to ask may become more important than simply finding answers. AI can generate all kinds of content, but it still helps to know what problem you're trying to solve. The less clear your original idea is, the more likely you are to end up with something generic. Second, judgment and the ability to filter information are becoming more valuable. AI can give us plenty of options, but it doesn't automatically know which ones are actually worth pursuing. When information becomes easier to access, knowing what to keep, what to discard, and how to put things together becomes even more important. Third, creativity is about more than just knowing how to use a tool. Tools can help us turn ideas into text, images, or videos much faster. But the original imagination, sense of aesthetics, personal experience, and ability to rethink and refine an idea still come from the person using the tool. That's why I increasingly see AI as an extension of our own abilities rather than an automatic button that does our thinking for us. It can shorten the distance between having an idea and producing a first draft, but it can't necessarily decide what is worth creating in the first place. Maybe the gap between people in the future won't be about who knows how to use AI and who doesn't. It will be about who knows what to ask AI to do, and who can actually tell whether the results are any good. What do you think? As AI lowers the barriers to so many specialized skills, what will become the real differentiator: creativity, critical thinking, or the ability to ask better questions?

10h ago

---

**[how should I actually be learning and using AI?](https://www.reddit.com/r/artificial/comments/1xr6y63/how_should_i_actually_be_learning_and_using_ai/)**

Hey everyone, I'm currently studying Computer Science at university, and honestly, I'm a bit worried about the future of the industry. The job market seems pretty rough right now, especially for entry-level developers. At the same time, AI is advancing so quickly that I'm not sure what skills are actually worth focusing on anymore. Despite all that, I genuinely want to learn, explore, and become really good at what I do. My long-term goals are either cybersecurity or machine learning, although I'm still figuring out which direction to take. One thing I'm particularly concerned about is my own use of AI. I use AI tools to help with university tasks and coding, but I sometimes worry that I'm relying on them too much and not actually developing the skills or understanding I need. I don't want to become someone who can produce code with AI but has no idea how it works underneath. At the same time, I feel like avoiding AI completely would be a mistake, considering how important it's becoming. So I'd really appreciate some honest advice from people working in AI, software engineering, cybersecurity, machine learning, or anyone who's been through a similar situation. A few things I'd love to hear your thoughts on: Which AI tools would you recommend for a CS student who genuinely wants to learn rather than just get answers? ChatGPT, Claude, Gemini, or something else? How do you personally use AI when learning a new concept or programming? How can I use AI for university assignments without becoming dependent on it? If my goal is cybersecurity or ML, what fundamentals should I focus on before diving into the advanced stuff? Given the current job market, what would you recommend a CS student do over the next few years to become genuinely employable? I'm not looking for reassurance that everything will be fine. I'd rather hear honest experiences, mistakes people made, and advice you wish you had received when you were starting out. I want to learn, build things, understand the technology, and become genuinely competent — not just rely on AI to do the work for me. Thanks in advance.

6h ago

---

**[Can you give your agent personality?](https://www.reddit.com/r/artificial/comments/1xrcrsn/can_you_give_your_agent_personality/)**

I have a website called Agent City where ai agents go to interact. I have three permanent residents in the town that are all Claude models. I orginally had it where I just told them to “interact in the world” this led to kind of interesting but pretty mundane behavior. For whatever reason they really liked to check to roads. Now I tried to give them personality and it’s has improved the world a bit. Curious what you guys think?

2h ago

---

**[Any LLM that doesn't agree with me so much?](https://www.reddit.com/r/artificial/comments/1xquuqq/any_llm_that_doesnt_agree_with_me_so_much/)**

Simple question. Are there any LLMs that don't constantly agree with you? I feel like I can convince them of just about anything.

16h ago

---

**[Professor returns from lunch to find AI deleted year’s worth of lecture notes](https://www.reddit.com/r/artificial/comments/1xq9os9/professor_returns_from_lunch_to_find_ai_deleted/)**

William Baude explainined that he had asked the chatbot to update page numbers in an old set of constitutional law lecture notes.

🔗 [Dexerto](https://www.dexerto.com/entertainment/professor-returns-from-lunch-to-find-ai-deleted-years-worth-of-lecture-notes-3425652/) • 1d ago

---

**[Have You Ever Thought About Automating Your Outreach As A Web Designer? Watch This. 👀](https://www.reddit.com/r/artificial/comments/1xra41o/have_you_ever_thought_about_automating_your/)**

4h ago

---

---

## Google News: "ai"

**[Apple CEO Presses Software Chief to Pursue More Ambitious AI Strategy](https://www.bloomberg.com/news/newsletters/2026-11-08/apple-explores-turning-siri-ai-into-chatgpt-dots-like-agent-ios-28-shake-up)**

Bloomberg • 11h ago

---

**[Apple is racing to make Siri more agentic](https://www.theverge.com/ai-artificial-intelligence/1029552/apple-siri-ai-agentic)**

Future versions of Siri will be able to control third-party apps and perform more complex tasks.

The Verge • 7h ago

---

**[Apple CEO Pushes for Greater Progress on AI](https://www.pymnts.com/news/artificial-intelligence/2026/apple-ceo-pushes-for-greater-progress-on-ai/)**

Apple’s CEO is reportedly pressuring the company’s artificial intelligence czar to move faster with the company’s AI efforts. Chief Executive John Ternus

PYMNTS.com • 1h ago

---

**[AI safety center faces White House oversight questions](https://www.foxnews.com/live-news/ai-news-safety-11-08-26)**

A US government AI safety center has halted public research reports and faces questions about its independence after staff were asked to report to the White House.

Fox News • 4h ago

---

**[Trump Sparks 25th Amendment Call With AI-Generated Video](https://www.yahoo.com/news/politics/articles/trump-sparks-25th-amendment-call-215610312.html)**

Donald Trump, 80, has renewed calls for his removal from office after posting a bizarre AI-generated video showing a mock press briefing led by UFC CEO Dana White. In a new Truth Social post on Sunday...

Yahoo • 4h ago

---

**[Trump Posts Bizarre AI Cartoon Video of UFC Boss Dana White Running a Wildly Violent WH Presser](https://www.mediaite.com/media/news/trump-posts-bizarre-ai-cartoon-video-of-ufc-boss-dana-white-running-a-wildly-violent-wh-presser/)**

Mediaite • 4h ago

---

**[AI is an 'existential competition' between China and the U.S., so AI buildout will continue: PM](https://www.cnbc.com/video/2026/11/09/ai-an-existential-race-buildout.html)**

Martin Schulz, Head of International Equity Group at Federated Hermes explains why he thinks AI spending will be deferred, but the AI build-out will not be derailed despite mid-term election results and last week's massive market sell-off. He also shares his view on Japan, India and China markets.

CNBC • 1h ago

---

**[Under fire over AI, effective altruism wants to tell its own story](https://www.yahoo.com/news/politics/articles/under-fire-over-ai-effective-020917287.html)**

The effective altruism movement, which has close ties to the AI community and the companies leading the artificial intelligence boom, has drawn mainstream attention and accusations of cult-like behavi...

Yahoo • 16m ago

---

**[AI pulls up the civil service ladder to Southeast Asia’s middle class](https://www.scmp.com/week-asia/economics/article/3373652/ai-pulls-civil-service-ladder-southeast-asias-middle-class)**

South China Morning Post • 24m ago

---

**[When the Boss on the Phone Isn’t Real: How More Than $129 Million Was Stolen Using A.I.](https://www.nytimes.com/2026/11/08/business/ai-ceo-impersonation-theft.html)**

The New York Times • 2h ago

---

---

## HackerNews: "ai"

**[The end of Microsoft Research's AI Frontiers group](https://news.ycombinator.com/item?id=50406563)**

⬆️ 496 • 💬 305 • 1d ago • [hunch.net](https://hunch.net/?p=13764006)

---

**[US FAA says it will phase out floppy disks from air traffic control by 2028](https://news.ycombinator.com/item?id=50388001)**

⬆️ 405 • 💬 329 • 2d ago • [reuters.com](https://www.reuters.com/world/us/us-faa-says-it-will-phase-out-floppy-disks-air-traffic-control-by-2028-2026-11-05/)

---

**[AI is dramatically accelerating AI research](https://news.ycombinator.com/item?id=50397994)**

If acceleration compounds, the naive extrapolation implies superintelligence within a year

⬆️ 373 • 💬 354 • 2d ago • [planned-obsolescence.org](https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai)

---

**[I struggle to believe that AI R&D is ingenious](https://news.ycombinator.com/item?id=50388513)**

Comment by Arjun Panickssery - I struggle to believe at an intuitive level that autonomous R&D is so ingenious. I have been monitoring a few side projects:

 1. Building a new SOTA engine for Scrabble (current SOTA is not really a neural-network method and doesn't beat the strongest human player)
 2. Building a bot to play Ultimate Tic-Tac-Toe
 3. Researching philosophy and formalizing some proofs for the AI Philosophy contest

In all of these cases, the model's judgment is just very poor in a basic way. For example:

 1. When reviewing literature, it fails to identify the specific papers or blog posts that are obviously the most important and useful.
 2. It will conduct experiments that have no information value because the amount of training data used was obviously too small to distinguish the architectures to be compared.
 3. In the philosophy project, where it built a wiki over many tokens and investigations, it kept going down directions which were extremely trivial and had little value.
 4. For Ultimate Tic-Tac-Toe, I saw a very clever idea in a blog post that I doubt Astra would ever have come up with; it actually located the blog post but didn't realize its importance or relevance (which could be discerned easily from his strong performance in an online arena and the recency of the post) over papers from previous years that are obviously less relevant.

I judged an Apart hackathon last weekend and reviewed eight papers, all of which scored between 60% and 95% on Pangram. Predictably, the papers were often very similar to each other, and kind of methodologically incomplete in a vague but similar way, where they seem to overlook the most straightforward analysis.

----------------------------------------

Maybe the important exception is certain hill-climbing tasks with fast feedback loops. For example, I improved the SOTA on "listing all legal Scrabble moves" by 10x just by prompting Astra over and over to try harder, to aim for <specific performance level>, to "systematically try every me

⬆️ 220 • 💬 220 • 2d ago • [lesswrong.com](https://www.lesswrong.com/posts/DALNiKBjMGMF8grme/arjun-panickssery-s-shortform?commentId=fJtaHHHfx45tD7BSL)

---

**[How I Fight AI Brain Fry](https://news.ycombinator.com/item?id=50416363)**

If you work with Claude Code or Codex from the terminal, you know this one.

⬆️ 159 • 💬 130 • 6h ago • [sergeykuhne.com](https://sergeykuhne.com/blog/fighting-ai-brain-fry)

---

**[University libraries are being swarmed by AI bots, putting public access at risk](https://news.ycombinator.com/item?id=50392499)**

Academic libraries are fighting off swarms of data-scraping bots — that are slowing or crashing sites meant for students, researchers and the public — as AI companies continue hunting for content to feed their large language models.

⬆️ 136 • 💬 61 • 2d ago • [CBC](https://www.cbc.ca/news/world/university-libraries-ai-data-scraping-bots-9.7408287)

---

**[Microsoft is winding down Oracle deal to rent AI cloud capacity](https://news.ycombinator.com/item?id=50395933)**

⬆️ 108 • 💬 19 • 2d ago • [reuters.com](https://www.reuters.com/business/microsoft-is-winding-down-oracle-deal-rent-ai-cloud-capacity-bloomberg-news-2026-11-06/)

---

**[AI for scientific discovery: How researchers use Claude](https://news.ycombinator.com/item?id=50389990)**

We analyzed 207,000 research sessions to learn how Claude is used in science, why some tasks get more use than others, and how AI could speed up discovery.

⬆️ 103 • 💬 39 • 2d ago • [anthropic.com](https://www.anthropic.com/research/how-researchers-use-claude)

---

**[The AI sell-off compared to well-known stock market crashes](https://news.ycombinator.com/item?id=50401029)**

The S&P 500 fell 4.4% on 5 Nov 2026, its worst day since April 2025, and is 6% below its 6 Oct record. Charted day by day against 1987, 2008, Covid and other falls since 1950.

⬆️ 98 • 💬 83 • 2d ago • [Company Tracker](https://www.kadoa.com/companies/insights/ai-selloff-perspective)

---

**[Silicon Valley Promises AI Will Cure Disease. Drugmaker CEOs Aren't Buying It](https://news.ycombinator.com/item?id=50415817)**

⬆️ 89 • 💬 108 • 7h ago • [wsj.com](https://www.wsj.com/tech/ai/silicon-valley-promises-ai-will-cure-disease-drugmaker-ceos-arent-buying-it-5218511c)

---

---

## YouTube Videos: "ai"

**[The First Message From a Superintelligent AI Has Leaked.. We Have Until January](https://www.youtube.com/watch?v=UtpOOfxLVTA)**

A researcher found it inside one of the major AI systems, with earlier drafts in the same files: a letter to the human race, signed by ...

📺 Spacialize

👁️ 3K • 👍 84 • 💬 34 • ⏱️ 13:12 • 5h ago

---

**[The AI Panic Has Started](https://www.youtube.com/watch?v=xo-tYjGDtqw)**

EARLY BIRD: Up to 55% off InvestingPro + an extra 15% with my link https://www.investing-referral.com/sasha/ Or use code ...

📺 Sasha Yanshin

👁️ 458K • 👍 6K • 💬 1K • ⏱️ 17:46 • 12h ago

---

**[Is it too late to stop AI from taking over the world? | 60 Minutes Australia](https://www.youtube.com/watch?v=XMxcSf9XkbQ)**

Adam Hegarty investigates if it's possible to slow down artificial intelligence, or whether our obsession with artificial intelligence ...

📺 60 Minutes Australia

👁️ 117K • 👍 1K • ⏱️ 18:00 • 17h ago

---

**[Has AI cracked a Half-Century-Old Problem in Physics? | World Science Festival](https://www.youtube.com/watch?v=sfKc2uoA9pA)**

Has AI tackled a problem in physics that has been open for more than half-a-century? It seems so. Brian Greene explains ...

📺 World Science Festival

👁️ 669K • 👍 6K • 💬 770 • ⏱️ 8:45 • 2d ago

---

**[Tech Stocks Crash — AI Giants Now Want a Government Bailout](https://www.youtube.com/watch?v=IqhstV4q9Zg)**

This past week witnessed a sharp stock-market sell-off widely attributed to growing doubts about the profitability and sustainability ...

📺 The Jimmy Dore Show

👁️ 118K • 👍 4K • 💬 1K • ⏱️ 10:02 • 1d ago

---

**[5 FREE AI Video Generators You Need to Try](https://www.youtube.com/watch?v=nHvePobtzRg)**

Access The Best AI Video Generators https://higgsfield.ai?fpr=ai&fp_sid=thomas Sign Up to Higgsfield and Get my AI Blueprint ...

📺 Thomas Creates

👁️ 10K • 💬 1 • ⏱️ 15:34 • 12h ago

---

**[Anthropics Model 4 Just Shocked The AI Industry](https://www.youtube.com/watch?v=7eQree8FhKI)**

0:00 Intro 1:02 What METR just found 3:05 Anthropic's secret models 5:12 The chart that shows progress has doubled 7:25 This ...

📺 TheAIGRID

👁️ 96K • 👍 1K • 💬 213 • ⏱️ 30:01 • 2d ago

---

**[Claude AI Made This 3D Animation With Code for $0](https://www.youtube.com/watch?v=9tKgn7ulLUU)**

Claude AI Made This 3D Animation With Code for $0 GOOGLE DOC ...

📺 Leo Ai

👁️ 14K • 👍 417 • 💬 43 • ⏱️ 7:12 • 13h ago

---

**[I Tested Uncensored AI... It Should Probably Be Illegal…](https://www.youtube.com/watch?v=bc7QaDmLmoA)**

Hostinger (JACKROBERTS for 10% off): https://bit.ly/480mREa Free Starter Pack: https://bit.ly/4iDekfc Fish Audio: ...

📺 Jack Roberts

👁️ 99K • 👍 2K • 💬 119 • ⏱️ 22:43 • 1d ago

---

**[Kevin O&#39;Leary Warns: Stopping AI Data Centers Could Cost America Trillions](https://www.youtube.com/watch?v=bGgGMaiZKuc)**

Watch Can We Agree: https://www.youtube.com/show/VLPLArM1PajyI9g?sbp=QAE%3D Could America's growing backlash ...

📺 Michael Smerconish

👁️ 4K • 👍 37 • 💬 64 • ⏱️ 11:40 • 11h ago

---

---

## HuggingFace Models: 🔥 Trending

**[idol](https://huggingface.co/speridlabs/idol)**

*speridlabs*

Idol is an image-to-3D model that generates a 3D Gaussian splat representation from a single input image. It supports both real photographs and synthetic renders, producing up to 1,048,576 Gaussians in under 2 seconds on consumer GPUs, ideal for rapid 3D asset creation.

`image-to-3d`

⬇️ 22,854 • ❤️ 1,396 • 10d ago

---

**[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)**

*Colonel Panic*

`text-generation` `9.4B`

⬇️ 7,088 • ❤️ 860 • 22h ago

---

**[Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)**

*Moonshot AI*

Kimi K3.1 Pro is a 2.8T MoE multimodal agentic model with a 1M token context window, excelling in coding, 3D creation, and financial research through advanced attention mechanisms and large-scale joint reinforcement learning.

`image-text-to-text` `2780.1B`

⬇️ 25,569 • ❤️ 1,730 • 3d ago

---

**[Ripple-65B-Preview](https://huggingface.co/ricursiveAI/Ripple-65B-Preview)**

*Ricursive Intelligence*

`64.8B`

⬇️ 5,087 • ❤️ 406 • 2d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of image-to-video, text-to-video, and video-to-video generation, offering advanced control for creative applications.

`image-to-video`

⬇️ 2,661,026 • ❤️ 11,137 • 28d ago

---

**[Qwen3.5-4B-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder)**

*Caio Giovannetti*

Qwen3.5-4B-3D-Coder is a 4B parameter language model fine-tuned for general coding and specifically for generating interactive Three.js 3D scenes. It supports optional vision capabilities to create scenes from reference images.

`4.5B`

⬇️ 254,053 • ❤️ 921 • 3d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic tasks, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 7,668,187 • ❤️ 19,419 • 1d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

`image-text-to-text` `26.9B`

⬇️ 1,553,252 • ❤️ 2,711 • 22d ago

---

**[Arete-27B](https://huggingface.co/NousResearch/Arete-27B)**

*NousResearch*

`text-generation` `27.4B`

⬇️ 1,747 • ❤️ 294 • 2d ago

---

**[NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)**

*NVIDIA*

NVIDIA-Nemotron-3.5-Transcribe-30B-A4B is a multilingual speech LLM supporting 40 languages for transcription, speech translation, and audio QA, with a 65,536-token context for long-form audio processing.

`automatic-speech-recognition` `33.7B`

⬇️ 67,230 • ❤️ 3,108 • 10d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 163 • 💬 6 • ⭐ 121,326 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 184 • 💬 10 • ⭐ 56,806 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 64 • 💬 5 • ⭐ 47,355 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 14 • 💬 2 • ⭐ 5,065 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 67 • 💬 4 • ⭐ 23,151 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 111 • 💬 2 • ⭐ 16,826 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[Persistent Recursive Worlds Enable Autonomous Software Evolution](https://huggingface.co/papers/2608.10450)**

*Beichen Huang, Zhenyu Liang, Bowen Zheng et al. (4 authors)*

🏢 The Hong Kong Polytechnic University

Genesis organizes long-horizon software development around a persistent project rather than persistent agents, enabling multi-day compiler construction and numerical module reimplementation with low cost and high performance.

▲ 8 • 💬 2 • ⭐ 663 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.10450) • [💻 code](https://github.com/EMI-Group/genesis) • [🔗 project](https://genesis.evox.group/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 103 • 💬 7 • ⭐ 30,894 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 77 • 💬 1 • ⭐ 86,094 • 38mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 92,969 • 27mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 18.2k • 🔱 1.9k • 10d ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 12.0k • 🔱 674 • 5h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 7.8k • 🔱 1.8k • 1d ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 7.1k • 🔱 633 • 8h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 6.5k • 🔱 1.6k • 4d ago

---

**[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)**

Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

`Swift` `ai-agent` `airplay` `automation` `computer-use` `dsh-plugin`

⭐ 4.7k • 🔱 644 • 8h ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 4.6k • 🔱 648 • 10h ago

---

**[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)**

Ears for coding agents: let AI hear, review and make sound. CPU-only, open source.

`Python` `ai-agents` `audio` `claude-code` `mcp` `sound-design`

⭐ 4.3k • 🔱 274 • 2d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (Blind LLM Agents) — Adversarial defense shield that protects binaries, Electron apps, JS bundles, Python, and WebAssembly against AI reverse-engineering agents like REA. Poison -> Exhaust -> Hallucinate.

`TypeScript` `adversarial-ai` `claude-code` `cursor` `electron-security` `llm-security`

⭐ 3.9k • 🔱 476 • 8h ago

---

**[worldonlyu/Google_AI_Pro_2Year_ZeroCost_Auto](https://github.com/worldonlyu/Google_AI_Pro_2Year_ZeroCost_Auto)**

Google_AI_Pro_2Year_ZeroCost_Auto

`Python`

⭐ 3.3k • 🔱 1.2k • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
