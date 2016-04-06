Affiliated subscriptions
########################

:date: 2010-10-10 10:10
:tags: Affiliated filter lists, Website
:category: Articles
:slug: 2010/10/10/affiliated-subscriptions
:authors: Michael

The new website currently lists considerably fewer external subscriptions than it once did. This is as a result of a review that I have carried of the Adblock Plus recommended subscriptions in which I was somewhat surprised to discover that several contained deprecated syntax and inefficient filters, therefore rendering them unsuitable for the homepage. The most common issues that I noticed were:

**Use of simplified element syntax**
    Simplified element syntax is delineated by the use of just one hash symbol ("#") in the rule and is currently present in Adblock Plus for reasons of `backwards compatibility only`_. It has been suggested that support for rules of this type may be removed at some point in the future, which further necessitates that affiliated subscriptions use the `more recent and efficient syntax for element hiding`_.
**Domains not clearly indicated**
    Since `the Adblock Plus 1.1 release`_ over a year ago, the beginning of a domain name may be indicated by `two vertical bars ("||")`_ and the end by the use of `a caret separator character ("^")`_. This syntax reduces the risk of false positives appearing and it is therefore highly advisable that it is implemented in filter subscriptions.
**Inefficient element hiding rules**
    I have noticed that element hiding rules are seldom implemented efficiently in existing subscriptions, which slows down the speed at which Adblock Plus may process the lists. There are two ways in which filters may be optimised: the tag name, such as "div", may be removed from filters only specifying the id ("###") or the class ("##.") and only one class, indicated by the presence of a full stop ("."), need be referenced. Therefore **example.com##div.box.advert** may have the unnecessary class removed (**example.com##div.advert**) and the tag not specified (**example.com##.advert**).
**Subscriptions contain redundant filters, either when used alone or as a supplement**
    Subscriptions should not contain multiple filters that are logically redundant, as this unnecessarily increases the size of a supplement and the complexity of maintaining it. `Famlam's redundancy checker`_ enables anyone to check lists of filters to verify that no more rules are present than need to be.
**No sections present in the subscription**
    Although not an issue that would prevent a subscription from being listed on the EasyList website, it is highly recommended that filters are sorted in a logical order with sections to delineate the purpose of particular rules. This makes the supplement far easier to both maintain and adjust, as rules may be easily found and altered.

If authors would like their filter subscription to be evaluated for the website they should check that all of the above issues are not present in their subscription and then `e-mail me`_ with a request that their list be considered. It is expected that the subscription should already be listed `on the Adblock Plus website`_, as this is the origin of all the essential data about the filter list; if not `an e-mail should be sent`_ to request that this page updated first.

.. _`backwards compatibility only`: https://adblockplus.org/en/filters#elemhide_simplified
.. _`more recent and efficient syntax for element hiding`: https://adblockplus.org/en/filters#elemhide
.. _`two vertical bars ("||")`: https://adblockplus.org/en/filters#anchors
.. _`a caret separator character ("^")`: https://adblockplus.org/en/filters#separators
.. _`Famlam's redundancy checker`: https://arestwo.org/famlam/redundantRuleChecker.html
.. _`on the Adblock Plus website`: https://adblockplus.org/en/subscriptions
.. _`e-mail me`: easylist.blog@gmail.com
.. _`an e-mail should be sent`: subscriptionlist@adblockplus.org
.. _`the Adblock Plus 1.1 release` : https://adblockplus.org/releases/adblock-plus-11-released
