import streamlit as st

st.text('Fixed width text')

"""
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

"""

# Show a spinner during a process
with st.spinner(text='In progress'):
  time.sleep(3)
  st.success('Done')

# Show and update progress bar
bar = st.progress(50)
time.sleep(3)
bar.progress(100)

st.balloons()
st.snow()
st.toast('Mr Stay-Puft')
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
st.exception(e)
