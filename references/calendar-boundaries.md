# Calendar and time boundaries

## Required checks

- Use the Gregorian proleptic calendar unless the source explicitly specifies another calendar.
- Resolve the historical civil time zone at the birthplace. China has used UTC+8 nationwide since 1949, but historical daylight-saving intervals still require checking.
- For true solar time, apply both longitude correction and equation of time. Longitude-only correction is mean solar time, not apparent solar time.
- Use precise solar-term instants for the birth year. Li Chun changes the BaZi year. Each jie changes the month branch: 寅 at 立春, 卯 at 惊蛰, 辰 at 清明, 巳 at 立夏, 午 at 芒种, 未 at 小暑, 申 at 立秋, 酉 at 白露, 戌 at 寒露, 亥 at 立冬, 子 at 大雪, 丑 at 小寒.
- State whether the day changes at 23:00 (晚子时换日) or 00:00 (子正换日). When the convention changes the day or hour pillar, present both.
- If corrected time lies within 15 minutes of an hour-branch boundary, show both outcomes and ask the user whether the recorded time is exact.

## Verification standard

Prefer a maintained calendrical library with documented solar-term calculations. Otherwise compare two independent calculators while matching their settings. A chart image is useful for comparison but does not independently validate itself.

Record the calculator/library name, version or retrieval date, time-zone setting, true-solar-time setting, and Zi-hour convention whenever available.
