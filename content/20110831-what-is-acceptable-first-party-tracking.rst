What is acceptable first-party tracking?
########################################

:date: 2011-08-31 18:17
:tags: EasyPrivacy
:category: Articles
:slug: 2011/08/31/what-is-acceptable-first-party-tracking
:authors: Michael

Although all third-party tracking is blocked outright by EasyPrivacy, `the subscription's policy`_ is slightly more lenient with first-party tracking, specifying that that items should be blocked only if they "collect a significant amount of personal data". As the wording is ambiguous, I have decided to convey my interpretation of the policy with regard various pieces of information available from the user and whether the subscription should specifically prevent the collection of such data.

**IP address and user agent**
  Although this information is recorded in system logs, the details make users identifiable, making this information personal. I would therefore suggest that EasyPrivacy should continue to regard the first-party collection of such data as unacceptable and prevent it being sent to any additional systems on the domain wherever possible.

**Screen resolution, colour depth and browser plugins**
  This information is not located in the system logs and pertains only to the user's system. I would therefore suggest that tracking this information is unacceptable.

**Time zone**
  Time zone provides a very approximate location of the user, and I would therefore suggest that this information should be classified as personal and prevented from being collected where possible.

**Language**
  If the language is that of the website the I do not have an issue with the information being collected, as it is about the site rather than user. However, to record the value set in the browser oversteps the mark in my opinion.

**JavaScript status**
  I would regard the JavaScript status as generic information provided that trackers do not attempt to determine the reason why scripts are unavailable, and I would therefore suggest collecting this type of information is acceptable.

**Advert blocking status**
  There is no intrinsic issue with detection of advert blocking software (we do not object to websites adding unobtrusive messages to their pages specifically for users of such programs). Therefore, provided that no detailed information such as the name of program responsible is collected, I would regard this type of tracking as acceptable.

**Page status**
  Information about the page itself, such as the address or whether the content has loaded, is not personal information, and I would therefore suggest that collecting information about the site status is acceptable.

**"Random" numbers**
  I have no issue with genuinely random numbers being generated on each page or the use of a timestamp. However, I would not consider it acceptable to use a number to track the user's visit trail around a website without their consent, as this would make the value little better than an IP address.

**Object tracking (e.g. using Flash or Java to track users)**
  In the vast majority of instances objects are unnecessary alternatives to other methods of tracking, such as JavaScript. Furthermore, these objects can set cookies that cannot be easily controlled by the browser. I would therefore regard the collection of information using plug-ins as unacceptable in practically all circumstances.

.. _`the subscription's policy`: https://easylist.adblockplus.org/en/policy#easyprivacy
