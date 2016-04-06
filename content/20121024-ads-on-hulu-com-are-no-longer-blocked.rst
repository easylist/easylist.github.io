Ads on hulu.com are no longer blocked
#####################################

:date: 2012-10-24 10:02
:tags: Adblock Plus, EasyList, known issues
:category: Articles
:slug: 2012/10/24/ads-on-hulu-com-are-no-longer-blocked
:authors: MonztA

**Problem:**
  Video ads on `hulu.com`_ show up before the actual video starts. 

**Affects:**
 * `hulu.com`_ 
 * any other page where Hulu videos are embedded 

**Cause:**
  Hulu videos on external sites are embedded in a HTML frame (example: `huffingtonpost.com`_). While the video ads on Hulu itself can still be blocked (a countdown shows up instead of a video ad), embedded videos on external sites will no longer play unless videa ads are allowed. This forced us to add specific whitelists for these ads. 

**Solution (Firefox only!):**
  Unfortunately, there is no way to block the ads on Hulu and allow them on external sites as the latter are embedded in a HTML frame. If you do not watch Hulu video on external sites, you can disable the whitelists and still watch videos on `hulu.com`_ without ads. Here is a step-by-step instruction how to disable them: 

1. Click on the "ABP" icon in Firefox (it is most likely in the left corner at the bottom) and choose "Filter preferences...". 
2. Click on `this button on the right`_. 
3. Click on the "Find" button that appeared on the top. 
4. Type **hulu.com/published** and disable these two exception rules **@@||hulu.com/published/*.flv** and **@@||hulu.com/published/*.mp4** by unticking them like `shown in this screenshot`_. 
5. Close the filter preferences window of Adblock Plus. 

.. _`hulu.com`: http://www.hulu.com/
.. _`huffingtonpost.com`: http://www.huffingtonpost.com/2012/10/17/jon-stewart-scoffs-at-paul-ryan-soup-kitchen_n_1973566.html
.. _`this button on the right`: https://easylist.adblockplus.org/blog-images/abp_preferences.png
.. _`shown in this screenshot`: https://easylist.adblockplus.org/blog-images/abp_preferences_2.png
