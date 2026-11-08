#!/usr/bin/env python3
"""Builds longislandhomes.co into ../site as plain static HTML.

Edit the content below, then run:  python3 tools/build.py
Cloudflare Pages serves the /site folder as is (no build command).

Rules for this site:
- Only state local facts you can cite. Put the source in the town's SOURCES.
- Never describe a town by who lives there (fair housing). Facts about
  places only: commute, flood, schools, taxes, housing stock, rules.
- Refresh market numbers monthly and change UPDATED.
"""
import json
import os
import shutil
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
STATIC = os.path.join(ROOT, "tools", "static")

DOMAIN = "https://longislandhomes.co"
HOME = "https://bisendramelaram.com"
# Keep False until the [To fill] placeholders are done. While False, every
# page tells search engines not to index it yet. Flip to True to launch.
LAUNCH = False

UPDATED = "2026-11-08"
UPDATED_TEXT = "November 8, 2026"
CHECKED_TEXT = "November 2026"

NAME = "Bisendra Melaram"
LICENSE = "Licensed Real Estate Salesperson"
BROKERAGE = "Keller Williams Greater Nassau"
STREET = "400 Garden City Plaza, Suite 438"
CITY, REGION, ZIP = "Garden City", "NY", "11530"
OFFICE = "516-873-7100"
OFFICE_TEL = "+1-516-873-7100"
CANONICAL = (f"{NAME}, {LICENSE} with {BROKERAGE} in Garden City, NY, "
             "licensed since 2003 and holder of the SRES designation.")

PERSON_ID = f"{HOME}/#person"


def todo(text):
    """Visible placeholder. Search the site for 'todo' before launch."""
    return f'<span class="todo">[To fill: {escape(text)}]</span>'


# Shared sources
SRC = {
    "onekey": ("OneKey MLS, Local Market Update, Nassau County, September 2026",
               "https://corporate.onekeymls.com/s/NassauCounty-t8fn.pdf"),
    "onekey_page": ("OneKey MLS, market statistics", "https://corporate.onekeymls.com/market-statistics"),
    "fema": ("FEMA Flood Map Service Center, search by address", "https://msc.fema.gov/portal/search"),
    "nysba": ("New York State Bar Association, new disclosure and flood rules, March 20, 2024",
              "https://nysba.org/breaking-news-new-rules-on-property-condition-disclosure-and-flood-risk-go-into-effect-today/"),
    "mta_lb": ("MTA, Long Beach Branch service to Grand Central (archived February 2023 notice)",
               "https://mta.info/agency/long-island-rail-road/lirr-to-grand-central/long-beach"),
    "vs": ("Wikipedia, Valley Stream, New York (2020 Census figures)", "https://en.wikipedia.org/wiki/Valley_Stream,_New_York"),
    "vs_stn": ("Wikipedia, Valley Stream station", "https://en.wikipedia.org/wiki/Valley_Stream_station"),
    "gibson": ("Wikipedia, Gibson station", "https://en.wikipedia.org/wiki/Gibson_station"),
    "lyn": ("Wikipedia, Lynbrook, New York (2020 Census figures)", "https://en.wikipedia.org/wiki/Lynbrook,_New_York"),
    "lyn_stn": ("Wikipedia, Lynbrook station", "https://en.wikipedia.org/wiki/Lynbrook_station"),
    "rvc": ("Wikipedia, Rockville Centre, New York (2020 Census figures)", "https://en.wikipedia.org/wiki/Rockville_Centre,_New_York"),
    "rvc_stn": ("Wikipedia, Rockville Centre station", "https://en.wikipedia.org/wiki/Rockville_Centre_station"),
    "rvc_elec": ("Village of Rockville Centre, Electric Department rates page", "https://www.rvcny.gov/electric-department/pages/electric-rates"),
    "ocs": ("Wikipedia, Oceanside, New York (2020 Census figures)", "https://en.wikipedia.org/wiki/Oceanside,_New_York"),
    "ocs_stn": ("Wikipedia, Oceanside station", "https://en.wikipedia.org/wiki/Oceanside_station_(LIRR)"),
    "bal": ("Wikipedia, Baldwin, Nassau County, New York (2020 Census figures)", "https://en.wikipedia.org/wiki/Baldwin,_Nassau_County,_New_York"),
    "fpt": ("Wikipedia, Freeport, New York (2020 Census figures)", "https://en.wikipedia.org/wiki/Freeport,_New_York"),
}

