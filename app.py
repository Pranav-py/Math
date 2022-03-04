# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 15:51:40 2022

@author: pranav.reddy
"""
import pandas as pd
import numpy as np
#import glob
#import datetime
#import winsound 
import streamlit as st
import random
#import time

#import matplotlib.pyplot as plt
#import seaborn as sns
#import plotly_express as px
#import plotly.graph_objects as go
#from plotly.subplots import make_subplots

#from operator import attrgetter
#import matplotlib.colors as mcolors
#import matplotlib.ticker as mticker
#import plotly.figure_factory as ff


#Page
st.title('Heading')

choice=st.sidebar.radio('Select decimals', (0,1,2))


rand_nos=[(random.randint(1,10)),random.randint(1,10)]
rand_decimal=[round(random.uniform(0,1),2),round(random.uniform(0,1),2)]
print(rand_decimal)


rand_nos=[round(rand_nos[0]+rand_decimal[0],choice),round(rand_nos[1]+rand_decimal[1],choice)]

print(rand_nos)

if 'ans' not in st.session_state:
    st.session_state.ans=0
    st.session_state.score=0

#st.write(st.session_state.ans)

st.header(str(rand_nos[0])+'+'+str(rand_nos[1]))


input=st.number_input('Your ans here',value=0)
#check=st.button('Check')
#if check:
#   st.write(st.session_state.ans)
#input=float(input)

#st.session_state.ans=float(st.session_state.ans)


#st.write(str(st.session_state.ans==input))

if st.session_state.ans==input:
    st.success(str(st.session_state.ans)+' - That\'s correct!')
    st.session_state.score +=1
    st.success('Your score is '+str(st.session_state.score))
    
else:
    st.warning('Correct answer is '+str(st.session_state.ans))
    st.session_state.score -=1
    st.error(st.session_state.score)

st.session_state.ans=round(rand_nos[0]+rand_nos[1],2)


clear=st.button('Clear')
if clear:
    st.session_state.score =0

