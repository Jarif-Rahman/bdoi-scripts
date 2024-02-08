#!/usr/bin/env python 

import sys

from cmscontrib.AddTeam import add_team

# Create teams
team = {
    "Class 7": "class7",
    "Class 8": "class8",
    "Class 9": "class9",
    "Class 10": "class10",
    "Class 11": "class11", 
    "Class 12/HSC 2024": "hsc", 
    "SSC 2024 Candidates": "ssc", 
    "Others": "others"
}

for name, code in team.items(): 
    add_team(code, name)