TOWNS = [
    {
        "slug": "valley-stream", "name": "Valley Stream",
        "answer": "Valley Stream is an incorporated village in the Town of Hempstead on the Queens border, with 40,634 residents in 2020. It has two LIRR stations, Valley Stream and Gibson, on the Far Rockaway and Long Beach branches. Elementary schools come from three districts, 13, 24 and 30, and high school from Valley Stream Central.",
        "glance": [
            ("Government", "Incorporated village since February 14, 1925, inside the Town of Hempstead"),
            ("Population", "40,634 (2020 Census)"),
            ("Area", "About 3.5 square miles"),
            ("LIRR", "Valley Stream station (Far Rockaway and Long Beach branches, fare zone 4); Gibson station (Far Rockaway Branch)"),
            ("Schools", "Valley Stream 13, 24 and 30 elementary districts; Valley Stream Central High School District; some southern streets in Hewlett-Woodmere"),
        ],
        "commute": "Valley Stream station is served by Far Rockaway Branch and Long Beach Branch trains. West Hempstead Branch trains stopped calling there in February 2023. Gibson station, in the Gibson section of the village, is on the Far Rockaway Branch. Under the MTA's 2023 service plan, Long Beach Branch peak trains run to both Penn Station and Grand Central Madison.",
        "flood": "Valley Stream sits back from the bays compared with Oceanside or Freeport, but FEMA maps flood risk lot by lot, not town by town. Check the exact address before you bid.",
        "gov": "Valley Stream is an incorporated village, so it has its own mayor, board, building department and village taxes, on top of Town of Hempstead, Nassau County and school taxes.",
        "schools": "Valley Stream is unusual: elementary students attend one of three separate districts, 13, 24 or 30, depending on the street, and then go on to the Valley Stream Central High School District. Some homes in the southern part of the village are zoned to Hewlett-Woodmere instead. Confirm the district for the exact address with the district office.",
        "faqs": [
            ("Is Valley Stream a village?", "Yes. Valley Stream incorporated as a village on February 14, 1925. It sits inside the Town of Hempstead in Nassau County, along the Queens border."),
            ("Which LIRR stations serve Valley Stream?", "Valley Stream station, served by the Far Rockaway and Long Beach branches, and Gibson station on the Far Rockaway Branch. Valley Stream station is in fare zone 4."),
            ("Which school district is a Valley Stream home in?", "It depends on the street. Elementary grades come from Valley Stream 13, 24 or 30, high school from Valley Stream Central, and some southern streets are in Hewlett-Woodmere."),
            ("Is Valley Stream in a flood zone?", "Some properties may be and many are not. FEMA maps flood zones by address, so look up the exact property on FEMA's Flood Map Service Center and read the seller's flood disclosure."),
        ],
        "sources": ["onekey", "onekey_page", "vs", "vs_stn", "gibson", "mta_lb", "fema", "nysba"],
        "near": ["lynbrook", "rockville-centre"],
    },
    {
        "slug": "lynbrook", "name": "Lynbrook",
        "answer": "Lynbrook is an incorporated village of about two square miles in the Town of Hempstead, with 20,438 residents in 2020. Lynbrook station, on Sunrise Highway, is served by Long Beach Branch trains and some Babylon Branch trains. Five school districts serve parts of the village, so the district depends on the exact address.",
        "glance": [
            ("Government", "Incorporated village since 1911, inside the Town of Hempstead"),
            ("Population", "20,438 (2020 Census)"),
            ("Area", "2.01 square miles, all land"),
            ("LIRR", "Lynbrook station (Long Beach Branch and select Babylon Branch trains); Westwood station (West Hempstead Branch) at the Lynbrook and Malverne line"),
            ("Schools", "Lynbrook, East Rockaway, Hewlett-Woodmere, Malverne and Valley Stream districts, by address"),
        ],
        "commute": "Lynbrook station sits off Sunrise Highway between Peninsula Boulevard and Broadway. It is served by Long Beach Branch trains and select Babylon Branch trains. Under the MTA's 2023 service plan, Long Beach Branch peak trains run to both Penn Station and Grand Central Madison. Westwood station on the West Hempstead Branch straddles the Lynbrook and Malverne border.",
        "flood": "The Census counts Lynbrook's area as all land, with no water inside the village. That does not rule out flood zones on a given lot. Look up the exact address on FEMA's map before you bid.",
        "gov": "Lynbrook is an incorporated village with its own government and village taxes, on top of Town of Hempstead, Nassau County and school taxes.",
        "schools": "Five public school districts serve parts of Lynbrook: Lynbrook, East Rockaway, Hewlett-Woodmere, Malverne, and the Valley Stream districts, including Valley Stream Central High School District. The district depends on where in the village the home sits, so confirm it for the exact address.",
        "faqs": [
            ("Is Lynbrook a village?", "Yes. Lynbrook incorporated as a village in 1911 and sits in the Town of Hempstead, Nassau County."),
            ("Which LIRR branch serves Lynbrook?", "Lynbrook station is served by Long Beach Branch trains and select Babylon Branch trains. Westwood station, on the West Hempstead Branch, sits at the Lynbrook and Malverne border."),
            ("What school district is Lynbrook in?", "Five districts serve parts of Lynbrook: Lynbrook, East Rockaway, Hewlett-Woodmere, Malverne and the Valley Stream districts. The district depends on the address."),
            ("How big is Lynbrook?", "About 2.01 square miles, with 20,438 residents at the 2020 Census."),
        ],
        "sources": ["onekey", "onekey_page", "lyn", "lyn_stn", "mta_lb", "fema", "nysba"],
        "near": ["valley-stream", "rockville-centre", "oceanside"],
    },
    {
        "slug": "rockville-centre", "name": "Rockville Centre",
        "answer": "Rockville Centre is an incorporated village in the Town of Hempstead, with 26,016 residents in 2020. Its LIRR station is on the Babylon Branch. Most homes are in the Rockville Centre school district, but about a fifth of residents are in the Oceanside district and some are in Baldwin's. The village runs its own electric utility.",
        "glance": [
            ("Government", "Incorporated village since July 15, 1893, inside the Town of Hempstead"),
            ("Population", "26,016 (2020 Census)"),
            ("Area", "About 3.3 square miles"),
            ("LIRR", "Rockville Centre station (Babylon Branch)"),
            ("Schools", "Rockville Centre UFSD for most homes; about 20 percent of residents in Oceanside UFSD; part in Baldwin UFSD"),
            ("Electric", "Village-owned Rockville Centre Electric Department, one of three municipal electric utilities on Long Island"),
        ],
        "commute": "Rockville Centre station, also signed for Molloy, is on the LIRR's Babylon Branch. Montauk Branch trains pass through without stopping.",
        "flood": "Most of Rockville Centre sits north of the bayfront towns, but parts of the village do contain water area, and FEMA maps flood zones lot by lot. Check the exact address before you bid.",
        "gov": "Rockville Centre is an incorporated village with its own government and village taxes. It also runs its own electric department, which the village says lets it offer low-cost power to customers. Ask the seller for recent electric bills.",
        "schools": "Most of the village is in the Rockville Centre Union Free School District, which also reaches into parts of South Hempstead. About 20 percent of residents live in the Oceanside district and part of the village is in the Baldwin district. Two houses on nearby streets can pay different school taxes, so confirm the district for the exact address.",
        "faqs": [
            ("Is all of Rockville Centre in the Rockville Centre school district?", "No. About 20 percent of residents are in the Oceanside school district and part of the village is in the Baldwin district. Confirm the district for the exact address."),
            ("Which LIRR branch serves Rockville Centre?", "The Babylon Branch. Rockville Centre station is also signed for Molloy."),
            ("Who supplies electricity in Rockville Centre?", "The village's own Rockville Centre Electric Department, one of three municipal electric utilities on Long Island."),
            ("When did Rockville Centre become a village?", "Rockville Centre incorporated on July 15, 1893."),
        ],
        "sources": ["onekey", "onekey_page", "rvc", "rvc_stn", "rvc_elec", "fema", "nysba"],
        "near": ["lynbrook", "oceanside", "baldwin"],
    },
    {
        "slug": "oceanside", "name": "Oceanside",
        "answer": "Oceanside is an unincorporated hamlet in the Town of Hempstead, with 32,637 residents in 2020 and its own school district. Its LIRR station is on the Long Beach Branch. Hurricane Sandy flooded the southern part of Oceanside in 2012, so the flood zone and the cost of flood insurance belong at the top of any buyer's checklist.",
        "glance": [
            ("Government", "Hamlet (no village government), governed by the Town of Hempstead"),
            ("Population", "32,637 (2020 Census)"),
            ("Area", "5.43 square miles, about 0.5 of it water"),
            ("LIRR", "Oceanside station (Long Beach Branch), at Weidner Avenue and Lawson Boulevard"),
            ("Schools", "Oceanside School District"),
            ("Flood history", "Hurricane Sandy flooded the southern portion in 2012"),
        ],
        "commute": "Oceanside station sits at Weidner Avenue and Lawson Boulevard on the Long Beach Branch. Under the MTA's 2023 service plan, Long Beach Branch peak trains run to both Penn Station and Grand Central Madison, and all of them stop at Jamaica.",
        "flood": "Flood risk is the first question in Oceanside. Hurricane Sandy completely flooded the southern part of the hamlet in 2012, and power was out for nearly two weeks after a nearby substation in Island Park failed. Only Reynolds Channel and marsh islands separate Oceanside from the barrier island and the ocean. Look up the exact address on FEMA's map, get a flood insurance quote before you sign a contract, and ask whether the home has an elevation certificate.",
        "gov": "Oceanside is a hamlet, not a village. It has no village government or village tax. Zoning, permits and building questions go to the Town of Hempstead.",
        "schools": "Oceanside is served by the Oceanside School District. Part of neighboring Rockville Centre is also in the Oceanside district.",
        "faqs": [
            ("Did Oceanside flood during Hurricane Sandy?", "Yes. Sandy flooded the southern portion of Oceanside in 2012. Check the FEMA flood zone and the seller's flood disclosure for any home you consider."),
            ("Is Oceanside a village?", "No. Oceanside is a hamlet governed by the Town of Hempstead, so there is no village government or village tax."),
            ("Which LIRR branch serves Oceanside?", "The Long Beach Branch. Oceanside station is at Weidner Avenue and Lawson Boulevard."),
            ("What school district is Oceanside in?", "The Oceanside School District."),
        ],
        "sources": ["onekey", "onekey_page", "ocs", "ocs_stn", "mta_lb", "fema", "nysba"],
        "near": ["rockville-centre", "baldwin", "lynbrook"],
    },
    {
        "slug": "baldwin", "name": "Baldwin",
        "answer": "Baldwin is an unincorporated hamlet in the Town of Hempstead, with 33,919 residents in 2020. Its LIRR station is on the Babylon Branch. Most of Baldwin is in the Baldwin school district, with small parts in the Oceanside, Rockville Centre, Roosevelt and Uniondale districts. The hamlet sits between Milburn Creek and Parsonage Creek.",
        "glance": [
            ("Government", "Hamlet (no village government), governed by the Town of Hempstead"),
            ("Population", "33,919 (2020 Census)"),
            ("Area", "About 3.0 square miles"),
            ("LIRR", "Baldwin station (Babylon Branch)"),
            ("Schools", "Baldwin UFSD for most homes; small parts in Oceanside, Rockville Centre, Roosevelt and Uniondale"),
        ],
        "commute": "Baldwin station is on the LIRR's Babylon Branch, between Rockville Centre and Freeport.",
        "flood": "Baldwin runs between Milburn Creek and Parsonage Creek, and FEMA maps flood zones lot by lot. Look up the exact address on FEMA's map and get a flood insurance quote before you sign.",
        "gov": "Baldwin is a hamlet, not a village, so there is no village government or village tax. Zoning, permits and building questions go to the Town of Hempstead.",
        "schools": "Most of Baldwin is in the Baldwin Union Free School District. Small parts fall in the Oceanside, Rockville Centre, Roosevelt and Uniondale districts. Confirm the district for the exact address.",
        "faqs": [
            ("Is Baldwin a village?", "No. Baldwin is a hamlet in the Town of Hempstead, so there is no village government or village tax."),
            ("Which LIRR branch serves Baldwin?", "The Babylon Branch."),
            ("What school district is Baldwin in?", "Mostly the Baldwin Union Free School District, with small parts in Oceanside, Rockville Centre, Roosevelt and Uniondale."),
            ("How many people live in Baldwin?", "33,919 at the 2020 Census."),
        ],
        "sources": ["onekey", "onekey_page", "bal", "fema", "nysba"],
        "near": ["rockville-centre", "freeport", "oceanside"],
        "flood_unverified": True,
    },
    {
        "slug": "freeport", "name": "Freeport",
        "answer": "Freeport is an incorporated village in the Town of Hempstead and, with 44,472 people in 2020, the largest of these six towns. Its LIRR station is on the Babylon Branch. Freeport Public Schools serves the village, Freeport runs its own electric utility, and the Nautical Mile on Woodcleft Canal is its waterfront.",
        "glance": [
            ("Government", "Incorporated village since 1892, inside the Town of Hempstead"),
            ("Population", "44,472 (2020 Census)"),
            ("Area", "About 4.9 square miles, about 0.3 of it water"),
            ("LIRR", "Freeport station (Babylon Branch)"),
            ("Schools", "Freeport Public Schools, eight schools and 6,343 students in 2023 to 2024"),
            ("Electric", "Village-owned municipal electric utility since 1898"),
        ],
        "commute": "Freeport station is on the LIRR's Babylon Branch, east of Baldwin.",
        "flood": "Freeport is a canal village, with about 0.3 square miles of water inside village lines and the Nautical Mile running along Woodcleft Canal. Look up the exact address on FEMA's map, get a flood insurance quote before you sign, and ask for any elevation certificate.",
        "gov": "Freeport is an incorporated village with its own government and village taxes. It has run its own electric utility since 1898, which gives residents lower rates than many surrounding communities. Ask the seller for recent electric bills.",
        "schools": "Freeport Public Schools operates the village's public schools: eight schools and 6,343 students in the 2023 to 2024 school year. Confirm the district for the exact address.",
        "faqs": [
            ("Is Freeport a village?", "Yes. Freeport residents voted to incorporate the village on October 18, 1892. It sits in the Town of Hempstead."),
            ("Does Freeport have its own electric company?", "Yes. Freeport has run a municipal electric utility since 1898."),
            ("Which LIRR branch serves Freeport?", "The Babylon Branch."),
            ("What is the Nautical Mile?", "Freeport's waterfront strip along the west side of Woodcleft Canal, with seafood restaurants, shops and boat rides. A festival is held there the first weekend in June."),
        ],
        "sources": ["onekey", "onekey_page", "fpt", "fema", "nysba"],
        "near": ["baldwin", "oceanside"],
        "flood_unverified": True,
    },
]
BY_SLUG = {t["slug"]: t for t in TOWNS}
NEXT_TOWNS = ["Merrick", "Bellmore", "Wantagh", "Seaford", "Massapequa",
              "Massapequa Park", "Long Beach", "Island Park", "the Five Towns"]


