# Inform 7 source map

Checked **2026-11-12**. Scope: a reusable agent reference for writing and discussing
Inform; no copied manuals or game corpus. [Core](README.md) · [Scope](scope.md) ·
[Troubleshooting](troubleshooting.md).

## Lookup order and authority

1. Read the compact note or coverage row; reuse its specific destination.
2. For language/library behavior, open the **installed version-matched official
   section**, or its official web counterpart below. For exact built-in behavior,
   inspect the Index and installed Standard Rules. Confirm tricky behavior with
   a minimal compiled example.
3. For explanation/design, use Reed's local index, the Handbook, or the relevant
   RB example. For edge cases use a targeted forum thread, reading corrections.
4. For architecture study one relevant subsystem in a game. Search the wider web
   only when these routes do not resolve the question or version freshness matters.

The compiler pins in [toolchain.json](../../prototype/toolchain.json) are
**Inform 10.1.2 / Inform 6 6.41**. “Inform 7” names the language; 10.1.2 names
this release. **6M62 / 9.3** is an older I7 release, not Inform 6. The Inform 6
Designer's Manual is not the manual for Inform 7.

## Official documentation: local and online

Installed root on this workstation: `C:/Program Files/Inform` (or use
`INFORM_HOME` if configured). These paths were inspected, not inferred:

- `Documentation/doc1.html`: *Writing with Inform* entry; local pages use
  sequential `docNNN.html` names, **not** website `WI_chapter_section.html` names.
- `Documentation/Rdoc1.html`: *Recipe Book* entry.
- `Internal/Extensions/Graham Nelson/Standard Rules.i7x`: action definitions,
  built-in checks, responses, stage ordering, world-model behavior.
- `Internal/Extensions/Graham Nelson/Basic Inform.i7x`: core language-facing phrases.
- `Internal/Inter/`: kits implementing lower-level behavior.
- `Retrospective/`: historical versions; avoid accidentally consulting these
  for the current compiler.

