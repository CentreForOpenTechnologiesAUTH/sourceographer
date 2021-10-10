import pandas as pd

def get_input_metrics():
    df = pd.read_csv('input_metrics.csv', delimiter = ',')

    effectiveness = df['Effectiveness'].iloc[0]
    testing = df['Testing'].iloc[0]
    coverage = df['Coverage'].iloc[0]
    licensing = df['Licensing'].iloc[0]
    dual_licensing = df['Dual licensing model'].iloc[0]
    commercial_resources = df['Commercial resources'].iloc[0]
    commercial_training = df['Commercial training'].iloc[0]
    industry_adoption = df['Industry adoption'].iloc[0]
    foundation_attached = df['Non profit / Foundation attached'].iloc[0]
    company_attached = df['For profit company attached'].iloc[0]
    donations = df['Donations'].iloc[0]
    governance = df['Governance model'].iloc[0]
    roadmap = df['Project road-map'].iloc[0]
    code_of_conduct = df['Code of conduct'].iloc[0]
    coding_standards = df['Coding standards'].iloc[0]
    documentation_standards = df['Documentation standards'].iloc[0]
    localization = df['Localization Process'].iloc[0]
    user_guide = df['User guide'].iloc[0]

    df_ind = pd.read_csv('indicators.csv', delimiter = ',')

    df_ind['Effectiveness'] = df_ind['Effectiveness'].fillna(effectiveness)
    df_ind['Testing process'] = df_ind['Testing process'].fillna(testing)
    df_ind['Coverage'] = df_ind['Coverage'].fillna(coverage)
    df_ind['License type'] = df_ind['License type'].fillna(licensing)
    df_ind['Dual licensing'] = df_ind['Dual licensing'].fillna(dual_licensing)
    df_ind['Commercial resources'] = df_ind['Commercial resources'].fillna(commercial_resources)
    df_ind['Commercial training'] = df_ind['Commercial training'].fillna(commercial_training)
    df_ind['Industry adoption'] = df_ind['Industry adoption'].fillna(industry_adoption)
    df_ind['Non profit / Foundation support'] = df_ind['Non profit / Foundation support'].fillna(foundation_attached)
    df_ind['For profit company support'] = df_ind['For profit company support'].fillna(company_attached)
    df_ind['Donations'] = df_ind['Donations'].fillna(donations)
    df_ind['Governance model'] = df_ind['Governance model'].fillna(governance)
    df_ind['Project road-map'] = df_ind['Project road-map'].fillna(roadmap)
    df_ind['Code of conduct'] = df_ind['Code of conduct'].fillna(code_of_conduct)
    df_ind['Coding standards'] = df_ind['Coding standards'].fillna(coding_standards)
    df_ind['Documentation standards'] = df_ind['Documentation standards'].fillna(documentation_standards)
    df_ind['Localization process'] = df_ind['Localization process'].fillna(localization)
    df_ind['User guide'] = df_ind['User guide'].fillna(user_guide)

    df_ind.to_csv('indicators.csv', index = False)


if __name__ == '__main__':
    get_input_metrics()