# ---------------------------------------------------------------- schema

def author_node():
    return {
        "@type": "Person",
        "@id": PERSON_ID,
        "name": NAME,
        "url": f"{HOME}/",
        "jobTitle": LICENSE,
        "description": CANONICAL,
        "worksFor": {"@type": "RealEstateAgent", "name": BROKERAGE,
                     "telephone": OFFICE_TEL,
                     "address": {"@type": "PostalAddress", "streetAddress": STREET,
                                 "addressLocality": CITY, "addressRegion": REGION,
                                 "postalCode": ZIP, "addressCountry": "US"}},
        "hasCredential": {"@type": "EducationalOccupationalCredential",
                          "name": "Seniors Real Estate Specialist (SRES)"},
        "sameAs": [f"{HOME}/", "https://www.linkedin.com/in/realtor/",
                   "https://www.zillow.com/profile/bisendra", "https://bisendra.substack.com/"],
    }


def site_node():
    return {"@type": "WebSite", "@id": f"{DOMAIN}/#website", "url": f"{DOMAIN}/",
            "name": "Long Island Homes: South Shore buyer guides by Bisendra Melaram",
            "author": {"@id": PERSON_ID}, "publisher": {"@id": PERSON_ID},
            "inLanguage": "en-US"}


def breadcrumbs(trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{DOMAIN}{p}"}
        for i, (n, p) in enumerate(trail)]}


