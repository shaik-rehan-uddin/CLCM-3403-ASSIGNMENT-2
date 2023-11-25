import streamlit as st
from datetime import datetime
from data_handler import load_tasks, edit_task, remove_task


# Function to display tasks as a table
def view_tasks():
    tasks = load_tasks()
    st.header("Task List")

    if not tasks:
        st.write("No tasks available.")

    else:
        # Create a table with column headers
        table_data = []
        for index, task in enumerate(tasks):
            table_data.append(
                [task["name"], task["description"], task["priority"], task["due_date"]]
            )

        cols = st.columns((2, 2.5, 1.5, 2, 2, 2))
        headers = [
            "Name",
            "Description",
            "Priority",
            "Due Date",
            "Edit Task",
            "Delete Task",
        ]
        for col, header in zip(cols, headers):
            col.write("**" + header + "**")

        for index, row in enumerate(table_data):
            col1, col2, col3, col4, col5, col6 = st.columns((2, 2.5, 1.5, 2, 2, 2))

            col1.write(row[0])
            col2.write(row[1])
            col3.write(row[2])
            col4.write(row[3])
            if col5.button(f"Edit", key=f"Edit Task {index + 1}"):
                st.session_state.edit_index = index
                st.experimental_rerun()

            if col6.button("Delete", key=f"Remove Task {index + 1}"):
                remove_task(index)
                st.success("Task removed successfully!")
                st.experimental_rerun()

    if "edit_index" in st.session_state:
        index = st.session_state.edit_index
        if index < len(tasks):
            st.header("Edit Task")
            edited_name = st.text_input("Task Name", tasks[index]["name"])
            edited_description = st.text_area(
                "Task Description", tasks[index]["description"]
            )
            edited_priority = st.selectbox(
                "Priority",
                ("Low", "Medium", "High"),
                index=["Low", "Medium", "High"].index(tasks[index]["priority"]),
            )
            edited_due_date = st.date_input(
                "Due Date",
                datetime.strptime(tasks[index]["due_date"], "%Y-%m-%d"),
            )

            if st.button("Save Changes"):
                edit_task(
                    index,
                    edited_name,
                    edited_description,
                    edited_priority,
                    edited_due_date,
                )
                st.session_state.pop("edit_index")
                st.experimental_rerun()
