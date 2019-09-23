from fixPriceLabel import fix_price_label

# Test 01 when input string is Was £10, then £8, then £11, now £6 it should return "Was £11, now £9"
assert fix_price_label("Was £11, then £8, now £9") == "Was £11, now £9"

# Test 02 when input string is Was £12, then £9, now £10 it should return "Was £12, now £10"
assert fix_price_label("Was £12, then £9, now £10") == "Was £12, now £10"

# Test 03: when 3 reductions are made before increasing the last price
assert fix_price_label("Was £10, then £6, then £4, now £8") == "Was £10, now £8"

# Test 04: when there is a repeated value
assert fix_price_label("Was £10, then £8, then £8, now £6") == "Was £10, then £8, now £6"

# Test 05: return the pries with the same format as in the input string
assert fix_price_label("Was £21.50, then £15.75, then £10.25, now £6") == "Was £21.50, then £15.75, then £10.25, now £6"

# Test 06: further test that prices have the same format as in the input string
assert fix_price_label("Was £21.50, then £21.75, then £10.25, now £6") == "Was £21.75, then £10.25, now £6"

# Test 07: test we keep the correct format of two prices the same but expressed differently
assert fix_price_label("Was £18, then £17, then £18.00, now £11.50") == "Was £18.00, now £11.50"
