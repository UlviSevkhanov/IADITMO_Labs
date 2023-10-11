import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplcursors

try:
    df = pd.read_excel('D:\course.xlsx')
    print(df.columns)

    fig, ax = plt.subplots(figsize=(13, 8))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Форматирование даты на оси X

    # Установка интервала для абсциссы в один месяц
    month_interval = mdates.MonthLocator(interval=1)
    ax.xaxis.set_major_locator(month_interval)

    ax.plot(df['Дата'], df['Максимум'], label='MAX', marker='o', linestyle='-')
    ax.plot(df['Дата'], df['Минимум'], label='MIN', marker='o', linestyle='-')
    ax.set_title('Доллар-Рубль')
    ax.set_xlabel('Дата')
    ax.set_ylabel('Курс')
    ax.grid(True)
    ax.legend()

    plt.tight_layout()
    plt.xticks(rotation=45)  # Поворот дат на оси X для лучшей читаемости

    mplcursors.cursor(hover=True)

    plt.show()
except FileNotFoundError:
    print("File not found. Check the file path.")
except UnicodeDecodeError:
    print("Unable to decode the file with the specified encoding. Check encoding.")
