import streamlit as st

# สร้างหัวเรื่อง
st.title("Hello, Streamlit!")

# สร้างข้อความ
st.write("ยินดีต้อนรับสู่แอปพลิเคชันแรกของคุณ")

# สร้าง input เพื่อรับข้อมูลจากผู้ใช้
user_input = st.text_input("กรุณากรอกชื่อของคุณ:")

if user_input:
    st.write(f"สวัสดี {user_input}!")
