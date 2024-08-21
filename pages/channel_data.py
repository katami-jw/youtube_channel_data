import streamlit as st
import pandas as pd

st.title("Youtubeチャンネル調査")
st.write("気になるYouTubeチャンネルのチャンネルIDを入力してチャンネルの情報を見てみましょう")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    channel_data = pd.read_csv(uploaded_file,encoding="Shift-JIS")
    channel_data_dic = channel_data.to_dict(orient='records')
    #st.write(channel_data)

    st.image(channel_data_dic[0]['snippet.thumbnails.medium.url'])
    st.write("チャンネル名▶",channel_data_dic[0]['snippet.title'])
    st.markdown(channel_data_dic[0]['snippet.description'])

    col1, col2, col3 = st.columns(3)
    col1.metric(label="総再生数", value=channel_data_dic[0]['statistics.viewCount'])
    col2.metric(label="動画数", value=channel_data_dic[0]['statistics.videoCount'])
    col3.metric(label="登録者数", value=channel_data_dic[0]['statistics.subscriberCount'])