Announcing EasyAdult
####################

:date: 2011-05-30 17:30
:tags: EasyList
:category: Articles
:slug: 2011/05/30/announcing-easyadult
:authors: Michael

There has recently been considerable discussion among contributors to the EasyList project about the status of rules for adult domains in the subscription. `EasyList policy`_ has been that `filters for such websites have been excluded from the subscription`_, with users referred to `Fanboy's Adult / Dating List`_ as a supplement to the filter list. This policy resulted from two factors: adult domains were thought to require too much work to adequately filter and the belief that the subscription would be unfairly biased towards such websites, affecting user experience due to an increase in the download size and processing required. However, Ares2 has recently advanced arguments that have not only persuaded contributors that the EasyList project should filter adult domains, but that these rules should be included in the default version of EasyList.

Now that there are a lot more EasyList authors we are able to expand our website coverage without negatively affecting existing domains. Furthermore, as Ares2, MonztA, and Khrin are all keen to add rules for adult domains, there is the motivation among developers to support EasyList on adult websites. It was therefore agreed that there should be at least a supplement available with all such filters.

The reason that it was ultimately decided that rules for adult domains should be located in the default installation of EasyList is that the majority of users are simply not aware of customisation options and do not install the supplementary subscriptions that they need. While we acknowledge that many users of Adblock Plus do not visit adult domains, we believe that a large enough proportion do to warrant the default inclusion of rules for adult domains in EasyList. While there are likely to be a lot of filters for adult domains, the actual effect that the additional rules will have on subscription performance is negligible due to optimisations in Adblock Plus.

The authors responsible for the EasyAdult section (Ares2, MonztA and Khrin) have therefore started to add filters to the repository; this section is `now included in the default installation of EasyList`_. Any tracking items found on adult domains will be added to EasyPrivacy, although it is not anticipated that there many specific services will be discovered. However, EasyAdult is far from finished, and we would therefore welcome contributions in the `filter suggestions`_ and `false positive reports`_ forums, preferably with an indication that the referenced domain contains adult content.

Users who would prefer not to have filters for adult domains may `install`_ the variant "`EasyList without adult filters`_" from the homepage.

.. _`EasyList policy`: https://easylist.adblockplus.org/en/policy#easylist
.. _`filters for such websites have been excluded from the subscription`: https://easylist.adblockplus.org/blog/2010/12/12/an-important-reminder-about-adult-websites
.. _`Fanboy's Adult / Dating List`: https://fanboy.co.nz/
.. _`now included in the default installation of EasyList`: https://hg.adblockplus.org/easylist/rev/7bf4ac3950f5
.. _`false positive reports`: http://forums.lanik.us/viewforum.php?f=62
.. _`filter suggestions`: http://forums.lanik.us/viewforum.php?f=64
.. _`install`: abp://subscribe?location=https://easylist-downloads.adblockplus.org/easylist_noadult.txt&title=EasyList%20without%20rules%20for%20adult%20sites
.. _`EasyList without adult filters`: https://easylist-downloads.adblockplus.org/easylist_noadult.txt
.. _`homepage`: https://easylist.adblockplus.org/en/#easylistnoadult
