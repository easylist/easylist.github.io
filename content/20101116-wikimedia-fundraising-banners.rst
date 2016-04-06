Wikimedia fundraising banners
#############################

:date: 2010-11-16 21:20
:tags: known issues, EasyList, EasyPrivacy
:category: Articles
:slug: 2010/11/16/wikimedia-fundraising-banners
:authors: Michael

There is an almost annual contention over the `Wikimedia`_ `fundraising banners`_ that appear on websites including the widely visited `Wikipedia`_ requesting donations. As it is that time of year again, it appears prudent to formally explain the position of subscriptions towards such items.

EasyList policy dictates that self promotion is not specifically blocked by the subscriptions, although such items are equally not whitelisted if they happen to be removed by general filters; as the Wikimedia banners are present to inform people about the organisation's own products, they fall into this category. Furthermore, as we actively encourage website owners to request donations from users for financial support as an alternative to placing advertisements on their domain it is hypocritical to subsequently remove them using the subscriptions.

While there have been criticisms of the banners being annoying, this is not a reason for them to be blocked by EasyList. "Annoying" is a subjective quality that is very difficult to define and therefore implement as a fair and unbiased policy.

It should be noted that EasyPrivacy blocks tracking on the domains with the filter **||bits.wikimedia.org/geoiplookup**, a rule that incidentally removes the banners. This filter is present to prevent the collection of personal data rather to fulfil than the additional purpose of removing the site notices that ultimately appears to have been served.

If you want to block the Wikimedia fundraising notice, just add the following rule to your "Custom filters" in Adblock Plus: 

**||wikimedia.org/wiki/Special:BannerLoader?$domain=wikipedia.org** 

People who want to donate money to Wikimedia should do so on `their donations page`_.

.. _Wikimedia: http://www.wikimedia.org/
.. _fundraising banners: http://meta.wikimedia.org/wiki/Fundraising_2010
.. _Wikipedia: http://www.wikipedia.org/
.. _their donations page: http://wikimediafoundation.org/wiki/Donate
