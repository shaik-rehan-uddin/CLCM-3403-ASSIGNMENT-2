import streamlit as st
from streamlit_option_menu import option_menu
from data_handler import add_task
from view_tasks import view_tasks


# Main function to run the Streamlit app
def main():
    st.title("Task Management App")

    menu_options = ["Add Task", "View Tasks"]

    if st.session_state.get("add_task", False):
        st.session_state["menu_option"] = 1
        print(st.session_state)
        manual_select = st.session_state["menu_option"]
    else:
        manual_select = None

    navbar = option_menu(
        None,
        menu_options,
        icons=["file-earmark-plus-fill", "card-checklist"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        manual_select=manual_select,
        key="nav_bar",
    )
    navbar

    if navbar == "Add Task":
        name = st.text_input("Task Name")
        description = st.text_area("Task Description")
        priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        due_date = st.date_input("Due Date")
        if st.button("Add Task", key="add_task"):
            add_task(name, description, priority, due_date)
            st.success("Task added successfully!")

    elif navbar == "View Tasks":
        view_tasks()


if __name__ == "__main__":
    main()
