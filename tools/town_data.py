"""Checked town facts for longislandhomes.co, kept apart from the page layout.

Every figure names its source. Refresh monthly (see CONTENT-CALENDAR.md).
Fair housing: facts about places only, never about who lives there.
"""

HOME = "https://bisendramelaram.com"

GTFS_LABEL = "LIRR GTFS schedule feed, version GO202_26, published November 6, 2026"
GTFS_URL = "https://rrgtfsfeeds.s3.amazonaws.com/gtfslirr.zip"
SAMPLE_DAY = "Wednesday, November 11, 2026"

# Weekday morning peak, trains arriving 7:00 to 9:30 AM, direct trains only (no change at Jamaica).
# (station, branch, Penn: trains, min-max minutes, median; Grand Central Madison: same)
RAIL = {
    "valley-stream": [
        ("Valley Stream", "Long Beach and Far Rockaway", (6, "31 to 39", "34"), (5, "31 to 35", "32")),
        ("Gibson", "Far Rockaway", (2, "36 to 41", None), (2, "39", None)),
    ],
    "lynbrook": [("Lynbrook", "Long Beach and Babylon", (6, "34 to 42", "36"), (4, "34 to 35", "35"))],
    "rockville-centre": [("Rockville Centre", "Babylon", (7, "34 to 38", "36"), (4, "36 to 40", "37"))],
    "oceanside": [("Oceanside", "Long Beach", (4, "41 to 49", "43.5"), (3, "41 to 42", "42"))],
    "baldwin": [("Baldwin", "Babylon", (7, "37 to 41", "39"), (4, "39 to 43", "40"))],
    "freeport": [("Freeport", "Babylon", (7, "40 to 45", "42"), (4, "42 to 46", "43"))],
}

# American Community Survey 2020 to 2024 five-year estimates, via Census Reporter (checked Nov 2026).
# (housing units, median value of owner-occupied homes as estimated by owners, Census Reporter profile)
CENSUS = {
    "valley-stream": (12957, 616100, "https://censusreporter.org/profiles/16000US3676705-valley-stream-ny/"),
    "lynbrook": (7507, 611900, "https://censusreporter.org/profiles/16000US3643874-lynbrook-ny/"),
    "rockville-centre": (10332, 818700, "https://censusreporter.org/profiles/16000US3663264-rockville-centre-ny/"),
    "oceanside": (11328, 634300, "https://censusreporter.org/profiles/16000US3654441-oceanside-ny/"),
    "baldwin": (11190, 593800, "https://censusreporter.org/profiles/16000US3604143-baldwin-ny/"),
    "freeport": (14793, 505900, "https://censusreporter.org/profiles/16000US3627485-freeport-ny/"),
}

# Official district sites, each opened and checked in November 2026. None means not linked yet.
D = {
    "VS13": ("Valley Stream Union Free School District 13", "https://www.valleystream13.com/"),
    "VS24": ("Valley Stream Union Free School District 24", None),
    "VS30": ("Valley Stream Union Free School District 30", "https://www.valleystream30.com/"),
    "VSC": ("Valley Stream Central High School District", "https://www.vschsd.org/"),
    "HW": ("Hewlett-Woodmere Union Free School District", None),
    "LYN": ("Lynbrook Public Schools", "https://www.lynbrookschools.org/"),
    "ER": ("East Rockaway Union Free School District", None),
    "MAL": ("Malverne Union Free School District", None),
    "RVC": ("Rockville Centre Union Free School District", "https://www.rvcschools.org/"),
    "OCS": ("Oceanside Union Free School District", "https://www.oceansideschools.org/"),
    "BAL": ("Baldwin Union Free School District", "https://www.baldwinschools.org/"),
    "ROO": ("Roosevelt Union Free School District", None),
    "UNI": ("Uniondale Union Free School District", None),
    "FPT": ("Freeport Public Schools", "https://www.freeportschools.org/"),
}
DISTRICTS = {
    "valley-stream": ["VS13", "VS24", "VS30", "VSC", "HW"],
    "lynbrook": ["LYN", "ER", "HW", "MAL", "VSC"],
    "rockville-centre": ["RVC", "OCS", "BAL"],
    "oceanside": ["OCS"],
    "baldwin": ["BAL", "OCS", "RVC", "ROO", "UNI"],
    "freeport": ["FPT"],
}
DISTRICT_NOTE = {
    "lynbrook": "The Valley Stream districts that serve part of Lynbrook include the Valley Stream Central High School District. Ask the district which elementary district serves a given street.",
}

