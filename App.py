import streamlit as st
import math

st.title("✈️ Vertical Speed & Descent Angle Calculator")

with st.form("vsi_form"):
    speed = st.number_input("Current speed (knots):", min_value=1, step=1, format="%d")
    distance = st.number_input("Distance to waypoint (NM):", min_value=1, step=1, format="%d")
    current_alt = st.number_input("Current altitude (ft):", step=1, format="%d")
    target_alt = st.number_input("Target altitude (ft):", step=1, format="%d")
    submit = st.form_submit_button("Calculate VSI & Angle")

if submit:
    altitude_diff = target_alt - current_alt  # + = climb, - = descent
    if altitude_diff == 0:
        st.success("✅ You are already at the target altitude.")
    else:
        # Time to waypoint in minutes
        time_minutes = (distance / speed) * 60
        vsi = altitude_diff / time_minutes  # ft/min (signed)
        vsi_rounded = round(vsi)
        mode = "Climb" if vsi_rounded > 0 else "Descent"

        # Calculate descent/climb angle in degrees
        distance_ft = distance * 6076  # NM → feet
        angle_rad = math.atan2(altitude_diff, distance_ft)
        angle_deg = round(math.degrees(angle_rad), 2)

        st.success(
            f"Required Vertical Speed: {vsi_rounded:+d} ft/min ({mode})\n"
            f"Descent/Climb Angle: {angle_deg}°"
        )
