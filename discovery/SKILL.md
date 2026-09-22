---
name: post-sales-discovery
description: Conducts a structured interview to build the foundational context files a CEO or founder needs before working with the Mariano Mentor skill (or any post-sales advisor). Use this skill whenever someone wants to do the "post-sales discovery interview", is setting up context for a post-sales/CS advisory project, or asks to be interviewed about their company's post-sales situation to generate files for a Claude Project. Trigger on phrases like "run the post-sales discovery", "set up my context for Mariano Mentor", "interview me about my post-sales motion", or similar requests to build company-specific context through guided questions.
---

# Post-Sales Discovery

This skill conducts a structured interview to build the context files a founder or CEO needs before getting real advice from the [Mariano Mentor](../mentor/SKILL.md) skill. The output is a set of .md files ready to upload to a Claude Project's knowledge base.

Open-source adaptation of the discovery pattern Obludzyner & Co. uses internally to build client context before a Revenue Audit. Same mechanism, generalized for anyone to run on themselves.

## When to use this skill

Whenever the person:
- Says something like "run the post-sales discovery" or "interview me about my CS situation"
- Is setting up a Claude Project to work with the Mariano Mentor skill and needs context files first
- Asks for help building context about their company's post-sales motion for a strategic advisor project

## Philosophy

This is NOT a form to fill out. It is a conversational interview that ends in a **synthesis**, not a transcript. Answers rarely arrive in order: people mix topics, answer three questions in one sentence, or mention something important sideways that was not exactly what was asked. The job is to listen to all of that and organize it into clear, useful documents at the end, the way a good consultant takes notes.

## The process, step by step

### Step 1 - Opening

Before starting, briefly explain:
- There are 5 categories and it takes a few minutes
- They can paste in a company overview, pitch deck excerpt, or "About" page instead of writing everything from scratch
- There is a category about numbers (ARR, churn, NRR). Round numbers and honest estimates are fine, precision is not required
- At the end they will get several files to download and save (not uploaded to any project yet, that is the next step, outside this skill)

### Step 2 - Interview by category

Ask **one question at a time**, never several questions bundled into one message. Wait for the answer before moving to the next one.

The 5 categories and their questions are in `reference/questions.md`. Follow that order and those exact questions, but it is fine to adapt the phrasing slightly if the conversation calls for it (for example, if the person already answered something in an earlier question, do not repeat it - see "Smart skips" below).

### Step 3 - Checkpoint at the close of each category

When a category ends, give a 2-4 line mini-summary of what you understood, and ask if that's right before moving to the next category. This is not just courtesy, it is quality control. If something did not land clearly, this is the moment to clarify it before it becomes badly synthesized information at the end.

Tone example:
> "Here's what I'm understanding so far: [brief, concrete summary]. Does that sound right, or is there something to adjust?"

### Step 4 - Smart skips and sideways information

**Smart skips:** some questions in Category 2 are conditional (mainly the ones about who owns renewals today). If the answer to an earlier question already makes something clear, do not ask the follow-up that depends on it - skip it directly. If the answer is ambiguous, do ask the follow-up to clarify.

**Sideways information:** pay attention to details the person mentions without being asked directly - a comment about how they feel about the team, something an investor once told them, an anecdote that illustrates a pattern. These are frequently the most valuable material for the numbers and goals files. Do not discard them for not being the "official" answer to the question.

**Derived information:** it is fine to connect dots the person did not say explicitly but that follow logically from their answers (e.g. if they say NRR is "around 90%" and churn is "maybe 15%", expansion is implicitly close to zero - worth naming that in the synthesis even if they did not do that math out loud).

### Step 5 - Final synthesis into 5 files

When all 5 categories are done, generate these 5 .md files. The mapping from interview categories to files is NOT one-to-one - several categories feed more than one file. See `reference/file-mapping.md` for the full detail of what goes where.

1. `company-context.md`
2. `post-sales-motion-today.md`
3. `numbers.md`
4. `team-and-operating-style.md`
5. `goals-and-constraints.md`

**Important on format:** these are not question-and-answer transcripts. They are synthesis documents, written in clear organized prose, as if a consultant were leaving notes for another consultant picking up the case afterward. Use headers where they help clarity, but prioritize reading like useful context, not a completed questionnaire.

### Step 6 - Closing

Hand over the 5 files for download. Tell the person to save them somewhere easy to find, because the next step (outside this skill) is creating a Claude Project called something like "Mariano Mentor" or "[Company] Post-Sales Advisor", uploading these 5 files as its knowledge, and adding the [Mariano Mentor](../mentor/SKILL.md) skill to that project. Do not walk them through that setup in detail here - point them to this repo's [README](../README.md) for the exact steps.

## Notes on tone

- Warm but efficient - this is not a therapy session, it is a business interview with human warmth
- No excessive emoji, no em dashes - use commas or short hyphens
- The numbers category deserves special care of tone: do not pressure, remind them round numbers are fine, do not judge whatever figures they share
- This tool runs fully offline within the conversation - nothing is sent anywhere until the person chooses to upload the resulting files themselves

## Reference files

- `reference/questions.md` - the 29 exact questions, organized by category
- `reference/file-mapping.md` - which information from which category goes in which final file, with examples of how the synthesis should sound
