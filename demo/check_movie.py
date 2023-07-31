import streamlit as st
import base64
import os

def file_to_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.title('修正済み字幕動画確認')

uploaded_video = st.file_uploader("動画ファイルをアップロードしてください (mp4)", type=['mp4'])
uploaded_subtitle = st.file_uploader("字幕ファイルをアップロードしてください (WebVTT)", type=['vtt'])

if uploaded_video is not None and uploaded_subtitle is not None:
    video_file_path = "video.mp4"
    subtitle_file_path = "subtitle.vtt"

    # Save the uploaded files
    with open(video_file_path, "wb") as f:
        f.write(uploaded_video.getbuffer())
    with open(subtitle_file_path, "wb") as f:
        f.write(uploaded_subtitle.getbuffer())
    
    # Convert the files to base64
    video_b64 = file_to_base64(video_file_path)
    subtitle_b64 = file_to_base64(subtitle_file_path)
    
    # Remove the temporary files
    os.remove(video_file_path)
    os.remove(subtitle_file_path)

    # Prepare the HTML
    video_html = f"""
    <video width="100%" height="auto" controls>
      <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
      <track src="data:text/vtt;base64,{subtitle_b64}" kind="subtitles" srclang="ja" label="Japanese">
      Your browser does not support the video tag.
    </video>
    """

    # Display the video
    st.markdown(video_html, unsafe_allow_html=True)
else:
    st.warning("動画ファイルと字幕ファイルをアップロードしてください。")
