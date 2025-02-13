DROP TABLE if exists "ad_campaigns";

CREATE TABLE "ad_campaigns" (
    "Campaign_ID" VARCHAR(50) PRIMARY KEY,
    "Budget" INTEGER,
    "Duration" INTEGER,
    "Platform" VARCHAR(50),
    "Content_Type" VARCHAR(50),
    "Target_Age" VARCHAR(10),
    "Target_Gender" VARCHAR(10),
    "Region" VARCHAR(10),
    "Clicks" INTEGER,
    "Conversions" INTEGER,
    "CTR" FLOAT,
    "CPC" FLOAT,
    "Conversion_Rate" FLOAT,
    "Success" INTEGER
);

select count(*) from "ad_campaigns"

select * from "ad_campaigns"


COPY ad_campaigns 
FROM '/ad_campaign_performance.csv' 
DELIMITER ',' 
CSV HEADER;
