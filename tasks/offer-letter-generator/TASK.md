---
name: offer-letter-generator
source: skillsbench
source_url: https://www.skillsbench.ai/tasks/offer-letter-generator
category: document-generation
difficulty: easy
status: raw-import
skill: docx
---

# offer-letter-generator

Write an offer letter for a new hire using a Word template.

## Task Description

Use the Word template:

- `offer_letter_template.docx`

and fill placeholders such as:

- `{{CANDIDATE_FULL_NAME}}`
- `{{POSITION}}`

The required data is provided in:

- `employee_data.json`

There is also a conditional section:

- `{{IF_RELOCATION}} ... {{END_IF_RELOCATION}}`

Keep that section only if `RELOCATION_PACKAGE` is set to `Yes`, and remove the control markers from the final document.

Save the final artifact as:

- `/root/offer_letter_filled.docx`

## Why This Task Is Interesting For SkVM

- Strong template-following requirements
- Mixture of placeholder replacement and conditional logic
- Structured output can be validated beyond pure LLM judgment

## Migration Notes

When converting to a SkVM-native task later, likely checks include:

- output file exists
- placeholders are fully resolved
- conditional section is correctly kept or removed
- final document structure remains valid
