import instaloader
import streamlit as st
import pandas as pd
import base64

bot = instaloader.Instaloader()
st.header("Instagram Scraper")
user_input = st.text_input("Account(s) : ")


# Retrieve the data concerning the profiles entered by the user

def get_profiles(ig_account):
    data = []
    list_of_users = ig_account.split()
    for i in list_of_users:
        profile = instaloader.Profile.from_username(bot.context, i)
        data += [[profile.username, profile.userid, profile.mediacount, profile.followers, profile.followees]]
    return data


# Create a dataframe using the data previously retrieved

def create_df(data):
    df = pd.DataFrame(data, columns=["username", "user_id", "number_of_posts", "followers", "following"])
    return df


def main():
    if user_input:
        data = get_profiles(user_input)
        dataframe = create_df(data)
        st.write(dataframe)  # Show the dataframe to the user
        download = st.button('Download CSV File')
        if download:
            csv = dataframe.to_csv(index=False)  # Convert the dataframe into a CSV file
            b64 = base64.b64encode(csv.encode()).decode()
            link = f'<a href="data:file/csv;base64,{b64}" download="instagram.csv">Click here to download your file</a>'
            st.markdown(link, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
