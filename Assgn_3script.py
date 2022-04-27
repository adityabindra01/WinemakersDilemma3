from numpy import dsplit
import streamlit as st


# Whenever sensi or speci go below 0.5, the model reaches breakeven

st.title('Winemakers Dilemma - Part 3')

st.text('Name: Aditya Bindra | Andrew ID: adityabi')

P_hsugar = st.slider('Chance of high sugar', step=2, value=10)
P_typsug = st.slider('Chance of typical sugar', step=2, value=30)
P_no_sugar = st.slider('Chance of no usgar', step=2, value=60)
P_mold = st.slider('Chance of botrytis', step=2, value=10)

P_ds = 0.76* ((P_mold/100)*3300000 + 0.9*420000) + 0.24* ((P_no_sugar/100)*960000 + (P_typsug/100)*1410000 + (P_hsugar/100)*1500000) 
P_dns = 0.75* ((P_no_sugar/100)*960000 + (P_typsug/100)*1410000 + (P_hsugar/100)*1500000) + 0.25*((P_mold/100)*3300000 + 0.9*420000)
cv_calc = 0.34* (P_ds) + 0.66* (P_dns)


if (P_no_sugar + P_typsug + P_hsugar) > 100:
    st.error("Error: total chance can't be over 100%")


st.success(f'EV = {cv_calc}')

if(cv_calc > 960000): 
    st.success('Recommended Alternative: Buy Clairvoyance')
else:
    st.success('Recommended Alternative: No Clairvoyance')