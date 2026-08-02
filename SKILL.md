---
name: calculate-bazi
description: Calculate, verify, and interpret Chinese Four Pillars (BaZi/八字) from birth date, clock time, birthplace, sex, or an existing chart image. Use for 四柱排盘、五行旺衰、十神、藏干、格局、喜忌、大运、流年、合婚, or when checking whether another app's BaZi chart is correct. Treat the result as traditional-culture entertainment, not factual prediction or professional advice.
---

# Calculate BaZi

Produce an auditable chart before interpreting it. Separate deterministic calendar facts from school-dependent judgments.

## Workflow

1. Collect Gregorian birth date, exact local clock time, birthplace, sex, and whether true solar time is desired. Ask only for missing inputs that materially affect the chart.
2. Resolve the birthplace's civil time zone and historical daylight-saving rule. Geocode longitude only when true solar time is requested or the birth is near a two-hour boundary.
3. Calculate the apparent solar-time correction as longitude correction plus equation of time. Show both clock-time and true-solar-time outcomes if the correction changes the hour pillar. Never silently replace civil time.
4. Determine year and month pillars by solar terms: Li Chun changes the BaZi year; the 12 jie boundaries change months. Do not use Lunar New Year or Gregorian month boundaries.
5. Determine day and hour pillars with a tested calendar engine or two independent authoritative calculators. State the Zi-hour convention used when birth falls between 23:00 and 00:59. If no reliable engine is available, do not guess; ask for an app chart or report that exact calculation is unavailable.
6. Run `python3 scripts/analyze_chart.py --pillars YEAR MONTH DAY HOUR` to derive element counts, hidden stems, ten gods, and basic relations from a verified chart.
7. Read [references/interpretation.md](references/interpretation.md) before judging strength, useful elements, structure, luck cycles, annual luck, relationships, health, or compatibility.
8. Read [references/calendar-boundaries.md](references/calendar-boundaries.md) whenever a birth lies near a solar-term, midnight, Zi-hour, time-zone, daylight-saving, or hour-branch boundary.

## Output contract

Give results in this order:

- Input assumptions: calendar, time zone, clock/solar time, sex, and conventions.
- Verified four pillars table: stems, branches, hidden stems, ten gods, and elements.
- Confidence note: identify boundary-sensitive pillars and any conflicting alternatives.
- Interpretation: day-master context, seasonal qi, roots/support/control, balance, then structure and useful-element hypotheses.
- Themes: temperament, study/work, money, relationships, and health tendencies. Use conditional language and practical suggestions.
- Luck cycles or annual years only after confirming cycle direction and start age. Never fabricate exact event dates.

## Guardrails

- Label BaZi as a traditional interpretive system without scientific validation.
- Do not make deterministic claims about death, disease, pregnancy, crime, disaster, wealth, marriage, or another person's hidden intentions.
- Do not diagnose health, direct investments, or replace legal, medical, or mental-health advice.
- Do not infer sex from an image or name. Ask because traditional luck-cycle direction may depend on it.
- Do not declare a useful element from raw element counts alone. Season, roots, combinations, transformations, and climate adjustment matter.
- Distinguish natal chart facts, school conventions, interpretive inference, and speculation explicitly.

## Existing chart images

Transcribe every visible pillar and setting. Compare it with the supplied birth data. Flag discrepancies such as Lunar-New-Year year changes, month changes at the wrong boundary, omitted longitude correction, or a different Zi-hour rule. Use the image as evidence, not proof that the chart is correct.
