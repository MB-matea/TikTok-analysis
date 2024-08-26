import streamlit as st
import pandas as pd
from api import get_data
import plotly.express as px
import plotly.graph_objects as go
from st_aggrid import AgGrid, JsCode, GridOptionsBuilder
import ast

# Set the page layout to wide for better visual space
st.set_page_config(layout='wide')

# Create a sidebar with a logo and instructions
st.sidebar.markdown("<img src='https://static.vecteezy.com/system/resources/previews/023/986/561/non_2x/tiktok-logo-tiktok-logo-transparent-tiktok-icon-transparent-free-free-png.png' width=100 /> <h1 style='display:inline-block'>TikTok analiza</h1>", unsafe_allow_html=True)
st.sidebar.markdown("Analiziraj tiktok videozapise")
st.sidebar.markdown("<ol><li>Unesi <i>hashtag</i> koji želiš analizirati</li> <li>Klikni <i>Pretraži</i>.</li>", unsafe_allow_html=True)

# Input field for the hashtag
hashtag = st.text_input('Unesi hashtag koji želiš analizirati', value="")

# Button to trigger the search
if st.button('Pretraži'):
    # Display header with the searched hashtag
    st.header(f'Rezultati za: {hashtag}')
    # Call the get_data function to fetch data
    get_data(hashtag)

    # Load in existing data to test it out
    df = pd.read_csv('tiktokdata.csv')

    # Create a clickable link for each video
    df['video_link'] = df.apply(lambda row: f"https://www.tiktok.com/@{row['username']}/video/{row['id']}", axis=1)
    # Render links as HTML in Streamlit
    df['video_link'] = df['video_link'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')

    # Remove unnecessary columns from the DataFrame
    df_new = df.drop(columns=['create_time', 'music_id', 'id'])
    # Sort the DataFrame by view count in descending order
    df_new = df_new.sort_values(by=['view_count'], ascending=False)

    # Define the desired column order
    desired_order = ['username', 'video_link', 'view_count', 'like_count', 'comment_count', 'share_count', 'hashtag_names','video_description', 'region_code']

    # Reorganize columns according to the desired order
    df_new = df_new[desired_order]

    # Rename columns to be more descriptive (in the local language)
    df_new = df_new.rename(columns={
        'username': 'Korisničko ime',
        'video_link': 'Link na video',
        'view_count': 'Broj pregleda',
        'like_count': 'Broj lajkova',
        'comment_count': 'Broj komentara',
        'share_count': 'Broj dijeljenja',
        'hashtag_names': 'Hashtagovi',
        'video_description': 'Opis videa',
        'region_code': 'Država'
    })

    # Convert the hashtag lists from string representation to actual lists
    df_new['Hashtagovi'] = df_new['Hashtagovi'].apply(lambda x: ', '.join(ast.literal_eval(x)) if isinstance(x, str) else x)

    # Apply CSS to format the table appearance
    st.markdown("""
        <style>
        .dataframe {
            width: 100%;
            max-height: 500px;  /* Set maximum height for vertical scroll */
            margin-left: auto;
            margin-right: auto;
            overflow-x: auto;  /* Enable horizontal scroll */
            overflow-y: auto;  /* Enable vertical scroll */
            display: block;
        }
        .dataframe th {
            position: sticky;
            top: 0;
            background-color: white;
            z-index: 1;
            text-align: left;
            padding: 10px;
        }
        .dataframe td {
            text-align: left;
            padding: 10px;
            max-width: 500px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Display the table in the app
    st.header('TikTok - podaci')
    st.write(df_new.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Chart 1 - Create a scatter plot to show video engagement stats
    st.header('Angažman')
    scatter1 = px.scatter(df, x='share_count', y='comment_count', hover_data=['username'], size='comment_count', color='like_count', labels={
        'share_count': 'Broj dijeljenja',  
        'comment_count': 'Broj komentara',
        'like_count': 'Broj lajkova',
        'username': 'Korisničko ime'
    })
    
    st.plotly_chart(scatter1, use_container_width=True)


    # Chart 2 - Create a bar chart to visualize engagement by region
    st.header('Angažman prema regijama')
    engagement_by_region = df.groupby('region_code').agg({
        'like_count': 'sum',
        'view_count': 'sum',
        'comment_count': 'sum'
    }).reset_index()

    fig_region = go.Figure(data=[
        go.Bar(name='Lajkovi', x=engagement_by_region['region_code'], y=engagement_by_region['like_count'], marker_color='lightblue'),
        go.Bar(name='Pregledi', x=engagement_by_region['region_code'], y=engagement_by_region['view_count'], marker_color='lightgreen'),
        go.Bar(name='Komentari', x=engagement_by_region['region_code'], y=engagement_by_region['comment_count'], marker_color='lightcoral')
    ])

    fig_region.update_layout(barmode='group', xaxis_title='Država', yaxis_title='Angažman')
    st.plotly_chart(fig_region, use_container_width=True, log_y=True)

    # Function to safely extract hashtags from strings
    def extract_hashtags(hashtag_list_str):
        hashtags = ast.literal_eval(hashtag_list_str)
        return hashtags if isinstance(hashtags, list) else []

    df['hashtags'] = df['hashtag_names'].apply(extract_hashtags)

    # Flatten the list of hashtags, excluding the searched hashtag
    all_hashtags = [ht for sublist in df['hashtags'] for ht in sublist if ht.lower() != hashtag.lower()]

    # Count occurrences of each hashtag
    hashtag_counts = pd.Series(all_hashtags).value_counts()

    # Chart 3 - Create a bar chart to show the top 10 hashtags excluding the searched one
    st.header(f'Top 10 hashtagova uz "{hashtag}"')
    # Plotting the top 10 hashtags excluding the searched one
    if not hashtag_counts.empty:
        top_10_hashtags = hashtag_counts.head(10)
        
        fig_hashtags = px.bar(
            x=top_10_hashtags.values, 
            y=top_10_hashtags.index, 
            orientation='h', 
            labels={'x': 'Broj videozapisa', 'y': 'Hashtag'},

        )
        st.plotly_chart(fig_hashtags, use_container_width=True)
    else:
        st.write(f"Nije pronađeno drugih hashtagova osim '{hashtag}'")
    

    
    