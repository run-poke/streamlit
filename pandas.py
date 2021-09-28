

import streamlit as st
import pandas as pd


def main():

    st.table(pd.DataFrame({
        'first column': [10, 20, 30, 40],
        'second column': [100, 200, 300, 400]
    }))


if __name__ == '__main__':
    main()
