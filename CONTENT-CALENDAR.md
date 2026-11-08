# Content calendar for longislandhomes.co

Fresh, dated facts are what get a page quoted by Google and AI assistants. Every refresh ends the same way: change `UPDATED` and `UPDATED_TEXT` in `tools/build.py`, add a dated line to `UPDATES`, rebuild, and redeploy.

## Every month
- When OneKey MLS posts the new Nassau County Local Market Update (usually in the first two weeks), update the county table on every town page and the county range (`COUNTY_RANGE`). Source: https://corporate.onekeymls.com/market-statistics
- Add the town-level numbers from Bisendra's MLS search for the same month, once he supplies them.
- Recheck any village, district or MTA page the town guides cite.

## When the LIRR publishes a new schedule
- Download the GTFS feed (https://rrgtfsfeeds.s3.amazonaws.com/gtfslirr.zip), rerun the weekday 7:00 to 9:30 AM direct-train count for each station, and update `RAIL`, `GTFS_LABEL` and `SAMPLE_DAY` in `tools/town_data.py`. Schedules change several times a year.

## Fixed dates (Town of Hempstead and Nassau County)
- Early December: confirm the Assessment Review Commission window for the next roll and update the grievance dates on town pages and the glossary.
- January 4: the tentative roll and the grievance window open. Publish a reminder in the updates log.
- January 1 and July 1: general tax halves due. April 1 and October 1: school tax halves due. Recheck the schedule page each January.
- March 1: the grievance window closes. Update the dates for the following year once ARC posts them.

## Every year
- December: when the Census Bureau releases new American Community Survey five-year estimates, update `CENSUS` in `tools/town_data.py`.
- Spring: recheck FEMA's flood pages and any new Nassau flood map dates.
- Before each new town guide: gather the same facts (government, stations and ride times, districts with official links, Census figures, flood context) from primary sources only.
