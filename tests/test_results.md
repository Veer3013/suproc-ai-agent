# Suproc AI Agent - Evaluation Tests

## Summary

- Total Tests: 10
- Passed: 10
- Failed: 0

---

## Test 1 – Exact Supplier Match

Input:
Need biodegradable raw material supplier in Kerala

Expected:
Return exact supplier(s).

Status:
✅ PASS

---

## Test 2 – Closest Match

Input:
Need food grade packaging supplier in Tamil Nadu with capacity 10000 delivery in 30 days

Expected:
No exact supplier → closest matches.

Status:
✅ PASS

---

## Test 3 – Logistics Search

Input:
Need logistics company in Telangana

Status:
✅ PASS

---

## Test 4 – Packaging Search

Input:
Need packaging supplier in Karnataka

Status:
✅ PASS

---

## Test 5 – Capacity Constraint

Input:
Need packaging supplier with capacity 50000

Status:
✅ PASS

---

## Test 6 – Delivery Constraint

Input:
Need supplier with delivery in 5 days

Status:
✅ PASS

---

## Test 7 – Missing Information

Input:
Need supplier

Expected:
Parser handles missing constraints.

Status:
✅ PASS

---

## Test 8 – Validation

Expected:
Duplicate and invalid suppliers removed.

Status:
✅ PASS

---

## Test 9 – Human Approval

Expected:
Agent generates outreach but waits for approval.

Status:
✅ PASS

---

## Test 10 – Closest Match Explanation

Expected:
Show matched and unmatched constraints.

Status:
✅ PASS

---

## Known Limitations

- Uses a synthetic SQLite dataset.
- No live supplier APIs.
- CLI interface only.
- No automatic email sending.