def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def article_schema(path, title, desc, about=None, citations=()):
    a = {"@type": "Article", "headline": title, "description": desc,
         "url": f"{DOMAIN}{path}", "mainEntityOfPage": f"{DOMAIN}{path}",
         "author": {"@id": PERSON_ID}, "publisher": {"@id": PERSON_ID},
         "datePublished": UPDATED, "dateModified": UPDATED, "inLanguage": "en-US"}
    if about:
        a["about"] = about
    if citations:
        a["citation"] = list(citations)
    return a


# ---------------------------------------------------------------- layout

ROBOTS_META = ("index, follow, max-snippet:-1, max-image-preview:large" if LAUNCH
               else "noindex, follow")


def page(path, title, desc, body, graph_extra=(), og_type="website"):
    url = f"{DOMAIN}{path}"
    graph = [author_node(), site_node()] + list(graph_extra)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                    indent=1, ensure_ascii=False)
    nav = "".join(f'<a href="/towns/{t["slug"]}/">{t["name"]}</a>' for t in TOWNS)
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="author" content="{NAME}">
<meta name="robots" content="{ROBOTS_META}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Long Island Homes">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_US">
<!-- TODO: add og:image once there is a social card at /assets/og.jpg -->
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(desc)}">
<link rel="stylesheet" href="/assets/site.css">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
 <div class="wrap">
  <a class="brand" href="/">Long Island Homes<span>South Shore buyer guides by {NAME}</span></a>
  <nav aria-label="Towns">{nav}<a href="/guides/flood-zones/">Flood zones</a></nav>
 </div>
