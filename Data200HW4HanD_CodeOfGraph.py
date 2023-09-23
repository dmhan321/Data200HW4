import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd



# Streamlit App
st.title("Visualizations of Mountain Flowers")

data = pd.read_csv(r"mountain_flowers.csv")
df = pd.DataFrame(data)

# Graph 1: Scatter plot
st.subheader("1: Scatter Plot")

df_Colorado_lotus = df[df['name'] == 'Colorado lotus']
fig, ax = plt.subplots()
ax.scatter(df_Colorado_lotus['petal_length'], df_Colorado_lotus['petal_width'])
plt.xlabel('petal_length')
plt.ylabel('Petal_width')
plt.title('petal_length and Petal_width of Colorado lotus')
st.pyplot(fig)

st.write("""Observation:  according to the graph above, there is no significant 
correlation between the petal_length and petal_width in Colorado lotus.""")


# Graph: Bar Chart
st.subheader("2: Bar Chart")
# group the dataframe by column 'name' and calculate mean, 
# and then reset index, the old index ('name') is added as a column. 
df1 = df.groupby('name').mean().reset_index()

fig, ax = plt.subplots()
ax.bar(df1['name'], height = df1['petal_length'])

#add labels and title
plt.xlabel("Name of flowers")
plt.ylabel("Average petal length")
plt.title("Average petal length by flower")
plt.xticks(rotation = 30) # rotate xticks to avoild overlap.

st.pyplot(fig)

st.write("""Observation: according to the graph above, 
         the Colorado lotus has the longest petal length 
         and the violet has the shortest petal length.""")

# Visualize dataframe:
st.subheader("Detailed Data View")
st.dataframe(df)
