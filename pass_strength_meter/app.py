import streamlit as st
import re
import random
import string

st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

def suggest_strong_password():
    length = 12
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(all_chars) for _ in range(length))

# 🖼️ UI
st.title("🔐 Password Strength Meter")
st.write("Check how secure your password is and get suggestions to improve it.")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)

    st.markdown("### 🔎 Results:")
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
        for tip in feedback:
            st.markdown(tip)
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below:")
        for tip in feedback:
            st.markdown(tip)

    st.markdown("---")
    st.markdown("### 💡 Need help?")
    if st.button("Suggest a Strong Password"):
        st.info("Try this: **" + suggest_strong_password() + "**")
