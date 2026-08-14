
### Matrix A — the demand

What each genre requires, independent of any tool. Scale 0–3: 0 irrelevant, 1 minor, 2 important, 3 critical. Median of three independent models.

| Consideration | Info brief | Investigation summary | Research proposal | Recommendation | Incident notification | Postmortem | Status update | Decision record | Dissent | Reference docs |
|---|---|---|---|---|---|---|---|---|---|---|
| Precision | +2† | +3† | +3† | +2† | +2† | +3† | +2† | +3† | +3† | +3† |
| Brevity | +2† | +2† | +1† | +2† | +3† | +1† | +3† | +1† | +1† | +1† |
| Scannability | +3† | +2† | +2† | +3† | +3† | +2† | +3† | +2† | +2† | +3† |
| Actionability | 0† | +3† | +3† | +3† | +3† | +2† | +2† | +1† | +1† | +2† |
| Confidence calibration | +2† | +3† | +3† | +2† | +3† | +3† | +2† | +2† | +3† | +2† |
| Empathy | +1† | +2† | +2† | +2† | +3† | +3† | +1† | +1† | +2† | +2† |
| Persuasive force | 0† | +1† | +3† | +3† | +1† | +1† | +1† | +2† | +3† | 0 |
| Accountability | +1† | +3† | +2† | +2† | +2† | +3† | +2† | +3† | +2† | +2† |
| Accessibility | +2† | +2† | +2† | +2† | +3† | +2† | +3† | +2† | +2† | +3† |
| Durability | +2† | +2† | +2† | +2† | +1† | +3† | +1† | +3† | +2† | +3† |

`†` = one model declined to score this cell. `·` = no model scored it.

### Matrix B — the supply

What each technique does to that quality. Scale −2 to +2: +2 serves it strongly, 0 neutral, −2 actively damages it. Median of three independent models.

| Consideration | ASD-STE100 | BLUF/Army | Minto | Amazon memo | ISO 24495-1 | Blameless PM | Toulmin | Hemingway | Hotaling | repo skills |
|---|---|---|---|---|---|---|---|---|---|---|
| Precision | +2 | **+1!** | **+1!** | +1 | **+1!** | **+1!** | +2 | **+1!** | **+2!** | **+2!** |
| Brevity | +2 | +2 | +1 | **+0!** | **+1!** | +0† | **-1!** | +1 | +1 | **+1!** |
| Scannability | **+1!** | +2 | +1 | **0!** | **+1!** | **+1!** | **+1!** | +2 | +1† | **+1!** |
| Actionability | **+1!** | +2 | +1 | **+2!** | **+1!** | **+1!** | +0† | 0† | +2† | +2 |
| Confidence calibration | **+1!** | **+1!** | **+1!** | **+1!** | **+2!** | **+2!** | +2 | **-1!** | **+1!** | **+1!** |
| Empathy | **0!** | **0!** | **+1!** | +1 | **+1!** | **+2!** | +1 | **0!** | **+2!** | **+0!** |
| Persuasive force | -1 | +1 | **+2!** | **+2!** | 0† | -1 | **+1!** | +0† | **+2!** | -1 |
| Accountability | +1 | **+1!** | +2† | **+1!** | +2† | -1 | +1 | **+1!** | +1 | +1 |
| Accessibility | +2 | +1 | +1† | **+1!** | **+2!** | **+1!** | **-1!** | +1 | +1 | **+2!** |
| Durability | +1 | **+1!** | +1 | +2 | +1 | **+2!** | **+1!** | **+1!** | +1 | **+1!** |

**Contested cells** — the three models differ  by two points or more, so the median is not a consensus and should not be read as one:

- **Precision × BLUF/Army** — +3, +1, +1
- **Precision × Minto** — +3, +1, +1
- **Precision × ISO 24495-1** — +3, +1, +1
- **Precision × Blameless PM** — +3, +1, +1
- **Precision × Hemingway** — +3, -1
- **Precision × Hotaling** — +3, +2, +1
- **Precision × repo skills** — +3, +2, +1
- **Brevity × Amazon memo** — +2, -1
- **Brevity × ISO 24495-1** — +3, +1, +1
- **Brevity × Toulmin** — +3, -1, -1
- **Brevity × repo skills** — +0, +2, +1
- **Scannability × ASD-STE100** — +3, +1, +1
- **Scannability × Amazon memo** — +3, +0, -1
- **Scannability × ISO 24495-1** — +3, +1, +1
- **Scannability × Blameless PM** — +2, +0, +1
- **Scannability × Toulmin** — +3, -1
- **Scannability × repo skills** — +3, +1, +1
- **Actionability × ASD-STE100** — +0, +2, +1
- **Actionability × Amazon memo** — +3, +2, +1
- **Actionability × ISO 24495-1** — +3, +1, +1
- **Actionability × Blameless PM** — +2, +0, +1
- **Confidence calibration × ASD-STE100** — +2, +0
- **Confidence calibration × BLUF/Army** — +3, -1
- **Confidence calibration × Minto** — +3, -1
- **Confidence calibration × Amazon memo** — +2, +0, +1
- **Confidence calibration × ISO 24495-1** — +3, +1
- **Confidence calibration × Blameless PM** — +3, +2, +1
- **Confidence calibration × Hemingway** — +3, -1, -1
- **Confidence calibration × Hotaling** — +3, +1, +1
- **Confidence calibration × repo skills** — +2, +0
- **Empathy × ASD-STE100** — +1, -1
- **Empathy × BLUF/Army** — +1, -1
- **Empathy × Minto** — +2, +0
- **Empathy × ISO 24495-1** — +3, +1, +1
- **Empathy × Blameless PM** — +3, +2, +1
- **Empathy × Hemingway** — +1, -1
- **Empathy × Hotaling** — +3, +0
- **Empathy × repo skills** — +2, -1
- **Persuasive force × Minto** — +3, +2, +1
- **Persuasive force × Amazon memo** — +3, +2, +1
- **Persuasive force × Toulmin** — +0, +2, +1
- **Persuasive force × Hotaling** — +3, +1
- **Accountability × BLUF/Army** — +3, +1, +1
- **Accountability × Amazon memo** — +3, +1, +1
- **Accountability × Hemingway** — +3, -1
- **Accessibility × Amazon memo** — +2, +0
- **Accessibility × ISO 24495-1** — +3, +2, +1
- **Accessibility × Blameless PM** — +2, +0
- **Accessibility × Toulmin** — +2, -1, -1
- **Accessibility × repo skills** — +3, +2, +1
- **Durability × BLUF/Army** — +2, +0, +1
- **Durability × Blameless PM** — +3, +2, +1
- **Durability × Toulmin** — +0, +2, +1
- **Durability × Hemingway** — +3, -1
- **Durability × repo skills** — +3, +1, +1

`†` = one model declined to score this cell. `·` = no model scored it.
