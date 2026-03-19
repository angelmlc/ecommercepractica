def calculate_conversion_rate(df):
    """Compara clics en categoría sale (4) vs categorías regulares."""
    sale_clicks = len(df[df['PAGE 1 (MAIN CATEGORY)'] == 4])
    regular_clicks = len(df[df['PAGE 1 (MAIN CATEGORY)'].isin([1, 2, 3])])
    return {"sale_clicks": sale_clicks, "regular_clicks": regular_clicks}

def identify_session_depth(df):
    """Encuentra las sesiones con mayor número de clics."""
    return df.groupby('SESSION ID')['ORDER'].max().sort_values(ascending=False)
