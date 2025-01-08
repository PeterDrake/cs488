# CS 488 Software Development
Spring 2025

**Instructor**: [Peter Drake](https://sites.google.com/a/lclark.edu/drake/home)
(includes my [appointment calendar](https://calendar.app.google/XiynwHJNprXgGxWd8))  
**Meetings**: 12:30-3:30 PM Tu/Th, Olin 305  
**Final release party**: 9:30-11:30 AM, Tuesday, May 6

[Course Policies](https://github.com/PeterDrake/drakepedia/blob/master/administrivia/policies.md)  
[Class Notes](https://github.com/PeterDrake/cs488/tree/main/lessons)  
[Pythonorama](https://github.com/alainkaegi/pythonorama/blob/main/README.md)  
[Collaborative Glossary](https://docs.google.com/document/d/1ZEuJ2BPR2Gbh65tMgPfvKOBvWIORiKy-w-4yFI0g1vk/edit?usp=sharing)

You can post questions to the [class email list](25sp-cs-488-01@lclark.edu) 24/7!

**Course texts:**  
Ko, [*Cooperative Software Development*](https://faculty.washington.edu/ajko/books/cooperative-software-development/)
(online)  
Refactoring.Guru, [*Design Patterns*](https://refactoring.guru/design-patterns) (online)  
Roseman, [*TkDocs Tutorial*](https://tkdocs.com/tutorial/index.html) (online)

You will also be expected to seek out and read articles, tutorials, etc. as they become relevant to your project.

## Overview
This course will cover some theory and give you a great deal of practice in developing a large, complex piece of  software as part of a team. We will focus specifically on the eXtreme Programming (XP) technique.

CS 383 Algorithm Design & Analysis is a prerequisite for this course. You are expected to be proficient with the  Python programming language and common data structures and algorithms. There will be a small amount of lecture at the  beginning of each day, but you will spend most of your time in class building software together.

Before launching into the main project, we will spend a few weeks on a small practice project or “spike”: implementing  the dice game *Qwixx* ([rules](https://www.ultraboardgames.com/qwixx/game-rules.php), [scoresheet](https://boardgamegeek.com/file/download_redirect/e183511b21ad0dc4f4fe14cc08d1d9870da8376730d289e9/SingleQwixxScoresheetA4.pdf)).

You will spend the vast majority of the semester working with a team to produce a single large software system. These  are not the contrived projects you've seen in past courses; they are real-world problems for which our "customers" need  software solutions.

## Learning Objectives
Upon completing this course, you should be able to:

- explain and use XP values and practices, including pair programming, refactoring, and test-driven  development.
- use a variety of software development tools, including a source control management system (Git),  a unit testing tool (such as pytest), and a task management tool (GitHib Projects).
- estimate the work required to complete a development task.
- perform incremental object-oriented design using design patterns.
- work with a customer to develop software that meets their needs.
- work with a team on a nontrivial piece of software.
- communicate with your fellow developers, your customer, and outsiders (including me) about the design and progress of your project.

## Course Structure
There will be a short lecture, discussion, or activity at the beginning of each session. (There will be more of this in the first few days.) The rest of your time in class will be spent working with your team on either the practice “spike” project or your main project.

Each project will be broken down into “iterations”; your team will produce a working program at the end of each  iteration. The iterations are one week for the spike and two for the main project:

| Spike: Qwixx | Main Project
|--------------| --
| Jan 28-30    | Feb 18-27
| Feb 4-6      | Mar 4-13
| Feb 11-13    | Mar 18 - Apr 3
|              | Apr 8-17
|              | Apr 22 - May 1
|              | Release party: May 6


Programming will happen in class. Outside of class, there will be a variety of readings, reflections, and conferences. (I've scheduled six hours of class per week to avoid any team scheduling issues. Since you should spend the same total  amount of time on this class as on others, there will be less "homework".)

You are strongly encouraged to keep a journal as you work, so you can remember what you worked on, whom you worked with, what problems you encountered, and how you resolved them. Being able to communicate these things in writing is not busywork but one of the learning objectives of the course!

There are no exams. We will hold a release party during the final exam period.

## Group dynamics
Some of the most valuable lessons you'll learn in this class have nothing to do with Python or Git. They are about working in a team under stress. I can’t claim to be an expert in this area, but I can give some advice, especially in the context of eXtreme Programming.

Remember the XP values: simplicity, communication, feedback, respect, and courage. These are not just about the software but also about our relationships with each other (and the customer). **We must have the courage to address problems by communicating respectfully with each other.**

In a Platonic idealized XP team, all members are at the same level of skill and experience (perhaps with differing areas of expertise). We all know this does not happen in the real world, including in this class. **We must all work to learn what we don't know and teach others what we do.** This is true in the real world and even more so in the classroom (where learning is the highest priority).

**It is not healthy for the team for one pair -- or worse, one person -- to take over part or all of the project.** The  joke is that such people become targets for meteors. Less hyperbolically, it is very easy to imagine a situation where the one person who understands a central class or library is sick and the rest of the team can't do anything that day. Even if it doesn't come to this, everyone is unhappy if one person feels "I did all the work" and another feels "I
never got to do anything".

To avoid this:
- **Make sure everyone is included in all pair or group decisions.** Genuinely listen to what others have to say. Some tips:
  - Don't interrupt.
  - Paraphrase what the other person said or asked. If you don't understand, ask.
  - Be aware of how often different people are speaking. If every other utterance is yours, you may be speaking too often. If you go for an hour without speaking, you're probably not speaking enough.
- **Don't be a hero.** It is good to make a contribution, even an above-average contribution. It is not good to take on a bunch of work because you believe (correctly or otherwise) that you can do it better or faster by yourself. Specifically, **never code alone or outside of class**. Feel free to do research and practice outside of class, but then...
- **The rookie should drive.** When someone doesn't understand a concept, a class, or a design element, they should be doing the typing. Think back to your CS classes. Sometimes the instructor projected code as they wrote it. Sometimes you watched another student or two write code. Sometimes you wrote code yourself. When did you learn the most? I'm betting it's the last one. It's easy to zone out when you're just watching and to ignore your audience when you're doing both the thinking and the typing.
- **Keep up.** If you feel you need more knowledge or practice, get it. I can help with this.

These are challenging issues, especially for those of us who pride ourselves on understanding the formal, unambiguous rules of computing. Working with people is, nonetheless, an important life skill. This class, where the stakes are relatively low, is an excellent opportunity to practice.
