PROJECT_ID = "sales-de-pipeline-project"

ENV = "dev"  # ganti ke "prod" kalau mau deploy

DATASET = {
    "raw": f"raw_{ENV}",
    "stg": f"stg_{ENV}",
    "mart": f"mart_{ENV}"
}

RAW_DATASET = DATASET["raw"]

SOURCES = {
    "sales_detail": "https://docs.google.com/spreadsheets/d/14OM6iglE_o7fpyI0KcKcOVWH0pWV_1ml_19VnsyTDvE/export?format=csv&gid=695686821",
    "customer_info": "https://docs.google.com/spreadsheets/d/14OM6iglE_o7fpyI0KcKcOVWH0pWV_1ml_19VnsyTDvE/export?format=csv&gid=1449212302",
    "product_info": "https://docs.google.com/spreadsheets/d/14OM6iglE_o7fpyI0KcKcOVWH0pWV_1ml_19VnsyTDvE/export?format=csv&gid=1841070731",
    "customer_segment": "https://docs.google.com/spreadsheets/d/14OM6iglE_o7fpyI0KcKcOVWH0pWV_1ml_19VnsyTDvE/export?format=csv&gid=155929925",
    "customer_country": "https://docs.google.com/spreadsheets/d/14OM6iglE_o7fpyI0KcKcOVWH0pWV_1ml_19VnsyTDvE/export?format=csv&gid=568052554",
    "product_detail": "https://docs.google.com/spreadsheets/d/14OM6iglE_o7fpyI0KcKcOVWH0pWV_1ml_19VnsyTDvE/export?format=csv&gid=1299566569"
}