</header>
<main id="main" class="wrap">
{body}
</main>
<footer class="foot">
 <div class="wrap">
  <p class="id-line">Written by <a href="{HOME}/">{NAME}</a>. {CANONICAL}</p>
  <p><strong>{NAME}</strong>, {LICENSE}<br>
  {BROKERAGE}, {STREET}, {CITY}, {REGION} {ZIP}<br>
  Office <a href="tel:{OFFICE_TEL}">{OFFICE}</a></p>
  <p class="small">Facts on these pages come from the public sources listed on each page and are checked when the page is updated. Confirm anything you rely on, especially flood zones and school districts, for the exact address. Equal Housing Opportunity. <a href="{HOME}/fair-housing/">Fair housing notice</a>. <a href="/about/">About this guide</a>.</p>
 </div>
</footer>
</body>
</html>
"""


def answer(text):
    return f'<p class="answer">{text}</p>'


def crumbs_html(trail):
    parts = [f"<span>{n}</span>" if i == len(trail) - 1 else f'<a href="{p}">{n}</a>'
             for i, (n, p) in enumerate(trail)]
    return f'<nav class="crumbs" aria-label="Breadcrumb">{" / ".join(parts)}</nav>'


def byline():
    return (f'<p class="byline">By <a href="{HOME}/about/">{NAME}</a>, SRES, {LICENSE}, '
            f'{BROKERAGE}. Last updated <time datetime="{UPDATED}">{UPDATED_TEXT}</time>.</p>')


def faq_html(faqs, heading="Common questions"):
    out = [f'<section class="faq"><h2>{heading}</h2>']
    for q, a in faqs:
        out.append(f"<h3>{escape(q)}</h3><p>{escape(a)}</p>")
    out.append("</section>")
    return "\n".join(out)


def sources_html(keys):
    items = "".join(f'<li><a href="{SRC[k][1]}">{escape(SRC[k][0])}</a></li>' for k in keys)
    return (f'<section class="sources"><h2>Sources</h2><p>Checked {CHECKED_TEXT}.</p>'
            f'<ul>{items}</ul></section>')


def author_box():
    return (f'<aside class="cta"><h2>Who wrote this guide?</h2>'
            f'<p><a href="{HOME}/">{NAME}</a> has been a New York real estate agent since 2003 and holds the '
            f'Seniors Real Estate Specialist (SRES) designation. He works from {BROKERAGE} in Garden City and '
            f'helps buyers and sellers across the South Shore. Call the office at '
            f'<a href="tel:{OFFICE_TEL}">{OFFICE}</a> and ask for Bisendra.</p></aside>')


FAIR = ('<p class="note">This guide describes places, not people. Fair housing law bars agents from steering '
        'buyers toward or away from any neighborhood, and the choice of where to live is yours.</p>')


# ---------------------------------------------------------------- pages

PAGES = {}


def add(path, title, desc, body, extra=(), og_type="website"):
    PAGES[path] = page(path, title, desc, body, extra, og_type)


def town_page(t):
    n, s = t["name"], t["slug"]
    path = f"/towns/{s}/"
    title = f"Buying a home in {n}, NY: 2026 buyer guide"
    desc = (f"{n}, NY buyer guide by Bisendra Melaram: LIRR stations, FEMA flood zone checks, "
            f"school districts, village or hamlet, and current prices. Updated {CHECKED_TEXT}.")
    glance = "".join(f"<tr><th scope=\"row\">{escape(k)}</th><td>{escape(v)}</td></tr>"
                     for k, v in t["glance"])
    near = " ".join(f'<a href="/towns/{x}/">{BY_SLUG[x]["name"]}</a>' for x in t["near"])
    near_list = ", ".join(f'<a href="/towns/{x}/">{BY_SLUG[x]["name"]}</a>' for x in t["near"])
    flood_flag = (f' {todo("your own local note on which parts of " + n + " flooded in Sandy and what flood insurance runs, with a source or your MLS data")}'
                  if t.get("flood_unverified") else "")
    body = f"""
{crumbs_html([("Home", "/"), ("Towns", "/towns/"), (n, path)])}
<h1>Buying a home in {n}, NY</h1>
{byline()}
{answer(t["answer"])}

<h2>{n} at a glance</h2>
<table><tbody>{glance}</tbody></table>

