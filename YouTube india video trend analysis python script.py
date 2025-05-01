#!/usr/bin/env python
# coding: utf-8

# In[66]:


# Reading the data from the path from my local machine
import pandas as pd

# Example path to your CSV file (update this to your actual path)
file_path = r"D:\Information Technology\Youtube tranding data anlysis\Youtube_indian_video_trend\INvideos.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Preview the data
df.head()


# In[67]:


# Get the shape and info
df.shape
df.info()

# See missing values
df.isnull().sum()

# Check for duplicates
df.duplicated().sum()


# In[68]:


df.describe()


# In[69]:


df.drop(columns=['description'], inplace=True)
df.drop(columns=['tags'], inplace=True)
df.columns


# In[74]:


df.isnull().sum()


# In[76]:


df.duplicated().sum()


# In[78]:


# Loop through each column and check for duplicated values
for col in df.columns:
    num_duplicates = df[col].duplicated().sum()
    if num_duplicates > 0:
        print(f"'{col}' has {num_duplicates} duplicated values")


# In[82]:


# Convert 'trending_date' to datetime format
df['trending_date'] = pd.to_datetime(df['trending_date'], format='%y.%d.%m', errors='coerce')
print(df['trending_date'].dtypes)
print(df['trending_date'].head())


# In[84]:


# Total views per day

daily_views = df.groupby('trending_date')['views'].sum().reset_index()

# Sort by date
daily_views = daily_views.sort_values('trending_date')

#Ploting to see the trand

import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.plot(daily_views['trending_date'], daily_views['views'], marker='o', linestyle='-')
plt.title('Total Trending Views Over Time')
plt.xlabel('Trending Date')
plt.ylabel('Total Views')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[88]:


# This plot is for average weekly rolling trands

daily_views['rolling_views'] = daily_views['views'].rolling(window=7).mean()

plt.figure(figsize=(12, 6))
plt.plot(daily_views['trending_date'], daily_views['rolling_views'], color='red')
plt.title('7-Day Rolling Average of Trending Views')
plt.xlabel('Trending Date')
plt.ylabel('Views')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[126]:


top_videos = df.groupby('video_id')['views'].max().sort_values(ascending=False).head(5)
top_video_ids = top_videos.index.tolist()

top_df = df[df['video_id'].isin(top_video_ids)]

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.figure(figsize=(13, 4))

# Plot each video’s views over time
for vid in top_video_ids:
    video_data = top_df[top_df['video_id'] == vid].sort_values('trending_date')
    plt.plot(video_data['trending_date'], video_data['views'], label=video_data['title'].iloc[0][:50])

plt.title('Top 5 Trending Videos – Views Growth Over Time')
plt.xlabel('Trending Date')
plt.ylabel('Views (in Millions)')
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x/1e6:.1f}M'))

plt.legend(title='Video Title', loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()
plt.show()


# In[104]:


top_videos = df.groupby('title')['views'].max().sort_values(ascending=False).head(5)
top_video_ids = top_videos.index.tolist()
top_video_ids


# In[112]:


top_videos = df.groupby('title')['views'].max().sort_values(ascending=False).head(5)

# Convert views to millions and format

top_videos_in_million = top_videos / 1e6

top_videos_in_million = top_videos_in_million.apply(lambda x: f"{x:.2f}M")

# Print the million indexing value

print(top_videos_in_million.reset_index())


# In[146]:


# Group by channel title and get max-views for each channel 

top_channels = df.groupby('channel_title')['views'].max().sort_values(ascending=False).head(5)

# Convert views to millions and format

top_channels_in_million = top_channels / 1e6

top_channels_in_million = top_channels_in_million.apply(lambda x: f"{x:.2f}M")

# Display the top channels and their max views in millions

print(top_channels_in_million.reset_index())


# In[150]:


top_video_titles = top_videos.index.tolist()
top_video_titles


# In[152]:


# Analyze the first video

video_title = top_video_titles[0]  # Change index 0 to 1, 2, 3, 4 for others
single_video_df = df[df['title'] == video_title].sort_values('trending_date')

plt.figure(figsize=(10, 6))
plt.plot(single_video_df['trending_date'], single_video_df['views'] / 1e6, marker='o')

# Add labels and title

plt.title(f"Daily View Trend: '{video_title}'")
plt.xlabel('Trending Date')
plt.ylabel('Views (in Millions)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:




