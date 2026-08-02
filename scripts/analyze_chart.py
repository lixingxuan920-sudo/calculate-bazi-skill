#!/usr/bin/env python3
"""Analyze a verified four-pillar chart; this script does not calculate calendars."""

import argparse
import json
import sys

STEMS = "甲乙丙丁戊己庚辛壬癸"
BRANCHES = "子丑寅卯辰巳午未申酉戌亥"
ELEMENT = {
    "甲": "木", "乙": "木", "丙": "火", "丁": "火", "戊": "土",
    "己": "土", "庚": "金", "辛": "金", "壬": "水", "癸": "水",
}
POLARITY = {stem: ("阳" if i % 2 == 0 else "阴") for i, stem in enumerate(STEMS)}
HIDDEN = {
    "子": ["癸"], "丑": ["己", "癸", "辛"], "寅": ["甲", "丙", "戊"],
    "卯": ["乙"], "辰": ["戊", "乙", "癸"], "巳": ["丙", "戊", "庚"],
    "午": ["丁", "己"], "未": ["己", "丁", "乙"], "申": ["庚", "壬", "戊"],
    "酉": ["辛"], "戌": ["戊", "辛", "丁"], "亥": ["壬", "甲"],
}
GENERATES = {"木": "火", "火": "土", "土": "金", "金": "水", "水": "木"}
CONTROLS = {"木": "土", "土": "水", "水": "火", "火": "金", "金": "木"}
SIX_COMBINES = {frozenset(x) for x in ["子丑", "寅亥", "卯戌", "辰酉", "巳申", "午未"]}
CLASHES = {frozenset(x) for x in ["子午", "丑未", "寅申", "卯酉", "辰戌", "巳亥"]}


def ten_god(day, other):
    de, oe = ELEMENT[day], ELEMENT[other]
    same_polarity = POLARITY[day] == POLARITY[other]
    if oe == de:
        return "比肩" if same_polarity else "劫财"
    if GENERATES[de] == oe:
        return "食神" if same_polarity else "伤官"
    if GENERATES[oe] == de:
        return "偏印" if same_polarity else "正印"
    if CONTROLS[de] == oe:
        return "偏财" if same_polarity else "正财"
    if CONTROLS[oe] == de:
        return "七杀" if same_polarity else "正官"
    raise AssertionError("unreachable")


def parse_pillar(text):
    if len(text) != 2 or text[0] not in STEMS or text[1] not in BRANCHES:
        raise argparse.ArgumentTypeError(f"invalid pillar: {text!r}; expected e.g. 壬午")
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pillars", nargs=4, required=True, type=parse_pillar,
                        metavar=("YEAR", "MONTH", "DAY", "HOUR"))
    args = parser.parse_args()
    labels = ["year", "month", "day", "hour"]
    day_stem = args.pillars[2][0]
    counts = {e: 0 for e in "木火土金水"}
    rows = []
    branches = []
    for label, pillar in zip(labels, args.pillars):
        stem, branch = pillar
        branches.append(branch)
        counts[ELEMENT[stem]] += 1
        for hidden in HIDDEN[branch]:
            counts[ELEMENT[hidden]] += 1
        rows.append({
            "position": label, "pillar": pillar,
            "stem_element": ELEMENT[stem],
            "stem_ten_god": "日主" if label == "day" else ten_god(day_stem, stem),
            "hidden_stems": [
                {"stem": h, "element": ELEMENT[h], "ten_god": ten_god(day_stem, h)}
                for h in HIDDEN[branch]
            ],
        })
    relations = []
    for i in range(4):
        for j in range(i + 1, 4):
            pair = frozenset((branches[i], branches[j]))
            if len(pair) == 2 and pair in SIX_COMBINES:
                relations.append({"type": "六合", "positions": [labels[i], labels[j]], "branches": branches[i] + branches[j]})
            if len(pair) == 2 and pair in CLASHES:
                relations.append({"type": "六冲", "positions": [labels[i], labels[j]], "branches": branches[i] + branches[j]})
    print(json.dumps({
        "pillars": rows,
        "raw_element_occurrences": counts,
        "relations": relations,
        "warning": "Raw counts are descriptive only; do not infer strength or useful elements from counts alone."
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
