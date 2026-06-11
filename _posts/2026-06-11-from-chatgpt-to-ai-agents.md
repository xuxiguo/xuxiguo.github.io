---
title: "A Brain in a Glass Box: From ChatGPT to AI Agents"
date: 2026-06-11
categories: ["AI Agents", "AI Thoughts"]
description: "ChatGPT could think but could not act. This is the story of how a brain in a glass box grew hands, and why that shift from answering to acting changes how we research and learn."
---

In November 2022, OpenAI released ChatGPT, and within about two months it had reached 100 million users — the fastest adoption of any consumer application in history.<sup>[[1]](#ref1)</sup> I remember the first time I used it for real work. I asked it to write a short Python script to clean a messy dataset, and it produced something elegant in seconds. Then I copied the code into my terminal, ran it, and watched it fail. I pasted the error back into the chat. It apologized, fixed the bug, and handed me new code. I copied that back. It failed again — a different error. Paste, apologize, repeat.

I was doing all the work of being the hands. The intelligence was extraordinary. But it lived behind glass.

That experience — brilliant reasoning trapped behind a wall it could not reach across — is still the best way I know to understand what has happened in AI over the last three years. The headline is not that the models got smarter, though they did. The headline is that the brain grew hands. The chatbot learned to act. And that single shift, from answering to acting, is what people now mean when they say "AI agent."

---

## The Brain in the Glass Box

When you strip away the hype, the original ChatGPT was a brilliant brain locked in a glass box.

It could reason about almost anything. It could write code, draft an essay, explain a proof, summarize a filing. But it could not run the code it wrote. It could not open the file, query the database, check whether its answer was correct, or take a single action in the world. It produced words, and a human had to carry those words across the glass and turn them into action.

I have come to think of it as hiring a world-class consultant who can draw you a beautiful blueprint but cannot pick up a hammer. The blueprint is real value. But if you have to build the entire house yourself, brick by brick, the consultant's genius is bottlenecked by your own two hands.

<figure>
  <img src="/assets/img/blog/agents-fig2-glassbox-vs-agent.png"
       alt="Two-panel diagram. Left: a chatbot drawn as an LLM in a glass box, with a human doing a copy-paste loop. Right: an agent drawn as the same LLM connected directly to tools (run code, browse web, query data) with a feedback loop."
       class="img-fluid" style="max-width:100%; border-radius:4px;">
  <figcaption class="figure-caption text-center mt-2">
    <strong>Figure 1.</strong> The chatbot reasons but cannot act, so a human ferries every answer and error back and forth. The agent is the same brain, now wired directly to tools — it acts, observes the result, and tries again on its own.
  </figcaption>
</figure>

This is not a knock on those early models. It is a description of their shape. A language model, on its own, is a kind of function: text goes in, text comes out. It has no memory beyond the current conversation, no ability to act, and no way to test its work against reality. It is pure cognition with no limbs.

The story of AI agents is the story of giving that cognition limbs — and then teaching it to use them without someone holding its hand at every step.

---

## Three Things the Brain Was Missing

If you want to turn a brain in a box into something that can actually get work done, you have to add three things.

First, it needs to **reason in steps** — not just produce an answer, but plan, try, notice when something goes wrong, and adjust. Second, it needs **tools** — hands that can run code, search the web, query a database, send a message. Third, it needs **memory** — some way to hold onto what it has learned across a long task instead of starting fresh every time.

The remarkable thing about the last three years is that the field added these capabilities almost in that exact order. You can lay the milestones out on a timeline and watch a chatbot slowly grow into an agent.

<figure>
  <img src="/assets/img/blog/agents-fig1-timeline.png"
       alt="A horizontal timeline in three colored eras. The Chatbot (2022-2023): ReAct, ChatGPT, Toolformer. Tool Use (2023): GPT-4 plus plugins, AutoGPT and BabyAGI, function calling. The Agent (2024-2026): computer use, MCP, Operator, Agent Skills, and 2026 as the year of agents."
       class="img-fluid" style="max-width:100%; border-radius:4px;">
  <figcaption class="figure-caption text-center mt-2">
    <strong>Figure 2.</strong> A short history of a fast three years. Each wave added what the last one lacked — first reasoning, then tools, then autonomy. (Spacing is schematic, not to scale.)
  </figcaption>
</figure>

Let me walk through the three turns that matter most.

---

## Turn One: Learning to Reason in Steps

About a month before ChatGPT launched, a group of researchers published a paper with an awkward name and an elegant idea: ReAct, short for "Reasoning and Acting."<sup>[[2]](#ref2)</sup>

Their insight was that language models were being asked to do too much in one leap. Pose a hard question and the model would blurt out an answer in a single shot, like a student guessing on an exam. ReAct interleaved two things instead: a thought ("I need to find X, so first I should look up Y") and an action ("search for Y"), followed by another thought based on what came back. Reason, act, observe. Reason again.

This sounds almost too simple to matter. But it changed the texture of what models could do. A model that reasons in steps can break a big problem into small ones, recover from a wrong turn, and use the result of one action to decide the next. The ReAct paper has since been cited more than eleven thousand times — a fair measure of how foundational the idea turned out to be.<sup>[[2]](#ref2)</sup>

This was the first crack in the glass. The brain learned to think out loud, one step at a time, in a way that left room for action between the steps.

---

## Turn Two: Learning to Use Tools

A thought is only useful if you can act on it. The second turn gave the model hands.

In early 2023, researchers at Meta published Toolformer, which showed that a language model could teach itself *when* to call an external tool — a calculator, a search engine, a calendar — and weave the result back into its answer.<sup>[[3]](#ref3)</sup> At almost the same time, the idea moved from research into products with startling speed. In March 2023, OpenAI added plugins and a code interpreter to ChatGPT, letting it browse the web and run Python.<sup>[[4]](#ref4)</sup> By June, the API offered "function calling," a clean way for developers to hand the model a set of tools and let it decide which to invoke.<sup>[[5]](#ref5)</sup>

This is the moment the consultant picked up the hammer. A model with tools is no longer limited to producing words. It can run the code it just wrote, read the error, and fix it — without a human ferrying text back and forth across the glass. The copy-paste dance I described at the start simply disappears. What used to cost me thirty minutes of pasting now takes an agent thirty seconds, because it is holding both the pen and the hammer.

That spring also produced a burst of wild experiments — AutoGPT, BabyAGI, AgentGPT — that tried to chain these abilities into fully autonomous agents pursuing a goal on their own.<sup>[[6]](#ref6)</sup> Most were more demo than product; they would loop, get confused, and wander off. But they were a genuine glimpse of the direction, and they put the word "agent" into everyone's vocabulary.

---

## The Agent Loop

Put reasoning and tools together and you get something with a recognizable rhythm. Engineers call it the agent loop, and once you see it you cannot unsee it.

<figure>
  <img src="/assets/img/blog/agents-fig3-agent-loop.png"
       alt="A circular diagram with an augmented LLM at the center (memory, tools, retrieval) surrounded by three stages: Think (plan the next step), Act (call a tool), and Observe (read the result), cycling back through a goal check."
       class="img-fluid" style="max-width:78%; display:block; margin:0 auto; border-radius:4px;">
  <figcaption class="figure-caption text-center mt-2">
    <strong>Figure 3.</strong> The agent loop: think, act, observe, and check whether the goal is met. A single research-cleaning task might run this loop dozens of times before it finishes.
  </figcaption>
</figure>

The loop is simple. The agent thinks about what to do next. It acts, by calling a tool. It observes the result. Then it decides whether the goal is met — and if not, it loops again. A data-cleaning task might run that loop fifty times: load the data, notice a column is malformed, write a fix, run it, check the output, find another problem, and so on, until the dataset is clean.

Anthropic, in a widely read 2024 guide, drew a useful line here.<sup>[[7]](#ref7)</sup> They distinguished *workflows*, where a human wires together a fixed sequence of steps in advance, from *agents*, where the model "dynamically directs its own processes and tool usage, maintaining control over how it accomplishes tasks." A workflow follows a recipe you wrote. An agent decides the recipe as it goes. The same guide offered a piece of advice I think about often: start simple, and add agentic complexity only when a simpler approach falls short. The goal is not to build the most autonomous system imaginable. It is to build the simplest one that actually solves your problem.

---

## The Ladder of Autonomy

It helps to see all of this as a ladder rather than a switch. "Agent" is not a single thing you either are or are not; it is a position on a spectrum of how much of the steering wheel you have handed to the machine.

<figure>
  <img src="/assets/img/blog/agents-fig4-autonomy-ladder.png"
       alt="A five-rung ladder. From bottom to top: Chatbot (answers your question), Tool-using assistant (calls one tool when asked), Workflow (runs a fixed recipe), Agent (picks its own steps and tools), Multi-agent system (delegates to a team). Arrows show more autonomy going up and more human control going down."
       class="img-fluid" style="max-width:100%; border-radius:4px;">
  <figcaption class="figure-caption text-center mt-2">
    <strong>Figure 4.</strong> Autonomy is a ladder, not a switch. Each rung hands the machine a little more of the steering wheel — and the right rung depends on the task and how much you trust the machine with it.
  </figcaption>
</figure>

At the bottom is the plain chatbot: it answers, and you do everything else. One rung up is the tool-using assistant, which will call a single tool when you ask. Above that sits the workflow, which runs a multi-step recipe you designed. Higher still is the agent proper, which chooses its own steps and tools to reach a goal you set. And at the top is the multi-agent system, where one agent delegates to a whole team of specialists — the subject I take up in a companion post.

Every rung trades human control for machine autonomy. None of them is the "right" level in the abstract; the right level depends on the task and on how much you trust the machine with it. Cleaning a dataset under your supervision is a very different proposition from letting an agent move money or email a client unsupervised. Knowing where on the ladder you want to stand — and why — is quietly becoming a skill in its own right.

---

## Why This Matters for Research and Learning

I care about this evolution because of what it does to how we work and how we learn.

For research, the move from chatbot to agent is the difference between an assistant that drafts and an assistant that does. An agent can pull a sample from a database, run the regression, format the table, and flag the result that looks wrong — looping through the tedious middle of empirical work that used to eat days. Anthropic's computer use and OpenAI's Operator pushed this further still, letting a model drive a web browser and operate a computer directly.<sup>[[8]](#ref8)</sup><sup>[[9]](#ref9)</sup> The brain now reaches across the glass on its own.

But here I want to be careful, because the same power that makes agents useful makes them risky in a specific way for learning.

When a chatbot hands a student an answer, the student still has to do the work of using it. When an agent does the entire task — pulls the data, writes the code, produces the chart — the student can walk away with a finished result without ever passing through the struggle that builds judgment. I have written before about the apprenticeship problem: we become good at research not by reading answers but by wrestling with messy data, being wrong, and slowly learning why. An agent that removes the struggle can quietly remove the learning along with it.

The answer is not to avoid agents. It is to use them deliberately — to stay on the ladder at the rung where you are still doing the thinking that matters, and to let the machine take the parts that are genuinely mechanical. That is a judgment call, and teaching it well may be one of the more important pedagogical tasks of the next few years.

---

## 2026: The Year the Agents Arrived

For all the progress, agents are still early. Surveys through 2026 show a striking gap between experimentation and production: a large share of organizations report piloting AI agents in some form, but only a minority have actually put them into production at scale.<sup>[[10]](#ref10)</sup> McKinsey's read is similar — plenty of pilots, far fewer deployments that have crossed into everyday operations.<sup>[[11]](#ref11)</sup> The brain has hands now, but it is still learning to use them reliably, and the work of making agents trustworthy is mostly still ahead of us.

I find that genuinely exciting rather than discouraging. We are near the beginning of this, not the end. The tools improve month over month, and the questions of how to use them well — where to put a human in the loop, which tasks to delegate, how to keep an autonomous system honest — are wide open. Those are not questions a model can answer for us. They are ours.

A brain grew hands. What it builds with them is still up to us.

In a companion piece, I want to open up the agent and look at the parts inside — the skills, the connectors, the specialist sub-agents, and the automatic guardrails that turn a raw model into something you can trust with real work. If the story here was how the brain grew hands, the next one is about the scaffolding we build around it.

---

## References

<ol>
  <li id="ref1">Reuters. <a href="https://www.reuters.com/technology/chatgpt-sets-record-fastest-growing-user-base-analyst-note-2023-02-01/" target="_blank">"ChatGPT sets record for fastest-growing user base." February 2023.</a></li>
  <li id="ref2">Yao, S., et al. <a href="https://arxiv.org/abs/2210.03629" target="_blank">"ReAct: Synergizing Reasoning and Acting in Language Models." arXiv:2210.03629, 2022.</a></li>
  <li id="ref3">Schick, T., et al. <a href="https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html" target="_blank">"Toolformer: Language Models Can Teach Themselves to Use Tools." NeurIPS 2023.</a></li>
  <li id="ref4">OpenAI. <a href="https://openai.com/index/chatgpt-plugins/" target="_blank">"ChatGPT plugins." March 2023.</a></li>
  <li id="ref5">OpenAI. <a href="https://openai.com/index/function-calling-and-other-api-updates/" target="_blank">"Function calling and other API updates." June 2023.</a></li>
  <li id="ref6">Significant Gravitas. <a href="https://github.com/Significant-Gravitas/AutoGPT" target="_blank">AutoGPT (and related early autonomous-agent projects such as BabyAGI), 2023.</a></li>
  <li id="ref7">Anthropic. <a href="https://www.anthropic.com/research/building-effective-agents" target="_blank">"Building Effective Agents." December 2024.</a></li>
  <li id="ref8">Anthropic. <a href="https://www.anthropic.com/news/3-5-models-and-computer-use" target="_blank">"Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku." October 2024.</a></li>
  <li id="ref9">OpenAI. <a href="https://openai.com/index/introducing-operator/" target="_blank">"Introducing Operator." January 2025.</a></li>
  <li id="ref10">DigitalApplied. <a href="https://www.digitalapplied.com/blog/agentic-ai-statistics-2026-definitive-collection-150-data-points" target="_blank">"Agentic AI Statistics 2026." (Aggregated industry surveys.)</a></li>
  <li id="ref11">CIO / McKinsey. <a href="https://www.cio.com/article/4107315/agentic-ai-in-2026-more-mixed-than-mainstream.html" target="_blank">"Agentic AI in 2026: More mixed than mainstream." December 2025.</a></li>
</ol>
