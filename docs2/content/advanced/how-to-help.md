---
id: advanced.how-to-help
title: "How to Help"
section: advanced
path:
  - "Advanced"
  - "How to Help"
version: "5.1"
status: needs-review
icon: community
summary: "Ways to help Bforartists: test, report, write docs, translate, code and share."
---
Bforartists is free and open source, and it grows with the help of its community. There are many ways to help, with or without coding.

## Ways to help

- **Use it and tell us:** report bugs and suggest improvements (see the pages before this one).
- **Improve this manual:** every page has an **Edit this page** link; fix a typo, add a screenshot or write a missing section.
- **Help others:** answer questions on the Discord.
- **Translate** the interface or the manual.
- **Code:** fixes and features are welcome as pull requests on GitHub. A maintainer can [build your pull request](#ask-for-a-test-build-of-a-pull-request) for testing.
- **Share:** show your art made with Bforartists and tell others about it.
- **Support:** donations help keep the project going.

## Ask for a test build of a pull request

When you send a pull request to Bforartists, a maintainer can build it for you on GitHub, so you and others can check that it compiles and try it, without a local build setup. You ask for a build with a **comment** on the pull request. The comment must start with the word `build`.

> **Note:** Only the owner, members and collaborators of the Bforartists repository can start a build with a comment. If you are a contributor without that role, ask a maintainer to write the comment.

### Build commands

Write the command as a new comment on the pull request. Words are not case sensitive, and you can combine them in any order after `build`. A comment with an unknown word starts nothing.

| Comment | What it does |
| --- | --- |
| `build` | Builds on all three platforms (Windows, Linux and macOS). No report comment is posted. The results show as checks on the pull request. |
| `build all` | Builds on all three platforms and posts a report comment with the results. |
| `build windows` | Builds on one platform only. Use `windows`, `linux` or `macos`. A report comment is posted. |
| `build windows lite` | Builds the **Lite** version, which is the fastest build. Use it for a quick check. |
| `build windows no-report` | Builds without a report comment. |
| `build windows upload` | Packages the build as a zip file and uploads it, so you can download it from the report and try it. |
| `build windows + test_python` | After the build, starts Bforartists once and adds a cube, to check that the Python interface starts without a crash. The report shows the test result. |

You can combine the words, for example `build all lite upload + test_python`. Only one platform name can be in a comment.

### Where to find the result

- The pull request shows a check for each platform, named **Build windows**, **Build linux** and **Build macos**. It is pending while the build runs, then passed or failed.
- With a report, the bot posts a comment with a table of the results. With `upload`, the table has a download link for each zip file.
- You can also start a build by hand: open **Actions** on the repository page on GitHub and run the workflow of a platform.
