# Everything works as intended. Obviously I don't my server info public so I left placeholders
import mysql.connector
from mysql.connector import Error

def connect_database():
    """Establishes connection to the database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',          # Update with your host
            user='your_username',      # Update with your username
            password='your_password',  # Update with your password
            database='gym_db'          # Update with your database name
        )
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Task 1: Add a Member
def add_member(member_id, name, age):
    """Add a new member to the Members table."""
    conn = connect_database()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            values = (member_id, name, age)
            cursor.execute(query, values)
            conn.commit()
            print("Member added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# Task 2: Add a Workout Session
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    """Add a new workout session to the WorkoutSessions table."""
    conn = connect_database()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
            values = (member_id, date, duration_minutes, calories_burned)
            cursor.execute(query, values)
            conn.commit()
            print("Workout session added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# Task 3: Updating Member Information
def update_member_age(member_id, new_age):
    """Update the age of a member."""
    conn = connect_database()
    if conn:
        try:
            cursor = conn.cursor()
            # Check if member exists
            cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
            if cursor.fetchone():
                query = "UPDATE Members SET age = %s WHERE id = %s"
                cursor.execute(query, (new_age, member_id))
                conn.commit()
                print("Member age updated successfully.")
            else:
                print("Member ID does not exist.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    """Delete a workout session based on its session ID."""
    conn = connect_database()
    if conn:
        try:
            cursor = conn.cursor()
            # Check if session exists
            cursor.execute("SELECT * FROM WorkoutSessions WHERE id = %s", (session_id,))
            if cursor.fetchone():
                query = "DELETE FROM WorkoutSessions WHERE id = %s"
                cursor.execute(query, (session_id,))
                conn.commit()
                print("Workout session deleted successfully.")
            else:
                print("Session ID does not exist.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# Advanced Data Analysis

# Task 1: SQL BETWEEN Usage
def get_members_in_age_range(start_age, end_age):
    """Retrieve members whose ages fall between the specified range."""
    conn = connect_database()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"
            cursor.execute(query, (start_age, end_age))
            results = cursor.fetchall()
            for row in results:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# Example calls to test the functions
if __name__ == "__main__":
    # Add a member
    add_member(1, 'Carol', 28)
    
    # Add a workout session
    add_workout_session(1, '2024-09-14', 45, 400)
    
    # Update a member's age
    update_member_age(1, 29)
    
    # Delete a workout session
    delete_workout_session(1)
    
    # Retrieve members in age range
    get_members_in_age_range(25, 30)