import difflib

text1 = """
Договор на сумма 15000 рублей. Спасибо.
"""
text2 = """
Договор на сумма 17500 рублей. Спасибо.
"""

text1 = text1.splitlines()
text2 = text2.splitlines()

d = difflib.Differ()
diff = d.compare(text1, text2)
print('\n'.join(diff))
print('*'*40)
du = difflib.unified_diff(text1, text2)
print('\n'.join(list(du)))