# One local point each for sellers and buyers, drawn from the town's own facts above.
SELLER_POINT = {
    "valley-stream": "Name the right district. Three elementary districts and part of Hewlett-Woodmere serve the village, and the disclosure form asks you which one serves your home.",
    "lynbrook": "Name the right district. Five districts serve parts of the village, and the disclosure form asks you which one serves your home.",
    "rockville-centre": "Have your village electric bills ready. The village runs its own electric department, and buyers will ask what power costs.",
    "oceanside": "Expect flood questions first. Sandy flooded the southern part of the hamlet in 2012, so have your flood insurance policy, any elevation certificate and your claims history ready.",
    "baldwin": "Know your district and your flood zone. Most of Baldwin is in the Baldwin district, but small parts are in four others, and the hamlet runs between two creeks.",
    "freeport": "Have your flood papers and village electric bills ready. Freeport is a canal village with its own electric utility, and buyers ask about both.",
}
BUYER_POINT = {
    "valley-stream": "Two stations serve the village. Valley Stream station has the faster direct morning trains, and Gibson has fewer.",
    "lynbrook": "Lynbrook station has both Long Beach and Babylon Branch trains, so check which branch your train runs on before you rely on it.",
    "rockville-centre": "Check the district before you fall for the house. About a fifth of residents are in the Oceanside district, not Rockville Centre's.",
    "oceanside": "Get a flood insurance quote before you sign. Oceanside has the longest direct morning ride of these six towns, a median 43.5 minutes to Penn Station.",
    "baldwin": "Baldwin is a hamlet, so there is no village tax, and permits and zoning go through the Town of Hempstead.",
    "freeport": "Freeport is the largest of these six towns, with the most housing units, and it has the lowest owner-estimated median home value of the six in Census figures.",
}

EXTRA_SRC = {
    "gtfs": (GTFS_LABEL, GTFS_URL),
    "hempstead_tax": ("Town of Hempstead Receiver of Taxes, tax payment schedule", "https://hempsteadny.gov/381/Tax-Payment-Schedule"),
    "arc": ("Nassau County Assessment Review Commission, filing an appeal", "https://www.nassaucountyny.gov/arc"),
    "lrv": ("Nassau County LandRecord Lookup, property assessment records", "https://lrv.nassaucountyny.gov/"),
    "dtf_newbuyers": ("NYS Department of Taxation and Finance, Assessments and property taxes for new homebuyers (updated May 14, 2026)",
                      "https://www.tax.ny.gov/pit/property/new-homebuyers/"),
    "fema_risk": ("FEMA, flood risk for homeowners and renters (updated November 4, 2020)",
                  "https://www.fema.gov/flood-maps/products-tools/know-your-risk/homeowners-renters"),
    "rpl462": ("New York Real Property Law section 462, property condition disclosure statement (NY State Senate)",
               "https://www.nysenate.gov/legislation/laws/RPP/462"),
    "nar_settlement": ("National Association of REALTORS, What the NAR settlement means for home buyers and sellers (updated May 24, 2024)",
                       "https://www.nar.realtor/the-facts/what-the-nar-settlement-means-for-home-buyers-and-sellers"),
    "dtf_transfer": ("NYS Department of Taxation and Finance, Real estate transfer tax", "https://www.tax.ny.gov/bus/transfer/rptidx.htm"),
    "courts_dies": ("New York State Unified Court System, When someone dies", "https://nycourts.gov/courthelp/WhenSomeoneDies"),
    "rpapl1304": ("New York RPAPL section 1304, 90-day pre-foreclosure notice (NY State Senate)",
                  "https://www.nysenate.gov/legislation/laws/RPA/1304"),
}
for _s, (_u, _v, _url) in CENSUS.items():
    EXTRA_SRC[f"census_{_s}"] = ("Census Reporter, American Community Survey 2020 to 2024 five-year estimates", _url)

