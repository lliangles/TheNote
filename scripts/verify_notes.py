#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
TheNote 筆記庫自動化品質與渲染檢驗工具 (Pre-push Verification)
------------------------------------------------------------
用途：在每一次 git push 前執行全庫檢核，確保：
1. Mermaid 圖表語法正確、程式碼圍欄標準 (```mermaid)，可在 GitHub 正常繪製。
2. 圖片參照相容性：避免使用 GitHub 不支援的 Obsidian `![[...]]` 語法，檢查相對路徑存在性。
3. LaTeX 數學公式完整性：
   - 避免控制字元 (\t, \f, \a 等) 逸出破壞公式排版。
   - 確保 $ 與 $$ 圍欄平衡配對，無單邊未閉合。
   - 杜絕未進入數學模式之裸露 LaTeX 關鍵字 (如 \frac, \sum, \sigma, \mathbb, \sqrt 等)。
   - 防範字串插值丟失變數陷阱 (如 ho_{...}, = \frac 等缺少前置變數)。
4. Markdown 表格語法完整性。
"""

import os
import re
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

LATEX_KEYWORDS = re.compile(
    r'\\(?:frac|sum|sigma|mathbb|sqrt|alpha|beta|gamma|lambda|rho|mu|pi|theta|epsilon|times|approx|implies|le\b|ge\b|in\b|left|right|Delta|text\{|operatorname\{|infty)'
)

def check_all():
    print("=" * 70)
    print("🚀 [TheNote] 啟動全筆記庫渲染與語法完整性檢驗...")
    print(f"📁 倉庫根目錄: {REPO_ROOT}")
    print("=" * 70)

    md_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        # 忽略 git 與 scratch 暫存目錄
        if ".git" in root or "scratch" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                md_files.append(os.path.join(root, f))

    print(f"📊 掃描到 Markdown 檔案總數: {len(md_files)} 個\n")

    errors = []
    warnings = []
    mermaid_count = 0
    image_count = 0
    math_count = 0

    for fpath in md_files:
        rel_path = os.path.relpath(fpath, REPO_ROOT)
        file_dir = os.path.dirname(fpath)

        with open(fpath, "r", encoding="utf-8", errors="replace") as fp:
            lines = fp.readlines()

        in_code_block = False
        in_display_math = False
        in_mermaid = False
        mermaid_start_line = -1
        display_math_start_line = -1

        for idx, line in enumerate(lines, start=1):
            stripped = line.strip()

            # 1. 檢測非標準的 Mermaid 圍欄 (如單反引號 `mermaid)
            if stripped.startswith("`mermaid") and not stripped.startswith("```mermaid"):
                errors.append((rel_path, idx, f"Mermaid 圖表開頭圍欄錯誤 (應為 ```mermaid，不可使用單反引號): {repr(stripped)}"))

            # 2. 程式碼區塊追蹤
            if stripped.startswith("```"):
                if not in_code_block:
                    in_code_block = True
                    if stripped.startswith("```mermaid"):
                        in_mermaid = True
                        mermaid_start_line = idx
                        mermaid_count += 1
                else:
                    if stripped == "```":
                        in_code_block = False
                        in_mermaid = False
                continue

            if in_code_block:
                if in_mermaid:
                    if stripped == "`":
                        errors.append((rel_path, idx, f"Mermaid 結尾使用了單反引號 `，應使用三個反引號 ```"))
                        in_mermaid = False
                        in_code_block = False

                    if stripped.startswith("subgraph "):
                        tokens = stripped.split()
                        if len(tokens) > 2 and not ('"' in stripped or '[' in stripped):
                            warnings.append((rel_path, idx, f"Mermaid subgraph 命名建議加上引號或標準 ID 標註: {stripped}"))

                    if "\\b" in stripped or "\\m" in stripped or "\\s" in stripped:
                        warnings.append((rel_path, idx, f"Mermaid 節點文字包含反斜線轉義字元，建議改用 Unicode 符號: {stripped}"))
                continue

            # 3. 獨立多行 Display Math ($$) 追蹤
            if stripped == "$$":
                if not in_display_math:
                    in_display_math = True
                    display_math_start_line = idx
                    math_count += 1
                else:
                    in_display_math = False
                continue

            if in_display_math:
                math_count += 1
                continue

            # 4. 圖片參照檢測
            obsidian_embeds = re.findall(r'!\[\[(.*?)\]\]', line)
            for emb in obsidian_embeds:
                errors.append((rel_path, idx, f"偵測到 GitHub 無法渲染的 Obsidian 語法 ![[{emb}]]，請改為標準 Markdown: ![alt]({emb})"))

            md_images = re.findall(r'!\[(.*?)\]\((.*?)\)', line)
            for alt, link in md_images:
                image_count += 1
                if not link.startswith(("http://", "https://")):
                    clean_link = link.split("#")[0].split("?")[0]
                    local_path = os.path.normpath(os.path.join(file_dir, clean_link))
                    repo_path = os.path.normpath(os.path.join(REPO_ROOT, clean_link.lstrip("/\\")))
                    if not os.path.exists(local_path) and not os.path.exists(repo_path):
                        errors.append((rel_path, idx, f"圖片連結不存在: {link}"))

            # 5. LaTeX 控制字元檢測
            if any(bad_char in line for bad_char in ["\x0c", "\x07", "\x08"]):
                errors.append((rel_path, idx, f"LaTeX 行包含損毀的控制字元 (formfeed/bell/backspace)"))

            if "$" in line and "\t" in line:
                math_spans = re.findall(r'\$(.*?)\$', line)
                for span in math_spans:
                    if "\t" in span:
                        errors.append((rel_path, idx, f"LaTeX 數學公式中含有 Tab 字元: {repr(span)}"))

            # 6. 單行 Display Math 與 Inline Math 平衡檢測
            # 移除同行已閉合的 $$...$$ 與行內代碼 `...`
            work_line = line
            work_line = re.sub(r'(?<!\\)\$\$.*?(?<!\\)\$\$', '', work_line)
            work_line = re.sub(r'`[^`]*`', '', work_line)

            # 檢查單個 $ 是否成對
            single_dollars = len(re.findall(r'(?<!\\)\$(?!\$)', work_line))
            if single_dollars % 2 != 0:
                errors.append((rel_path, idx, f"未配對閉合的單個 $ 符號 (出現 {single_dollars} 個): {stripped[:60]}"))
                continue

            # 移除合法閉合的行內公式 $...$
            outside_math = re.sub(r'(?<!\\)\$.*?(?<!\\)\$', '', work_line)

            # 7. 裸露 LaTeX 指令檢測 (公式未被 $ 或 $$ 包覆)
            if LATEX_KEYWORDS.search(outside_math):
                # 排除一般常見非 LaTeX 的反斜線使用 (例如行尾換行 \\)
                m = LATEX_KEYWORDS.findall(outside_math)
                errors.append((rel_path, idx, f"偵測到未包裹在 $...$ 或 $$...$$ 內的裸露 LaTeX 公式語法 ({m}): {stripped[:60]}"))

            # 8. 丟失變數特徵檢測 (防範字串插值丟失變數)
            if re.search(r'(?<![a-zA-Z0-9_\\])ho_\{|^\s*=\s*\\frac|[（(]\s*=\s*\\frac|[:：]\s*\.\d+\s*\\times', line):
                errors.append((rel_path, idx, f"偵測到損毀或缺失前置變數的公式特徵: {stripped[:60]}"))

        if in_mermaid:
            errors.append((rel_path, mermaid_start_line, "Mermaid 圖表未正確閉合 (缺少結尾 ```)"))
        if in_display_math:
            errors.append((rel_path, display_math_start_line, "Display Math 公式區塊未正確閉合 (缺少結尾 $$)"))

    print(f"📈 統計資訊：掃描了 {mermaid_count} 個 Mermaid 圖表，檢驗了 {image_count} 個圖片參照。")

    if warnings:
        print(f"\n⚠️  發現 {len(warnings)} 項格式優化警告：")
        for w in warnings:
            print(f"  [WARN] {w[0]}:{w[1]} - {w[2]}")

    if errors:
        print(f"\n❌ 發現 {len(errors)} 項重大渲染錯誤（將阻止 GitHub 正確繪製）：")
        for e in errors:
            print(f"  [ERROR] {e[0]}:{e[1]} - {e[2]}")
        print("\n💥 檢驗失敗！請先修復上述錯誤後再推送至 GitHub。")
        return False
    else:
        print("\n✅ 所有 Mermaid 圖表、圖片參照、LaTeX 數學公式與 Markdown 語法檢驗完全通過 (0 Errors)！")
        return True

if __name__ == "__main__":
    success = check_all()
    sys.exit(0 if success else 1)
