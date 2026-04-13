import streamlit as st

st.title("📚 Articles by Giorgio BUONANO")
search_query = st.text_input("Search your article here")

articles = [
    {
        #"Title": "Building and Environment",
        "Category": "Building & Environment",
        "Links": [
            {"name": "Design and preliminary experimental assessment of a personalized air-cleaning system for transport microenvironments _15 April 2026", "url": "https://doi.org/10.1016/j.buildenv.2026.114390"},
            {"name": "Emission rates of particle-bound heavy metals and polycyclic aromatic hydrocarbons in PM fractions from indoor combustion sources_1 November 2024", "url": "https://doi.org/10.1016/j.buildenv.2024.112033"},
            {"name": "Effect of bedroom environment on sleep and physiological parameters for individuals with good sleep quality: A pilot study_1 November 2024", "url": "https://doi.org/10.1016/j.buildenv.2024.111994"},
            {"name": "A simplified approach to evaluate the lung cancer risk related to airborne particles emitted by indoor sources _15 October 2021", "url": "https://doi.org/10.1016/j.buildenv.2021.108143"},
            {"name": "The effect of the ventilation retrofit in a school on CO2, airborne particles, and energy consumptions_June 2019", "url": "https://doi.org/10.1016/j.buildenv.2019.04.001"},
            {"name": "Airborne particle emission rates and doses received in operating rooms from surgical smoke_15 March 2019", "url": "https://doi.org/10.1016/j.buildenv.2019.01.044"},
            {"name": "A simplified benchmark of ultrafine particle dispersion in idealized urban street canyons: A wind tunnel study_November 2015", "url": "https://doi.org/10.1016/j.buildenv.2015.05.045"},
            {"name": "Characteristics of particles and black carbon emitted by combustion of incenses, candles and anti-mosquito products_October 2012", "url": "https://doi.org/10.1016/j.buildenv.2015.05.045"},
            {"name": "A simplified benchmark of ultrafine particle dispersion in idealized urban street canyons: A wind tunnel study_November 2015", "url": "https://doi.org/10.1016/j.buildenv.2015.05.045"},
        ]
    },
    {
        "Title": "The Science of The Total Environment",
        "Category": "The Science of The Total Environment",
        "Links": [
            {"name": "Editor's Note to Particle-related exposure, dose and lung cancer risk of primary school children in two European countries_20 February 2026", "url": "https://doi.org/10.1016/j.scitotenv.2026.181507"},
            {"name": "Close proximity risk assessment for SARS-CoV-2 infection_10 November 2021", "url": "https://doi.org/10.1016/j.scitotenv.2021.148749"},
            {"name": "Effect of ventilation strategies and air purifiers on the children's exposure to airborne particles and gaseous pollutants in school gyms_10 April 2020", "url": "https://doi.org/10.1016/j.scitotenv.2019.135673"},
            {"name": "A novel approach to evaluate the lung cancer risk of airborne particles emitted in a city_15 March 2019", "url": "https://doi.org/10.1016/j.scitotenv.2018.11.432"},
            {"name": "Effectiveness of commercial face masks to reduce personal PM exposure_10 February 2019", "url": "https://doi.org/10.1016/j.scitotenv.2018.09.109"},
            {"name": "Lung cancer risk assessment due to traffic-generated particles exposure in urban street canyons: A numerical modelling approach_1 August 2018", "url": "https://doi.org/10.1016/j.scitotenv.2018.03.093"},
            {"name": "Particle-related exposure, dose and lung cancer risk of primary school children in two European countries_March 2018", "url": "https://doi.org/10.1016/j.scitotenv.2017.10.256"},
            {"name": "Do air quality targets really represent safe limits for lung cancer risk", "url": "https://doi.org/10.1016/j.scitotenv2016.11.216"},
            {"name": "Charged particles and cluster ions produced during cooking activities", "url": "https://doi.org/10.1016/j.scitotenv.2014.08.011"},
            
            
        ]
    },
    {
        "Title": "Environment International",
        "Category": "Environment International",
        "Links": [
            {"name": "Quantitative assessment of the risk of airborne transmission of SARS-CoV-2 infection: Prospective and retrospective applications_December 2020", "url": "https://doi.org/10.1016/j.envint.2020.106112"},
            {"name": "How can airborne transmission of COVID-19 indoors be minimised?_September 2020", "url": "https://doi.org/10.1016/j.envint.2020.105832"},
            {"name": "Estimation of airborne viral emission: Quanta emission rate of SARS-CoV-2 for infection risk assessment_August 2020", "url": "https://doi.org/10.1016/j.envint.2020.105794"},
            {"name": "Estimated health impacts from maritime transport in the Mediterranean region and benefits from the use of cleaner fuels_May 2020", "url": "https://doi.org/10.1016/j.envint.2020.105670"},
            {"name": "Airborne particles in indoor environment of homes, schools, offices and aged care facilities: The main routes of exposure_November 2017", "url": "https://doi.org/10.1016/j.envint.2017.07.025"},
            {"name": "Children's well-being at schools: Impact of climatic conditions and air pollution_September 2016", "url": "https://doi.org/10.1016/j.envint.2016.05.009"},
            {"name": "Airborne particles in indoor environment of homes, schools, offices and aged care facilities: The main routes of exposure_November 2017", "url": "https://doi.org/10.1016/j.envint.2017.07.025"},



            
        ]
    },

    {
    "Title": "Environmental pollution",
    "Category": "Environmental pollution",
    "Links": [
        {"name": "Characterization of airborne particles emitted by an electrically heated tobacco smoking system_September 2018", "url": "https://doi.org/10.1016/j.envpol.2018.04.137"},
        {"name": "Indoor exposure to particles emitted by biomass-burning heating systems and evaluation of dose and lung cancer risk received by population_April 2018", "url": "https://doi.org/10.1016/j.envpol.2017.12.055"},
        {"name": "The influence of lifestyle on airborne particle surface area doses received by different Western populations_January 2018", "url": "https://doi.org/10.1016/j.envpol.2017.09.023"},
        {"name": "The influence of lifestyle on airborne particle surface area doses received by different Western populations_January 2018", "url": "https://doi.org/10.1016/j.envpol.2017.09.023"},
    

    ]
},

    {
    "Title": "Environmental pollution",
    "Category": "Environmental pollution",
    "Links": [
        {"name": "Characterization of airborne particles emitted by an electrically heated tobacco smoking system_September 2018", "url": "https://doi.org/10.1016/j.envpol.2018.04.137"},
        {"name": "Indoor exposure to particles emitted by biomass-burning heating systems and evaluation of dose and lung cancer risk received by population_April 2018", "url": "https://doi.org/10.1016/j.envpol.2017.12.055"},
        {"name": "The influence of lifestyle on airborne particle surface area doses received by different Western populations_January 2018", "url": "https://doi.org/10.1016/j.envpol.2017.09.023"},
        {"name": "The influence of lifestyle on airborne particle surface area doses received by different Western populations_January 2018", "url": "https://doi.org/10.1016/j.envpol.2017.09.023"}
    ]
}
# Sidebar categories
categories = ["All"] + sorted({article["Category"] for article in articles})
selected_category = st.sidebar.radio("📂 Select Category", categories)

# Filter articles by category
if selected_category == "All":
    filtered_articles = articles
else:
    filtered_articles = [a for a in articles if a["Category"] == selected_category]

# Filter by search query
if search_query:
    filtered_articles = [a for a in filtered_articles if search_query.lower() in a["Title"].lower()]

    



 # Display articles grouped by category
categories = sorted({a["Category"] for a in filtered_articles})

for category in categories:
    st.markdown(f"### 🏛️ {category}")  # show category once

    for article in filtered_articles:
        if article["Category"] == category:
            for link in article["Links"]:
                # Everything inside the for loop MUST be indented
                col1, col2 = st.columns([4, 1])

                with col1:
                    # Add a bullet or emoji before article name
                    st.write("📚 " + link["name"])

                with col2:
                    st.link_button("🔗 View", link["url"])

    st.divider()

    # Filter by search query
if search_query:
    filtered_articles = [
        a for a in filtered_articles
        if (
            search_query.lower() in a.get("Title", "").lower()  # safe access to Title
            or any(search_query.lower() in link["name"].lower() for link in a["Links"])  # search in link names
        )
    ]

 import qrcode

# Your deployed Streamlit URL
url = "https://your-app-name.streamlit.app"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(url)
qr.make(fit=True)

# Create an image file
img = qr.make_image(fill='black', back_color='white')
img.save("streamlit_qr.png")