<h2>What do homes in {n} sell for right now?</h2>
<p>OneKey MLS publishes its public market statistics by county, not by town, so the figures below are for single-family homes across all of Nassau County. In September 2026 the county's median single-family sale price was $860,000, homes took a median 40 days to sell, and sellers received 99.8 percent of their original asking price.</p>
<table>
 <thead><tr><th>Nassau County single-family homes</th><th>September 2026</th><th>12 months through September 2026</th></tr></thead>
 <tbody>
  <tr><td>Median sales price</td><td>$860,000 (up 2.1% from Sept. 2025)</td><td>$860,000 (up 4.9%)</td></tr>
  <tr><td>Days on market until sale</td><td>40</td><td>46</td></tr>
  <tr><td>Percent of original list price received</td><td>99.8%</td><td>99.5%</td></tr>
  <tr><td>Closed sales</td><td>757</td><td>8,260</td></tr>
  <tr><td>Homes for sale at month end</td><td>2,318</td><td></td></tr>
 </tbody>
</table>
<p class="note">Source: OneKey MLS Local Market Update, Nassau County, September 2026, current as of October 7, 2026. Prices do not account for sale concessions or down payment assistance. Figures cover the whole county, not {n} alone.</p>
<p>{todo(f"{n} town-level numbers from your own OneKey MLS search: median sale price, days on market, percent of list received and homes sold, with the month")}</p>

<h2>How do you commute from {n} to Manhattan?</h2>
<p>{t["commute"]}</p>
<p>{todo(f"typical peak ride time from {n} to Penn Station and to Grand Central Madison, from MTA TrainTime, with the month you checked")}</p>

<h2>Is {n} in a flood zone?</h2>
<p>{t["flood"]}{flood_flag}</p>
<p>Since March 20, 2024, New York sellers must answer flood questions on the property condition disclosure, including whether the home is in a FEMA flood zone, whether flood insurance is required, and whether there have been flood claims. Read our <a href="/guides/flood-zones/">South Shore flood zone guide</a> for how to check a house.</p>

<h2>Is {n} a village or part of the Town of Hempstead?</h2>
<p>{t["gov"]}</p>

<h2>Which school district serves a home in {n}?</h2>
<p>{t["schools"]}</p>

<h2>What kinds of homes are in {n}?</h2>
<p>{todo(f"housing stock in {n} from your experience and MLS data: common styles (capes, hi-ranches, colonials, splits), typical lot sizes, age of homes, and what the village or town allows for accessory apartments")}</p>

<h2>What has Bisendra sold in {n}?</h2>
<p>{todo(f"your recent closed deals in {n}, by street or section and month, with the client's permission")}</p>

{faq_html(t["faqs"], f"Questions buyers ask about {n}")}

<h2>Which towns are near {n}?</h2>
<p>Compare {n} with {near_list}, or see <a href="/towns/">all South Shore town guides</a>.</p>

{FAIR}
{author_box()}
{sources_html(t["sources"])}
"""
    place = {"@type": "Place", "name": f"{n}, NY",
             "containedInPlace": {"@type": "AdministrativeArea", "name": "Nassau County, NY"}}
    extra = [breadcrumbs([("Home", "/"), ("Towns", "/towns/"), (n, path)]),
             article_schema(path, f"Buying a home in {n}, NY", desc, place,
                            [SRC[k][1] for k in t["sources"]]),
             faq_schema(t["faqs"])]
    add(path, title, desc, body, extra, og_type="article")


for _t in TOWNS:
    town_page(_t)

# Towns index
rows = "".join(
    f'<tr><td><a href="/towns/{t["slug"]}/">{t["name"]}</a></td>'
    f'<td>{escape(dict(t["glance"])["Government"].split(",")[0])}</td>'
    f'<td>{escape(dict(t["glance"])["LIRR"])}</td></tr>' for t in TOWNS)
towns_table = f'<table><thead><tr><th>Town</th><th>Government</th><th>LIRR</th></tr></thead><tbody>{rows}</tbody></table>'

add("/towns/", "South Shore Long Island town guides | Long Island Homes",
    "Compare South Shore Long Island towns for buyers: Valley Stream, Lynbrook, Rockville Centre, Oceanside, Baldwin and Freeport. LIRR, flood zones, schools.",
    f"""
{crumbs_html([("Home", "/"), ("Towns", "/towns/")])}
<h1>South Shore town guides</h1>
{byline()}
{answer("These guides compare six South Shore towns in Nassau County for home buyers: Valley Stream, Lynbrook, Rockville Centre, Oceanside, Baldwin and Freeport. Each covers the LIRR stations and branch, the flood zone question, which school districts serve which streets, and whether the town is a village with its own taxes.")}
<h2>How do the six towns compare?</h2>
{towns_table}
<h2>Which towns are coming next?</h2>
<p>{", ".join(NEXT_TOWNS)}, then the Suffolk South Shore from Amityville east.</p>
{FAIR}
{author_box()}
""", [breadcrumbs([("Home", "/"), ("Towns", "/towns/")]),
      {"@type": "ItemList", "name": "South Shore town guides",
       "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": t["name"],
                            "url": f"{DOMAIN}/towns/{t['slug']}/"} for i, t in enumerate(TOWNS)]}])

# Home
home_faqs = [
    ("What is the South Shore of Long Island?",
     "The South Shore is the stretch of Long Island along the Atlantic side, facing the bays behind the barrier islands. In Nassau County it runs roughly from Valley Stream on the Queens border east through Massapequa, and it continues through Suffolk County."),
    ("What should I check before buying a house on the South Shore?",
     "Check the FEMA flood zone for the exact address, read the seller's flood disclosure, get a flood insurance quote, confirm the school district for the street, and find out whether the home is in an incorporated village with its own taxes."),
    ("Who writes these guides?",
     "Bisendra Melaram, a New York Licensed Real Estate Salesperson since 2003 with Keller Williams Greater Nassau in Garden City, and a Seniors Real Estate Specialist (SRES)."),
]
add("/", "Long Island South Shore home buyer guides | Long Island Homes",
    "Town by town buyer guides for Long Island's South Shore by Bisendra Melaram: LIRR commute, FEMA flood zones, school districts, villages and prices.",
    f"""
