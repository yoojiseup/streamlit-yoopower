import streamlit as st
import pandas as pd
# folium 객체를 rendering해줄 streamlit_folium의 folium_static를 받아옵니다.(설치 필요)
from streamlit_folium import folium_static
# 지도 라이브러리 folium을 import 합니다.
import folium
from folium.plugins import MarkerCluster

st.title("제주도에서 가장 핫한 곳은?")

df = pd.read_csv("jeju_place.csv")


# folium의 지도 객체를 받습니다.
m = folium.Map([sum(df["위도"])/len(df["위도"]),sum(df["경도"])/len(df["경도"])],zoom_start=9)
marker_cluster = MarkerCluster().add_to(m)

# 지도위에 위,경도에 점을 찍습니다.
for i, j in zip(df["위도"],df["경도"]):
    folium.CircleMarker(
        [i,j]
    ).add_to(marker_cluster)

# [TODO] 이번에는 st.로 시작하지 않습니다! 지도 m을 folium_static을 이용하여 시각화합니다.
folium_static(m)