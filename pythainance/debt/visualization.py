import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_public_debt_composition(debt):
    plt.figure(figsize=(12,6))
    plt.stackplot(debt.date,
                  debt['1. หนี้รัฐบาล (1.1+1.2+1.3)'],
                  debt['2. หนี้รัฐวิสาหกิจ (2.1+2.2)'],
                  debt['5. หนื้หน่วยงานของรัฐ (5.1+5.2)'],
                  labels=['Government Debt', 'State Enterprise Debt', 'Government Agency Debt'],
                  colors=['#2E86C1', '#F1C40F', '#E74C3C'])
    plt.title('Public Debt Composition by Sector', fontsize=14)
    plt.legend(loc='upper left')
    plt.xticks(debt.date[::19], rotation=45)
    plt.ylabel('Million THB')
    plt.tight_layout()
    plt.show()

def plot_debt_gdp(debt):
    fig, ax1 = plt.subplots(figsize=(12,6))
    ax1.plot(debt.date, debt['Debt : GDP (%)'], color='#C0392B', marker='o')
    ax1.set_ylabel('Debt-to-GDP Ratio (%)', color='#C0392B')
    ax1.tick_params(axis='y', labelcolor='#C0392B')
    ax2 = ax1.twinx()
    ax2.plot(debt.date, debt['ประมาณการ GDP (ล้านบาท)'], color='#27AE60')
    ax2.set_ylabel('GDP (Million THB)', color='#27AE60')
    ax2.tick_params(axis='y', labelcolor='#27AE60')
    plt.title('Debt-to-GDP Ratio vs GDP Growth', fontsize=14)
    plt.xticks(debt.date[::19], rotation=45)
    plt.tight_layout()
    plt.show()

def plot_covid_debt_impact(debt):
    covid_debt = debt[['เงินกู้ภายใต้ พ.ร.ก. COVID-19 พ.ศ. 2563',
                       'เงินกู้ภายใต้ พ.ร.ก. COVID-19 เพิ่มเติม พ.ศ. 2564']].sum(axis=1)
    non_covid_debt = debt['1. หนี้รัฐบาล (1.1+1.2+1.3)'] - covid_debt
    plt.figure(figsize=(12,6))
    plt.stackplot(debt.date, non_covid_debt, covid_debt,
                  labels=['General Government Debt', 'COVID-19 Related Debt'],
                  colors=['#3498DB','#F39C12'])
    plt.title('Government Debt: COVID-19 Impact', fontsize=14)
    plt.legend(loc='upper left')
    plt.xticks(debt.date[::19], rotation=45)
    plt.ylabel('Million THB')
    plt.tight_layout()
    plt.show()

def plot_foreign_debt_and_exchange(debt):
    fig, ax1 = plt.subplots(figsize=(12,6))
    ax1.plot(debt.date, debt['หนี้ต่างประเทศ'], color='#16A085')
    ax1.set_ylabel('Foreign Debt (Million THB)', color='#16A085')
    ax1.tick_params(axis='y', labelcolor='#16A085')
    ax2 = ax1.twinx()
    ax2.plot(debt.date, debt['อัตราแลกเปลี่ยน (บาท)'], color='#D35400', linestyle='--')
    ax2.set_ylabel('Exchange Rate (THB per USD)', color='#D35400')
    ax2.tick_params(axis='y', labelcolor='#D35400')
    plt.title('Foreign Debt Exposure and Exchange Rate', fontsize=14)
    plt.xticks(debt.date[::19], rotation=45)
    plt.tight_layout()
    plt.show()

def plot_debt_guarantee_status(debt):
    plt.figure(figsize=(12,6))
    plt.plot(debt.date, debt['2.1 หนี้ที่รัฐบาลค้ำประกัน'], label='Government Guaranteed', color='#9B59B6')
    plt.plot(debt.date, debt['2.2 หนี้ที่รัฐบาลไม่ค้ำประกัน'], label='Non-Guaranteed', color='#2ECC71')
    plt.title('State Enterprise Debt Guarantee Status', fontsize=14)
    plt.legend()
    plt.xticks(debt.date[::19], rotation=45)
    plt.ylabel('Million THB')
    plt.tight_layout()
    plt.show()

def plot_debt_metrics_correlation(debt):
    cols = ['1. หนี้รัฐบาล (1.1+1.2+1.3)',
            '2. หนี้รัฐวิสาหกิจ (2.1+2.2)',
            '5. หนื้หน่วยงานของรัฐ (5.1+5.2)',
            'Debt : GDP (%)',
            'อัตราแลกเปลี่ยน (บาท)']
    english_labels = [
        'Government Debt',
        'State Enterprise Debt',
        'Government Agency Debt',
        'Debt-to-GDP Ratio',
        'Exchange Rate'
    ]
    plt.figure(figsize=(10,8))
    sns.heatmap(debt[cols].corr(),
                annot=True,
                cmap='coolwarm',
                fmt='.2f',
                linewidths=0.5,
                xticklabels=english_labels,
                yticklabels=english_labels)
    plt.title('Key Debt Metrics Correlation', fontsize=14)
    plt.tight_layout()
    plt.show()

def plot_debt_gdp_with_crisis(debt):
    debt['date'] = pd.to_datetime(debt['date'])
    plt.figure(figsize=(14,7))
    plt.plot(debt['date'], debt['Debt : GDP (%)'],
             color='#2c3e50',
             linewidth=2.5,
             marker='o',
             markersize=5)
    plt.axvspan(pd.to_datetime('2020-03-01'), pd.to_datetime('2022-12-01'),
                alpha=0.2, color='#e74c3c', label='COVID-19 Crisis')
    max_debt = debt.loc[debt['Debt : GDP (%)'].idxmax()]
    plt.annotate(f'Peak: {max_debt["Debt : GDP (%)"]:.1f}%',
                 xy=(max_debt['date'], max_debt['Debt : GDP (%)']),
                 xytext=(20,20),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->'))
    plt.title('Thailand Debt-to-GDP Ratio with Crisis Periods', fontsize=16)
    plt.ylabel('Debt/GDP (%)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_debt_service_heatmap(debt):
    debt['Interest_Payment'] = debt['รวม'] * 0.03
    debt['Debt_Service_Ratio'] = debt['Interest_Payment'] / debt['ประมาณการ GDP (ล้านบาท)']
    pivot_table = debt.pivot_table(index='year',
                                   columns='month',
                                   values='Debt_Service_Ratio',
                                   aggfunc='mean')
    plt.figure(figsize=(14,8))
    sns.heatmap(pivot_table,
                cmap='RdYlGn_r',
                annot=True,
                fmt='.2%',
                linewidths=0.5)
    plt.title('Debt Service Capacity Heatmap (by Year-Month)', fontsize=16)
    plt.xlabel('Month')
    plt.ylabel('Year')
    plt.tight_layout()
    plt.show()