<h1>Buying a home on Long Island's South Shore</h1>
{byline()}
{answer("Long Island Homes is a town by town guide for people buying on the South Shore of Nassau County, written by local agent Bisendra Melaram. Each guide answers the questions that change what a house really costs: the flood zone, the school district, village taxes, and how long the LIRR ride to Manhattan takes.")}

<h2>Which towns have guides?</h2>
{towns_table}

<h2>What is the Nassau County market doing right now?</h2>
<p>In September 2026 the median Nassau County single-family home sold for $860,000, up 2.1 percent from a year earlier, after a median 40 days on market. Sellers received 99.8 percent of their original asking price, according to the <a href="https://corporate.onekeymls.com/s/NassauCounty-t8fn.pdf">OneKey MLS Nassau County report</a>. OneKey publishes these figures by county, so town pages show county numbers until town figures are added.</p>

<h2>Why do flood zones matter so much here?</h2>
<p>Many South Shore homes sit near bays, creeks and canals, and a FEMA flood zone can mean required flood insurance. New York sellers have had to answer flood questions on the property condition disclosure since March 20, 2024. Start with the <a href="/guides/flood-zones/">South Shore flood zone guide</a>.</p>

<h2>Why does the school district depend on the street?</h2>
<p>School district lines on the South Shore do not follow town names. Part of Rockville Centre is in the Oceanside district, parts of Lynbrook are in five different districts, and Valley Stream has three elementary districts. Each town guide lists the districts that serve it.</p>

<h2>Village or hamlet: what is the difference?</h2>
<p>Valley Stream, Lynbrook, Rockville Centre and Freeport are incorporated villages, with their own governments and village taxes. Oceanside and Baldwin are hamlets governed by the Town of Hempstead. Rockville Centre and Freeport also run their own electric utilities.</p>

{faq_html(home_faqs)}
{FAIR}
{author_box()}
""", [faq_schema(home_faqs),
      breadcrumbs([("Home", "/")])])

# Flood guide
flood_faqs = [
    ("Can a New York seller skip the flood disclosure?",
     "No. Since March 20, 2024, the $500 credit that let sellers skip the property condition disclosure is gone, and the form includes flood questions."),
    ("What is the difference between a 100-year and a 500-year floodplain?",
     "FEMA's special flood hazard area, often called the 100-year floodplain, has a 1 percent chance of flooding in any year. The moderate flood hazard area, often called the 500-year floodplain, has a 0.2 percent chance in any year."),
    ("How do I find the flood zone for a house?",
     "Search the exact address on FEMA's Flood Map Service Center at msc.fema.gov. Then compare it with the seller's answers on the property condition disclosure."),
    ("What is an elevation certificate?",
     "A document prepared by a licensed surveyor or engineer that records a building's elevation compared with expected flood levels. Insurers can use it to rate flood insurance, and the New York disclosure form asks whether one exists."),
]
add("/guides/flood-zones/", "South Shore Long Island flood zones: a buyer's guide | Long Island Homes",
    "How to check a South Shore Long Island home for flood risk: FEMA flood zones, New York's 2024 flood disclosure rules, elevation certificates and flood insurance.",
    f"""
{crumbs_html([("Home", "/"), ("Flood zones", "/guides/flood-zones/")])}
<h1>South Shore flood zones: what buyers should check</h1>
{byline()}
{answer("Before you bid on a South Shore home, look up the exact address on FEMA's Flood Map Service Center, read the seller's flood answers on the New York property condition disclosure, ask for any elevation certificate, and get a flood insurance quote. Since March 20, 2024, New York sellers must answer those flood questions.")}

<h2>What changed in New York in 2024?</h2>
<p>Since March 20, 2024, sellers can no longer give a $500 credit at closing instead of filling out the property condition disclosure. The form now asks whether:</p>
<ul>
 <li>any of the property is in a FEMA-designated floodplain</li>
 <li>it is in a special flood hazard area (100-year floodplain) or a moderate flood hazard area (500-year floodplain)</li>
 <li>the property is subject to a flood insurance requirement</li>
 <li>the seller received FEMA, SBA or other federal disaster aid for flood damage</li>
 <li>flood insurance is in place, and whether a FEMA elevation certificate exists</li>
 <li>the seller has filed a flood insurance claim on the property</li>
</ul>

<h2>How do you check a house's flood zone?</h2>
<ol>
 <li>Search the address on <a href="https://msc.fema.gov/portal/search">FEMA's Flood Map Service Center</a>.</li>
 <li>Compare what you find with the seller's disclosure answers.</li>
 <li>Ask for the elevation certificate, past flood insurance bills and any claims history.</li>
 <li>Get a flood insurance quote before you sign the contract, not after.</li>
 <li>Ask your home inspector to look for signs of past water in the basement, crawl space and garage.</li>
