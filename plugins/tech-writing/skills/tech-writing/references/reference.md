# Reference

Reference is for lookup. The reader knows what they want and needs the fact fast. Describe, and only describe.

## Shape

Mirror the structure of the thing you document: one section per command, endpoint, resource, or config block, in the order the product uses. Give every entry the same pattern.

````markdown
## `<name>`

<One sentence: what it is or does.>

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `<field>` | `<type>` | `<default>` | <What it controls. Allowed values and limits.> |

**Errors:** `<code>`: <when it happens>.

**Example:**
```<lang>
<smallest example that shows usage>
```
````

## Rules

- State facts: names, types, defaults, allowed values, limits, side effects, errors, and version availability.
- Take the facts from the code, schema, or `--help` output, not from memory. Mark anything you could not verify.
- Use the same pattern, order, and terms in every entry, so the reader can scan.
- Use tables for fields with the same attributes. Use prose only for behavior a table cannot hold.
- Give one short example per entry when usage is not obvious from the signature.
- Write a warning only where misuse causes data loss, a security problem, or an outage.

## Leave out

Instructions, tutorials, design rationale, opinions, and recommendations. Link to the how-to guide or explanation instead.

Depth: [diataxis.fr/reference](https://diataxis.fr/reference/)
