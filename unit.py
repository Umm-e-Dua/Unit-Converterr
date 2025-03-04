import streamlit as st


st.title("🌍 Unit Converter App")
st.markdown("### Converts Length, Weight, and Time Instantly")
st.write("✨ Welcome! Convert any unit easily ✨ 📌 Select a category & get instant results.")


categories = st.selectbox("Choose a Category", ["Length", "Weight", "Time"])


length_units = ["Kilometers to Miles", "Miles to Kilometers"]

weight_units = ["Kilograms to Pounds", "Pounds to Kilograms"]

time_units = ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", 
              "Hours to Minutes", "Hours to Days", "Days to Hours"]


def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60 
        elif unit == "Minutes to Seconds":
            return value * 60  
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return None

if categories == "Length":
    unit = st.selectbox("📏 Select Conversion", length_units)
elif categories == "Weight":
    unit = st.selectbox("⚖ Select Conversion", weight_units)
elif categories == "Time":
    unit = st.selectbox("⏳ Select Conversion", time_units)


value = st.number_input("🔢 Enter Value to Convert:", min_value=0.0, format="%.2f")


if st.button("Convert"):
    result = convert_units(categories, value, unit)
    if result is not None:
        st.success(f"✅ The result is: {result:.2f}")
   