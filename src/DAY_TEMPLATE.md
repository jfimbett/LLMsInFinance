# Day Template for LLMs in Finance Course

This template ensures consistency across all days in the course.

## Lecture Template (lecture/index.qmd)

```qmd
---
title: "Day X: [Topic Title]"
author: "Your Name"
date: "2025-05-XX"
format:
  revealjs:
    theme: default
    slide-number: true
    preview-links: auto
    css: ../../styles.css
    logo: ../../images/logo_header.svg
---

# [Main Title]

## Overview of Today's Lecture

- Topic 1
- Topic 2
- Topic 3
- Topic 4

{{< include 01-topic-one.qmd >}}

{{< include 02-topic-two.qmd >}}

{{< include 03-topic-three.qmd >}}

{{< include 04-topic-four.qmd >}}

## What's Next?

- Summary of key concepts
- Preview of practical session
- Preparation for next day
```

## Practical Session Template

### For RevealJS format (practical-session/index.qmd):
```qmd
---
title: "Day X: Practical Session - [Topic]"
author: "Your Name"
date: "2025-05-XX"
format:
  revealjs:
    theme: default
    slide-number: true
    preview-links: auto
    css: ../../styles.css
    logo: ../../images/logo_header.svg
---

# [Practical Session Title]

## Today's Practical Session

{{< include 01-setup.qmd >}}

{{< include 02-exercise-one.qmd >}}

{{< include 03-exercise-two.qmd >}}

{{< include 04-wrap-up.qmd >}}

## Summary

- What we accomplished
- Key takeaways
- Next steps
```

### For HTML format (alternative):
```qmd
---
title: "Day X Practical Session: [Topic]"
author: "Your Name"
date: "2025-05-XX"
format:
  html:
    toc: true
    code-fold: show
    code-tools: true
    highlight-style: github
    css: ../../styles.css
---

# [Practical Session Title]

Content here...
```

## CSS Classes Available

The centralized `../../styles.css` provides these useful classes:

### Content Styling
- `.financial-concept` - Gradient background for key financial concepts
- `.code-exercise` - Dashed border box for coding exercises
- `.instructor-note` - Yellow highlighted instructor notes
- `.key-concept` - Blue highlighted important concepts
- `.alert-info`, `.alert-warning`, `.alert-success`, `.alert-danger` - Bootstrap-style alerts

### Layout
- `.two-columns` - Split content into two columns
- Automatic logo placement in bottom-left corner

### Usage Examples
```qmd
::: {.financial-concept}
A derivative is a financial contract whose value depends on an underlying asset.
:::

::: {.code-exercise}
Exercise: Create a simple sentiment analysis function
:::

::: {.instructor-note}
Remember to explain the difference between training and inference.
:::
```
