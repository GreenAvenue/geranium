import gantt
from datetime import date, datetime, timedelta, timezone
import pandas as pd


df = pd.read_csv('~/issues.csv')

df = df.loc[:, ['no', 'type', 'title', 'assignees',
                'state', 'created_at', 'due_on',
                'project', 'project_status']]
df = df[(df['type'] == 'Issue')
      & (df['state'] != 'closed')]
df['created_at'] = pd.to_datetime(df['created_at'])
df['due_on'] = pd.to_datetime(df['due_on'])
df = df.sort_values('due_on').reset_index(drop=True)


FILENAME = 'geranium_open_tasks'

task_list = list()
gantt_master_project = gantt.Project(name='Gantt chart')

gantt_map = {}
for _proj in df['project'].unique():
    gantt_map.setdefault(_proj, gantt.Project(name=_proj))

assignee_color_map = {
    'ma3-ndbox': '#98fb98',
    'rothr4': '#ffdead',
    'hizakozo': '#afeeee'
}

for no, title, assignees, created_at, proj, due_on in df.loc[:, ['no', 'title', 'assignees', 'created_at', 'project', 'due_on']].itertuples(False):
    duration = 1 if pd.isna(due_on) else (due_on - created_at).days

    assignee_list = [gantt.Resource(_user) for _user in assignees.split(';')]
    tasks = gantt.Task(
                name='#{0}: {1}'.format(no, title),
                start=created_at,
                duration=duration,
                percent_done=0,
                resources=assignee_list,
                color=assignee_color_map.get(assignees.split(';')[0], '#d8bfd8')
            )
    gantt_map[proj].add_task(tasks)

gantt.define_font_attributes(
    fill='black',
    stroke='black',
    stroke_width=0,
    font_family='Verdana'
)

today = datetime.now(timezone(timedelta(hours=9)))
start = pd.to_datetime(df['created_at'].min()-timedelta(days=7))
end = pd.to_datetime(df['due_on'].max()+timedelta(days=14))

for _sub_proj in gantt_map.keys():
    gantt_master_project.add_task(gantt_map[_sub_proj])

gantt_master_project.make_svg_for_tasks(
    filename=FILENAME+'.svg',
    today=datetime(today.year, today.month, today.day),
    start=datetime(start.year, start.month, start.day),
    end=datetime(end.year, end.month, end.day)
)
