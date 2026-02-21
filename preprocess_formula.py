import re
def preprocess_formula(formula: str,add_replacements:dict|None=None) -> str:
    """transfer the formula that user inputs to the python-form(that can be identified by the lib 'sympy')"""
    assert isinstance(formula,str) and isinstance(add_replacements,dict|None)
    replacements= {"^": "**", "×": "*", "÷": "/", ":": "/",
                                 "⅓": "(1/3)", "⅔": "(2/3)", "⅛": "(0.125)", "⅜": "(0.375)", "⅝": "(0.625)", "⅞": "(0.875)", "½": "(0.5)", "¼": "(0.25)", "¾": "(0.75)",
                                 "[": "(", "]": ")", "{": "(", "}": ")", "【": "(", "】": ")", "（": "(", "）": ")", "［": "(", "］": ")", "｛": "(", "｝": ")", "「": "(", "」": ")",
                                 "０": "0", "１": "1", "２": "2", "３": "3", "４": "4", "５": "5", "６": "6", "７": "7", "８": "8", "９": "9",
                                 "＋": "+", "－": "-", "＊": "*", "／": "/", "⁄": "/", "＝": "=", "．": ".", "：": "/", "·": "*", "＾": "**", "mod": "%",
                                 "ａ": "a", "ｂ": "b", "ｃ": "c", "ｄ": "d", "ｅ": "e", "ｆ": "f", "ｇ": "g", "ｈ": "h", "ｉ": "i", "ｊ": "j", "ｋ": "k", "ｌ": "l", "ｍ": "m",
                                 "ｎ": "n", "ｏ": "o", "ｐ": "p", "ｑ": "q", "ｒ": "r", "ｓ": "s", "ｔ": "t", "ｕ": "u", "ｖ": "v", "ｗ": "w", "ｘ": "x", "ｙ": "y", "ｚ": "z"}
    if add_replacements is not None:
        replacements.update(add_replacements)
    for src, dest in replacements.items(): formula = formula.replace(src, dest)
    return str(re.sub(r'[a-zA-Z]+', lambda matches: ''.join([_char + '*' for _char in matches.group(0)[:-1]] + [matches.group(0)[-1]]),re.sub(r'(\d+)([a-zA-Z]+)', r'\1*\2', re.sub(r'(\d+)\((.*?)\)', r'\1*(\2)',re.sub(r'([a-zA-Z]+)\((.*?)\)', r'\1*(\2)',re.sub(r'\((.*?)\)([a-zA-Z]+)', r'(\1)*\2',re.sub(r'(\d+)([a-zA-Z()]+)',lambda matches: str(f"{str(matches.group(1))}*{'*'.join(matches.group(2))}"),re.sub(r'\(([^()]+)\)',lambda matches: (str(f"({preprocessed_f})") if (re.search(r'\d|[a-zA-Z]',preprocessed_f := preprocess_formula(matches.group(1)),re.UNICODE)) else preprocessed_f),re.sub(r'[\s,，]+', '',formula,flags=re.UNICODE)),flags=re.UNICODE).replace('(*', "(").replace('*)', ")"), flags=re.DOTALL),flags=re.DOTALL),flags=re.UNICODE | re.DOTALL),flags=re.UNICODE)).strip())
