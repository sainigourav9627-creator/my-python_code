calendar Module

calendar Python का built-in module है। इसका इस्तेमाल calendar से related information निकालने के लिए होता है।

सबसे पहले module import:


import calendar



| Function       | काम                        | Syntax                         |
| -------------- | -------------------------- | ------------------------------ |
| `isleap()`     | Leap year check            | `calendar.isleap(2024)`        |
| `month()`      | एक महीने का calendar       | `calendar.month(2026, 9)`      |
| `calendar()`   | पूरे साल का calendar       | `calendar.calendar(2026)`      |
| `weekday()`    | Weekday number             | `calendar.weekday(2026, 9, 1)` |
| `monthrange()` | First weekday + total days | `calendar.monthrange(2026, 9)` |




weekday() Number

0 → Monday
1 → Tuesday
2 → Wednesday
3 → Thursday
4 → Friday
5 → Saturday
6 → Sunday
