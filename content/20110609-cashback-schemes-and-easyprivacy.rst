Cashback schemes and EasyPrivacy
################################

:date: 2011-06-09 18:35
:tags: EasyPrivacy, known issues
:category: Articles
:slug: 2011/06/09/cashback-schemes-and-easyprivacy
:authors: Michael

**Problem:**
 Some cashback systems do not function correctly when EasyPrivacy is enabled.

**Affects:**
  * http://www.extrarebates.com/ (`view report`_)
  * Other cashback systems are also likely to be affected and will be listed as they are reported.


**Cause:**
  Cashback websites work by either setting a third party cookie or directing people to a special address to inform the shopping website that the user is eligible for a discount. Shopping websites then need to be able to view the information to identify the user and reduce the item cost if applicable. However, EasyPrivacy is designed to prevent such details being collected; the shopping website therefore lacks the information to suggest that a special offer should be applied and charges to full price instead of the discounted rate.

**Solution:**
  I have `previously recommended`_, and would still advocate, that Adblock Plus should be disabled on important websites and when shopping. This will ensure that subscriptions do not interfere with the purchasing of goods and will therefore prevent issues from arising with cashback schemes. However, regardless of whether or not advert blocking software is installed, I would always recommend that you confirm the price of an item before paying.

.. _`view report`: https://forums.lanik.us/viewtopic.php?t=8502
.. _`previously recommended`: https://easylist.adblockplus.org/blog/2010/10/29/filter-subscriptions-and-important-internet-transactions
