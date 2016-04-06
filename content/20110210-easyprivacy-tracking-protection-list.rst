EasyPrivacy Tracking Protection List
####################################

:date: 2011-02-10 17:00
:tags: EasyPrivacy, Tracking Protection Lists
:category: Articles
:slug: 2011/02/10/easyprivacy-tracking-protection-list
:authors: Michael

EasyPrivacy is a comparatively recent subscription in the context of the EasyList project, but it is one that has garnered significant interest recently due to current privacy concerns, which this list of filters was written to address. Yet I had never suspected the possibility of repurposing the subscription not only for a different browser, but also for an entirely different filter processing engine.

However, this opportunity presented itself when `Microsoft`_ recently announced `Tracking Protection Lists`_ for `Internet Explorer 9`_. After some discussion with Microsoft just over a month ago we found that we were able to automatically convert the majority of EasyPrivacy filters to a suitable form for Internet Explorer, and a script has therefore been uploaded to our host server to automate this process every ten minutes. This new subscription variant has been entitled EasyPrivacy Tracking Protection List or, in its abbreviated form, `EasyPrivacy TPL`_, and may be `installed from Microsoft's Tracking Protection List page`_.

Furthermore, the script that generates the EasyList subscriptions has been updated to include the conversion process from Adblock Plus to Tracking Protection List format and these changes have been `committed`_ to `the repository`_, from where `combineSubscriptions.py`_ may be downloaded and used for the automatic conversion of other subscriptions.

I would therefore encourage anyone interested in using the subscription to install the release candidate version of `Internet Explorer 9`_, a browser that appears to have been significantly improved since the last release, and install `EasyPrivacy Tracking Protection List`_, which is now `listed on the homepage`_. Any `suggestions`_ or `false positives`_ should be reported in the respective sections of `the EasyList forums`_, which does not require registration in order to post.

.. _`Microsoft`: http://www.microsoft.com/
.. _`Tracking Protection Lists`: http://blogs.msdn.com/b/ie/archive/2010/12/07/ie9-and-privacy-introducing-tracking-protection-v8.aspx
.. _`EasyPrivacy TPL`: http://easylist-msie.adblockplus.org/easyprivacy.tpl
.. _`installed from Microsoft's Tracking Protection List page`: http://ie.microsoft.com/testdrive/Browser/TrackingProtectionLists/Default.html
.. _`committed`: https://hg.adblockplus.org/easylistcombinations/rev/50f21baafda3
.. _`the repository`: https://hg.adblockplus.org/easylistcombinations
.. _`combineSubscriptions.py`: https://hg.adblockplus.org/easylistcombinations/file/tip/combineSubscriptions.py
.. _`Internet Explorer 9`: http://www.beautyoftheweb.com/
.. _`EasyPrivacy Tracking Protection List`: http://easylist-msie.adblockplus.org/easyprivacy.tpl
.. _`listed on the homepage`: https://easylist.adblockplus.org/#easyprivacytpl
.. _`suggestions`: http://forums.lanik.us/viewforum.php?f=62
.. _`false positives`: http://forums.lanik.us/viewforum.php?f=64
.. _`the EasyList forums`: http://forums.lanik.us/
