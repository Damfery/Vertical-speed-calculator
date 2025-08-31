import streamlit as st

st.title("✈️ Vertical Speed Calculator")

# Step-by-step input
speed = st.number_input("Enter current speed (knots):", step=1, format="%d")
distance = st.number_input("Enter distance to waypoint (NM):", step=1, format="%d")
current_alt = st.number_input("Enter current altitude (ft):", step=1, format="%d")
target_alt = st.number_input("Enter target altitude (ft):", step=1, format="%d")

if st.button("Calculate VSI"):
    altitude_to_lose = current_alt - target_alt
    if altitude_to_lose <= 0:
        st.success("✅ No descent needed. You are already at or below target altitude.")
    else:
        time_minutes = (distance / speed) * 60
        vsi = altitude_to_lose / time_minutes
        st.success(f"Required Vertical Speed: **{round(vsi)} ft/min**")
