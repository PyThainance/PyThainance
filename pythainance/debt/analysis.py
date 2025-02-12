# pythainance/debt/analysis.py

import os
import pandas as pd

def load_debt_data(filepath="pythainance/dataset/debt.xlsx"):
    """
    Load debt data from an Excel file and convert the index to datetime.
    """
    if not os.path.exists(filepath):
        # If the file does not exist, use the loader to set up the data
        from pythainance.debt.loader import setup_debt_data, fix_format_debt_data
        setup_debt_data()
        fix_format_debt_data()
    
    df = pd.read_excel(filepath, index_col=0)
    # Convert the index to datetime for time series analysis
    df.index = pd.to_datetime(df.index, format="%d/%m/%Y")
    return df

def compute_government_debt(df):
    """
    Compute government debt by aggregating data from sections 1.1, 1.2, and 1.3.
    If the column "หนี้รัฐบาล" exists, it will be used directly. Otherwise, the
    function will sum up the sub-columns accordingly.
    
    Example column groups (adjust these based on the actual dataset):
        1.1: ['หนี้ที่รัฐบาลกู้โดยตรง', 'หนี้ต่างประเทศ', 'เงินกู้เพื่อใช้ในแผนงาน/โครงการของรัฐบาล', ...]
        1.2: ['หนี้ที่รัฐบาลกู้เพื่อชดใช้ความเสียหายให้แก่กองทุนเพื่อการฟื้นฟูฯ', 'FIDF 1', 'FIDF 3']
        1.3: ['หนี้เงินกู้ล่วงหน้าเพื่อปรับโครงสร้างหนี้', ...]
    """
    if "หนี้รัฐบาล" in df.columns:
        return df["หนี้รัฐบาล"]
    
    # Define example column lists for each group (adjust these to match your dataset)
    cols_1_1 = ["หนี้ที่รัฐบาลกู้โดยตรง", "หนี้ต่างประเทศ", "เงินกู้เพื่อใช้ในแผนงาน/โครงการของรัฐบาล",
                "เงินกู้ให้กู้ต่อ", "หนี้ในประเทศ", "เงินกู้ชดเชยการขาดดุลงบประมาณ และการบริหารหนี้",
                "พันธบัตรโครงการช่วยเพิ่มเงินกองทุน", "เงินกู้เพื่อการปรับโครงสร้างหนี้ต่างประเทศ",
                "เงินกู้เพื่อฟื้นฟูและเสริมสร้างความมั่นคงทางเศรษฐกิจ", "เงินกู้ภายใต้ พ.ร.ก. COVID-19 พ.ศ. 2563",
                "เงินกู้ภายใต้ พ.ร.ก. COVID-19 เพิ่มเติม พ.ศ. 2564", "เงินกู้เพื่อนำเข้ากองทุนส่งเสริมการประกันภัย",
                "เงินกู้เพื่อวางระบบบริหารจัดการน้ำ", "เงินกู้ให้กู้ต่อ",
                "เงินกู้เพื่อปรับโครงสร้างหนี้ต่างประเทศที่กระทรวงการคลังค้ำประกัน",
                "เงินกู้เพื่อใช้ในการดำเนินโครงการเงินกู้ DPL",
                "เงินกู้เพื่อการพัฒนาระบบบริหารจัดการทรัพยากรน้ำและระบบขนส่งทางถนนระยะเร่งด่วน"]
    
    cols_1_2 = ["หนี้ที่รัฐบาลกู้เพื่อชดใช้ความเสียหายให้แก่กองทุนเพื่อการฟื้นฟูฯ", "FIDF 1", "FIDF 3"]
    
    cols_1_3 = ["หนี้เงินกู้ล่วงหน้าเพื่อปรับโครงสร้างหนี้", "หนี้เงินกู้เพื่อชดเชยการขาดดุลงบประมาณ",
                "เงินกู้ภายใต้ พ.ร.ก. COVID-19 พ.ศ. 2563", "เงินกู้ภายใต้ พ.ร.ก. COVID-19 พ.ศ. 2564",
                "หนี้เงินกู้เพื่อชดใช้ความเสียหายให้แก่กองทุนเพื่อการฟื้นฟูฯ", "FIDF 1", "FIDF 3",
                "หนี้เงินกู้เพื้่อฟื้นฟูและเสริมสร้างความมั่นคงทางเศรษฐกิจ",
                "หนี้เงินกู้เพื่อการพัฒนาระบบบริหารจัดการทรัพยากรน้ำและระบบขนส่งทางถนนระยะเร่งด่วน"]
    
    # Filter the columns that actually exist in the DataFrame
    cols_1_1 = [col for col in cols_1_1 if col in df.columns]
    cols_1_2 = [col for col in cols_1_2 if col in df.columns]
    cols_1_3 = [col for col in cols_1_3 if col in df.columns]
    
    debt_1_1 = df[cols_1_1].sum(axis=1) if cols_1_1 else pd.Series(0, index=df.index)
    debt_1_2 = df[cols_1_2].sum(axis=1) if cols_1_2 else pd.Series(0, index=df.index)
    debt_1_3 = df[cols_1_3].sum(axis=1) if cols_1_3 else pd.Series(0, index=df.index)
    
    government_debt = debt_1_1 + debt_1_2 + debt_1_3
    return government_debt

def compute_debt_to_gdp_ratio(df):
    """
    Return the debt-to-GDP ratio from the 'Debt : GDP (%)' column.
    """
    return df["Debt : GDP (%)"]

def compute_total_debt(df):
    """
    Return the total debt from the 'รวม' column.
    """
    return df["รวม"]

# Additional analysis functions (e.g., for state enterprise debt) can be added here.
