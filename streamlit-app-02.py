import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import seaborn as sns
import matplotlib.pyplot as plt

titanic_df = pd.read_csv('titanic.csv')


def data_preview():
    # components.html(f"""<div style='font-size:20px'><b><u>Previewing Titanic Dataset</u></b></div>""")
    st.title("Previewing Titanic Dataset")
    top_n_rows = st.selectbox("Select top n rows to view", (10, 50, 100, 200))
    st.dataframe(titanic_df.head(top_n_rows))
    st.title("Description of the dataset")
    st.write(titanic_df.describe())
    st.write("There are " + str(titanic_df.shape[0]) + " observations in the dataset")
    st.write("There are " + str(titanic_df.shape[1]) + " features in the dataset")


def data_exploration():
    global fig, axs
    st.title("Exploratory Data Analysis")
    left_column, right_column = st.columns(2)
    no_of_dead = titanic_df['Survived'].value_counts()[0]
    no_of_survived = titanic_df['Survived'].value_counts()[1]
    percent_of_survival = no_of_survived / titanic_df.shape[0] * 100
    percent_of_dead = no_of_dead / titanic_df.shape[0] * 100
    plt.figure(figsize=(10, 8))
    sns.countplot(titanic_df['Survived'])
    plt.xlabel('Passenger Survival', size=15, labelpad=15)
    plt.ylabel('Number of Passengers', size=15, labelpad=15)
    plt.xticks((0, 1), ['Dead ({0:.2f}%)'.format(percent_of_dead), 'Survived ({0:.2f}%)'.format(percent_of_survival)])
    plt.tick_params(axis='x', labelsize=13)
    plt.tick_params(axis='y', labelsize=13)
    plt.title('Distribution of Passenger Survival', size=15, y=1.05)
    with left_column:
        # st.write("Passenger Survival")
        st.pyplot(plt)
    plt.figure(figsize=(10, 8))
    sns.heatmap(titanic_df.drop(['PassengerId'], axis=1).corr(), annot=True, square=True, cmap='coolwarm',
                annot_kws={'size': 14})
    plt.tick_params(axis='x', labelsize=13)
    plt.tick_params(axis='y', labelsize=13)
    plt.title('Feature Correlation', size=15, y=1.05)
    with right_column:
        # st.write("Correlation")
        st.pyplot(plt)
    cont_features = ['Age', 'Fare']
    surv = titanic_df['Survived'] == 1
    fig, axs = plt.subplots(ncols=2, nrows=1, figsize=(10, 8))
    plt.subplots_adjust(right=1.5)
    for i, feature in enumerate(cont_features):
        print(i)
        # Distribution of survival in feature
        sns.distplot(titanic_df[~surv][feature], label='Not Survived', hist=True, color='#e74c3c', ax=axs[i])
        sns.distplot(titanic_df[surv][feature], label='Survived', hist=True, color='#2ecc71', ax=axs[i])

        # # Distribution of feature in dataset
        # sns.distplot(titanic_df[feature], label='Training Set', hist=False, color='#e74c3c', ax=axs[1][i])
        # sns.distplot(titanic_df[feature], label='Test Set', hist=False, color='#2ecc71', ax=axs[1][i])

        axs[i].set_xlabel('')
        axs[i].set_xlabel('')

        for j in range(1):
            axs[j].tick_params(axis='x', labelsize=20)
            axs[j].tick_params(axis='y', labelsize=20)

        axs[i].legend(loc='upper right', prop={'size': 20})
        # axs[1][i].legend(loc='upper right', prop={'size': 20})
        axs[i].set_title('Distribution of Survival in {}'.format(feature), size=15, y=1.05)
    # axs[1][0].set_title('Distribution of {} Feature'.format('Age'), size=20, y=1.05)
    # axs[1][1].set_title('Distribution of {} Feature'.format('Fare'), size=20, y=1.05)
    st.pyplot(plt)


def feature_engineer():
    global fig, axs
    st.title("Feature Engineering")
    titanic_df['Fare'] = pd.qcut(titanic_df['Fare'], 13)
    fig, axs = plt.subplots(figsize=(22, 9))
    sns.countplot(x='Fare', hue='Survived', data=titanic_df)
    plt.xlabel('Fare', size=15, labelpad=20)
    plt.ylabel('Passenger Count', size=15, labelpad=20)
    plt.tick_params(axis='x', labelsize=10)
    plt.tick_params(axis='y', labelsize=15)
    plt.legend(['Not Survived', 'Survived'], loc='upper right', prop={'size': 15})
    plt.title('Count of Survival in {} Feature'.format('Fare'), size=15, y=1.05)
    st.pyplot(plt)


if __name__ == "__main__":
    section = st.sidebar.radio("Sections", ("Data Preview", "Data Exploration", "Feature Engineering"))
    if section == "Data Preview":
        data_preview()
    if section == "Data Exploration":
        data_exploration()
    if section == "Feature Engineering":
        feature_engineer()
