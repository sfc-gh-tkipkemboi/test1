import streamlit as st

def app():
    st.title('Streamlit Live Show YouTube Playlist', 
             anchor=False
    )

    video_ids = [
        '58LClFx3WOY',
        'T_ZmJecsqCs',
        'PLKkudXYCNI',
        'ZwOnB_uRdX0',
        'BfatISexzUo',
        'WHTWO0IMh4w',
        'BPKZkAaHcdI',
        '4rXfdzEVSsY',
        'mAbpqL53pPI'
    ]

    for video_id in video_ids:
        st.video(f'https://www.youtube.com/watch?v={video_id}')
        st.divider()

if __name__ == '__main__':
    app()