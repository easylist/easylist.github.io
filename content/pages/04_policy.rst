:title: Policy

---------------
EasyList policy
---------------

The goal of EasyList is to block `ads </2011/07/11/the-definition-of-advert-and-link-exchange-policy.html>`_ on English and International sites. Self-promotion (any type of advertising that promotes goods or services that are owned or operated by the domain owner and doesn’t get commercially compensated for by third parties (examples can include new features, new posts, newsletters, subscriptions to printed media products, merchandise etc.)) won't be targeted directly. By blocking the following:
        - Ad scripts (Generic and site-specific)
        - Ad images 
        - Text/CSS ads
        - Pre/mid/end video ads
        - Affiliate links/images/widgets
        - Cosmetic filtering (Generic and site-specific CSS)
        - Ad servers (Block servers that host ads/ad-related contents)
        - Linking, loading or initialising to known Adservers, or ad scripts.
        - Ad servers used as clickthrough servers also blocked outright.
        - Inserting ad elements (cosmetic, servers or scripts) into a page
        - Prevent popups/popunders (Block scripts or domains that cause popups/popunders/ad notifications)
        - Placeholders of non-trivial size (Usually ≥50px tall and ≥50px wide)
        - Invideo/InSlideshow Ads (This is *NOT* the same as a site using embedded youtube videos).
                - 1st or 3rd-party content.
                - Videos/slideshows that aren't directly related to the specific webpage being shown. 
                - May autoplay and/or follows user on scroll. 
        - "Consent messages" using any of these techniques. 

Anti-adblock in EasyList will cover cosmetic and generic blocks checks:
        - Prevent adblock users showing a website
        - Create elements to disrupt viewing a website

For legal reasons, anti-adblock this will only cover:
        - Adult websites
        - File or Link hosting/sharing
        - Streaming/Torrent/Comic sites
        - Any historical anti-adblock rules

- Abusive adservers are classed as ad or tracking providers that continously deploys new revolving domains to evade EasyList or EasyPrivacy. 
        - Using "Revolving domains" with harmful javascript and popups.
        - We are an adblock and privacy list
        - Montoring EasyList Github commits to then circumvent adblock filters with changing/revolving domains or scripts.
        - Adcompanies websites have no useful purporse for EasyList/EasyPrivacy users except trying to create more counters and more spam domains.
        - It doesn't matter if the source domain is a different domain. We don't care.
        - Will be blocked without warning.
        - If you're an abusive ad company, disable EasyList. 
        - If the domain changes we will update the filters.

------------------
EasyPrivacy policy
------------------

The goal of EasyPrivacy is to block tracking and improve end user privacy. By blocking the following:
        - Analytics
        - AntiBot or Bot checks
        - Telemetry
        - Tracking Pixels or cookies (being set, checked or get)
        - Referrers
        - Beacons
        - Fingerprinting
        - Email tracking
        - Impressions / Event / Perf / Pageview logging
        - User agent checks or monitoring
        - Resource miners
        - Hit counters
        - CNAME trackers
        - Notification servers / popups including any tracking covered by Easyprivacy policy
        - Linking, loading or initialising to known tracking servers, or scripts
        - Some unnecessary 3rd-party scripts/images
        - "Consent messages" using any of these tracking techniques, covered by Easyprivacy policy
 
When a site is attempting to track, it'll be put into one of 4 categories.
        - Generic blocks (common URL/tracking filter patterns) used by 1st/3rd-parties.
        - 1st-party tracking. Self-hosted trackers and CNAME trackers.
        - 3rd-party tracking. Hosted by another provider, which hosts a tracking script, but not actually a tracking company.
        - Tracking-servers. Where the server has only one purpose to track/analyze user, will be blocked at the url level.
