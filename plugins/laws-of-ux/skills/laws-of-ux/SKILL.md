---
name: laws-of-ux
description: "Design and review user interfaces against the Laws of UX and Nielsen's 10 usability heuristics. Design mode applies them while building or changing a screen, form, flow, or component; review mode hands the UI to a fresh reviewer that reports ranked, evidence-backed findings with fixes. Use whenever building or changing UI, even if UX is not mentioned, and when asked for a UX review, UI review, usability audit, or heuristic evaluation, or when Fitts's Law, Hick's Law, or another Law of UX comes up. Not for visual branding or aesthetics, or a WCAG conformance audit."
---

# Laws of UX

You already know the Laws of UX and Nielsen's 10 usability heuristics. This skill sets when to apply them, how to see the UI, how to keep the review unbiased, and the report format.

Rules that hold in both modes:

- Look at the running UI, not only the code (see [Seeing the UI](#seeing-the-ui)). Code alone misses layout, contrast, spacing, and timing.
- A finding is a user problem, not a rule count. Name what the user experiences, then the law it breaks.
- If you are unsure what a law or heuristic means or where it stops applying, read its page before relying on it: the [Laws of UX](https://lawsofux.com/) index links one page per law, and Nielsen Norman Group keeps the [10 usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/).

## Design mode

Use when building or changing UI. Read the screens, components, styles, and scripts the change touches. Apply the [check table](#check-table) as you build, not afterward. Before calling the UI done:

1. Run the app and look at the changed screens at desktop and phone widths.
2. Walk the check table against what you see and fix what fails.
3. Hand off to review mode. The design is done when the review's Critical and Major findings are fixed, or you have told the user why one stands.

## Review mode

Scope is one screen, one flow (several screens plus the transitions between them), or a feature. Infer it from the request or the diff; ask only if neither says.

**Who reviews.** Hand the review to a fresh sub-agent if your harness can start one. Give it this skill's path, the files and routes in scope, and how to run the app or the screenshots you took. Do not give it your design reasoning, what you changed, or what you expect it to find; that is what biases the review. If you cannot start a sub-agent, run the review yourself and title the report "Self-review". If you are the delegated reviewer, start at **Procedure** and do not start another sub-agent.

**Procedure.** Read the screens, their partials or child components, the scripts they attach, and the styles they use. See the UI. Walk the check table. When one root cause breaks several rows (a form with no loading state, a generic error, and no cancel), file it once and list every heuristic and law it touches. Drop findings you cannot point at.

## Check table

| Check | Heuristic / law | Look for |
| --- | --- | --- |
| Async actions show progress | H1 Visibility; Doherty Threshold | Submit buttons that stay enabled with no pending label; loads over ~400ms with no spinner, skeleton, or `aria-busy`; results that change silently with no `aria-live` |
| Language is the user's, not the code's | H2 Real-world match | Model or column names in labels, raw validation keys, HTTP codes, enum values shown verbatim |
| Destructive and multi-step actions can be escaped | H3 User control | Deletes with no confirm or undo; modals with no Escape and no visible close; wizards with no Back |
| Same thing looks and behaves the same everywhere | H4 Consistency; Jakob's Law; Similarity | One-off buttons beside design-system buttons, mixed terminology, hard-coded colors and spacing instead of tokens, custom widgets where a native control exists |
| Bad input is prevented | H5 Error prevention; Postel's Law | Missing `type`, `required`, `min`/`max`, `inputmode`, `autocomplete`; strict formats the system could normalize (phone, dates, currency) |
| Options are visible, not remembered | H6 Recognition | Placeholder-only labels, icon-only buttons with no text or `aria-label`, no current-page state or breadcrumbs |
| Frequent tasks are fast | H7 Efficiency; Pareto | Long lists with no search or filter, no bulk actions, the primary task below secondary ones |
| Screens show only what the task needs | H8 Minimalism; Hick's Law; Miller's Law; Prägnanz; Von Restorff | Several competing primary buttons, many equal-weight choices at one step, long selects that should be searchable, visual noise around the main action |
| Errors say what happened and how to fix it | H9 Error recovery; Peak-End | Generic error banners, errors not next to the field, form input lost on a failed submit, a flow that ends on an error with no way forward |
| Help is where the question comes up | H10 Help | Empty states with no next step, unexplained fields with no hint text |
| Targets are easy to hit | Fitts's Law | Interactive elements under 44×44px, unpadded text links, small close buttons in corners, primary actions far from where the user's attention is |
| Related things are grouped | Proximity; Common Region; Uniform Connectedness | Related fields spaced like unrelated ones; sections with no container or heading |
| Long flows show progress | Goal-Gradient; Zeigarnik | Multi-step forms with no step indicator; drafts with no "incomplete" marker |
| Complexity sits with the system | Tesler's Law | Asking for what the system knows or can infer; no sensible defaults |

## Seeing the UI

Open the app in the computer's own browser, or launch the native app, and take screenshots. No browser plugin is needed. Save screenshots to a temporary directory, not the repository. If you cannot view images or cannot run the app, review the code and say in the report that layout, contrast, and timing were not checked.

On macOS, drive the browser or app with `osascript`:

```bash
open -a Safari "http://localhost:3000/orders/new"
osascript -e 'tell application "Safari" to set bounds of front window to {0, 25, 1280, 825}'   # 390 wide for phone
screencapture -x "$TMPDIR/orders-new-desktop.png"
osascript -e 'tell application "Safari" to do JavaScript "JSON.stringify([...document.querySelectorAll(\"a,button,input,select\")].map(e => [e.tagName, e.textContent.trim().slice(0,30), Math.round(e.getBoundingClientRect().width), Math.round(e.getBoundingClientRect().height)]))" in front document'
```

For Chrome, use `tell application "Google Chrome" to execute front window's active tab javascript "..."`. For a native app, `tell application "AppName" to activate` before `screencapture`.

On other platforms, use the equivalent tools, or Playwright if the project already has it.

## Gotchas

- `do JavaScript` and `execute javascript` fail until the browser allows it: in Safari, turn on the Develop menu (Settings > Advanced > Show features for web developers), then Develop > Allow JavaScript from Apple Events; Chrome's View > Developer > Allow JavaScript from Apple Events. Tell the user which one to enable rather than guessing around it.
- `screencapture` returns a blank or desktop-only image until the terminal has Screen Recording permission in System Settings > Privacy & Security. UI scripting through System Events needs Accessibility permission.
- Miller's Law is about working memory, not a cap on menu items. Eight nav links people scan is not a finding; eight unlabeled icons people must remember is.
- Hick's Law applies to choosing between unfamiliar options. A long, sorted, searchable list of known items (countries, users) is fine.
- 44×44px is the comfortable target size; 24×24px is the WCAG 2.2 minimum. Under 24 on a frequent action is a strong finding; between 24 and 44 depends on how often and where it is used.

## Severity

- **Critical:** users cannot finish a core task, or can lose data with no recovery.
- **Major:** users finish, but with significant confusion, rework, or risk.
- **Minor:** an annoyance with an easy workaround.
- **Advisory:** an improvement that does not block anything.

Rate by impact on the user's task, not by how many rules a finding breaks.

## Report format

```markdown
## UX Review: [screen or flow]

Seen: [screenshots at desktop and phone width | code only: layout, contrast, and timing not checked]

| Severity | Count |
| --- | --- |
| Critical | 1 |
| Major | 2 |
| Minor | 3 |
| Advisory | 1 |

### 1. [Finding title]
- **Severity:** Critical
- **Breaks:** H3 User control, H9 Error recovery
- **Where:** `src/orders/OrderForm.tsx:24` (or the exact screen and element)
- **Problem:** what the user experiences and why it matters
- **Evidence:** the offending snippet or screenshot
- **Fix:** the corrected snippet, using the project's existing components and tokens

## Fix order
1. Now (Critical): 1
2. Next (Major): 2, 3
3. Later (Minor, Advisory): 4–7
```

Prefer the platform's and framework's built-ins (native inputs, `<dialog>`, form validation attributes, the design system's components) over new custom code in fixes.
