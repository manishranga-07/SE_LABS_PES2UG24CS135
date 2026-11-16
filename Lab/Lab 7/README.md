# L6_L7_10 — Bus Transit Fare

## Lab 7: Fuzzing for Input Validation Bugs with Hypothesis

### About

Lab 7 explores dynamic property-based fuzz testing as a security and quality assurance technique. Using the **Hypothesis** fuzzing library in Python, we uncover unexpected crashes, boundary errors, and unhandled exceptions across three key transit fare processing functions:
1. `parse_transit_corridor(corridor_code)` — Parses origin, destination, and zone counts to calculate corridor transit fares.
2. `lookup_concession_discount(category_name)` — Retrieves fare multiplier discounts for concession passenger categories.
3. `compute_passenger_density(occupancy_ratio_str)` — Calculates passenger-per-kilometer transit density ratios.

Through Hypothesis property-based testing (`@given(st.text() | st.none())`), we uncovered critical input validation vulnerabilities (including `AttributeError`, `ValueError`, `KeyError`, and `ZeroDivisionError`), shrunk them down to minimal reproducing test cases, and hardened the application using defensive programming.

---

### Files

| File | Description |
|------|-------------|
| `processor.py` | Hardened, defensively programmed application script (zero crashes) |
| `processor_buggy.py` | Reference copy of the original buggy starter script |
| `test_processor.py` | Property-based fuzz test suite using Hypothesis and Pytest |
| `hypothesis_fuzzing_failures.png` | Terminal capture of initial test failures uncovered by Hypothesis |
| `hypothesis_tests_passing.png` | Terminal capture of 100% test pass on hardened code |
| `submissions/` | Submission package containing final PDF report and screenshot assets |
| `submissions/Lab7_Fuzzing_Input_Validation.pdf` | Comprehensive 4-page submission PDF report with screenshots |
| `submissions/Lab7_Fuzzing_Combined_Screenshots.png` | High-resolution combined image of all 4 lab steps |

---

### Hypothesis Fuzz Testing Results

- **Starter Code**: 3 / 3 test cases failed under Hypothesis fuzzing.
- **Failures Discovered**:
  - `parse_transit_corridor`: Crashed with `AttributeError` on `None`, and `ValueError` (unpack count) on `""`.
  - `lookup_concession_discount`: Crashed with `AttributeError` on `None`, and `KeyError` on unrecognized/empty keys `""`.
  - `compute_passenger_density`: Crashed with `AttributeError` on `None`, `ValueError` on missing delimiters `""` or non-numeric tokens `'/'`, and `ZeroDivisionError` on `km = 0`.
- **Hardened Code**: 3 / 3 test cases passing (300 randomized fuzz trials across all functions with **zero crashes**).

---

### Commands to Run

#### 1. Run the Application
```bash
python processor.py
```
**Example Inputs:**
- Corridor: `DT-UP-3` &rarr; `Route DT->UP: 3 Zones, Fare $4.75`
- Concession: `STUDENT` &rarr; `Multiplier: 0.5`
- Passenger Density: `50/10.0` &rarr; `Density: 5.0`

#### 2. Run Hypothesis Fuzz Tests
```bash
pytest test_processor.py
```
*(or `python -m pytest test_processor.py`)*

---

### Deliverables Checklist

- [x] **Deliverable 1:** PDF Document with screenshots (`submissions/Lab7_Fuzzing_Input_Validation.pdf`)
- [x] **Deliverable 2:** Fixed application python script (`processor.py`)
- [x] **Deliverable 3:** Updated `test_processor.py` code using Hypothesis
