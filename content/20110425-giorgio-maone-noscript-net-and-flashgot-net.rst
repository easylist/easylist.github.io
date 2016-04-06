Giorgio Maone, NoScript.net and FlashGot.net
############################################

:date: 2011-04-25 18:46
:tags: EasyList, known issues
:category: Articles
:slug: 2011/04/25/giorgio-maone-noscript-net-and-flashgot-net
:authors: Michael

**Problem:**
  Some adverts are not blocked by EasyList on Giorgio Maone's add-on websites.

**Affects:**
  * http://noscript.net/
  * http://flashgot.net/

**Cause:**
  At the end of February the EasyList project were privately notified that there remained some unblocked adverts on Giorgio Maone's add-on websites which were slightly different to items usually blocked by the subscription. Instead of being an external file or text links, the images were encoded and saved in an embedded stylesheet, which meant that the only way to remove them would be to use element hiding rules to collapse the unwanted area.

  Aware that the difficulty of filtering out images encoded in this method (**data:image**), I `requested support for the format in the Adblock Plus forums`_, referring merely to "a familiar website" instead of explicitly naming the problematic domains. However, as such encoded images are not easily distinguished because they have no file name, it was decided that it might be better to wait and see whether the rules that `RUAdList`_ implemented were successful. While, under normal circumstances, filters would be added immediately, prior events (see `Wladimir's`_ and `Giorgio's`_ blogs) led the authors to concur that "we shouldn't start a cat and mouse game again".

  This issue was then pushed to the back of our minds until the topic was `publicly raised in the Adblock Plus forums`_ on the ninth of April, with a user asking Giorgio the same question that he asked us: why were adverts still present on the NoScript website? Although Hubird, the Adversity author, explained that he believed that "the NoScript developer actively makes it difficult for subscription authors to remove ads from his site (changing site design in an effort to thwart attempts)", an assertion which MonztA, an EasyList author, agreed with, Giorgio responded with the following post, which I have included in its entirety to avoid possible misinterpretation:

    @Hubird, @Montza:

    No.

    I haven't touched the "site design" for almost two years now, and I don't "actively make" anything about it.

    Those units probably difficult to remove, but because they're just static images embedded in the page itself, which don't even perform any extra round trip to my own server -- let alone a 3rd party server -- and therefore don't implement any persistent tracking / behavioral stuff.

    Of course the DOM being a bit random doesn't help either, but this picture of an evil and obsessive webmaster "actively" watching subscription authors and "changing site design in an effort to thwart attempts" is quite off base.

    -- `Giorgio Maone`_

  I and several others interpreted this statement to mean that the websites would not be changed in the event that filters were added for the domains, and I therefore committed what would be the first of many rules, reasoning that "`if a website is not actively altered I see no reason why EasyList should not filter out all the adverts`_".

  There were initially a couple of `minor`_ `changes`_ to the subscription, which were ultimately suggested to have resulted from a lack of testing on the website, as we assumed that the pages would remain static. I further proposed that the filters should be more specific to avoid false positives, a change that was implemented for both `NoScript.net`_ and `FlashGot.net`_.

  However, we then became increasingly aware that the filters were ineffective when we checked the domains, and therefore subsequently altered the rules on several occasions for both websites (the full `list of revisions for NoScript.net`_ and the `list of revisions for FlashGot.net`_ and are publicly available from `our repository`_). Although we were aware that the website was randomly altered by the server, we all agreed that certain elements of randomness, such as using alternative and altering tag names, was definitely not present when filters were first added for the domains.

  I further discovered from MonztA, an EasyList author and moderator on the Adblock Plus forums, that Giorgio posted anonymously as "Guest" on `two`_ `occasions`_ to report issues with the website, something that I consider to be unfair given that he was an involved party in the discussion. It also became apparent that a member of the community was being provided with pages that did not include adverts on Giorgio's domains, making it increasingly difficult to successfully filter the unwanted sections.

  We eventually decided, having attempted repeatedly to remove the adverts without false positives, that it would be more productive and informative to `remove the filters specifically for Giorgio's domains from EasyList`_ and explain the circumstances in a blog post. While I cannot say that this is an unexpected result given past events, I can say that I am disappointed that I could not take Giorgio at his word when he claimed that the "picture of [him as a] webmaster "actively" watching subscription authors and "changing site design in an effort to thwart attempts" is quite off base". Security depends on the people you trust, as any author of major browser extensions will be aware, and I am certainly less inclined to trust Giorgio after this incident.

**Solution:**
  There aren't really many solutions to the current state of affairs. The use of images encoded and embedded in the stylesheet means that only element hiding rules may be used to collapse the adverts, and the constant randomisation of the domains, in addition to interventions to prevent existing rules from functioning, means that any publicly announced filters are usually invalid within a few hours. Furthermore, at least one member of the advert blocking community who might have been able to assist is unable to view the adverts after his IP address was identified and alternative pages provided.

  While not an optimum solution, it would appear that the only certain method to avoid Giorgio's adverts is to cease visiting both domains entirely.

**Update: 29/05/2011**
  Ares2 claims to have found some safe filters with which do not cause false positives, and I have therefore permitted him to commit these rules to the subscription.

.. _`requested support for the format in the Adblock Plus forums`: https://adblockplus.org/forum/viewtopic.php?t=6968
.. _`RUAdList`: http://code.google.com/p/ruadlist/
.. _`Wladimir's`: https://adblockplus.org/blog/attention-noscript-users
.. _`Giorgio's`: http://hackademix.net/2009/05/04/dear-adblock-plus-and-noscript-users-dear-mozilla-community/
.. _`publicly raised in the Adblock Plus forums`: https://adblockplus.org/forum/viewtopic.php?f=1&t=7356
.. _`if a website is not actively altered I see no reason why EasyList should not filter out all the adverts`: https://adblockplus.org/forum/viewtopic.php?f=1&t=7356#p45663
.. _`minor`: https://hg.adblockplus.org/easylist/rev/6eaa4e863a4a
.. _`changes`: https://hg.adblockplus.org/easylist/rev/18aee58644f6
.. _`Giorgio Maone`: https://adblockplus.org/forum/viewtopic.php?f=1&t=7356#p45639
.. _`NoScript.net`: https://hg.adblockplus.org/easylist/rev/1035c7842ce8
.. _`FlashGot.net`: https://hg.adblockplus.org/easylist/rev/4ec885e7bf06
.. _`list of revisions for NoScript.net`: https://hg.adblockplus.org/easylist/log?rev=noscript.net
.. _`list of revisions for FlashGot.net`: https://hg.adblockplus.org/easylist/log?rev=flashgot.net
.. _`the Adblock Plus forums topic about the issue`: https://adblockplus.org/forum/viewtopic.php?f=1&t=7356
.. _`our repository`: https://hg.adblockplus.org/easylist/
.. _`two`: https://adblockplus.org/forum/viewtopic.php?t=7356&start=15#p46104
.. _`occasions`: https://adblockplus.org/forum/viewtopic.php?f=1&t=7356&start=15#p46106
.. _`remove the filters specifically for Giorgio's domains from EasyList`: https://hg.adblockplus.org/easylist/rev/73a64ca3ae82
