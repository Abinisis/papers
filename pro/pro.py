import streamlit as st
from PIL import Image, ImageDraw

# ---- circular image ----
import os
from PIL import Image

BASE_DIR = os.path.dirname(__file__)
img_path = os.path.join(BASE_DIR, "photo.jpg")

img = Image.open(img_path).convert("RGBA")
st.image(img, width=120)

# ---- HEADER (bigger + slightly left) ----
st.markdown(
    """
    <div style="
        text-align: left;
        font-size: 34px;
        font-weight: 700;
        margin-left: 40px;
        margin-bottom: 0px;
        letter-spacing: 1px;
    ">
    📚 ARTICLES & PAPERS
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<div style='width:80px;height:3px;background:#999;margin:6px 0 20px 40px;'></div>",
    unsafe_allow_html=True
)

# ---- IMAGE + AUTHOR ----
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(make_circle("photo.jpg"), width=120)
    st.caption("by G. Buonano")

search_query = st.text_input("Search your article here")

articles = [
    {
        #"Title": "BUILDING & ENVIRONMENT",
        "Category": "BUILDING & ENVIRONMENT",
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
        "Title": "THE SCIENCE OF THE TOTAL ENVIRONMENT",
        "Category": "THE SCIENCE OF THE TOTAL ENVIRONMENT",
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
        "Title": "ENVIRONMENT INTERNATIONAL",
        "Category": "ENVIRONMENT INTERNATIONAL",
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
    "Title": "SIENTIFIC REPORTS",
    "Category": "SIENTIFIC REPORTS",
    "Links": [
        {"name": "Size-segregated content of heavy metals and polycyclic aromatic hydrocarbons in airborne particles emitted by indoor sources_05 September 2024", "url": "https://doi.org/10.1038/s41598-024-70978-3?urlappend=%3Futm_source%3Dresearchgate.net%26utm_medium%3Darticle"},
        {"name": "Indoor exposure to particles emitted by biomass-burning heating systems and evaluation of dose and lung cancer risk received by population_April 2018", "url": "https://doi.org/10.1016/j.envpol.2017.12.055"},
        {"name": "The influence of lifestyle on airborne particle surface area doses received by different Western populations_January 2018", "url": "https://doi.org/10.1016/j.envpol.2017.09.023"},
        {"name": "The influence of lifestyle on airborne particle surface area doses received by different Western populations_January 2018", "url": "https://doi.org/10.1016/j.envpol.2017.09.023"}
    ]
},
{
    "Title": "ENVIRONMENTAL POLLUTION",
    "Category": "ENVIRONMENTAL POLLUTION",
    "Links": [
        {"name": "Characterization of airborne particles emitted by an electrically heated tobacco smoking system_September 2018", "url": "https://doi.org/10.1016/j.envpol.2018.04.137"},
        {"name": "Indoor exposure to particles emitted by biomass-burning heating systems and evaluation of dose and lung cancer risk received by population_April 2018", "url": "https://doi.org/10.1016/j.envpol.2017.12.055"},
        {"name": "The influence of lifestyle on airborne particle surface area doses received by different Western populations_January 2018", "url": "https://doi.org/10.1016/j.envpol.2017.09.023"},
        {"name": "The influence of lifestyle on airborne particle surface area doses received by different Western populations_January 2018", "url": "https://doi.org/10.1016/j.envpol.2017.09.023"}
    ]
},

{
    "Title": "OTHERS ",
    "Category": "OTHERS ",
    "Links": [
        {"name": "Link between SARS-CoV-2 emissions and airborne concentrations: closing the gap in understanding_6 Oct 2021", "url": "https://doi.org/10.48550/arXiv.2110.02706"},
        {"name": "Practical Indicators for Risk of Airborne Transmission in Shared Indoor Environments and their Application to COVID-19 Outbreaks_september 28, 2021.", "url": "https://doi.org/10.1101/2021.04.21.21255898"},
        {"name": "Lung Cancer Risk of a Population Exposed to Airborne Particles: The Contribution of Different Activities and Microenvironments_2019", "url": "https://doi.org/10.1201/9780429055959-8"},
        {"name": "Stabile, 2014 AOH_2014", "url": "https://www.researchgate.net/publication/282325115_Stabile_2014_AOH"},
        {"name": "Manigrasso, e-cig lobes asimmetry_ september 2015", "url": "https://www.researchgate.net/publication/282324937_Manigrasso_2015_e-cig_lobes_asimmetry"},
        {"name": "Manigrasso,_ september 2015", "url": "https://www.researchgate.net/publication/282324766_Manigrasso_2015_e-cig_lobes_asimmetry"},
        {"name": "Airborne exposure of hairdressers during hair bleaching: A human chamber exposure study_ january 2014", "url": "https://www.researchgate.net/publication/289022240_Airborne_exposure_of_hairdressers_during_hair_bleaching_A_human_chamber_exposure_study"},
        {"name": "Numerical analysis of particle exposure mitigation in cooking activities through a residential ceiling hood,_January 2012", "url": "https://www.researchgate.net/publication/288554744_Numerical_analysis_of_particle_exposure_mitigation_in_cooking_activities_through_a_residential_ceiling_hood"},
        {"name": "Measurement of cooking-generated particle charge_january 2014", "url": "https://www.researchgate.net/publication/287434053_Measurement_of_cooking-generated_particle_charge"},
        {"name": "Ultrafine particle size distribution during high velocity impact of high density metals_ Jun 2011", "url": "https://doi.org/10.1063/1.3686233"},
        {"name": "Direct and indirect measurement of WBGT index in transversal flow_january 2009", "url": "https://www.researchgate.net/publication/288554744_Numerical_analysis_of_particle_exposure_mitigation_in_cooking_activities_through_a_residential_ceiling_hood"},
        {"name": "Characterization of the imgc-dh100l pressure balance using finite element analysis_January 2008", "url": "https://www.researchgate.net/publication/283605736_Characterization_of_the_imgc-dh100l_pressure_balance_using_finite_element_analysis"},


    ]
},

{
    "Title": "JOURNALS", 
    "Category": "JOURNALS",
    "Links": [
        {"name": "A Eulerian-Lagrangian approach for the CFD analysis of airborne disease transmission in a car cabin_ June2021", "url": "https://doi.org/10.1088/1742-6596/2177/1/012015"},
        {"name": "A novel approach for the numerical analysis of waste-to-energy plants_June 2019.", "url": "https://doi.org/10.1088/1742-6596/1599/1/012025"},
        {"name": "Particle and Carbon Dioxide Concentration Levels in a Surgical Room Conditioned with a Window/Wall Air-Conditioning System_13 February 2020", "url": "https://doi.org/10.3390/ijerph17041180"},
        {"name": "Effect of indoor-generated airborne particles on radon progeny dynamics_15 August 2016", "url": "https://doi.org/10.1016/j.jhazmat.2016.04.051"},
        {"name": "A70 Air pollution and city travel: choices in commuter exposure to inhalable particulates_june 2015", "url": "https://doi.org/10.1016/j.jth.2015.04.558"},
        {"name": "Individual exposure of women to fine and coarse PM_ April 2015", "url": "https://doi.org/10.30638/eemj.2015.092"},
        {"name": "Estimation of inhaled ultrafine particle surface area dose for urban environments_ November 2014", "url": "https://doi.org/10.21914/anziamj.v55i0.7819"},
        {"name": "Ultrafine particle generation by high-velocity impact of metal projectiles _ may 2014", "url": "https://doi.org/10.1088/1742-6596/500/18/182018"},
        {"name": "NSAM-derived total surface area versus SMPS-derived “mobility equivalent” surface area for different environmentally relevant aerosols_ December 2013", "url": "https://doi.org/10.1016/j.jaerosci.2013.08.003"},
        {"name": "Individual exposure of women to fine and coarse PM_ April 2015", "url": "https://doi.org/10.30638/eemj.2015.092"},
        {"name": "Ultrafine particle emission from incinerators: The role of the fabric filter_January 2012", "url": "https://doi.org/10.1080/10473289.2011.636501"},


    ]
},
{
    "Title": "CONFERENCE", 
    "Category": "CONFERENCE",
    "Links": [
        {"name": "Correlation of pedestrian exposure to atmospheric aerosol in urban areas in relation to anthropogenic pressures by means of Geographic Information System (GIS)_April 2015", "url": "https://www.researchgate.net/publication/274070927_Correlazione_dell'esposizione_dei_pedoni_all'aerosol_atmosferico_in_aree_urbane_in_relazione_alle_pressioni_antropiche_mediante_Geographic_Information_System_GIS"},
        {"name": "Numerical assessment of human particle exposure from cooking activities_July 2014.", "url": "https://www.researchgate.net/publication/276061742_Numerical_assessment_of_human_particle_exposure_from_cooking_activities"},
        {"name": "The effects of ultrafine particles from traffic emissions on children's health (UPTECH): Preliminary results from three Italian schools_july 2012", "url": "https://www.researchgate.net/publication/263673495_The_effects_of_ultrafine_particles_from_traffic_emissions_on_children's_health_UPTECH_Preliminary_results_from_three_Italian_schools"},
        {"name": "The influence of the uncertainty on monitoring stack emissions in a waste-to-energy plant_may 2008", "url": "https://doi.org/10.1109/IMTC.2008.4547331"},
        {"name": "A70 Air pollution and city travel: choices in commuter exposure to inhalable particulates_june 2015", "url": "https://doi.org/10.1016/j.jth.2015.04.558"},
    ]
}
]

# Sidebar categories
categories = ["All"] + sorted({article["Category"] for article in articles})
selected_category = st.sidebar.radio(" 🏛️Select Category", categories)

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

