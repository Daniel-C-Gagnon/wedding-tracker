from datetime import datetime, timezone

class ContributionManager:
    def __init__(self, supabase_client):
        self.supabase_client = supabase_client


    def add_contributions(self, amount, user_id):
        '''

        Add a new savings entry (amount + timestamp) to the contributions table.

        Parameters:
        amount (float): The amount saved.

        Returns:
        dict: Result of the insertion.

        '''

        if amount < 0:
            raise ValueError(f'The amount ${amount} is less than zero. Please enter a valid amount.')

        contribution = {
            'amount': amount,
            'user_id': user_id,
            'date_added': datetime.now(timezone.utc).isoformat()
        }

        self.supabase_client.table("contributions").insert(contribution).execute()

        return f"🚀🚀🚀 Successfully added ${amount:.2f} to your wedding savings! 🚀🚀🚀"


    def get_all_contributions(self):
        '''

        Return all rows from the contributions table.

        '''

        response = self.supabase_client.table("contributions_view").select("*").execute()

        return response.data

    def get_total_savings(self):
        '''

        Use the above method to calculate the total saved and total saved by user

        '''

        rows = self.get_all_contributions()
        total = sum(row['amount'] for row in rows)

        return total

    def add_user(self, uid, display_name):
        '''
        Adds user to the database with their id, display_name and created_at

        '''

        data = {
            'id': uid,
            'display_name': display_name,
            'created_at': datetime.now(timezone.utc).strftime('%Y-%m-%d')
        }

        try:
            self.supabase_client.table("profiles").insert(data).execute()
            return f"🎉 Added user {display_name}!"
        except Exception as e:
            raise ValueError(f'Failed to insert user: {e}')


if __name__ == "__main__":
    from supabase import create_client
    import streamlit as st
    from datetime import timezone, datetime

    supabase = create_client(st.secrets["supabase_url"],
                             st.secrets["supabase_service_key"]
                             )

    cm = ContributionManager(supabase)
    # result = cm.add_contributions(25.00, 123)
    result = cm.add_user('9f3eaf28-319f-459e-9b11-a203b4729f73', 'Adriana')
    print(result)
