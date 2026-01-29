#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import datetime

from matplotlib import rcParams

DATE_FORMAT = '%Y-%m-%d'
TODAY = '2025-07-17'

TITLE = "Gartenteich anlegen"
TITLE_SIZE = 12
TITLE_FONT_WEIGHT = "bold"

FONT_COLOR = "#0C0C0C"

X_LABEL = ""
Y_LABEL = ""
LABEL_SIZE = 8

DAY_FONT_SIZE = 8
MONTH_FONT_SIZE = 10
MONTH_FONT_WEIGHT = "bold"

BAR_COLOR = "#30C7DC"
TASKTYPE_BAR_COLORS = {
    "In Vorbereitung": "#694fff",
    "Im Plan": "#dce238",
    "Abgeschlossen": "#5fdc00",
    "Verspaetet": "#ff6e61",
    "Abgebrochen": "#4b4b4b"
}  

FONT_FAMILY = "sans-serif"
FONT_SANS_SERIF = ["Arial", "Roboto", "DejaVu Sans"]



rcParams['font.family'] = FONT_FAMILY
rcParams['font.sans-serif'] = FONT_SANS_SERIF
rcParams['axes.titlesize'] = TITLE_SIZE
rcParams['axes.labelsize'] = LABEL_SIZE

def build_week_ticks(start_date, end_date):

    mondays = pd.date_range(start=start_date, end=end_date, freq='W-MON')
    return mondays, [d.strftime('%d') for d in mondays]

def plot_gantt(tasks, output_path=None):
    if tasks.empty:
        print("No tasks to plot.")
        return
    
    start_date = tasks['start_date'].min()
    end_date = tasks['end_date'].max()

    tasks = tasks.sort_values(by=['start_date', 'task_group'], 
                              ascending=False)

    fig, ax = plt.subplots(figsize=(12, 6))

    bars = []

    for _, task in tasks.iterrows():
        duration = (task['end_date'] - task['start_date']).days
        bar = ax.barh(
                task['task_group'] + ': ' + task['task_description'],
                width=duration,
                height=0.6,
                left=task['start_date'],
                color=TASKTYPE_BAR_COLORS.get(task['task_status'], BAR_COLOR)
        )
    
    ax.plot(mdates.date2num(datetime.datetime.fromisoformat(TODAY))*np.array([1, 1]),
             ax.get_ylim(),'k--')

    week_positions, week_labels = build_week_ticks(start_date, end_date)

    ax.set_title(TITLE,
          fontsize=TITLE_SIZE, color=FONT_COLOR).set_fontweight(TITLE_FONT_WEIGHT)
    ax.set_xlabel(X_LABEL, fontsize=LABEL_SIZE, color=FONT_COLOR)
    ax.set_ylabel(Y_LABEL, fontsize=LABEL_SIZE, color=FONT_COLOR)
    ax.tick_params(axis='both', colors=FONT_COLOR)
    ax.set_xticks(week_positions)
    ax.set_xticklabels(week_labels, fontsize=DAY_FONT_SIZE, 
                        color=FONT_COLOR)
    ax.grid(axis='x', linestyle='--', alpha=0.4)

    sec_ax = ax.secondary_xaxis('bottom')
    sec_ax.xaxis.set_major_formatter(mdates.DateFormatter('%b. %y'))
    sec_ax.xaxis.set_major_locator(mdates.MonthLocator())
    sec_ax.tick_params(axis='x', labelsize=MONTH_FONT_SIZE, 
                        colors=FONT_COLOR)
    sec_ax.spines['bottom'].set_position(('outward', 20))

    # Monatslinie
    for label in sec_ax.get_xticklabels():
        label.set_fontsize(MONTH_FONT_SIZE)
        label.set_weight(MONTH_FONT_WEIGHT)
        label.set_color(FONT_COLOR)
   
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
        sec_ax.spines[spine].set_visible(False)

 # Legende
    handles = []
    for task_statuss, color in TASKTYPE_BAR_COLORS.items():
        patch = mpatches.Patch(color=color, label=task_statuss)
        handles.append(patch)

    ax.legend(handles=handles, loc='best', framealpha=0.8)

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        plt.show()

tl = pd.DataFrame(columns=('task_group', 'task_description', 'task_status', 
                                'start_date', 'end_date'))
tl.loc[0] =["Tiefbau","Blumen umbetten","Abgebrochen","2025-06-14","2025-06-19"]
tl.loc[len(tl)]=["Tiefbau",  "Grube graben", "Abgeschlossen", "2025-06-19", "2025-06-30"]
tl.loc[len(tl)]=["Bauseits",  "Fundamentgraben erstellen", "Abgeschlossen", 
                 "2025-07-01", "2025-07-04"]
tl.loc[len(tl)]=["Bauseits",  "Streifenfundament giessen", "Abgeschlossen",
                  "2025-07-04", "2025-07-06"]
tl.loc[len(tl)]=["Bauseits",  "GaLa-Bau beauftragen", "Verspaetet", 
                 "2025-07-10", "2025-07-14"]
tl.loc[len(tl)]=["Bauseits",  "Mauersteine legen", "Abgeschlossen",
                  "2025-07-06", "2025-07-16"]
tl.loc[len(tl)]=["Betonbauer",  "Mauer betonieren", "Im Plan",
                  "2025-07-16", "2025-07-20"]
tl.loc[len(tl)]=["GaLa-Bau",  "Teichfolie auslegen", "Im Plan", 
                 "2025-07-20", "2025-07-22"]
tl.loc[len(tl)]=["Bauseits",  "Drainage aufbauen", "Im Plan", 
                 "2025-07-22", "2025-07-24"]
tl.loc[len(tl)]=["Bauseits",  "Kies einfuellen", "Im Plan",
                  "2025-07-24", "2025-07-28"]
tl.loc[len(tl)]=["Bauseits",  "Wasser einlassen", "In Vorbereitung",
                  "2025-07-30", "2025-08-10"]
print(tl)
tl['start_date'] = pd.to_datetime(tl['start_date'], format=DATE_FORMAT)
tl['end_date'] = pd.to_datetime(tl['end_date'], format=DATE_FORMAT)
tl.set_index(pd.DatetimeIndex(tl['start_date'].values), inplace=True)
plot_gantt(tl)
