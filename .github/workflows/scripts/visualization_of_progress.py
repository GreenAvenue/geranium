from github import Github
import numpy as np
import pandas as pd

# Please set a token.
token = ''

GIT = Github(token)
ORG = 'GreenAvenue'
REPO = 'geranium'

TRGT_COLS = [
    'no',
    'title',
    'assignees',
    'milestone',
    'labels',
    'state',
    'user',
    'created_at',
    'closed_at',
    'closed_by',
    'updated_at'
]

repo = [_repo for _repo in GIT.get_organization(ORG).get_repos(type='public')
           if _repo.name == REPO][0]

proj_cols = ['no', 'project', 'project_status']
df_proj = pd.DataFrame(columns=proj_cols)
projects = repo.get_projects()
for _proj in projects:
    for _proj_col in _proj.get_columns():
        for _card in _proj_col.get_cards():
            issue = _card.get_content()
            if issue is None:
                continue
            df_proj = df_proj.append(pd.Series([issue.number, _proj.name, _proj_col.name],
                                     index=proj_cols,
                                     name=len(df_proj)))

#import sys
#sys.exit(0)

issues = [[_issue.number,
           _issue.title,
           _issue.assignees,
           _issue.milestone,
           _issue.labels,
           _issue.state,
           _issue.user,
           _issue.created_at,
           _issue.closed_at,
           _issue.closed_by,
           _issue.updated_at]
             for _issue in repo.get_issues(state='all')]


def make_col_act_man_hour(x):
    if x is None:
        return None
    man_hour_labels = [float(_label[5:].split('h')[0]) for _label in x.split(';')
                          if '実工数:' in _label]
    if len(man_hour_labels) > 1:
        #TODO: (Future)Error handling.
        pass
    if len(man_hour_labels) == 0:
        return None

    return np.min(man_hour_labels)

def make_col_est_man_hour(x):
    if x is None:
        return None
    man_hour_labels = [float(_label[6:].split('h')[0]) for _label in x.split(';')
                          if '見積工数:' in _label]
    if len(man_hour_labels) != 1:
        #TODO: (Future)Error handling.
        pass
    if len(man_hour_labels) == 0:
        return None

    return np.min(man_hour_labels)

df_issues = pd.DataFrame(issues, columns=TRGT_COLS)
df_issues['assignees'] = df_issues['assignees'].map(lambda x: ';'.join([_x.login for _x in x]))
df_issues['due_on'] = df_issues['milestone'].map(lambda x: None if x is None else x.due_on)
df_issues['milestone'] = df_issues['milestone'].map(lambda x: None if x is None else x.title)
df_issues['labels'] = df_issues['labels'].map(lambda x: ';'.join([_x.name for _x in x]))
df_issues['user'] = df_issues['user'].map(lambda x: None if x is None else x.login)
df_issues['closed_by'] = df_issues['closed_by'].map(lambda x: None if x is None else x.login)
df_issues['actual_man_hour'] = df_issues['labels'].map(make_col_act_man_hour)
df_issues['estimated_man_hour'] = df_issues['labels'].map(make_col_est_man_hour)
df_issues = df_issues.merge(df_proj, on='no', how='left')
df_issues.sort_values('no').to_csv('issues.csv', index=False)
