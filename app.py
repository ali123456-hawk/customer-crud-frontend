import streamlit as st
from api import get_customers, create_customer, update_customer, delete_customer

st.title("Customer CRUD System")

menu = ["Create", "View", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

# CREATE
if choice == "Create":
    st.subheader("Add Customer")

    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    if st.button("Create"):
        res = create_customer({
            "name": name,
            "email": email,
            "phone": phone
        })
        st.success(res)

# VIEW
elif choice == "View":
    st.subheader("All Customers")
    customers = get_customers()
    st.write(customers)

# UPDATE
elif choice == "Update":
    st.subheader("Update Customer")

    cid = st.number_input("Customer ID", min_value=1)
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    if st.button("Update"):
        res = update_customer(cid, {
            "name": name,
            "email": email,
            "phone": phone
        })
        st.success(res)

# DELETE
elif choice == "Delete":
    st.subheader("Delete Customer")

    cid = st.number_input("Customer ID", min_value=1)

    if st.button("Delete"):
        res = delete_customer(cid)
        st.success(res)