Online: [official documentation hub](https://ganelson.github.io/inform-website/doc/),
[WI contents](https://ganelson.github.io/inform-website/book/WI_1_1.html),
[RB contents](https://ganelson.github.io/inform-website/book/RB_1_1.html).
The hub links example indexes and version history. Online pages can change;
prefer the installed manual for a version dispute.

Under `C:/Program Files/Inform/Documentation/`:

| Question | Local file | Official web section |
|---|---|---|
| Kind/default/property | `doc50.html` | [WI 4.1](https://ganelson.github.io/inform-website/book/WI_4_1.html) |
| Descriptions as queries | `doc80.html` | [WI 6.1](https://ganelson.github.io/inform-website/book/WI_6_1.html) |
| Try/silent actions | `doc99.html` | [WI 7.4](https://ganelson.github.io/inform-website/book/WI_7_4.html) |
| After suppresses reporting | `doc100.html` | [WI 7.5](https://ganelson.github.io/inform-website/book/WI_7_5.html) |
| Scenes | `doc148.html` | [WI 10.1](https://ganelson.github.io/inform-website/book/WI_10_1.html) |
| Action processing / implementation | `doc176.html` / `doc183.html` | [WI 12.2](https://ganelson.github.io/inform-website/book/WI_12_2.html) / [12.9](https://ganelson.github.io/inform-website/book/WI_12_9.html) |
| Rules for NPCs/any actor | `doc185.html` / `doc188.html` | [WI 12.11](https://ganelson.github.io/inform-website/book/WI_12_11.html) / [12.14](https://ganelson.github.io/inform-website/book/WI_12_14.html) |
| Visible/touchable/carried | `doc191.html` | [WI 12.17](https://ganelson.github.io/inform-website/book/WI_12_17.html) |
| Which action rulebook? | `doc195.html` | [WI 12.21](https://ganelson.github.io/inform-website/book/WI_12_21.html) |
| Relations | `doc196.html` | [WI 13.1](https://ganelson.github.io/inform-website/book/WI_13_1.html) |
| Tables | `doc244.html` | [WI 16.1](https://ganelson.github.io/inform-website/book/WI_16_1.html) |
| Grammar / noun names / disambiguation | `doc263.html` / `doc270.html` / `doc281.html` | [WI 17.1](https://ganelson.github.io/inform-website/book/WI_17_1.html) / [17.8](https://ganelson.github.io/inform-website/book/WI_17_8.html) / [17.19](https://ganelson.github.io/inform-website/book/WI_17_19.html) |
| Activities | `doc285.html` | [WI 18.1](https://ganelson.github.io/inform-website/book/WI_18_1.html) |
| Rule ordering / outcomes | `doc330.html` / `doc335.html` | [WI 19.6](https://ganelson.github.io/inform-website/book/WI_19_6.html) / [19.11](https://ganelson.github.io/inform-website/book/WI_19_11.html) |
| Deferred text / snapshot | `doc347.html` | [WI 20.7](https://ganelson.github.io/inform-website/book/WI_20_7.html) |
| Lists / advanced kinds and phrases | `doc350.html` / `doc361.html` | [WI 21.1](https://ganelson.github.io/inform-website/book/WI_21_1.html) / [22.1](https://ganelson.github.io/inform-website/book/WI_22_1.html) |
| Debug commands | `doc388.html` | [WI 24.3](https://ganelson.github.io/inform-website/book/WI_24_3.html) |
| Extensions | `doc426.html` | [WI 27.1](https://ganelson.github.io/inform-website/book/WI_27_1.html) |

Find an unlisted local section without rediscovering the site:

```powershell
rg -l '<title>.*Understanding names' 'C:/Program Files/Inform/Documentation' -g 'doc*.html'
rg -n 'check stage rule|report stage rule' 'C:/Program Files/Inform/Internal/Extensions/Graham Nelson/Standard Rules.i7x'
```

Read the selected HTML as text or through a browser; avoid dumping the whole
manual. If extracting text in Python, follow root `AGENTS.md`'s uv requirements.

## Guides, community, and extensions

| Resource | Use it for / limitation |
|---|---|
| [intfiction.org documentation and resources hub](https://intfiction.org/t/inform-7-documentation-and-resources/3311) | Best discovery map here: manuals, alternative guides, technical references, extensions, source games, organization and testing. Community-maintained; follow its primary links and check versions. |
| [Inform 7 Handbook v3, Jim Aikin](https://inform-7-handbook.readthedocs.io/en/v3.0/) | More expansive explanations; explicitly targets 10.1.2. HTML is marked in construction; its front page links the PDF. |
| [Emily Short's I7 FAQ](https://emshort.blog/how-to-play/writing-if/inform-7/inform-7-faq/) | World modeling, troubleshooting and design questions with further links. Last updated 2011: useful reasoning, historical syntax/ecosystem. |
| [Juhana Leinonen: Structuring Inform 7 code](https://nitku.net/blog/2016/04/structuring-inform-7-code/) | Organizing mechanisms and content; design advice, not a language mandate. |
| [Ryan Veeder's implementation process](https://www.rcveeder.net/blog/2016/08/10/the-imitable-process-of-ryan-veeder/) | Moving from map/details to source organization and narrative voice; one author's approach. |
| [The perils of INSTEAD](https://intfiction.org/t/the-perils-of-instead/51796) | Action-stage pitfalls. **Read post 2's correction** about earlier accessibility checks; the opening post overstates bypassing. |
| [Common mistakes and crutches](https://intfiction.org/t/most-common-mistakes-and-crutches-for-those-starting-out-with-inform-7/55818) | Subtle action/grammar requirements and recurring misconceptions; reproduce claims under the project compiler. |
| [Friends of I7 extensions, 10.1](https://i7.github.io/extensions/) | Compatible extension discovery, source and documentation. Read dependency/version requirements and extension tests before adopting. Older branches are not interchangeable. |
| [Official kits guide](https://ganelson.github.io/inform/inbuild/M-agtk.html) | Boundary between high-level Inform and low-level implementation. Only needed when ordinary I7 hooks are inadequate. |

For a new forum lookup, use a precise query such as
`site:intfiction.org "Inform 7" "carrying requirements"` or the exact rule/error
name plus `10.1.2`. Do not start with generic “Inform tutorial” searches.

**Aaron Reed, locally:** if present, read `references/aaron-reed/topics.md`, then
`index.md`, then selected `pages/pdf-NNN.txt` files. `rg -uuu` includes this ignored
directory. Printed body page N corresponds to PDF N+31; `page-map.csv` resolves
other pages. Extraction loses source tabs and wraps code: it is not compile-ready.
Keep the book/extraction private. The historical
[companion site](https://inform7.textories.com/) was found in search but direct
fetch timed out during this research; do not depend on it. Its indexed 2016 note
recommends legacy 6G60 for following the book, not this project's 10.1.2.

## Game source: choose by the question

These are study destinations, not tested dependencies or endorsements of every
idiom. Read the license before adapting code; source availability alone is not
permission to republish it. Start with a heading or subsystem, not an entire game.

| Source | What to study | Version caveat |
|---|---|---|
| [Blue Lacuna, Aaron A. Reed](https://blue-lacuna.textories.com/source.html) | World setup, compassless/landmark movement, adaptive difficulty and pacing, and semi-random event tables. [Targeted reading routes below](#blue-lacuna-reading-routes). | Source specifies **5Z71** and bundled legacy extensions; CC BY-NC-SA 3.0. Study the mechanisms, then adapt and test under 10.1.2. |
| [Bronze, Emily Short; maintained example port](https://github.com/I7-Examples/Bronze) | A complete world, navigation aids, adaptive hints, and novice-player support. | Repository explicitly says 6M62. |
| [Counterfeit Monkey, Emily Short and contributors](https://github.com/i7/counterfeit-monkey) | Large-system organization: start with `Counterfeit Monkey.inform/Source/story.ni` and follow includes into `.materials/Extensions`; transformation machinery, tables and optimization. | README says 6M62; modified bundled extensions matter. CC BY-SA 4.0 with asset exceptions. |
| [Kerkerkruip, Victor Gijsbers and contributors](https://github.com/i7/kerkerkruip) | Rule-driven simulation/combat and automated testing; inspect `.materials`, `tests`, and `fighttests`. | Historical project with extension dependencies; do not assume a 10.1.2 build. |
| [Andrew Plotkin's game/source index](https://eblong.com/zarf/if.html) | **Advent Window** for a small recent puzzle; **Hadean Lands** for a large puzzle system and automation. The author links source alongside each. | Index/source availability verified; source builds not tested here. Hadean Lands is historical (resource hub lists 6G60). |

### Blue Lacuna reading routes

Start at the [source contents](https://blue-lacuna.textories.com/source/source.html).
Some numbered HTML pages failed to fetch during verification; the
[complete plain text](https://blue-lacuna.textories.com/source/source.txt) worked.
Search within it for the headings/identifiers below; extract only the relevant
section rather than loading the whole game into context.

- **World setup:** Core's world-model extensions (props, setpieces, views), then
  the island's `Setup & Initialization`. Follow the story-mode activation scene
  to see how setup swaps objects and changes puzzle configuration.
- **Nontraditional movement:** the player-command sections for room-name travel
  and `Going by Landmark`; compare keyword destinations, adjacent movement,
  discovered landmarks, and route traversal with ordinary compass actions.
- **Dynamic difficulty and pacing:** [the drama manager](https://blue-lacuna.textories.com/source/source_478.html)
  distinguishes story/puzzle mode from ongoing adaptation. Early behavior informs
  a mode recommendation the player can choose; the boredom meter tracks stalled
  progress and motivates hints, events, and exploration prompts. Follow its
  excitement conditions and the island's story-mode setup for actual consequences.
- **Semi-random events:** Lacuna Ambience's `Ambient Messages`, then regional
  ambience and day/night tables. Inspect `Table of Potential Messages` and
  `fire one off by frequency`: eligibility filters (including time/tide),
  randomized ordering, frequency categories, triggers, and per-turn cleanup.
  Useful pattern: context selects eligible material before randomness selects
  what appears.

These routes were checked against the published source on 2026-11-12; the game
was not compiled here. Treat its historical syntax and library overrides as
version-specific examples.

## Verification

The installed WI sections listed above were located by their actual HTML titles;
action rules, NPC applicability, text substitution, scene recurrence, and debug
commands were read locally. The official online manuals were consulted separately,
along with the linked primary guides and community discussions. Game selection
is based on the authors'/maintainers' pages and the forum resource map, not a
claimed exhaustive source audit.

The original **Tuning Bench** example in [the core](README.md) was compiled with
Inform 10.1.2 / Inform 6 6.41 and played with the project's pinned console Glulxe
on 2026-11-12. Checks covered implicit taking, successful tuning, refusal on
repetition, rejection of a non-instrument, inventory and the resulting tuned
state. Scratch source, compiler logs, and console output are in ignored
`prototype/build/reference-check/`; these are reproducible working artifacts,
not a new chapter-catalog entry.
Future changes should recheck affected behavior and update the date/version;
links and external projects may evolve. Keep the core small and put new specialist
knowledge behind a targeted link rather than expanding the startup reading list.
