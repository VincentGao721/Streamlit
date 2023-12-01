import streamlit as st
import pandas as pd
import numpy as np 
# markdown 
# st.markdown('Streamlit Demo')

# 设置网页标题
st.title('12.1 实习工作日志 ')

# 展示一级标题
st.header('1. 今日完成')

st.text("继续streamlit的学习")
st.text("学习巩固数据表达形式等相关知识")
code1='''pip install streamlit'''
st.code(code1, language='bash')

st.header('2. 明日计划')

# 展示二级标题
st.subheader('2.1 继续学习streamlit相关知识')

st.text('尝试新的画图方式')

code2 = '''import streamlit as st
st.markdown('Streamlit Demo')'''
st.code(code2, language='python')

df = pd.DataFrame(
    np.random.randn(10,5),
    columns=('第%s列' % (i+1) for i in range(5))
)

st.table(df)

df = pd.DataFrame(
    np.random.randn(10,5),
    columns=('第%s列' % (i+1) for i in range(5))
)

st.dataframe(df.style.highlight_max(axis=0))

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 F", "1.2 F")
col2.metric("Wind", "9 mph", "-8%")
col1.metric("Humidity", "86%", "4%")

#折线图 
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

#面积图 
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a', 'b', 'c']
)

st.area_chart(chart_data)

#柱状图 
chart_data = pd.DataFrame(
    np.random.randn(50,3),
    columns = ['a', 'b', 'c'])
st.bar_chart(chart_data)

#地图
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50,50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df)