# Seller guides on bisendramelaram.com that every town page links to.
SELLER_GUIDES = [
    ("How to price a home in Nassau County", f"{HOME}/sellers/pricing/"),
    ("What it costs to sell on Long Island", f"{HOME}/sellers/cost-to-sell/"),
    ("When to list a South Shore home", f"{HOME}/sellers/best-time-to-sell/"),
    ("New York's property condition disclosure", f"{HOME}/sellers/property-condition-disclosure/"),
    ("Nassau property taxes and grievances", f"{HOME}/sellers/property-taxes/"),
    ("How Bisendra sells a home", f"{HOME}/how-i-sell-a-home/"),
]

# Glossary: (term, definition, source key or None). Plain definitions drawn from the sources above.
GLOSSARY = [
    ("Incorporated village", "A municipality inside a New York town with its own elected government, building department and village tax. Valley Stream, Lynbrook, Rockville Centre and Freeport are incorporated villages in the Town of Hempstead.", None),
    ("Hamlet", "An unincorporated community with no village government. Zoning, permits and town services come from the town. Oceanside and Baldwin are hamlets in the Town of Hempstead.", None),
    ("Town of Hempstead", "The Nassau County town that contains all six South Shore communities in these guides. Its Receiver of Taxes collects school and general property taxes.", "hempstead_tax"),
    ("Special flood hazard area", "FEMA's high-risk flood zone, often called the 100-year floodplain, with a 1 percent chance of flooding in any year. Mortgages on homes in it can require flood insurance.", "fema"),
    ("Moderate flood hazard area", "FEMA's moderate-risk zone, often called the 500-year floodplain, with a 0.2 percent chance of flooding in any year.", "fema"),
    ("Elevation certificate", "A document from a licensed surveyor or engineer that records a building's elevation against expected flood levels. Insurers can use it to rate flood insurance, and New York's disclosure form asks whether one exists.", "nysba"),
    ("Property condition disclosure statement", "The form New York sellers of most one to four family homes must give buyers before the buyer signs a contract. Since March 20, 2024 it cannot be replaced by a $500 credit, and it includes flood questions.", "rpl462"),
    ("Assessment Review Commission (ARC)", "The Nassau County agency that hears property assessment appeals, often called grievances. The next filing window runs January 4 to March 1, 2027.", "arc"),
    ("AROW", "Assessment Review On the Web, ARC's online system for filing a Nassau County assessment appeal.", "arc"),
    ("Level of assessment", "The share of market value a county uses for assessed value. Nassau County's is 0.1 percent, so assessed value is the county's market value estimate divided by 1,000.", "lrv"),
    ("STAR credit", "New York's School Tax Relief benefit for a primary residence. New owners register for the STAR credit with the state tax department once the home is their primary residence.", "dtf_newbuyers"),
    ("Real estate transfer tax", "New York's tax on a sale of real property: $2 for each $500 of the price, paid by the seller by default.", "dtf_transfer"),
    ("Mansion tax", "An extra 1 percent New York tax on residences sold for $1 million or more, paid by the buyer.", "dtf_transfer"),
    ("Union free school district", "A form of New York public school district, often shortened to UFSD. On the South Shore district lines do not follow village or hamlet lines.", None),
    ("Grand Central Madison", "The LIRR terminal under Grand Central Terminal in Manhattan, the second Manhattan destination besides Penn Station.", "mta_lb"),
    ("Direct train", "In these guides, a train that reaches Penn Station or Grand Central Madison without a change at Jamaica.", "gtfs"),
    ("Closed sale", "A sale that has gone to closing, with the deed transferred. Closed sales show what buyers actually paid, unlike asking prices.", "onekey_page"),
    ("Days on market", "In OneKey MLS reports, days on market until sale: how long the homes that sold were on the market.", "onekey"),
    ("Percent of original list price received", "The sale price divided by the first list price, as OneKey MLS reports it. Above 100 percent means homes sold above their original asking price.", "onekey"),
    ("Buyer agreement", "A written agreement between a buyer and their agent. Since August 17, 2024, agents who are REALTORS need one before touring a home with a buyer.", "nar_settlement"),
    ("Surrogate's Court", "The New York court that handles estates, including probate and administration, which give an executor or administrator authority to sell a home.", "courts_dies"),
    ("90-day pre-foreclosure notice", "The notice New York lenders must send a homeowner at least 90 days before starting a foreclosure on a home loan.", "rpapl1304"),
]
