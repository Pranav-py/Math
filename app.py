# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 15:51:40 2022

@author: pranav.reddy
"""

import streamlit as st
import random



#Page
st.title('What is ')
col1, col2 = st.columns(2)

#Sidebar choice
choice_d=st.sidebar.radio('Select decimals', (0,1,2))
choice_o=st.sidebar.radio('Select arithmetic',('+','-','/','*','%'))

#Generate Random numbers
rand_nos=[(random.randint(1,10)),random.randint(1,10)]
rand_decimal=[round(random.uniform(0,1),2),round(random.uniform(0,1),2)]
rand_nos=[round(rand_nos[0]+rand_decimal[0],choice_d),round(rand_nos[1]+rand_decimal[1],choice_d)]


#Create ans & score in session
if 'ans' not in st.session_state:
    st.session_state.ans=0
    st.session_state.score=0

#st.write(st.session_state.ans)

# User Question Text & input here 

if choice_o=='/':
    col1.title(str(rand_nos[0])+choice_o+str(round(rand_nos[1],0)))
else:
    col1.title(str(rand_nos[0])+choice_o+str(rand_nos[1]))




input=col2.number_input('Your ans here')



if st.session_state.ans==input:
    col2.success(str(st.session_state.ans)+' - That\'s correct!')
    st.session_state.score +=1
    col2.success('Your score is '+str(st.session_state.score))
    
else:
    col2.warning('Correct answer is '+str(st.session_state.ans))
    st.session_state.score -=1
    col2.error(st.session_state.score)

if choice_o=='+':
    st.session_state.ans=round(rand_nos[0]+rand_nos[1],2)
elif choice_o=='-':
    st.session_state.ans=round(rand_nos[0]-rand_nos[1],2)
elif choice_o=='/':
    st.session_state.ans=round(rand_nos[0]/round(rand_nos[1],0),2)

input=''


clear=st.button('Clear')
if clear:
    st.session_state.score =0

print(choice_o)
