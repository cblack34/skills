# How-to guide

A how-to guide gets a competent reader to a goal they already have. They are working, not learning. Usefulness beats completeness.

## Shape

````markdown
# <Task in the reader's words, starting with a verb>

<One sentence on when you need this, only if the title does not make it obvious.>

## Before you begin
- <Required access, versions, or state. Omit the section if there is none.>

## <Optional subheading per phase, for long tasks only>
1. <Condition first, then the action: "To X, run:">
   ```sh
   <command>
   ```
2. <Next action.>

## Verify
<One check that proves it worked, and the expected output.>
````

## Rules

- Start from the reader's goal, not from the tool's features. Title it as the task: "Rotate the API key", not "API key rotation".
- Number the steps. Write one action per step, with the imperative verb first.
- Assume the reader knows the basics. Do not explain how to open a terminal or what Git is.
- Handle real forks with a condition: "If you use Docker, run X. Otherwise, run Y." Keep it to the forks the reader will hit.
- Give exact commands, paths, and values the reader can copy. Mark placeholders as `<like-this>` and say what goes in them.
- End with how to verify success. Add troubleshooting only for failures you know happen, as "If you see `<error>`, do X."

## Leave out

Background, history, why the system works this way, every flag, and alternatives the reader did not ask for. Link to the reference or explanation instead.

Depth: [diataxis.fr/how-to-guides](https://diataxis.fr/how-to-guides/)
