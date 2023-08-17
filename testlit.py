import streamlit as st

st.text('Fixed width text')


# Show a spinner during a process
with st.spinner(text='In progress'):
  st.success('Done')

# Show and update progress bar
bar = st.progress(50)
bar.progress(100)

st.balloons()
st.snow()
st.toast('Mr Stay-Puft')
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
