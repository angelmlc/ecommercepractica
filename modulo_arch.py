def get_country_name(df):
    """Mapea códigos numéricos a nombres de países."""
    mapping = {
        1: "Australia", 2: "Austria", 3: "Belgium",
        12: "unidentified", 29: "Poland",
        41: "United Kingdom", 42: "USA", 44: "com"
    }
    df['COUNTRY_NAME'] = df['COUNTRY'].map(mapping)
    return df

def clean_currency_data(df):
    """Valida que los precios sean positivos y no nulos."""
    df = df.dropna(subset=['PRICE'])
    df = df[df['PRICE'] > 0]
    return df

def segment_by_period(df, mes_inicio=4, mes_fin=8):
    """Filtra el DataFrame por rango de meses (4-8)."""
    return df[(df['MONTH'] >= mes_inicio) & (df['MONTH'] <= mes_fin)]
