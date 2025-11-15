import pandas as pd
import glob
import os

# Load Excel
set1 = pd.read_excel("data/raw/training_set_rel3.xls")

input_pattern = "data/raw/Prompt-*.csv"
output_dir = "data/processed"
os.makedirs(output_dir, exist_ok=True)

group_12 = []
group_3456 = []

for file in glob.glob(input_pattern):
    fname = os.path.basename(file)
    prompt_id = fname.replace("Prompt-", "").replace(".csv", "")
    prompt_id_int = int(prompt_id)

    # === Nhóm 1: Prompt 1 và 2 (format tốt) ===
    if prompt_id_int in [1, 2]:
        df = pd.read_csv(file)
        df = df.rename(columns={'Essay ID': 'essay_id'})
        
        merged = pd.merge(df, set1[['essay_id', 'essay']],
                          on='essay_id', how='left')

        out_path = f"{output_dir}/essay_set{prompt_id}.csv"
        merged.to_csv(out_path, index=False)
        print("Saved:", out_path)

        group_12.append(merged)

    # === Nhóm 2: Prompt 3–6 (format khác, nhiều comma vấn đề) ===
    else:
        # Đọc raw dạng flexible
        df = pd.read_csv(file, engine="python")
        # tìm cột chứa ID
        id_col = None
        for c in df.columns:
            if c.lower() in ["essay id", "essay_id", "id"]:
                id_col = c
                break
        
        if id_col is None:
            print("❌ Không tìm thấy essay_id trong file:", file)
            continue
        
        df = df.rename(columns={id_col: "essay_id"})
        
        merged = pd.merge(df, set1[['essay_id', 'essay']],
                          on='essay_id', how='left')

        out_path = f"{output_dir}/essay_set{prompt_id}.csv"
        merged.to_csv(out_path, index=False)
        print("Saved:", out_path)

        group_3456.append(merged)


# === Save group 1 ===
if group_12:
    all_12 = pd.concat(group_12, ignore_index=True)
    all_12.to_csv(f"{output_dir}/essay_set_12_all.csv", index=False)
    print("Saved: data/processed/essay_set_12_all.csv")

# === Save group 2 ===
if group_3456:
    all_3456 = pd.concat(group_3456, ignore_index=True)
    all_3456.to_csv(f"{output_dir}/essay_set_3456_all.csv", index=False)
    print("Saved: data/processed/essay_set_3456_all.csv")
