def sales_funnel_analysis(df):
    """Analiza la pérdida de usuarios entre páginas 1 y 5."""
    return df['PAGE'].value_counts().sort_index()

def conversion_by_photography_type(df):
    """Compara rendimiento de fotos en face (1) vs profile (2)."""
    return df.groupby('MODEL PHOTOGRAPHY')['ORDER'].count()