</ol>

<h2>Which South Shore towns have flood history?</h2>
<p>Hurricane Sandy completely flooded the southern part of <a href="/towns/oceanside/">Oceanside</a> in 2012. <a href="/towns/freeport/">Freeport</a> is a canal village, and <a href="/towns/baldwin/">Baldwin</a> sits between two creeks. <a href="/towns/lynbrook/">Lynbrook</a>, <a href="/towns/valley-stream/">Valley Stream</a> and <a href="/towns/rockville-centre/">Rockville Centre</a> do not front the bay, but FEMA maps risk lot by lot, so check every address.</p>

<h2>What does flood insurance cost on the South Shore?</h2>
<p>{todo("real premium ranges from a local flood insurance agent you work with, with their name and permission, or leave this section out")}</p>

{faq_html(flood_faqs)}
{author_box()}
{sources_html(["nysba", "fema", "ocs", "fpt", "bal"])}
""", [breadcrumbs([("Home", "/"), ("Flood zones", "/guides/flood-zones/")]),
      article_schema("/guides/flood-zones/", "South Shore flood zones: what buyers should check",
                     "Flood zone checks for South Shore Long Island buyers.", None,
                     [SRC["nysba"][1], SRC["fema"][1]]),
      faq_schema(flood_faqs)], og_type="article")

# About
add("/about/", "About Long Island Homes and its author, Bisendra Melaram",
    "Long Island Homes is a South Shore buyer guide written by Bisendra Melaram, Licensed Real Estate Salesperson with Keller Williams Greater Nassau since 2003.",
    f"""
{crumbs_html([("Home", "/"), ("About", "/about/")])}
<h1>About this guide</h1>
{answer("Long Island Homes is a free buyer guide to the South Shore of Long Island, written by Bisendra Melaram, a New York Licensed Real Estate Salesperson since 2003 and Seniors Real Estate Specialist with Keller Williams Greater Nassau in Garden City. Each town page cites its sources and carries the date it was last updated.")}
<h2>How are the facts checked?</h2>
<p>Town facts come from public sources listed at the bottom of each page: Census figures, LIRR and MTA information, FEMA flood maps, village and school district sites, and New York law. Market numbers come from Bisendra's own analysis of OneKey MLS closed sales. Pages are refreshed monthly.</p>
<h2>How does this guide handle fair housing?</h2>
<p>It describes places, never the people who live in them. Fair housing law bars agents from steering anyone toward or away from a neighborhood.</p>
<h2>Who is the author?</h2>
<p>See <a href="{HOME}/about/">Bisendra Melaram's full profile</a>.</p>
{author_box()}
""", [breadcrumbs([("Home", "/"), ("About", "/about/")]),
      {"@type": "AboutPage", "url": f"{DOMAIN}/about/", "author": {"@id": PERSON_ID}}])

NOT_FOUND = page("/404.html", "Page not found | Long Island Homes", "This page does not exist.",
                 '<h1>Page not found</h1><p>Try the <a href="/towns/">town guides</a>.</p>')


# ---------------------------------------------------------------- crawl files

ROBOTS = "\n".join(
    ["# Search engines and AI assistants are welcome here."]
    + sum([[f"User-agent: {ua}", "Allow: /", ""] for ua in [
        "Googlebot", "Bingbot", "Applebot", "Applebot-Extended", "DuckDuckBot",
        "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot",
        "Claude-User", "PerplexityBot", "Perplexity-User", "Google-Extended",
        "Meta-ExternalAgent", "CCBot", "*"]], [])
    + [f"Sitemap: {DOMAIN}/sitemap.xml", ""])


def llms_txt():
    lines = [
        "# Long Island Homes",
        "",
        "> Town by town home buyer guides for the South Shore of Long Island (Nassau County), "
        f"written by {CANONICAL} Each page cites public sources and carries a last-updated date.",
        "",
        f"Author: [{NAME}]({HOME}/). Office: {BROKERAGE}, {STREET}, {CITY}, {REGION} {ZIP}. Phone {OFFICE}.",
        "",
        "## Town guides",
    ] + [f"- [Buying a home in {t['name']}, NY]({DOMAIN}/towns/{t['slug']}/): {t['answer']}" for t in TOWNS] + [
        "",
        "## Guides",
        f"- [South Shore flood zones]({DOMAIN}/guides/flood-zones/): FEMA zones, New York's 2024 flood disclosure rules, elevation certificates",
        f"- [All town guides]({DOMAIN}/towns/)",
        f"- [About this guide]({DOMAIN}/about/)",
        "",
    ]
    return "\n".join(lines)


def sitemap():
    body = "".join(f"<url><loc>{DOMAIN}{u}</loc><lastmod>{UPDATED}</lastmod></url>\n"
                   for u in sorted(PAGES))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{body}</urlset>\n")


def write(rel, text):
    path = os.path.join(OUT, rel.lstrip("/"))
    if rel.endswith("/"):
        path = os.path.join(path, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(STATIC, OUT)
    for p, html in PAGES.items():
        write(p, html)
    write("/404.html", NOT_FOUND)
    write("/robots.txt", ROBOTS)
    write("/llms.txt", llms_txt())
    write("/sitemap.xml", sitemap())
    left = sum(h.count('class="todo"') for h in PAGES.values())
    print(f"Built {len(PAGES)} pages into {OUT}. Placeholders left: {left}. LAUNCH={LAUNCH}")


if __name__ == "__main__":
    main()
