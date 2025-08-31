import streamlit as st

st.title("✈️ Vertical Speed Calculator")

with st.form("vsi_form"):
    speed = st.number_input("Current speed (knots):", min_value=1, step=1, format="%d")
    distance = st.number_input("Distance to waypoint (NM):", min_value=1, step=1, format="%d")
    current_alt = st.number_input("Current altitude (ft):", step=1, format="%d")
    target_alt = st.number_input("Target altitude (ft):", step=1, format="%d")
    submit = st.form_submit_button("Calculate VSI")

if submit:
    altitude_diff = target_alt - current_alt  # + = climb, - = descent
    if altitude_diff == 0:
        st.success("✅ You are already at the target altitude.")
    else:
        # time to waypoint in minutes
        time_minutes = (distance / speed) * 60
        vsi = altitude_diff / time_minutes  # ft/min (signed)
        vsi_rounded = round(vsi)
        mode = "Climb" if vsi_rounded > 0 else "Descent"
        st.success(f"Required Vertical Speed: {vsi_rounded:+d} ft/min ({mode})")
